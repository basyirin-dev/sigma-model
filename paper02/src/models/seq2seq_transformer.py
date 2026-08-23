"""Seq2Seq Transformer Architecture for Paper 02 Mechanism Gate.

Spec: 2-layer, 4-head standard Transformer (d_model=128, dim_ff=512) with representation
hooks for representation geometry / CKA probes and greedy sequence generation.
"""

from __future__ import annotations

import math

import torch
import torch.nn as nn


class PositionalEncoding(nn.Module):
    """Sinusoidal positional encoding with batch_first layout."""

    def __init__(self, d_model: int, max_len: int = 500, dropout: float = 0.1) -> None:
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe = torch.zeros(1, max_len, d_model)
        pe[0, :, 0::2] = torch.sin(position * div_term)
        pe[0, :, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Add positional encoding to input tensor x of shape (batch, seq_len, d_model)."""
        return self.dropout(x + self.pe[:, : x.size(1), :])


class Seq2SeqTransformer(nn.Module):
    """Standard 2-layer, 4-head Seq2Seq Transformer for compositional benchmarks."""

    def __init__(
        self,
        vocab_size: int,
        d_model: int = 128,
        nhead: int = 4,
        num_layers: int = 2,
        dim_ff: int = 512,
        dropout: float = 0.1,
        pad_idx: int = 0,
    ) -> None:
        super().__init__()
        self.pad_idx = pad_idx
        self.d_model = d_model
        self.vocab_size = vocab_size

        self.embedding = nn.Embedding(vocab_size, d_model, padding_idx=pad_idx)
        self.pos_encoding = PositionalEncoding(d_model, dropout=dropout)

        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=nhead,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            dim_feedforward=dim_ff,
            dropout=dropout,
            batch_first=True,
        )
        self.output_proj = nn.Linear(d_model, vocab_size)

        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)

    def encode(self, src: torch.Tensor) -> torch.Tensor:
        """Compute encoder contextual representations for representation geometry analysis."""
        src_emb = self.pos_encoding(self.embedding(src) * math.sqrt(self.d_model))
        src_pad_mask = src == self.pad_idx
        return self.transformer.encoder(src_emb, src_key_padding_mask=src_pad_mask)

    def encode_pooled(self, src: torch.Tensor) -> torch.Tensor:
        """Masked mean-pool encoder states over non-padding tokens."""
        memory = self.encode(src)  # (B, S, D)
        mask = (src != self.pad_idx).unsqueeze(-1).float()  # (B, S, 1)
        sum_pooled = (memory * mask).sum(dim=1)  # (B, D)
        denom = mask.sum(dim=1).clamp(min=1.0)
        return sum_pooled / denom

    def forward(self, src: torch.Tensor, tgt: torch.Tensor) -> torch.Tensor:
        """Forward pass through encoder-decoder with causal target masking."""
        memory = self.encode(src)
        src_pad_mask = src == self.pad_idx
        tgt_pad_mask = tgt == self.pad_idx

        tgt_emb = self.pos_encoding(self.embedding(tgt) * math.sqrt(self.d_model))
        tgt_len = tgt.size(1)
        tgt_mask = torch.triu(torch.ones(tgt_len, tgt_len, device=tgt.device), diagonal=1).bool()

        out = self.transformer.decoder(
            tgt_emb,
            memory,
            tgt_mask=tgt_mask,
            tgt_key_padding_mask=tgt_pad_mask,
            memory_key_padding_mask=src_pad_mask,
        )
        return self.output_proj(out)

    def generate(
        self,
        src: torch.Tensor,
        max_len: int = 25,
        sos_idx: int = 1,
        eos_idx: int = 2,
    ) -> torch.Tensor:
        """Autoregressive greedy sequence decoding."""
        batch_size = src.size(0)
        memory = self.encode(src)
        src_pad_mask = src == self.pad_idx

        generated = torch.full((batch_size, 1), sos_idx, dtype=torch.long, device=src.device)
        finished = torch.zeros(batch_size, dtype=torch.bool, device=src.device)

        for _ in range(max_len):
            tgt_emb = self.pos_encoding(self.embedding(generated) * math.sqrt(self.d_model))
            tgt_len = generated.size(1)
            tgt_mask = torch.triu(
                torch.ones(tgt_len, tgt_len, device=src.device), diagonal=1
            ).bool()

            out = self.transformer.decoder(
                tgt_emb,
                memory,
                tgt_mask=tgt_mask,
                memory_key_padding_mask=src_pad_mask,
            )
            logits = self.output_proj(out[:, -1, :])
            next_token = logits.argmax(dim=-1, keepdim=True)

            # Mask finished sequences to maintain padding or eos
            next_token = torch.where(
                finished.unsqueeze(-1),
                torch.full_like(next_token, self.pad_idx),
                next_token,
            )
            generated = torch.cat([generated, next_token], dim=1)
            finished = finished | (next_token.squeeze(-1) == eos_idx)

            if finished.all():
                break

        return generated

    def count_parameters(self) -> int:
        """Count total trainable parameters in the model."""
        return sum(p.numel() for p in self.parameters() if p.requires_grad)
