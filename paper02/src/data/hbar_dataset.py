"""H-Bar Zero-Leakage Compositional Dataset Generator for Paper 02.

Provides deterministic data generation, strict zero-leakage assertion between training and
OOD evaluation sets, vocabulary mapping, and PyTorch DataLoader constructors.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset

if TYPE_CHECKING:
    pass

# Token -> Action symbol mappings
PRIMITIVES: dict[str, str] = {
    "jump": "JUMP",
    "walk": "WALK",
    "run": "RUN",
    "look": "LOOK",
    "left": "LTURN",
    "right": "RTURN",
    "twice": "X2",
    "thrice": "X3",
    "and": "AND",
    "after": "AFTER",
    "around": "AROUND",
    "opposite": "OPPOSITE",
}


def gen_simple(rng: random.Random) -> tuple[str, str]:
    """Single primitive or simple 1-step modified command (train domain)."""
    base = rng.choice(["walk", "run", "jump", "look"])
    r = rng.random()
    if r > 0.7:
        d = rng.choice(["left", "right"])
        return (f"{base} {d}", f"{PRIMITIVES[base]} {PRIMITIVES[d]}")
    elif r > 0.4:
        m = rng.choice(["twice", "thrice"])
        return (f"{m} {base}", f"{PRIMITIVES[m]} {PRIMITIVES[base]}")
    else:
        return (base, PRIMITIVES[base])


def gen_id_medium(rng: random.Random) -> tuple[str, str]:
    """In-distribution test commands (same structural distribution as train)."""
    base = rng.choice(["walk", "run", "jump", "look"])
    parts, actions = [base], [PRIMITIVES[base]]
    if rng.random() > 0.5:
        d = rng.choice(["left", "right"])
        parts.append(d)
        actions.append(PRIMITIVES[d])
    if rng.random() > 0.6:
        m = rng.choice(["twice", "thrice"])
        parts.insert(0, m)
        actions.insert(0, PRIMITIVES[m])
    return (" ".join(parts), " ".join(actions))


def gen_hard_ood(rng: random.Random) -> tuple[str, str]:
    """Strictly unseen compositional recombinations (OOD evaluation)."""
    r = rng.random()
    if r < 0.25:  # modifier + jump + direction
        mod = rng.choice(["twice", "thrice"])
        d = rng.choice(["left", "right"])
        return (f"{mod} jump {d}", f"{PRIMITIVES[mod]} JUMP {PRIMITIVES[d]}")
    elif r < 0.45:  # opposite + base + direction
        base = rng.choice(["jump", "walk"])
        d = rng.choice(["left", "right"])
        return (f"opposite {base} {d}", f"OPPOSITE {PRIMITIVES[base]} {PRIMITIVES[d]}")
    elif r < 0.65:  # conjunction
        b1 = rng.choice(["jump", "walk"])
        b2 = rng.choice(["run", "look"])
        conj = rng.choice(["and", "after"])
        if conj == "and":
            return (f"{b1} {conj} {b2}", f"{PRIMITIVES[b1]} {PRIMITIVES[conj]} {PRIMITIVES[b2]}")
        return (f"{conj} {b1} {b2}", f"{PRIMITIVES[conj]} {PRIMITIVES[b1]} {PRIMITIVES[b2]}")
    elif r < 0.80:  # around + direction + modifier
        d = rng.choice(["left", "right"])
        return (f"jump around {d} twice", f"JUMP AROUND {PRIMITIVES[d]} X2")
    # Triple composition
    mods = rng.sample(["twice", "thrice", "opposite"], 2)
    d = rng.choice(["left", "right"])
    return (
        f"{mods[0]} {mods[1]} jump {d}",
        f"{PRIMITIVES[mods[0]]} {PRIMITIVES[mods[1]]} JUMP {PRIMITIVES[d]}",
    )


@dataclass(frozen=True)
class HBarDataSplits:
    """Container for the generated H-Bar benchmark dataset splits."""

    train_pairs: list[tuple[str, str]]
    id_pairs: list[tuple[str, str]]
    ood_pairs: list[tuple[str, str]]
    comp_pairs: list[tuple[str, str]]
    vocab: dict[str, int]
    inv_vocab: dict[int, str]


def generate_hbar_splits(
    n_train: int = 10000,
    n_test_id: int = 2000,
    n_test_ood: int = 2000,
    n_comp_probe: int = 2000,
    seed: int = 42,
) -> HBarDataSplits:
    """Generate deterministic H-Bar dataset splits with zero-leakage guarantee."""
    rng = random.Random(seed)

    train_pairs = [gen_simple(rng) for _ in range(n_train)]
    id_pairs = [gen_id_medium(rng) for _ in range(n_test_id)]
    ood_pairs = [gen_hard_ood(rng) for _ in range(n_test_ood)]
    comp_pairs = [gen_hard_ood(rng) for _ in range(n_comp_probe)]

    # Verify zero-leakage invariant: no OOD command should ever appear in the training split
    train_cmds = {c for c, _ in train_pairs}
    ood_cmds = {c for c, _ in ood_pairs}
    overlap = train_cmds.intersection(ood_cmds)
    if overlap:
        raise ValueError(
            f"Zero-leakage invariant violated: {len(overlap)} commands overlap between train and OOD splits."
        )

    # Build canonical vocabulary
    vocab: dict[str, int] = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2}
    for pairs in [train_pairs, id_pairs, ood_pairs, comp_pairs]:
        for c, a in pairs:
            for tok in c.split() + a.split():
                if tok not in vocab:
                    vocab[tok] = len(vocab)

    inv_vocab = {v: k for k, v in vocab.items()}

    return HBarDataSplits(
        train_pairs=train_pairs,
        id_pairs=id_pairs,
        ood_pairs=ood_pairs,
        comp_pairs=comp_pairs,
        vocab=vocab,
        inv_vocab=inv_vocab,
    )


class HBarDataset(Dataset[dict[str, torch.Tensor]]):
    """PyTorch Dataset for command-to-action pairs."""

    def __init__(self, pairs: list[tuple[str, str]], vocab: dict[str, int]) -> None:
        self.pairs = pairs
        self.vocab = vocab

    def __len__(self) -> int:
        return len(self.pairs)

    def __getitem__(self, idx: int) -> dict[str, torch.Tensor]:
        cmd, act = self.pairs[idx]
        src_tokens = [self.vocab[tok] for tok in cmd.split()]
        act_tokens = [self.vocab[tok] for tok in act.split()]

        # Target input: <SOS> + tokens
        tgt_in = [self.vocab["<SOS>"]] + act_tokens
        # Target output: tokens + <EOS>
        tgt_out = act_tokens + [self.vocab["<EOS>"]]

        return {
            "src": torch.tensor(src_tokens, dtype=torch.long),
            "tgt_in": torch.tensor(tgt_in, dtype=torch.long),
            "tgt_out": torch.tensor(tgt_out, dtype=torch.long),
        }


def collate_hbar_batch(batch: list[dict[str, torch.Tensor]], pad_idx: int = 0) -> dict[str, torch.Tensor]:
    """Pad variable-length sequences to the maximum length in the batch."""
    src_list = [item["src"] for item in batch]
    tgt_in_list = [item["tgt_in"] for item in batch]
    tgt_out_list = [item["tgt_out"] for item in batch]

    src_padded = torch.nn.utils.rnn.pad_sequence(src_list, batch_first=True, padding_value=pad_idx)
    tgt_in_padded = torch.nn.utils.rnn.pad_sequence(
        tgt_in_list, batch_first=True, padding_value=pad_idx
    )
    tgt_out_padded = torch.nn.utils.rnn.pad_sequence(
        tgt_out_list, batch_first=True, padding_value=pad_idx
    )

    return {
        "src": src_padded,
        "tgt_in": tgt_in_padded,
        "tgt_out": tgt_out_padded,
    }


def create_hbar_dataloaders(
    splits: HBarDataSplits,
    batch_size: int = 64,
    seed: int = 42,
    num_workers: int = 0,
) -> dict[str, DataLoader[Any]]:
    """Build PyTorch DataLoaders for train, id, ood, and comp splits."""

    def _worker_init(worker_id: int) -> None:
        np.random.seed(seed + worker_id)
        random.seed(seed + worker_id)

    train_drop_last = len(splits.train_pairs) >= batch_size
    comp_drop_last = len(splits.comp_pairs) >= batch_size

    kw_train = {
        "batch_size": batch_size,
        "shuffle": True,
        "num_workers": num_workers,
        "pin_memory": False,
        "drop_last": train_drop_last,
        "collate_fn": lambda b: collate_hbar_batch(b, pad_idx=splits.vocab["<PAD>"]),
        "worker_init_fn": _worker_init,
    }
    kw_comp = {
        "batch_size": batch_size,
        "shuffle": True,
        "num_workers": num_workers,
        "pin_memory": False,
        "drop_last": comp_drop_last,
        "collate_fn": lambda b: collate_hbar_batch(b, pad_idx=splits.vocab["<PAD>"]),
        "worker_init_fn": _worker_init,
    }
    kw_eval = {
        "batch_size": batch_size,
        "shuffle": False,
        "num_workers": num_workers,
        "pin_memory": False,
        "collate_fn": lambda b: collate_hbar_batch(b, pad_idx=splits.vocab["<PAD>"]),
        "worker_init_fn": _worker_init,
    }

    return {
        "train": DataLoader(HBarDataset(splits.train_pairs, splits.vocab), **kw_train),
        "id": DataLoader(HBarDataset(splits.id_pairs, splits.vocab), **kw_eval),
        "ood": DataLoader(HBarDataset(splits.ood_pairs, splits.vocab), **kw_eval),
        "comp": DataLoader(HBarDataset(splits.comp_pairs, splits.vocab), **kw_comp),
    }
