"""Unit tests for Seq2Seq Transformer model (Paper 02 Task 5.2)."""

from __future__ import annotations

import torch

from paper02.src.models.transformer import Seq2SeqTransformer, TransformerConfig


class TestSeq2SeqTransformer:
    """Test transformer forward pass, loss calculation, and activation caching."""

    def test_forward_output_shape(self) -> None:
        cfg = TransformerConfig(vocab_size=32, d_model=64, n_heads=2, n_encoder_layers=2, n_decoder_layers=2)
        model = Seq2SeqTransformer(cfg)

        batch_size = 4
        src_len = 8
        tgt_len = 6

        src = torch.randint(1, 30, (batch_size, src_len))
        tgt_in = torch.randint(1, 30, (batch_size, tgt_len))

        logits = model(src, tgt_in)
        assert logits.shape == (batch_size, tgt_len, 32)

    def test_compute_loss(self) -> None:
        cfg = TransformerConfig(vocab_size=32, d_model=64, n_heads=2)
        model = Seq2SeqTransformer(cfg)

        src = torch.randint(1, 30, (4, 8))
        tgt = torch.randint(1, 30, (4, 7))

        loss, logits = model.compute_loss(src, tgt)
        assert loss.ndim == 0
        assert not torch.isnan(loss)
        assert loss.item() > 0.0

    def test_residual_stream_activation_caching(self) -> None:
        cfg = TransformerConfig(vocab_size=32, d_model=64, n_heads=2)
        model = Seq2SeqTransformer(cfg)

        src = torch.randint(1, 30, (2, 5))
        tgt_in = torch.randint(1, 30, (2, 4))

        _ = model(src, tgt_in)
        assert "src_emb" in model.layer_activations
        assert "decoder_final" in model.layer_activations
        assert model.layer_activations["decoder_final"].shape == (2, 4, 64)
