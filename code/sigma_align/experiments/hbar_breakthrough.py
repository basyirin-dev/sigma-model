"""Breakthrough Experiment Harness for Compositional Generalization Dynamics.

Supports:
1. Long-run grokking tests (50,000 to 100,000 steps with weight decay options).
2. Equal-cumulative-exposure timing discrimination matrix:
   - constant_low: lambda = 0.2 throughout (total = 400)
   - early_burst: lambda = 1.0 for steps 0-400, then 0.0 (total = 400)
   - late_burst: lambda = 0.0 for steps 0-1600, then 1.0 for steps 1600-2000 (total = 400)
   - pulsed: lambda = 1.0 every 5th step (total = 400)
"""

from __future__ import annotations

from typing import Any

import numpy as np
import torch
import torch.nn as nn
from torch.amp.autocast_mode import autocast
from torch.amp.grad_scaler import GradScaler
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

from sigma_align.experiments.hbar_model import HBarTransformer
from sigma_align.experiments.hbar_train import _stack_batch, fast_evaluate
from sigma_align.monitoring.proxy import (
    RGA_OPERATORS,
    compute_gca,
    compute_rga,
    compute_sigma_tilde,
)


def train_breakthrough_model(
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
    """Train one run under a breakthrough condition configuration."""
    cond_cfg: dict[str, Any] = dict(cfg["conditions"][condition])
    train_cfg: dict[str, Any] = cfg["training"]
    proxy_cfg: dict[str, Any] = cfg.get("proxy", {})
    model_cfg: dict[str, Any] = cfg["model"]

    n_timesteps = n_timesteps or int(train_cfg["n_timesteps"])
    eval_every = eval_every or int(train_cfg["eval_every"])
    lr = lr if lr is not None else float(train_cfg["lr"])
    eval_max_batches = int(train_cfg.get("eval_max_batches", 8))
    grad_clip = float(train_cfg.get("gradient_clip_norm", 1.0))
    weight_decay = float(cond_cfg.get("weight_decay", 0.0))

    print(f"\n{'=' * 60}")
    print(f"Run #{run_id:02d}: {condition.upper()} | steps={n_timesteps} | wd={weight_decay}")
    print(f"{'=' * 60}")

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

    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    criterion = nn.CrossEntropyLoss(ignore_index=0)
    scaler = GradScaler("cuda", enabled=use_amp)

    metrics: dict[str, list[float]] = {
        "step": [],
        "loss": [],
        "acc_id": [],
        "acc_ood": [],
        "effective_comp_weight": [],
        "sigma_tilde": [],
        "gca": [],
        "rga": [],
        "param_norm": [],
    }

    # Timing / exposure configuration
    mode = cond_cfg.get("mode", "baseline")
    comp_weight = float(cond_cfg.get("comp_weight", 0.0))
    comp_every = int(cond_cfg.get("comp_every", 1))
    start_step = int(cond_cfg.get("start_step", 0))
    end_step = int(cond_cfg.get("end_step", n_timesteps))

    has_comp = comp_weight > 0.0 or mode in ["constant", "window", "pulsed"]
    comp_iter = iter(loaders["comp"]) if has_comp else None

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

        optimizer.zero_grad(set_to_none=True)

        with autocast("cuda", enabled=use_amp):
            out = model(src, tgt_input)
            task_loss = criterion(out.reshape(-1, out.size(-1)), tgt_target.reshape(-1))

        # Determine current effective compositional weight
        curr_comp_weight = 0.0
        if mode == "constant":
            if global_step % comp_every == 0:
                curr_comp_weight = comp_weight
        elif mode == "window":
            if start_step <= global_step < end_step and global_step % comp_every == 0:
                curr_comp_weight = comp_weight
        elif mode == "pulsed":
            if global_step % comp_every == 0:
                curr_comp_weight = comp_weight

        total_loss = task_loss
        if curr_comp_weight > 0.0 and comp_iter is not None:
            try:
                c_src, c_tgt = next(comp_iter)
            except StopIteration:
                comp_iter = iter(loaders["comp"])
                c_src, c_tgt = next(comp_iter)

            c_src, c_tgt = c_src.to(device), c_tgt.to(device)
            with autocast("cuda", enabled=use_amp):
                c_out = model(c_src, c_tgt[:, :-1])
                c_loss = criterion(c_out.reshape(-1, c_out.size(-1)), c_tgt[:, 1:].reshape(-1))
            total_loss = total_loss + curr_comp_weight * c_loss

        scaler.scale(total_loss).backward()
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
        scaler.step(optimizer)
        scaler.update()

        # Evaluate at checkpoints
        if global_step % eval_every == 0 or global_step == n_timesteps - 1:
            acc_id = fast_evaluate(
                model, loaders["id"], device, use_amp, max_batches=eval_max_batches
            )
            acc_ood = fast_evaluate(
                model, loaders["ood"], device, use_amp, max_batches=eval_max_batches
            )

            # Compute proxy metrics
            gca = compute_gca(model, train_probe, comp_probe, criterion, device, use_amp)
            rga = compute_rga(
                model,
                rga_sample,
                loaders["train"].dataset.vocab,
                device,
                use_amp,
                operators=tuple(proxy_cfg.get("rga_operators") or RGA_OPERATORS),
                n_pairs=int(proxy_cfg.get("rga_n_pairs", 2000)),
                seed=run_id,
            )
            sigma_tilde = compute_sigma_tilde(
                gca,
                rga,
                fuse_gca=float(proxy_cfg.get("fuse_gca", 0.5)),
                fuse_rga=float(proxy_cfg.get("fuse_rga", 0.5)),
            )

            param_norm = float(
                torch.sqrt(sum((p**2).sum() for p in model.parameters() if p.requires_grad)).item()
            )

            metrics["step"].append(global_step)
            metrics["loss"].append(float(task_loss.item()))
            metrics["acc_id"].append(acc_id)
            metrics["acc_ood"].append(acc_ood)
            metrics["effective_comp_weight"].append(curr_comp_weight)
            metrics["sigma_tilde"].append(sigma_tilde)
            metrics["gca"].append(gca)
            metrics["rga"].append(rga)
            metrics["param_norm"].append(param_norm)

            pbar.set_postfix({
                "loss": f"{task_loss.item():.3f}",
                "ID": f"{acc_id:.1f}%",
                "OOD": f"{acc_ood:.1f}%",
                "RGA": f"{rga:.3f}",
            })

        global_step += 1
        pbar.update(1)

    pbar.close()
    return metrics
