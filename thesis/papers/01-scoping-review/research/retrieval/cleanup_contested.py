#!/usr/bin/env python3
"""
Paper 01 — Phase 6: resolve multi-claimed files in annotations.csv.

For each PDF file assigned to >1 study, extract the file's true title
(first-page text) and keep only the study whose title best matches it
(score >= 2). Un-mark the other studies (has_pdf=no) unless they hold a
DIFFERENT unique file. Files with no decisive match leave all studies
unmarked.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

from pdfminer.high_level import extract_text

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
PDF_DIR = BASE / "research" / "pdfs"
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
PDF_PREFIX = "thesis/papers/01-scoping-review/research/pdfs/"

NON_LATIN = [(0x4E00, 0x9FFF), (0x3040, 0x30FF), (0x0400, 0x04FF),
             (0x0600, 0x06FF), (0xAC00, 0xD7AF), (0x0E00, 0x0E7F)]


def has_non_latin(text: str) -> bool:
    for ch in text:
        cp = ord(ch)
        for lo, hi in NON_LATIN:
            if lo <= cp <= hi:
                return True
    return False


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def title_score(cand: str, k: str) -> int:
    if len(k) < 25:
        return 0
    if cand[:60] == k[:60] or cand[:50] == k[:50]:
        return 3
    if k in cand and len(k) >= 35:
        return 2
    if k[:40] in cand[:220] and len(k) >= 30:
        return 1
    return 0


def main():
    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))
    by_sid = {r["study_id"]: r for r in annot}

    # file -> studies
    file_studies = defaultdict(list)
    for r in annot:
        p = (r.get("pdf_path") or "")
        if p:
            file_studies[p.split("/")[-1]].append(r["study_id"])

    contested = {f: list(dict.fromkeys(sids)) for f, sids in file_studies.items()
                 if len(set(sids)) > 1}
    print(f"Contested files: {len(contested)}")

    unmarked = 0
    for fname, sids in contested.items():
        p = PDF_DIR / fname
        if not p.exists():
            continue
        try:
            first = extract_text(str(p), page_numbers=[0], maxpages=1)[:700]
        except Exception:
            continue
        if has_non_latin(first):
            # foreign file: unmark ALL (not a valid I1 full text)
            for sid in sids:
                r = by_sid[sid]
                if r["has_pdf"] == "yes" and r.get("pdf_path", "").endswith(fname):
                    r["has_pdf"] = "no"; r["needs_download"] = "yes"
                    r["pdf_status"] = "no-pdf"; r["pdf_path"] = ""
                    unmarked += 1
            continue
        cand = norm(first)
        scored = []
        for sid in sids:
            r = by_sid[sid]
            s = title_score(cand, norm(r.get("title", "")))
            scored.append((s, sid))
        scored.sort(reverse=True)
        best_score, best_sid = scored[0]
        if best_score >= 2:
            # keep best only; unmark others IF they point to this file
            for s, sid in scored:
                if sid == best_sid:
                    continue
                r = by_sid[sid]
                if r.get("pdf_path", "").endswith(fname):
                    r["has_pdf"] = "no"; r["needs_download"] = "yes"
                    r["pdf_status"] = "no-pdf"; r["pdf_path"] = ""
                    unmarked += 1
        else:
            # no decisive match: unmark all pointing to this file
            for sid in sids:
                r = by_sid[sid]
                if r.get("pdf_path", "").endswith(fname):
                    r["has_pdf"] = "no"; r["needs_download"] = "yes"
                    r["pdf_status"] = "no-pdf"; r["pdf_path"] = ""
                    unmarked += 1

    with open(ANNOT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(annot[0].keys()))
        w.writeheader()
        w.writerows(annot)

    from collections import Counter
    print(f"Unmarked (contested): {unmarked}")
    print("Annotations:", dict(Counter(r["has_pdf"] for r in annot)))


if __name__ == "__main__":
    main()
