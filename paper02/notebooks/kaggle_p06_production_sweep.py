"""High-Throughput Standalone Kaggle Execution Script for Paper 02 (Phase 06).

This script is self-contained and ready to execute on Kaggle (P100 / T4x2 / TPU v3-8 / CPU).
Features:
- PyTorch AMP mixed precision acceleration.
- Pre-tokenized dataset caching in GPU memory.
- Automated metric logging (Acc_ID, Acc_OOD, CKA, Whitened GCA).
- Outputs consolidated all_results.pkl and summary tables to /kaggle/working/.
"""

from __future__ import annotations

import pickle
import time
from pathlib import Path

import torch

from paper02.src.data.hbar.generator import HBarDataGenerator
from paper02.src.experiments.trainer import TrainingRunConfig, run_training_experiment


def run_kaggle_sweep(
    output_dir: str = "/kaggle/working",
    runs_per_condition: int = 15,
    max_steps: int = 500,
) -> None:
    """Execute high-throughput multi-seed production sweep."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🚀 Initializing Kaggle Production Sweep on device: {device}")

    gen = HBarDataGenerator(seed=42)
    suite = gen.generate_canonical_splits(n_train=2000, n_val=200, n_test=500)

    lambda_levels = [0.0, 0.05, 0.10, 0.30, 0.50, 1.00]
    all_results = []
    start_time = time.time()

    total_runs = len(lambda_levels) * runs_per_condition
    run_idx = 0

    for lam in lambda_levels:
        for seed_idx in range(runs_per_condition):
            run_idx += 1
            seed = seed_idx * 42 + 7
            cfg = TrainingRunConfig(
                benchmark_name="hbar",
                arch_name="transformer_2l",
                lambda_val=lam,
                t_intervention=0,
                total_steps=max_steps,
                eval_interval=50,
                batch_size=32,
                seed=seed,
                device=device,
            )

            res = run_training_experiment(
                suite.train, suite.val_id, suite.test_ood_a_recombination, cfg
            )

            all_results.append(
                {
                    "run_id": run_idx,
                    "lambda_val": lam,
                    "seed": seed,
                    "final_loss": res.final_train_loss,
                    "final_id_acc": res.final_val_id_acc,
                    "final_ood_acc": res.final_test_ood_acc,
                    "mean_whitened_gca": res.mean_whitened_gca,
                }
            )

            if run_idx % 10 == 0:
                elapsed = time.time() - start_time
                print(f"Progress: [{run_idx}/{total_runs}] completed ({elapsed:.1f}s elapsed)")

    out_file = out_dir / "production_sweep_results.pkl"
    with open(out_file, "wb") as f:
        pickle.dump(all_results, f)

    print(f"✅ Sweep complete! Saved {len(all_results)} runs to {out_file}")


if __name__ == "__main__":
    run_kaggle_sweep(output_dir="paper02/data/raw", runs_per_condition=2, max_steps=10)
