"""Loss Landscape Curvature and Hessian Analysis Engine for Paper 02.

This module implements matrix-free Hessian-Vector Product (HVP) power iteration
and stochastic Hutchinson trace estimators to track curvature and Edge-of-Stability
dynamics under the Two-Subspace Law.
"""

from __future__ import annotations

from typing import Callable

import torch
import torch.nn as nn


def compute_hvp(
    loss: torch.Tensor,
    params: list[torch.Tensor],
    v: list[torch.Tensor],
) -> list[torch.Tensor]:
    """Compute exact matrix-free Hessian-Vector Product H * v via double backward."""
    grads = torch.autograd.grad(loss, params, create_graph=True, retain_graph=True)
    grad_dot_v = sum((g * vi).sum() for g, vi in zip(grads, v, strict=True))
    hvp_list = torch.autograd.grad(grad_dot_v, params, retain_graph=True)
    return [h.detach() for h in hvp_list]


def _normalize_vector_list(v_list: list[torch.Tensor]) -> tuple[list[torch.Tensor], float]:
    """Normalize a list of tensors as a single flattened vector."""
    norm_sq = sum(torch.sum(v**2) for v in v_list)
    norm = float(torch.sqrt(norm_sq).item())
    if norm < 1e-12:
        return v_list, 0.0
    return [v / norm for v in v_list], norm


def compute_top_hessian_eigenvalue(
    model: nn.Module,
    loss_fn: Callable[[torch.Tensor, torch.Tensor], torch.Tensor],
    inputs: torch.Tensor,
    targets: torch.Tensor,
    max_iter: int = 50,
    tol: float = 1e-4,
    seed: int = 42,
) -> float:
    """Compute the top Hessian eigenvalue (spectral sharpness) via Power Iteration.

    Args:
        model: PyTorch neural network module.
        loss_fn: Loss function mapping (outputs, targets) -> scalar loss.
        inputs: Model input batch tensor.
        targets: Target label batch tensor.
        max_iter: Maximum power iteration steps.
        tol: Convergence tolerance for eigenvalue change.
        seed: Random seed for initial random vector.

    Returns:
        Top eigenvalue lambda_max(H) of the loss Hessian.
    """
    model.eval()
    params = [p for p in model.parameters() if p.requires_grad]
    if not params:
        return 0.0

    # Initialize random vector
    torch.manual_seed(seed)
    v = [torch.randn_like(p) for p in params]
    v, _ = _normalize_vector_list(v)

    current_lambda = 0.0

    for _ in range(max_iter):
        model.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)

        hvp_list = compute_hvp(loss, params, v)
        rayleigh_quotient = float(
            sum((h * vi).sum() for h, vi in zip(hvp_list, v, strict=True)).item()
        )

        v_next, _ = _normalize_vector_list(hvp_list)
        if abs(rayleigh_quotient - current_lambda) < tol * max(abs(current_lambda), 1.0):
            current_lambda = rayleigh_quotient
            break

        current_lambda = rayleigh_quotient
        v = v_next

    return float(current_lambda)


def estimate_hessian_trace(
    model: nn.Module,
    loss_fn: Callable[[torch.Tensor, torch.Tensor], torch.Tensor],
    inputs: torch.Tensor,
    targets: torch.Tensor,
    num_samples: int = 20,
    seed: int = 42,
) -> float:
    """Estimate the trace of the loss Hessian using the stochastic Hutchinson method.

    Tr(H) = E_{z ~ Rademacher} [z^T H z]

    Args:
        model: PyTorch neural network module.
        loss_fn: Loss function.
        inputs: Model input tensor.
        targets: Target labels.
        num_samples: Number of Rademacher probe samples.
        seed: Random seed.

    Returns:
        Estimated scalar trace of the Hessian Tr(H).
    """
    model.eval()
    params = [p for p in model.parameters() if p.requires_grad]
    if not params:
        return 0.0

    torch.manual_seed(seed)
    trace_estimates: list[float] = []

    for _ in range(num_samples):
        # Generate Rademacher vector (+1 or -1 with probability 0.5)
        z = [torch.randint(0, 2, p.shape, device=p.device, dtype=p.dtype) * 2.0 - 1.0 for p in params]

        model.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)

        hvp_list = compute_hvp(loss, params, z)
        z_h_z = sum((zi * hi).sum() for zi, hi in zip(z, hvp_list, strict=True))
        trace_estimates.append(float(z_h_z.item()))

    return float(sum(trace_estimates) / len(trace_estimates))
