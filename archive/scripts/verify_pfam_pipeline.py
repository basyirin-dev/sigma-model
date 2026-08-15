#!/usr/bin/env python3
"""
Σ-Model — Pfam Data Pipeline Integration Test.

Parses Pfam seed alignments, extracts domain architectures, builds
vocabulary, generates compositional splits, and reports statistics.

Usage:
    # Quick verification (first 500 families, CPU, <5s)
    PYTHONPATH=code:$PYTHONPATH python scripts/verify_pfam_pipeline.py --quick 500

    # Full pipeline (all 30 134 families, ~2-5 min)
    PYTHONPATH=code:$PYTHONPATH python scripts/verify_pfam_pipeline.py --full

    # Full pipeline with cache to data/pfam/processed/
    PYTHONPATH=code:$PYTHONPATH python scripts/verify_pfam_pipeline.py --full --cache

    # With precomputed similarity matrix (18h, separate step)
    PYTHONPATH=code:$PYTHONPATH python scripts/verify_pfam_pipeline.py \\
        --full --sim-matrix PATH  # PATH = data/pfam/processed/similarity_matrix.npy
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

# ── Path setup ──────────────────────────────────────────────────
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "code"))

from sigma.config import load_config  # noqa: E402

# ── Data paths ──────────────────────────────────────────────────
SEED_PATH = os.path.join(REPO_ROOT, "data", "pfam", "raw", "Pfam-A.seed.gz")
CLANS_PATH = os.path.join(REPO_ROOT, "data", "pfam", "raw", "Pfam-A.clans.tsv")
CONFIG_PATH = os.path.join(REPO_ROOT, "experiments", "configs", "pfam-base.yaml")
PROCESSED_DIR = os.path.join(REPO_ROOT, "data", "pfam", "processed")

# ── Pipeline imports (after path setup) ─────────────────────────
from sigma.proteins.data import (  # noqa: E402
    build_domain_vocab,
    extract_domain_architectures,
    parse_stockholm,
)
from sigma.proteins.splits import (  # noqa: E402
    compute_split_statistics,
    make_compositional_splits,
)


def _count_records(filepath: str) -> int:
    """Count Stockholm records in a file without parsing sequences."""
    import gzip
    opener = gzip.open if filepath.endswith(".gz") else open
    count = 0
    with opener(filepath, "rt", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#=GF AC"):
                count += 1
    return count


def _print_stats(stats: dict) -> None:
    """Print statistics table."""
    for split_type, entry in stats.items():
        label = split_type.replace("_", " ").title()
        print(f"\n  ── {label} ──")
        print(f"    ID architectures : {entry['n_id']}")
        print(f"    OOD architectures: {entry['n_ood']}")
        print(f"    Unique families  : ID={entry['unique_families_id']}, "
              f"OOD={entry['unique_families_ood']}, "
              f"shared={entry['unique_families_shared']}")
        print(f"    Avg length       : ID={entry['avg_length_id']:.2f}, "
              f"OOD={entry['avg_length_ood']:.2f}")
        if "recombination_distance_id_ood" in entry:
            print(f"    Recomb distance  : {entry['recombination_distance_id_ood']:.4f}")


def _print_length_histogram(architectures: list[list[str]]) -> None:
    """Print ASCII histogram of architecture lengths."""
    lengths = [len(a) for a in architectures]
    if not lengths:
        print("    (no architectures)")
        return
    max_len = max(lengths)
    bins = list(range(1, max_len + 2))
    hist, edges = np.histogram(lengths, bins=bins)
    print(f"\n  Architecture length distribution (n={len(lengths)}):")
    for i in range(len(hist)):
        if hist[i] > 0:
            bar = "█" * min(hist[i] // max(1, max(hist) // 40), 40)
            pct = 100.0 * hist[i] / len(lengths)
            print(f"    len={edges[i]:.0f}: {hist[i]:>6d} ({pct:4.1f}%)  {bar}")
    print(f"    Mean: {np.mean(lengths):.2f}  Median: {np.median(lengths):.0f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Pfam data pipeline integration test")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--quick", type=int, metavar="N", default=0,
                       help="Parse first N families only (default: all)")
    group.add_argument("--full", action="store_true",
                       help="Parse all families (default if no --quick)")

    parser.add_argument("--cache", action="store_true",
                        help="Save processed artifacts to data/pfam/processed/")
    parser.add_argument("--sim-matrix", type=str, metavar="PATH",
                        help="Path to precomputed similarity matrix .npy")
    args = parser.parse_args()

    # Determine max records
    max_records: int | None = None
    label = "full"
    if args.quick:
        max_records = args.quick
        label = f"quick (first {max_records})"

    # Determine similarity matrix
    if args.sim_matrix:
        sim_path = args.sim_matrix
        if not os.path.isfile(sim_path):
            print(f"ERROR: similarity matrix not found: {sim_path}")
            sys.exit(1)
        print(f"  Using similarity matrix: {sim_path}")
    else:
        sim_path = None
        print("  NOTE: No similarity matrix provided — using identity matrix.")
        print("        Recombination distances will be 0.0.")
        print("        Run precompute_similarity_matrix() separately for production use.\n")

    # Load config for filtering defaults
    cfg = load_config(CONFIG_PATH) if os.path.isfile(CONFIG_PATH) else {}
    min_len = cfg.get("data", {}).get("min_domain_arch_length", 2)
    max_len = cfg.get("data", {}).get("max_domain_arch_length", 15)

    # ── Step 0: Count records ─────────────────────────────────
    print(f"Pfam Data Pipeline — {label}")
    print(f"  Seed file: {SEED_PATH}")
    print(f"  Config   : {CONFIG_PATH}")
    print(f"  Filters  : min_len={min_len}, max_len={max_len}")
    print()

    total_records = _count_records(SEED_PATH)
    if max_records is None or max_records > total_records:
        max_records = total_records
    print(f"  Total records in seed file: {total_records}")
    print(f"  Parsing: {max_records} records\n")

    t_start = time.perf_counter()

    # ── Step 1: Parse Stockholm ──────────────────────────────
    print("[1/5] Parsing Stockholm records ...")
    t0 = time.perf_counter()
    records = parse_stockholm(SEED_PATH, max_records=max_records)
    t1 = time.perf_counter()
    n_records = len(records)
    n_seq = sum(r["seq_count"] for r in records)
    print(f"  Parsed {n_records} records ({n_seq} sequences) in {t1 - t0:.1f}s")

    # ── Step 2: Extract domain architectures ─────────────────
    print("\n[2/5] Extracting domain architectures ...")
    t0 = time.perf_counter()
    architectures = extract_domain_architectures(
        records, min_length=min_len, max_length=max_len,
    )
    t1 = time.perf_counter()
    print(f"  Extracted {len(architectures)} architectures in {t1 - t0:.2f}s")
    # Memory: release records to free memory
    del records
    if not architectures:
        print("ERROR: no architectures extracted — cannot continue")
        sys.exit(1)

    # ── Step 3: Build vocabulary ─────────────────────────────
    print("\n[3/5] Building domain vocabulary ...")
    t0 = time.perf_counter()
    token2id, id2token, clan_map = build_domain_vocab(
        architectures, clan_map_path=CLANS_PATH,
    )
    t1 = time.perf_counter()
    n_families = len(token2id) - 5  # exclude special tokens
    print(f"  Vocabulary size: {len(token2id)} ({n_families} domain families + 5 special)")
    print(f"  Clans mapped   : {len(clan_map)}")
    print(f"  Token ID range : 0..{len(token2id) - 1}")
    print(f"  Build time     : {t1 - t0:.2f}s")

    # ── Step 4: Generate compositional splits ────────────────
    print("\n[4/5] Generating compositional splits ...")
    t0 = time.perf_counter()

    # Build identity similarity matrix (or load real one)
    accessions = [id2token[i] for i in range(5, len(token2id))]
    if sim_path:
        sim_matrix = np.load(sim_path)
    else:
        n = len(accessions)
        sim_matrix = np.eye(n, dtype=np.float32)

    try:
        splits = make_compositional_splits(
            architectures,
            sim_matrix,
            accessions,
            clans_tsv_path=CLANS_PATH,
        )
    except ValueError as e:
        print(f"  Split generation failed: {e}")
        sys.exit(1)

    t1 = time.perf_counter()
    print(f"  Splits generated in {t1 - t0:.2f}s")

    # ── Step 5: Report statistics ────────────────────────────
    print("\n[5/5] Computing split statistics ...")
    stats = compute_split_statistics(
        splits,
        similarity_matrix=sim_matrix if sim_path else None,
        accessions=accessions if sim_path else None,
    )
    _print_stats(stats)
    _print_length_histogram(architectures)

    # ── Summary ──────────────────────────────────────────────
    elapsed = time.perf_counter() - t_start
    all_nonempty = all(
        splits[t]["id"] and splits[t]["ood"]
        for t in ("type_a", "type_b", "type_c")
    )
    print(f"\n{'=' * 55}")
    print(f"PIPELINE {'PASSED' if all_nonempty else 'INCOMPLETE'}  ({elapsed:.1f}s)")
    print(f"{'=' * 55}")

    if all_nonempty:
        print(f"  Records parsed     : {n_records}")
        print(f"  Architectures      : {len(architectures)}")
        print(f"  Vocabulary size    : {len(token2id)}")
        def _ratio(t):
            return f"{len(splits[t]['id'])}:{len(splits[t]['ood'])}"
        print(f"  Type A ID:OOD      : {_ratio('type_a')}")
        print(f"  Type B ID:OOD      : {_ratio('type_b')}")
        print(f"  Type C ID:OOD      : {_ratio('type_c')}")
    else:
        print("  WARNING: one or more splits have empty sets")
        for t in ("type_a", "type_b", "type_c"):
            d = splits[t]
            print(f"  {t}: ID={len(d['id'])}, OOD={len(d['ood'])}")

    # ── Cache ────────────────────────────────────────────────
    if args.cache:
        _cache_artifacts(
            architectures, token2id, id2token, clan_map,
            splits, stats, sim_matrix if sim_path else None, accessions,
        )


def _cache_artifacts(
    architectures: list[list[str]],
    token2id: dict[str, int],
    id2token: dict[int, str],
    clan_map: dict[str, str],
    splits: dict,
    stats: dict,
    sim_matrix: np.ndarray | None,
    accessions: list[str],
) -> None:
    """Save processed artifacts to ``data/pfam/processed/``."""
    import torch

    os.makedirs(PROCESSED_DIR, exist_ok=True)
    print(f"\n── Caching to {PROCESSED_DIR}/ ──")

    # ── Raw architectures (JSON for inspection) ──
    arch_path = os.path.join(PROCESSED_DIR, "architectures.json")
    with open(arch_path, "w") as f:
        json.dump(architectures, f)
    print(f"  architectures.json    : {len(architectures)} architectures")

    # ── Tokenized architecture tensor ──
    max_len = max(len(a) for a in architectures) if architectures else 1
    pad_id = token2id.get("<PAD>", 0)
    n = len(architectures)
    tokens = np.full((n, max_len), pad_id, dtype=np.int64)
    for i, arch in enumerate(architectures):
        for j, d in enumerate(arch):
            tokens[i, j] = token2id.get(d, token2id.get("<UNK>", 4))
    tensor_path = os.path.join(PROCESSED_DIR, "architectures.pt")
    torch.save(torch.from_numpy(tokens), tensor_path)
    print(f"  architectures.pt      : {tokens.shape} int64 tensor")

    # ── Vocabulary JSON ──
    vocab_path = os.path.join(PROCESSED_DIR, "vocab.json")
    with open(vocab_path, "w") as f:
        json.dump({"token2id": token2id, "id2token": {int(k): v for k, v in id2token.items()}}, f)
    print(f"  vocab.json            : {len(token2id)} tokens")

    # ── Clan map ──
    clan_path = os.path.join(PROCESSED_DIR, "clan_map.json")
    with open(clan_path, "w") as f:
        json.dump(clan_map, f)
    print(f"  clan_map.json         : {len(clan_map)} clans")

    # ── Split indices ──
    # Convert architecture lists to indices for efficient loading
    arch_list = list(architectures)
    arch_index = {id(a): i for i, a in enumerate(arch_list)}
    split_indices: dict = {}
    for stype in ("type_a", "type_b", "type_c"):
        split_indices[stype] = {}
        for subset in ("id", "ood"):
            subset_archs = splits[stype][subset]
            indices = [arch_index[id(a)] for a in subset_archs]
            split_indices[stype][subset] = indices

    splits_path = os.path.join(PROCESSED_DIR, "splits.pt")
    torch.save(split_indices, splits_path)
    print("  splits.pt             : 3 types x 2 subsets = 6 index lists")

    # ── Split statistics ──
    stats_path = os.path.join(PROCESSED_DIR, "split_stats.json")
    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=2)
    print("  split_stats.json      : 3 split types")

    # ── Similarity matrix copy ──
    sim_out = os.path.join(PROCESSED_DIR, "similarity_matrix.npy")
    if sim_matrix is not None and not os.path.isfile(sim_out):
        np.save(sim_out, sim_matrix)
        print(f"  similarity_matrix.npy : {sim_matrix.shape} float32")

    print(f"\n  Cached to {PROCESSED_DIR}/ — ready for Phase 02+")


if __name__ == "__main__":
    main()
