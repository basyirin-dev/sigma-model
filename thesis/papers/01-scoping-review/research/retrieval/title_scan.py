#!/usr/bin/env python3
"""
Paper 01 — Phase 6: title-based scan of research/pdfs/ to catch every
file that matches an included study, regardless of filename convention.

Strategy per PDF:
  1. Extract first-page text (pdfminer), skip non-Latin (foreign).
  2. Reconstruct arXiv ID from garbled header if present.
  3. Match by normalized title prefix/containment (strict, min title len 25).
  4. Fallback: first-author surname + year among user-style files.
Then update annotations (has_pdf/needs_download/pdf_status/pdf_path) and
regenerate the queue.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

from pdfminer.high_level import extract_text

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
PDF_DIR = BASE / "research" / "pdfs"
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"

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


def main():
    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))
    annot_by_sid = {r["study_id"]: r for r in annot}

    # study index
    title_idx = {}
    arxiv_idx = {}
    for r in annot:
        t = norm(r.get("title", ""))
        if len(t) >= 25:
            title_idx.setdefault(t, r)
        aid = (r.get("arxiv_id") or "").strip().split("v")[0]
        if aid:
            arxiv_idx.setdefault(aid, r)

    # claim map: study_id -> [pdf filenames]
    claims: dict[str, list[str]] = {}
    file_claims: dict[str, list[str]] = {}  # file -> studies claiming it
    foreign = []

    for p in sorted(PDF_DIR.glob("*.pdf")):
        try:
            first = extract_text(str(p), page_numbers=[0], maxpages=1)[:700]
        except Exception:
            continue
        if has_non_latin(first):
            foreign.append(p.name)
            continue
        cand = norm(first)
        aid = extract_arxiv_id(first)

        rec = None
        if len(cand) > 30:
            best, best_score = None, 0
            for k, v in title_idx.items():
                score = 0
                if cand[:60] == k[:60] or cand[:50] == k[:50]:
                    score = 3
                elif k in cand and len(k) >= 35:
                    score = 2
                elif k[:40] in cand[:220] and len(k) >= 30:
                    score = 1
                if score > best_score:
                    best_score, best = score, v
            rec = best
        if rec is None and aid:
            rec = arxiv_idx.get(aid)
        if rec:
            # record claim; resolve single-claim later
            file_claims.setdefault(p.name, []).append(rec["study_id"])

    # Only accept files claimed by EXACTLY ONE study (no over-claiming);
    # ambiguous files leave all candidate studies in the queue.
    for fname, sids in file_claims.items():
        uniq = list(dict.fromkeys(sids))
        if len(uniq) == 1:
            claims.setdefault(uniq[0], []).append(fname)

    # filename fallback: for studies still unmatched, try surname+year
    user_files = [p.name for p in PDF_DIR.glob("*.pdf")
                  if "_arxiv" not in p.name and "_oa" not in p.name]
    claimed_files = {f for v in claims.values() for f in v}
    for r in annot:
        if r["study_id"] in claims:
            continue
        authors = (r.get("authors") or "")
        year = (r.get("year") or "").strip()
        if not authors or not year:
            continue
        surname = authors.split(";")[0].split(",")[0].strip().split()[-1].lower()
        cands = [f for f in user_files
                 if Path(f).stem.lower().replace("_", " ").startswith(surname)
                 and year in f and f not in claimed_files]
        if len(cands) == 1:
            claims.setdefault(r["study_id"], []).append(cands[0])

    # ---- update annotations ----
    updated = 0
    for sid, files in claims.items():
        r = annot_by_sid.get(sid)
        if not r:
            continue
        if r["has_pdf"] != "yes":
            r["has_pdf"] = "yes"
            r["needs_download"] = "no"
            r["pdf_status"] = "retrieved-file"
            updated += 1
        r["pdf_path"] = PDF_PREFIX + Path(files[0]).name
        r["pdf_status"] = "retrieved-file"

    with open(ANNOT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(annot[0].keys()))
        w.writeheader()
        w.writerows(annot)

    from collections import Counter
    print(f"Files scanned: {len(list(PDF_DIR.glob('*.pdf')))} | foreign skipped: {len(foreign)}")
    print(f"Studies claimed: {len(claims)} | newly marked has_pdf=yes: {updated}")
    print("Annotations:", dict(Counter(r["has_pdf"] for r in annot)))
    print("Foreign:", foreign[:10])


if __name__ == "__main__":
    main()
