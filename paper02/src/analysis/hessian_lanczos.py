"""Lanczos Curvature and Hessian Spectrum Engine for Paper 02 (Task 5.3).

Computes the top-k eigenvalues lambda_1 >= ... >= lambda_k of the loss Hessian via
matrix-free Lanczos iterations with full re-orthogonalization.
"""

from __future__ import annotations

from typing import Callable

import numpy as np
import scipy.linalg
import torch
import torch.nn as nn

from paper02.src.analysis.hessian import compute_hvp


def _dot_product_lists(v1: list[torch.Tensor], v2: list[torch.Tensor]) -> float:
    return float(sum((a * b).sum() for a, b in zip(v1, v2, strict=True)).item())


def compute_lanczos_eigenvalues(
    model: nn.Module,
    loss_fn: Callable[[torch.Tensor, torch.Tensor], torch.Tensor],
    inputs: torch.Tensor,
    targets: torch.Tensor,
    num_eigenvalues: int = 5,
    num_iterations: int = 25,
    seed: int = 42,
) -> np.ndarray:
    """Compute the top-k eigenvalues of the loss Hessian via Lanczos tridiagonalization.

    Args:
        model: PyTorch module.
        loss_fn: Scalar loss function.
        inputs: Input tensor batch.
        targets: Target tensor batch.
        num_eigenvalues: Number of top eigenvalues to return (k).
        num_iterations: Number of Lanczos iterations (m >= k).
        seed: Random seed for initial probe vector.

    Returns:
        1D numpy array of top-k eigenvalues sorted in descending order.
    """
    model.eval()
    params = [p for p in model.parameters() if p.requires_grad]
    if not params:
        return np.zeros(num_eigenvalues)

    torch.manual_seed(seed)
    # Generate initial normalized probe vector v1
    v = [torch.randn_like(p) for p in params]
    norm_v = torch.sqrt(sum(torch.sum(vi**2) for vi in v))
    v = [vi / norm_v for vi in v]

    v_basis: list[list[torch.Tensor]] = [v]
    alpha_list: list[float] = []
    beta_list: list[float] = []

    for _ in range(num_iterations):
        model.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)

        # Matrix-free HVP w = H * v
        w = compute_hvp(loss, params, v)

        # alpha = <w, v>
        alpha = _dot_product_lists(w, v)
        alpha_list.append(alpha)

        # Re-orthogonalize w against all previous basis vectors (Full Re-orthogonalization)
        for v_prev in v_basis:
            proj = _dot_product_lists(w, v_prev)
            w = [wi - proj * vp for wi, vp in zip(w, v_prev, strict=True)]

        # beta = ||w||
        beta = float(torch.sqrt(sum(torch.sum(wi**2) for wi in w)).item())
        if beta < 1e-8:
            break
        beta_list.append(beta)

        v = [wi / beta for wi in w]
        v_basis.append(v)

    # Construct Rayleigh-Ritz / Tridiagonal matrix T
    m = len(alpha_list)
    t_mat = np.diag(alpha_list)
    if len(beta_list) > 0:
        for i, b in enumerate(beta_list[: m - 1]):
            t_mat[i, i + 1] = b
            t_mat[i + 1, i] = b

    # Eigenvalues of symmetric tridiagonal matrix T
    eigs = scipy.linalg.eigvalsh(t_mat)
    sorted_eigs = np.sort(eigs)[::-1]
    return sorted_eigs[:num_eigenvalues]
