#!/usr/bin/env python3
"""
Paper 02 — Phase 6 shared retrieval helpers (Tasks 6.1.1-6.1.5)

Shared by retrieve.py (full 3-attempt pipeline), manifest.py (OA manifest
builder) and download.py (manifest consumer).

Conventions:
  - PDFs        -> research/full-text-pdfs/<id>_<firstauthor>_<year>.pdf
  - texts       -> research/full-text-txt/  (Phase 3 extraction)
  - statuses    -> retrieved-arxiv | retrieved-oa | retrieved-manual
                   | unavailable (reason: no-identifier|no-oa|download-failed
                   | paywalled|not-found) | pending
  - attempts    -> "1:<source>:<outcome>; 2:<source>:<outcome>; ..."
                   (task 6.1.4: max 3 distinct sources before Unavailable)
"""

from __future__ import annotations

import csv
import json
import os
import re
import ssl
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
PDF_DIR = BASE / "research" / "full-text-pdfs"
TXT_DIR = BASE / "research" / "full-text-txt"
RETR_DIR = BASE / "research" / "retrieval"

POOL_CSV = BASE / "research" / "screening-data" / "full-text" / "records-to-review.csv"
STATUS_CSV = RETR_DIR / "retrieval-status.csv"
MANIFEST_CSV = RETR_DIR / "oa-manifest.csv"
PAYWALL_CSV = RETR_DIR / "paywalled-to-fetch.csv"
LOG_MD = BASE / "research" / "full-text-retrieval-log.md"
REPORT_MD = RETR_DIR / "retrieval-report.md"

for _dir in (PDF_DIR, TXT_DIR, RETR_DIR):
    _dir.mkdir(parents=True, exist_ok=True)

# Sandboxed/dev networks may MITM TLS with an untrusted CA; set
# SIGMA_SSL_VERIFY=0 to disable verification (default keeps it ON).
SSL_VERIFY = os.environ.get("SIGMA_SSL_VERIFY", "1") not in ("0", "false", "no")
_SSL_CTX = None if SSL_VERIFY else ssl._create_unverified_context()

HEADERS = {"User-Agent": ("Mozilla/5.0 (X11; Linux x86_64) SigmaModel/2.0 "
                          "(mailto:research@example.org)")}
# Set your real email via env for Unpaywall politeness:
UNPAYWALL_EMAIL = os.environ.get("UNPAYWALL_EMAIL", "research@example.org")

MAX_ATTEMPTS = 3


def arxiv_pdf_url(arxiv_id: str) -> str:
    """arXiv id may carry a version suffix ('2010.05465v1'); PDF URL uses the bare id."""
    base = arxiv_id.strip().split("v")[0]
    return f"https://arxiv.org/pdf/{base}"


def openalex_lookup(doi: str) -> str | None:
    """Best OA PDF url for a DOI via OpenAlex (free API), else None."""
    url = f"https://api.openalex.org/works/doi:{doi}?mailto={UNPAYWALL_EMAIL}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20, context=_SSL_CTX) as resp:
            d = json.loads(resp.read().decode())
        best = d.get("best_oa_location") or {}
        pdf = best.get("pdf_url")
        if pdf:
            return pdf
        content = d.get("content_urls") or {}
        if content.get("pdf"):
            return content["pdf"]
        return (d.get("open_access") or {}).get("oa_url")
    except Exception:
        return None


def unpaywall_lookup(doi: str) -> str | None:
    """Best OA PDF url for a DOI via Unpaywall (free API, email required)."""
    url = f"https://api.unpaywall.org/v2/{doi}?email={UNPAYWALL_EMAIL}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20, context=_SSL_CTX) as resp:
            d = json.loads(resp.read().decode())
        loc = d.get("best_oa_location") or {}
        pdf = loc.get("url_for_pdf") or loc.get("url")
        return pdf
    except Exception:
        return None


def download(url: str, dest: Path, timeout: int = 30) -> bool:
    """Download a PDF to dest. Returns success (rejects non-PDF payloads)."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            data = resp.read()
        if len(data) < 2000 or data[:4] != b"%PDF":
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return True
    except Exception:
        return False


def is_pdf_bytes(data: bytes) -> bool:
    return data[:4] == b"%PDF"


def first_author_surname(authors: str) -> str:
    if not authors:
        return "unknown"
    first = authors.split(";")[0].strip()
    if "," in first:
        return first.split(",")[0].strip()
    parts = first.split()
    return parts[-1] if parts else "unknown"


def safe_name(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_")
    return s[:40] or "unknown"


def pdf_name(rec: dict) -> str:
    year = (rec.get("year") or "").strip() or "unknown"
    surname = safe_name(first_author_surname(rec.get("authors", "")))
    return f"{rec['id']}_{surname}_{year}.pdf"


def load_records(path: Path = POOL_CSV) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def oa_download(pdf_url: str | None, dest: Path) -> str:
    """Download from an OA URL; return 'ok' or 'no-oa' for attempt logging."""
    return "ok" if pdf_url and download(pdf_url, dest) else "no-oa"


def add_attempt(rec: dict, source: str, outcome: str) -> None:
    cur = (rec.get("ft_attempts") or "").strip()
    step = f"{source}:{outcome}"
    rec["ft_attempts"] = f"{cur}; {step}".strip("; ") if cur else step
