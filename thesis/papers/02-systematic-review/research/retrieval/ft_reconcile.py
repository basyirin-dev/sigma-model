#!/usr/bin/env python3
"""
Paper 02 — Phase 6 full-text eligibility reconciliation (Tasks 6.2-6.3)

Combines the two independent full-text assessments (S1 + S2) with the
retrieval statuses and produces the final eligibility file:

  - unretrieved records        -> Exclude FT5 (task 6.1.4 / 6.2.4)
  - consensus Include/Exclude  -> kept
  - disagreement or any Uncertain -> conflict (6.3.1); per protocol 6.3.3
    no-consensus cases default to Include but are flagged for human review
  - near-duplicate titles      -> FT6 candidates flagged (human confirms)

Also computes Cohen's kappa (3-way + binary) between S1 and S2 (CC.1.6) and
draws the 20% validation sample for the human validation pass (seed fixed).

Usage:
  python ft_reconcile.py

Outputs:
  research/retrieval/eligibility-decisions.csv   (all 395)
  research/retrieval/fulltext-exclusions.md      (FT1-FT8 counts + lists)
  research/retrieval/ft-conflicts.md             (conflict log, task 6.3)
  research/retrieval/validation-20.csv           (20% human validation sample)
"""

from __future__ import annotations

import csv
import difflib
import random
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
RETR = BASE / "research" / "retrieval"
POOL_CSV = BASE / "research" / "screening-data" / "full-text" / "records-to-review.csv"
S1_CSV = RETR / "ft-assessment-s1.csv"
S2_CSV = RETR / "ft-assessment-s2.csv"
OUT_CSV = RETR / "eligibility-decisions.csv"
EXCL_MD = RETR / "fulltext-exclusions.md"
CONFLICTS_MD = RETR / "ft-conflicts.md"
VALIDATION_CSV = RETR / "validation-20.csv"

VALIDATION_SEED = 20260804
VALIDATION_FRACTION = 0.20

INCLUDE, EXCLUDE, UNCERTAIN = "Include", "Exclude", "Uncertain"

FT_LABELS = {
    "FT1": "No OOD/compositional split reported",
    "FT2": "Only ID results reported",
    "FT3": "Insufficient quantitative detail (no accuracy numbers, no extractable data)",
    "FT4": "Not actually about neural network models",
    "FT5": "Full text unavailable (after 3 attempts)",
    "FT6": "Duplicate content (superseded by later publication)",
    "FT7": "Review or opinion paper without original results",
    "FT8": "Other (specify)",
}


def kappa(a: list[str], b: list[str]) -> float:
    n = len(a)
    if n == 0:
        return 0.0
    cats = set(a) | set(b)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pe = sum((sum(1 for x in a if x == c) / n) * (sum(1 for y in b if y == c) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe != 1 else 1.0


def binary_kappa(a: list[str], b: list[str]) -> tuple[float, int]:
    hard = [(x, y) for x, y in zip(a, b) if x != UNCERTAIN and y != UNCERTAIN]
    if len(hard) < 2:
        return 0.0, len(hard)
    return kappa([x for x, _ in hard], [y for _, y in hard]), len(hard)


def normalize_title(t: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()


def find_duplicate_candidates(titles: dict[str, str]) -> list[tuple[str, str, float]]:
    """Near-duplicate title pairs -> FT6 candidates (human confirms)."""
    norms = {rid: normalize_title(t) for rid, t in titles.items() if t}
    ids = list(norms)
    out = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = norms[ids[i]], norms[ids[j]]
            if not a or not b:
                continue
            r = difflib.SequenceMatcher(None, a, b).ratio()
            if r >= 0.90:
                out.append((ids[i], ids[j], round(r, 3)))
    return out


def main() -> None:
    with open(POOL_CSV, "r", encoding="utf-8") as f:
        pool = {r["id"]: r for r in csv.DictReader(f)}
    with open(S1_CSV, "r", encoding="utf-8") as f:
        s1 = {r["id"]: r for r in csv.DictReader(f)}
    with open(S2_CSV, "r", encoding="utf-8") as f:
        s2 = {r["id"]: r for r in csv.DictReader(f)}

    assessed_ids = [rid for rid, rec in pool.items() if rec.get("ft_pdf_path")]
    s1_dec = [s1[rid]["decision"] for rid in assessed_ids]
    s2_dec = [s2[rid]["decision"] for rid in assessed_ids]

    k3 = kappa(s1_dec, s2_dec)
    kb, kn = binary_kappa(s1_dec, s2_dec)

    # ── Merge ─────────────────────────────────────────────────────────
    rows = []
    conflicts: list[tuple[str, str, str, str]] = []
    stats = Counter()
    reasons = Counter()

    for rid, rec in pool.items():
        retrieved = bool(rec.get("ft_pdf_path"))
        if not retrieved:
            rows.append({
                "id": rid, "title": rec.get("title", ""), "year": rec.get("year", ""),
                "decision": EXCLUDE, "reason": "FT5", "retrieved": "no",
                "s1": "", "s2": "", "note": "full text unavailable after 3 attempts",
            })
            stats[EXCLUDE] += 1
            reasons["FT5"] += 1
            continue

        d1, r1 = s1[rid]["decision"], s1[rid]["reason"]
        d2, r2 = s2[rid]["decision"], s2[rid]["reason"]
        if d1 == d2 and d1 != UNCERTAIN:
            decision, reason, note = d1, r1 or r2, f"s1={d1} s2={d2}"
            if decision == EXCLUDE:
                reasons[reason] += 1
        else:
            conflicts.append((rid, d1, d2, rec.get("title", "")))
            decision, reason, note = INCLUDE, "", "conflict: default Include (6.3.3); flagged"
        rows.append({
            "id": rid, "title": rec.get("title", ""), "year": rec.get("year", ""),
            "decision": decision, "reason": reason, "retrieved": "yes",
            "s1": d1, "s2": d2, "note": note,
        })
        stats[decision] += 1
        if decision == EXCLUDE:
            reasons[reason] += 1

    # ── FT6 duplicate candidates (human confirms; retrieved records only) ──
    dup = find_duplicate_candidates(
        {r["id"]: r["title"] for r in rows if r["retrieved"] == "yes"}
    )
    if dup:
        dup_ids = {rid for pair in dup for rid in pair}
        for row in rows:
            if row["id"] in dup_ids and row["decision"] == INCLUDE:
                row["note"] = (row["note"] + " | FT6-dup-candidate").strip(" |")
                row["decision"] = UNCERTAIN  # flag for discussion, don't auto-exclude
                stats[INCLUDE] -= 1
                stats[UNCERTAIN] += 1

    # ── Write eligibility decisions ───────────────────────────────────
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "year", "decision", "reason",
                                          "retrieved", "s1", "s2", "note"])
        w.writeheader()
        w.writerows(rows)

    # ── Exclusions report ─────────────────────────────────────────────
    excl = [r for r in rows if r["decision"] == EXCLUDE]
    with open(EXCL_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Full-Text Exclusions (Task 6.2/6.4)\n\n")
        f.write(f"**Total excluded at full-text stage**: {len(excl)}\n\n")
        f.write("| Code | Reason | Count |\n")
        f.write("|------|--------|------:|\n")
        for code, label in FT_LABELS.items():
            f.write(f"| {code} | {label} | {reasons[code]} |\n")
        f.write("\n## Excluded Records (by code, first 50 per code)\n\n")
        for code in FT_LABELS:
            items = [r for r in excl if r["reason"] == code][:50]
            if not items:
                continue
            f.write(f"### {code}: {FT_LABELS[code]}\n\n")
            f.write("| ID | Title |\n")
            f.write("|----|-------|\n")
            for r in items:
                f.write(f"| {r['id']} | {r['title'][:70]} |\n")
            f.write("\n")

    # ── Conflict log (task 6.3) ───────────────────────────────────────
    with open(CONFLICTS_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Full-Text Conflict Log (Task 6.3)\n\n")
        f.write(f"**Conflicts (S1 vs S2 disagreement or Uncertain)**: {len(conflicts)}\n\n")
        f.write("Resolution per protocol 6.3.2-6.3.3: discussed against criteria "
                "definitions; no consensus -> default to Include, flagged for "
                "human validation (20% sample + this log).\n\n")
        f.write("| ID | S1 | S2 | Title |\n")
        f.write("|----|----|----|-------|\n")
        for rid, d1, d2, t in conflicts:
            f.write(f"| {rid} | {d1} | {d2} | {t[:70]} |\n")

    # ── 20% validation sample (CC.1.6) ────────────────────────────────
    rng = random.Random(VALIDATION_SEED)
    sample_ids = set(rng.sample(assessed_ids, max(1, int(len(assessed_ids) * VALIDATION_FRACTION))))
    with open(VALIDATION_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "decision", "reason", "s1", "s2"])
        w.writeheader()
        for r in rows:
            if r["id"] in sample_ids:
                w.writerow({k: r.get(k, "") for k in
                            ["id", "title", "decision", "reason", "s1", "s2"]})

    # ── Summary ───────────────────────────────────────────────────────
    print("Eligibility decisions (all 395):")
    for d, c in stats.most_common():
        print(f"  {d:10s} {c}")
    print("Exclusion reasons:", dict(reasons.most_common()))
    print(f"Kappa S1 vs S2: 3-way {k3:.3f} | binary {kb:.3f} (n={kn})")
    print(f"Conflicts: {len(conflicts)} | FT6-dup candidates: {len(dup)}")
    print(f"Validation sample: {len(sample_ids)} records (seed={VALIDATION_SEED})")
    print(f"Outputs: {OUT_CSV.name}, {EXCL_MD.name}, {CONFLICTS_MD.name}, {VALIDATION_CSV.name}")


if __name__ == "__main__":
    main()
