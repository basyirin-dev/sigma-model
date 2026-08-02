#!/usr/bin/env python3
"""
Paper 01 — Phase 6: post-Batch-A bookkeeping.

1. Mark user-confirmed inaccessible studies (P575, P596) as pdf_status
   = 'inaccessible' in annotations.csv and retrieval-status.csv.
2. Re-add the `batch` column to download-queue.csv (rebuild drops it)
   and re-sort by (batch order, -relevance).
3. Report counts.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
QUEUE_CSV = BASE / "research" / "retrieval" / "download-queue.csv"

INACCESSIBLE = {"P575", "P596"}  # user-confirmed inaccessible


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
    # 1. Mark inaccessible in annotations + status
    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))
    for r in annot:
        if r["study_id"] in INACCESSIBLE:
            r["pdf_status"] = "inaccessible"
            r["has_pdf"] = "no"
            r["needs_download"] = "no"  # not downloadable -> out of the download loop
    with open(ANNOT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(annot[0].keys()))
        w.writeheader()
        w.writerows(annot)

    with open(STATUS_CSV, "r", encoding="utf-8") as f:
        status = list(csv.DictReader(f))
    # map study_id -> id
    sid_to_id = {r["study_id"]: r["id"] for r in annot}
    for r in status:
        if r["id"] in {sid_to_id.get(s) for s in INACCESSIBLE}:
            r["status"] = "inaccessible"
    with open(STATUS_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(status[0].keys()))
        w.writeheader()
        w.writerows(status)

    # 2. Re-batch the queue
    with open(QUEUE_CSV, "r", encoding="utf-8") as f:
        queue = list(csv.DictReader(f))
    for r in queue:
        r["batch"] = batch(r)
    queue.sort(key=lambda r: (ORDER.get(r["batch"], 9), -int(r["relevance_score"])))
    with open(QUEUE_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(queue[0].keys()))
        w.writeheader()
        w.writerows(queue)

    print("Annotations:", dict(Counter(r["has_pdf"] for r in annot)))
    print("Queue:", len(queue), "| batches:", dict(Counter(r["batch"] for r in queue)))
    print("P575/P596 marked inaccessible.")


if __name__ == "__main__":
    main()
