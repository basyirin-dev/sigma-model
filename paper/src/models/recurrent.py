"""Recurrent Seq2Seq Architecture Baseline for Paper 02 (Task 5.2).

Implements Architecture C (Gated Recurrent Seq2Seq) to evaluate the universality
of the Two-Subspace Critical Pressure Law across non-attention recurrent networks.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

import torch
import torch.nn as nn


@dataclass
class RecurrentConfig:
    """Hyperparameters for Recurrent Seq2Seq Model."""

    vocab_size: int = 32
    d_model: int = 128
    d_hidden: int = 128
    n_layers: int = 2
    dropout: float = 0.1
    pad_idx: int = 0


class RecurrentSeq2Seq(nn.Module):
    """Gated Recurrent Unit (GRU) Seq2Seq Encoder-Decoder."""

    DEFAULT_VOCAB_SIZE: ClassVar[int] = 32

    def __init__(self, config: RecurrentConfig | None = None) -> None:
        super().__init__()
        self.config = config or RecurrentConfig()

        self.src_embedding = nn.Embedding(
            self.config.vocab_size, self.config.d_model, padding_idx=self.config.pad_idx
        )
        self.tgt_embedding = nn.Embedding(
            self.config.vocab_size, self.config.d_model, padding_idx=self.config.pad_idx
        )

        self.encoder = nn.GRU(
            input_size=self.config.d_model,
            hidden_size=self.config.d_hidden,
            num_layers=self.config.n_layers,
            dropout=self.config.dropout if self.config.n_layers > 1 else 0.0,
            batch_first=True,
        )

        self.decoder = nn.GRU(
            input_size=self.config.d_model,
            hidden_size=self.config.d_hidden,
            num_layers=self.config.n_layers,
            dropout=self.config.dropout if self.config.n_layers > 1 else 0.0,
            batch_first=True,
        )

        self.lm_head = nn.Linear(self.config.d_hidden, self.config.vocab_size)
        self.layer_activations: dict[str, torch.Tensor] = {}

    def forward(self, src: torch.Tensor, tgt_input: torch.Tensor) -> torch.Tensor:
        """Forward pass through recurrent encoder and decoder."""
        src_emb = self.src_embedding(src)
        tgt_emb = self.tgt_embedding(tgt_input)

        _, hidden_enc = self.encoder(src_emb)
        decoder_out, _ = self.decoder(tgt_emb, hidden_enc)

        self.layer_activations["decoder_hidden"] = decoder_out.detach()
        logits = self.lm_head(decoder_out)
        return logits

    def compute_loss(
        self,
        src: torch.Tensor,
        tgt: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """Compute cross-entropy loss given input and target sequences."""
        tgt_input = tgt[:, :-1]
        tgt_expected = tgt[:, 1:]

        logits = self.forward(src, tgt_input)
        loss = nn.functional.cross_entropy(
            logits.reshape(-1, self.config.vocab_size),
            tgt_expected.reshape(-1),
            ignore_index=self.config.pad_idx,
        )
        return loss, logits
