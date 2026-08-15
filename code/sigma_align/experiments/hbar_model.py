"""HBarTransformer seq2seq model (ported from the archived pilot notebook, cell 2).

Adds ``encode()`` — encoder states for the RGA probe — while keeping the decoder
path of the original ``forward`` bit-for-bit identical (parity with the archived
pilot runs).
"""

from __future__ import annotations

import math

import torch
import torch.nn as nn


class PositionalEncoding(nn.Module):
    """Sinusoidal positional encoding, broadcast over the batch dim (batch_first)."""

    def __init__(self, d_model: int, max_len: int = 500, dropout: float = 0.1):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        position = torch.arange(max_len).unsqueeze(1)  # (max_len, 1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe = torch.zeros(1, max_len, d_model)  # (1, max_len, d)
        pe[0, :, 0::2] = torch.sin(position * div_term)
        pe[0, :, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:  # x: (B, S, d)
        return self.dropout(x + self.pe[:, : x.size(1), :])


class HBarTransformer(nn.Module):
    """2-layer, 4-head Transformer (paper §11.1 spec)."""

    def __init__(
        self,
        vocab_size: int,
        d_model: int = 128,
        nhead: int = 4,
        num_layers: int = 2,
        dim_ff: int = 512,
        dropout: float = 0.1,
        pad_idx: int = 0,
    ):
        super().__init__()
        self.pad_idx = pad_idx
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
        """Encoder states for the RGA probe (masked mean-pooled downstream)."""
        src_emb = self.pos_encoding(self.embedding(src))
        return self.transformer.encoder(src_emb, src_key_padding_mask=(src == self.pad_idx))

    def forward(self, src: torch.Tensor, tgt: torch.Tensor) -> torch.Tensor:
        memory = self.encode(src)
        tgt_emb = self.pos_encoding(self.embedding(tgt))
        tgt_len = tgt.size(1)
        tgt_mask = torch.triu(torch.ones(tgt_len, tgt_len, device=tgt.device), diagonal=1)
        tgt_mask = tgt_mask.masked_fill(tgt_mask == 1, float("-inf"))
        out = self.transformer.decoder(tgt_emb, memory, tgt_mask=tgt_mask)
        return self.output_proj(out)

    def count_parameters(self) -> int:
        return sum(p.numel() for p in self.parameters())
