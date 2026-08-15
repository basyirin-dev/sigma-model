import logging
import pickle
import sys

import numpy as np
import torch
import torch.nn as nn
from torch.amp.autocast_mode import autocast
from torch.amp.grad_scaler import GradScaler
from tqdm.auto import tqdm

from sigma.models.transformer import SigmaTransformer
from sigma.ode.solver import SigmaODESolver

logger = logging.getLogger(__name__)


def fast_evaluate(model, loader, device, use_amp: bool = False, max_batches: int = 8) -> float:
    """Fast approximate evaluation over a subset of batches.

    Maps to: Section 3.5 and Algorithm 3.2 in manuscript.tex.
    Uses at most max_batches to reduce evaluation overhead during training.
    Reports token-level accuracy ignoring padding (index 0).

    Args:
        model: PyTorch model (SigmaTransformer).
        loader: DataLoader yielding (src, tgt) tuples.
        device: Torch device string.
        use_amp: Enable automatic mixed precision.
        max_batches: Maximum number of batches to evaluate.

    Returns:
        Token-level accuracy in percent (0-100).
    """
    model.eval()
    correct = total = 0
    with torch.inference_mode():
        for i, (src, tgt) in enumerate(loader):
            if i >= max_batches:
                break
            src, tgt = src.to(device), tgt.to(device)
            with autocast("cuda", enabled=use_amp):
                out = model(src, tgt[:, :-1])
            preds = out.argmax(dim=-1)
            mask = tgt[:, 1:] != 0
            correct += ((preds == tgt[:, 1:]) & mask).sum().item()
            total += mask.sum().item()
    model.train()
    return 100.0 * correct / total if total > 0 else 0.0


def evaluate_model(model, id_loader, ood_loader, device, use_amp: bool = False) -> dict:
    """Full evaluation on ID and OOD test loaders.

    Maps to: Section 10.1 and Table 3 in manuscript.tex.
    Reports token-level accuracy on both in-distribution and
    out-of-distribution splits, used for compositional gap analysis.

    Args:
        model: PyTorch model (SigmaTransformer).
        id_loader: In-distribution test DataLoader.
        ood_loader: Out-of-distribution test DataLoader.
        device: Torch device string.
        use_amp: Enable automatic mixed precision.

    Returns:
        dict with keys "acc_id" and "acc_ood" (percent, 0-100).
    """
    model.eval()
    results = {}
    for tag, loader in [("acc_id", id_loader), ("acc_ood", ood_loader)]:
        if loader is None:
            results[tag] = 0.0
            continue
        correct = total = 0
        with torch.inference_mode():
            for src, tgt in loader:
                src, tgt = src.to(device), tgt.to(device)
                with autocast("cuda", enabled=use_amp):
                    out = model(src, tgt[:, :-1])
                preds = out.argmax(dim=-1)
                mask = tgt[:, 1:] != 0
                correct += ((preds == tgt[:, 1:]) & mask).sum().item()
                total += mask.sum().item()
        results[tag] = 100.0 * correct / total if total > 0 else 0.0
    model.train()
    return results


def train_sigma_model(
    condition: str = "baseline",
    run_id: int = 0,
    n_timesteps: int = 2000,
    eval_every: int = 50,
    lr: float = 0.001,
    lambda_sigma: float = 0.3,
    train_loader=None,
    test_loader=None,
    ood_loader=None,
    comp_loader=None,
    device: str = "cpu",
    use_amp: bool = False,
    checkpoint_dir: str | None = None,
    result_dir: str | None = None,
    vocab_size: int | None = None,
):
    """Run one complete Σ-Model training experiment for a given condition.

    Maps to: Algorithm 3.2 and Section 10.1 in manuscript.tex;
    lambda_sigma maps to Eq 25 (schema-targeting loss weight).
    Orchestrates model creation, ODE step, curriculum loss modulation,
    evaluation, checkpointing, and result serialisation.

    VRAM complexity: The simplified ODE solver is pure NumPy (naturally
    detached from autograd), uses a single backward pass per step with
    no retain_graph or create_graph. No RDM storage or dual-gradient
    computation is performed. Total VRAM is O(batch_size * d_model *
    num_layers), identical to standard transformer training.

    Args:
        condition: One of "baseline" (standard SGD), "additive", or
            "multiplicative" (sigma-targeting curriculum).
        run_id: Unique run index for seeding and file naming.
        n_timesteps: Total training steps.
        eval_every: Evaluate every N steps.
        lr: Base learning rate.
        lambda_sigma: Weight for schema-targeting compositional loss
            (lambda_sigma in Eq 25). Default 0.3.
        train_loader: Training data DataLoader.
        test_loader: In-distribution test DataLoader.
        ood_loader: Out-of-distribution test DataLoader.
        comp_loader: Compositional probe DataLoader (used in Phase 2+).
        device: Torch device string ("cpu" or "cuda").
        use_amp: Enable automatic mixed precision.
        checkpoint_dir: If set, save model checkpoints every 500 steps.
        result_dir: If set, save final metrics pickle.

    Returns:
        dict: Training metrics including step-wise loss, acc_id, acc_ood,
            sigma_tilde, phase, lr_eff, and a "final" key with final
            evaluation results.
    """
    logger.info(
        "Python %s | PyTorch %s | CUDA %s | GPU %s",
        sys.version.split()[0],
        torch.__version__,
        torch.version.cuda or "none",
        torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
    )

    torch.manual_seed(run_id * 42 + 7)
    np.random.seed(run_id * 42 + 7)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(run_id * 42 + 7)
        torch.backends.cudnn.deterministic = True

    model = SigmaTransformer(vocab_size=vocab_size or 50).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss(ignore_index=0)
    scaler = GradScaler("cuda", enabled=use_amp)

    metrics = {
        "step": [],
        "loss": [],
        "acc_id": [],
        "acc_ood": [],
        "sigma_tilde": [],
        "phase": [],
        "lr_eff": [],
    }

    sigma_critical_val = 0.15
    delta_star_val = 0.55

    if condition == "baseline":
        use_curriculum = False
        coupling_mode = None
        coupling_str = 0.0
        sigma_init_value = 0.10
    elif condition == "additive":
        use_curriculum = True
        coupling_mode = "additive"
        coupling_str = 0.20
        sigma_init_value = 0.05
    else:
        use_curriculum = True
        coupling_mode = "multiplicative"
        coupling_str = 0.20
        sigma_init_value = 0.05

    ode_solver = SigmaODESolver(sigma_init=sigma_init_value)
    comp_iter = iter(comp_loader) if (use_curriculum and comp_loader) else None

    data_iter = iter(train_loader)
    global_step = 0
    pbar = tqdm(total=n_timesteps, desc=f"[{condition}] run{run_id:02d}")

    while global_step < n_timesteps:
        try:
            src, tgt = next(data_iter)
        except StopIteration:
            data_iter = iter(train_loader)
            src, tgt = next(data_iter)

        src, tgt = src.to(device), tgt.to(device)
        tgt_input = tgt[:, :-1]
        tgt_target = tgt[:, 1:]
        effective_lr = lr

        optimizer.zero_grad(set_to_none=True)

        with autocast("cuda", enabled=use_amp):
            out = model(src, tgt_input)
            task_loss = criterion(out.reshape(-1, out.size(-1)), tgt_target.reshape(-1))

        ode_state = ode_solver.step(
            global_step, n_timesteps, sigma_critical_val, delta_star_val,
            coupling_mode=coupling_mode, coupling_str=coupling_str,
            sigma_init=sigma_init_value,
        )

        if use_curriculum and ode_state["phase"] >= 2:
            effective_lr = lr * (1.0 + 0.2 * ode_state["sigma"])
            for pg in optimizer.param_groups:
                pg["lr"] = effective_lr

        total_loss = task_loss
        if use_curriculum:
            if coupling_mode == "additive":
                total_loss = task_loss * (1.0 + coupling_str * (1.0 - ode_state["sigma"]))
            elif coupling_mode == "multiplicative":
                total_loss = task_loss * (1.0 + coupling_str * ode_state["sigma"])

            if ode_state["phase"] >= 2 and comp_iter is not None and global_step % 5 == 0:
                try:
                    c_src, c_tgt = next(comp_iter)
                except StopIteration:
                    comp_iter = iter(comp_loader)
                    c_src, c_tgt = next(comp_iter)
                c_src, c_tgt = c_src.to(device), c_tgt.to(device)
                with autocast("cuda", enabled=use_amp):
                    c_out = model(c_src, c_tgt[:, :-1])
                    c_loss = criterion(c_out.reshape(-1, c_out.size(-1)), c_tgt[:, 1:].reshape(-1))
                total_loss = total_loss + lambda_sigma * (1.0 - ode_state["sigma"]) * c_loss

        scaler.scale(total_loss).backward()
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        scaler.step(optimizer)
        scaler.update()

        if global_step % eval_every == 0:
            acc_id = fast_evaluate(model, test_loader, device, use_amp, max_batches=8)
            acc_ood = fast_evaluate(model, ood_loader, device, use_amp, max_batches=8)
            metrics["step"].append(global_step)
            metrics["loss"].append(task_loss.item())
            metrics["acc_id"].append(acc_id)
            metrics["acc_ood"].append(acc_ood)
            metrics["sigma_tilde"].append(ode_state["sigma"])
            metrics["phase"].append(ode_state["phase"])
            metrics["lr_eff"].append(effective_lr)
            pbar.set_postfix({
                "loss": f"{task_loss.item():.3f}",
                "id": f"{acc_id:.1f}",
                "ood": f"{acc_ood:.1f}",
                "sigma": f"{ode_state['sigma']:.2f}",
                "P": ode_state["phase"],
            })

        if checkpoint_dir and global_step % 500 == 0 and global_step > 0:
            torch.save(
                {"step": global_step, "ode": ode_state, "state": model.state_dict()},
                f"{checkpoint_dir}/{condition}_run{run_id}_s{global_step}.pt",
            )

        global_step += 1
        pbar.update(1)

    pbar.close()

    final_ev = evaluate_model(model, test_loader, ood_loader, device, use_amp)
    metrics["final"] = final_ev

    if result_dir:
        with open(f"{result_dir}/{condition}_run{run_id}.pkl", "wb") as f:
            pickle.dump(
                {
                    "metrics": metrics,
                    "config": {
                        "condition": condition,
                        "run_id": run_id,
                        "n_timesteps": n_timesteps,
                    },
                    "seed": run_id * 42 + 7,
                    "seed_formula": "run_id * 42 + 7",
                },
                f,
            )

    del model
    if "cuda" in device:
        torch.cuda.empty_cache()
    return metrics
