#!/usr/bin/env python3
"""
Paper 01 — Phase 8: quality report + sensitivity analysis (Tasks 8.2.6, 8.3, 8.4).

Reads research/quality-scores.csv (D1-D8, composite, tier) plus
charted-data.csv (subdomains) and sigma-trap-signal.csv, and produces:

  - 8.2.6: `low_credibility` flag column (tier D or E; composite < 1.6) added
    to quality-scores.csv (idempotent — existing column untouched).
  - 8.3:   sensitivity comparisons full set (1,268) vs high-credibility subset
    (tiers A+B, composite >= 2.4): subdomain distributions, sigma-trap signal
    prevalence, score-by-year trend.
  - 8.4:   summary statistics (composite distribution, median, IQR,
    per-dimension medians), score-by-subdomain, score-by-year, figures
    research/charting/figures/quality-*.png.
  - report: research/charting/quality-report.md

Config: research/charting/rubric-config.yaml (tier thresholds, sensitivity
cutoffs). Outputs are reproducible from charted data (CC.2.4); CSV only, no
large artifacts (CC.5.2).
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import yaml

matplotlib.use("Agg")

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
SCORES_CSV = BASE / "research" / "quality-scores.csv"
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
SIGNAL_CSV = BASE / "research" / "sigma-trap-signal.csv"
REPORT_MD = BASE / "research" / "charting" / "quality-report.md"
FIG_DIR = BASE / "research" / "charting" / "figures"
CONFIG = BASE / "research" / "charting" / "rubric-config.yaml"

DIMS = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
RATER_DIMS = ["D2", "D3", "D4", "D5", "D7", "D8"]


def parse_score(v: str) -> float | None:
    v = (v or "").strip()
    if not v:
        return None
    try:
        return float(v)
    except ValueError:
        return None


def main() -> int:
    cfg = yaml.safe_load(open(CONFIG, encoding="utf-8"))
    tiers = cfg["tiers"]  # {"A": 3.2, "B": 2.4, "C": 1.6, "D": 0.8}
    low_max = float(cfg["low_credibility_max"])        # 1.6
    sens_min = float(cfg["sensitivity_min"])            # 2.4

    rows = list(csv.DictReader(open(SCORES_CSV, newline="", encoding="utf-8")))
    fields = list(rows[0].keys())
    n_all = len(rows)

    # ---------------- 8.2.6: low-credibility flag column ----------------
    if "low_credibility" not in fields:
        fields.append("low_credibility")
        for r in rows:
            comp = parse_score(r.get("composite"))
            r["low_credibility"] = "1" if (comp is not None and comp < low_max) else "0"
        with open(SCORES_CSV, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
        n_flag = sum(1 for r in rows if r["low_credibility"] == "1")
    else:
        n_flag = sum(1 for r in rows if (r.get("low_credibility") or "") == "1")

    # ---------------- load subdomains + sigma-trap signal ----------------
    subdomains: dict[str, str] = {}
    for r in csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")):
        subdomains[r["paper_id"]] = r.get("subdomains", "")
    signal_ids = {r["paper_id"] for r in
                  csv.DictReader(open(SIGNAL_CSV, newline="", encoding="utf-8"))}

    # ---------------- set splits ----------------
    def composite(r) -> float | None:
        return parse_score(r.get("composite"))

    full = [r for r in rows]
    sens = [r for r in rows if (composite(r) or 0.0) >= sens_min]

    # ---------------- helpers ----------------
    def subdomain_split(rs: list[dict]) -> Counter:
        c: Counter = Counter()
        for r in rs:
            for s in re_split(subdomains.get(r["paper_id"], "")):
                c[s] += 1
        return c

    def re_split(s: str) -> list[str]:
        return [x.strip() for x in s.replace(";", ",").split(",") if x.strip()]

    def pct(n: int, d: int) -> str:
        return f"{100.0 * n / d:.1f}%" if d else "n/a"

    def signal_stats(rs: list[dict]) -> tuple[int, str]:
        n = sum(1 for r in rs if r["paper_id"] in signal_ids)
        return n, pct(n, len(rs))

    def year_stats(rs: list[dict]) -> list[tuple[str, int, float, int]]:
        by_year: dict[str, list[float]] = {}
        for r in rs:
            c = composite(r)
            if c is None:
                continue
            by_year.setdefault(r["year"], []).append(c)
        out = []
        for y in sorted(by_year):
            vals = by_year[y]
            out.append(((y or "(unknown)"), len(vals), sum(vals) / len(vals), len(vals)))
        return out

    def median(vals: list[float]) -> float:
        s = sorted(vals)
        n = len(s)
        if n == 0:
            return float("nan")
        if n % 2:
            return s[n // 2]
        return (s[n // 2 - 1] + s[n // 2]) / 2

    def iqr(vals: list[float]) -> tuple[float, float]:
        s = sorted(vals)
        n = len(s)
        if n == 0:
            return (float("nan"), float("nan"))
        lo = s[max(0, n // 4 - 1)] if n % 4 else s[n // 4]
        hi = s[min(n - 1, 3 * n // 4)] if n % 4 else s[3 * n // 4 - 1]
        return (lo, hi)

    # ---------------- 8.4.1 summary stats ----------------
    comps_full = [c for c in (composite(r) for r in full) if c is not None]
    comps_sens = [c for c in (composite(r) for r in sens) if c is not None]

    def dim_medians(rs: list[dict]) -> dict[str, float]:
        out = {}
        for d in DIMS:
            vals = [parse_score(r.get(d)) for r in rs]
            vals = [v for v in vals if v is not None]
            out[d] = median(vals) if vals else float("nan")
        return out

    md_full = dim_medians(full)
    md_sens = dim_medians(sens)

    # ---------------- 8.4.2 by-subdomain ----------------
    sub_full = subdomain_split(full)
    sub_sens = subdomain_split(sens)

    # ---------------- 8.4.3 by-year ----------------
    yr_full = year_stats(full)
    yr_sens = year_stats(sens)

    # ---------------- figures ----------------
    FIG_DIR.mkdir(exist_ok=True)

    def fig_composite(vals_full: list[float], vals_sens: list[float], fname: str) -> None:
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.hist(vals_full, bins=20, alpha=0.6, label="full set")
        ax.hist(vals_sens, bins=20, alpha=0.6, label="tiers A+B")
        ax.set_xlabel("composite")
        ax.set_ylabel("papers")
        ax.legend()
        fig.tight_layout()
        fig.savefig(FIG_DIR / fname, dpi=150)
        plt.close(fig)

    def fig_tiers(rs: list[dict], fname: str) -> None:
        c = Counter(r["tier"] for r in rs)
        order = ["A", "B", "C", "D", "E"]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar([t for t in order if c[t]], [c[t] for t in order if c[t]])
        ax.set_xlabel("tier")
        ax.set_ylabel("papers")
        fig.tight_layout()
        fig.savefig(FIG_DIR / fname, dpi=150)
        plt.close(fig)

    def fig_subdomains(c_full: Counter, c_sens: Counter, fname: str) -> None:
        top = [s for s, _ in c_full.most_common(12)]
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(top, [c_full[s] for s in top], alpha=0.6, label="full set")
        ax.bar(top, [c_sens[s] for s in top], alpha=0.6, label="tiers A+B")
        ax.set_xlabel("subdomain")
        ax.set_ylabel("papers")
        ax.tick_params(axis="x", rotation=45)
        ax.legend()
        fig.tight_layout()
        fig.savefig(FIG_DIR / fname, dpi=150)
        plt.close(fig)

    def fig_year(yr: list[tuple[str, int, float, int]], fname: str) -> None:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot([y for y, _, _, _ in yr], [m for _, _, m, _ in yr], marker="o")
        ax.set_xlabel("year")
        ax.set_ylabel("mean composite")
        fig.tight_layout()
        fig.savefig(FIG_DIR / fname, dpi=150)
        plt.close(fig)

    fig_composite(comps_full, comps_sens, "quality-composite-hist.png")
    fig_tiers(full, "quality-tiers.png")
    fig_subdomains(sub_full, sub_sens, "quality-subdomains.png")
    fig_year(yr_full, "quality-year-trend.png")

    # ---------------- sigma-trap signal ----------------
    sig_full_n, sig_full_pct = signal_stats(full)
    sig_sens_n, sig_sens_pct = signal_stats(sens)

    # ---------------- report ----------------
    q1, q3 = iqr(comps_full)
    lines = []
    add = lines.append
    add("# Quality assessment report — Paper 01, Phase 8")
    add("")
    add(f"- Papers scored: **{n_all}** (all included studies)")
    add(f"- Composite range 0–4; tiers: A ≥ {tiers['A']}, B ≥ {tiers['B']}, "
        f"C ≥ {tiers['C']}, D ≥ {tiers['D']}, E below D")
    add(f"- **8.2.6** low-credibility flag (tier D/E, composite < {low_max}): "
        f"**{n_flag}** papers")
    add(f"- **8.3** sensitivity subset (tiers A+B, composite ≥ {sens_min}): "
        f"**{len(sens)}** papers")
    add("")
    add("## 8.4.1 Summary statistics")
    add("")
    add(f"- Composite median: **{median(comps_full):.2f}**  "
        f"(IQR {q1:.2f}–{q3:.2f}), n={len(comps_full)}")
    add("- Per-dimension medians (full set): "
        + ", ".join(f"{d}={md_full[d]:.2f}" for d in DIMS))
    add("- Per-dimension medians (tiers A+B): "
        + ", ".join(f"{d}={md_sens[d]:.2f}" for d in DIMS))
    add("")
    add("## 8.4.2 Score by subdomain (full set)")
    add("")
    add("| subdomain | full | tiers A+B |")
    add("|---|---|---|")
    for s, n in sub_full.most_common(15):
        add(f"| {s} | {n} | {sub_sens.get(s, 0)} |")
    add("")
    add("## 8.4.3 Score by year")
    add("")
    add("| year | full n | full mean | A+B n | A+B mean |")
    add("|---|---|---|---|---|")
    yr_sens_map = {y: (n, m) for y, n, m, _ in yr_sens}
    for y, n, m, _ in yr_full:
        sn, sm = yr_sens_map.get(y, (0, float("nan")))
        sm_s = f"{sm:.2f}" if sm == sm else "—"
        add(f"| {y} | {n} | {m:.2f} | {sn} | {sm_s} |")
    add("")
    add("## 8.3 Sensitivity: full set vs tiers A+B")
    add("")
    add(f"- σ-trap signal papers (relevance_final ≥ 4 or revised): "
        f"**{sig_full_n} / {n_all} ({sig_full_pct})** full vs "
        f"**{sig_sens_n} / {len(sens)} ({sig_sens_pct})** A+B")
    add("")
    add("Figures: `quality-composite-hist.png`, `quality-tiers.png`, "
        "`quality-subdomains.png`, `quality-year-trend.png`")

    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"quality-scores rows: {n_all}; low-credibility flagged: {n_flag}")
    print(f"sensitivity subset (A+B, >= {sens_min}): {len(sens)}")
    print(f"sigma-trap signal: {sig_full_n}/{n_all} full, {sig_sens_n}/{len(sens)} sens")
    print(f"report -> {REPORT_MD.name}; figures -> {FIG_DIR.name}/quality-*")
    return 0


if __name__ == "__main__":
    sys.exit(main())
