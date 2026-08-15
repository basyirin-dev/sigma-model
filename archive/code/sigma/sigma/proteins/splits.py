"""Train/val/test splitting strategies — compositional splits for Pfam domain architectures.

Three split types with increasing difficulty:
    - Type A (familiar recombinations):  same families, rearranged
    - Type B (new family recombinations):  held-out families in novel combos
    - Type C (cross-fold recombination):   held-out clans
"""

from __future__ import annotations

import random
from typing import Any

import numpy as np

from sigma.ode.equations import psi_geometric
from sigma.proteins.data import _load_clans


def _base(acc: str) -> str:
    """Strip version suffix from a Pfam accession."""
    return acc.split(".")[0] if "." in acc else acc


def _check_matrix(accessions: list[str], similarity_matrix: np.ndarray) -> None:
    """Verify similarity matrix dimensions match the accession list."""
    n = len(accessions)
    if similarity_matrix.shape != (n, n):
        raise ValueError(
            f"similarity_matrix shape {similarity_matrix.shape} does not match "
            f"len(accessions)={n}"
        )


def recombination_distance(
    arch_a: list[str],
    arch_b: list[str],
    similarity_matrix: np.ndarray,
    accessions: list[str],
) -> float:
    """Compute recombination distance between two domain architectures.

    Distance = 1 - mean_{d1 in A, d2 in B} psi_geometric(1.0, 1.0, phi=sim_matrix[d1,d2])

    Since psi_geometric(1.0, 1.0, phi=s) = s, this simplifies to
    1 - mean similarity over all cross-domain pairs.

    Args:
        arch_a: First domain architecture (e.g. ``["PF00001.1", "PF00002.1"]``).
        arch_b: Second domain architecture.
        similarity_matrix: N×N similarity matrix from ``precompute_similarity_matrix``.
        accessions: Ordered list of accessions corresponding to matrix rows/columns.

    Returns:
        float: Recombination distance in [0, 1]. 0 = identical, 1 = maximally distant.
    """
    if not arch_a or not arch_b:
        return 1.0
    if arch_a == arch_b:
        return 0.0

    acc_to_idx = {acc: i for i, acc in enumerate(accessions)}
    sims: list[float] = []
    for d1 in arch_a:
        if d1 not in acc_to_idx:
            raise ValueError(f"Accession {d1!r} not found in similarity matrix")
        i = acc_to_idx[d1]
        for d2 in arch_b:
            if d2 not in acc_to_idx:
                raise ValueError(f"Accession {d2!r} not found in similarity matrix")
            j = acc_to_idx[d2]
            s = similarity_matrix[i, j]
            sims.append(psi_geometric(1.0, 1.0, phi=s))

    return 1.0 - float(np.mean(sims)) if sims else 1.0


def make_compositional_splits(
    architectures: list[list[str]],
    similarity_matrix: np.ndarray,
    accessions: list[str],
    *,
    seed: int = 42,
    id_ratio: float = 0.8,
    held_out_family_ratio: float = 0.2,
    held_out_clan_ratio: float = 0.2,
    clans_tsv_path: str = "data/pfam/raw/Pfam-A.clans.tsv",
) -> dict[str, dict[str, list[list[str]]]]:
    """Generate three compositional split types for Pfam domain architectures.

    Args:
        architectures: Domain architecture sequences (list of accession lists).
        similarity_matrix: N×N similarity matrix (for validation only — used by downstream tasks).
        accessions: Ordered accessions corresponding to matrix rows/columns.
        seed: Random seed.
        id_ratio: Fraction of architectures in the ID (training) set (default 0.8).
        held_out_family_ratio: Fraction of domain families held out for Type B (default 0.2).
        held_out_clan_ratio: Fraction of clans held out for Type C (default 0.2).
        clans_tsv_path: Path to Pfam-A.clans.tsv for clan-level hold-out.

    Returns:
        dict: Keys ``type_a``, ``type_b``, ``type_c``; each a dict with ``id`` and ``ood`` lists.
    """
    if not architectures:
        raise ValueError("architectures list is empty")

    _check_matrix(accessions, similarity_matrix)

    rng = random.Random(seed)
    archs = list(architectures)
    rng.shuffle(archs)

    # ── Type A: familiar recombinations (random split with family coverage) ──
    split_idx = max(1, int(len(archs) * id_ratio))
    id_a = archs[:split_idx]
    ood_a = archs[split_idx:]

    # Ensure all families in OOD also appear in ID
    families_ood = {_base(d) for a in ood_a for d in a}
    families_id = {_base(d) for a in id_a for d in a}
    missing = families_ood - families_id
    if missing:
        for arch in list(ood_a):
            if missing & {_base(d) for d in arch}:
                id_a.append(arch)
                ood_a.remove(arch)
                families_id.update(_base(d) for d in arch)
                missing -= {_base(d) for d in arch}
                if not missing:
                    break

    _arch_index = {id(a): i for i, a in enumerate(archs)}
    id_a.sort(key=lambda a: _arch_index[id(a)])
    ood_a.sort(key=lambda a: _arch_index[id(a)])

    result: dict[str, dict[str, list[list[str]]]] = {
        "type_a": {"id": id_a, "ood": ood_a},
    }

    # ── Type B: new family recombinations (family-level hold-out) ──
    all_families = sorted({_base(d) for a in architectures for d in a})
    n_hold = max(1, int(len(all_families) * held_out_family_ratio))
    rng.shuffle(all_families)
    held_out_families = set(all_families[:n_hold])

    id_b = [a for a in architectures if not any(_base(d) in held_out_families for d in a)]
    ood_b = [a for a in architectures if any(_base(d) in held_out_families for d in a)]

    if not id_b or not ood_b:
        raise ValueError(
            "Type B split produced empty set — reduce held_out_family_ratio "
            f"(tried {held_out_family_ratio}, {n_hold} families)"
        )

    result["type_b"] = {"id": id_b, "ood": ood_b}

    # ── Type C: cross-fold recombination (clan-level hold-out) ──
    clan_map = _load_clans(clans_tsv_path)

    all_clans: set[str] = set()
    for a in architectures:
        for d in a:
            clan = clan_map.get(_base(d))
            if clan:
                all_clans.add(clan)

    if not all_clans:
        raise ValueError(
            "No clans found — cannot produce Type C split. "
            "Check clans_tsv_path."
        )

    n_hold_clans = max(1, int(len(all_clans) * held_out_clan_ratio))
    sorted_clans = sorted(all_clans)
    rng.shuffle(sorted_clans)
    held_out_clans = set(sorted_clans[:n_hold_clans])

    def _in_held_out_clan(arch: list[str]) -> bool:
        for d in arch:
            c = clan_map.get(_base(d))
            if c and c in held_out_clans:
                return True
        return False

    id_c = [a for a in architectures if not _in_held_out_clan(a)]
    ood_c = [a for a in architectures if _in_held_out_clan(a)]

    if not id_c or not ood_c:
        raise ValueError(
            "Type C split produced empty set — reduce held_out_clan_ratio "
            f"(tried {held_out_clan_ratio}, {n_hold_clans} clans)"
        )

    result["type_c"] = {"id": id_c, "ood": ood_c}

    return result


def compute_split_statistics(
    split_dict: dict[str, dict[str, list[list[str]]]],
    similarity_matrix: np.ndarray | None = None,
    accessions: list[str] | None = None,
) -> dict[str, dict[str, Any]]:
    """Compute summary statistics for all three split types.

    Args:
        split_dict: Output from ``make_compositional_splits``.
        similarity_matrix: N×N similarity matrix for recombination distance computation.
        accessions: Ordered accessions for matrix indexing.

    Returns:
        dict: Nested dict with per-split-type statistics.
    """
    stats: dict[str, dict[str, Any]] = {}
    for split_type in ("type_a", "type_b", "type_c"):
        if split_type not in split_dict:
            continue
        id_set = split_dict[split_type]["id"]
        ood_set = split_dict[split_type]["ood"]

        families_id = {_base(d) for a in id_set for d in a}
        families_ood = {_base(d) for a in ood_set for d in a}

        entry: dict[str, Any] = {
            "n_id": len(id_set),
            "n_ood": len(ood_set),
            "unique_families_id": len(families_id),
            "unique_families_ood": len(families_ood),
            "unique_families_shared": len(families_id & families_ood),
            "avg_length_id": float(np.mean([len(a) for a in id_set])) if id_set else 0.0,
            "avg_length_ood": float(np.mean([len(a) for a in ood_set])) if ood_set else 0.0,
        }

        if similarity_matrix is not None and accessions is not None:
            dists = [
                recombination_distance(a, b, similarity_matrix, accessions)
                for a in id_set[:100]
                for b in ood_set[:100]
            ]
            entry["recombination_distance_id_ood"] = float(np.mean(dists)) if dists else 0.0

        stats[split_type] = entry

    return stats
