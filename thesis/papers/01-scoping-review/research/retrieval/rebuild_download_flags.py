#!/usr/bin/env python3
"""
Paper 01 — Phase 6: rebuild annotations download flags from ACTUAL files.

Scans every PDF in research/pdfs/, extracts first-page text, matches to
included studies (title prefix/containment + arXiv-ID reconstruction).
Non-English PDFs (CJK/Cyrillic) are NOT counted as full texts (I1).

Updates:
  - annotations.csv: has_pdf / needs_download / pdf_status / pdf_path
  - download-queue.csv: only studies with no PDF file on disk
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

from pdfminer.high_level import extract_text

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
PDF_DIR = BASE / "research" / "pdfs"
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
OUT_ANNOT = BASE / "research" / "retrieval" / "annotations.csv"
OUT_QUEUE = BASE / "research" / "retrieval" / "download-queue.csv"

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
    with open(INCLUDED_CSV, "r", encoding="utf-8") as f:
        included = list(csv.DictReader(f))
    # index: normalized title -> study; arxiv_id -> study
    title_idx = {}
    arxiv_idx = {}
    for r in included:
        t = norm(r.get("title", ""))
        if len(t) >= 25:
            title_idx.setdefault(t, r)
        aid = (r.get("arxiv_id") or "").strip().split("v")[0]
        if aid:
            arxiv_idx.setdefault(aid, r)

    # map study_id -> list of pdf paths
    study_pdfs = defaultdict(list)
    foreign_pdfs = []

    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    print(f"Scanning {len(pdfs)} PDFs...")
    for p in pdfs:
        try:
            first = extract_text(str(p), page_numbers=[0], maxpages=1)[:600]
        except Exception:
            continue
        if has_non_latin(first):
            foreign_pdfs.append(p.name)
            continue  # non-English: not a valid full text for I1
        aid = extract_arxiv_id(first)
        cand = norm(first)
        rec = None
        if len(cand) > 30:
            best, best_score = None, 0
            for k, v in title_idx.items():
                score = 0
                if cand[:60] == k[:60] or cand[:50] == k[:50]:
                    score = 3
                elif k in cand and len(k) >= 35:
                    score = 2
                elif k[:40] in cand[:200] and len(k) >= 30:
                    score = 1
                if score > best_score:
                    best_score, best = score, v
            rec = best
        if rec is None and aid:
            rec = arxiv_idx.get(aid)
        if rec:
            study_pdfs[rec["study_id"]].append(p.name)

    print(f"Matched {len(study_pdfs)} studies to PDFs; {len(foreign_pdfs)} foreign-language PDFs skipped")

    # ---- filename-based fallback: first-author surname + year ----
    # Catches PDFs whose first-page text didn't title-match (publisher
    # layouts, garbled extraction). Only takes unique, unambiguous files
    # (single candidate for the surname-year pair, not an automated
    # _arxiv/_oa download already claimed, not foreign-language).
    user_files = [p for p in pdfs
                  if "_arxiv" not in p.name and "_oa" not in p.name
                  and p.name.lower().endswith(".pdf")]
    for r in included:
        if r["study_id"] in study_pdfs:
            continue
        authors = (r.get("authors") or "")
        year = (r.get("year") or "").strip()
        if not authors or not year:
            continue
        surname = authors.split(";")[0].split(",")[0].strip().split()[-1].lower()
        cands = [p.name for p in user_files
                 if p.stem.lower().replace("_", " ").startswith(surname) and year in p.name
                 and p.name not in {f for v in study_pdfs.values() for f in v}]
        if len(cands) == 1:
            study_pdfs[r["study_id"]].append(cands[0])

    print(f"After filename fallback: {len(study_pdfs)} studies matched")

    # ---- merge with retrieval-status authoritative pdf_path ----
    with open(STATUS_CSV, "r", encoding="utf-8") as f:
        status_rows = list(csv.DictReader(f))
    for st in status_rows:
        if st.get("pdf_path") and Path(BASE.parent.parent.parent, st["pdf_path"]).exists():
            # find study_id for this record id
            for r in included:
                if r["id"] == st["id"]:
                    study_pdfs.setdefault(r["study_id"], []).append(st["pdf_path"])
                    break

    # ---- update annotations ----
    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))
    cols = list(annot[0].keys())
    pdf_prefix = "thesis/papers/01-scoping-review/research/pdfs/"
    for r in annot:
        pdfs = study_pdfs.get(r["study_id"], [])
        if pdfs:
            r["has_pdf"] = "yes"
            r["needs_download"] = "no"
            r["pdf_status"] = "retrieved-file"
            # normalize to repo-root-relative path
            fname = Path(pdfs[0]).name
            r["pdf_path"] = pdf_prefix + fname
        else:
            r["has_pdf"] = "no"
            r["needs_download"] = "yes"
            # normalize stale retrieved-* labels when no file is on disk
            if (r.get("pdf_status") or "").startswith("retrieved") or r["pdf_status"] in ("retrieved-file", "no-pdf"):
                r["pdf_status"] = "no-pdf"
    if "pdf_path" not in cols:
        cols = cols + ["pdf_path"]

    with open(OUT_ANNOT, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(annot)

    # ---- rebuild download queue ----
    queue = [r for r in annot
             if r["needs_download"] == "yes" and not r.get("dup_within_lib")]
    seen = set()
    deduped = []
    for r in sorted(queue, key=lambda r: -int(r.get("relevance_score") or 1)):
        key = norm(r.get("download_url", "") or r["title"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)

    qcols = ["study_id", "id", "title", "authors", "year", "doi", "arxiv_id",
             "relevance_score", "pdf_status", "download_url", "source_db"]
    with open(OUT_QUEUE, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=qcols, extrasaction="ignore")
        w.writeheader()
        w.writerows(deduped)

    has = sum(1 for r in annot if r["has_pdf"] == "yes")
    need = sum(1 for r in annot if r["needs_download"] == "yes")
    print(f"\nIncluded: {len(annot)} | has_pdf: {has} | needs_download: {need}")
    print(f"Download queue: {len(deduped)}")
    print(f"Foreign-language PDFs (skipped, not counted): {foreign_pdfs}")


if __name__ == "__main__":
    main()
