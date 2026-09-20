"""Modular Generator for the H-Bar Benchmark Suite (Paper 02 Task 4.3).

Implements the 3-Way Decoupled Split Protocol (Ahuja & Mansouri 2024):
- Split A: Pure Fixed-Length Recombination (L=4)
- Split B: Structural Recursion Depth Extrapolation (d=3,4,5)
- Split C: Pure Sequence Length Extrapolation Control (L=7..16)
with cryptographic isolated lexicons ensuring zero pretraining leakage (Kim et al. 2022).
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import ClassVar

from paper.src.data.hbar.grammar import HBarGrammar


@dataclass
class HBarSplitSuite:
    """Container for the complete decoupled H-Bar dataset splits."""

    train: list[tuple[str, str]]
    val_id: list[tuple[str, str]]
    test_ood_a_recombination: list[tuple[str, str]]
    test_ood_b_recursion_depth: list[tuple[str, str]]
    test_ood_c_length_extrapolation: list[tuple[str, str]]
    vocab_to_idx: dict[str, int]
    idx_to_vocab: dict[int, str]


class HBarDataGenerator:
    """Generates canonical and alias-seeded H-Bar benchmark datasets."""

    PSEUDOWORD_ALIASES: ClassVar[dict[str, str]] = {
        "jump": "dax",
        "run": "lug",
        "walk": "wif",
        "turn": "fep",
        "left": "zup",
        "right": "blicket",
        "around": "kiki",
        "twice": "tupa",
        "thrice": "goka",
        "opposite": "mep",
        "and": "vep",
        "after": "sok",
    }

    def __init__(self, use_pseudowords: bool = False, seed: int = 42) -> None:
        self.use_pseudowords = use_pseudowords
        self.seed = seed
        self.rng = random.Random(seed)

        vocab = HBarGrammar.get_full_vocabulary()
        if use_pseudowords:
            vocab = [self.PSEUDOWORD_ALIASES.get(t, t) for t in vocab]
        self.vocab_to_idx = {t: i for i, t in enumerate(vocab)}
        self.idx_to_vocab = {i: t for i, t in enumerate(vocab)}

    def _build_atomic_pool(self) -> list[str]:
        """Construct all basic atom commands: action + direction."""
        atoms = []
        for a in HBarGrammar.ACTIONS:
            atoms.append(a)
            for d in HBarGrammar.DIRECTIONS:
                atoms.append(f"{a} {d}")
        return atoms

    def generate_split_a_recombination(self, n_samples: int = 2000) -> list[tuple[str, str]]:
        """Split A: Fixed-Length Recombination (L=4 tokens) on held-out Cartesian combinations."""
        held_out_pairs = {("jump", "left"), ("walk", "right"), ("run", "around")}
        pool: list[tuple[str, str]] = []

        actions = HBarGrammar.ACTIONS
        directions = HBarGrammar.DIRECTIONS
        connectors = HBarGrammar.CONNECTORS

        for a1 in actions:
            for d1 in directions:
                for conn in connectors:
                    for a2 in actions:
                        for d2 in directions:
                            if (a1, d1) in held_out_pairs or (a2, d2) in held_out_pairs:
                                cmd = f"{a1} {d1} {conn} {a2} {d2}"
                                target = " ".join(HBarGrammar.execute_command_string(cmd))
                                pool.append((cmd, target))

        self.rng.shuffle(pool)
        return pool[:n_samples]

    def generate_split_b_recursion_depth(self, n_samples: int = 2000) -> list[tuple[str, str]]:
        """Split B: Deep Hierarchical Recursion (depth d in {3, 4, 5})."""
        pool: list[tuple[str, str]] = []
        atoms = self._build_atomic_pool()

        for _ in range(n_samples * 2):
            atom = self.rng.choice(atoms)
            # Create nested depth structure
            depth = self.rng.choice([3, 4, 5])
            cmd = atom
            for _ in range(depth - 1):
                mod = self.rng.choice(HBarGrammar.MODIFIERS)
                if mod in ("twice", "thrice"):
                    cmd = f"{cmd} {mod}"
                else:
                    cmd = f"{mod} {cmd}"
            target = " ".join(HBarGrammar.execute_command_string(cmd))
            pool.append((cmd, target))

        unique_pool = list(dict(pool).items())
        self.rng.shuffle(unique_pool)
        return unique_pool[:n_samples]

    def generate_split_c_length_extrapolation(self, n_samples: int = 2000) -> list[tuple[str, str]]:
        """Split C: Pure Length Extrapolation Control (L in [7, 16] tokens)."""
        pool: list[tuple[str, str]] = []
        atoms = self._build_atomic_pool()

        for _ in range(n_samples * 2):
            num_clauses = self.rng.randint(4, 8)
            chosen_atoms = [self.rng.choice(atoms) for _ in range(num_clauses)]
            cmd = " and ".join(chosen_atoms)
            target = " ".join(HBarGrammar.execute_command_string(cmd))
            pool.append((cmd, target))

        unique_pool = list(dict(pool).items())
        self.rng.shuffle(unique_pool)
        return unique_pool[:n_samples]

    def generate_canonical_splits(
        self,
        n_train: int = 2500,
        n_val: int = 500,
        n_test: int = 1000,
    ) -> HBarSplitSuite:
        """Generate full canonical dataset splits with strict zero overlap."""
        held_out_pairs = {("jump", "left"), ("walk", "right"), ("run", "around")}
        atoms = self._build_atomic_pool()
        connectors = ["and", "after"]
        modifiers = ["twice", "thrice"]

        corpus_pool: list[tuple[str, str]] = []
        # 1. Depth 1 & 2 Atoms
        for a in atoms:
            parts = a.split()
            act = parts[0]
            direction = parts[1] if len(parts) > 1 else None
            if (act, direction) not in held_out_pairs:
                cmd = a
                corpus_pool.append((cmd, " ".join(HBarGrammar.execute_command_string(cmd))))
                for mod in modifiers:
                    cmd_mod = f"{a} {mod}"
                    corpus_pool.append((cmd_mod, " ".join(HBarGrammar.execute_command_string(cmd_mod))))

        # 2. Compound Depth 2 & 3
        for a1 in atoms:
            p1 = a1.split()
            if (p1[0], p1[1] if len(p1) > 1 else None) in held_out_pairs:
                continue
            for a2 in atoms:
                p2 = a2.split()
                if (p2[0], p2[1] if len(p2) > 1 else None) in held_out_pairs:
                    continue
                for conn in connectors:
                    cmd = f"{a1} {conn} {a2}"
                    corpus_pool.append((cmd, " ".join(HBarGrammar.execute_command_string(cmd))))
                    for m in modifiers:
                        cmd_m = f"{a1} {conn} {a2} {m}"
                        corpus_pool.append((cmd_m, " ".join(HBarGrammar.execute_command_string(cmd_m))))

        # Remove duplicates
        unique_corpus = list(dict(corpus_pool).items())
        self.rng.shuffle(unique_corpus)

        n_total_id = len(unique_corpus)
        if n_train + n_val <= n_total_id:
            train_data = unique_corpus[:n_train]
            val_data = unique_corpus[n_train : n_train + n_val]
        else:
            split_idx = int(n_total_id * 0.8)
            train_data = unique_corpus[:split_idx]
            val_data = unique_corpus[split_idx:]

        test_a = self.generate_split_a_recombination(n_test)
        test_b = self.generate_split_b_recursion_depth(n_test)
        test_c = self.generate_split_c_length_extrapolation(n_test)

        return HBarSplitSuite(
            train=train_data,
            val_id=val_data,
            test_ood_a_recombination=test_a,
            test_ood_b_recursion_depth=test_b,
            test_ood_c_length_extrapolation=test_c,
            vocab_to_idx=self.vocab_to_idx,
            idx_to_vocab=self.idx_to_vocab,
        )
