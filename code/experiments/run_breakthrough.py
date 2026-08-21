"""Breakthrough Experiment CLI Runner.

Usage:
    # Run 50,000-step grokking test (or smoke test):
    python code/experiments/run_breakthrough.py --config code/experiments/configs/grokking_50k.yaml --smoke
    python code/experiments/run_breakthrough.py --config code/experiments/configs/grokking_50k.yaml

    # Run equal-cumulative-exposure timing discrimination matrix:
    python code/experiments/run_breakthrough.py --config code/experiments/configs/exposure_matrix.yaml
"""

from __future__ import annotations

import argparse
import os
import pickle
import random
import sys
from pathlib import Path
from typing import Any

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))

from sigma_align.config import load_config
from sigma_align.experiments.hbar_breakthrough import train_breakthrough_model
from sigma_align.experiments.hbar_data import (
    generate_hard_compositional_data,
    make_loaders,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Breakthrough Experiment Runner.")
    p.add_argument("--config", required=True, help="Path to YAML config")
    p.add_argument("--condition", action="append", help="Specific condition(s) to run")
    p.add_argument("--n-runs", type=int, help="Runs per condition")
    p.add_argument("--n-timesteps", type=int, help="Steps per run")
    p.add_argument("--eval-every", type=int, help="Evaluation cadence")
    p.add_argument("--outdir", default="output/breakthrough", help="Output directory")
    p.add_argument("--smoke", action="store_true", help="Quick smoke test mode")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_config(args.config)

    if args.n_runs is not None:
        cfg["experiment"]["n_runs_per_condition"] = args.n_runs
    if args.n_timesteps is not None:
        cfg["training"]["n_timesteps"] = args.n_timesteps
    if args.eval_every is not None:
        cfg["training"]["eval_every"] = args.eval_every

    if args.smoke:
        cfg["experiment"]["n_runs_per_condition"] = 1
        cfg["training"]["n_timesteps"] = 300
        cfg["training"]["eval_every"] = 50
        print(">>> SMOKE TEST MODE (1 run x 300 steps)")

    conditions = args.condition or list(cfg["conditions"].keys())
    n_runs = int(cfg["experiment"]["n_runs_per_condition"])
    n_timesteps = int(cfg["training"]["n_timesteps"])
    eval_every = int(cfg["training"]["eval_every"])
    global_seed = int(cfg["reproducibility"]["global_seed"])
    batch_size = int(cfg["training"]["batch_size"])
    num_workers = int(cfg["training"]["num_workers"])

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    use_amp = torch.cuda.is_available() and bool(cfg["training"].get("use_amp", True))

    random.seed(global_seed)
    np.random.seed(global_seed)
    torch.manual_seed(global_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(global_seed)
        print(f"GPU: {torch.cuda.get_device_name(0)} | AMP={use_amp}")
    else:
        print("Running on CPU")

    os.makedirs(args.outdir, exist_ok=True)

    print("Generating H-Bar dataset splits...")
    train_pairs, test_pairs, ood_pairs, comp_pairs, vocab = generate_hard_compositional_data(
        n_train=int(cfg["data"]["n_train"]),
        n_test_id=int(cfg["data"]["n_test_id"]),
        n_test_ood=int(cfg["data"]["n_test_ood"]),
        n_comp=int(cfg["data"]["n_comp"]),
    )
    loaders = make_loaders(
        train_pairs,
        test_pairs,
        ood_pairs,
        comp_pairs,
        vocab,
        batch_size=batch_size,
        seed=global_seed,
        num_workers=0 if not torch.cuda.is_available() else num_workers,
    )

    all_results: dict[str, list[dict[str, Any]]] = {}
    for condition in conditions:
        print(f"\n{'=' * 65}\nCONDITION: {condition.upper()}\n{'=' * 65}")
        cond_runs = []
        for run_id in range(n_runs):
            metrics = train_breakthrough_model(
                condition=condition,
                run_id=run_id,
                cfg=cfg,
                loaders=loaders,
                device=device,
                use_amp=use_amp,
                n_timesteps=n_timesteps,
                eval_every=eval_every,
                lr=float(cfg["training"]["lr"]),
            )
            cond_runs.append(metrics)
        all_results[condition] = cond_runs

    # Save results
    out_file = Path(args.outdir) / f"{cfg['experiment']['name']}_results.pkl"
    with open(out_file, "wb") as f:
        pickle.dump(all_results, f)
    print(f"\n[DONE] Results saved to {out_file}")


if __name__ == "__main__":
    main()
