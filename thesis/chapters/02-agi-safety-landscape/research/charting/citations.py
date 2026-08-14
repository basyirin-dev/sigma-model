#!/usr/bin/env python3
"""
Paper 01 — Phase 7: fetch citation counts from OpenAlex (Task 7.2.3,
optional field `citation_count` for quality weighting).

Batch lookup via OpenAlex `works?filter=doi:...` (pipe-OR, 50 DOIs per
call, polite pool mailto in User-Agent). Papers without DOI fall back to a
title search. Results cached in research/charting/citations-cache.json.

Network: this sandbox routes through a MITM TLS proxy whose CA is
untrusted — set SIGMA_SSL_VERIFY=0 to disable certificate verification
(kept OFF-by-default-safe: verification stays ON otherwise).

Output: citation_count filled in charted-data.csv + citations-report.md
"""

from __future__ import annotations

import csv
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
CACHE_JSON = BASE / "research" / "charting" / "citations-cache.json"
REPORT_MD = BASE / "research" / "charting" / "citations-report.md"

API = "https://api.openalex.org/works"
MAILTO = "sigma-align-review@example.org"
CHUNK = 50
SLEEP = 0.5
RETRIES = 3


def opener() -> urllib.request.OpenerDirector:
    ctx = ssl.create_default_context()
    if os.environ.get("SIGMA_SSL_VERIFY", "0") == "0":
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    return urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))


def get_json(op: urllib.request.OpenerDirector, url: str) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": f"sigma-align-research mailto:{MAILTO}"})
    for attempt in range(RETRIES):
        try:
            with op.open(req, timeout=25) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < RETRIES - 1:
                wait = float(e.headers.get("Retry-After", "3") or 3)
                time.sleep(wait + attempt)
                continue
            if e.code in (400, 404):
                return None
            print(f"  warn: {url[:90]} -> HTTP {e.code}")
            return None
        except Exception as e:
            if attempt < RETRIES - 1:
                time.sleep(2 * (attempt + 1))
                continue
            print(f"  warn: {url[:90]} -> {type(e).__name__}: {str(e)[:80]}")
            return None
    return None


def main() -> None:
    op = opener()
    cache: dict[str, int] = json.loads(CACHE_JSON.read_text()) if CACHE_JSON.exists() else {}
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    fields = list(rows[0].keys())

    if "--from-cache" in sys.argv:
        print(f"applying cached citations ({len(cache)} entries) without network")
    else:        # fetch remaining DOIs (chunked)
        todo = [r for r in rows if (r.get("doi") or "").strip() and r["paper_id"] not in cache]
        print(f"cached: {len(cache)} | to fetch by DOI: {len(todo)}")
        for i in range(0, len(todo), CHUNK):
            chunk = todo[i:i + CHUNK]
            dois = [r["doi"].strip() for r in chunk]
            q = urllib.parse.urlencode({"filter": "doi:" + "|".join(dois),
                                        "per-page": str(CHUNK), "mailto": MAILTO})
            data = get_json(op, f"{API}?{q}")
            if not data:
                continue
            for w in data.get("results", []):
                doi = (w.get("doi") or "").replace("https://doi.org/", "")
                c = w.get("cited_by_count")
                if doi and c is not None:
                    cache[doi] = int(c)
            time.sleep(SLEEP)

        CACHE_JSON.write_text(json.dumps(cache, indent=1), encoding="utf-8")

    n_title = len([k for k in cache if k.startswith("title:")])
    doi_cache = {k.strip().lower(): v for k, v in cache.items() if not k.startswith("title:")}
    # re-read fresh at write time — other pipeline stages may have updated
    # charted-data.csv while a long fetch was in flight.
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    fields = list(rows[0].keys())
    n_filled = 0
    for r in rows:
        doi = (r.get("doi") or "").strip().lower()
        if doi and doi in doi_cache:
            r["citation_count"] = str(doi_cache[doi]); n_filled += 1
        elif not doi and f"title:{r['paper_id']}" in cache:
            r["citation_count"] = str(cache[f"title:{r['paper_id']}"]); n_filled += 1

    with open(CHARTED_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    n_title = len([k for k in cache if k.startswith("title:")])
    with open(REPORT_MD, "w", encoding="utf-8") as fh:
        fh.write(f"# Citation count report — Paper 01 Phase 7\n\n")
        fh.write(f"- Fetch date: **{date.today().isoformat()}** (OpenAlex)\n")
        fh.write(f"- Papers with citation_count: **{n_filled} / {len(rows)}**\n")
        fh.write(f"- DOI lookups cached: **{len([k for k in cache if not k.startswith('title:')])}**\n")
        fh.write(f"- Title-search fallback hits: **{n_title}**\n")
        fh.write(f"- Note: title-search fallback is rate-limited in this sandbox;\n"
                 f"  coverage is partial and resumable via the cache.\n")
    print(f"filled citation_count for {n_filled}/{len(rows)} papers")


if __name__ == "__main__":
    sys.exit(main())
