"""Unit tests for Lanczos Hessian spectrum engine (Paper 02 Task 5.3)."""

from __future__ import annotations

import pytest
import torch
import torch.nn as nn

from paper.src.analysis.hessian_lanczos import compute_lanczos_eigenvalues


class SimpleQuadraticModel(nn.Module):
    """Quadratic module with known analytical eigenvalues."""

    def __init__(self, eigs: list[float]) -> None:
        super().__init__()
        self.w = nn.Parameter(torch.zeros(len(eigs)))
        self.register_buffer("A_diag", torch.tensor(eigs, dtype=torch.float32))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return 0.5 * torch.sum(self.A_diag * (self.w**2))


def dummy_loss(out: torch.Tensor, tgt: torch.Tensor) -> torch.Tensor:
    return out


class TestLanczosSpectrum:
    """Test top-k eigenvalue extraction via Lanczos tridiagonalization."""

    def test_lanczos_top_eigenvalues(self) -> None:
        true_eigs = [20.0, 15.0, 10.0, 5.0, 1.0]
        model = SimpleQuadraticModel(true_eigs)

        inputs = torch.empty(0)
        targets = torch.empty(0)

        calc_eigs = compute_lanczos_eigenvalues(
            model, dummy_loss, inputs, targets, num_eigenvalues=3, num_iterations=15
        )

        assert len(calc_eigs) == 3
        # Top eigenvalue should closely match 20.0
        assert pytest.approx(calc_eigs[0], rel=0.05) == 20.0
        # Second eigenvalue should closely match 15.0
        assert pytest.approx(calc_eigs[1], rel=0.10) == 15.0
