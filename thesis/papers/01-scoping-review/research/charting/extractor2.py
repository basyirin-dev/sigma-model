#!/usr/bin/env python3
"""
Paper 01 — Phase 7: INDEPENDENT second-pass extractor (Task 7.3.1, CC.1.6).

A deliberately separate implementation from heuristic.py: own keyword
tables, own decision rules, no shared config import. Re-extracts the [†]
categorical fields for the validation sample papers, using the same
evidence text (abstract + full-text excerpt) but an independent judgment.

Independence properties vs heuristic.py:
  - different keywords (mostly negation-based / distinct phrasings)
  - title+abstract only (no body-text scanning for pubtype)
  - different decision thresholds and tie-breaks

Output: research/charting/validation-extractor2.csv
"""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
PDF_MAP_CSV = BASE / "research" / "charting" / "pdf-map.csv"
PDF_DIR = BASE / "research" / "pdfs"
SAMPLE_CSV = BASE / "research" / "charting" / "validation-sample.csv"
OUT_CSV = BASE / "research" / "charting" / "validation-extractor2.csv"


def _pats(*words: str) -> list[re.Pattern]:
    return [re.compile(rf"\b{re.escape(w)}", re.I) for w in words]


def pubtype(title: str, text: str) -> str:
    tl = title.lower()
    if any(w in tl for w in ("survey", "review", "overview", "state of the art")):
        return "review"
    if re.search(r"\bwe (evaluat|test|train|run|conduct|measure|compare)\b", text) or \
       re.search(r"\b(empirical|experiment|benchmark|dataset)\w*\b", text):
        return "empirical"
    if re.search(r"\b(theorem|proof|formal model|axiom)\w*\b", text):
        return "theoretical"
    if re.search(r"\bwe argue|we contend|position paper|this paper argues\b", text):
        return "position"
    if re.search(r"\b(opinion|commentary|viewpoint|editorial)\b", text):
        return "opinion"
    return "other"


def subdomains(text: str) -> list[str]:
    hits: list[str] = []
    rules = [
        ("value alignment", r"align\w*|corrigib\w*|rlhf|reward (model|hack)|preference"),
        ("interpretability", r"interpretab\w*|explainab\w*|mechanistic|circuit\w*|transparen\w*"),
        ("robustness", r"robust\w*|adversarial|out.of.distribution|distributional shift|verification"),
        ("mesa-optimization", r"mesa\w*|deceptive align\w*|deception|learned optimiz"),
        ("governance", r"govern\w*|regulat\w*|oversight|policymakers?|audit\w*"),
        ("ethics", r"ethic\w*|moral\w*|fairness|bias|human rights|value pluralism"),
        ("capabilities", r"capabilit\w*|power.seeking|existential risk|superintell\w*|x.risk"),
    ]
    for name, pat in rules:
        if re.search(pat, text, re.I):
            hits.append(name)
    return hits


def formal_framework(text: str) -> list[str]:
    hits = []
    if re.search(r"game.theor\w*|equilibri\w*|nash|bargain\w*|payoff\w*", text, re.I):
        hits.append("game theory")
    if re.search(r"decision.theor\w*|expected utility|utility function|preference order", text, re.I):
        hits.append("decision theory")
    if re.search(r"dynamical system\w*|differential equation\w*|attractor\w*|bifurcation", text, re.I):
        hits.append("dynamical systems")
    if re.search(r"information.theor\w*|entropy|mutual information|shannon", text, re.I):
        hits.append("information theory")
    if not hits and re.search(r"formal\w*|mathematical (framework|model)|axiom", text, re.I):
        hits.append("other")
    return hits if hits else ["none"]


def math_formalism(text: str) -> list[str]:
    hits = []
    if re.search(r"differential equation|ODE\b|PDE\b", text, re.I):
        hits.append("ODEs")
    if re.search(r"probabil\w*|bayes\w*|stochastic|distribution", text, re.I):
        hits.append("probability")
    if re.search(r"\blogic\b|logical|propositional|first.order|theorem", text, re.I):
        hits.append("logic")
    if re.search(r"optimiz\w*|gradient|objective|loss function|reward function", text, re.I):
        hits.append("optimization")
    return hits if hits else ["none"]


def methodology(text: str, is_empirical: bool) -> str:
    if not is_empirical:
        return "not_applicable"
    if re.search(r"simulat\w*|agent.based|gridworld|environments?|seeds?", text, re.I):
        return "simulation"
    if re.search(r"case stud\w*", text, re.I):
        return "case study"
    if re.search(r"experiment\w*|user stud\w*|controlled|survey|questionnaire", text, re.I):
        return "experiment"
    if re.search(r"theoretical|conceptual|formal", text, re.I):
        return "theory"
    if re.search(r"analyz\w*|observational|regression|correlation", text, re.I):
        return "analysis"
    return "not_applicable"


def internal_reps(text: str) -> str:
    strong = re.search(r"internal representation\w*|latent (representation|space)|feature geometry|circuit\w*|embeddings?|activations?", text, re.I)
    if not strong:
        return "no"
    if re.search(r"safet\w*|align\w*|risk|failure|decept", text, re.I):
        return "yes"
    return "implicitly"


def schema_coherence(text: str) -> str:
    if re.search(r"schema coherence|sigma coherence|coherence of.*representation", text, re.I):
        return "yes"
    if re.search(r"compositional\w*|disentangl\w*|latent ontology|feature geometry|abstraction hierarch", text, re.I):
        return "related concept"
    return "no"


def limitations(text: str) -> str:
    if re.search(r"(limitation\w*|acknowledge|caveat\w*)", text, re.I) or \
       re.search(r"not (generaliz\w*|applicable|complete)|does not (address|cover)", text, re.I):
        return "yes"
    if re.search(r"future (work|research)|open (question|problem)|remains (an )?open", text, re.I):
        return "partially"
    return "no"


def evidence_text(pdf: str, abstract: str) -> str:
    if pdf:
        try:
            out = subprocess.run(["pdftotext", "-f", "1", "-l", "3", str(PDF_DIR / pdf), "-"],
                                 capture_output=True, text=True, timeout=45)
            txt = out.stdout or ""
            if txt.strip():
                return txt[:8000]
        except Exception:
            pass
    return (abstract or "")[:3000]


def main() -> None:
    inc = {r["study_id"]: r for r in
           csv.DictReader(open(INCLUDED_CSV, newline="", encoding="utf-8"))}
    pmap = {r["study_id"]: r["pdf_file"] for r in
            csv.DictReader(open(PDF_MAP_CSV, newline="", encoding="utf-8"))}
    sample = [r["paper_id"] for r in csv.DictReader(open(SAMPLE_CSV, newline="", encoding="utf-8"))]
    charted = {r["paper_id"]: r for r in
               csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8"))}

    out_rows = []
    for pid in sorted(sample):
        c = charted[pid]
        abstract = inc.get(pid, {}).get("abstract") or ""
        text = evidence_text(pmap.get(pid, ""), abstract)
        pub = pubtype(c["title"], abstract or text[:2000])
        out_rows.append({
            "paper_id": pid,
            "publication_type": pub,
            "subdomains": "; ".join(subdomains(text)),
            "formal_framework": "; ".join(formal_framework(text)),
            "mathematical_formalism": "; ".join(math_formalism(text)),
            "methodology": methodology(text, pub == "empirical"),
            "discusses_internal_representations": internal_reps(text),
            "discusses_schema_coherence": schema_coherence(text),
            "limitations_stated": limitations(text),
        })

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)
    print(f"extractor2 ran on {len(out_rows)} sample papers -> {OUT_CSV.name}")


if __name__ == "__main__":
    sys.exit(main())
