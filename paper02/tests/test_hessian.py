"""Unit tests for loss landscape curvature and Hessian engines (Paper 02 Task 4.2)."""

from __future__ import annotations

import pytest
import torch
import torch.nn as nn

from paper02.src.analysis.hessian import (
    compute_hvp,
    compute_top_hessian_eigenvalue,
    estimate_hessian_trace,
)


class QuadraticModel(nn.Module):
    """Simple linear module where loss Hessian equals a known positive-definite matrix A."""

    def __init__(self, diag_values: list[float]) -> None:
        super().__init__()
        self.w = nn.Parameter(torch.zeros(len(diag_values)))
        self.register_buffer("A_diag", torch.tensor(diag_values, dtype=torch.float32))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Returns 1/2 w^T A w
        return 0.5 * torch.sum(self.A_diag * (self.w**2))


def dummy_loss_fn(outputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    return outputs


class TestHessianAnalysis:
    """Test matrix-free HVP, top eigenvalue power iteration, and trace estimation."""

    def test_hvp_exact_quadratic(self) -> None:
        diag = [10.0, 5.0, 2.0, 1.0]
        model = QuadraticModel(diag)
        inputs = torch.empty(0)

        # Vector v = [1, 1, 1, 1]
        v = [torch.ones(4)]
        loss = model(inputs)
        hvp = compute_hvp(loss, [model.w], v)

        assert len(hvp) == 1
        expected = torch.tensor(diag) * torch.ones(4)
        assert torch.allclose(hvp[0], expected, atol=1e-5)

    def test_top_eigenvalue_power_iteration(self) -> None:
        diag = [12.5, 6.0, 3.0, 0.5]
        model = QuadraticModel(diag)
        inputs = torch.empty(0)
        targets = torch.empty(0)

        top_eig = compute_top_hessian_eigenvalue(
            model, dummy_loss_fn, inputs, targets, max_iter=40, tol=1e-5
        )

        assert pytest.approx(top_eig, rel=1e-3) == 12.5

    def test_trace_estimation_hutchinson(self) -> None:
        diag = [10.0, 4.0, 2.0, 1.0]
        true_trace = sum(diag)  # 17.0
        model = QuadraticModel(diag)
        inputs = torch.empty(0)
        targets = torch.empty(0)

        # Hutchinson estimator with 100 Rademacher samples
        est_trace = estimate_hessian_trace(
            model, dummy_loss_fn, inputs, targets, num_samples=100, seed=42
        )

        assert pytest.approx(est_trace, rel=0.15) == true_trace
