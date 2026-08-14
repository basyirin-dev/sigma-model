#!/usr/bin/env python3
"""
Paper 02 — Phase 6 final included studies (Task 6.4)

Compiles the final list of included studies from the adjudicated
eligibility decisions, assigns Study IDs S001-SXXX (task 6.4.2), compiles
the excluded full-text list with reasons (6.4.3), and computes the
inclusion rate: included / retrieved full-text (6.4.4).

Usage:
  python ft_included.py

Outputs:
  research/included-studies.csv        (final Included, S001-SXXX)
  research/excluded-fulltext.csv       (Excluded with FT reasons)
  prints inclusion rate
"""

from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
RETR = BASE / "research" / "retrieval"
POOL_CSV = BASE / "research" / "screening-data" / "full-text" / "records-to-review.csv"
ELIG_CSV = RETR / "eligibility-decisions.csv"
INC_CSV = BASE / "research" / "included-studies.csv"
EXC_CSV = BASE / "research" / "excluded-fulltext.csv"

FIELDS = ["study_id", "id", "title", "authors", "year", "doi", "arxiv_id",
          "source_db", "journal", "url"]


def main() -> None:
    with open(POOL_CSV, "r", encoding="utf-8") as f:
        pool = {r["id"]: r for r in csv.DictReader(f)}
    with open(ELIG_CSV, "r", encoding="utf-8") as f:
        elig = list(csv.DictReader(f))

    included = sorted((r for r in elig if r["decision"] == "Include"), key=lambda r: r["id"])
    excluded = sorted((r for r in elig if r["decision"] == "Exclude"), key=lambda r: r["id"])

    for i, row in enumerate(included, 1):
        row["study_id"] = f"S{i:03d}"

    with open(INC_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for row in included:
            rec = pool[row["id"]]
            out = {k: rec.get(k, "") for k in FIELDS}
            out["study_id"] = row["study_id"]
            w.writerow(out)

    with open(EXC_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "year", "reason", "note"],
                           extrasaction="ignore")
        w.writeheader()
        for row in excluded:
            w.writerow({"id": row["id"], "title": row["title"], "year": row["year"],
                        "reason": row["reason"], "note": row["note"]})

    retrieved = sum(1 for r in elig if r["retrieved"] == "yes")
    rate = len(included) / retrieved * 100 if retrieved else 0.0

    print(f"Included studies: {len(included)} (S001-S{len(included):03d})")
    print(f"Excluded at full-text stage: {len(excluded)}")
    print(f"Retrieved full texts assessed: {retrieved}")
    print(f"Inclusion rate (6.4.4): {len(included)}/{retrieved} = {rate:.1f}%")
    print(f"Outputs: {INC_CSV.name}, {EXC_CSV.name}")


if __name__ == "__main__":
    main()
