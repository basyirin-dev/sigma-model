#!/usr/bin/env python3
"""
Paper 01 — Phase 7: σ-trap signal export + per-batch theme digest.

Task: give the review's alignment-failure synthesis the highest-signal rows
and a familiarization digest of what each extraction batch contained.

Outputs:
  research/sigma-trap-signal.csv    — papers with final relevance >= 4 or an
                                     AI revision, with seed vs final + justification
  research/charting/theme-digest.md — per-batch topic clusters (subdomains +
                                     key_contribution keyword counts)
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
BATCH_DIR = BASE / "research" / "charting" / "ai-prompt-batches"
OUT_SIGNAL = BASE / "research" / "sigma-trap-signal.csv"
OUT_DIGEST = BASE / "research" / "charting" / "theme-digest.md"

STOP = set("""the of and a to in for on with we our this that is are as by from an it
its their these those be was were has have had not at or about more most such can
use using used via into over under between while when where which paper work study
results result model models system systems approach method methods framework
propose proposes proposed present presents introduce introduces show shows
demonstrate demonstrates demonstrate addresses address discuss discusses
argue argues suggest suggests provide provides develop develops develop""".split())


def main() -> None:
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    ann = {r["study_id"]: r["relevance_score"] for r in
           csv.DictReader(open(BASE / "research" / "retrieval" / "annotations.csv"))}

    # --- sigma-trap signal export -------------------------------------------
    signal = []
    for r in rows:
        final = (r.get("relevance_sigma_trap") or "").strip()
        seed = (ann.get(r["paper_id"], "") or "").strip()
        revised = final not in ("", seed)
        if not final:
            continue
        if int(final) >= 4 or revised:
            signal.append({
                "paper_id": r["paper_id"], "title": r["title"], "year": r["year"],
                "relevance_seed": seed, "relevance_final": final,
                "revised": "yes" if revised else "no",
                "relevance_justification": r.get("relevance_justification", ""),
                "subdomains": r.get("subdomains", ""),
                "formal_framework": r.get("formal_framework", ""),
            })
    with open(OUT_SIGNAL, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(signal[0].keys()))
        w.writeheader()
        w.writerows(signal)

    # --- per-batch theme digest ---------------------------------------------
    batch_of: dict[str, str] = {}
    for bf in sorted(BATCH_DIR.glob("batch-*.jsonl")):
        for line in bf.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            import json
            batch_of[json.loads(line)["paper_id"]] = bf.stem
    by_batch: dict[str, list[dict]] = {f"batch-{i:02d}": [] for i in range(1, 6)}
    for r in rows:
        b = batch_of.get(r["paper_id"])
        if b and b in by_batch:
            by_batch[b].append(r)

    with open(OUT_DIGEST, "w", encoding="utf-8") as fh:
        fh.write("# Per-batch theme digest — Paper 01 Phase 7\n\n")
        for b in sorted(by_batch):
            br = by_batch[b]
            subs = Counter()
            kws = Counter()
            rel = Counter()
            for r in br:
                for s in (r.get("subdomains") or "").split(";"):
                    s = s.strip()
                    if s:
                        subs[s] += 1
                kc = r.get("key_contribution") or ""
                for tok in re.findall(r"[a-z][a-z-]{3,}", kc.lower()):
                    if tok not in STOP and len(tok) >= 5:
                        kws[tok] += 1
                rel[r.get("relevance_sigma_trap", "")] += 1
            fh.write(f"## {b} ({len(br)} papers)\n\n")
            fh.write("**Subdomains:** " + ", ".join(
                f"{k} ({v})" for k, v in subs.most_common(6)) + "\n\n")
            fh.write("**Top keywords (key_contribution):** " + ", ".join(
                f"{k} ({v})" for k, v in kws.most_common(12)) + "\n\n")
            fh.write("**Relevance dist:** " + ", ".join(
                f"σ={k}:{v}" for k, v in sorted(rel.items(), key=lambda x: str(x[0]))) + "\n\n")

    print(f"sigma-trap signal: {len(signal)} rows -> {OUT_SIGNAL.name}")
    print(f"theme digest: {OUT_DIGEST.name}")


if __name__ == "__main__":
    sys.exit(main())
