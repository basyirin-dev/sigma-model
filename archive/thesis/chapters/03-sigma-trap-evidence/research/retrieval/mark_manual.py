#!/usr/bin/env python3
"""
Paper 02 — Phase 6 reconcile manually downloaded PDFs (Task 6.1 follow-up)

Scans research/full-text-pdfs/ for PDFs named <P02_id>_*.pdf that are not
yet recorded in the review pool and marks them as manually retrieved
(ft_retrieval_status = retrieved-manual). Safe to re-run: records that
already have a retrieved status are left untouched.

Usage:
  python mark_manual.py

Outputs:
  updates records-to-review.csv + retrieval-status.csv + retrieval log/report
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import retrieval_common as C  # noqa: E402,N812
from retrieve import status_row, write_log_and_report  # noqa: E402


def main() -> None:
    records = C.load_records()
    by_id = {r["id"]: r for r in records}
    marked = 0

    for f in sorted(C.PDF_DIR.iterdir()):
        m = re.match(r"(P02_\d{4})_", f.name)
        if not m or not f.is_file():
            continue
        rid = m.group(1)
        rec = by_id.get(rid)
        if rec is None:
            continue
        if rec.get("ft_retrieval_status") in ("retrieved-arxiv", "retrieved-oa",
                                               "retrieved-manual"):
            continue  # already retrieved; don't clobber
        rec["ft_retrieval_status"] = "retrieved-manual"
        rec["ft_pdf_path"] = str(f)
        cur = (rec.get("ft_attempts") or "").strip()
        rec["ft_attempts"] = f"{cur}; manual:ok".strip("; ")
        marked += 1

    if marked:
        C.save_csv(C.POOL_CSV, records)
        C.save_csv(C.STATUS_CSV, [status_row(r) for r in records])
        paywall = [r for r in records if r["ft_retrieval_status"] == "unavailable"]
        C.save_csv(C.PAYWALL_CSV, paywall)
        write_log_and_report(records)

    stats = Counter(r["ft_retrieval_status"] for r in records)
    print(f"Marked {marked} manually retrieved PDFs")
    print("Pool statuses:", dict(stats.most_common()))
    print(f"Remaining unavailable: {stats['unavailable']}")


if __name__ == "__main__":
    main()
