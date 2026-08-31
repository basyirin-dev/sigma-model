"""Unit tests for statistical power analysis and Granger causality diagnostics (Paper 02 Task 4.4)."""

from __future__ import annotations

import numpy as np
import pytest
from paper02.src.analysis.analyze_gate import logistic_step_fn
from paper02.src.analysis.power import (
    compute_augmented_dickey_fuller_test,
    compute_bootstrap_threshold_ci,
    compute_clopper_pearson_ci,
    compute_granger_causality_test,
    compute_minimal_detectable_effect_size,
    compute_panel_var_granger_test,
    compute_portmanteau_q_test,
    compute_tost_power,
    compute_var_lag_order_selection,
)

class TestStatisticalPower:
    """Test MDES calculations and TOST statistical power bounds."""

    def test_mdes_sample_size_scaling(self) -> None:
        # For n = 30, alpha = 0.05, power = 0.90 -> MDES around 0.835
        mdes_30 = compute_minimal_detectable_effect_size(n_per_cell=30, alpha=0.05, power=0.90)
        assert pytest.approx(mdes_30, abs=0.05) == 0.835

        # Larger sample size -> smaller detectable effect
        mdes_100 = compute_minimal_detectable_effect_size(n_per_cell=100, alpha=0.05, power=0.90)
        assert mdes_100 < mdes_30

    def test_tost_power_supercritical(self) -> None:
        # High power for margin delta = 2.5 with sigma = 0.5 and n = 30
        power = compute_tost_power(n_per_cell=30, delta=2.5, sigma=0.5, alpha=0.05)
        assert power > 0.95


class TestGrangerCausality:
    """Test Granger causality F-test engine."""

    def test_granger_causal_relationship(self) -> None:
        rng = np.random.default_rng(42)
        n = 100
        # Source signal
        source = rng.normal(size=n)
        # Target signal driven by lag-1 of source: y_t = 0.8 * s_{t-1} + noise
        target = np.zeros(n)
        for t in range(1, n):
            target[t] = 0.8 * source[t - 1] + rng.normal(scale=0.2)

        res = compute_granger_causality_test(source, target, max_lag=1)
        assert res["f_stat"] > 10.0
        assert res["p_value"] < 0.001
        assert res["r2_unrestricted"] > res["r2_restricted"]

    def test_granger_independent_series(self) -> None:
        rng = np.random.default_rng(42)
        n = 100
        source = rng.normal(size=n)
        target = rng.normal(size=n)  # Independent noise

        res = compute_granger_causality_test(source, target, max_lag=1)
        assert res["p_value"] > 0.05


class TestBootstrapThresholdCI:
    """Test non-parametric bootstrap confidence intervals for lambda_crit."""

    def test_bootstrap_threshold_coverage(self) -> None:
        lambda_vals = np.array([0.0, 0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00])
        # True threshold at lambda = 0.25
        escape_fractions = logistic_step_fn(lambda_vals, k=25.0, lambda_crit=0.25)

        low, high = compute_bootstrap_threshold_ci(
            lambda_vals, escape_fractions, n_boot=200, ci=0.95, seed=42
        )
        assert low <= 0.25 <= high
        assert high - low < 0.15


class TestEconometricAndBinomialInference:
    """Test ADF stationarity, VAR lag selection, panel Granger, and Clopper-Pearson CIs."""

    def test_clopper_pearson_exact_bounds(self) -> None:
        # For 30/30 successes (100% late-onset recovery), 95% Clopper-Pearson CI is [0.884, 1.000]
        low, high = compute_clopper_pearson_ci(k_successes=30, n_trials=30, confidence=0.95)
        assert pytest.approx(low, abs=0.01) == 0.884
        assert pytest.approx(high, abs=1e-5) == 1.000

        # Intermediate case: 15/30 successes (50%)
        low_50, high_50 = compute_clopper_pearson_ci(k_successes=15, n_trials=30, confidence=0.95)
        assert low_50 < 0.5 < high_50

    def test_adf_stationarity_raw_vs_differenced(self) -> None:
        rng = np.random.default_rng(42)
        # Raw non-stationary random walk / step-growth: y_t = y_{t-1} + noise
        raw_series = np.cumsum(rng.normal(loc=0.5, scale=0.2, size=100))
        res_raw = compute_augmented_dickey_fuller_test(raw_series, max_lags=1)
        assert not res_raw["is_stationary"]
        assert res_raw["p_value"] > 0.05

        # First-differenced stationary series
        diff_series = np.diff(raw_series)
        res_diff = compute_augmented_dickey_fuller_test(diff_series, max_lags=1)
        assert res_diff["is_stationary"]
        assert res_diff["p_value"] < 0.05

    def test_var_lag_order_selection(self) -> None:
        rng = np.random.default_rng(42)
        n = 120
        source = rng.normal(size=n)
        # Target with true lag-2 dependency: y_t = 0.5 * y_{t-1} + 0.3 * s_{t-2} + eps
        target = np.zeros(n)
        for t in range(2, n):
            target[t] = 0.4 * target[t - 1] + 0.5 * source[t - 2] + rng.normal(scale=0.1)

        res = compute_var_lag_order_selection(source, target, max_lags=4)
        assert res["optimal_lag_aic"] in [1, 2, 3]
        assert "aic_scores" in res
        assert "bic_scores" in res

    def test_panel_var_granger_test(self) -> None:
        rng = np.random.default_rng(42)
        panel_src = []
        panel_tgt = []
        for _ in range(10):
            s = rng.normal(size=80)
            t = np.zeros(80)
            for step in range(2, 80):
                t[step] = 0.3 * t[step - 1] + 0.6 * s[step - 1] + rng.normal(scale=0.2)
            panel_src.append(s)
            panel_tgt.append(t)

        panel_res = compute_panel_var_granger_test(panel_src, panel_tgt, lag_order=2)
        assert panel_res["pooled_f_stat"] > 2.0
        assert panel_res["p_value"] < 0.05
        assert panel_res["delta_r2"] > 0.05
        assert len(panel_res["seed_f_stats"]) == 10

    def test_portmanteau_q_test(self) -> None:
        rng = np.random.default_rng(42)
        white_noise = rng.normal(size=200)
        res = compute_portmanteau_q_test(white_noise, max_lags=10)
        assert res["is_white_noise"]
        assert res["p_value"] > 0.05
