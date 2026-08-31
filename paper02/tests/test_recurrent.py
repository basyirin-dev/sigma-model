"""Unit tests for Recurrent Seq2Seq baseline model (Paper 02 Task 5.2)."""

from __future__ import annotations

import torch

from paper02.src.models.recurrent import RecurrentConfig, RecurrentSeq2Seq


class TestRecurrentSeq2Seq:
    """Test recurrent model forward pass, loss, and hidden state caching."""

    def test_forward_output_shape(self) -> None:
        cfg = RecurrentConfig(vocab_size=32, d_model=64, d_hidden=64, n_layers=2)
        model = RecurrentSeq2Seq(cfg)

        src = torch.randint(1, 30, (4, 8))
        tgt_in = torch.randint(1, 30, (4, 6))

        logits = model(src, tgt_in)
        assert logits.shape == (4, 6, 32)

    def test_compute_loss(self) -> None:
        cfg = RecurrentConfig(vocab_size=32, d_model=64, d_hidden=64)
        model = RecurrentSeq2Seq(cfg)

        src = torch.randint(1, 30, (3, 6))
        tgt = torch.randint(1, 30, (3, 5))

        loss, logits = model.compute_loss(src, tgt)
        assert loss.ndim == 0
        assert not torch.isnan(loss)
        assert loss.item() > 0.0

    def test_activation_caching(self) -> None:
        cfg = RecurrentConfig(vocab_size=32, d_model=64, d_hidden=64)
        model = RecurrentSeq2Seq(cfg)

        src = torch.randint(1, 30, (2, 4))
        tgt_in = torch.randint(1, 30, (2, 3))

        _ = model(src, tgt_in)
        assert "decoder_hidden" in model.layer_activations
        assert model.layer_activations["decoder_hidden"].shape == (2, 3, 64)
