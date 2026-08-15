#!/usr/bin/env python3
"""
Paper 01 — Phase 7: export charted data (Task 7.5.1/7.5.2, CC.4.3).

Writes research/charted-data.csv and research/charted-data.json (the
canonical review-level exports named in the phase plan) from the working
charting/charted-data.csv, plus a small manifest with schema version.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
SRC_CSV = BASE / "research" / "charting" / "charted-data.csv"
OUT_CSV = BASE / "research" / "charted-data.csv"
OUT_JSON = BASE / "research" / "charted-data.json"


def main() -> None:
    rows = list(csv.DictReader(open(SRC_CSV, newline="", encoding="utf-8")))
    fields = list(rows[0].keys())

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    records = []
    for r in rows:
        rec = {k: (v if v != "" else None) for k, v in r.items()}
        for k in ("year", "relevance_sigma_trap", "citation_count"):
            if rec.get(k) not in (None, ""):
                try:
                    rec[k] = int(float(rec[k]))
                except ValueError:
                    pass
        records.append(rec)

    manifest = {
        "schema_version": "1.0",
        "n_papers": len(records),
        "exported_at": __import__("datetime").date.today().isoformat(),
        "fields": fields,
        "records": records,
    }
    OUT_JSON.write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"exported {len(records)} records -> {OUT_CSV.name} ({OUT_CSV.stat().st_size//1024}KB) "
          f"+ {OUT_JSON.name} ({OUT_JSON.stat().st_size//1024}KB)")


if __name__ == "__main__":
    sys.exit(main())
