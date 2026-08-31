"""Unit tests for the continuous stiff solver engine (Paper 02 Task 5.1)."""

from __future__ import annotations

import pytest

from paper02.src.continuous.solver import ContinuousTwoSubspaceSolver
from paper02.src.continuous.two_subspace_ode import TwoSubspaceParams


class TestContinuousSolver:
    """Test solver accuracy, state invariants, and bifurcation properties."""

    def test_critical_pressure_formula(self) -> None:
        params = TwoSubspaceParams(a_C=2.0, b_C=0.5)
        solver = ContinuousTwoSubspaceSolver(params)
        assert pytest.approx(solver.compute_critical_pressure(), abs=1e-5) == 0.25

    def test_subcritical_trap_convergence(self) -> None:
        # lambda = 0.0 < lambda_crit -> converges to E_S (u=1, v=0)
        params = TwoSubspaceParams(a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, lambda_val=0.0)
        solver = ContinuousTwoSubspaceSolver(params)
        res = solver.solve(initial_state=(0.1, 0.05), t_span=(0.0, 30.0))

        assert res.state_invariants_valid
        assert not res.is_supercritical
        assert pytest.approx(res.final_state[0], abs=1e-2) == 1.0  # u converges to theta_S
        assert pytest.approx(res.final_state[1], abs=1e-3) == 0.0  # v decays to 0

    def test_supercritical_escape_convergence(self) -> None:
        # lambda = 1.0 > lambda_crit (0.5) -> converges to E_C (u < 1, v > 0)
        params = TwoSubspaceParams(
            a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=1.0
        )
        solver = ContinuousTwoSubspaceSolver(params)
        res = solver.solve(initial_state=(0.1, 0.05), t_span=(0.0, 30.0))

        assert res.state_invariants_valid
        assert res.is_supercritical
        assert res.final_state[1] > 0.4  # v activates to (lambda*a_C - b_C)/kappa = 0.5
        assert pytest.approx(res.final_state[1], abs=1e-2) == 0.5

    def test_invalid_initial_state_raises(self) -> None:
        solver = ContinuousTwoSubspaceSolver()
        with pytest.raises(ValueError, match="Initial states must be non-negative"):
            solver.solve(initial_state=(-0.1, 0.5))
