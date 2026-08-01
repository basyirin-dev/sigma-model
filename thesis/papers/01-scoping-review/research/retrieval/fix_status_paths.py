#!/usr/bin/env python3
"""
Paper 01 — Phase 6: fix retrieval-status.pdf_path entries.

- Resolve stored paths against the real pdfs folder; drop entries whose
  file does not exist.
- Drop known-wrong assignments: foreign-language versions (Aoki_2026,
  Snetkov_2025) and mismapped files (Liu_2026 -> Cybersecurity,
  Safron_2023 -> Deceptive alignment).
- Then rebuild download flags from disk.
"""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
PDF_DIR = BASE / "research" / "pdfs"

# pdf files that must NOT count as full texts (foreign language / wrong paper)
EXCLUDE_FILES = {
    "Aoki_2026.pdf",        # Japanese version of P193
    "Aoki_2026_oa.pdf",
    "Snetkov_2025.pdf",     # Russian version of P276
    "Snetkov_2025_oa.pdf",
    "Jin_2025.pdf",         # Chinese psychology journal, not in library
    "Liu_2026.pdf",         # Chinese journal, not mapped to any study
    "Aganova_2025_oa.pdf",  # foreign-language OA
    "Villaver_2026_oa.pdf", # foreign-language OA
    "Li_2026_oa.pdf",       # foreign-language OA
}

# record-id -> file that was wrongly assigned
WRONG_ASSIGNMENTS = {
    "P01_0787": "Liu_2026.pdf",       # Cybersecurity got Chinese journal
    "P01_2443": "Safron_2023.pdf",    # 'Deceptive alignment' got Value-Cores file
}


def main():
    with open(STATUS_CSV, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())

    fixed = 0
    dropped = 0
    for r in rows:
        p = (r.get("pdf_path") or "").strip()
        if not p:
            continue
        fname = Path(p).name

        # wrong assignments -> clear
        if r["id"] in WRONG_ASSIGNMENTS and WRONG_ASSIGNMENTS[r["id"]] == fname:
            r["pdf_path"] = ""
            r["status"] = "no-doi" if r.get("doi", "") == "" else "paywalled"
            dropped += 1
            continue

        # excluded files (foreign / not in library) -> clear
        if fname in EXCLUDE_FILES:
            r["pdf_path"] = ""
            r["status"] = "no-pdf-foreign"
            dropped += 1
            continue

        # resolve actual file: check both path conventions
        candidate = PDF_DIR / fname
        if not candidate.exists():
            # maybe stored relative to repo root under thesis/...
            alt = BASE.parent.parent / p
            if not alt.exists():
                r["pdf_path"] = ""
                r["status"] = "missing-file"
                dropped += 1
                continue

        # normalize to paper-relative path
        r["pdf_path"] = f"thesis/papers/01-scoping-review/research/pdfs/{fname}"
        if not r["status"].startswith("retrieved"):
            r["status"] = "retrieved-file"
        fixed += 1

    with open(STATUS_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    print(f"Fixed paths: {fixed}, dropped: {dropped}")
    print("Status distribution:", dict(Counter(r["status"] for r in rows)))
    print("Remaining research-relative paths:",
          sum(1 for r in rows if (r.get("pdf_path") or "").startswith("research/")))


if __name__ == "__main__":
    main()
