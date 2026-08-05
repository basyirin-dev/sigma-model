#!/usr/bin/env python3
"""
Paper 02 — Phase 6 OA manifest builder (Task 6.1)

Builds research/retrieval/oa-manifest.csv — the ordered download list for
download.py. Works offline for arXiv records (URLs are deterministic);
with --online it also resolves OpenAlex OA URLs for DOI records.

Rows:
  - arXiv records     -> url = https://arxiv.org/pdf/<id>,  priority 1
  - DOI-only records  -> priority 2; url = lookup-needed (offline)
                        or resolved OA URL (--online)
  - no-identifier     -> omitted from manifest (tracked in retrieval-status)

Usage:
  python manifest.py [--online]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import retrieval_common as C  # noqa: E402,N812


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--online", action="store_true",
                    help="resolve OpenAlex OA URLs for DOIs (needs network)")
    args = ap.parse_args()

    records = C.load_records()
    rows = []
    n_arxiv = n_doi = n_lookup = 0

    for rec in records:
        rid = rec["id"]
        arxiv_id = (rec.get("arxiv_id") or "").strip()
        doi = (rec.get("doi") or "").strip()

        if arxiv_id:
            rows.append({
                "id": rid, "title": rec.get("title", ""), "year": rec.get("year", ""),
                "source": "arxiv", "url": C.arxiv_pdf_url(arxiv_id), "priority": 1,
                "doi": doi, "status": "pending",
            })
            n_arxiv += 1
        elif doi:
            url = "lookup-needed"
            if args.online:
                pdf = C.openalex_lookup(doi)
                if pdf:
                    url = pdf
                else:
                    n_lookup += 1
            else:
                n_lookup += 1
            rows.append({
                "id": rid, "title": rec.get("title", ""), "year": rec.get("year", ""),
                "source": "openalex", "url": url, "priority": 2,
                "doi": doi, "status": "pending",
            })
            n_doi += 1
        # no-identifier records: no manifest entry; handled via manual fetch list

    C.save_csv(C.MANIFEST_CSV, rows)
    print(f"Manifest rows: {len(rows)} (arxiv={n_arxiv}, doi={n_doi}, "
          f"doi-still-lookup-needed={n_lookup})")
    print(f"Output: {C.MANIFEST_CSV.relative_to(C.BASE.parent.parent.parent)}")
    if n_lookup and not args.online:
        print("Hint: re-run with --online (needs network) or fill 'lookup-needed' "
              "rows via the OpenAlex API (agent web_fetch) before downloading.")


if __name__ == "__main__":
    main()
