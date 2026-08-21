"""Measured Stage-1 schema-coherence proxy (σ̃_A) for the mechanism gate.

Motivation (archived-data finding, 2026-08-16): the pilot's *scheduled* σ knob
does **not** lead OOD (σ-leads-fraction = 0.00 across conditions). The
leading-indicator test therefore uses a **measured** proxy instead of the
scheduled knob:

- GCA — gradient-composition alignment: cosine between the main-task loss
  gradient and the compositional-probe loss gradient over a fixed parameter
  slice (``output_proj`` + first encoder layer + embedding), mapped to [0, 1].
- RGA — representational-geometry alignment: mean same-operator cosine
  similarity minus random-pair cosine similarity over masked mean-pooled
  encoder states, clipped to [0, 1]. Operator labels come from the target
  action tokens (X2/X3/OPPOSITE/AFTER/AND/AROUND).

Fused proxy: ``sigma_tilde = 0.5 * (GCA + RGA)`` ∈ [0, 1]. Per-run min-max
normalisation is applied downstream in the analysis (not here), per the phase-04
spec. The full GCA/RGA/AC machinery plus two-stage calibration (Props 3.6–3.7)
stays in the companion report (P10).
"""

from __future__ import annotations

import random

import torch
import torch.nn as nn
from torch.amp.autocast_mode import autocast

# Operator tokens whose presence in a target action defines the RGA label.
RGA_OPERATORS = ("X2", "X3", "OPPOSITE", "AFTER", "AND", "AROUND")


def gca_parameters(model: nn.Module) -> list[nn.Parameter]:
    """Fixed parameter slice for GCA: output_proj + first encoder layer + embedding."""
    params: list[nn.Parameter] = []
    params.extend(model.output_proj.parameters())
    params.extend(model.transformer.encoder.layers[0].parameters())
    params.append(model.embedding.weight)
    return params


def _grad_vector(loss: torch.Tensor, params: list[nn.Parameter]) -> torch.Tensor | None:
    """Flatten the loss gradient w.r.t. the given parameters into one vector."""
    grads = torch.autograd.grad(loss, params, allow_unused=True)
    vecs = [g.detach().float().reshape(-1) for g in grads if g is not None]
    if not vecs:
        return None
    return torch.cat(vecs)


def compute_gca(
    model: nn.Module,
    main_batch: tuple[torch.Tensor, torch.Tensor],
    comp_batch: tuple[torch.Tensor, torch.Tensor],
    criterion: nn.Module,
    device: torch.device,
    use_amp: bool,
) -> float:
    """Gradient-composition alignment on fixed probe batches, mapped to [0, 1].

    The model is put in eval mode for the measurement (dropout off, deterministic)
    and its training/eval mode is restored afterwards. Gradients are computed with
    ``torch.autograd.grad`` only — optimizer state and ``.grad`` buffers are untouched.
    """
    was_training = model.training
    model.eval()
    try:
        src, tgt = main_batch
        c_src, c_tgt = comp_batch
        src, tgt = src.to(device), tgt.to(device)
        c_src, c_tgt = c_src.to(device), c_tgt.to(device)
        params = gca_parameters(model)

        with autocast("cuda", enabled=use_amp):
            out = model(src, tgt[:, :-1])
            main_loss = criterion(out.reshape(-1, out.size(-1)), tgt[:, 1:].reshape(-1))
        g_main = _grad_vector(main_loss, params)
        if g_main is None:
            return 0.5

        with autocast("cuda", enabled=use_amp):
            c_out = model(c_src, c_tgt[:, :-1])
            comp_loss = criterion(c_out.reshape(-1, c_out.size(-1)), c_tgt[:, 1:].reshape(-1))
        g_comp = _grad_vector(comp_loss, params)
        if g_comp is None:
            return 0.5

        cos = torch.nn.functional.cosine_similarity(g_main, g_comp, dim=0)
        return float(min(1.0, max(0.0, (cos.item() + 1.0) / 2.0)))
    finally:
        model.train(was_training)


def _masked_mean_pool(states: torch.Tensor, src: torch.Tensor, pad_idx: int) -> torch.Tensor:
    """Mean over non-padding positions of the encoder states (B, S, d) → (B, d)."""
    mask = (src != pad_idx).unsqueeze(-1)
    pooled = (states * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)
    return pooled


def compute_rga(
    model: nn.Module,
    sample: list[tuple[torch.Tensor, torch.Tensor]],
    vocab: dict[str, int],
    device: torch.device,
    use_amp: bool,
    operators: tuple[str, ...] = RGA_OPERATORS,
    n_pairs: int = 5000,
    seed: int = 0,
) -> float:
    """Representational-geometry alignment, clipped to [0, 1].

    ``sample`` is a list of ``(src, tgt)`` tensor pairs (e.g. drawn from the comp
    dataset). Each example's operator label is the set of operator tokens present
    in its target action. Returns mean same-operator cosine − mean random-pair
    cosine over masked mean-pooled encoder states, clipped to [0, 1].
    """
    if len(sample) < 2:
        return 0.5
    op_ids = [vocab[op] for op in operators if op in vocab]
    was_training = model.training
    model.eval()
    try:
        srcs = torch.stack([s for s, _ in sample]).to(device)
        with torch.inference_mode():
            with autocast("cuda", enabled=use_amp):
                states = model.encode(srcs)
            pooled = _masked_mean_pool(states, srcs, model.pad_idx).float()
            pooled = torch.nn.functional.normalize(pooled, dim=1)
            sims = pooled @ pooled.T  # (B, B) cosine similarities

        n = len(sample)
        labels: list[set[int]] = []
        for _, tgt in sample:
            tok = tgt.tolist()
            labels.append({t for t in op_ids if t in tok})

        same_pairs = [(i, j) for i in range(n) for j in range(i + 1, n) if labels[i] & labels[j]]
        if not same_pairs:
            return 0.0
        mean_same = float(sims[[i for i, _ in same_pairs], [j for _, j in same_pairs]].mean())

        rng = random.Random(seed)
        rand_pairs = [(rng.randrange(n), rng.randrange(n)) for _ in range(n_pairs)]
        mean_random = float(sims[[i for i, _ in rand_pairs], [j for _, j in rand_pairs]].mean())
        return float(min(1.0, max(0.0, mean_same - mean_random)))
    finally:
        model.train(was_training)


def compute_sigma_tilde(
    gca: float,
    rga: float,
    fuse_gca: float = 0.5,
    fuse_rga: float = 0.5,
) -> float:
    """Fused Stage-1 proxy: ``0.5 * (GCA + RGA)`` ∈ [0, 1]."""
    return float(min(1.0, max(0.0, fuse_gca * gca + fuse_rga * rga)))
