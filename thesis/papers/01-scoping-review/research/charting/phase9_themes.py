#!/usr/bin/env python3
"""
Paper 01 — Phase 9 (Task 9.2): scripted theme-extraction support.

Stage 1 (run before open coding): tokenize key_contribution across the full
corpus and per subdomain cluster; emit term/bigram frequencies to
charting/theme-keywords.md as raw material for open coding.

Stage 2 (after open coding; THEMES populated with keyword rules): compute
per-theme membership (papers matching any rule over the charted text fields),
theme x quality-tier cross-tab (quality-scores.csv), theme x year series,
and cross-cutting status. Emits charting/theme-stats.md.

Operationalization (Phase A): corpus = charted fields key_contribution,
relevance_justification, open_questions, subdomains; single-coder method;
83.4% key_contribution fill disclosed.
"""

from __future__ import annotations

import os
import re
import sys
from collections import Counter
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl-cfg")

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
QUALITY_CSV = BASE / "research" / "quality-scores-unique.csv"
KEYWORDS_MD = BASE / "research" / "charting" / "theme-keywords.md"
STATS_MD = BASE / "research" / "charting" / "theme-stats.md"
FIG_DIR = BASE / "research" / "charting" / "figures"

STOP = set("""a an and are as at be by for from in is it of on or that the to was
with this these those their its which who whom whose what when where why how
not no nor but yet so if then than too very can will just should would could
may might must shall has have had having been being does did doing paper
papers study studies review surveys survey article articles work works we our
us i you he she they them his her their our ourself myself themselves
systematic scoping using use used based focus focused focusing aim aims
present presents propose proposes propose provide provides providing address
addresses addressing examine examines examining explore explores exploring
investigate investigates investigating analyze analyses analyze assess
assesses assessing discuss discusses discussing highlight highlights
highlighting argue argues arguing suggest suggests suggesting find finds
finding findings result results show shows showing demonstrate demonstrates
demonstrating evidence empirical theoretical conceptual overview
introduction conclusion background methods results discussion analysis
analyses abstract full text literature large""".split())

TEXT_FIELDS = ("key_contribution", "relevance_justification", "open_questions")

# Filled after open coding (Stage 2). Each theme: label -> keyword rules.
# Single words are matched as token prefixes; phrases as substrings over the
# lowercased charted text. Cross-cutting status is computed from data
# (spans >= 3 subdomains), not hardcoded.
THEMES: dict[str, list[str]] = {
    "Proxy reward & reward hacking": [
        "reward hack", "reward hacking", "specification gaming", "proxy reward",
        "reward model", "reward models", "proxy objective", "reward overoptimization",
        "reward misspecif"],
    "Deceptive alignment & sycophancy": [
        "deceptive alignment", "deception", "decept", "sycophancy", "machiavellian",
        "betrayal", "ulterior"],
    "Preference & value learning (RLHF/DPO)": [
        "rlhf", "reinforcement learning from human feedback", "preference learning",
        "preference optimization", "human feedback", "dpo", "constitutional ai",
        "preference-based", "preference data"],
    "Evaluation, benchmarks & measurement": [
        "benchmark", "benchmarks", "evaluation", "evaluat", "metric", "metrics",
        "measurement", "test item", "test suite", "assess"],
    "Interpretability & mechanistic analysis": [
        "interpretab", "mechanistic", "circuit", "probing", "monosemantic",
        "feature attribution", "sparse autoencoder", "neuron"],
    "Internal representation structure & schema": [
        "internal representation", "representation structure", "representation engineering",
        "schema", "latent", "world model", "model internals", "activation",
        "representational"],
    "Robustness, security & adversarial": [
        "robust", "adversarial", "attack", "defense", "defence", "jailbreak",
        "poisoning", "backdoor", "prompt injection", "security"],
    "Governance, incentives & sociotechnical": [
        "governance", "regulation", "regulatory", "oversight", "incentive",
        "principal-agent", "sociotechnical", "audit", "accountability", "legislation"],
    "Ethics, fairness & human values": [
        "moral", "ethic", "fairness", "bias", "human values", "rights",
        "beneficence", "responsibility", "society"],
    "Capabilities, control & existential risk": [
        "control problem", "existential risk", "superintelligence", "x-risk",
        "catastrophic", "misalignment", "alignment problem", "agi", "corrigibility"],
    "Formal methods & mathematical theory": [
        "formal", "theorem", "proof", "axiom", "axiomatic", "bayesian",
        "mathematical", "probability", "decision theory", "game theory",
        "dynamical systems", "optimization theory"],
    "Human-AI interaction & collaborative alignment": [
        "human-ai", "human-robot", "human-machine", "human in the loop",
        "joint reasoning", "collaboration", "interactive", "human-ai alignment"],
    "Compositional generalization & sigma-trap": [
        "compositional generalization", "sigma trap", "sigma-trap", "σ-trap",
        "compositional", "systematic generalization", "schema coherence"],
}


def load() -> tuple[list[dict], dict[str, dict]]:
    rows = []
    with open(CHARTED_CSV, newline="", encoding="utf-8") as fh:
        import csv
        for r in csv.DictReader(fh):
            rows.append(r)
    qual = {}
    with open(QUALITY_CSV, newline="", encoding="utf-8") as fh:
        import csv
        for r in csv.DictReader(fh):
            qual[r["paper_id"]] = r
    return rows, qual


def stage1(rows: list[dict]) -> None:
    overall = Counter()
    per_sub: dict[str, Counter] = {}
    for r in rows:
        toks: list[str] = []
        for f in TEXT_FIELDS:
            toks += tokenize(r.get(f) or "")
        overall.update(toks)
        subs = [s.strip() for s in (r.get("subdomains") or "").split(";") if s.strip()]
        for s in subs:
            per_sub.setdefault(s, Counter()).update(toks)

    lines = ["# Theme extraction raw material — Paper 01 Phase 9 (9.2)",
             "",
             f"Corpus: `key_contribution`, `relevance_justification`, `open_questions` "
             f"of {len(rows)} papers. Single-coder method; 83.4% key_contribution fill.",
             "",
             "## Top unigrams (overall)",
             "",
             "| term | n |\n|---|---|"]
    for t, n in overall.most_common(40):
        lines.append(f"| {t} | {n} |")
    lines.append("\n## Top bigrams (overall)\n\n| term | n |\n|---|---|")
    bg = Counter()
    for r in rows:
        toks = []
        for f in TEXT_FIELDS:
            toks += tokenize(r.get(f) or "")
        bg.update(bigrams(toks))
    for t, n in bg.most_common(40):
        lines.append(f"| {t} | {n} |")
    for s in sorted(per_sub):
        lines.append(f"\n## Top unigrams — {s}\n\n| term | n |\n|---|---|")
        for t, n in per_sub[s].most_common(20):
            lines.append(f"| {t} | {n} |")
    with open(KEYWORDS_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"theme-keywords written: {KEYWORDS_MD.name}")


def paper_text(r: dict) -> str:
    return " ".join((r.get(f) or "") for f in TEXT_FIELDS).lower()


def tokenize(text: str) -> list[str]:
    text = text.lower()
    toks = re.findall(r"[a-z][a-z0-9\-]{2,}", text)
    return [t for t in toks if t not in STOP]


def bigrams(tokens: list[str]) -> list[str]:
    return [f"{a} {b}" for a, b in zip(tokens, tokens[1:]) if len(a) > 2 and len(b) > 2]


def match_theme(text: str, kws: list[str]) -> bool:
    """Single words match as token prefixes; phrases as substrings."""
    tokens = re.findall(r"[a-z0-9-]+", text)
    for kw in kws:
        if " " in kw:
            if kw in text:
                return True
        elif any(t.startswith(kw) for t in tokens):
            return True
    return False


def stage2(rows: list[dict], qual: dict[str, dict]) -> None:
    if not THEMES:
        print("THEMES not populated — run open coding first (edit script).")
        return
    n = len(rows)
    out = ["# Theme statistics — Paper 01 Phase 9 (9.2.2-9.2.5)",
           "",
           f"Themes operationalized as keyword rules over charted text fields "
           f"({', '.join(TEXT_FIELDS)}); membership = any keyword hit. "
           f"Total papers: {n}.",
           "",
           "| Theme | cross-cutting | papers | % of 1136 | tier A | tier B | "
           "tier C | tier D/E | low-cred |",
           "|---|---|---|---|---|---|---|---|---|"]
    rows_by_id = {r["paper_id"]: r for r in rows}
    theme_members: dict[str, list[str]] = {}
    theme_subs: dict[str, Counter] = {}
    for label, kws in THEMES.items():
        members = [r["paper_id"] for r in rows if match_theme(paper_text(r), kws)]
        theme_members[label] = members
        subs = Counter()
        for pid in members:
            r = rows_by_id[pid]
            for s in (r.get("subdomains") or "").split(";"):
                s = s.strip()
                if s:
                    subs[s] += 1
        theme_subs[label] = subs
    out = ["# Theme statistics — Paper 01 Phase 9 (9.2.2-9.2.5)",
           "",
           f"Themes operationalized as keyword rules over charted text fields "
           f"({', '.join(TEXT_FIELDS)}); membership = any keyword hit. "
           f"Single words are token-prefix matches, phrases are substring matches. "
           f"Total papers: {n}.",
           "",
           "| Theme | cross-cutting | papers | % of 1136 | tier A | tier B | "
           "tier C | tier D/E | low-cred |",
           "|---|---|---|---|---|---|---|---|---|"]
    for label, members in theme_members.items():
        n_sub = sum(1 for v in theme_subs[label].values() if v >= 1)
        cc = "yes" if n_sub >= 3 else "no"
        t = Counter(qual.get(pid, {}).get("tier", "?") for pid in members)
        lowcred = sum(1 for pid in members
                      if qual.get(pid, {}).get("low_credibility", "").strip() == "1")
        out.append(
            f"| {label} | {cc} | {len(members)} | "
            f"{len(members) / n * 100:.1f}% | {t.get('A', 0)} | {t.get('B', 0)} | "
            f"{t.get('C', 0)} | {t.get('D', 0) + t.get('E', 0)} | {lowcred} |")
    out.append("\n## Theme x year (papers)\n\n| Theme | " + " | ".join(
        str(y) for y in range(2015, 2027)) + " |\n|---|" + "---|" * 12 + "|")
    for label, members in theme_members.items():
        yc = Counter()
        for pid in members:
            r = rows_by_id[pid]
            y = r.get("year") or ""
            if y.isdigit():
                yc[int(y)] += 1
        out.append(f"| {label} | " + " | ".join(
            str(yc.get(y, 0)) for y in range(2015, 2027)) + " |")
    out.append("\n## Theme membership overlap (Jaccard, top pairs)")
    out.append("\n| pair | Jaccard |\n|---|---|")
    pairs = []
    labels = list(THEMES)
    for i, a in enumerate(labels):
        sa = set(theme_members[a])
        for b in labels[i + 1:]:
            sb = set(theme_members[b])
            j = len(sa & sb) / len(sa | sb) if sa | sb else 0.0
            pairs.append((f"{a} / {b}", j))
    for name, j in sorted(pairs, key=lambda x: -x[1])[:12]:
        out.append(f"| {name} | {j:.3f} |")
    with open(STATS_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"theme-stats written: {STATS_MD.name}")
    # theme x year figure
    FIG_DIR.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 5))
    for i, (label, members) in enumerate(theme_members.items()):
        yc = Counter()
        for pid in members:
            y = (rows_by_id[pid].get("year") or "")
            if y.isdigit():
                yc[int(y)] += 1
        ax.plot(range(2015, 2027), [yc.get(y, 0) for y in range(2015, 2027)],
                marker="o", ms=2.5, label=label)
    ax.set_xlabel("year")
    ax.set_ylabel("papers")
    ax.set_title("Thematic focus over time (keyword-rule membership)")
    ax.legend(fontsize=6.5, ncol=2)
    fig.tight_layout()
    for ext in ("png", "pdf", "svg"):
        fig.savefig(FIG_DIR / f"phase9-themes-year.{ext}", dpi=150, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    rows, qual = load()
    stage1(rows)
    stage2(rows, qual)
    return 0


if __name__ == "__main__":
    sys.exit(main())
