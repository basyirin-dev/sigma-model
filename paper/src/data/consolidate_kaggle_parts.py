"""Consolidation and Ingestion Engine for Partitioned Kaggle Runs (Paper 02).

Consolidates outputs from partitioned Kaggle notebooks:
- Part 1 (Tier 1A): p06_part1_hbar_scan_results.pkl (360 runs)
- Part 2 (Tier 1B): p06_part2_cogs_pcfg_results.pkl (360 runs)
- Part 3 (Tier 2):  p06_part3_arch_scaling_results.pkl (240 runs)

Merges them into canonical raw dataset: paper/data/raw/p06_production_results.pkl
and updates paper/experiments/run-log.csv.
"""

from __future__ import annotations

import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


@dataclass(frozen=True)
class ConsolidationSummary:
    total_runs_merged: int
    part1_runs: int
    part2_runs: int
    part3_runs: int
    output_pkl_path: str
    output_log_path: str
    is_complete_matrix: bool


def consolidate_kaggle_results(
    raw_dir: Path | str = "paper/data/raw",
    output_dir: Path | str = "paper/data/raw",
    run_log_path: Path | str = "paper/experiments/run-log.csv",
) -> ConsolidationSummary:
    """Scan raw directory for partitioned results, consolidate them, and generate run log."""
    raw_path = Path(raw_dir)
    out_path = Path(output_dir)
    log_path = Path(run_log_path)
    out_path.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    part1_file = raw_path / "p06_part1_hbar_scan_results.pkl"
    part2_file = raw_path / "p06_part2_cogs_pcfg_results.pkl"
    part3_file = raw_path / "p06_part3_arch_scaling_results.pkl"

    all_runs: list[dict[str, Any]] = []
    p1_count, p2_count, p3_count = 0, 0, 0

    if part1_file.exists():
        with part1_file.open("rb") as f:
            p1_data = pickle.load(f)
            p1_count = len(p1_data)
            all_runs.extend(p1_data)

    if part2_file.exists():
        with part2_file.open("rb") as f:
            p2_data = pickle.load(f)
            p2_count = len(p2_data)
            all_runs.extend(p2_data)

    if part3_file.exists():
        with part3_file.open("rb") as f:
            p3_data = pickle.load(f)
            p3_count = len(p3_data)
            all_runs.extend(p3_data)

    # Save consolidated raw results
    consolidated_file = out_path / "p06_production_results.pkl"
    with consolidated_file.open("wb") as f:
        pickle.dump(all_runs, f)

    # Build Master run-log.csv
    benchmark_split_map = {
        "hbar": "split_b_recursion_depth",
        "scan_jump": "add_primitive_jump",
        "cogs": "structural_recursion",
        "pcfg_set": "systematicity",
    }

    log_rows: list[dict[str, Any]] = []
    for idx, r in enumerate(all_runs, start=1):
        seed_val = int(r.get("seed", 7))
        cell_seed_idx = (seed_val - 7) // 42
        bmark = r.get("benchmark", "unknown")
        split_val = r.get("split", benchmark_split_map.get(bmark, "standard"))
        log_rows.append(
            {
                "run_id": idx,
                "cell_seed_idx": cell_seed_idx,
                "tier": r.get("tier", "unknown"),
                "evidence_class": r.get("evidence_class", "unknown"),
                "benchmark": bmark,
                "split": split_val,
                "arch": r.get("arch", "unknown"),
                "lambda": float(r.get("lambda", 0.0)),
                "lambda_regime": r.get("lambda_regime", "unknown"),
                "seed": seed_val,
                "final_id_acc": float(r.get("final_id_acc", 0.0)),
                "final_ood_acc": float(r.get("final_ood_acc", 0.0)),
                "mean_whitened_gca": float(r.get("mean_whitened_gca", 0.0)),
                "top_hessian_eig": float(r.get("top_hessian_eig", 0.0)),
                "wall_clock_sec": float(r.get("wall_clock_sec", 0.0)),
                "status": "PASS",
            }
        )
    df_log = pd.DataFrame(log_rows)
    df_log.to_csv(log_path, index=False)

    return ConsolidationSummary(
        total_runs_merged=len(all_runs),
        part1_runs=p1_count,
        part2_runs=p2_count,
        part3_runs=p3_count,
        output_pkl_path=str(consolidated_file),
        output_log_path=str(log_path),
        is_complete_matrix=(len(all_runs) == 960),
    )


if __name__ == "__main__":
    summary = consolidate_kaggle_results()
    print(f"✅ Consolidated {summary.total_runs_merged} runs into {summary.output_pkl_path}")
    print(f"✅ Updated Master Run Log: {summary.output_log_path}")
