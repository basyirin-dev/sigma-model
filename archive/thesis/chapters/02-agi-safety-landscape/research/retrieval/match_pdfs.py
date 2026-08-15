#!/usr/bin/env python3
"""
Paper 01 — Phase 6: robust match of user-downloaded PDFs to studies.

Handles: arXiv reversed headers (digits/letters scrambled by extraction),
title containment, arXiv ID extraction from garbled header, foreign-
language detection, duplicate detection vs automated downloads.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path
from collections import Counter

from pdfminer.high_level import extract_text

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
PDF_DIR = BASE / "research" / "pdfs"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"

# Non-Latin script detection (CJK, Cyrillic, etc.)
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
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def extract_arxiv_id(text: str) -> str | None:
    """Extract arXiv ID from garbled header like '9 1 0 2  r p A ... 1 v 0 4 5 1 0 . 4 0 9'."""
    # reconstruct reversed char stream: remove spaces, reverse
    compact = re.sub(r"\s+", "", text)
    rev = compact[::-1]
    m = re.search(r"(\d{4}\.\d{4,5})(?:v\d+)?", rev)
    if m:
        return m.group(1)
    return None


def main():
    with open(INCLUDED_CSV, "r", encoding="utf-8") as f:
        included = list(csv.DictReader(f))
    title_idx = {}
    for r in included:
        title_idx.setdefault(norm(r["title"]), r)

    with open(STATUS_CSV, "r", encoding="utf-8") as f:
        status_rows = list(csv.DictReader(f))
    status_by_id = {r["id"]: r for r in status_rows}

    user_pdfs = sorted(p for p in PDF_DIR.glob("*.pdf")
                       if "_arxiv" not in p.name and "_oa" not in p.name)
    print(f"User-style PDFs to match: {len(user_pdfs)}")

    results = []
    for p in user_pdfs:
        try:
            first_text = extract_text(str(p), page_numbers=[0], maxpages=1)[:600]
        except Exception as e:
            results.append({"pdf": p.name, "study": None, "match": "ERROR",
                            "arxiv": "", "lang": "", "note": str(e)[:40]})
            continue

        # 1. foreign-language check
        lang = "non-EN" if has_non_latin(first_text) else "EN"

        # 2. arXiv ID from garbled header
        aid = extract_arxiv_id(first_text)
        rec = None
        match_kind = "none"

        # 3. title matching — strict: require record title >= 25 chars,
        #    exact/prefix match first, strong containment only for long titles.
        cand = norm(first_text)
        if len(cand) > 30:
            best = None
            best_score = 0
            for k, v in title_idx.items():
                if len(k) < 25:
                    continue  # skip generic short titles like "AI alignment"
                score = 0
                if cand[:60] == k[:60] or cand[:50] == k[:50]:
                    score = 3
                elif k in cand and len(k) >= 35:
                    score = 2
                elif k[:40] in cand[:200] and len(k) >= 30:
                    score = 1
                if score > best_score:
                    best_score = score
                    best = v
            if best is not None:
                rec = best
                match_kind = "title"

        # 4. arXiv ID fallback
        if rec is None and aid:
            for v in included:
                if v.get("arxiv_id", "") and aid in v["arxiv_id"]:
                    rec = v
                    match_kind = "arxiv-id"
                    break

        results.append({"pdf": p.name, "study": rec.get("study_id") if rec else None,
                        "match": match_kind, "arxiv": aid or "", "lang": lang,
                        "note": rec["title"][:50] if rec else first_text[:40].replace("\n", " ")})

    # Print summary
    matched = [r for r in results if r["study"]]
    unmatched = [r for r in results if not r["study"]]
    print(f"\nMatched: {len(matched)}/{len(results)}")
    print(f"Unmatched: {len(unmatched)}")
    for r in unmatched:
        print(f"  {r['pdf']:42s} lang={r['lang']:5s} arxiv={r['arxiv']:12s} {r['note'][:45]}")

    # Duplicates: user PDF matching a study already retrieved automatically
    print("\n=== Duplicates (study already retrieved) ===")
    dups = []
    for r in matched:
        st = status_by_id.get(next((v for v in included if v.get("study_id") == r["study"]), {}).get("id", ""), {})
        if st.get("status", "").startswith("retrieved"):
            dups.append(r)
    print(f"Duplicate downloads: {len(dups)}")
    for r in dups:
        print(f"  {r['pdf']:42s} -> {r['study']} (already retrieved)")

    print(f"\n=== NEW retrievals (was paywalled/no-doi/oa-link-failed) ===")
    new_ret = []
    for r in matched:
        inc = next((v for v in included if v.get("study_id") == r["study"]), None)
        st = status_by_id.get(inc["id"], {}) if inc else {}
        if not st.get("status", "").startswith("retrieved"):
            new_ret.append((r, st.get("status", "?")))
    print(f"Newly retrieved: {len(new_ret)}")
    for r, old in new_ret:
        print(f"  {r['pdf']:42s} -> {r['study']} (was {old})")


if __name__ == "__main__":
    main()
