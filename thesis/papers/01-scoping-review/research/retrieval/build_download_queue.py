#!/usr/bin/env python3
"""
Paper 01 — Phase 6: enrich annotations.csv with download/duplicate flags
and produce a deduplicated download-queue.csv for the user's batch
downloads (thousands remaining beyond the first 500).

Columns added to annotations.csv:
  pdf_status      - retrieval status (retrieved-arxiv/oa/manual, paywalled, ...)
  has_pdf         - yes/no
  needs_download  - yes (no PDF yet) / no (already have)
  dup_within_lib  - study ID of a duplicate record within the included list
  dup_pdf_file    - yes if a second PDF file duplicates an already-retrieved study
  download_url    - best URL to fetch (DOI resolve, arXiv pdf, or record URL)

download-queue.csv: needs_download=yes, sorted by relevance desc, deduplicated.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
OUT_ANNOT = BASE / "research" / "retrieval" / "annotations.csv"
OUT_QUEUE = BASE / "research" / "retrieval" / "download-queue.csv"


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))
    with open(STATUS_CSV, "r", encoding="utf-8") as f:
        status_rows = list(csv.DictReader(f))
    status_by_id = {r["id"]: r for r in status_rows}

    # ---- within-library duplicate detection (same DOI or normalized title) ----
    doi_groups = defaultdict(list)
    title_groups = defaultdict(list)
    for r in annot:
        doi = (r.get("doi") or "").strip().lower()
        if doi:
            doi_groups[doi].append(r)
        t = norm(r.get("title", ""))
        if len(t) > 25:
            title_groups[t].append(r)

    dup_map = {}  # study_id -> duplicate-of study_id
    for groups in (doi_groups, title_groups):
        for key, members in groups.items():
            if len(members) > 1:
                members_sorted = sorted(members, key=lambda m: m.get("study_id", ""))
                keeper = members_sorted[0]["study_id"]
                for m in members_sorted[1:]:
                    if m["study_id"] not in dup_map:
                        dup_map[m["study_id"]] = keeper

    # ---- duplicate PDF files (same study, multiple files) ----
    pdf_by_study = defaultdict(list)
    for st in status_rows:
        if st.get("pdf_path"):
            pdf_by_study[st["id"]].append(st["pdf_path"])

    # ---- enrich annotations ----
    out_cols = list(annot[0].keys()) + ["pdf_status", "has_pdf", "needs_download",
                                        "dup_within_lib", "dup_pdf_file", "download_url"]
    for r in annot:
        st = status_by_id.get(r["id"], {})
        status = st.get("status", "unknown")
        pdf_path = st.get("pdf_path", "")
        has_pdf = "yes" if (status.startswith("retrieved") or pdf_path) else "no"
        r["pdf_status"] = status
        r["has_pdf"] = has_pdf
        r["needs_download"] = "no" if has_pdf == "yes" else "yes"
        r["dup_within_lib"] = dup_map.get(r["study_id"], "")
        r["dup_pdf_file"] = "yes" if len(pdf_by_study.get(r["id"], [])) > 1 else "no"
        # best download URL
        if r.get("arxiv_id"):
            r["download_url"] = f"https://arxiv.org/pdf/{r['arxiv_id'].split('v')[0]}"
        elif r.get("doi"):
            r["download_url"] = f"https://doi.org/{r['doi']}"
        else:
            r["download_url"] = st.get("url", "") or (r.get("url") or "")

    with open(OUT_ANNOT, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=out_cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(annot)

    # ---- download queue (deduplicated, relevance desc) ----
    queue = [r for r in annot if r["needs_download"] == "yes" and not r["dup_within_lib"]]
    # dedupe by download_url (avoid downloading same paper twice)
    seen_url = set()
    deduped = []
    for r in sorted(queue, key=lambda r: -int(r.get("relevance_score") or 1)):
        u = r.get("download_url", "")
        key = norm(u) or norm(r["title"])
        if key in seen_url:
            continue
        seen_url.add(key)
        deduped.append(r)

    qcols = ["study_id", "id", "title", "authors", "year", "doi", "arxiv_id",
             "relevance_score", "pdf_status", "download_url", "source_db"]
    with open(OUT_QUEUE, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=qcols, extrasaction="ignore")
        w.writeheader()
        w.writerows(deduped)

    # ---- summary ----
    has = sum(1 for r in annot if r["has_pdf"] == "yes")
    need = sum(1 for r in annot if r["needs_download"] == "yes")
    inlib_dups = len(dup_map)
    print(f"Total included: {len(annot)}")
    print(f"Has PDF: {has}")
    print(f"Needs download: {need}")
    print(f"Within-library duplicates flagged: {inlib_dups}")
    print(f"Download queue (deduped): {len(deduped)}")
    print(f"\nAnnotations: {OUT_ANNOT.name}")
    print(f"Queue: {OUT_QUEUE.name}")
    print("\nWithin-library duplicate examples:")
    shown = 0
    for r in annot:
        if r["dup_within_lib"] and shown < 10:
            print(f"  {r['study_id']} dup of {r['dup_within_lib']} | {r['title'][:55]}")
            shown += 1


if __name__ == "__main__":
    main()
