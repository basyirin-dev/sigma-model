#!/usr/bin/env python3
"""
Paper 01 — Phase 6: regenerate download-queue.csv purely from
annotations.csv (the single source of truth). No file scan.

Filter: needs_download=yes AND not dup_within_lib; dedupe by URL;
sort by (batch, -relevance).
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
QUEUE_CSV = BASE / "research" / "retrieval" / "download-queue.csv"


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def access_path(r):
    if r["arxiv_id"]:
        return "arxiv-direct"
    if r["doi"]:
        if r["pdf_status"] == "oa-link-failed":
            return "doi-oa-retry"
        if r["pdf_status"] in ("paywalled-confirmed", "inaccessible"):
            return "doi-confirmed"
        return "doi-paywalled"
    return "scopus-only"


def batch(r):
    path = access_path(r)
    rel = int(r["relevance_score"])
    if path == "doi-confirmed":
        return "X-inaccessible-or-paywalled"
    if path == "doi-oa-retry":
        return "A-oa-retry"
    if path == "doi-paywalled":
        return "B1-doi-rel5-4" if rel >= 4 else "C1-doi-rel3"
    if path == "scopus-only":
        return "B2-scopus-rel5-4" if rel >= 4 else ("C2-scopus-rel3" if rel == 3 else "D-rel2")
    return "D-rel2"


ORDER = {"A-oa-retry": 0, "B1-doi-rel5-4": 1, "B2-scopus-rel5-4": 2,
         "C1-doi-rel3": 3, "C2-scopus-rel3": 4, "D-rel2": 5,
         "X-inaccessible-or-paywalled": 6}


def main():
    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))

    queue = [r for r in annot
             if r["needs_download"] == "yes" and not r.get("dup_within_lib")]
    seen = set()
    deduped = []
    for r in sorted(queue, key=lambda r: -int(r.get("relevance_score") or 1)):
        key = norm(r.get("download_url", "") or r["title"])
        if key in seen:
            continue
        seen.add(key)
        r["batch"] = batch(r)
        deduped.append(r)

    deduped.sort(key=lambda r: (ORDER.get(r["batch"], 9), -int(r["relevance_score"])))

    qcols = ["study_id", "id", "title", "authors", "year", "doi", "arxiv_id",
             "relevance_score", "pdf_status", "download_url", "source_db", "batch"]
    with open(QUEUE_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=qcols, extrasaction="ignore")
        w.writeheader()
        w.writerows(deduped)

    print(f"Queue: {len(deduped)}")
    print("Batches:", dict(Counter(r["batch"] for r in deduped)))


if __name__ == "__main__":
    main()
