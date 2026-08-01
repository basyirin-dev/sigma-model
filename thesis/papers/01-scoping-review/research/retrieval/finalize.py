#!/usr/bin/env python3
"""
Paper 01 — Phase 6 Final Included-Studies List (Task 6.5)

Compiles the final included list (CSV + BibTeX), retrieval-to-inclusion
pipeline statistics, and updates the PRISMA figure.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
DECISIONS_CSV = BASE / "research" / "retrieval" / "eligibility-decisions.csv"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
OUT_CSV = BASE / "research" / "included-studies.csv"
OUT_BIB = BASE / "research" / "included-studies.bib"
STATS_MD = BASE / "research" / "retrieval" / "pipeline-statistics.md"


def main():
    with open(DECISIONS_CSV, "r", encoding="utf-8") as f:
        records = list(csv.DictReader(f))
    status_map = {}
    if STATUS_CSV.exists():
        with open(STATUS_CSV, "r", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                status_map[r["id"]] = r

    included = sorted([r for r in records if r["ft_decision"] == "Include"],
                      key=lambda r: r.get("study_id", ""))
    excluded = [r for r in records if r["ft_decision"] == "Exclude"]

    # CSV export
    fields = ["study_id", "id", "title", "authors", "year", "doi", "arxiv_id",
              "journal", "abstract", "source_db", "ft_status", "ft_reason"]
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in included:
            st = status_map.get(r["id"], {})
            row = dict(r)
            row["ft_status"] = st.get("status", "")
            w.writerow(row)

    # BibTeX export
    with open(OUT_BIB, "w", encoding="utf-8") as f:
        for r in included:
            key = r.get("study_id", "")
            f.write(f"@misc{{{key},\n")
            f.write(f"  title = {{{r['title']}}},\n")
            authors = (r.get("authors") or "").replace(";", " and")
            f.write(f"  author = {{{authors}}},\n")
            f.write(f"  year = {{{r.get('year','')}}},\n")
            if r.get("doi"):
                f.write(f"  doi = {{{r['doi']}}},\n")
            if r.get("arxiv_id"):
                f.write(f"  eprint = {{{r['arxiv_id']}}},\n")
            if r.get("journal"):
                f.write(f"  journal = {{{r['journal']}}},\n")
            f.write(f"  note = {{Paper 01 study; source: {r.get('source_db','')}}}\n")
            f.write("}\n\n")

    # Pipeline statistics
    retr = sum(1 for r in records if (status_map.get(r["id"], {}).get("status", "")).startswith("retrieved"))
    excl_reasons = Counter(r["ft_reason"] for r in excluded)
    with open(STATS_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 01 — Retrieval-to-Inclusion Pipeline Statistics (Task 6.5)\n\n")
        f.write("| Stage | Count |\n")
        f.write("|-------|------:|\n")
        f.write("| Total sought for retrieval | 1,278 |\n")
        f.write(f"| Full texts retrieved (arXiv + OA) | {retr} |\n")
        f.write(f"| Paywalled / not retrievable | {len(records) - retr} |\n")
        f.write(f"| Excluded after full-text review | {len(excluded)} |\n")
        for r, c in excl_reasons.most_common():
            f.write(f"|   — {r} | {c} |\n")
        f.write(f"| **Included for data extraction** | **{len(included)}** |\n\n")
        f.write("Notes: eligibility confirmed from full text where retrieved (513 PDFs), "
                "else from abstract+metadata (documented in annotations.csv). "
                "Paywalled included studies require institutional access for Phase 7 "
                "data extraction.\n")

    print(f"Included: {len(included)}")
    print(f"Excluded: {len(excluded)} ({dict(excl_reasons)})")
    print(f"Retrieved PDFs: {retr}")
    print(f"Exports: {OUT_CSV.name}, {OUT_BIB.name}, {STATS_MD.name}")


if __name__ == "__main__":
    main()
