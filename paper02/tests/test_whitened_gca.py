"""Unit tests for Whitened (Subspace-Projected) Gradient Cosine Alignment (Paper 02 Task 5.3)."""

from __future__ import annotations

import torch

from paper02.src.analysis.whitened_gca import compute_whitened_gca
from paper02.src.models.transformer import Seq2SeqTransformer, TransformerConfig


class TestWhitenedGCA:
    """Test raw vs whitened GCA to verify elimination of step-0 initialization artifact."""

    def test_whitened_gca_step_zero_orthogonality(self) -> None:
        torch.manual_seed(42)
        cfg = TransformerConfig(vocab_size=32, d_model=64, n_heads=2)
        model = Seq2SeqTransformer(cfg)

        src = torch.randint(1, 30, (8, 6))
        tgt = torch.randint(1, 30, (8, 6))

        sub_src = torch.randint(1, 30, (8, 6))
        sub_tgt = torch.randint(1, 30, (8, 6))

        loss_train, _ = model.compute_loss(src, tgt)
        loss_comp, _ = model.compute_loss(sub_src, sub_tgt)

        res = compute_whitened_gca(model, loss_train, loss_comp)

        assert "raw_gca" in res
        assert "whitened_gca" in res
        # Whitened GCA at random initialization is small (|g_A^proj| < 0.25)
        assert abs(res["whitened_gca"]) < 0.25
