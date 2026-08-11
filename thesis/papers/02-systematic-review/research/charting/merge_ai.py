#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.2.3): validate + merge external-AI extraction
output into the long-format charted data.

Reads:
  - research/charting/prefill.json                      (bibliographic seeds)
  - research/charting/pilot-extractions/pilot-rows.jsonl (gold standard)
  - research/charting/ai-prompt-batches/ai-output/batch-*.jsonl (AI output)

Validates every record against charted-schema.yaml (field names, controlled
vocabularies, numeric ranges, sub-exp contract), applies `flag` corrections
(logged in notes as ai-revised:field=old->new), computes calculated fields
(id_ood_gap_raw, id_ood_gap_se, reproducibility_score, model_scale_category
fallback), and merges into the LONG format: one row per
study x split x architecture x intervention (template section 3, Tasks
7.2.4-7.2.6), keyed by sub_exp_id = {study_id}_E{NN}.

Outputs:
  - research/charted-data.csv        (long format, study fields + sub-exp fields)
  - research/charted-data-main.csv   (one row per study, main form only)
  - research/charting/merge-report.md
"""

from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
CHARTING = BASE / "research" / "charting"
PREFILL_JSON = CHARTING / "prefill.json"
PILOT_JSONL = CHARTING / "pilot-extractions" / "pilot-rows.jsonl"
SCHEMA_YAML = CHARTING / "charted-schema.yaml"
AI_OUT_DIR = CHARTING / "ai-prompt-batches" / "ai-output"
OUT_CSV = BASE / "research" / "charted-data.csv"
OUT_MAIN_CSV = BASE / "research" / "charted-data-main.csv"
REPORT_MD = CHARTING / "merge-report.md"

REQUIRED_STUDY_FIELDS = [  # schema-level required, ai-source (must appear in contract)
    "pub_type", "task_primary", "ood_split_type", "arch_primary", "arch_family",
    "model_scale_category", "train_regime", "baseline_regime", "augmentation_used",
    "curriculum_used", "meta_learning_used", "id_metric_type", "ood_metric_type",
    "effect_size_type", "effect_size_computed_by_extractor", "schema_coherence_measured",
    "repr_analysis", "ci_reported", "error_bars_reported", "n_seeds_reported",
    "sig_test_reported", "multiple_testing_correction", "data_leakage_check",
    "code_available", "data_available", "model_weights_available",
    "relevance_sigma_trap", "relevance_sigma_justification",
    "relevance_alignment", "relevance_alignment_justification",
    "limitations_stated", "open_questions_stated",
]

BOOL_SYNONYMS = {
    "true": "TRUE", "false": "FALSE", "yes": "TRUE", "no": "FALSE",
    "y": "TRUE", "n": "FALSE", "1": "TRUE", "0": "FALSE",
    "unclear": "FALSE",
}


def normalize_vocab(value, allowed: set[str]) -> str | None:
    """Case-insensitive match against the controlled vocabulary."""
    v = str(value).strip()
    if v in allowed:
        return v
    up = v.upper()
    if up in allowed:
        return up
    if up in BOOL_SYNONYMS and BOOL_SYNONYMS[up] in allowed:
        return BOOL_SYNONYMS[up]
    return None


def load_schema() -> dict:
    return yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))


def build_meta(cfg: dict) -> tuple[dict, dict]:
    """Return (field->meta, vocab name -> set of allowed values)."""
    meta: dict[str, dict] = {}
    for f in cfg["study_fields"] + cfg["subexp_fields"]:
        meta[f["name"]] = f
    vocab: dict[str, set[str]] = {}
    for name, vals in cfg["vocabularies"].items():
        vocab[name] = {str(x) for x in vals}
    return meta, vocab


def validate_study_record(obj: dict, meta: dict, vocab: dict,
                          prefill: dict) -> tuple[list[str], list[str]]:
    """Return (errors, notes) for one AI study record."""
    errors: list[str] = []
    sid = obj.get("study_id")
    if not sid or sid not in prefill:
        errors.append(f"unknown study_id {sid!r}")
        return errors, []
    for key in obj:
        if key in ("study_id", "sub_experiments", "flag"):
            continue
        if key not in meta:
            errors.append(f"unknown field {key!r}")
    for key in REQUIRED_STUDY_FIELDS:
        if key not in obj:
            errors.append(f"missing required field {key!r}")
    # vocabulary + numeric validation
    for key, val in obj.items():
        if key in ("study_id", "sub_experiments", "flag") or not isinstance(val, str):
            continue
        fm = meta.get(key)
        if not fm or val == "":
            continue
        if "vocabulary" in fm:
            allowed = vocab.get(fm["vocabulary"], set())
            if normalize_vocab(val, allowed) is None:
                errors.append(f"field {key} value {val!r} not in vocabulary "
                              f"{fm['vocabulary']}")
        elif fm.get("data_type") in ("numeric", "integer"):
            rng = fm.get("range")
            if rng is not None:
                try:
                    num = float(val)
                except ValueError:
                    errors.append(f"field {key} value {val!r} not numeric")
                    continue
                lo, hi = rng
                if not (lo <= num <= hi):
                    errors.append(f"field {key} value {val} out of range {rng}")
    return errors, []


def normalize_record(obj: dict, meta: dict, vocab: dict) -> dict:
    """Normalize vocab values + numbers in a record (mutating-safe copy)."""
    out = dict(obj)
    for key, val in list(out.items()):
        if key in ("study_id", "sub_experiments", "flag") or not isinstance(val, str):
            continue
        fm = meta.get(key)
        if not fm or val == "":
            continue
        if "vocabulary" in fm:
            allowed = vocab.get(fm["vocabulary"], set())
            norm = normalize_vocab(val, allowed)
            if norm is not None:
                out[key] = norm
        elif fm.get("data_type") == "numeric":
            try:
                out[key] = f"{float(val):g}"
            except ValueError:
                pass
        elif fm.get("data_type") == "integer":
            try:
                out[key] = str(int(float(val)))
            except ValueError:
                pass
    return out


def calc_gap(row: dict) -> None:
    """Fill calculated fields in a study-level row (in place)."""
    try:
        idm, ood = float(row.get("id_acc_mean") or "nan"), float(row.get("ood_acc_mean") or "nan")
        if math.isfinite(idm) and math.isfinite(ood):
            row["id_ood_gap_raw"] = f"{idm - ood:.6g}"
    except ValueError:
        pass
    try:
        ids = float(row.get("id_acc_sd") or "nan")
        odds = float(row.get("ood_acc_sd") or "nan")
        idn = float(row.get("id_acc_n_seeds") or "nan")
        odon = float(row.get("ood_acc_n_seeds") or "nan")
        if all(math.isfinite(x) for x in (ids, odds, idn, odon)) \
                and idn > 1 and odon > 1:
            se = math.sqrt(ids ** 2 / idn + odds ** 2 / odon)
            row["id_ood_gap_se"] = f"{se:.6g}"
    except ValueError:
        pass
    # reproducibility_score from availability flags
    flags = [row.get("code_available"), row.get("data_available"),
             row.get("model_weights_available")]
    n_true = sum(1 for f in flags if f == "TRUE")
    row["reproducibility_score"] = {3: "high", 2: "medium", 1: "partial", 0: "low"}[n_true]
    # model_scale_category fallback from param_count
    if row.get("param_count") and not row.get("model_scale_category"):
        try:
            pc = float(row["param_count"])
            row["model_scale_category"] = ("small" if pc < 1e6 else
                                           "medium" if pc < 1e8 else
                                           "large" if pc < 1e10 else "xl")
        except ValueError:
            pass


def main() -> None:
    cfg = load_schema()
    meta, vocab = build_meta(cfg)
    prefill = json.loads(PREFILL_JSON.read_text(encoding="utf-8"))
    study_field_names = [f["name"] for f in cfg["study_fields"]]
    subexp_field_names = [f["name"] for f in cfg["subexp_fields"]]

    # pilot gold standard (protected)
    pilots: dict[str, dict] = {}
    for line in PILOT_JSONL.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rec = json.loads(line)
            pilots[rec["study_id"]] = rec

    # merge AI output
    out_files = sorted(AI_OUT_DIR.glob("batch-*.jsonl"))
    merged: dict[str, dict] = {}
    bad: list[tuple[str, str, str]] = []
    revisions: list[str] = []
    n_flags = 0

    for f in out_files:
        for lineno, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                bad.append((f.name, f"line {lineno}", "invalid JSON"))
                continue
            errors, _ = validate_study_record(obj, meta, vocab, prefill)
            if errors:
                bad.append((f.name, str(obj.get("study_id")), "; ".join(errors[:3])))
                continue
            sid = obj["study_id"]
            if sid in pilots:
                bad.append((f.name, sid, "pilot gold standard — re-extraction rejected"))
                continue
            obj = normalize_record(obj, meta, vocab)
            # apply flag corrections
            flags = obj.get("flag") or {}
            if not isinstance(flags, dict):
                bad.append((f.name, sid, "flag not an object"))
                continue
            notes_log = []
            for field, val in flags.items():
                if field not in meta or "vocabulary" not in meta.get(field, {}):
                    bad.append((f.name, sid, f"unknown/non-categorical flag field {field}"))
                    continue
                allowed = vocab.get(meta[field]["vocabulary"], set())
                norm = normalize_vocab(val, allowed)
                if norm is None:
                    bad.append((f.name, sid, f"flag {field} value {val!r} not in vocabulary"))
                    continue
                old = obj.get(field, "")
                if old != norm:
                    obj[field] = norm
                    notes_log.append(f"ai-revised:{field}={old}->{norm}")
                    revisions.append(f"{sid}:{field}:{old}->{norm}")
                    n_flags += 1
            obj["notes"] = ((obj.get("notes") or "") + " | " + " | ".join(notes_log)).strip(" |")
            merged[sid] = obj

    missing = [sid for sid in prefill if sid not in merged and sid not in pilots]
    n_merged = len(merged)

    # build long-format rows
    long_rows: list[dict] = []
    main_rows: list[dict] = []

    def default_subexp(sid: str) -> dict:
        return {k: "" for k in subexp_field_names} | {
            "sub_exp_id": f"{sid}_E001", "experiment_label": "default",
            "task": "", "arch": "", "train_regime": "",
            "effect_size_type": "none",
        }

    for sid in sorted(prefill, key=lambda s: int(s[1:])):
        rec = merged.get(sid) or pilots.get(sid)
        if rec is None:
            continue
        row = {k: "" for k in study_field_names}
        row.update({k: rec.get(k, "") for k in study_field_names})
        # prefilled bibliographic from prefill.json (never overwritten by AI blanks)
        for k in ("study_id", "id", "title", "authors", "year", "venue", "doi",
                  "arxiv_id", "extractor_id"):
            if k in prefill[sid] and prefill[sid][k] not in ("", None):
                row[k] = prefill[sid][k]
        # peer_reviewed / pub_venue_type: AI confirms from full text; prefill is
        # the fallback when the AI left the field empty (pilot finding R1)
        for k in ("peer_reviewed", "pub_venue_type"):
            if row.get(k) in ("", None):
                if k in prefill[sid] and prefill[sid][k] not in ("", None):
                    row[k] = prefill[sid][k]
        calc_gap(row)
        main_rows.append(row)

        subexps = rec.get("sub_experiments") or []
        if not subexps:
            subexps = [default_subexp(sid)]
        for se in subexps:
            if not isinstance(se, dict):
                continue
            se = normalize_record(se, meta, vocab)
            errors, _ = validate_subexp(se, meta, vocab, sid)
            if errors:
                bad.append(("(sub_exp)", sid, "; ".join(errors)))
                continue
            lrow = dict(row)
            lrow.update({k: se.get(k, "") for k in subexp_field_names})
            # ensure key linkage
            lrow["study_id"] = sid
            lrow["id"] = row["id"]
            lrow["sub_exp_id"] = se.get("sub_exp_id") or f"{sid}_E001"
            # calculated sub-exp gap
            try:
                idm = float(se.get("id_acc_mean") or "nan")
                ood = float(se.get("ood_acc_mean") or "nan")
                if math.isfinite(idm) and math.isfinite(ood):
                    lrow["id_ood_gap"] = f"{idm - ood:.6g}"
            except ValueError:
                pass
            long_rows.append(lrow)

    # write long CSV
    long_cols = ["study_id", "id", "split_id", "arch_id", "intervention_id",
                 "sub_exp_id"] + study_field_names + subexp_field_names
    long_cols = list(dict.fromkeys(long_cols))
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=long_cols, extrasaction="ignore")
        w.writeheader()
        for r in long_rows:
            r["split_id"] = r.get("split_id", "") or "default"
            r["arch_id"] = r.get("arch_id", "") or "default"
            r["intervention_id"] = r.get("intervention_id", "") or "default"
            w.writerow(r)
    with open(OUT_MAIN_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=study_field_names)
        w.writeheader()
        w.writerows(main_rows)

    # report
    with open(REPORT_MD, "w", encoding="utf-8") as fh:
        fh.write("# AI merge report — Paper 02 Phase 7 (Task 7.2)\n\n")
        fh.write(f"- AI output files read: **{len(out_files)}**\n")
        fh.write(f"- Studies merged (AI): **{n_merged}**\n")
        fh.write(f"- Gold-standard pilots (protected): **{len(pilots)}** "
                 f"({', '.join(sorted(pilots))})\n")
        fh.write(f"- Studies missing from AI output: **{len(missing)}** "
                 f"({', '.join(missing[:20]) or '—'}{' …' if len(missing) > 20 else ''})\n")
        fh.write(f"- Long-format rows: **{len(long_rows)}** "
                 f"(study x split x arch x intervention)\n")
        fh.write(f"- Main-form rows: **{len(main_rows)}**\n")
        fh.write(f"- flag corrections applied: **{n_flags}**\n")
        fh.write(f"- Invalid records rejected: **{len(bad)}**\n")
        if revisions:
            fh.write("\n## Revisions applied\n\n")
            for r in revisions:
                fh.write(f"- {r}\n")
        if bad:
            fh.write("\n## Rejected records\n\n")
            for f_, p, reason in bad:
                fh.write(f"- {f_}: {p} — {reason}\n")
        if missing:
            fh.write("\n## Missing studies (re-run batch)\n\n")
            for sid in missing:
                fh.write(f"- {sid}\n")

    print(f"AI studies merged: {n_merged}; pilots: {len(pilots)}; "
          f"missing: {len(missing)}; flags: {n_flags}; bad: {len(bad)}")
    print(f"long rows: {len(long_rows)} -> {OUT_CSV}; main rows: {len(main_rows)}")
    print(f"wrote {REPORT_MD.name}")


def validate_subexp(se: dict, meta: dict, vocab: dict, sid: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    if not se.get("sub_exp_id"):
        errors.append("missing sub_exp_id")
    elif not se["sub_exp_id"].startswith(f"{sid}_E"):
        errors.append(f"sub_exp_id {se['sub_exp_id']!r} must start with {sid}_E")
    for key, val in se.items():
        if key in ("sub_exp_id", "notes") or not isinstance(val, str):
            continue
        fm = meta.get(key)
        if not fm or val == "":
            continue
        if "vocabulary" in fm:
            if normalize_vocab(val, vocab.get(fm["vocabulary"], set())) is None:
                errors.append(f"sub_exp field {key} value {val!r} not in vocabulary")
        elif fm.get("data_type") in ("numeric", "integer"):
            rng = fm.get("range")
            if rng is not None:
                try:
                    num = float(val)
                    if not (rng[0] <= num <= rng[1]):
                        errors.append(f"sub_exp field {key} value {val} out of range {rng}")
                except ValueError:
                    errors.append(f"sub_exp field {key} value {val!r} not numeric")
    return errors, []


if __name__ == "__main__":
    sys.exit(main())
