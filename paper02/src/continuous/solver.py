"""Continuous Stiff ODE/SDE Solver Engine for Paper 02 (Task 5.1).

Provides high-precision adaptive integration (atol=1e-8, rtol=1e-8) for the two-subspace
continuous dynamical system, invariant boundary checking, and Jacobian eigenvalue extraction.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np
from scipy.integrate import solve_ivp

from paper02.src.continuous.two_subspace_ode import (
    TwoSubspaceParams,
    TwoSubspaceSystem,
)


@dataclass(frozen=True)
class SolverResult:
    """Numerical integration trajectory and diagnostic summary."""

    t: np.ndarray
    u: np.ndarray
    v: np.ndarray
    mu_perp: float
    is_supercritical: bool
    state_invariants_valid: bool
    final_state: tuple[float, float]


class ContinuousTwoSubspaceSolver:
    """High-precision adaptive integrator for the two-subspace gradient flow."""

    def __init__(
        self,
        params: TwoSubspaceParams | None = None,
        atol: float = 1e-8,
        rtol: float = 1e-8,
        method: str = "Radau",
    ) -> None:
        self.params = params or TwoSubspaceParams()
        self.system = TwoSubspaceSystem(self.params)
        self.atol = atol
        self.rtol = rtol
        self.method = method

    def compute_critical_pressure(self) -> float:
        """Compute the analytical critical pressure threshold lambda_crit = b_C / a_C."""
        return self.system.lambda_crit

    def compute_transverse_eigenvalue(self, lambda_val: float | None = None) -> float:
        """Compute the transverse Jacobian eigenvalue mu_perp = lambda * a_C - b_C."""
        lam = self.params.lambda_val if lambda_val is None else lambda_val
        return lam * self.params.a_C - self.params.b_C

    def solve(
        self,
        initial_state: tuple[float, float] = (0.01, 0.001),
        t_span: tuple[float, float] = (0.0, 50.0),
        t_eval: Sequence[float] | None = None,
    ) -> SolverResult:
        """Integrate continuous gradient flow system with state invariant checks."""
        u0, v0 = initial_state
        if u0 < 0.0 or v0 < 0.0:
            raise ValueError(f"Initial states must be non-negative, got u0={u0}, v0={v0}")

        def rhs(t: float, y: np.ndarray) -> np.ndarray:
            return self.system.vector_field(t, y)

        sol = solve_ivp(
            rhs,
            t_span,
            [u0, v0],
            method=self.method,
            t_eval=t_eval,
            atol=self.atol,
            rtol=self.rtol,
        )

        t_arr = sol.t
        u_arr = sol.y[0]
        v_arr = sol.y[1]

        # Verify state-space invariants: u >= 0, v >= 0, u <= 1.5, v <= 1.5
        invariants_valid = bool(
            np.all(u_arr >= -1e-6)
            and np.all(v_arr >= -1e-6)
            and np.all(u_arr <= 1.5)
            and np.all(v_arr <= 1.5)
        )

        # Clip minimal numerical underflows to 0.0
        u_clean = np.maximum(u_arr, 0.0)
        v_clean = np.maximum(v_arr, 0.0)

        final_u = float(u_clean[-1])
        final_v = float(v_clean[-1])
        mu_p = self.compute_transverse_eigenvalue()

        return SolverResult(
            t=t_arr,
            u=u_clean,
            v=v_clean,
            mu_perp=mu_p,
            is_supercritical=(self.params.lambda_val > self.system.lambda_crit),
            state_invariants_valid=invariants_valid,
            final_state=(final_u, final_v),
        )
