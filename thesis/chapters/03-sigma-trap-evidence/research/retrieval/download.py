#!/usr/bin/env python3
"""
Paper 02 — Phase 6 OA manifest consumer (Task 6.1)

Downloads every URL in research/retrieval/oa-manifest.csv (built by
manifest.py) into research/full-text-pdfs/ and updates the review pool's
retrieval status. Run on a machine with network access.

Usage:
  python download.py [--limit N] [--only pending|failed]

Resume-safe: records whose pdf already exists are skipped and marked
retrieved-arxiv/retrieved-oa (by manifest source).
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import retrieval_common as C  # noqa: E402,N812


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--only", choices=["pending", "failed"], default=None)
    args = ap.parse_args()

    if not C.MANIFEST_CSV.exists():
        print(f"Missing manifest: {C.MANIFEST_CSV}. Run manifest.py first.")
        sys.exit(1)

    manifest = C.load_records(C.MANIFEST_CSV)
    pool = {r["id"]: r for r in C.load_records()}
    stats = Counter()

    todo = [m for m in manifest if m.get("url") != "lookup-needed"]
    if args.only:
        seen = {m["id"]: m.get("status", "") for m in manifest}
        todo = [m for m in todo if seen.get(m["id"]) == args.only]
    if args.limit:
        todo = todo[: args.limit]

    for m in todo:
        rec = pool.get(m["id"])
        if rec is None:
            continue
        dest = C.PDF_DIR / C.pdf_name(rec)

        src = "retrieved-arxiv" if m["source"] == "arxiv" else "retrieved-oa"
        if dest.exists() and dest.stat().st_size >= 2000:
            rec["ft_retrieval_status"] = src
            rec["ft_pdf_path"] = str(dest)
            m["status"] = "done"
            stats[rec["ft_retrieval_status"]] += 1
            continue

        ok = C.download(m["url"], dest)
        if ok:
            rec["ft_retrieval_status"] = src
            rec["ft_pdf_path"] = str(dest)
            m["status"] = "done"
            stats[rec["ft_retrieval_status"]] += 1
        else:
            m["status"] = "failed"
            stats["failed"] += 1

    C.save_csv(C.POOL_CSV, list(pool.values()))
    C.save_csv(C.MANIFEST_CSV, manifest)
    print("Download pass complete:", dict(stats))


if __name__ == "__main__":
    main()
