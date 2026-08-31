"""Unit tests for the 301-point continuous flow grid simulation (Paper 02 Task 6.1)."""

from __future__ import annotations

import pandas as pd

from paper02.src.continuous.simulate_continuous_grid import run_continuous_grid_simulation


class TestContinuousGridSimulation:
    """Test continuous parameter sweep, bifurcation separatrix extraction, and CSV generation."""

    def test_grid_simulation_mini(self, tmp_path) -> None:
        raw_dir = tmp_path / "raw"
        proc_dir = tmp_path / "processed"

        summary = run_continuous_grid_simulation(
            lambda_range=(0.0, 0.5),
            delta_lambda=0.1,  # 6 lambda points
            initial_conditions=[(0.1, 0.01), (0.5, 0.05)],  # 2 ICs
            output_dir_raw=raw_dir,
            output_dir_processed=proc_dir,
        )

        assert summary.num_lambda_points == 6
        assert summary.num_trajectories == 12  # 6 * 2
        assert summary.lambda_crit_analytical == 0.5

        # Check raw CSV
        df_grid = pd.read_csv(summary.output_grid_path)
        assert len(df_grid) == 12
        assert "lambda" in df_grid.columns
        assert "final_u" in df_grid.columns
        assert "final_v" in df_grid.columns

        # Check separatrix CSV
        df_sep = pd.read_csv(summary.output_separatrix_path)
        assert len(df_sep) == 6
        assert "is_supercritical" in df_sep.columns
