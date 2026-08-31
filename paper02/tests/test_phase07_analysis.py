"""Unit and Regression Tests for Phase 07 Statistical Analysis & Figure Generation.

Verifies:
- Tidy table derivation engine across multi-benchmark production archives.
- Bifurcation curve fitting and bootstrap confidence intervals.
- Publication figure generation (PDF, PNG, TikZ) and JSON metadata sidecars.
- Standards compliance for figure sidecars (CC.3.2, CC.3.4, CC.3.6).
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from paper02.src.analysis.generate_publication_figures import (
    generate_all_publication_figures,
)
from paper02.src.analysis.run_phase07_analysis import (
    run_bifurcation_bootstrap_analysis,
    run_phase07_analysis_pipeline,
)
from paper02.src.data.derive_processed_tables import (
    ProcessedTablesSummary,
    derive_all_processed_tables,
)


class TestPhase07Analysis:
    """Test suite covering Phase 07 data derivation, statistical testing, and figures."""

    def test_derive_all_processed_tables_production(self, tmp_path: Path) -> None:
        """Verify derive_all_processed_tables generates all 6 tidy tables."""
        summary = derive_all_processed_tables(
            raw_pkl_path="paper02/data/raw/p06_production_results.pkl",
            processed_dir=tmp_path,
            gate_pkl_path="paper02/data/raw/all_results.pkl",
        )
        assert isinstance(summary, ProcessedTablesSummary)
        assert summary.ood_summary_rows > 0
        assert summary.inflection_rows > 0
        assert summary.cka_trajectory_rows > 0
        assert summary.tost_comparison_rows > 0
        assert summary.granger_rows > 0
        assert summary.hessian_rows > 0

        # Verify all files exist
        expected_files = [
            "ood_summary_table.csv",
            "inflection_breakpoints.csv",
            "cka_trajectories.csv",
            "pairwise_welch_tost.csv",
            "granger_causality_results.csv",
            "hessian_spectral_summary.csv",
        ]
        for fname in expected_files:
            fpath = tmp_path / fname
            assert fpath.exists(), f"Missing table {fname}"
            df = pd.read_csv(fpath)
            assert not df.empty, f"Table {fname} is empty"

    def test_bifurcation_bootstrap_analysis(self) -> None:
        """Verify logistic change-point fitting and bootstrap intervals."""
        df_summary = pd.read_csv("paper02/data/processed/ood_summary_table.csv")
        (
            lam_crit,
            lam_ci_low,
            lam_ci_high,
            k_fit,
            k_ci_low,
            k_ci_high,
            is_sharp,
        ) = run_bifurcation_bootstrap_analysis(df_summary, num_bootstrap=100)

        assert 0.0 <= lam_crit <= 0.05
        assert lam_ci_low <= lam_crit <= lam_ci_high
        assert k_fit > 0.0
        assert k_ci_low <= k_fit <= k_ci_high

    def test_publication_figure_generation(self, tmp_path: Path) -> None:
        """Verify all 5 publication figures and metadata sidecars are rendered."""
        meta_list = generate_all_publication_figures(
            processed_dir="paper02/data/processed",
            output_dir=tmp_path,
        )
        assert len(meta_list) == 5

        for i in range(1, 6):
            matched_pdf = list(tmp_path.glob(f"figure{i}_*.pdf"))
            matched_png = list(tmp_path.glob(f"figure{i}_*.png"))
            matched_tex = list(tmp_path.glob(f"figure{i}_*.tex"))
            matched_meta = tmp_path / f"figure{i}_metadata.json"

            assert len(matched_pdf) == 1, f"Missing PDF for Figure {i}"
            assert len(matched_png) == 1, f"Missing PNG for Figure {i}"
            assert len(matched_tex) == 1, f"Missing TikZ for Figure {i}"
            assert matched_meta.exists(), f"Missing metadata sidecar for Figure {i}"

            with open(matched_meta, encoding="utf-8") as f:
                meta = json.load(f)
            assert meta.get("colorblind_safe") is True
            assert "DRAFT_ANALYSIS" in meta.get("status", "")
            assert len(meta.get("caption", "")) > 20

    def test_run_phase07_pipeline_execution(self, tmp_path: Path) -> None:
        """Verify full pipeline execution and structured result object."""
        res = run_phase07_analysis_pipeline(
            raw_pkl_path="paper02/data/raw/p06_production_results.pkl",
            processed_dir=tmp_path / "processed",
            figures_dir=tmp_path / "figures",
            num_bootstrap=50,
        )
        assert res.num_figures_generated == 5
        assert res.below_eos_ceiling is True
        assert (tmp_path / "processed" / "phase07_analysis_summary.json").exists()
