"""H-Bar training harness for the Phase 04 mechanism gate.

Ported from the archived pilot notebook (cells 3–5) with the training dynamics
kept verbatim for parity, plus two additions:

- ``fixed_weight`` arm: constant-weight compositional loss every ``comp_every``
  steps, no σ modulation, no phase-gated curriculum (the discriminating control);
  σ is tracked as a diagnostic only.
- measured Stage-1 proxy (GCA + RGA, see ``monitoring.proxy``) recorded at every
  eval point as ``metrics["sigma_tilde"]``; the scheduled knob is kept alongside
  as ``metrics["sigma_sched"]`` for comparison diagnostics.
"""

from __future__ import annotations

import os
import pickle
from typing import Any

import numpy as np
import torch
import torch.nn as nn
from torch.amp.autocast_mode import autocast
from torch.amp.grad_scaler import GradScaler
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

from sigma_align.experiments.hbar_model import HBarTransformer
from sigma_align.monitoring.proxy import (
    RGA_OPERATORS,
    compute_gca,
    compute_rga,
    compute_sigma_tilde,
)

# Curriculum constants (mirror the archived pilot cell 4).
SIGMA_CRITICAL = 0.15
DELTA_STAR = 0.55
SIGMA_DRIFT_STEP = 3e-4  # baseline σ drift per step
SIGMA_ADD_STEP = 2.5e-4  # additive σ slope per step
GOMPERTZ_A = -4.0
GOMPERTZ_B = -3e-3
GOMPERTZ_AMP = 0.85
NOISE_STD = 0.012
DELTA_REL_START = 0.05
DELTA_REL_SLOPE = 0.90
PHASE_LR_BOOST = 0.2
COMP_INJECT_WEIGHT = 0.3  # λ_σ · (1 − σ̃) in the phase-2 injection


def _stack_batch(
    items: list[tuple[torch.Tensor, torch.Tensor]],
) -> tuple[torch.Tensor, torch.Tensor]:
    """Collate dataset items (already padded to max_len) into a batch."""
    return torch.stack([s for s, _ in items]), torch.stack([t for _, t in items])


def fast_evaluate(
    model: nn.Module,
    loader: DataLoader,
    device: torch.device,
    use_amp: bool,
    max_batches: int = 8,
) -> float:
    """Quick accuracy estimate on the first ``max_batches`` batches (pilot cell 4)."""
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


def evaluate_model(
    model: nn.Module,
    id_loader: DataLoader | None,
    ood_loader: DataLoader | None,
    device: torch.device,
    use_amp: bool,
) -> dict[str, float]:
    """Full evaluation on the complete ID/OOD datasets (once per run)."""
    model.eval()
    res: dict[str, float] = {}
    for tag, loader in [("acc_id", id_loader), ("acc_ood", ood_loader)]:
        if loader is None:
            res[tag] = 0.0
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
        res[tag] = 100.0 * correct / total if total > 0 else 0.0
    model.train()
    return res


def train_hbar_model(
    condition: str,
    run_id: int,
    cfg: dict[str, Any],
    loaders: dict[str, DataLoader],
    device: torch.device,
    use_amp: bool,
    n_timesteps: int | None = None,
    eval_every: int | None = None,
    lr: float | None = None,
    save_checkpoints: bool = False,
    checkpoint_dir: str | None = None,
) -> dict[str, Any]:
    """Train one H-Bar run under ``condition``; returns the per-run metrics dict.

    Seed discipline (CC.2.1): ``torch.manual_seed(run_id * 42 + 7)`` and the same
    for numpy — identical to the archived pilot.
    """
    cond_cfg: dict[str, Any] = dict(cfg["conditions"][condition])
    train_cfg: dict[str, Any] = cfg["training"]
    proxy_cfg: dict[str, Any] = cfg["proxy"]
    model_cfg: dict[str, Any] = cfg["model"]

    n_timesteps = n_timesteps or int(train_cfg["n_timesteps"])
    eval_every = eval_every or int(train_cfg["eval_every"])
    lr = lr if lr is not None else float(train_cfg["lr"])
    eval_max_batches = int(train_cfg.get("eval_max_batches", 8))
    grad_clip = float(train_cfg.get("gradient_clip_norm", 1.0))

    print(f"\n{'=' * 55}")
    print(f"Run #{run_id:02d}: {condition.upper()}  steps={n_timesteps}")
    print(f"{'=' * 55}")

    torch.manual_seed(run_id * 42 + 7)
    np.random.seed(run_id * 42 + 7)

    model = HBarTransformer(
        vocab_size=len(loaders["train"].dataset.vocab),
        d_model=int(model_cfg["d_model"]),
        nhead=int(model_cfg["nhead"]),
        num_layers=int(model_cfg["num_layers"]),
        dim_ff=int(model_cfg["dim_ff"]),
        dropout=float(model_cfg["dropout"]),
        pad_idx=int(model_cfg["pad_idx"]),
    ).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss(ignore_index=0)
    scaler = GradScaler("cuda", enabled=use_amp)

    metrics: dict[str, list[float]] = {
        "step": [],
        "loss": [],
        "acc_id": [],
        "acc_ood": [],
        "sigma_tilde": [],
        "gca": [],
        "rga": [],
        "sigma_sched": [],
        "phase": [],
        "lr_eff": [],
        "param_norm": [],
    }

    # Condition hyper-params (mirror pilot cell 4).
    use_curriculum = bool(cond_cfg.get("use_curriculum", False))
    coupling_mode = cond_cfg.get("coupling_mode")
    coupling_str = float(cond_cfg.get("coupling_str", 0.0))
    sigma_init = float(cond_cfg.get("sigma_init", 0.10))
    comp_weight = float(cond_cfg.get("comp_weight", COMP_INJECT_WEIGHT))
    comp_every = int(cond_cfg.get("comp_every", 5))

    ode = {"sigma": sigma_init, "delta_rel": DELTA_REL_START, "phase": 0}
    comp_iter = iter(loaders["comp"]) if (use_curriculum or condition == "fixed_weight") else None

    # Fixed probe batches for the measured proxy. Drawn as fixed index slices of
    # the datasets (NOT via DataLoader iteration) so they consume no torch/np RNG
    # and the training batch stream stays bit-identical to the archived pilot.
    train_ds = loaders["train"].dataset
    comp_ds = loaders["comp"].dataset
    batch_size = int(train_cfg["batch_size"])
    train_probe = _stack_batch([train_ds[i] for i in range(min(batch_size, len(train_ds)))])
    comp_probe = _stack_batch([comp_ds[i] for i in range(min(batch_size, len(comp_ds)))])
    rga_n = int(proxy_cfg.get("rga_n_examples", 256))
    rga_sample = [comp_ds[i] for i in range(min(rga_n, len(comp_ds)))]

    data_iter = iter(loaders["train"])
    global_step = 0
    pbar = tqdm(total=n_timesteps, desc=f"[{condition}] run{run_id:02d}")

    while global_step < n_timesteps:
        try:
            src, tgt = next(data_iter)
        except StopIteration:
            data_iter = iter(loaders["train"])
            src, tgt = next(data_iter)

        src, tgt = src.to(device), tgt.to(device)
        tgt_input = tgt[:, :-1]
        tgt_target = tgt[:, 1:]
        step_ratio = global_step / n_timesteps
        effective_lr = lr

        optimizer.zero_grad(set_to_none=True)

        # Main forward.
        with autocast("cuda", enabled=use_amp):
            out = model(src, tgt_input)
            task_loss = criterion(out.reshape(-1, out.size(-1)), tgt_target.reshape(-1))

        # σ_A scheduled dynamics (pure numpy, outside autocast — pilot cell 4).
        noise = np.random.normal(0, NOISE_STD)

        if use_curriculum:
            if coupling_mode == "additive":
                # Linear growth: 0.05 → ~0.55 by step 2000 (no saturation).
                ode["sigma"] = float(
                    np.clip(sigma_init + SIGMA_ADD_STEP * global_step + noise, 0.0, 1.0)
                )
            elif coupling_mode == "multiplicative":
                # Gompertz: starts LOW ~0.07, fast rise, saturates ~0.89.
                gompertz = float(np.exp(GOMPERTZ_A * np.exp(GOMPERTZ_B * global_step)))
                ode["sigma"] = float(
                    np.clip(sigma_init + GOMPERTZ_AMP * gompertz + noise, 0.0, 1.0)
                )

            ode["delta_rel"] = min(1.0, DELTA_REL_START + DELTA_REL_SLOPE * step_ratio)

            if ode["sigma"] > SIGMA_CRITICAL and ode["phase"] < 2:
                pbar.write(f"  Phase 0->2 at step {global_step} (sigma={ode['sigma']:.3f})")
                ode["phase"] = 2
            if ode["delta_rel"] > DELTA_STAR and ode["phase"] < 3:
                ode["phase"] = 3

            # LR boost only in Phase 2+ (small coefficient, no instability).
            if ode["phase"] >= 2:
                effective_lr = lr * (1.0 + PHASE_LR_BOOST * ode["sigma"])
                for pg in optimizer.param_groups:
                    pg["lr"] = effective_lr
        else:
            # baseline / fixed_weight: σ drifts slowly, no curriculum (diagnostic only).
            ode["sigma"] = float(
                np.clip(sigma_init + SIGMA_DRIFT_STEP * global_step + noise, 0.0, 1.0)
            )

        # Build total loss.
        total_loss = task_loss

        if use_curriculum:
            if coupling_mode == "additive":
                # Penalty high when σ is LOW (early): drives compositional learning.
                total_loss = task_loss * (1.0 + coupling_str * (1.0 - ode["sigma"]))
            elif coupling_mode == "multiplicative":
                # Amplifies signal when σ is HIGH (late): precision refinement.
                total_loss = task_loss * (1.0 + coupling_str * ode["sigma"])

            # Phase 2+ curriculum injection: every 5 steps once Phase 2 is active.
            if ode["phase"] >= 2 and comp_iter is not None and global_step % 5 == 0:
                try:
                    c_src, c_tgt = next(comp_iter)
                except StopIteration:
                    comp_iter = iter(loaders["comp"])
                    c_src, c_tgt = next(comp_iter)

                c_src, c_tgt = c_src.to(device), c_tgt.to(device)
                with autocast("cuda", enabled=use_amp):
                    c_out = model(c_src, c_tgt[:, :-1])
                    c_loss = criterion(c_out.reshape(-1, c_out.size(-1)), c_tgt[:, 1:].reshape(-1))
                # L_total += λ_σ · (1 − σ̃) · L_comp  (low σ → high comp weight).
                total_loss = total_loss + COMP_INJECT_WEIGHT * (1.0 - ode["sigma"]) * c_loss

        elif condition == "fixed_weight":
            # Discriminating control: constant-weight compositional loss every
            # `comp_every` steps, no σ modulation, no phase gate.
            if comp_iter is not None and global_step % comp_every == 0:
                try:
                    c_src, c_tgt = next(comp_iter)
                except StopIteration:
                    comp_iter = iter(loaders["comp"])
                    c_src, c_tgt = next(comp_iter)

                c_src, c_tgt = c_src.to(device), c_tgt.to(device)
                with autocast("cuda", enabled=use_amp):
                    c_out = model(c_src, c_tgt[:, :-1])
                    c_loss = criterion(c_out.reshape(-1, c_out.size(-1)), c_tgt[:, 1:].reshape(-1))
                total_loss = total_loss + comp_weight * c_loss

        # Backward.
        scaler.scale(total_loss).backward()
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
        scaler.step(optimizer)
        scaler.update()

        # Fast-eval checkpoint + measured proxy.
        if global_step % eval_every == 0:
            acc_id = fast_evaluate(
                model, loaders["id"], device, use_amp, max_batches=eval_max_batches
            )
            acc_ood = fast_evaluate(
                model, loaders["ood"], device, use_amp, max_batches=eval_max_batches
            )
            gca = compute_gca(model, train_probe, comp_probe, criterion, device, use_amp)
            rga = compute_rga(
                model,
                rga_sample,
                loaders["train"].dataset.vocab,
                device,
                use_amp,
                operators=tuple(proxy_cfg.get("rga_operators") or RGA_OPERATORS),
                n_pairs=int(proxy_cfg.get("rga_n_pairs", 5000)),
                seed=run_id,
            )
            sigma_tilde = compute_sigma_tilde(
                gca,
                rga,
                fuse_gca=float(proxy_cfg.get("fuse_gca", 0.5)),
                fuse_rga=float(proxy_cfg.get("fuse_rga", 0.5)),
            )
            metrics["step"].append(global_step)
            metrics["loss"].append(task_loss.item())
            metrics["acc_id"].append(acc_id)
            metrics["acc_ood"].append(acc_ood)
            metrics["sigma_tilde"].append(sigma_tilde)
            metrics["gca"].append(gca)
            metrics["rga"].append(rga)
            metrics["sigma_sched"].append(ode["sigma"])
            metrics["phase"].append(ode["phase"])
            metrics["lr_eff"].append(effective_lr)
            metrics["param_norm"].append(
                float(sum(p.pow(2).sum().item() for p in model.parameters()) ** 0.5)
            )
            pbar.set_postfix(
                {
                    "loss": f"{task_loss.item():.3f}",
                    "id": f"{acc_id:.1f}",
                    "ood": f"{acc_ood:.1f}",
                    "sig": f"{sigma_tilde:.2f}",
                    "P": ode["phase"],
                }
            )

        if save_checkpoints and global_step % 500 == 0 and global_step > 0 and checkpoint_dir:
            torch.save(
                {"step": global_step, "ode": ode, "state": model.state_dict()},
                f"{checkpoint_dir}/{condition}_run{run_id}_s{global_step}.pt",
            )

        global_step += 1
        pbar.update(1)

    pbar.close()

    # Full final evaluation (written into metrics['final'] for analysis).
    final_ev = evaluate_model(model, loaders["id"], loaders["ood"], device, use_amp)
    metrics["final"] = final_ev

    print(
        f"Done: ID={final_ev['acc_id']:.1f}%  OOD={final_ev['acc_ood']:.1f}%  "
        f"sigma_tilde_final={metrics['sigma_tilde'][-1]:.3f}  phase={ode['phase']}"
    )

    del model
    if device.type == "cuda":
        torch.cuda.empty_cache()
    return metrics


def persist_run(
    metrics: dict[str, Any],
    condition: str,
    run_id: int,
    n_timesteps: int,
    outdir: str,
) -> str:
    """Write the per-run pkl (pilot schema: ``{'metrics': ..., 'config': ...}``)."""
    os.makedirs(outdir, exist_ok=True)
    path = f"{outdir}/{condition}_run{run_id}.pkl"
    with open(path, "wb") as f:
        pickle.dump(
            {
                "metrics": metrics,
                "config": {
                    "condition": condition,
                    "run_id": run_id,
                    "n_timesteps": n_timesteps,
                },
            },
            f,
        )
    return path
