#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.5.1/7.5.2, CC.4.3): export charted data.

Reads the long-format research/charted-data.csv and emits:
  - research/charted-data.json   nested: study -> sub_experiments
  - research/charted-data.csv    long format (canonical, already written by
                                 merge_ai.py / quality.py; this script re-emits
                                 it unchanged after a final pass)
  - research/charted-data-main.csv  one row per study (re-emitted)

The JSON follows template section 7 export format 3 (nested paper ->
sub-experiments) for programmatic validation and OSF deposit.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
CHARTED_CSV = BASE / "research" / "charted-data.csv"
OUT_JSON = BASE / "research" / "charted-data.json"

# study-level columns (prefix of the long CSV) — everything up to sub-exp keys
SUBEXP_KEYS = {"sub_exp_id", "experiment_label", "task", "arch", "train_regime",
               "id_acc_mean", "id_acc_sd", "id_acc_n_seeds", "ood_acc_mean",
               "ood_acc_sd", "ood_acc_n_seeds", "id_ood_gap", "effect_size_type",
               "effect_size_value", "effect_size_se", "schema_coherence_value",
               "notes"}


def main() -> None:
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    study_fields = [k for k in rows[0].keys()
                    if k not in SUBEXP_KEYS and k not in
                    ("split_id", "arch_id", "intervention_id")]
    nested: dict[str, dict] = {}
    for r in rows:
        sid = r["study_id"]
        study = nested.setdefault(sid, {k: r.get(k, "") for k in study_fields})
        study.setdefault("sub_experiments", [])
        subexp = {k: r.get(k, "") for k in SUBEXP_KEYS}
        subexp["split_id"] = r.get("split_id", "default")
        subexp["arch_id"] = r.get("arch_id", "default")
        subexp["intervention_id"] = r.get("intervention_id", "default")
        study["sub_experiments"].append(subexp)

    # order studies by S-number; sub-experiments by sub_exp_id
    ordered = {}
    for sid in sorted(nested, key=lambda s: int(s[1:])):
        study = nested[sid]
        study["sub_experiments"].sort(key=lambda se: se.get("sub_exp_id", ""))
        ordered[sid] = study

    OUT_JSON.write_text(
        json.dumps(ordered, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    n_sub = sum(len(s["sub_experiments"]) for s in ordered.values())
    print(f"wrote {OUT_JSON.name}: {len(ordered)} studies, {n_sub} sub-experiments")
    print(f"canonical long CSV: {CHARTED_CSV.name} ({len(rows)} rows)")


if __name__ == "__main__":
    sys.exit(main())
