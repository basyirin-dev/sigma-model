#!/usr/bin/env python3
"""
Paper 01 — Phase 6: unmark studies whose PDF file is corrupt/invalid.

Detects invalid PDFs (extraction error / error-page files) and clears
has_pdf for studies pointing only at those files. Valid alternatives
per study are kept.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from pdfminer.high_level import extract_text

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
PDF_DIR = BASE / "research" / "pdfs"
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
PDF_PREFIX = "thesis/papers/01-scoping-review/research/pdfs/"

# uniform suspicious sizes seen in corrupt downloads (bytes)
SUSPECT_SIZES = {2663, 2677, 2711, 2717, 2719, 2726, 2732, 2756, 2943, 2946,
                 3038, 29963, 60799, 105481}


def is_valid_pdf(p: Path) -> bool:
    if not p.exists():
        return False
    size = p.stat().st_size
    if size in SUSPECT_SIZES or size < 2000:
        return False
    try:
        extract_text(str(p), page_numbers=[0], maxpages=1)
        return True
    except Exception:
        return False


def main():
    # cache validity per file
    valid_cache: dict[str, bool] = {}
    for p in PDF_DIR.glob("*.pdf"):
        valid_cache[p.name] = is_valid_pdf(p)

    corrupt = [n for n, v in valid_cache.items() if not v]
    print(f"Corrupt/invalid PDFs: {len(corrupt)} / {len(valid_cache)}")

    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))

    # group studies by file; a study is OK if it has >=1 valid file
    unmarked = 0
    for r in annot:
        p = (r.get("pdf_path") or "")
        if not p or r["has_pdf"] != "yes":
            continue
        fname = Path(p).name
        if valid_cache.get(fname, False):
            continue  # valid file, keep
        # invalid file: unmark unless another valid file exists for this study
        other_valid = False
        # (we only store one pdf_path per study, so no alternative)
        r["has_pdf"] = "no"
        r["needs_download"] = "yes"
        r["pdf_status"] = "corrupt-file"
        r["pdf_path"] = ""
        unmarked += 1

    with open(ANNOT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(annot[0].keys()))
        w.writeheader()
        w.writerows(annot)

    print(f"Studies unmarked (corrupt file): {unmarked}")
    print("Annotations:", dict(Counter(r["has_pdf"] for r in annot)))
    with open(BASE / "research/retrieval/corrupt-files.txt", "w") as f:
        for n in sorted(corrupt):
            f.write(n + "\n")


if __name__ == "__main__":
    main()
