"""H-Bar compositional benchmark data (ported from the archived pilot notebook).

Source: ``archive/experiments/h-bar-experiment.ipynb`` cell 1 (canonical). The
generators are ported verbatim so the gate reproduces the archived pilot's data
distribution exactly; only function names are snake-cased for PEP8 (N802).

The H-Bar suite is a SCAN-style compositional benchmark: commands are sequences
of primitives (jump/walk/run/look), modifiers (twice/thrice), and combinators
(and/after/around/opposite); the target action sequence is the token-wise
composition. OOD examples are novel recombinations never seen in training.
"""

from __future__ import annotations

import random
from typing import Any

import numpy as np
from torch.utils.data import DataLoader
from tqdm.auto import tqdm

from sigma_align.utils.data import SCANDataset

# Token → action mapping (identical to the archived pilot).
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


def gen_simple() -> tuple[str, str]:
    """Single primitive, optionally with a direction or a modifier."""
    base = random.choice(["walk", "run", "jump", "look"])
    r = random.random()
    if r > 0.7:
        d = random.choice(["left", "right"])
        return (f"{base} {d}", f"{PRIMITIVES[base]} {PRIMITIVES[d]}")
    elif r > 0.4:
        m = random.choice(["twice", "thrice"])
        return (f"{m} {base}", f"{PRIMITIVES[m]} {PRIMITIVES[base]}")
    else:
        return (base, PRIMITIVES[base])


def gen_medium() -> tuple[str, str]:
    """One primitive plus up to one direction and one modifier (ID test)."""
    base = random.choice(["walk", "run", "jump", "look"])
    parts, actions = [base], [PRIMITIVES[base]]
    if random.random() > 0.5:
        d = random.choice(["left", "right"])
        parts.append(d)
        actions.append(PRIMITIVES[d])
    if random.random() > 0.6:
        m = random.choice(["twice", "thrice"])
        parts.insert(0, m)
        actions.insert(0, PRIMITIVES[m])
    return (" ".join(parts), " ".join(actions))


def gen_hard_ood() -> tuple[str, str]:
    """Novel compositional recombinations — never seen in training."""
    r = random.random()
    if r < 0.25:  # modifier + jump + direction
        mod = random.choice(["twice", "thrice"])
        d = random.choice(["left", "right"])
        return (f"{mod} jump {d}", f"{PRIMITIVES[mod]} JUMP {PRIMITIVES[d]}")
    elif r < 0.45:  # opposite + base + direction
        base = random.choice(["jump", "walk"])
        d = random.choice(["left", "right"])
        return (f"opposite {base} {d}", f"OPPOSITE {PRIMITIVES[base]} {PRIMITIVES[d]}")
    elif r < 0.65:  # conjunction
        b1 = random.choice(["jump", "walk"])
        b2 = random.choice(["run", "look"])
        conj = random.choice(["and", "after"])
        if conj == "and":
            return (f"{b1} {conj} {b2}", f"{PRIMITIVES[b1]} {PRIMITIVES[conj]} {PRIMITIVES[b2]}")
        return (f"{conj} {b1} {b2}", f"{PRIMITIVES[conj]} {PRIMITIVES[b1]} {PRIMITIVES[b2]}")
    elif r < 0.80:  # around + direction + modifier
        d = random.choice(["left", "right"])
        return (f"jump around {d} twice", f"JUMP AROUND {PRIMITIVES[d]} X2")
    # triple composition
    mods = random.sample(["twice", "thrice", "opposite"], 2)
    d = random.choice(["left", "right"])
    return (
        f"{mods[0]} {mods[1]} jump {d}",
        f"{PRIMITIVES[mods[0]]} {PRIMITIVES[mods[1]]} JUMP {PRIMITIVES[d]}",
    )


def generate_hard_compositional_data(
    n_train: int = 16000,
    n_test_id: int = 4000,
    n_test_ood: int = 1500,
    n_comp: int = 2000,
) -> tuple[
    list[tuple[str, str]],
    list[tuple[str, str]],
    list[tuple[str, str]],
    list[tuple[str, str]],
    dict[str, int],
]:
    """Generate the four H-Bar splits and the shared vocabulary.

    Returns ``(train_pairs, test_pairs, ood_pairs, comp_pairs, vocab)`` — the
    ``comp_pairs`` split is the compositional probe set (OOD-hard, re-drawn).
    """
    print(f"   Generating {n_train:,} training examples ...")
    train_pairs = [gen_simple() for _ in tqdm(range(n_train))]
    print(f"   Generating {n_test_id:,} ID test examples ...")
    test_pairs = [gen_medium() for _ in tqdm(range(n_test_id))]
    print(f"   Generating {n_test_ood:,} OOD test examples ...")
    ood_pairs = [gen_hard_ood() for _ in tqdm(range(n_test_ood))]
    print(f"   Generating {n_comp:,} compositional probe examples ...")
    comp_pairs = [gen_hard_ood() for _ in tqdm(range(n_comp))]

    vocab: dict[str, int] = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2}
    for pairs in [train_pairs, test_pairs, ood_pairs, comp_pairs]:
        for c, a in pairs:
            for tok in c.split() + a.split():
                if tok not in vocab:
                    vocab[tok] = len(vocab)

    print("\n   Dataset statistics:")
    print(f"   Train avg len : {np.mean([len(c.split()) for c, _ in train_pairs]):.1f} tokens")
    print(f"   ID test avg   : {np.mean([len(c.split()) for c, _ in test_pairs]):.1f} tokens")
    print(f"   OOD avg len   : {np.mean([len(c.split()) for c, _ in ood_pairs]):.1f} tokens")
    print(f"   Vocab size    : {len(vocab)}")
    return train_pairs, test_pairs, ood_pairs, comp_pairs, vocab


def make_loaders(
    train_pairs: list[tuple[str, str]],
    test_pairs: list[tuple[str, str]],
    ood_pairs: list[tuple[str, str]],
    comp_pairs: list[tuple[str, str]],
    vocab: dict[str, int],
    batch_size: int,
    seed: int,
    num_workers: int = 0,
) -> dict[str, Any]:
    """Build the train / ID / OOD / comp DataLoaders (mirrors pilot cell 3)."""

    def _worker_init(worker_id: int) -> None:
        np.random.seed(seed + worker_id)

    kw_train = dict(
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True,
        drop_last=True,
        worker_init_fn=_worker_init,
    )
    kw_eval = dict(
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True,
        worker_init_fn=_worker_init,
    )
    return {
        "train": DataLoader(SCANDataset(train_pairs, vocab), **kw_train),
        "id": DataLoader(SCANDataset(test_pairs, vocab), **kw_eval),
        "ood": DataLoader(SCANDataset(ood_pairs, vocab), **kw_eval),
        "comp": DataLoader(SCANDataset(comp_pairs, vocab), **kw_train),
    }
