#!/usr/bin/env python3
"""
Paper 01 — Phase 9 (Task 9.1): descriptive numerical summary supplement.

Extends the Phase 7 summary (summary.py) with the analyses required by
9.1.1-9.1.5 that were not already computed:
  - venue distribution (normalized) + venue category
  - subdomain x year time series
  - conditional subdomain co-occurrence matrix
  - methodology x subdomain cross-tab
  - formal vs conceptual breakdown (formal = formal_framework != none OR
    mathematical_formalism != none), overall, by year, by subdomain
  - geographic distribution via curated venue-country proxy
    (documented in venue-country-map.md)

Input : research/charting/charted-data.csv (working copy, canonical)
Output: research/charting/phase9-summary.md
        research/charting/venue-country-map.md (proxy documentation)
        research/charting/figures/phase9-*.{png,pdf,svg} (publication-ready)
        summary-statistics.md <- appended "Phase 9 supplement" pointer

Operationalizations (locked in Phase A, see phases/09_thematic_synthesis.md):
  - missing year (14 rows): excluded from time series, reported separately
  - geography: venue-country proxy; arXiv/global and unassigned buckets
    disclosed; no per-paper affiliation coding this run
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl-cfg")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
OUT_MD = BASE / "research" / "charting" / "phase9-summary.md"
COUNTRY_MD = BASE / "research" / "charting" / "venue-country-map.md"
SUMMARY_MD = BASE / "research" / "charting" / "summary-statistics.md"
FIG_DIR = BASE / "research" / "charting" / "figures"

SUBDOMAINS = [
    "value alignment",
    "ethics",
    "robustness",
    "capabilities",
    "interpretability",
    "governance",
    "mesa-optimization",
    "other",
]

# Normalized venue aliases (exact/startswith rules applied in order).
VENUE_ALIASES: list[tuple[str, str]] = [
    ("arxiv preprint", "arXiv"),
    ("arxiv", "arXiv"),
    ("corr", "arXiv"),
    ("aaai", "AAAI"),
    ("aies", "AIES (AAAI/ACM)"),
    ("aies 2018", "AIES (AAAI/ACM)"),
    ("aies 2020", "AIES (AAAI/ACM)"),
    ("aies 2021", "AIES (AAAI/ACM)"),
    ("aies 2023", "AIES (AAAI/ACM)"),
    ("advances in neural information processing", "NeurIPS"),
    ("iclr", "ICLR"),
    ("learning representations", "ICLR"),
    ("proceedings of machine learning research", "PMLR"),
    ("lecture notes in computer science", "LNCS (Springer)"),
    ("lecture notes in networks and systems", "LNNS (Springer)"),
    ("communications in computer and information science", "CCIS (Springer)"),
    ("proceedings of the annual meeting of the association for computational linguistics",
     "ACL"),
    ("association for computational linguistics", "ACL"),
    ("emnlp", "EMNLP"),
    ("naacl", "NAACL"),
    ("eacl", "EACL"),
    ("coling", "COLING"),
    ("aamas", "AAMAS"),
    ("ceur workshop", "CEUR Workshop Proceedings"),
    ("human factors in computing systems", "ACM CHI"),
    ("international joint conference on neural networks", "IJCNN"),
    ("ieee", "IEEE venues"),
    ("acm international conference proceeding", "ACM venues"),
    ("acm/ieee", "ACM/IEEE venues"),
    ("proceedings of the acm web conference", "ACM WWW"),
    ("acm sigkdd", "ACM KDD"),
    ("ijcai", "IJCAI"),
    ("international joint conference on artificial intelligence", "IJCAI"),
    ("icassp", "IEEE venues"),
    ("ai magazine", "AI Magazine"),
    ("ai alignment forum", "AI Alignment Forum"),
    ("journal of artificial intelligence research", "JAIR"),
    ("transactions on machine learning research", "TMLR"),
    ("scientific reports", "Scientific Reports"),
    ("philosophical studies", "Philosophical Studies"),
    ("philosophy and technology", "Philosophy and Technology"),
    ("minds and machines", "Minds and Machines"),
    ("synthese", "Synthese"),
    ("ai and society", "AI and Society"),
    ("ai and ethics", "AI and Ethics"),
    ("ai ethics", "AI and Ethics"),
    ("ethics and information technology", "Ethics and Information Technology"),
    ("ethics of artificial intelligence", "Ethics of AI (book)"),
    ("contemporary debates in the ethics of artificial intelligence",
     "Contemporary Debates in the Ethics of AI (book)"),
    ("frontiers in artificial intelligence and applications",
     "Frontiers in AI and Applications (IOS Press)"),
    ("frontiers in artificial intelligence", "Frontiers in AI"),
    ("frontiers in psychology", "Frontiers in Psychology"),
    ("studies in applied philosophy, epistemolog", "SAPERE (Springer)"),
    ("law, governance and technology series", "Law, Governance and Technology (Springer)"),
    ("big data and cognitive computing", "Big Data and Cognitive Computing (MDPI)"),
    ("informatica", "Informatica (Slovenia)"),
    ("ieee access", "IEEE Access"),
    ("ieee spectrum", "IEEE Spectrum"),
    ("applied human factors and ergonomics", "AHFE"),
    ("blockchain computing and applications", "IEEE BCCA"),
    ("undefined", "undefined"),
]

# Venue -> country (publisher/association HQ basis; see venue-country-map.md).
VENUE_COUNTRY: dict[str, str] = {
    "arXiv": "global (arXiv)",
    "AAAI": "US",
    "AIES (AAAI/ACM)": "US",
    "NeurIPS": "US",
    "ICLR": "US",
    "PMLR": "US",
    "LNCS (Springer)": "DE (Springer Nature)",
    "LNNS (Springer)": "DE (Springer Nature)",
    "CCIS (Springer)": "DE (Springer Nature)",
    "ACL": "US",
    "EMNLP": "US",
    "NAACL": "US",
    "EACL": "EU (ACL chapter)",
    "COLING": "international",
    "AAMAS": "international",
    "CEUR Workshop Proceedings": "DE (CEUR-WS)",
    "ACM CHI": "US",
    "IJCNN": "US (IEEE)",
    "IEEE venues": "US (IEEE)",
    "ACM venues": "US (ACM)",
    "ACM/IEEE venues": "US",
    "ACM WWW": "US",
    "ACM KDD": "US",
    "IJCAI": "international",
    "AI Magazine": "US",
    "AI Alignment Forum": "grey (AAF)",
    "JAIR": "US",
    "TMLR": "international",
    "Scientific Reports": "DE (Springer Nature)",
    "Philosophical Studies": "DE (Springer Nature)",
    "Philosophy and Technology": "DE (Springer Nature)",
    "Minds and Machines": "DE (Springer Nature)",
    "Synthese": "DE (Springer Nature)",
    "AI and Society": "DE (Springer Nature)",
    "AI and Ethics": "DE (Springer Nature)",
    "Ethics and Information Technology": "DE (Springer Nature)",
    "Ethics of AI (book)": "UK (OUP)",
    "Contemporary Debates in the Ethics of AI (book)": "UK (OUP)",
    "Frontiers in AI and Applications (IOS Press)": "NL (IOS Press)",
    "Frontiers in AI": "CH (Frontiers)",
    "Frontiers in Psychology": "CH (Frontiers)",
    "SAPERE (Springer)": "DE (Springer Nature)",
    "Law, Governance and Technology (Springer)": "DE (Springer Nature)",
    "Big Data and Cognitive Computing (MDPI)": "CH (MDPI)",
    "Informatica (Slovenia)": "SI",
    "IEEE Access": "US (IEEE)",
    "IEEE Spectrum": "US (IEEE)",
    "AHFE": "international",
    "IEEE BCCA": "US (IEEE)",
    "undefined": "unassigned",
}

VENUE_CATEGORY: dict[str, str] = {
    "arXiv": "preprint",
    "AAAI": "conference",
    "AIES (AAAI/ACM)": "conference",
    "NeurIPS": "conference",
    "ICLR": "conference",
    "PMLR": "conference",
    "LNCS (Springer)": "proceedings",
    "LNNS (Springer)": "proceedings",
    "CCIS (Springer)": "proceedings",
    "ACL": "conference",
    "EMNLP": "conference",
    "NAACL": "conference",
    "EACL": "conference",
    "COLING": "conference",
    "AAMAS": "conference",
    "CEUR Workshop Proceedings": "workshop",
    "ACM CHI": "conference",
    "IJCNN": "conference",
    "IEEE venues": "conference",
    "ACM venues": "conference",
    "ACM/IEEE venues": "conference",
    "ACM WWW": "conference",
    "ACM KDD": "conference",
    "IJCAI": "conference",
    "AI Magazine": "journal",
    "AI Alignment Forum": "grey literature",
    "JAIR": "journal",
    "TMLR": "journal",
    "Scientific Reports": "journal",
    "Philosophical Studies": "journal",
    "Philosophy and Technology": "journal",
    "Minds and Machines": "journal",
    "Synthese": "journal",
    "AI and Society": "journal",
    "AI and Ethics": "journal",
    "Ethics and Information Technology": "journal",
    "Ethics of AI (book)": "book",
    "Contemporary Debates in the Ethics of AI (book)": "book",
    "Frontiers in AI and Applications (IOS Press)": "proceedings",
    "Frontiers in AI": "journal",
    "Frontiers in Psychology": "journal",
    "SAPERE (Springer)": "book",
    "Law, Governance and Technology (Springer)": "book",
    "Big Data and Cognitive Computing (MDPI)": "journal",
    "Informatica (Slovenia)": "journal",
    "IEEE Access": "journal",
    "IEEE Spectrum": "magazine",
    "AHFE": "conference",
    "IEEE BCCA": "conference",
    "undefined": "unassigned",
}

COLORS = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3", "#937860",
          "#DA8BC3", "#8C8C8C"]


def normalize_venue(v: str) -> str:
    v = (v or "").strip().lower()
    if not v:
        return "unassigned"
    for alias, norm in VENUE_ALIASES:
        if v.startswith(alias):
            return norm
    return "Other venue"


def save_fig(fig, stem: str) -> None:
    for ext in ("png", "pdf", "svg"):
        fig.savefig(FIG_DIR / f"{stem}.{ext}", dpi=150, bbox_inches="tight")


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out) + "\n"


def main() -> int:
    FIG_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(CHARTED_CSV, dtype=str)
    df = df.fillna("")
    n = len(df)

    # --- venue normalization ------------------------------------------------
    df["venue_norm"] = df["venue"].map(normalize_venue)
    vc = df["venue_norm"].value_counts()
    top_venues = [v for v in vc.index
                  if v not in ("Other venue", "unassigned") and vc[v] >= 3]
    other_n = int(vc.sum() - sum(vc[t] for t in top_venues))
    venue_rows = [[v, int(vc[v])] for v in top_venues] + [["Other venue", other_n]]
    venue_rows.sort(key=lambda r: -r[1])

    cat = df["venue_norm"].map(lambda v: VENUE_CATEGORY.get(v, "other"))
    cat_rows = [[k, int(v)] for k, v in cat.value_counts().items()]

    # --- subdomain x year ---------------------------------------------------
    years_all = pd.to_numeric(df["year"], errors="coerce")
    has_year = years_all.notna()
    df["year_i"] = years_all.astype("Int64")
    year_range = sorted(y for y in df.loc[has_year, "year_i"].unique() if pd.notna(y))

    sub_year = {}
    for s in SUBDOMAINS:
        mask = df["subdomains"].str.split(";").map(lambda xs: s in [x.strip() for x in xs])
        sub_year[s] = {int(y): int((mask & (df["year_i"] == y)).sum()) for y in year_range}

    # --- subdomain co-occurrence (conditional) ------------------------------
    sub_sets = {
        s: set(df.loc[df["subdomains"].str.split(";").map(
            lambda xs: s in [x.strip() for x in xs]), "paper_id"])
        for s in SUBDOMAINS
    }
    cooc = pd.DataFrame(0, index=SUBDOMAINS, columns=SUBDOMAINS)
    for a in SUBDOMAINS:
        for b in SUBDOMAINS:
            if a == b:
                cooc.loc[a, b] = len(sub_sets[a])
            else:
                cooc.loc[a, b] = len(sub_sets[a] & sub_sets[b])
    cond = cooc.div(cooc.values.diagonal().astype(float), axis=0).round(3)
    pair_rows = []
    for a in SUBDOMAINS:
        for b in SUBDOMAINS:
            if a < b and cooc.loc[a, b] > 0:
                denom = min(len(sub_sets[a]), len(sub_sets[b]))
                pair_rows.append(
                    [f"{a} + {b}", int(cooc.loc[a, b]),
                     f"{cooc.loc[a, b] / denom * 100:.1f}%"])
    pair_rows.sort(key=lambda r: -float(r[2].rstrip("%")))

    # --- methodology x subdomain --------------------------------------------
    meth_sub = pd.DataFrame(0, index=df["methodology"].value_counts().index,
                            columns=SUBDOMAINS)
    for _, r in df.iterrows():
        subs = [s.strip() for s in (r["subdomains"] or "").split(";") if s.strip()]
        m = r["methodology"] or "missing"
        for s in subs:
            if s in meth_sub.columns:
                meth_sub.loc[m, s] += 1

    # --- formal vs conceptual ------------------------------------------------
    def is_formal(r: pd.Series) -> bool:
        ff = (r["formal_framework"] or "").strip().lower()
        mf = (r["mathematical_formalism"] or "").strip().lower()
        return ff not in ("", "none", "nan") or mf not in ("", "none", "nan")

    df["formal"] = df.apply(is_formal, axis=1)
    n_formal = int(df["formal"].sum())
    n_conceptual = n - n_formal
    formal_year = {
        int(y): [int((df["formal"] & (df["year_i"] == y)).sum()),
                 int(((~df["formal"]) & (df["year_i"] == y)).sum())]
        for y in year_range
    }
    formal_sub = {}
    for s in SUBDOMAINS:
        mask = df["subdomains"].str.split(";").map(lambda xs: s in [x.strip() for x in xs])
        formal_sub[s] = [int((mask & df["formal"]).sum()), int((mask & ~df["formal"]).sum())]

    # --- geography -----------------------------------------------------------
    df["country"] = df["venue_norm"].map(lambda v: VENUE_COUNTRY.get(v, "unassigned"))
    geo_rows = [[k, int(v)] for k, v in df["country"].value_counts().items()]

    # =========================================================================
    # Figures
    # =========================================================================
    # 1. venue distribution (horizontal bar)
    fig, ax = plt.subplots(figsize=(9, 5))
    labs = [v if len(v) < 34 else v[:31] + "..." for v, _ in venue_rows[:15]]
    ax.barh(range(len(venue_rows[:15])), [v for _, v in venue_rows[:15]],
            color=COLORS[0])
    ax.set_yticks(range(len(labs)))
    ax.set_yticklabels(labs, fontsize=8)
    ax.set_xlabel("papers")
    ax.set_title("Venue distribution (normalized, top 15 + Other)")
    fig.tight_layout()
    save_fig(fig, "phase9-venue-distribution")
    plt.close(fig)

    # 2. subdomain x year (lines)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for i, s in enumerate(SUBDOMAINS):
        ax.plot(year_range, [sub_year[s][y] for y in year_range], marker="o", ms=3,
                label=s, color=COLORS[i % len(COLORS)])
    ax.set_xlabel("year")
    ax.set_ylabel("papers")
    ax.set_title("AGI safety subdomain focus over time (multi-select)")
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    save_fig(fig, "phase9-subdomains-year")
    plt.close(fig)

    # 3. conditional co-occurrence heatmap
    fig, ax = plt.subplots(figsize=(8.5, 7))
    data = cond.to_numpy(dtype=float)
    im = ax.imshow(data, cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(len(SUBDOMAINS)))
    ax.set_xticklabels([s.replace("value alignment", "value\nalignment") for s in SUBDOMAINS],
                       fontsize=7)
    ax.set_yticks(range(len(SUBDOMAINS)))
    ax.set_yticklabels(SUBDOMAINS, fontsize=8)
    for i in range(len(SUBDOMAINS)):
        for j in range(len(SUBDOMAINS)):
            ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", fontsize=6)
    ax.set_title("P(subdomain B | subdomain A) among included papers")
    fig.colorbar(im, ax=ax, fraction=0.046)
    fig.tight_layout()
    save_fig(fig, "phase9-subdomain-cooccurrence")
    plt.close(fig)

    # 4. methodology x subdomain heatmap
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    mvals = meth_sub.to_numpy(dtype=float)
    im = ax.imshow(mvals, cmap="YlGnBu")
    ax.set_xticks(range(len(SUBDOMAINS)))
    ax.set_xticklabels([s.replace("value alignment", "value\nalignment") for s in SUBDOMAINS],
                       fontsize=7)
    ax.set_yticks(range(len(meth_sub.index)))
    ax.set_yticklabels(meth_sub.index, fontsize=8)
    for i in range(len(meth_sub.index)):
        for j in range(len(SUBDOMAINS)):
            v = int(mvals[i, j])
            if v:
                ax.text(j, i, str(v), ha="center", va="center", fontsize=6,
                        color="black")
    ax.set_title("Methodology x subdomain (papers)")
    fig.colorbar(im, ax=ax, fraction=0.046)
    fig.tight_layout()
    save_fig(fig, "phase9-methodology-subdomain")
    plt.close(fig)

    # 5. formal vs conceptual by year (stacked)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    fy = [formal_year[y][0] for y in year_range]
    cy = [formal_year[y][1] for y in year_range]
    ax.bar(year_range, fy, label="formal (framework or formalism)", color=COLORS[0])
    ax.bar(year_range, cy, bottom=fy, label="conceptual/qualitative", color=COLORS[1])
    ax.set_xlabel("year")
    ax.set_ylabel("papers")
    ax.set_title("Formal vs conceptual papers by year")
    ax.legend(fontsize=8)
    fig.tight_layout()
    save_fig(fig, "phase9-formal-conceptual-year")
    plt.close(fig)

    # 6. geography (bar)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    geo_sorted = sorted(geo_rows, key=lambda r: -r[1])
    ax.bar([g for g, _ in geo_sorted], [v for _, v in geo_sorted], color=COLORS[0])
    ax.set_xticklabels([g for g, _ in geo_sorted], rotation=35, ha="right", fontsize=7)
    ax.set_ylabel("papers")
    ax.set_title("Venue-country proxy (publisher/association HQ basis)")
    fig.tight_layout()
    save_fig(fig, "phase9-geography")
    plt.close(fig)

    # =========================================================================
    # Markdown outputs
    # =========================================================================
    lines = ["# Phase 9 summary supplement — Paper 01 (Task 9.1)",
             "",
             f"- **Total papers: {n}** (working copy `research/charting/charted-data.csv`)",
             "- Operationalizations: see `phases/09_thematic_synthesis.md` (Phase A).",
             "",
             "## 9.1.1a Venue distribution (normalized)",
             "",
             markdown_table(["Venue", "n"], venue_rows),
             "",
             "## 9.1.1b Venue category",
             "",
             markdown_table(["Category", "n"], cat_rows),
             "",
             "## 9.1.2a Subdomain x year (papers, multi-select)",
             "",
             markdown_table(["Subdomain", *[str(y) for y in year_range]],
                            [[s, *[str(sub_year[s][y]) for y in year_range]]
                             for s in SUBDOMAINS]),
             "",
             f"Note: {int((~has_year).sum())} papers with missing year excluded from the "
             "time series.",
             "",
             "## 9.1.2b Conditional subdomain co-occurrence (top pairs)",
             "",
             "P(A+B) = co-occurrence / min(count A, count B).",
             "",
             markdown_table(["Subdomain pair", "co-occur", "% of smaller"], pair_rows[:15]),
             "",
             "## 9.1.3a Methodology x subdomain (papers)",
             "",
             markdown_table(["Methodology", *SUBDOMAINS],
                            [[m, *[str(meth_sub.loc[m, s]) for s in SUBDOMAINS]]
                             for m in meth_sub.index]),
             "",
             "## 9.1.3b Formal vs conceptual (formal = formal_framework != none OR "
             "mathematical_formalism != none)",
             "",
             markdown_table(["Formality", "n", "%"],
                            [["formal", n_formal, f"{n_formal / n * 100:.1f}%"],
                             ["conceptual/qualitative", n_conceptual,
                              f"{n_conceptual / n * 100:.1f}%"],
                             ["by subdomain", "", ""]]),
             markdown_table(["Subdomain", "formal", "conceptual"],
                            [[s, str(formal_sub[s][0]), str(formal_sub[s][1])]
                             for s in SUBDOMAINS]),
             "",
             "## 9.1.1c Geographic distribution (venue-country proxy)",
             "",
             "Basis: publisher/association HQ country; see "
             "`venue-country-map.md` for the full mapping and limitations. "
             "Qualitative institutional narrative: Phase 0.5 "
             "`research/key-institutions.md`.",
             "",
             markdown_table(["Country / group", "n"], geo_rows),
             "",
             "## Figures",
             "",
             "Publication-ready figures (PNG preview + PDF + SVG):",
             "",
             "| Figure | File stem |",
             "|---|---|",
             "| Venue distribution | `figures/phase9-venue-distribution` |",
             "| Subdomain focus over time | `figures/phase9-subdomains-year` |",
             "| Conditional co-occurrence | `figures/phase9-subdomain-cooccurrence` |",
             "| Methodology x subdomain | `figures/phase9-methodology-subdomain` |",
             "| Formal vs conceptual by year | `figures/phase9-formal-conceptual-year` |",
             "| Geography (venue-country proxy) | `figures/phase9-geography` |",
             "",
             ]
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    # venue-country-map.md (documentation)
    with open(COUNTRY_MD, "w", encoding="utf-8") as fh:
        fh.write("# Venue-country proxy map — Paper 01 Phase 9 (9.1.1)\n\n")
        fh.write("Curated mapping used for the geographic distribution. Basis: "
                 "publisher/association headquarters country. This is a proxy: it "
                 "attributes papers to the country of the venue's publisher, not the "
                 "authors' institutions. Per-paper affiliation coding was not "
                 "performed in this run (Phase A operationalization).\n\n")
        fh.write(markdown_table(["Venue (normalized)", "Category", "Country/group"],
                                [[v, VENUE_CATEGORY.get(v, "other"),
                                  VENUE_COUNTRY.get(v, "unassigned")]
                                 for v in sorted(VENUE_COUNTRY)]))
        fh.write("\nVenues not listed map to `unassigned` (tail of 500+ low-frequency "
                 "venues). Coverage: rows with an assigned venue-country "
                 f"= {int((df['country'] != 'unassigned').sum())}/{n} "
                 f"({(df['country'] != 'unassigned').mean() * 100:.1f}%).\n")

    # append pointer to summary-statistics.md
    with open(SUMMARY_MD, "a", encoding="utf-8") as fh:
        fh.write("\n\n---\n\n## Phase 9 supplement (Task 9.1)\n\n"
                 "See `phase9-summary.md` + `figures/phase9-*` (venue distribution, "
                 "subdomain x year, conditional co-occurrence, methodology x subdomain, "
                 "formal vs conceptual, venue-country proxy). Figures exported "
                 "publication-ready as PDF/SVG with PNG previews.\n")

    print(f"phase9-summary written: {OUT_MD.name}")
    print(f"figures: {sorted(p.name for p in FIG_DIR.glob('phase9-*'))}")
    print(f"geography coverage: {(df['country'] != 'unassigned').sum()}/{n} rows "
          f"({(df['country'] != 'unassigned').mean() * 100:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
