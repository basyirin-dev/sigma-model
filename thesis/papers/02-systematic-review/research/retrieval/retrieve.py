#!/usr/bin/env python3
"""
Paper 02 — Phase 6 Full-Text Retrieval (Task 6.1)

Full 3-attempt retrieval pipeline over all 395 Include+Uncertain records.
Run on a machine with network access (this repo's sandboxed shell cannot
reach the internet). For each record, tries up to MAX_ATTEMPTS=3 distinct
sources in order:

  1. arXiv PDF          (records with arxiv_id)
  2. OpenAlex OA        (records with doi)
  3. Unpaywall OA       (records with doi)
  4. publisher URL      (records whose url looks like a direct PDF)

Records still unobtained after 3 attempts are coded `unavailable` with a
reason (task 6.1.4); DOI/no-identifier records go to the manual fetch list
(author email / ResearchGate workflow, task 6.1.2).

Usage:
  python retrieve.py [--dry-run] [--limit N]

Outputs:
  research/full-text-pdfs/                    (downloaded PDFs; gitignored)
  research/retrieval/retrieval-status.csv     (per-record status + attempts)
  research/full-text-retrieval-log.md         (task 6.1.3 log)
  research/retrieval/paywalled-to-fetch.csv   (manual fetch workflow list)
  research/retrieval/retrieval-report.md      (statistics)
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import retrieval_common as C  # noqa: E402,N812


def status_row(rec: dict) -> dict:
    return {
        "id": rec["id"], "title": rec.get("title", ""), "year": rec.get("year", ""),
        "doi": rec.get("doi", ""), "arxiv_id": rec.get("arxiv_id", ""),
        "url": rec.get("url", ""), "decision": rec.get("decision", ""),
        "status": rec.get("ft_retrieval_status", "pending"),
        "attempts": rec.get("ft_attempts", ""),
        "pdf_path": rec.get("ft_pdf_path", ""),
    }


def write_log_and_report(records: list[dict]) -> None:
    """Regenerate research/full-text-retrieval-log.md + retrieval-report.md
    from the current pool state (no network)."""
    stats = Counter(r.get("ft_retrieval_status", "pending") for r in records)

    with open(C.LOG_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Full-Text Retrieval Log (Task 6.1.3)\n\n")
        f.write("**Records sought**: 395 (179 Include + 216 Uncertain from Phase 5)\n")
        f.write("**Retrieval method**: automated arXiv + OpenAlex/Unpaywall OA "
                "(`research/retrieval/retrieve.py` / `download.py`); 3-attempt rule "
                "per task 6.1.4; manual author/ResearchGate requests tracked in "
                "`research/retrieval/paywalled-to-fetch.csv`\n\n")
        f.write("| ID | Title | Status | Attempts | Reason | PDF |\n")
        f.write("|----|-------|--------|----------|--------|-----|\n")
        for r in records:
            pdf = "✓" if r.get("ft_pdf_path") else ""
            f.write(f"| {r['id']} | {(r.get('title') or '')[:60]} | "
                    f"{r.get('ft_retrieval_status','pending')} | "
                    f"{r.get('ft_attempts','')} | "
                    f"{(r.get('ft_retrieval_reason') or '')} | {pdf} |\n")
        f.write(f"\n**Unavailable after 3 attempts**: {stats['unavailable']} — see "
                f"`research/retrieval/paywalled-to-fetch.csv` for the manual fetch workflow.\n")

    with open(C.REPORT_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Full-Text Retrieval Report (Task 6.1)\n\n")
        f.write("| Metric | Count |\n")
        f.write("|--------|------:|\n")
        f.write(f"| Records sought | {len(records)} |\n")
        for k in ("retrieved-arxiv", "retrieved-oa", "retrieved-manual", "unavailable", "pending"):
            f.write(f"| {k} | {stats[k]} |\n")
        total = stats["retrieved-arxiv"] + stats["retrieved-oa"] + stats["retrieved-manual"]
        f.write(f"| **Total PDFs retrieved** | **{total}** |\n\n")
        f.write("- PDFs: `research/full-text-pdfs/` (gitignored)\n")
        f.write("- Status: `research/retrieval/retrieval-status.csv`\n")
        f.write("- Log: `research/full-text-retrieval-log.md`\n")
        f.write("- Manual fetch list: `research/retrieval/paywalled-to-fetch.csv`\n")


def run(retry_unavailable: bool = False, limit: int | None = None, dry_run: bool = False) -> None:
    records = C.load_records()
    if not retry_unavailable:
        records = [r for r in records if r.get("ft_retrieval_status") != "unavailable"]
    if limit:
        records = records[:limit]

    stats = Counter()
    paywall_rows: list[dict] = []
    done = 0

    for rec in records:
        rid = rec["id"]
        doi = (rec.get("doi") or "").strip()
        arxiv_id = (rec.get("arxiv_id") or "").strip()
        url = (rec.get("url") or "").strip()

        dest = C.PDF_DIR / C.pdf_name(rec)
        status, reason = "unavailable", "no-identifier"

        # ── Attempt 1: arXiv ──────────────────────────────────────────
        if arxiv_id and not dry_run:
            ok = C.download(C.arxiv_pdf_url(arxiv_id), dest)
            C.add_attempt(rec, "arxiv", "ok" if ok else "fail")
        if dry_run and arxiv_id:
            C.add_attempt(rec, "arxiv", "planned")
        if dest.exists() and dest.stat().st_size >= 2000:
            status, reason = "retrieved-arxiv", ""
        elif arxiv_id:
            # ── Attempt 2: OpenAlex OA ────────────────────────────────
            if doi:
                if dry_run:
                    C.add_attempt(rec, "openalex", "planned")
                else:
                    pdf_url = C.openalex_lookup(doi)
                    C.add_attempt(rec, "openalex", C.oa_download(pdf_url, dest))
                if dest.exists() and dest.stat().st_size >= 2000:
                    status, reason = "retrieved-oa", ""
            # ── Attempt 3: Unpaywall ───────────────────────────────────
            if not dest.exists() and doi:
                if dry_run:
                    C.add_attempt(rec, "unpaywall", "planned")
                else:
                    pdf_url = C.unpaywall_lookup(doi)
                    C.add_attempt(rec, "unpaywall", C.oa_download(pdf_url, dest))
                if dest.exists() and dest.stat().st_size >= 2000:
                    status, reason = "retrieved-oa", ""
        elif doi:
            # arXiv-less DOI records: OpenAlex then Unpaywall
            if dry_run:
                C.add_attempt(rec, "openalex", "planned")
                C.add_attempt(rec, "unpaywall", "planned")
            else:
                pdf_url = C.openalex_lookup(doi)
                C.add_attempt(rec, "openalex", C.oa_download(pdf_url, dest))
                if dest.exists() and dest.stat().st_size >= 2000:
                    status, reason = "retrieved-oa", ""
                else:
                    pdf_url = C.unpaywall_lookup(doi)
                    C.add_attempt(rec, "unpaywall", C.oa_download(pdf_url, dest))
                    if dest.exists() and dest.stat().st_size >= 2000:
                        status, reason = "retrieved-oa", ""

        if dry_run:
            status, reason = "planned", ""
        elif status == "unavailable" and (arxiv_id or doi):
            reason = "paywalled" if doi else "download-failed"
        elif not arxiv_id and not doi:
            reason = "no-identifier"

        rec["ft_retrieval_status"] = status
        rec["ft_pdf_path"] = str(dest) if status.startswith("retrieved") else ""
        stats[status] += 1
        if status == "unavailable":
            paywall_rows.append({
                "id": rid, "doi": doi, "arxiv_id": arxiv_id, "title": rec.get("title", ""),
                "year": rec.get("year", ""), "journal": rec.get("journal", ""),
                "url": url, "reason": reason, "attempts": rec.get("ft_attempts", ""),
            })
        done += 1
        if done % 50 == 0:
            print(f"  ...{done}/{len(records)}")

    # ── Write outputs (never in dry-run: preview only) ───────────────
    if not dry_run:
        C.save_csv(C.POOL_CSV, records)                   # keep pool in sync
        C.save_csv(C.STATUS_CSV, [status_row(r) for r in records])
        C.save_csv(C.PAYWALL_CSV, paywall_rows)
        write_log_and_report(records)

    total_retrieved = stats["retrieved-arxiv"] + stats["retrieved-oa"] + stats["retrieved-manual"]
    print(f"\n{'='*60}")
    for k, v in stats.most_common():
        print(f"  {k:20s} {v}")
    print(f"  Total retrieved: {total_retrieved}")
    print(f"{'='*60}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="plan only, no network")
    ap.add_argument("--limit", type=int, default=None, help="process only first N records")
    ap.add_argument("--retry-unavailable", action="store_true",
                    help="retry records coded unavailable")
    ap.add_argument("--log-only", action="store_true",
                    help="regenerate log/report from current pool state (no network)")
    args = ap.parse_args()
    if args.log_only:
        records = C.load_records()
        write_log_and_report(records)
        print(f"Log: {C.LOG_MD.name} | Report: {C.REPORT_MD.name}")
        return
    run(retry_unavailable=args.retry_unavailable, limit=args.limit, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
