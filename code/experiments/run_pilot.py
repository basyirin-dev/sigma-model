"""Phase 04 mechanism-gate pilot harness (thin orchestration — ADR-0004).

Ports the canonical pilot notebook (``archive/experiments/h-bar-experiment.ipynb``)
into a CLI: generates the H-Bar benchmark once, runs the four arms
(baseline / fixed_weight / additive / multiplicative) with the measured Stage-1
proxy (GCA + RGA), and persists ``all_results.pkl`` + ``summary.json`` + per-run
pkls in the pilot's schema.

Usage::

    python code/experiments/run_pilot.py --config code/experiments/configs/gate.yaml
    python code/experiments/run_pilot.py --condition fixed_weight --smoke
"""

from __future__ import annotations

import argparse
import json
import os
import pickle
import random
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import torch
from tqdm.auto import tqdm

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))

from sigma_align.config import load_config  # noqa: E402
from sigma_align.experiments.hbar_data import (  # noqa: E402
    generate_hard_compositional_data,
    make_loaders,
)
from sigma_align.experiments.hbar_train import persist_run, train_hbar_model  # noqa: E402

DEFAULT_CONFIG = str(Path(__file__).resolve().parent / "configs" / "gate.yaml")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Phase 04 mechanism-gate pilot (H-Bar).")
    p.add_argument("--config", default=DEFAULT_CONFIG, help="YAML config (ADR-0004)")
    p.add_argument(
        "--condition",
        choices=["baseline", "fixed_weight", "additive", "multiplicative"],
        action="append",
        help="arm(s) to run; default: all arms from config",
    )
    p.add_argument("--n-runs", type=int, help="runs per arm (overrides config)")
    p.add_argument("--n-timesteps", type=int, help="training steps per run")
    p.add_argument("--eval-every", type=int, help="eval/proxy cadence (steps)")
    p.add_argument("--seed", type=int, help="global seed (overrides config)")
    p.add_argument("--outdir", default="output/gate", help="results directory (gitignored)")
    p.add_argument(
        "--smoke",
        action="store_true",
        help="smoke mode: 1 run x 200 steps per arm",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_config(args.config)
    if args.seed is not None:
        cfg["reproducibility"]["global_seed"] = args.seed
    if args.n_runs is not None:
        cfg["experiment"]["n_runs_per_condition"] = args.n_runs
    if args.n_timesteps is not None:
        cfg["training"]["n_timesteps"] = args.n_timesteps
    if args.eval_every is not None:
        cfg["training"]["eval_every"] = args.eval_every

    if args.smoke:
        cfg["experiment"]["n_runs_per_condition"] = 1
        cfg["training"]["n_timesteps"] = 200
        print("SMOKE MODE: 1 run x 200 steps per arm")

    conditions = args.condition or list(cfg["experiment"]["conditions"])
    n_runs = int(cfg["experiment"]["n_runs_per_condition"])
    n_timesteps = int(cfg["training"]["n_timesteps"])
    eval_every = int(cfg["training"]["eval_every"])
    global_seed = int(cfg["reproducibility"]["global_seed"])
    batch_size = int(cfg["training"]["batch_size"])
    num_workers = int(cfg["training"]["num_workers"])

    # Device / AMP / determinism (CC.2.1).
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    use_amp = torch.cuda.is_available() and bool(cfg["training"]["use_amp"])
    random.seed(global_seed)
    np.random.seed(global_seed)
    torch.manual_seed(global_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(global_seed)
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        print(f"GPU: {torch.cuda.get_device_name(0)} | AMP={use_amp}")
    else:
        print("No GPU found — running on CPU")

    # Generate the benchmark once, shared across all arms/runs (pilot cell 1).
    random.seed(global_seed)
    np.random.seed(global_seed)
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
    print(
        f"DataLoaders ready: train={len(loaders['train'].dataset)} "
        f"id={len(loaders['id'].dataset)} ood={len(loaders['ood'].dataset)} "
        f"comp={len(loaders['comp'].dataset)}"
    )

    # Run all arms.
    all_results: dict[str, list[dict[str, Any]]] = {}
    for condition in conditions:
        print(f"\n{'=' * 60}\nCONDITION: {condition.upper()}\n{'=' * 60}")
        cond_runs = []
        for run_id in tqdm(range(n_runs), desc=f"[{condition}] runs", leave=False):
            metrics = train_hbar_model(
                condition=condition,
                run_id=run_id,
                cfg=cfg,
                loaders=loaders,
                device=device,
                use_amp=use_amp,
                n_timesteps=n_timesteps,
                eval_every=eval_every,
                lr=float(cfg["training"]["lr"]),
                save_checkpoints=bool(cfg["experiment"]["save_checkpoints"]),
                checkpoint_dir=f"{args.outdir}/checkpoints",
            )
            persist_run(metrics, condition, run_id, n_timesteps, args.outdir)
            cond_runs.append(metrics)
        all_results[condition] = cond_runs

        ood_final = [r["final"]["acc_ood"] for r in cond_runs]
        id_final = [r["final"]["acc_id"] for r in cond_runs]
        print(
            f"{condition.upper():14s}  ID={np.mean(id_final):.1f}+-{np.std(id_final):.1f}%  "
            f"OOD={np.mean(ood_final):.1f}+-{np.std(ood_final):.1f}%  "
            f"gap={np.mean(id_final) - np.mean(ood_final):.1f}%"
        )

    # Persist all_results.pkl + summary.json (pilot cells 5 & 8 schema).
    os.makedirs(args.outdir, exist_ok=True)
    with open(f"{args.outdir}/all_results.pkl", "wb") as f:
        pickle.dump(all_results, f)

    summary_stats = {
        c: {
            "condition": c,
            "final_acc_id_mean": float(np.mean([r["final"]["acc_id"] for r in runs])),
            "final_acc_id_std": float(np.std([r["final"]["acc_id"] for r in runs])),
            "final_acc_ood_mean": float(np.mean([r["final"]["acc_ood"] for r in runs])),
            "final_acc_ood_std": float(np.std([r["final"]["acc_ood"] for r in runs])),
            "raw_acc_ood": [r["final"]["acc_ood"] for r in runs],
            "n_runs": len(runs),
        }
        for c, runs in all_results.items()
    }
    best_cond = max(summary_stats, key=lambda c: summary_stats[c]["final_acc_ood_mean"])
    summary_json = {
        "experiment": {
            "date": datetime.now().isoformat(),
            "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
            "runs": sum(len(v) for v in all_results.values()),
            "amp": use_amp,
            "global_seed": global_seed,
            "config": str(args.config),
        },
        "results": {
            c: {
                "mean_ood": summary_stats[c]["final_acc_ood_mean"],
                "std_ood": summary_stats[c]["final_acc_ood_std"],
                "mean_id": summary_stats[c]["final_acc_id_mean"],
                "n_runs": summary_stats[c]["n_runs"],
            }
            for c in summary_stats
        },
        "best_condition": best_cond,
        "compositional_gap": (
            summary_stats["baseline"]["final_acc_id_mean"]
            - summary_stats["baseline"]["final_acc_ood_mean"]
        ),
    }
    with open(f"{args.outdir}/summary.json", "w") as f:
        json.dump(summary_json, f, indent=2)
    print(
        f"\nAll {sum(len(v) for v in all_results.values())} runs complete — "
        f"saved to {args.outdir}"
    )


if __name__ == "__main__":
    main()
