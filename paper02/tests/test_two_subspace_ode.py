"""Unit tests for the Two-Subspace Continuous Gradient Flow System (Paper 02)."""

from __future__ import annotations

import numpy as np
import pytest

from paper02.src.continuous.two_subspace_ode import (
    TwoSubspaceParams,
    TwoSubspaceSystem,
)


class TestTwoSubspaceParams:
    """Test parameter domain constraints and validation."""

    def test_default_parameters(self) -> None:
        params = TwoSubspaceParams()
        assert params.a_S == 1.0
        assert params.theta_S == 1.0
        assert params.b_S == 0.5
        assert params.a_C == 1.0
        assert params.b_C == 0.5
        assert params.kappa == 1.0
        assert params.lambda_val == 0.0

    @pytest.mark.parametrize(
        ("kwargs", "expected_err"),
        [
            ({"a_S": 0.0}, "a_S must be positive"),
            ({"theta_S": -1.0}, "theta_S must be positive"),
            ({"b_S": -0.1}, "b_S must be non-negative"),
            ({"a_C": 0.0}, "a_C must be positive"),
            ({"b_C": -0.5}, "b_C must be positive"),
            ({"kappa": 0.0}, "kappa must be positive"),
            ({"lambda_val": -0.2}, "lambda_val must be non-negative"),
        ],
    )
    def test_invalid_parameters_raise(self, kwargs: dict[str, float], expected_err: str) -> None:
        with pytest.raises(ValueError, match=expected_err):
            TwoSubspaceParams(**kwargs)


class TestTwoSubspaceDynamics:
    """Test theoretical invariants, fixed points, and bifurcations."""

    def test_critical_threshold_and_spectrum(self) -> None:
        params = TwoSubspaceParams(a_C=2.0, b_C=0.8)
        sys = TwoSubspaceSystem(params)
        assert np.isclose(sys.lambda_crit, 0.4)

        # Subcritical
        sys_sub = TwoSubspaceSystem(TwoSubspaceParams(a_C=2.0, b_C=0.8, lambda_val=0.2))
        assert sys_sub.mu_perp < 0.0
        assert sys_sub.mu_parallel < 0.0

        # Critical
        sys_crit = TwoSubspaceSystem(TwoSubspaceParams(a_C=2.0, b_C=0.8, lambda_val=0.4))
        assert np.isclose(sys_crit.mu_perp, 0.0)

        # Supercritical
        sys_super = TwoSubspaceSystem(TwoSubspaceParams(a_C=2.0, b_C=0.8, lambda_val=0.8))
        assert sys_super.mu_perp > 0.0

    def test_subcritical_stability_exchange(self) -> None:
        # lambda = 0.2 < lambda_crit = 0.5
        params = TwoSubspaceParams(
            a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, lambda_val=0.2
        )
        sys = TwoSubspaceSystem(params)
        es, ec = sys.fixed_points()

        # E_S should be stable
        assert es.is_physical
        assert es.is_stable
        assert np.isclose(es.u, 1.0 / (1.0 + 0.2 * 0.5))
        assert es.v == 0.0
        assert es.mu_perp < 0.0

        # E_C should be unphysical (v < 0) and unstable
        assert not ec.is_physical
        assert not ec.is_stable
        assert ec.v < 0.0

    def test_supercritical_stability_exchange(self) -> None:
        # lambda = 1.0 > lambda_crit = 0.5
        params = TwoSubspaceParams(
            a_S=1.0,
            theta_S=1.0,
            b_S=0.5,
            a_C=1.0,
            b_C=0.5,
            kappa=1.0,
            lambda_val=1.0,
        )
        sys = TwoSubspaceSystem(params)
        es, ec = sys.fixed_points()

        # E_S should be unstable saddle
        assert es.is_physical
        assert not es.is_stable
        assert es.mu_perp > 0.0

        # E_C should be physical and asymptotically stable
        assert ec.is_physical
        assert ec.is_stable
        expected_v = (1.0 * 1.0 - 0.5) / 1.0  # (lambda*a_C - b_C)/kappa = 0.5
        assert np.isclose(ec.v, expected_v)
        assert ec.mu_perp < 0.0  # Stable transverse eigenvalue at E_C

    def test_vector_field_at_fixed_points(self) -> None:
        params = TwoSubspaceParams(
            a_S=1.0,
            theta_S=1.0,
            b_S=0.5,
            a_C=1.0,
            b_C=0.5,
            kappa=1.0,
            lambda_val=1.0,
        )
        sys = TwoSubspaceSystem(params)
        es, ec = sys.fixed_points()

        vf_es = sys.vector_field(0.0, (es.u, es.v))
        assert np.allclose(vf_es, [0.0, 0.0], atol=1e-12)

        vf_ec = sys.vector_field(0.0, (ec.u, ec.v))
        assert np.allclose(vf_ec, [0.0, 0.0], atol=1e-12)


class TestAnalyticalVsNumericalIntegration:
    """Test that analytical closed-form solutions match numerical Runge-Kutta integration."""

    @pytest.mark.parametrize("l_val", [0.2, 0.5, 1.2])
    def test_trajectory_accuracy(self, l_val: float) -> None:
        params = TwoSubspaceParams(
            a_S=1.2, theta_S=0.8, b_S=0.4, a_C=1.5, b_C=0.75, kappa=1.2, lambda_val=l_val
        )
        sys = TwoSubspaceSystem(params)

        t_span = (0.0, 20.0)
        t_eval = np.linspace(0.0, 20.0, 200)
        u0, v0 = 0.2, 0.1

        # Numerical integration
        t_num, u_num, v_num = sys.numerical_solution(t_span, u0, v0, t_eval=t_eval)

        # Analytical integration
        u_ana, v_ana = sys.analytical_solution(t_eval, u0, v0)

        # Check maximal absolute error between analytical and numerical ODE integration
        err_u = np.max(np.abs(u_num - u_ana))
        err_v = np.max(np.abs(v_num - v_ana))

        assert err_u < 1e-6, f"u error too high: {err_u}"
        assert err_v < 1e-6, f"v error too high: {err_v}"

    def test_critical_algebraic_decay(self) -> None:
        # At lambda = lambda_crit, dv/dt = -kappa * v^2 => v(t) = v0 / (1 + kappa * v0 * t)
        params = TwoSubspaceParams(a_C=1.0, b_C=0.5, kappa=2.0, lambda_val=0.5)
        sys = TwoSubspaceSystem(params)
        assert np.isclose(sys.mu_perp, 0.0)

        t_eval = np.array([1.0, 5.0, 10.0, 50.0])
        v0 = 0.5
        _, v_ana = sys.analytical_solution(t_eval, 1.0, v0)

        expected_v = v0 / (1.0 + 2.0 * v0 * t_eval)
        assert np.allclose(v_ana, expected_v, atol=1e-12)


class TestEscapeTime:
    """Test escape time formula and critical divergence."""

    def test_subcritical_escape_time_is_none(self) -> None:
        params = TwoSubspaceParams(a_C=1.0, b_C=0.5, lambda_val=0.3)  # lambda < 0.5
        sys = TwoSubspaceSystem(params)
        assert sys.escape_time(v0=0.01) is None

    def test_supercritical_escape_time_matches_simulation(self) -> None:
        params = TwoSubspaceParams(a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=1.0)
        sys = TwoSubspaceSystem(params)

        v0 = 0.02
        alpha = 0.9
        t_esc = sys.escape_time(v0=v0, alpha=alpha)
        assert t_esc is not None
        assert t_esc > 0

        # Evaluate analytical trajectory at t_esc
        _, v_at_tesc = sys.analytical_solution(np.array([t_esc]), u0=0.5, v0=v0)
        _, ec = sys.fixed_points()
        assert np.isclose(v_at_tesc[0], alpha * ec.v, rtol=1e-4)

    def test_critical_slowing_down_divergence(self) -> None:
        # As lambda -> lambda_crit from above, escape time must diverge to infinity
        times = []
        for delta in [0.5, 0.2, 0.08, 0.03]:
            params = TwoSubspaceParams(a_C=1.0, b_C=0.5, lambda_val=0.5 + delta)
            sys = TwoSubspaceSystem(params)
            t_esc = sys.escape_time(v0=1e-4, alpha=0.9)
            assert t_esc is not None
            times.append(t_esc)

        # Monotonically increasing escape times as delta -> 0
        assert all(t1 < t2 for t1, t2 in zip(times, times[1:], strict=False))
