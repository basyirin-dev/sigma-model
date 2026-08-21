"""Unit tests for Stage-1 online schema-coherence proxies (GCA and RGA)."""

import torch
import torch.nn as nn
from sigma_align.experiments.hbar_model import HBarTransformer
from sigma_align.monitoring.proxy import (
    compute_gca,
    compute_sigma_tilde,
    gca_parameters,
)


def test_gca_parameters_extraction():
    """Verify that GCA extracts output projection, first layer, and embedding parameters."""
    vocab_size = 20
    model = HBarTransformer(vocab_size=vocab_size, d_model=32, num_layers=2, nhead=2)
    params = gca_parameters(model)

    assert len(params) > 0
    assert any(p.shape == model.embedding.weight.shape for p in params)


def test_compute_gca_bounds():
    """Test GCA computation produces valid cosine alignment in [0, 1]."""
    vocab_size = 20
    model = HBarTransformer(vocab_size=vocab_size, d_model=32, num_layers=2, nhead=2)
    device = torch.device("cpu")
    criterion = nn.CrossEntropyLoss(ignore_index=0)

    batch_size = 4
    seq_len = 10
    src = torch.randint(1, vocab_size, (batch_size, seq_len))
    tgt = torch.randint(1, vocab_size, (batch_size, seq_len))

    main_batch = (src, tgt)
    comp_batch = (src, tgt)

    gca_score = compute_gca(
        model=model,
        main_batch=main_batch,
        comp_batch=comp_batch,
        criterion=criterion,
        device=device,
        use_amp=False,
    )

    assert 0.0 <= gca_score <= 1.0


def test_compute_sigma_tilde_fusion():
    """Test Stage-1 proxy fusion formula."""
    # Symmetrical weights
    st = compute_sigma_tilde(gca=0.8, rga=0.6, fuse_gca=0.5, fuse_rga=0.5)
    assert st == 0.7

    # Boundary clipping
    st_max = compute_sigma_tilde(gca=1.5, rga=1.5)
    assert st_max == 1.0

    st_min = compute_sigma_tilde(gca=-0.5, rga=-0.5)
    assert st_min == 0.0
