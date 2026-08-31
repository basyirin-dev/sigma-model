"""Unified PyTorch DataLoaders and Batch Generators for Paper 02 (Task 5.2).

Provides memory-efficient tokenization, padding, batch collators, and online
primitive-substitution batch generators for computing the compositional loss L_comp.
"""

from __future__ import annotations

import random
from typing import Sequence

import torch
from torch.utils.data import DataLoader, Dataset

from paper02.src.data.hbar.grammar import HBarGrammar


class Seq2SeqDataset(Dataset):
    """Tokenized Sequence-to-Sequence Dataset for PyTorch DataLoaders."""

    def __init__(
        self,
        samples: Sequence[tuple[str, str]],
        vocab_to_idx: dict[str, int] | None = None,
        max_len: int = 64,
    ) -> None:
        self.samples = list(samples)
        if vocab_to_idx is None:
            vocab = HBarGrammar.get_full_vocabulary()
            self.vocab_to_idx = {t: i for i, t in enumerate(vocab)}
        else:
            self.vocab_to_idx = vocab_to_idx

        self.max_len = max_len
        self.pad_idx = self.vocab_to_idx.get("<pad>", 0)
        self.sos_idx = self.vocab_to_idx.get("<sos>", 1)
        self.eos_idx = self.vocab_to_idx.get("<eos>", 2)
        self.unk_idx = self.vocab_to_idx.get("<unk>", 3)

    def __len__(self) -> int:
        return len(self.samples)

    def _tokenize(self, text: str, add_sos_eos: bool = False) -> list[int]:
        tokens = text.strip().split()
        indices = [self.vocab_to_idx.get(t, self.unk_idx) for t in tokens]
        if add_sos_eos:
            indices = [self.sos_idx] + indices + [self.eos_idx]
        return indices[: self.max_len]

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        src_text, tgt_text = self.samples[idx]
        src_ids = self._tokenize(src_text, add_sos_eos=False)
        tgt_ids = self._tokenize(tgt_text, add_sos_eos=True)
        return torch.tensor(src_ids, dtype=torch.long), torch.tensor(tgt_ids, dtype=torch.long)


def collate_seq2seq(
    batch: list[tuple[torch.Tensor, torch.Tensor]],
    pad_idx: int = 0,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Pad variable-length source and target tensors into aligned rectangular batch tensors."""
    src_list, tgt_list = zip(*batch, strict=True)

    max_src = max(len(s) for s in src_list)
    max_tgt = max(len(t) for t in tgt_list)

    batch_size = len(batch)
    src_padded = torch.full((batch_size, max_src), pad_idx, dtype=torch.long)
    tgt_padded = torch.full((batch_size, max_tgt), pad_idx, dtype=torch.long)

    for i, (s, t) in enumerate(zip(src_list, tgt_list, strict=True)):
        src_padded[i, : len(s)] = s
        tgt_padded[i, : len(t)] = t

    return src_padded, tgt_padded


def create_dataloader(
    samples: Sequence[tuple[str, str]],
    vocab_to_idx: dict[str, int] | None = None,
    batch_size: int = 64,
    shuffle: bool = True,
    max_len: int = 64,
) -> DataLoader:
    """Create a high-throughput PyTorch DataLoader with dynamic batch padding."""
    ds = Seq2SeqDataset(samples, vocab_to_idx=vocab_to_idx, max_len=max_len)
    pad_idx = ds.pad_idx
    return DataLoader(
        ds,
        batch_size=batch_size,
        shuffle=shuffle,
        collate_fn=lambda b: collate_seq2seq(b, pad_idx=pad_idx),
    )


def generate_substitution_pairs(
    commands: Sequence[str],
    seed: int = 42,
) -> list[tuple[str, str]]:
    """Generate primitive substitution pairs (x_orig, x_sub) for L_comp computation.

    Substitutes an action primitive (e.g. 'jump' -> 'run') or direction ('left' -> 'right')
    to construct pairs with identical syntactic role structure.
    """
    rng = random.Random(seed)
    actions = HBarGrammar.ACTIONS
    directions = HBarGrammar.DIRECTIONS

    pairs: list[tuple[str, str]] = []
    for cmd in commands:
        tokens = cmd.split()
        if not tokens:
            continue
        sub_tokens = list(tokens)
        for i, t in enumerate(tokens):
            if t in actions:
                candidates = [a for a in actions if a != t]
                sub_tokens[i] = rng.choice(candidates)
                break
            elif t in directions:
                candidates = [d for d in directions if d != t]
                sub_tokens[i] = rng.choice(candidates)
                break
        pairs.append((cmd, " ".join(sub_tokens)))
    return pairs
