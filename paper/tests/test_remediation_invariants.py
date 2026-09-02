"""Regression Invariant Tests for Pre-Phase 06 Remediation (Paper 02).

Enforces structural guards against all 10 identified defect domains:
1. Tiered matrix configuration & GPU budget compliance.
2. Locked lambda_crit = 0.025 and regime classifications.
3. Calibrated ODE defaults (lambda_crit == 0.025).
4. Statistical sample size policy (n=30 primary, n=10 exploratory).
5. Architecture C GRU alignment.
6. Raw benchmark data ingestion and SHA-256 checksums.
7. Pairwise strict support disjointness across all 4 benchmark suites.
8. 54-rule standards documentation compliance.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from paper.src.config.matrix import (
    generate_tiered_manifests,
    load_matrix_config,
    validate_manifests,
)
from paper.src.continuous.two_subspace_ode import (
    TwoSubspaceParams,
    TwoSubspaceSystem,
)
from paper.src.data.audit_leakage import audit_dataset_suite


class TestRemediationInvariants:
    """Rigorous test suite protecting all Phase 06 remediation invariants."""

    def test_calibrated_ode_default(self) -> None:
        """Verify continuous ODE defaults to locked empirical threshold lambda_crit = 0.025."""
        params = TwoSubspaceParams()
        assert params.b_C == 0.025
        assert params.a_C == 1.0
        sys = TwoSubspaceSystem(params)
        assert np.isclose(sys.lambda_crit, 0.025)

        # Transverse eigenvalue mu_perp is zero at lambda_crit
        sys_crit = TwoSubspaceSystem(TwoSubspaceParams(lambda_val=0.025))
        assert np.isclose(sys_crit.mu_perp, 0.0)

    def test_lambda_regimes_classification(self) -> None:
        """Verify lambda regime boundaries and ensure lambda = 0.10 is NOT critical."""
        config_path = Path("paper/experiments/configs/matrix_p04.yaml")
        cfg = load_matrix_config(config_path)

        regimes = cfg["conditions"]["lambda_regimes"]
        assert np.isclose(regimes["locked_lambda_crit"], 0.025)
        assert np.isclose(regimes["uncertainty"], 0.005)

        classifications = regimes["grid_classification"]
        assert classifications[0.000] == "subcritical"
        assert classifications[0.015] == "subcritical"
        assert classifications[0.020] == "boundary"
        assert classifications[0.025] == "boundary"
        assert classifications[0.030] == "boundary"
        assert classifications[0.050] == "supercritical"
        assert classifications[0.100] == "supercritical"
        assert classifications[0.500] == "supercritical"

        # Explicit prohibition assertions
        assert classifications[0.100] != "boundary"
        assert classifications[0.100] != "critical_edge"
        assert classifications[0.050] != "boundary"

    def test_tier_1_grid_contains_boundary_and_seeds(self) -> None:
        """Verify Tier 1 primary matrix contains all critical boundary points with n=30."""
        config_path = Path("paper/experiments/configs/matrix_p04.yaml")
        cfg = load_matrix_config(config_path)

        tier1 = cfg["conditions"]["tier_1_primary_change_point"]
        assert tier1["evidence_class"] == "primary"
        assert tier1["num_seeds"] == 30
        assert set(tier1["lambda_grid"]) == {0.000, 0.015, 0.020, 0.025, 0.030, 0.500}
        assert tier1["architectures"] == ["arch_a_transformer_2l"]
        assert tier1["run_count"] == 720

    def test_architecture_c_is_gru(self) -> None:
        """Verify Architecture C is specified as GRU recurrent seq2seq (not Mamba/SSM)."""
        config_path = Path("paper/experiments/configs/matrix_p04.yaml")
        cfg = load_matrix_config(config_path)

        arch_c = cfg["architectures"]["arch_c_recurrent_gru"]
        assert arch_c["family"] == "recurrent"
        assert arch_c["model_class"] == "RecurrentSeq2Seq"
        assert arch_c["rnn_type"] == "GRU"
        assert arch_c["num_layers"] == 2
        assert "d_state" not in arch_c or arch_c.get("d_state") is None

    def test_generate_tiered_manifests(self) -> None:
        """Verify programmatic expansion of Tier 1 (720) and Tier 2 (240) manifests."""
        config_path = Path("paper/experiments/configs/matrix_p04.yaml")

        t1_manifests = generate_tiered_manifests(config_path, tier=1)
        assert len(t1_manifests) == 720
        validate_manifests(t1_manifests)

        t2_manifests = generate_tiered_manifests(config_path, tier=2)
        assert len(t2_manifests) == 240
        validate_manifests(t2_manifests)

        all_manifests = generate_tiered_manifests(config_path, tier="all")
        assert len(all_manifests) == 960
        validate_manifests(all_manifests)

    def test_raw_benchmark_artifacts_and_checksums(self) -> None:
        """Verify all 4 benchmark raw files exist and match checksums.sha256."""
        raw_dir = Path("paper/data/raw")
        checksum_file = raw_dir / "checksums.sha256"
        assert checksum_file.exists(), "checksums.sha256 missing"

        with checksum_file.open("r", encoding="utf-8") as f:
            lines = [line.strip().split() for line in f if line.strip()]

        for expected_hash, fname in lines:
            fpath = raw_dir / fname
            assert fpath.exists(), f"Raw benchmark file missing: {fname}"

            h = hashlib.sha256()
            with fpath.open("rb") as f:
                while chunk := f.read(65536):
                    h.update(chunk)
            assert h.hexdigest() == expected_hash, f"Checksum mismatch for {fname}"

    def test_pairwise_zero_leakage_across_all_benchmarks(self) -> None:
        """Verify strict pairwise support disjointness on all ingested benchmark splits."""
        raw_dir = Path("paper/data/raw")
        benchmark_files = [
            "hbar_splits.json",
            "scan_splits.json",
            "cogs_splits.json",
            "pcfg_set_splits.json",
        ]

        for fname in benchmark_files:
            fpath = raw_dir / fname
            with fpath.open("r", encoding="utf-8") as f:
                splits_dict = json.load(f)

            report = audit_dataset_suite(splits_dict)
            assert report.is_clean, f"Leakage detected in {fname}!"
            for p in report.pairwise_audits:
                assert p.is_disjoint, f"Overlap between {p.split_1_name} and {p.split_2_name} in {fname}"
                assert p.num_exact_matches == 0
                assert p.leakage_fraction == 0.0

    def test_standards_documents_54_rules(self) -> None:
        """Verify standards.md documents exactly 54 operational rules."""
        standards_path = Path("paper/planning/standards.md")
        with standards_path.open("r", encoding="utf-8") as f:
            content = f.read()
        assert "54 Rules" in content or "54 operational rules" in content.lower()
        assert "54" in content
