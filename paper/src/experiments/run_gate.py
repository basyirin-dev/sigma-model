"""Self-Contained Mechanism-Gate Execution Runner for Paper 02.

Executes the high-throughput 450-run matrix (Arm A dense lambda-sweep and Arm B late-onset
intervention), enforces deterministic seed discipline, logs 7 core metrics every 25 steps,
and serializes results to all_results.pkl.
"""

from __future__ import annotations

import argparse
import pickle
import random
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn as nn
import yaml
from torch.amp.autocast_mode import autocast
from torch.amp.grad_scaler import GradScaler
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

from paper.src.analysis.representation_geometry import compute_rga_metric
from paper.src.data.hbar_dataset import (
    HBarDataSplits,
    create_hbar_dataloaders,
    generate_hbar_splits,
)
from paper.src.models.seq2seq_transformer import Seq2SeqTransformer


@dataclass
class GateRunConfig:
    """Hyperparameters and metadata for a single gate run."""

    condition_type: str  # "arm_a_lambda" | "arm_b_late_intervention"
    condition_name: str  # e.g., "lambda_0.50" or "t_int_500"
    lambda_val: float
    intervention_step: int | None = None
    run_id: int = 0
    total_steps: int = 2000
    eval_interval: int = 25
    eval_max_batches: int = 8
    lr: float = 1e-3
    batch_size: int = 64
    d_model: int = 128
    nhead: int = 4
    num_layers: int = 2
    dim_ff: int = 512
    dropout: float = 0.1
    gradient_clip_norm: float = 1.0
    use_amp: bool = False
    device_str: str = "auto"


def evaluate_loader_accuracy(
    model: nn.Module,
    loader: DataLoader[Any],
    device: torch.device,
    use_amp: bool = False,
    max_batches: int | None = None,
) -> float:
    """Compute token-level prediction accuracy on a DataLoader."""
    model.eval()
    correct = 0
    total = 0

    with torch.inference_mode():
        for i, batch in enumerate(loader):
            if max_batches is not None and i >= max_batches:
                break
            src = batch["src"].to(device)
            tgt_in = batch["tgt_in"].to(device)
            tgt_out = batch["tgt_out"].to(device)

            with autocast("cuda", enabled=use_amp and device.type == "cuda"):
                logits = model(src, tgt_in)

            preds = logits.argmax(dim=-1)
            mask = tgt_out != 0  # Ignore padding token (0)
            correct += ((preds == tgt_out) & mask).sum().item()
            total += mask.sum().item()

    model.train()
    return float(100.0 * correct / total) if total > 0 else 0.0


def train_gate_run(
    config: GateRunConfig,
    data_splits: HBarDataSplits,
    device: torch.device | None = None,
    verbose: bool = True,
) -> dict[str, Any]:
    """Execute a single gate training run with full metric logging."""
    if device is None:
        if config.device_str == "auto":
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            device = torch.device(config.device_str)

    use_amp = config.use_amp and device.type == "cuda"

    # Enforce strict seed discipline: seed = run_id * 42 + 7
    seed = config.run_id * 42 + 7
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    if device.type == "cuda":
        torch.cuda.manual_seed_all(seed)

    # Instantiate model, loaders, and optimizer
    vocab_size = len(data_splits.vocab)
    model = Seq2SeqTransformer(
        vocab_size=vocab_size,
        d_model=config.d_model,
        nhead=config.nhead,
        num_layers=config.num_layers,
        dim_ff=config.dim_ff,
        dropout=config.dropout,
        pad_idx=0,
    ).to(device)

    eff_batch_size = min(
        config.batch_size, len(data_splits.train_pairs), len(data_splits.comp_pairs)
    )
    loaders = create_hbar_dataloaders(
        splits=data_splits,
        batch_size=eff_batch_size,
        seed=seed,
        num_workers=0,
    )

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=config.lr,
        betas=(0.9, 0.999),
        eps=1e-8,
    )
    criterion = nn.CrossEntropyLoss(ignore_index=0)
    scaler = GradScaler("cuda", enabled=use_amp)

    # Fixed sample for fast representation geometry tracking
    comp_probe_sample = data_splits.comp_pairs[:128]

    # Metrics container
    metrics: dict[str, list[float]] = {
        "step": [],
        "loss_train": [],
        "loss_comp": [],
        "acc_id": [],
        "acc_ood": [],
        "cka_rga": [],
        "param_norm": [],
    }

    train_iter = iter(loaders["train"])
    comp_iter = iter(loaders["comp"])

    pbar = tqdm(
        total=config.total_steps,
        desc=f"[{config.condition_name}|seed{config.run_id:02d}]",
        disable=not verbose,
    )

    for step in range(config.total_steps):
        # Determine effective lambda pressure for this step
        if config.condition_type == "arm_a_lambda":
            eff_lambda = config.lambda_val
        elif config.condition_type == "arm_b_late_intervention":
            t_int = config.intervention_step or 0
            eff_lambda = config.lambda_val if step >= t_int else 0.0
        else:
            eff_lambda = config.lambda_val

        # Fetch train batch
        try:
            batch = next(train_iter)
        except StopIteration:
            train_iter = iter(loaders["train"])
            batch = next(train_iter)

        src = batch["src"].to(device)
        tgt_in = batch["tgt_in"].to(device)
        tgt_out = batch["tgt_out"].to(device)

        optimizer.zero_grad(set_to_none=True)

        with autocast("cuda", enabled=use_amp):
            logits = model(src, tgt_in)
            loss_train = criterion(logits.reshape(-1, vocab_size), tgt_out.reshape(-1))

            loss_comp_val = 0.0
            if eff_lambda > 0.0:
                try:
                    c_batch = next(comp_iter)
                except StopIteration:
                    comp_iter = iter(loaders["comp"])
                    c_batch = next(comp_iter)

                c_src = c_batch["src"].to(device)
                c_tgt_in = c_batch["tgt_in"].to(device)
                c_tgt_out = c_batch["tgt_out"].to(device)

                c_logits = model(c_src, c_tgt_in)
                loss_comp = criterion(c_logits.reshape(-1, vocab_size), c_tgt_out.reshape(-1))
                loss_comp_val = float(loss_comp.item())
                total_loss = loss_train + eff_lambda * loss_comp
            else:
                total_loss = loss_train

        # Backward & optimization step
        scaler.scale(total_loss).backward()
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), config.gradient_clip_norm)
        scaler.step(optimizer)
        scaler.update()

        # Evaluation & metric logging every eval_interval steps
        if step % config.eval_interval == 0 or step == config.total_steps - 1:
            acc_id = evaluate_loader_accuracy(
                model, loaders["id"], device, use_amp, max_batches=config.eval_max_batches
            )
            acc_ood = evaluate_loader_accuracy(
                model, loaders["ood"], device, use_amp, max_batches=config.eval_max_batches
            )
            rga_val = compute_rga_metric(
                model, comp_probe_sample, data_splits.vocab, device, seed=seed
            )
            param_norm = float(
                sum(p.detach().pow(2).sum().item() for p in model.parameters()) ** 0.5
            )

            metrics["step"].append(step)
            metrics["loss_train"].append(float(loss_train.item()))
            metrics["loss_comp"].append(loss_comp_val)
            metrics["acc_id"].append(acc_id)
            metrics["acc_ood"].append(acc_ood)
            metrics["cka_rga"].append(rga_val)
            metrics["param_norm"].append(param_norm)

            if verbose:
                pbar.set_postfix(
                    {
                        "loss": f"{loss_train.item():.3f}",
                        "id": f"{acc_id:.1f}%",
                        "ood": f"{acc_ood:.1f}%",
                        "rga": f"{rga_val:.2f}",
                        "lam": f"{eff_lambda:.2f}",
                    }
                )

        pbar.update(1)

    pbar.close()

    # Full final evaluation across complete ID and OOD test splits
    final_acc_id = evaluate_loader_accuracy(model, loaders["id"], device, use_amp, max_batches=None)
    final_acc_ood = evaluate_loader_accuracy(
        model, loaders["ood"], device, use_amp, max_batches=None
    )

    result = {
        "config": asdict(config),
        "seed": seed,
        "metrics": metrics,
        "final": {
            "acc_id": final_acc_id,
            "acc_ood": final_acc_ood,
            "escaped": final_acc_ood >= 80.0,
            "final_param_norm": metrics["param_norm"][-1],
            "final_rga": metrics["cka_rga"][-1],
        },
    }

    del model, optimizer
    if device.type == "cuda":
        torch.cuda.empty_cache()

    return result


def run_gate_suite(
    config_path: str | Path = "paper/experiments/configs/gate_protocol.yaml",
    output_dir: str | Path | None = None,
    arm: str | None = None,
    seeds: list[int] | None = None,
    max_steps: int | None = None,
    smoke_test: bool = False,
    device_str: str = "auto",
) -> Path:
    """Orchestrate and serialize the complete mechanism gate suite."""
    with open(config_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    if output_dir is None:
        today_str = datetime.now().strftime("%Y-%m-%d")
        output_dir = Path(f"paper/experiments/{today_str}_gate")
    else:
        output_dir = Path(output_dir)

    runs_dir = output_dir / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)

    # Dataset generation
    if smoke_test:
        print("[Smoke-Test Mode Activated: Minimal Dataset & 50 Steps]")
        splits = generate_hbar_splits(
            n_train=1000, n_test_id=200, n_test_ood=200, n_comp_probe=200, seed=42
        )
        total_steps = max_steps or 50
        num_seeds_default = 2
    else:
        splits = generate_hbar_splits(
            n_train=cfg["data"]["n_train"],
            n_test_id=cfg["data"]["n_test_id"],
            n_test_ood=cfg["data"]["n_test_ood"],
            n_comp_probe=cfg["data"]["n_comp_probe"],
            seed=42,
        )
        total_steps = max_steps or int(cfg["optimization"]["total_steps"])
        num_seeds_default = int(cfg["experiment"]["seeds_per_condition"])

    seed_list = seeds if seeds is not None else list(range(num_seeds_default))
    all_configs: list[GateRunConfig] = []

    # Arm A: Dense lambda-sweep
    if arm is None or arm == "arm_a":
        lambda_vals = (
            [0.0, 0.5, 1.0]
            if smoke_test
            else [float(v) for v in cfg["arms"]["arm_a_dense_sweep"]["lambda_values"]]
        )
        for l_val in lambda_vals:
            for s in seed_list:
                all_configs.append(
                    GateRunConfig(
                        condition_type="arm_a_lambda",
                        condition_name=f"arm_a_lambda_{l_val:.2f}",
                        lambda_val=l_val,
                        run_id=s,
                        total_steps=total_steps,
                        eval_interval=int(cfg["optimization"]["eval_interval"]),
                        d_model=int(cfg["model"]["d_model"]),
                        nhead=int(cfg["model"]["nhead"]),
                        num_layers=int(cfg["model"]["num_encoder_layers"]),
                        dim_ff=int(cfg["model"]["dim_feedforward"]),
                        dropout=float(cfg["model"]["dropout"]),
                        device_str=device_str,
                    )
                )

    # Arm B: Late intervention
    if arm is None or arm == "arm_b":
        intervention_steps = (
            [0, 25]
            if smoke_test
            else [int(st) for st in cfg["arms"]["arm_b_late_intervention"]["intervention_steps"]]
        )
        l_val_b = float(cfg["arms"]["arm_b_late_intervention"]["lambda_val"])
        for t_int in intervention_steps:
            for s in seed_list:
                all_configs.append(
                    GateRunConfig(
                        condition_type="arm_b_late_intervention",
                        condition_name=f"arm_b_tint_{t_int}",
                        lambda_val=l_val_b,
                        intervention_step=t_int,
                        run_id=s,
                        total_steps=total_steps,
                        eval_interval=int(cfg["optimization"]["eval_interval"]),
                        d_model=int(cfg["model"]["d_model"]),
                        nhead=int(cfg["model"]["nhead"]),
                        num_layers=int(cfg["model"]["num_encoder_layers"]),
                        dim_ff=int(cfg["model"]["dim_feedforward"]),
                        dropout=float(cfg["model"]["dropout"]),
                        device_str=device_str,
                    )
                )

    print("=" * 75)
    print(f"Paper 02 Mechanism Gate Execution Runner — Total Planned Runs: {len(all_configs)}")
    print(f"Output Directory: {output_dir}")
    print("=" * 75)

    all_results: list[dict[str, Any]] = []

    for idx, run_cfg in enumerate(all_configs, 1):
        print(f"\n[{idx}/{len(all_configs)}] Running {run_cfg.condition_name} (seed {run_cfg.run_id})")
        res = train_gate_run(run_cfg, splits)
        all_results.append(res)

        # Save individual run pickle
        run_file = runs_dir / f"{run_cfg.condition_name}_run{run_cfg.run_id:02d}.pkl"
        with open(run_file, "wb") as f:
            pickle.dump(res, f)

    # Save consolidated all_results.pkl
    all_results_path = output_dir / "all_results.pkl"
    with open(all_results_path, "wb") as f:
        pickle.dump(
            {
                "timestamp": datetime.now().isoformat(),
                "config_file": str(config_path),
                "total_runs": len(all_results),
                "runs": all_results,
            },
            f,
        )

    print("\n" + "=" * 75)
    print(f"Gate Execution Complete! Saved {len(all_results)} runs to: {all_results_path}")
    print("=" * 75)

    return all_results_path


def main() -> None:
    """CLI entry point for gate runner."""
    parser = argparse.ArgumentParser(description="Paper 02 Mechanism Gate Execution Runner")
    parser.add_argument(
        "--config",
        type=str,
        default="paper/experiments/configs/gate_protocol.yaml",
        help="Path to YAML gate protocol config",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Directory to save run results",
    )
    parser.add_argument(
        "--arm",
        type=str,
        choices=["arm_a", "arm_b"],
        default=None,
        help="Run only Arm A or Arm B",
    )
    parser.add_argument(
        "--seeds",
        type=str,
        default=None,
        help="Comma-separated seed indices (e.g. 0,1,2)",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=None,
        help="Override total training steps",
    )
    parser.add_argument(
        "--smoke-test",
        action="store_true",
        help="Execute minimal smoke test (2 seeds, 50 steps)",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="auto",
        help="Compute device ('cuda', 'cpu', or 'auto')",
    )

    args = parser.parse_args()

    seed_list = [int(s.strip()) for s in args.seeds.split(",")] if args.seeds else None

    run_gate_suite(
        config_path=args.config,
        output_dir=args.output_dir,
        arm=args.arm,
        seeds=seed_list,
        max_steps=args.max_steps,
        smoke_test=args.smoke_test,
        device_str=args.device,
    )


if __name__ == "__main__":
    main()
