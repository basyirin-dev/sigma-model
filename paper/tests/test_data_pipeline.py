"""Unit tests for the raw data auditor and processed table derivation pipeline (Paper 02 Task 6.3)."""

from __future__ import annotations

import pandas as pd

from paper.src.analysis.check_raw_data import audit_raw_datasets
from paper.src.data.derive_processed_tables import derive_all_processed_tables


class TestDataPipeline:
    """Test raw data tensor auditing and tidy processed table generation."""

    def test_raw_data_auditor(self) -> None:
        report = audit_raw_datasets(raw_dir="paper/data/raw")
        assert report.is_clean
        assert report.nan_count == 0
        assert report.inf_count == 0
        assert report.total_runs_checked > 0

    def test_derive_processed_tables(self, tmp_path) -> None:
        proc_dir = tmp_path / "processed"
        summary = derive_all_processed_tables(
            raw_pkl_path="paper/data/raw/p06_production_results.pkl",
            processed_dir=proc_dir,
        )

        assert summary.ood_summary_rows >= 10
        assert summary.inflection_rows >= 1
        assert summary.tost_comparison_rows >= 10

        # Verify OOD summary contents
        df_ood = pd.read_csv(proc_dir / "ood_summary_table.csv")
        assert "mean_ood_acc" in df_ood.columns
        assert "escape_fraction" in df_ood.columns

        # Verify Inflection table
        df_inf = pd.read_csv(proc_dir / "inflection_breakpoints.csv")
        assert bool(df_inf[df_inf["arch"] == "transformer_2l"]["is_sharp_phase_transition"].iloc[0])

        # Verify dense-grid data integrity (D6)
        df_dense = pd.read_csv(proc_dir / "dense_grid_330_runs.csv")
        assert len(df_dense) == 330
        assert df_dense["lambda_val"].nunique() == 11
        assert "escaped" in df_dense.columns
        assert df_dense["escaped"].sum() > 0
        counts = df_dense.groupby("lambda_val")["escaped"].sum().to_dict()
        assert counts[0.0] == 2
        assert counts[0.015] == 13
        assert counts[0.020] == 12
        assert counts[0.025] == 15
        assert counts[0.030] == 12
        assert counts[0.500] == 30
