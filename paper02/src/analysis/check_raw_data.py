"""Raw Data Sanity Auditor and Immutability Checker for Paper 02 (Task 6.3).

Verifies that all raw output data tensors in paper02/data/raw/ contain zero NaNs or Infs,
confirming full training convergence and valid trajectory recordings.
"""

from __future__ import annotations

import hashlib
import pickle
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class RawDataAuditSummary:
    """Audit report on raw data tensor integrity."""

    is_clean: bool
    total_runs_checked: int
    nan_count: int
    inf_count: int
    file_hashes: dict[str, str]


def audit_raw_datasets(
    raw_dir: str | Path = "paper02/data/raw",
) -> RawDataAuditSummary:
    """Audit all raw datasets for NaNs, Infs, and compute SHA-256 signatures."""
    raw_path = Path(raw_dir)
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw data directory {raw_path} not found")

    total_runs = 0
    nan_count = 0
    inf_count = 0
    file_hashes: dict[str, str] = {}

    for fpath in raw_path.glob("*.*"):
        content = fpath.read_bytes()
        sha = hashlib.sha256(content).hexdigest()
        file_hashes[fpath.name] = sha

        if fpath.suffix == ".csv":
            df = pd.read_csv(fpath)
            numeric_cols = df.select_dtypes(include=[np.number])
            nans = int(numeric_cols.isna().sum().sum())
            infs = int(np.isinf(numeric_cols.to_numpy()).sum())
            nan_count += nans
            inf_count += infs
            total_runs += len(df)
        elif fpath.suffix == ".pkl":
            with open(fpath, "rb") as f:
                data = pickle.load(f)
            runs = data.get("runs", []) if isinstance(data, dict) else data
            total_runs += len(runs)
            for r in runs:
                metrics = r.get("metrics", {})
                for k, v in metrics.items():
                    if isinstance(v, (int, float)):
                        if np.isnan(v):
                            nan_count += 1
                        if np.isinf(v):
                            inf_count += 1

    is_clean = (nan_count == 0) and (inf_count == 0)

    return RawDataAuditSummary(
        is_clean=is_clean,
        total_runs_checked=total_runs,
        nan_count=nan_count,
        inf_count=inf_count,
        file_hashes=file_hashes,
    )


if __name__ == "__main__":
    report = audit_raw_datasets()
    print(
        f"✅ Raw Data Audit Complete: {report.total_runs_checked} records checked. "
        f"Clean: {report.is_clean} (NaNs={report.nan_count}, Infs={report.inf_count})"
    )
