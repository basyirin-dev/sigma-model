#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.4): data-quality checks on charted data.

Runs on research/charted-data.csv (long format):
  7.4.1  missing-data analysis — fields with >10% missing flagged
  7.4.2  inconsistent coding detection (e.g. "SCAN" vs "scan" vs "SCAN dataset")
  7.4.3  controlled-vocabulary normalization (writes a remediation CSV)
  7.4.4  numerical range checks (accuracies in [0,1], plausible SDs/seeds)
  7.4.5  cross-field validation rules V01-V20 (schema validation_rules)

Outputs:
  - research/charting/data-quality-report.md
  - research/charting/remediation-log.csv  (auto-normalized values)
"""

from __future__ import annotations

import csv
import math
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
CHARTING = BASE / "research" / "charting"
CHARTED_CSV = BASE / "research" / "charted-data.csv"
SCHEMA_YAML = CHARTING / "charted-schema.yaml"
REPORT_MD = CHARTING / "data-quality-report.md"
REMEDIATION_CSV = CHARTING / "remediation-log.csv"

MISSING_THRESHOLD = 0.10
NUMERIC_FIELDS = {
    "id_acc_mean": (0.0, 1.0), "id_acc_sd": (0.0, 1.0), "id_acc_n_seeds": (1, 1000),
    "ood_acc_mean": (0.0, 1.0), "ood_acc_sd": (0.0, 1.0), "ood_acc_n_seeds": (1, 1000),
    "id_acc_ci_lower": (0.0, 1.0), "id_acc_ci_upper": (0.0, 1.0),
    "ood_acc_ci_lower": (0.0, 1.0), "ood_acc_ci_upper": (0.0, 1.0),
    "param_count": (1, 1e12), "n_layers": (1, 1000), "hidden_dim": (1, 1e6),
    "train_n_examples": (1, 1e12), "train_n_tokens": (1, 1e15),
    "n_seeds_value": (1, 1000), "sig_test_pvalue": (0.0, 1.0),
    "relevance_sigma_trap": (1, 5), "relevance_alignment": (1, 5),
    "effect_size_value": (-1e3, 1e3), "effect_size_se": (0.0, 10.0),
}


def is_empty(v: str) -> bool:
    return v is None or str(v).strip() == ""


def main() -> None:
    cfg = yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))
    meta = {f["name"]: f for f in cfg["study_fields"] + cfg["subexp_fields"]}
    vocab: dict[str, set[str]] = {k: {str(x) for x in v} for k, v in
                                  cfg["vocabularies"].items()}
    rules = cfg["validation_rules"]

    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    n = len(rows)
    fields = list(rows[0].keys())
    report: list[str] = [
        "# Data quality report — Paper 02 Phase 7 (Task 7.4)",
        "",
        f"- Rows (long format): **{n}**",
        f"- Missing threshold: **{MISSING_THRESHOLD:.0%}**",
        "",
        "## 7.4.1 Missing data (fields >10% missing)",
        "",
        "| Field | Missing | Rate | |",
        "|---|---|---|---|",
    ]
    remediation: list[dict] = []
    norm_count = 0

    # --- 7.4.1 missingness ---
    missing_fields: list[tuple[str, int, float, str]] = []
    for f in fields:
        if f in ("study_id", "id", "sub_exp_id"):
            continue
        miss = sum(1 for r in rows if is_empty(r.get(f)))
        rate = miss / n if n else 0
        if rate > MISSING_THRESHOLD:
            fm = meta.get(f, {})
            flag = "FLAG-required" if (fm.get("required") and not fm.get("conditional")) \
                else "flag-optional/conditional"
            missing_fields.append((f, miss, rate, flag))
    for f, miss, rate, flag in sorted(missing_fields, key=lambda t: -t[2]):
        report.append(f"| {f} | {miss} | {rate:.1%} | {flag} |")
    if not missing_fields:
        report.append("| — | — | — | none above threshold |")

    # --- 7.4.2/7.4.3 inconsistent coding + normalization ---
    report += ["", "## 7.4.2 / 7.4.3 Inconsistent coding & vocabulary normalization", ""]
    for f in fields:
        fm = meta.get(f)
        if not fm or "vocabulary" not in fm:
            continue
        allowed = vocab.get(fm["vocabulary"], set())
        multi = fm.get("data_type") == "categorical-multi"

        def tokens(v: str) -> list[str]:
            return [t.strip() for t in v.split(";")] if multi else [v.strip()]

        seen: Counter[str] = Counter()
        for r in rows:
            v = r.get(f, "")
            if not is_empty(v):
                for t in tokens(v):
                    if t:
                        seen[t] += 1
        # detect variants: lowercase/case-folded duplicates of allowed values
        for raw, cnt in sorted(seen.items(), key=lambda kv: -kv[1]):
            up = raw.upper()
            if up in allowed and raw != up:
                for r in rows:
                    if not is_empty(r.get(f, "")):
                        toks = tokens(r[f])
                        if raw in toks:
                            new_toks = [up if t == raw else t for t in toks]
                            new = "; ".join(t for t in new_toks if t) if multi else new_toks[0]
                            r[f] = new
                            remediation.append({"field": f, "study_id": r["study_id"],
                                                "row": r["sub_exp_id"], "old": raw, "new": up})
                            norm_count += 1
                report.append(f"- `{f}`: '{raw}' x{cnt} normalized -> '{up}'")
            elif raw not in allowed:
                report.append(f"- `{f}`: **{raw!r} x{cnt} not in vocabulary "
                              f"({fm['vocabulary']})** — review manually")

    # --- 7.4.4 numeric range checks ---
    report += ["", "## 7.4.4 Numeric range checks", ""]
    out_of_range: list[str] = []
    for f, (lo, hi) in NUMERIC_FIELDS.items():
        for r in rows:
            v = r.get(f, "")
            if is_empty(v):
                continue
            try:
                num = float(v)
            except ValueError:
                out_of_range.append(f"{r['study_id']}/{f}: '{v}' not numeric")
                continue
            if not (lo <= num <= hi):
                out_of_range.append(f"{r['study_id']}/{f}: {num} outside [{lo}, {hi}]")
    # percentage-vs-proportion guard: accuracies reported as 0-100
    for f in ("id_acc_mean", "ood_acc_mean", "id_acc_sd", "ood_acc_sd"):
        for r in rows:
            v = r.get(f, "")
            if not is_empty(v):
                try:
                    num = float(v)
                    if num > 1.0 and num <= 100.0:
                        out_of_range.append(
                            f"{r['study_id']}/{f}: {num} looks like a PERCENTAGE — "
                            "convert to proportion 0-1")
                except ValueError:
                    pass
    if out_of_range:
        for o in out_of_range:
            report.append(f"- {o}")
    else:
        report.append("- no out-of-range values")

    # --- 7.4.5 cross-field validation V01-V20 ---
    report += ["", "## 7.4.5 Cross-field validation (V01-V20)", "",
               "| Rule | Severity | Violations |", "|---|---|---|"]
    rule_violations: list[tuple[str, str, str]] = []
    # honest per-rule error counts (not capped) for the summary
    error_counts: Counter[str] = Counter()

    def field(r: dict, name: str) -> str:
        return r.get(name, "")

    def fnum(v: str) -> float:
        """Parse numeric cell; raises ValueError for junk (rule = violation)."""
        return float(v)

    def check_rule(rid: str, vals: list[str], r: dict) -> bool:
        """Evaluate one V-rule for one row; junk numerics count as violations."""
        if rid == "V01":
            return is_empty(vals[0]) or not is_empty(vals[1])
        if rid == "V02":
            return is_empty(vals[0]) or not is_empty(vals[1])
        if rid == "V03":
            return is_empty(vals[0]) or (not is_empty(vals[1]) and fnum(vals[1]) >= 2)
        if rid == "V04":
            return is_empty(vals[0]) or (not is_empty(vals[1]) and fnum(vals[1]) >= 2)
        if rid == "V05":
            # sub-exp gap (S13) must equal its own id/ood means; study-level
            # gap (id_ood_gap_raw) is checked separately on the main CSV
            gap = field(r, "id_ood_gap")
            if is_empty(gap):
                return True
            return abs(fnum(gap) - (fnum(field(r, "id_acc_mean"))
                                    - fnum(field(r, "ood_acc_mean")))) <= 0.001
        if rid == "V06":
            return vals[0] == "none" or not is_empty(vals[1])
        if rid == "V07":
            return (vals[0] != "sigma_coupled"
                    or (not is_empty(vals[1]) and vals[1] != "not_applicable"))
        if rid == "V08":
            return vals[0] != "TRUE" or not is_empty(vals[1])
        if rid == "V09":
            return vals[0] != "TRUE" or (not is_empty(vals[1]) and fnum(vals[1]) >= 1)
        if rid == "V10":
            return vals[0] != "TRUE" or vals[1] not in ("", "none")
        if rid == "V11":
            return vals[0] != "TRUE" or not is_empty(vals[1])
        if rid == "V12":
            return vals[0] != "TRUE" or not is_empty(vals[1])
        if rid == "V13":
            return is_empty(vals[0]) or fnum(vals[0]) < 4 or len(vals[1] or "") >= 100
        if rid == "V14":
            return is_empty(vals[0]) or fnum(vals[0]) < 4 or len(vals[1] or "") >= 100
        if rid == "V15":
            return vals[0] != "none" or is_empty(field(r, "ood_acc_mean"))
        if rid == "V16":
            return is_empty(vals[0]) or is_empty(vals[1]) or vals[0] == vals[1]
        if rid == "V17":
            return vals[0] != "TRUE" or len(vals[1] or "") > 0
        if rid == "V18":
            return True  # info-only
        if rid == "V19":
            # model_scale_category consistent with param_count (when both present)
            if is_empty(vals[0]) or is_empty(field(r, "model_scale_category")):
                return True
            pc = fnum(vals[0])
            expect = ("small" if pc < 1e6 else
                      "medium" if pc < 1e8 else
                      "large" if pc < 1e10 else "xl")
            return field(r, "model_scale_category").strip().lower() == expect
        return True  # V20 advisory + unknown

    for rule in rules:
        rid = rule["id"]
        sev = rule.get("severity", "error")
        fields_ = rule["fields"]
        bad = 0
        for r in rows:
            vals = [field(r, f) for f in fields_]
            try:
                ok = check_rule(rid, vals, r)
            except ValueError:
                ok = False  # non-numeric cell where a number is required
            if not ok:
                bad += 1
                if sev == "error":
                    error_counts[rid] += 1
                if sum(1 for rid_, _, _ in rule_violations if rid_ == rid) < 60:
                    rule_violations.append((rid, sev, f"{r['study_id']}/{r['sub_exp_id']}"))
        flag = " ⚠" if bad and sev == "error" else ""
        report.append(
            f"| {rid} | {sev} | {bad}{flag} |")

    # study-level gap consistency (V05 on charted-data-main.csv)
    main_rows = list(csv.DictReader(
        open(BASE / "research" / "charted-data-main.csv", newline="", encoding="utf-8")))
    main_gap_bad = 0
    for r in main_rows:
        if is_empty(r.get("id_ood_gap_raw")):
            continue
        try:
            idm = float(r["id_acc_mean"] or "nan")
            ood = float(r["ood_acc_mean"] or "nan")
            if not math.isnan(idm) and not math.isnan(ood) and \
                    abs(float(r["id_ood_gap_raw"]) - (idm - ood)) > 0.001:
                main_gap_bad += 1
        except ValueError:
            main_gap_bad += 1
    report.append(
        f"- V05 (study-level, main CSV): {main_gap_bad} rows with id_ood_gap_raw "
        f"!= id_acc_mean - ood_acc_mean")

    # --- remediation log ---
    with open(REMEDIATION_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["field", "study_id", "row", "old", "new"])
        w.writeheader()
        w.writerows(remediation)
    with open(CHARTED_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    n_error_violations = sum(error_counts.values())
    report += [
        "",
        "## Summary",
        "",
        f"- Fields >10% missing: **{len(missing_fields)}** "
        f"({sum(1 for _, _, _, fl in missing_fields if fl.startswith('FLAG-required'))} required)",
        f"- Vocabulary values auto-normalized: **{norm_count}** "
        f"(see remediation-log.csv)",
        f"- Numeric range violations: **{len(out_of_range)}**",
        f"- V01-V20 error-level violations: **{n_error_violations}** "
        f"(per-rule: {', '.join(f'{k}={v}' for k, v in sorted(error_counts.items()))})",
    ]
    with open(REPORT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(report) + "\n")

    print(f"wrote {REPORT_MD.name}: {len(missing_fields)} missing>10% fields, "
          f"{norm_count} normalized, {len(out_of_range)} range issues, "
          f"{len(rule_violations)} V-rule violations")


if __name__ == "__main__":
    sys.exit(main())
