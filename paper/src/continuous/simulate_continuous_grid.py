"""Dense 301-Point Continuous Flow Grid Simulation Engine for Paper 02 (Task 6.1).

Integrates the two-subspace continuous dynamical system across lambda in [0.0, 3.0] (Delta lambda = 0.01)
across multiple initial conditions (u0, v0), computing fixed points, Jacobian eigenvalues,
and the theoretical unstable manifold (separatrix).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np
import pandas as pd

from paper.src.continuous.solver import ContinuousTwoSubspaceSolver
from paper.src.continuous.two_subspace_ode import TwoSubspaceParams


@dataclass(frozen=True)
class GridSimulationSummary:
    """Summary metrics from continuous grid integration."""

    num_lambda_points: int
    num_trajectories: int
    lambda_crit_analytical: float
    bifurcation_point: float
    output_grid_path: str
    output_separatrix_path: str


def run_continuous_grid_simulation(
    lambda_range: tuple[float, float] = (0.0, 3.0),
    delta_lambda: float = 0.01,
    initial_conditions: Sequence[tuple[float, float]] | None = None,
    output_dir_raw: str | Path = "paper/data/raw",
    output_dir_processed: str | Path = "paper/data/processed",
) -> GridSimulationSummary:
    """Run dense continuous parameter sweep and generate raw/processed grid datasets."""
    raw_dir = Path(output_dir_raw)
    processed_dir = Path(output_dir_processed)
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    if initial_conditions is None:
        # Default 5 representative initial conditions in [0.01, 0.99]^2
        initial_conditions = [
            (0.1, 0.01),
            (0.5, 0.01),
            (0.8, 0.1),
            (0.05, 0.2),
            (0.3, 0.3),
        ]

    min_lam, max_lam = lambda_range
    num_points = int(round((max_lam - min_lam) / delta_lambda)) + 1
    lambda_grid = np.linspace(min_lam, max_lam, num_points)

    grid_rows: list[dict[str, float | int | bool]] = []
    separatrix_rows: list[dict[str, float]] = []

    base_params = TwoSubspaceParams(a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0)
    lam_crit = base_params.b_C / base_params.a_C

    for lam_val in lambda_grid:
        p = TwoSubspaceParams(
            a_S=base_params.a_S,
            theta_S=base_params.theta_S,
            b_S=base_params.b_S,
            a_C=base_params.a_C,
            b_C=base_params.b_C,
            kappa=base_params.kappa,
            lambda_val=float(lam_val),
        )
        solver = ContinuousTwoSubspaceSolver(p, method="RK45", atol=1e-6, rtol=1e-6)
        mu_p = solver.compute_transverse_eigenvalue()

        # Fixed point coordinates
        u_star_s = p.a_S * p.theta_S / (p.a_S + p.lambda_val * p.b_S)
        v_star_s = 0.0

        if lam_val > lam_crit:
            u_star_c = u_star_s
            v_star_c = (lam_val * p.a_C - p.b_C) / p.kappa
        else:
            u_star_c = u_star_s
            v_star_c = 0.0

        # Save separatrix / bifurcation trajectory point
        separatrix_rows.append(
            {
                "lambda": float(lam_val),
                "mu_perp": float(mu_p),
                "u_star_shortcut": float(u_star_s),
                "v_star_shortcut": float(v_star_s),
                "u_star_schema": float(u_star_c),
                "v_star_schema": float(v_star_c),
                "is_supercritical": bool(lam_val > lam_crit),
            }
        )

        for idx, (u0, v0) in enumerate(initial_conditions):
            res = solver.solve(initial_state=(u0, v0), t_span=(0.0, 20.0))
            grid_rows.append(
                {
                    "lambda": float(lam_val),
                    "ic_index": idx,
                    "u0": float(u0),
                    "v0": float(v0),
                    "final_u": res.final_state[0],
                    "final_v": res.final_state[1],
                    "mu_perp": float(mu_p),
                    "is_supercritical": res.is_supercritical,
                    "invariants_valid": res.state_invariants_valid,
                }
            )

    df_grid = pd.DataFrame(grid_rows)
    df_separatrix = pd.DataFrame(separatrix_rows)

    grid_path = raw_dir / "continuous_flow_grid.csv"
    separatrix_path = processed_dir / "theoretical_separatrix.csv"

    df_grid.to_csv(grid_path, index=False)
    df_separatrix.to_csv(separatrix_path, index=False)

    return GridSimulationSummary(
        num_lambda_points=len(lambda_grid),
        num_trajectories=len(df_grid),
        lambda_crit_analytical=float(lam_crit),
        bifurcation_point=float(lam_crit),
        output_grid_path=str(grid_path),
        output_separatrix_path=str(separatrix_path),
    )


if __name__ == "__main__":
    summary = run_continuous_grid_simulation()
    print(f"✅ Continuous grid simulation complete: {summary.num_trajectories} trajectories computed.")
