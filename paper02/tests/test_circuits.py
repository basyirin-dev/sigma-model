"""Unit tests for mechanistic circuit diagnostics and subspace attribution (Paper 02 Task 4.2)."""

from __future__ import annotations

import numpy as np
import pytest

from paper02.src.analysis.circuits import (
    compute_head_schema_specialization,
    decompose_residual_stream,
    project_to_subspace,
)


class TestCircuitDiagnostics:
    """Test subspace projections, residual stream decomposition, and head specialization."""

    def test_subspace_projection_idempotence(self) -> None:
        rng = np.random.default_rng(42)
        activations = rng.normal(size=(20, 16))
        basis = rng.normal(size=(16, 4))

        proj_1 = project_to_subspace(activations, basis)
        proj_2 = project_to_subspace(proj_1, basis)

        assert np.allclose(proj_1, proj_2, atol=1e-5)

    def test_residual_stream_orthogonal_decomposition(self) -> None:
        # Construct orthogonal ambient space R^8 with shortcut spanned by e1..e2 and schema by e3..e4
        basis_s = np.eye(8)[:, :2]
        basis_c = np.eye(8)[:, 2:4]

        # Vector x = 2*e1 + 3*e3 + 5*e7
        activations = np.zeros((1, 8))
        activations[0, 0] = 2.0  # Shortcut
        activations[0, 2] = 3.0  # Schema
        activations[0, 6] = 5.0  # Orthogonal residual

        decomp = decompose_residual_stream(activations, basis_s, basis_c)

        assert np.allclose(decomp["shortcut_component"][0, :2], [2.0, 0.0])
        assert np.allclose(decomp["schema_component"][0, 2:4], [3.0, 0.0])
        assert np.allclose(decomp["residual_component"][0, 6], 5.0)
        assert pytest.approx(decomp["energy_fraction_shortcut"], abs=1e-4) == (4.0 / (4.0 + 9.0 + 25.0))
        assert pytest.approx(decomp["energy_fraction_schema"], abs=1e-4) == (9.0 / (4.0 + 9.0 + 25.0))

    def test_head_schema_specialization(self) -> None:
        basis_s = np.eye(8)[:, :2]
        basis_c = np.eye(8)[:, 2:4]

        # Schema-specialized head activations (dominated by e3, e4)
        schema_head = np.zeros((10, 8))
        schema_head[:, 2] = 5.0
        schema_head[:, 3] = 4.0
        schema_head[:, 0] = 0.1  # Minimal shortcut leakage

        score = compute_head_schema_specialization(schema_head, basis_s, basis_c)
        assert score > 100.0  # High schema specialization
