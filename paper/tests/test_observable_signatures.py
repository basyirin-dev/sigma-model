from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from paper.src.continuous.observable_signatures import (
    generate_observable_signatures_figure,
    simulate_escape_probability,
    simulate_late_onset_destabilization,
    simulate_rate_ordering,
)
from paper.src.continuous.two_subspace_ode import TwoSubspaceParams


class TestObservableSignatures:
    """Test verification of empirical bifurcation signatures."""

    def test_signature1_escape_probability_separatrix(self) -> None:
        params_base = TwoSubspaceParams(
            a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=0.0
        )
        lambda_crit = 0.5

        lambdas = np.array([0.2, 0.35, 0.45, 0.55, 0.7, 1.0])
        _, p_escape = simulate_escape_probability(
            params_base,
            lambdas,
            n_seeds=20,
            v0_mean=1e-3,
            v0_std=1e-4,
            t_max=200.0,
            coherence_threshold=0.03,
        )

        # Strictly 0 below lambda_crit, strictly 1 above lambda_crit
        sub_mask = lambdas < lambda_crit
        super_mask = lambdas > lambda_crit

        assert np.all(p_escape[sub_mask] == 0.0), f"Subcritical escape probability non-zero: {p_escape[sub_mask]}"
        assert np.all(p_escape[super_mask] == 1.0), f"Supercritical escape probability not unity: {p_escape[super_mask]}"

    def test_signature2_late_onset_destabilization(self) -> None:
        params_base = TwoSubspaceParams(
            a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=0.0
        )
        t_switch = 40.0
        t_all, u_all, v_all, t_sw = simulate_late_onset_destabilization(
            params_base,
            lambda_pre=0.2,
            lambda_post=1.0,
            t_switch=t_switch,
            t_total=90.0,
            u0=0.5,
            v0=0.1,
        )

        # Phase 1: at t_switch, v should be decaying toward 0
        pre_indices = t_all < t_switch
        v_pre = v_all[pre_indices]
        assert v_pre[-1] < 1e-3

        # Phase 2: at t_total, v should escape to v* = (1.0 * 1.0 - 0.5) / 1.0 = 0.5
        v_post_final = v_all[-1]
        assert np.isclose(v_post_final, 0.5, atol=1e-3)

        # u should adapt from u_pre* = 1.0/(1.0 + 0.2*0.5) to u_post* = 1.0/(1.0 + 1.0*0.5) = 0.6667
        assert np.isclose(u_all[-1], 2.0 / 3.0, atol=1e-3)

    def test_signature3_rate_ordering_power_law(self) -> None:
        params_base = TwoSubspaceParams(
            a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=0.0
        )
        deltas = np.array([0.02, 0.05, 0.1, 0.2, 0.5])
        _, tau_vals = simulate_rate_ordering(params_base, deltas, v0=1e-4, alpha=0.9)

        # Strict monotonic decrease: larger delta => shorter escape time
        assert all(t1 > t2 for t1, t2 in zip(tau_vals, tau_vals[1:], strict=False))

        # Check log-log slope ~ -1.0
        log_deltas = np.log(deltas)
        log_taus = np.log(tau_vals)
        slope, _ = np.polyfit(log_deltas, log_taus, 1)

        # Power law exponent must be approximately -1 (within +/- 0.15)
        assert -1.15 <= slope <= -0.85, f"Unexpected scaling exponent: {slope}"

    def test_figure_generation(self, tmp_path: Path) -> None:
        save_file = tmp_path / "test_signatures.png"
        fig = generate_observable_signatures_figure(save_path=save_file)
        assert fig is not None
        assert save_file.exists()
        plt.close(fig)
