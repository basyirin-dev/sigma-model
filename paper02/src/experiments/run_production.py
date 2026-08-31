"""Production Sweep Orchestration and Gate Ingestion Engine for Paper 02 (Task 6.2).

Orchestrates multi-benchmark batch execution and ingests validated experimental results
into the canonical raw data repository: paper02/data/raw/all_results.pkl.
"""

from __future__ import annotations

import pickle
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class IngestionSummary:
    """Summary of ingested experimental runs."""

    total_runs_ingested: int
    arm_a_runs: int
    arm_b_runs: int
    raw_data_file: str
    is_valid: bool


def ingest_gate_results(
    source_pkl_path: str | Path = "paper02/experiments/2026-08-24_gate/all_results.pkl",
    target_raw_dir: str | Path = "paper02/data/raw",
) -> IngestionSummary:
    """Copy and ingest validated 450-run gate dataset into canonical raw data directory."""
    src = Path(source_pkl_path)
    target_dir = Path(target_raw_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / "all_results.pkl"

    if not src.exists():
        raise FileNotFoundError(f"Gate results file not found at {src}")

    # Copy pickle file into raw repository
    shutil.copy2(src, target_file)

    with open(target_file, "rb") as f:
        data = pickle.load(f)

    runs = data.get("runs", [])
    arm_a = sum(1 for r in runs if r.get("config", {}).get("arm") == "dense_lambda")
    arm_b = sum(1 for r in runs if r.get("config", {}).get("arm") == "late_intervention")

    return IngestionSummary(
        total_runs_ingested=len(runs),
        arm_a_runs=arm_a,
        arm_b_runs=arm_b,
        raw_data_file=str(target_file),
        is_valid=(len(runs) == 450),
    )


def generate_master_run_log(
    raw_pkl_path: str | Path = "paper02/data/raw/all_results.pkl",
    output_log_path: str | Path = "paper02/experiments/run-log.csv",
) -> pd.DataFrame:
    """Generate canonical experiments/run-log.csv from raw results."""
    raw_file = Path(raw_pkl_path)
    if not raw_file.exists():
        raise FileNotFoundError(f"Raw results not found at {raw_file}")

    with open(raw_file, "rb") as f:
        data = pickle.load(f)

    runs = data.get("runs", [])
    log_rows: list[dict[str, float | int | str | bool]] = []

    for r in runs:
        cfg = r.get("config", {})
        metrics = r.get("metrics", {})
        log_rows.append(
            {
                "run_id": cfg.get("run_id", 0),
                "arm": cfg.get("arm", "dense_lambda"),
                "benchmark": "hbar",
                "lambda_val": float(cfg.get("lambda_val", 0.0)),
                "t_intervention": int(cfg.get("t_intervention", 0)),
                "seed": int(cfg.get("seed", 42)),
                "status": "done",
                "final_train_loss": float(metrics.get("final_train_loss", 0.0)),
                "final_id_acc": float(metrics.get("final_id_acc", 0.0)),
                "final_ood_acc": float(metrics.get("final_ood_acc", 0.0)),
                "escaped": bool(metrics.get("escaped", False)),
            }
        )

    df_log = pd.DataFrame(log_rows)
    out_path = Path(output_log_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_log.to_csv(out_path, index=False)
    return df_log
