"""Subspace-Projected (Whitened) Gradient Cosine Alignment (GCA) Engine for Paper 02 (Task 5.3).

Eliminates the step-0 ~0.95 initialization artifact in neural sequence models by
projecting out the shared token embedding parameter subspace P_emb:
    g_A^proj(t) = CosSim((I - P_emb) grad_theta L_comp, (I - P_emb) grad_theta L_train)
"""

from __future__ import annotations

import torch
import torch.nn as nn


def compute_flattened_gradients(
    loss: torch.Tensor,
    model: nn.Module,
    exclude_embedding: bool = False,
) -> torch.Tensor:
    """Compute and flatten model parameter gradients, optionally excluding embedding parameters.

    Args:
        loss: Scalar loss tensor.
        model: PyTorch neural network.
        exclude_embedding: If True, zeroes out / skips parameters associated with token embeddings.

    Returns:
        1D gradient tensor of shape (d_param_selected,).
    """
    model.zero_grad()
    grads = torch.autograd.grad(loss, [p for p in model.parameters() if p.requires_grad], retain_graph=True)

    grad_list: list[torch.Tensor] = []
    for (name, _), g in zip(model.named_parameters(), grads, strict=True):
        if exclude_embedding and ("embedding" in name.lower() or "emb" in name.lower()):
            continue
        grad_list.append(g.detach().reshape(-1))

    if not grad_list:
        return torch.zeros(1, device=loss.device)

    return torch.cat(grad_list)


def compute_whitened_gca(
    model: nn.Module,
    loss_train: torch.Tensor,
    loss_comp: torch.Tensor,
) -> dict[str, float]:
    """Compute raw GCA and subspace-projected (whitened) GCA between task and compositional gradients.

    Args:
        model: PyTorch sequence model.
        loss_train: Scalar task cross-entropy loss.
        loss_comp: Scalar compositional substitution loss.

    Returns:
        Dictionary with:
            - 'raw_gca': Cosine similarity across all model parameters.
            - 'whitened_gca': Subspace-projected cosine similarity excluding embedding layers.
    """
    # Raw GCA across all parameters
    grad_train_raw = compute_flattened_gradients(loss_train, model, exclude_embedding=False)
    grad_comp_raw = compute_flattened_gradients(loss_comp, model, exclude_embedding=False)

    norm_tr_raw = float(torch.linalg.norm(grad_train_raw).item() + 1e-10)
    norm_cp_raw = float(torch.linalg.norm(grad_comp_raw).item() + 1e-10)
    raw_cos = float(torch.dot(grad_train_raw, grad_comp_raw).item() / (norm_tr_raw * norm_cp_raw))

    # Whitened (Subspace-Projected) GCA
    grad_train_proj = compute_flattened_gradients(loss_train, model, exclude_embedding=True)
    grad_comp_proj = compute_flattened_gradients(loss_comp, model, exclude_embedding=True)

    norm_tr_proj = float(torch.linalg.norm(grad_train_proj).item() + 1e-10)
    norm_cp_proj = float(torch.linalg.norm(grad_comp_proj).item() + 1e-10)
    proj_cos = float(torch.dot(grad_train_proj, grad_comp_proj).item() / (norm_tr_proj * norm_cp_proj))

    return {
        "raw_gca": float(raw_cos),
        "whitened_gca": float(proj_cos),
    }
