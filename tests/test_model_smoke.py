"""Smoke test for HBarTransformer architecture and optimization step."""

import torch
import torch.nn as nn
from sigma_align.experiments.hbar_model import HBarTransformer


def test_hbar_transformer_forward_and_encode():
    """Verify Transformer model forward pass and encoder state extraction."""
    vocab_size = 15
    d_model = 32
    seq_len = 8
    batch_size = 2

    model = HBarTransformer(
        vocab_size=vocab_size,
        d_model=d_model,
        nhead=2,
        num_layers=1,
        dim_ff=64,
        dropout=0.0,
        pad_idx=0,
    )

    src = torch.randint(1, vocab_size, (batch_size, seq_len))
    tgt = torch.randint(1, vocab_size, (batch_size, seq_len))

    # 1. Test encoder representation extraction
    enc_states = model.encode(src)
    assert enc_states.shape == (batch_size, seq_len, d_model)

    # 2. Test forward pass
    out = model(src, tgt[:, :-1])
    assert out.shape == (batch_size, seq_len - 1, vocab_size)


def test_hbar_transformer_single_optim_step():
    """Verify backward gradient propagation and parameter update."""
    vocab_size = 15
    d_model = 32
    seq_len = 6
    batch_size = 2

    model = HBarTransformer(
        vocab_size=vocab_size,
        d_model=d_model,
        nhead=2,
        num_layers=1,
        dim_ff=64,
        pad_idx=0,
    )
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss(ignore_index=0)

    src = torch.randint(1, vocab_size, (batch_size, seq_len))
    tgt = torch.randint(1, vocab_size, (batch_size, seq_len))

    optimizer.zero_grad()
    out = model(src, tgt[:, :-1])
    loss = criterion(out.reshape(-1, vocab_size), tgt[:, 1:].reshape(-1))
    loss.backward()

    # Ensure gradients exist
    assert model.output_proj.weight.grad is not None
    optimizer.step()
