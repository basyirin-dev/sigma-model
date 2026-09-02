"""Unit tests for the mechanism-gate statistical analysis engine (Paper 02)."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import numpy as np
import pytest

from paper.src.analysis.analyze_gate import (
    compute_bootstrap_ci,
    compute_gate_verdict,
    compute_tost_equivalence,
    emit_gate_result_markdown,
    evaluate_gate_results,
    fit_logistic_separatrix,
    generate_gate_summary_table,
    logistic_step_fn,
    plot_gate_diagnostics,
)


class TestLogisticSeparatrixFit:
    """Test non-linear change-point logistic fitting."""

    def test_sharp_supercritical_step_fit(self) -> None:
        lambda_vals = np.array([0.0, 0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00])
        # Sharp step function at lambda_crit = 0.25 with k = 30.0
        synthetic_escapes = logistic_step_fn(lambda_vals, k=30.0, lambda_crit=0.25)

        k_fit, lam_crit_fit, r2 = fit_logistic_separatrix(lambda_vals, synthetic_escapes)

        assert k_fit >= 15.0, f"Expected steepness k >= 15.0, got {k_fit}"
        assert pytest.approx(lam_crit_fit, abs=0.05) == 0.25
        assert r2 > 0.95

    def test_smooth_dose_response_fails_steepness(self) -> None:
        lambda_vals = np.array([0.0, 0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00])
        # Smooth gradual dose-response with k = 3.0
        synthetic_escapes = logistic_step_fn(lambda_vals, k=3.0, lambda_crit=0.50)

        k_fit, lam_crit_fit, r2 = fit_logistic_separatrix(lambda_vals, synthetic_escapes)

        assert k_fit < 10.0, f"Expected smooth k < 10.0, got {k_fit}"


class TestTOSTEquivalence:
    """Test Two One-Sided Tests (TOST) equivalence testing."""

    def test_equivalent_supercritical_samples(self) -> None:
        rng = np.random.default_rng(42)
        s1 = rng.normal(loc=95.0, scale=0.5, size=30)
        s2 = rng.normal(loc=95.1, scale=0.5, size=30)

        is_equiv, p_low, p_up = compute_tost_equivalence(s1, s2, delta=2.5, alpha=0.05)
        assert is_equiv
        assert p_low < 0.05
        assert p_up < 0.05

    def test_non_equivalent_samples(self) -> None:
        rng = np.random.default_rng(42)
        s1 = rng.normal(loc=95.0, scale=1.0, size=30)
        s2 = rng.normal(loc=85.0, scale=1.0, size=30)

        is_equiv, _, _ = compute_tost_equivalence(s1, s2, delta=2.5, alpha=0.05)
        assert not is_equiv


class TestBootstrapCI:
    """Test bootstrap confidence interval estimation."""

    def test_bootstrap_coverage(self) -> None:
        rng = np.random.default_rng(42)
        data = rng.normal(loc=50.0, scale=2.0, size=100)
        low, high = compute_bootstrap_ci(data, num_bootstrap=1000, ci=0.95, seed=42)

        assert low < 50.0 < high
        assert high - low < 2.0


def _make_arm_a_runs(n_seeds: int = 5) -> list[dict]:
    """Arm A runs: subcritical cells trapped (OOD ~ 2%), supercritical escaped (OOD >= 95%)."""
    runs = []
    lambdas = [0.0, 0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00]
    for lam in lambdas:
        for s in range(n_seeds):
            is_super = lam >= 0.30
            ood_acc = 95.0 + s * 0.5 if is_super else 2.0 + s * 0.5
            runs.append(
                {
                    "config": {
                        "condition_type": "arm_a_lambda",
                        "condition_name": f"arm_a_lambda_{lam:.2f}",
                        "lambda_val": lam,
                        "run_id": s,
                    },
                    "metrics": {
                        "step": [0, 25, 50],
                        "acc_ood": [0.0, ood_acc / 2, ood_acc],
                    },
                    "final": {
                        "acc_id": 99.0,
                        "acc_ood": ood_acc,
                        "escaped": ood_acc >= 80.0,
                    },
                }
            )
    return runs


def _make_arm_b_runs(
    n_seeds: int = 5,
    acc_at_1000: float = 40.0,
    final_ood: float = 94.0,
    t_ints: list[int] | None = None,
) -> list[dict]:
    """Arm B runs with a logged step-1000 accuracy (default: trapped, Acc_OOD <= 50%)."""
    runs = []
    for t_int in t_ints or [0, 100, 250, 500, 1000]:
        for s in range(n_seeds):
            runs.append(
                {
                    "config": {
                        "condition_type": "arm_b_late_intervention",
                        "condition_name": f"arm_b_tint_{t_int}",
                        "lambda_val": 1.0,
                        "intervention_step": t_int,
                        "run_id": s,
                    },
                    "metrics": {
                        "step": [0, 1000, 2000],
                        "acc_ood": [20.0, acc_at_1000, final_ood],
                    },
                    "final": {
                        "acc_id": 99.0,
                        "acc_ood": final_ood,
                        "escaped": final_ood >= 80.0,
                    },
                }
            )
    return runs


class TestGateEvaluationPipeline:
    """Test end-to-end gate evaluation, summary table, markdown emission, and plotting."""

    @pytest.fixture
    def mock_gate_results(self) -> list[dict]:
        return _make_arm_a_runs() + _make_arm_b_runs()

    def test_gate_evaluation_and_outputs(self, mock_gate_results: list[dict]) -> None:
        eval_res = evaluate_gate_results(mock_gate_results)
        assert eval_res["verdict"] == "PASS"
        assert eval_res["criterion_1"]["pass"]
        assert eval_res["criterion_2"]["pass"]

        summary_df = generate_gate_summary_table(mock_gate_results)
        assert len(summary_df) == 15  # 10 Arm A + 5 Arm B
        assert "Condition" in summary_df.columns
        assert "Mean OOD ± Std" in summary_df.columns

        temp_dir = tempfile.mkdtemp()
        try:
            md_path = Path(temp_dir) / "gate-result.md"
            fig_path = Path(temp_dir) / "gate_diagnostic.png"

            emit_gate_result_markdown(eval_res, summary_df, output_path=md_path)
            assert md_path.exists()
            assert "PASS" in md_path.read_text(encoding="utf-8")

            plot_gate_diagnostics(eval_res, mock_gate_results, output_figure_path=fig_path)
            assert fig_path.exists()
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_criterion2_excludes_untrapped_runs(self) -> None:
        # t_int = 1000 runs NOT trapped at step 1000 (Acc_OOD > 50%) are excluded from
        # the pre-registered population (preregistration.md section 2).
        runs = _make_arm_a_runs() + _make_arm_b_runs(acc_at_1000=80.0)
        eval_res = evaluate_gate_results(runs)
        assert eval_res["criterion_2"]["trapped_count"] == 0
        assert eval_res["criterion_2"]["excluded_count"] == 5
        assert not eval_res["criterion_2"]["pass"]
        assert eval_res["verdict"] == "FAIL"

    def test_verdict_requires_criterion3(self) -> None:
        # C1 and C2 pass, but the lambda=2.0 supercritical cell sits ~4 pp off the
        # others -> TOST fails -> secondary consistency unmet -> verdict FAIL
        # (preregistration.md section 5 decision_rule).
        runs = _make_arm_a_runs()
        for r in runs:
            if r["config"]["lambda_val"] == 2.0:
                r["final"]["acc_ood"] -= 4.0
        runs += _make_arm_b_runs()
        eval_res = evaluate_gate_results(runs)
        assert eval_res["criterion_1"]["pass"]
        assert eval_res["criterion_2"]["pass"]
        assert not eval_res["criterion_3"]["pass"]
        assert eval_res["verdict"] == "FAIL"

    def test_verdict_inconclusive_ambiguity_band(self) -> None:
        # Preregistration.md section 5: INCONCLUSIVE only when k in [10, 15) AND
        # >= 1 separation inequality violated by < 2 SE.
        assert compute_gate_verdict(True, True, True, 20.0, 0.0, 0.0) == "PASS"
        assert compute_gate_verdict(True, True, False, 20.0, 0.0, 0.0) == "FAIL"
        assert compute_gate_verdict(False, True, True, 12.0, 0.02, 0.0466) == "INCONCLUSIVE"
        assert compute_gate_verdict(False, True, True, 12.0, 0.5, 0.0466) == "FAIL"
        assert compute_gate_verdict(False, True, True, 12.0, 0.0, 0.0) == "FAIL"
        assert compute_gate_verdict(False, True, True, 9.0, 0.02, 0.0466) == "FAIL"
