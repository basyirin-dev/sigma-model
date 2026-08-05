#!/usr/bin/env python3
"""
Paper 02 — Phase 6 full-text extraction (Task 6.2)

Runs pdftotext over every retrieved PDF in research/full-text-pdfs/ and
writes plain text to research/full-text-txt/<id>.txt. Flags records whose
extraction yields too little text (scanned/image-only PDFs).

Usage:
  python extract.py [--limit N]

Output:
  research/full-text-txt/<id>.txt     (one per retrieved PDF)
  prints extraction statistics
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import retrieval_common as C  # noqa: E402,N812

MIN_CHARS = 500


def extract_pdf(pdf: Path, out: Path) -> int:
    """Return extracted character count (0 if failed/empty)."""
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        r = subprocess.run(
            ["pdftotext", "-q", str(pdf), str(out)], capture_output=True, timeout=120
        )
        if r.returncode != 0 or not out.exists():
            return 0
        return out.stat().st_size
    except Exception:
        return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    pool = C.load_records()
    stats = Counter()
    low: list[str] = []
    done = 0

    for rec in pool:
        pdf_path = rec.get("ft_pdf_path", "")
        if not pdf_path or not Path(pdf_path).exists():
            stats["no-pdf"] += 1
            continue
        txt_out = C.TXT_DIR / f"{rec['id']}.txt"
        n = extract_pdf(Path(pdf_path), txt_out)
        if n >= MIN_CHARS:
            stats["extracted"] += 1
        elif n > 0:
            stats["low-quality"] += 1
            low.append(f"{rec['id']} ({n} chars)")
        else:
            stats["empty/scanned"] += 1
            low.append(f"{rec['id']} (empty)")
        done += 1
        if args.limit and done >= args.limit:
            break

    print("Extraction statistics:", dict(stats))
    if low:
        print(f"Low-quality/empty ({len(low)}):")
        for x in low[:20]:
            print("  ", x)
    print(f"Output dir: {C.TXT_DIR}")


if __name__ == "__main__":
    main()
