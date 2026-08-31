"""Configurable Seq2Seq Transformer Model for Paper 02 (Task 5.2).

Implements Architecture A (2-layer) and Architecture B (4-layer) seq2seq encoder-decoder
transformers with sinusoidal positional encodings, residual stream hooks, attention matrix
extraction, and cross-entropy loss calculation.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import ClassVar

import torch
import torch.nn as nn


class SinusoidalPositionalEncoding(nn.Module):
    """Standard sinusoidal positional encodings."""

    def __init__(self, d_model: int, max_len: int = 512) -> None:
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer("pe", pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (batch_size, seq_len, d_model)
        seq_len = x.size(1)
        return x + self.pe[:, :seq_len, :]


@dataclass
class TransformerConfig:
    """Hyperparameters for Seq2Seq Transformer."""

    vocab_size: int = 32
    d_model: int = 128
    n_heads: int = 4
    n_encoder_layers: int = 2
    n_decoder_layers: int = 2
    d_ff: int = 512
    dropout: float = 0.1
    max_len: int = 128
    pad_idx: int = 0


class Seq2SeqTransformer(nn.Module):
    """Modular Seq2Seq Transformer with residual stream hooks and attention taps."""

    DEFAULT_VOCAB_SIZE: ClassVar[int] = 32

    def __init__(self, config: TransformerConfig | None = None) -> None:
        super().__init__()
        self.config = config or TransformerConfig()
        d_model = self.config.d_model

        # Token & Positional Embeddings
        self.src_embedding = nn.Embedding(self.config.vocab_size, d_model, padding_idx=self.config.pad_idx)
        self.tgt_embedding = nn.Embedding(self.config.vocab_size, d_model, padding_idx=self.config.pad_idx)
        self.pos_encoding = SinusoidalPositionalEncoding(d_model, max_len=self.config.max_len)
        self.scale = math.sqrt(d_model)

        # Transformer Backbone
        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=self.config.n_heads,
            num_encoder_layers=self.config.n_encoder_layers,
            num_decoder_layers=self.config.n_decoder_layers,
            dim_feedforward=self.config.d_ff,
            dropout=self.config.dropout,
            batch_first=True,
        )

        # Output LM Head
        self.lm_head = nn.Linear(d_model, self.config.vocab_size, bias=False)
        # Weight tying
        self.lm_head.weight = self.tgt_embedding.weight

        # Residual stream activations cache
        self.layer_activations: dict[str, torch.Tensor] = {}

    def generate_square_subsequent_mask(self, sz: int, device: torch.device) -> torch.Tensor:
        """Causal autoregressive mask for decoder."""
        return torch.triu(torch.full((sz, sz), float("-inf"), device=device), diagonal=1)

    def forward(
        self,
        src: torch.Tensor,
        tgt_input: torch.Tensor,
        src_padding_mask: torch.Tensor | None = None,
        tgt_padding_mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        """Forward pass computing output logits.

        Args:
            src: Source token tensor of shape (batch_size, src_len).
            tgt_input: Target prefix tensor of shape (batch_size, tgt_len).
            src_padding_mask: Bool mask of shape (batch_size, src_len).
            tgt_padding_mask: Bool mask of shape (batch_size, tgt_len).

        Returns:
            Logits of shape (batch_size, tgt_len, vocab_size).
        """
        device = src.device
        tgt_seq_len = tgt_input.size(1)
        tgt_mask = self.generate_square_subsequent_mask(tgt_seq_len, device)

        src_emb = self.pos_encoding(self.src_embedding(src) * self.scale)
        tgt_emb = self.pos_encoding(self.tgt_embedding(tgt_input) * self.scale)

        # Store input embeddings in activation cache
        self.layer_activations["src_emb"] = src_emb.detach()
        self.layer_activations["tgt_emb"] = tgt_emb.detach()

        hidden = self.transformer(
            src=src_emb,
            tgt=tgt_emb,
            tgt_mask=tgt_mask,
            src_key_padding_mask=src_padding_mask,
            tgt_key_padding_mask=tgt_padding_mask,
        )

        self.layer_activations["decoder_final"] = hidden.detach()
        logits = self.lm_head(hidden)
        return logits

    def compute_loss(
        self,
        src: torch.Tensor,
        tgt: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """Compute cross-entropy loss given input and full target sequence (with <sos>)."""
        tgt_input = tgt[:, :-1]
        tgt_expected = tgt[:, 1:]

        src_pad = (src == self.config.pad_idx)
        tgt_pad = (tgt_input == self.config.pad_idx)

        logits = self.forward(src, tgt_input, src_padding_mask=src_pad, tgt_padding_mask=tgt_pad)
        loss = nn.functional.cross_entropy(
            logits.reshape(-1, self.config.vocab_size),
            tgt_expected.reshape(-1),
            ignore_index=self.config.pad_idx,
        )
        return loss, logits
