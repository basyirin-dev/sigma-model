#!/usr/bin/env python3
"""
Paper 01 — Phase 6 Full-Text Retrieval (Task 6.1, OA-only scope)

For all 1,278 Include+Uncertain records:
  1. arXiv ID -> download PDF from arxiv.org/pdf/<id>
  2. DOI       -> OpenAlex OA lookup (free API, no email) -> download OA PDF
  3. otherwise -> paywalled / no-doi status

Outputs:
  - research/pdfs/<firstauthor>_<year>.pdf          (downloaded PDFs)
  - research/retrieval/retrieval-status.csv          (per-record status)
  - research/retrieval/paywalled-to-fetch.csv        (manual fetch list)
  - research/retrieval/retrieval-report.md           (summary + manual steps)
"""

from __future__ import annotations

import csv
import json
import re
import time
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
SCREENING_CSV = BASE / "research" / "screening-results" / "paper01-screening-results.csv"
PDF_DIR = BASE / "research" / "pdfs"
PDF_DIR.mkdir(parents=True, exist_ok=True)
RETR_DIR = BASE / "research" / "retrieval"
RETR_DIR.mkdir(parents=True, exist_ok=True)

STATUS_CSV = RETR_DIR / "retrieval-status.csv"
PAYWALL_CSV = RETR_DIR / "paywalled-to-fetch.csv"
REPORT_MD = RETR_DIR / "retrieval-report.md"

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) SigmaModel/1.0 (mailto:research@example.org)"}
OPENALEX_MAILTO = "mailto:research@example.org"

# arXiv ID with version suffix removed for URL
def arxiv_pdf_url(arxiv_id: str) -> str:
    base = arxiv_id.strip().split("v")[0]
    return f"https://arxiv.org/pdf/{base}"


def openalex_oa_pdf(doi: str) -> str | None:
    """Return best OA PDF url for a DOI via OpenAlex, or None."""
    url = f"https://api.openalex.org/works/doi:{doi}?mailto={OPENALEX_MAILTO.split(':')[1]}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            d = json.loads(resp.read().decode())
        best = d.get("best_oa_location") or {}
        pdf = best.get("pdf_url")
        if pdf:
            return pdf
        # fall back to oa_url (landing page)
        oa_url = (d.get("open_access") or {}).get("oa_url")
        return oa_url
    except Exception:
        return None


def download(url: str, dest: Path, timeout: int = 30) -> bool:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        # only accept pdf-ish content
        ct = resp.headers.get("Content-Type", "")
        if len(data) < 2000:
            return False
        dest.write_bytes(data)
        return True
    except Exception:
        return False


def safe_name(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_")
    return s[:40] or "unknown"


def first_author_surname(authors: str) -> str:
    if not authors:
        return "unknown"
    first = authors.split(";")[0].strip()
    # "Last, First" or "First Last" or "Last F." handling
    if "," in first:
        return first.split(",")[0].strip()
    parts = first.split()
    return parts[-1] if parts else "unknown"


def main():
    with open(SCREENING_CSV, "r", encoding="utf-8") as f:
        records = [r for r in csv.DictReader(f)
                   if r["decision"] in ("Include", "Uncertain")]

    print(f"Records to retrieve: {len(records)}")

    status_rows = []
    paywall_rows = []
    stats = {"arxiv_attempt": 0, "arxiv_ok": 0, "oa_attempt": 0, "oa_ok": 0,
             "paywalled": 0, "no_doi": 0, "download_fail": 0}

    for i, r in enumerate(records):
        rid = r["id"]
        title = r.get("title", "")
        year = (r.get("year") or "").strip() or "unknown"
        doi = (r.get("doi") or "").strip()
        arxiv_id = (r.get("arxiv_id") or "").strip()
        authors = r.get("authors", "") or ""
        fname = f"{safe_name(first_author_surname(authors))}_{year}"

        pdf_path = ""
        status = ""
        source = ""

        # Path 1: arXiv
        if arxiv_id:
            stats["arxiv_attempt"] += 1
            dest = PDF_DIR / f"{fname}_arxiv.pdf"
            if download(arxiv_pdf_url(arxiv_id), dest):
                pdf_path = str(dest.relative_to(BASE.parent.parent.parent))
                status = "retrieved-arxiv"
                source = "arxiv"
                stats["arxiv_ok"] += 1
            else:
                status = "download-failed"
                source = "arxiv"
                stats["download_fail"] += 1
        # Path 2: DOI -> OpenAlex OA
        elif doi:
            stats["oa_attempt"] += 1
            pdf_url = openalex_oa_pdf(doi)
            if pdf_url:
                dest = PDF_DIR / f"{fname}_oa.pdf"
                if download(pdf_url, dest):
                    pdf_path = str(dest.relative_to(BASE.parent.parent.parent))
                    status = "retrieved-oa"
                    source = "openalex"
                    stats["oa_ok"] += 1
                else:
                    status = "oa-link-failed"
                    source = "openalex"
                    stats["download_fail"] += 1
            else:
                status = "paywalled"
                source = "openalex"
                stats["paywalled"] += 1
                paywall_rows.append({"id": rid, "doi": doi, "title": title,
                                     "year": year, "journal": r.get("journal", ""),
                                     "url": r.get("url", "")})
        else:
            status = "no-doi"
            source = "none"
            stats["no_doi"] += 1
            paywall_rows.append({"id": rid, "doi": "", "title": title,
                                 "year": year, "journal": r.get("journal", ""),
                                 "url": r.get("url", "")})

        status_rows.append({
            "id": rid, "title": title, "year": year, "doi": doi,
            "arxiv_id": arxiv_id, "status": status, "source": source,
            "pdf_path": pdf_path, "decision": r["decision"],
        })

        if (i + 1) % 100 == 0:
            print(f"  ...{i+1}/{len(records)}")

    # Write status CSV
    with open(STATUS_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(status_rows[0].keys()))
        w.writeheader()
        w.writerows(status_rows)

    # Write paywalled fetch list
    with open(PAYWALL_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "doi", "title", "year", "journal", "url"])
        w.writeheader()
        w.writerows(paywall_rows)

    # Report
    total_pdf = stats["arxiv_ok"] + stats["oa_ok"]
    with open(REPORT_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 01 — Full-Text Retrieval Report (Task 6.1)\n\n")
        f.write(f"**Date**: 2026-08-01\n")
        f.write(f"**Scope**: OA-only retrieval (arXiv + OpenAlex OA); paywalled recorded for manual fetch\n\n")
        f.write("## Retrieval Statistics\n\n")
        f.write("| Metric | Count |\n")
        f.write("|--------|------:|\n")
        f.write(f"| Records sought | {len(records)} |\n")
        f.write(f"| arXiv attempts | {stats['arxiv_attempt']} |\n")
        f.write(f"| arXiv retrieved | {stats['arxiv_ok']} |\n")
        f.write(f"| DOI/OA lookups | {stats['oa_attempt']} |\n")
        f.write(f"| OA retrieved | {stats['oa_ok']} |\n")
        f.write(f"| **Total PDFs retrieved** | **{total_pdf}** |\n")
        f.write(f"| Paywalled (manual fetch needed) | {stats['paywalled']} |\n")
        f.write(f"| No DOI / no URL | {stats['no_doi']} |\n")
        f.write(f"| Download failures | {stats['download_fail']} |\n\n")
        f.write("## Files\n\n")
        f.write(f"- PDFs: `research/pdfs/` ({total_pdf} files)\n")
        f.write(f"- Status log: `research/retrieval/retrieval-status.csv`\n")
        f.write(f"- Manual fetch list: `research/retrieval/paywalled-to-fetch.csv`\n")
        f.write(f"- This report: `research/retrieval/retrieval-report.md`\n\n")
        f.write("## Manual Steps for Paywalled Records\n\n")
        f.write("See the full step-by-step guide at the end of this phase for downloading\n")
        f.write("paywalled PDFs via UM OpenAthens and adding them to `research/pdfs/`.\n")

    print(f"\n{'='*60}")
    print(f"  Retrieval complete: {total_pdf} PDFs downloaded")
    print(f"  Paywalled: {stats['paywalled']} | No-DOI: {stats['no_doi']} | Failed: {stats['download_fail']}")
    print(f"  Status: {STATUS_CSV.name}")
    print(f"  Paywall list: {PAYWALL_CSV.name}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
