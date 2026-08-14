#!/usr/bin/env python3
"""
Paper 01 — Phase 7: scripted heuristic extraction of structured fields.

Deterministic, vocabulary-driven extraction of the [†] categorical fields
from the finalized schema (Task 7.2.3). Evidence text per paper:
  full-text (first 4 PDF pages) when mapped (pdf-map.csv), else abstract
  from included-studies.csv, else metadata only (fields left empty).

Fills: publication_type, subdomains, formal_framework,
mathematical_formalism, methodology, discusses_internal_representations,
discusses_schema_coherence, limitations_stated, relevance_sigma_trap (seed
kept from annotations), notes (evidence length + confidence flags).

Config: heuristic-config.yaml (keyword regexes) + charted-schema.yaml
(subdomain_mapping not needed here — config carries its own vocabularies).
Output: research/charting/charted-data.csv (updated in place of base).
"""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
PDF_MAP_CSV = BASE / "research" / "charting" / "pdf-map.csv"
PDF_DIR = BASE / "research" / "pdfs"
CONFIG_YAML = BASE / "research" / "charting" / "heuristic-config.yaml"
FULLTEXT_PAGES = 6
MAX_TEXT = 15000  # chars of evidence text per paper
MIN_ABS_CHARS = 100  # abstract long enough to classify from


def load_config() -> dict:
    return yaml.safe_load(CONFIG_YAML.read_text(encoding="utf-8"))


def compile_patterns(groups: dict[str, list[str]]) -> dict[str, list[re.Pattern]]:
    out: dict[str, list[re.Pattern]] = {}
    for name, pats in groups.items():
        compiled = []
        for p in pats:
            try:
                compiled.append(re.compile(p, re.I))
            except re.error as e:
                print(f"WARN: bad pattern {p!r} in {name}: {e}")
        out[name] = compiled
    return out


def pdf_text(pdf_file: str) -> str:
    path = PDF_DIR / pdf_file
    try:
        out = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(FULLTEXT_PAGES), str(path), "-"],
            capture_output=True, text=True, timeout=45,
        )
    except Exception:
        return ""
    return (out.stdout or "")


def evidence_text(basis: str, pdf_file: str, abstract: str) -> str:
    if basis == "full-text" and pdf_file:
        txt = pdf_text(pdf_file)
        if txt.strip():
            return txt[:MAX_TEXT]
    return abstract or ""


def hit_counts(text: str, patterns: list[re.Pattern]) -> int:
    return sum(len(p.findall(text)) for p in patterns)


def classify_multi(text: str, compiled: dict[str, list[re.Pattern]]) -> list[str]:
    scored = [(name, hit_counts(text, pats)) for name, pats in compiled.items()]
    hits = [n for n, c in scored if c > 0]
    return hits


def classify_pubtype(title: str, text: str, compiled: dict[str, list[re.Pattern]]) -> str:
    """publication_type decision:
    - 'survey/review/state of the art' in the TITLE -> review
    - empirical_hits > review_hits -> empirical (a survey-of-humans paper
      mentions 'survey' once but reports experiments/benchmarks many times)
    - review_hits > 0 -> review
    - else first priority bucket that hits: theoretical/position/opinion/
      technical_report -> other."""
    tl = title.lower()
    if re.search(r"\b(survey|review|state of the art|literature)\b", tl):
        return "review"
    emp = hit_counts(text, compiled["empirical"])
    rev = hit_counts(text, compiled["review"])
    if emp > rev:
        return "empirical"
    if rev > 0:
        return "review"
    for name in ("theoretical", "position", "opinion", "technical_report"):
        if hit_counts(text, compiled[name]) > 0:
            return name
    return "other"


def classify_single_best(text: str, compiled: dict[str, list[re.Pattern]]) -> str:
    scored = [(name, hit_counts(text, pats)) for name, pats in compiled.items()]
    scored.sort(key=lambda x: -x[1])
    return scored[0][0] if scored and scored[0][1] > 0 else "not_applicable"


def trinary(text: str, strong: list[re.Pattern], weak: list[re.Pattern],
            context: list[re.Pattern] | None = None) -> str:
    s = hit_counts(text, strong)
    if s == 0:
        return "no"
    if context is None or hit_counts(text, context) > 0:
        return "yes"
    return "implicitly"


def main() -> None:
    cfg = load_config()
    pt = compile_patterns(cfg["publication_type"])
    sub = compile_patterns(cfg["subdomains"])
    ff = compile_patterns(cfg["formal_framework"])
    mf = compile_patterns(cfg["mathematical_formalism"])
    meth = compile_patterns(cfg["methodology"])
    ir_strong = [re.compile(p, re.I) for p in cfg["discusses_internal_representations"]["strong"]]
    ir_ctx = [re.compile(p, re.I) for p in cfg["discusses_internal_representations"]["safety_context"]]
    sc_yes = [re.compile(p, re.I) for p in cfg["discusses_schema_coherence"]["yes"]]
    sc_rel = [re.compile(p, re.I) for p in cfg["discusses_schema_coherence"]["related"]]
    lim_yes = [re.compile(p, re.I) for p in cfg["limitations_stated"]["yes"]]
    lim_part = [re.compile(p, re.I) for p in cfg["limitations_stated"]["partial"]]

    inc = {r["study_id"]: r for r in
           csv.DictReader(open(INCLUDED_CSV, newline="", encoding="utf-8"))}
    pmap = {r["study_id"]: r["pdf_file"] for r in
            csv.DictReader(open(PDF_MAP_CSV, newline="", encoding="utf-8"))}
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    fields = list(rows[0].keys()) if rows else []

    n_ev = {"full-text": 0, "abstract": 0, "metadata": 0}
    for r in rows:
        basis = r["evidence_basis"]
        pdf = pmap.get(r["paper_id"], "")
        abstract = inc.get(r["paper_id"], {}).get("abstract") or ""
        text = evidence_text(basis, pdf, abstract)
        # publication_type is a paper-level judgment — classify from the
        # abstract (or the first ~2k chars of full text when no abstract).
        pub_text = abstract if len(abstract) > MIN_ABS_CHARS else text[:2000]
        # metadata-basis papers have no body evidence — the title itself is
        # evidence; classify subdomains from it to avoid wholesale empties.
        if basis == "metadata" or not text.strip():
            text = text + " " + r["title"]
        n_ev[basis] += 1

        pubs = classify_pubtype(r["title"], pub_text, pt)
        subs = classify_multi(text, sub)
        ffs = classify_multi(text, ff)
        mfs = classify_multi(text, mf)
        # "none" only when no bucket hit
        r["publication_type"] = pubs
        r["subdomains"] = "; ".join(subs) if subs else ""
        r["formal_framework"] = "; ".join(ffs) if ffs else "none"
        r["mathematical_formalism"] = "; ".join(mfs) if mfs else "none"
        r["methodology"] = classify_single_best(text, meth) if pubs == "empirical" else "not_applicable"
        r["discusses_internal_representations"] = trinary(text, ir_strong, [], ir_ctx)
        r["discusses_schema_coherence"] = (
            "yes" if hit_counts(text, sc_yes) > 0 else
            "related concept" if hit_counts(text, sc_rel) > 0 else "no")
        r["limitations_stated"] = (
            "yes" if hit_counts(text, lim_yes) > 0 else
            "partially" if hit_counts(text, lim_part) > 0 else "no")

        note = r["notes"] or ""
        if (basis == "metadata" or not text.strip()) and "low-evidence" not in note:
            note = (note + " | low-evidence: metadata-only").strip()
        r["notes"] = note

    with open(CHARTED_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"heuristic extraction applied to {len(rows)} rows")
    print(f"evidence: {n_ev}")


if __name__ == "__main__":
    sys.exit(main())
