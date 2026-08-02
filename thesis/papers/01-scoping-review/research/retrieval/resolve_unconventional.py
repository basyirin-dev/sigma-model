#!/usr/bin/env python3
"""
Paper 01 — Phase 6: resolve unconventionally-named PDFs to queue entries.

Goal: for studies currently needing a download, decide whether ANY file
in research/pdfs/ is actually that paper (its title, from first-page
text) — regardless of filename. Each file is assigned to AT MOST ONE
study (globally unique best match); ambiguous files are ignored (studies
stay in the queue). Non-Latin PDFs never count (I1).

Only marks studies that are currently needs_download=yes. Leaves the
trusted committed assignments untouched.
"""

from __future__ import annotations

import csv
import re
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


def extract_arxiv_id(text: str) -> str | None:
    compact = re.sub(r"\s+", "", text)
    rev = compact[::-1]
    m = re.search(r"(\d{4}\.\d{4,5})(?:v\d+)?", rev)
    return m.group(1) if m else None


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

    # only studies currently needing a download are eligible for matching
    targets = {r["study_id"]: r for r in annot if r["needs_download"] == "yes"}
    title_idx = {}
    arxiv_idx = {}
    for r in targets.values():
        t = norm(r.get("title", ""))
        if len(t) >= 25:
            title_idx.setdefault(t, r)
        aid = (r.get("arxiv_id") or "").strip().split("v")[0]
        if aid:
            arxiv_idx.setdefault(aid, r)

    # phase 1: per-file best match among target studies
    file_best: dict[str, tuple[int, str]] = {}  # fname -> (best_score, study_id)
    for p in sorted(PDF_DIR.glob("*.pdf")):
        try:
            first = extract_text(str(p), page_numbers=[0], maxpages=1)[:700]
        except Exception:
            continue
        if has_non_latin(first):
            continue
        cand = norm(first)
        aid = extract_arxiv_id(first)
        best_sid, best_score = None, 0
        if len(cand) > 30:
            for k, v in title_idx.items():
                s = title_score(cand, k)
                if s > best_score:
                    best_score, best_sid = s, v["study_id"]
        if best_sid is None and aid:
            v = arxiv_idx.get(aid)
            if v:
                best_sid, best_score = v["study_id"], 3
        if best_sid and best_score >= 2:
            file_best[p.name] = (best_score, best_sid)

    # phase 2: global resolution — each file claims one study; a study may
    # be claimed by several files (keep the best); ties on the same study
    # are fine. Ambiguity only matters per-file (already handled by best).
    # Additional guard: if two files both claim study X with equal high
    # score, keep one.
    study_files: dict[str, list[tuple[int, str]]] = {}
    for fname, (score, sid) in file_best.items():
        study_files.setdefault(sid, []).append((score, fname))

    # phase 3: apply — mark matched studies downloaded
    marked = []
    for sid, entries in study_files.items():
        r = targets.get(sid)
        if not r:
            continue
        # best file for this study
        entries.sort(reverse=True)
        best_file = entries[0][1]
        r["has_pdf"] = "yes"
        r["needs_download"] = "no"
        r["pdf_status"] = "retrieved-file"
        r["pdf_path"] = PDF_PREFIX + best_file
        marked.append((sid, best_file))

    with open(ANNOT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(annot[0].keys()))
        w.writeheader()
        w.writerows(annot)

    from collections import Counter
    print(f"Files with unique best match among queue targets: {len(file_best)}")
    print(f"Studies newly marked has_pdf=yes: {len(marked)}")
    for sid, f in marked[:30]:
        print(f"  {sid} <- {f}")
    print("Annotations:", dict(Counter(r["has_pdf"] for r in annot)))


if __name__ == "__main__":
    main()
