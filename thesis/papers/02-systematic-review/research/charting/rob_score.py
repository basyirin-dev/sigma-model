#!/usr/bin/env python3
"""
Paper 02 — Phase 8 (Task 8.3): σ-ROB scripted judgment engine.

Loads charting/rob-rules.yaml (ADR-0004 config-driven) and applies it to the
study-level charted data (research/charted-data-main.csv) plus long-format
aggregates (research/charted-data.csv), producing:

  research/risk-of-bias.csv          study-level D1-D6 + overall + rule trace
  research/charting/rob-diagnostic.md  judgment distribution + fill diagnostics

Operationalizations (phases/08_quality_assessment.md): blank -> Unclear,
explicit FALSE -> High trigger, D3 N/A when no intervention comparison,
overall = worst of applicable domains (quality-criteria.md §12.1).

Usage: python3 rob_score.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
MAIN_CSV = BASE / "research" / "charted-data-main.csv"
LONG_CSV = BASE / "research" / "charted-data.csv"
RULES = Path(__file__).resolve().parent / "rob-rules.yaml"
OUT_CSV = BASE / "research" / "risk-of-bias.csv"
OUT_MD = Path(__file__).resolve().parent / "rob-diagnostic.md"


def load_csv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def compute_aggregates(long_rows: list[dict], study_id: str) -> dict:
    """Aggregates derived from the long format for one study."""
    subs = [r for r in long_rows if r.get("study_id") == study_id]
    n_archs = len({r.get("arch_id") for r in subs})
    n_subs = len(subs)
    return {
        "n_subs": n_subs,
        "multi_arch": n_archs > 1,
    }


def evaluate(rules: dict, rec: dict, agg: dict) -> tuple[str, str]:
    """Return (judgment, rule_trace) for one domain."""
    domain_rules = rules["domains"]
    for domain, spec in domain_rules.items():
        judgment, trace = eval_domain(domain, spec, rec, agg)
        yield domain, judgment, trace


def match_clause(clause: dict, rec: dict, agg: dict) -> bool:
    if "field" in clause:
        val = (rec.get(clause["field"]) or "").strip()
        return val in clause["in"]
    if "computed" in clause:
        val = agg.get(clause["computed"])
        return bool(val) is clause["eq"]
    return False


def eval_domain(domain: str, spec: dict, rec: dict, agg: dict) -> tuple[str, str]:
    # na
    for group in spec.get("na", []):
        if all(match_clause(c, rec, agg) for c in group):
            return "N/A", f"{domain}:na"
    for level in ("high", "unclear", "low"):
        for group in spec.get(level, []):
            if all(match_clause(c, rec, agg) for c in group):
                return level.upper(), f"{domain}:{level}"
    return spec.get("default", "LOW"), f"{domain}:default"


def main() -> int:
    rules = yaml.safe_load(RULES.read_text(encoding="utf-8"))
    mains = load_csv(MAIN_CSV)
    longs = load_csv(LONG_CSV)
    long_by_study = {r.get("study_id"): r for r in longs}
    del long_by_study  # aggregates need the full list; handled below

    order = rules["overall"]["order"]  # [High, Unclear, Low]
    rank = {v: i for i, v in enumerate(order)}

    out_rows = []
    diag = {d: {"HIGH": 0, "UNCLEAR": 0, "LOW": 0, "N/A": 0} for d in rules["domains"]}
    diag["OVERALL"] = {"HIGH": 0, "UNCLEAR": 0, "LOW": 0, "N/A": 0}

    for rec in mains:
        sid = rec.get("study_id")
        agg = compute_aggregates(longs, sid)
        agg["interventional"] = (rec.get("train_regime_sigma") or "").strip() in (
            "other_sigma", "TRUE") or (rec.get("baseline_regime") or "").strip() != ""
        agg["multi_bench"] = (rec.get("tasks_secondary") or "").strip() != ""
        # R1 (pilot refinement): arch_detail free text lists multiple architectures
        # (e.g. "3 baseline seq2seq archs: ...; ...") missed by arch_id multiplicity.
        arch_detail = (rec.get("arch_detail") or "").strip()
        agg["multi_arch"] = agg["multi_arch"] or (";" in arch_detail)
        ns = (rec.get("n_seeds_value") or "").strip()
        agg["seeds_ge3"] = ns.isdigit() and int(ns) >= 3
        agg["seeds_lt3"] = ns.isdigit() and 0 <= int(ns) < 3
        agg["seeds_val_blank"] = ns == ""
        agg["no_uq"] = (rec.get("ci_reported") or "").strip() == "FALSE" and (
            rec.get("error_bars_reported") or "").strip() == "FALSE"
        agg["sig_no_corr"] = (rec.get("sig_test_reported") or "").strip() == "TRUE" and (
            rec.get("multiple_testing_correction") or "").strip() in ("none", "unclear")
        agg["has_effect_size"] = any(
            (rec.get(f) or "").strip() != "" for f in
            ("effect_size_value", "id_ood_gap_raw", "id_ood_gap_se"))
        agg["no_effect_size"] = not agg["has_effect_size"]

        row = {"study_id": sid, "title": rec.get("title", "")}
        dom_judgments: dict[str, str] = {}
        traces: list[str] = []
        for domain, spec in rules["domains"].items():
            j, t = eval_domain(domain, spec, rec, agg)
            dom_judgments[domain] = j
            traces.append(t)
            diag[domain][j] += 1
            row[domain] = j
        applicable = [j for j in dom_judgments.values() if j != "N/A"]
        overall = min(applicable, key=lambda j: rank[j]) if applicable else "N/A"
        diag["OVERALL"][overall] += 1
        row["overall"] = overall
        row["rule_trace"] = ";".join(traces)
        out_rows.append(row)

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        fieldnames = ["study_id", "title", "D1", "D2", "D3", "D4", "D5", "D6",
                      "overall", "rule_trace"]
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(out_rows)

    lines = ["# RoB diagnostic — Paper 02 Phase 8 (rob_score.py)",
             "",
             f"Studies assessed: {len(out_rows)}",
             "",
             "| Domain | HIGH | UNCLEAR | LOW | N/A |",
             "|---|---|---|---|---|"]
    for d, counts in diag.items():
        lines.append(f"| {d} | {counts['HIGH']} | {counts['UNCLEAR']} | "
                     f"{counts['LOW']} | {counts['N/A']} |")
    lines.append("")
    lines.append("Rule semantics: blank charted field -> UNCLEAR trigger; "
                 "explicit FALSE -> HIGH trigger (quality-criteria.md §12.3).")
    (OUT_MD.parent / OUT_MD.name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"risk-of-bias.csv written ({len(out_rows)} rows)")
    print(f"diagnostic written: {OUT_MD.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
