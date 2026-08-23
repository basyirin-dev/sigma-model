"""Representation Geometry and Centered Kernel Alignment (CKA) Analysis for Paper 02.

Provides linear CKA computation between activation representations and Representational
Geometry Alignment (RGA) metrics tracking schema manifold emergence.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

import torch
import torch.nn.functional as F  # noqa: N812

if TYPE_CHECKING:
    import torch.nn as nn

RGA_OPERATOR_TOKENS: tuple[str, ...] = (
    "X2",
    "X3",
    "OPPOSITE",
    "AFTER",
    "AND",
    "AROUND",
)


def compute_linear_cka(x: torch.Tensor, y: torch.Tensor) -> float:
    """Compute Linear Centered Kernel Alignment (CKA) between representations X and Y.

    Args:
        x: Activation tensor of shape (N, D1).
        y: Activation tensor of shape (N, D2).

    Returns:
        Scalar CKA similarity in [0, 1].
    """
    if x.size(0) != y.size(0):
        raise ValueError(
            f"Batch sizes must match for CKA computation: got {x.size(0)} vs {y.size(0)}"
        )

    n = x.size(0)
    if n < 2:
        return 1.0

    # Center representations: X_c = X - mean(X, dim=0)
    x_c = x - x.mean(dim=0, keepdim=True)
    y_c = y - y.mean(dim=0, keepdim=True)

    # Compute HSIC: tr(K_c L_c) = ||Y_c^T X_c||_F^2
    # This avoids forming the full N x N Gram matrices, achieving O(N * D1 * D2) scaling
    dot_prod = torch.matmul(x_c.t(), y_c)
    hsic_xy = torch.norm(dot_prod, p="fro") ** 2

    hsic_xx = torch.norm(torch.matmul(x_c.t(), x_c), p="fro") ** 2
    hsic_yy = torch.norm(torch.matmul(y_c.t(), y_c), p="fro") ** 2

    denom = torch.sqrt(hsic_xx * hsic_yy).clamp(min=1e-12)
    cka_val = (hsic_xy / denom).item()

    return float(min(1.0, max(0.0, cka_val)))


def compute_rga_metric(
    model: nn.Module,
    sample_pairs: list[tuple[str, str]],
    vocab: dict[str, int],
    device: torch.device,
    operators: tuple[str, ...] = RGA_OPERATOR_TOKENS,
    n_random_pairs: int = 2000,
    seed: int = 42,
) -> float:
    """Compute Representational Geometry Alignment (RGA) on encoder contextual states.

    Measures the difference between same-operator contextual cosine similarity and
    random-pair baseline cosine similarity.

    Args:
        model: Seq2SeqTransformer model with an `encode_pooled` method.
        sample_pairs: List of (command, action) pairs.
        vocab: Shared vocabulary dictionary.
        device: PyTorch compute device.
        operators: Target action tokens defining operator classes.
        n_random_pairs: Number of Monte Carlo random pairs for baseline similarity.
        seed: Random seed for pairing sampling.

    Returns:
        Scalar RGA metric in [0, 1].
    """
    if len(sample_pairs) < 4:
        return 0.5

    op_ids = {vocab[op] for op in operators if op in vocab}
    was_training = model.training
    model.eval()

    try:
        # Prepare and pad batch of sample inputs
        pad_idx = vocab.get("<PAD>", 0)
        src_tensors = [
            torch.tensor([vocab[t] for t in cmd.split() if t in vocab], dtype=torch.long)
            for cmd, _ in sample_pairs
        ]
        src_batch = torch.nn.utils.rnn.pad_sequence(
            src_tensors, batch_first=True, padding_value=pad_idx
        ).to(device)

        with torch.inference_mode():
            if hasattr(model, "encode_pooled"):
                pooled = model.encode_pooled(src_batch).float()
            else:
                memory = model.encode(src_batch)  # type: ignore[attr-defined]
                mask = (src_batch != pad_idx).unsqueeze(-1).float()
                pooled = (memory * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1.0)

            pooled = F.normalize(pooled, p=2, dim=1)
            sim_matrix = torch.matmul(pooled, pooled.t())  # (N, N)

        n = len(sample_pairs)
        labels: list[set[int]] = []
        for _, act in sample_pairs:
            act_tok_ids = {vocab[t] for t in act.split() if t in vocab}
            labels.append(act_tok_ids.intersection(op_ids))

        # Find same-operator pairs (i < j where labels share at least one operator)
        same_pairs = [
            (i, j) for i in range(n) for j in range(i + 1, n) if labels[i].intersection(labels[j])
        ]
        if not same_pairs:
            return 0.0

        i_idx = torch.tensor([i for i, _ in same_pairs], dtype=torch.long, device=device)
        j_idx = torch.tensor([j for _, j in same_pairs], dtype=torch.long, device=device)
        mean_same = sim_matrix[i_idx, j_idx].mean().item()

        # Sample random pairs for baseline similarity
        rng = random.Random(seed)
        rand_pairs = [
            (rng.randrange(n), rng.randrange(n))
            for _ in range(min(n_random_pairs, n * (n - 1) // 2))
        ]
        r_i = torch.tensor([i for i, _ in rand_pairs], dtype=torch.long, device=device)
        r_j = torch.tensor([j for _, j in rand_pairs], dtype=torch.long, device=device)
        mean_random = sim_matrix[r_i, r_j].mean().item()

        rga_val = mean_same - mean_random
        return float(min(1.0, max(0.0, rga_val)))

    finally:
        model.train(was_training)
