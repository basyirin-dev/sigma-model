#!/usr/bin/env python3
"""
Paper 02 — Phase 9 (Task 9.1): prepare synthesis analysis dataset.

Merges charted-data-main.csv with risk-of-bias.csv and computes derived
variables per the phase-doc operationalizations:

  id_ood_gap       ID accuracy - OOD accuracy (primary effect; id_ood_gap_raw
                   preferred, else computed from means)
  lor              log odds ratio ln((ID/(1-ID))/(OOD/(1-OOD))) with 0.5/n
                   continuity correction when a cell is 0 or 1
  cohens_d         (ID-OOD)/pooled_SD where both SDs present
  gap_se           standard error: id_ood_gap_se where present, else binomial
                   SE from the accuracies
  outlier          |z| > 3 on the gap distribution
  S0..S5           scenario flags (primary, not-HIGH, LOW-only, peer-reviewed,
                   code, seeds>=3) per Phase 8 sensitivity plan
  subgroup keys    benchmark family, arch family, model scale

Output: research/analysis/analysis-data.csv + analysis-data-report.md

Usage: python3 prepare_analysis_data.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
MAIN_CSV = BASE / "research" / "charted-data-main.csv"
ROB_CSV = BASE / "research" / "risk-of-bias.csv"
OUT_CSV = BASE / "research" / "analysis" / "analysis-data.csv"
OUT_MD = BASE / "research" / "analysis" / "analysis-data-report.md"


def num(s: str) -> float | None:
    try:
        v = float(s)
        return v if math.isfinite(v) else None
    except (TypeError, ValueError):
        return None


def lor_from(id_acc: float, ood_acc: float, n: int = 100) -> float:
    """Log odds ratio with 0.5/n continuity correction."""
    ida = min(max(id_acc, 0.5 / n), 1 - 0.5 / n)
    ooda = min(max(ood_acc, 0.5 / n), 1 - 0.5 / n)
    return math.log((ida / (1 - ida)) / (ooda / (1 - ooda)))


def binomial_se(p1: float, p2: float, n: int = 100) -> float:
    return math.sqrt(p1 * (1 - p1) / n + p2 * (1 - p2) / n)


def main() -> int:
    m = pd.read_csv(MAIN_CSV, dtype=str).fillna("")
    rob = pd.read_csv(ROB_CSV, dtype=str)
    df = m.merge(rob[["study_id", "overall"]], on="study_id", how="left")

    idv = pd.to_numeric(df["id_acc_mean"].replace("", pd.NA), errors="coerce")
    oov = pd.to_numeric(df["ood_acc_mean"].replace("", pd.NA), errors="coerce")
    raw_gap = pd.to_numeric(df["id_ood_gap_raw"].replace("", pd.NA), errors="coerce")
    gap_se = pd.to_numeric(df["id_ood_gap_se"].replace("", pd.NA), errors="coerce")
    id_sd = pd.to_numeric(df["id_acc_sd"].replace("", pd.NA), errors="coerce")
    ood_sd = pd.to_numeric(df["ood_acc_sd"].replace("", pd.NA), errors="coerce")
    ns = pd.to_numeric(df["n_seeds_value"].replace("", pd.NA), errors="coerce")

    # gap: prefer charted raw gap, else compute from means
    gap = raw_gap.where(raw_gap.notna(), idv - oov)
    df["id_ood_gap"] = gap

    # LOR with continuity correction
    lor = pd.Series(np.nan, index=df.index)
    ok = idv.notna() & oov.notna() & (idv > 0) & (idv < 1) & (oov > 0) & (oov < 1)
    for i in df.index[ok]:
        n = max(int(ns[i]) if pd.notna(ns[i]) else 100, 2)
        lor[i] = lor_from(idv[i], oov[i], n)
    df["lor"] = lor

    # Cohen's d where both SDs present
    pooled_sd = np.sqrt((id_sd**2 + ood_sd**2) / 2)
    df["cohens_d"] = (idv - oov) / pooled_sd

    # gap SE: charted SE, else binomial from means (n from seeds or 100)
    bin_se = pd.Series(np.nan, index=df.index)
    for i in df.index[ok]:
        n = max(int(ns[i]) if pd.notna(ns[i]) else 100, 2)
        bin_se[i] = binomial_se(idv[i], oov[i], n)
    df["gap_se"] = gap_se.where(gap_se.notna(), bin_se)

    # outlier flag on gap distribution
    g = gap.dropna()
    z = (g - g.mean()) / g.std()
    outliers = set(g.index[z.abs() > 3])
    df["outlier"] = df.index.isin(outliers)

    # scenario flags (Phase 8 sensitivity plan)
    df["S0"] = True
    df["S1_not_high"] = df["overall"] != "HIGH"
    df["S2_low_only"] = df["overall"] == "LOW"
    df["S3_peer_reviewed"] = df["peer_reviewed"] == "TRUE"
    df["S4_code"] = df["code_available"] == "TRUE"
    df["S5_seeds_ge3"] = ns >= 3

    # subgroup keys
    df["benchmark_family"] = df["task_primary"].where(
        df["task_primary"].isin(
            ["CFQ", "SCAN", "COGS", "gSCAN", "GeoQuery", "PCFG_SET", "MultiNLI",
             "CelebA", "Waterbirds", "ColoredMNIST", "CIFAR10", "Camelyon17"]),
        "custom")
    df["interventional"] = df["train_regime_sigma"].eq("other_sigma")

    cols = ["study_id", "id", "title", "year", "overall", "peer_reviewed",
            "code_available", "n_seeds_value", "task_primary", "benchmark_family",
            "arch_family", "model_scale_category", "train_regime_sigma",
            "baseline_regime", "id_acc_mean", "ood_acc_mean", "id_acc_sd",
            "ood_acc_sd", "id_ood_gap", "lor", "cohens_d", "gap_se", "outlier",
            "interventional", "schema_coherence_measured", "repr_analysis",
            "relevance_sigma_trap", "relevance_alignment",
            "S0", "S1_not_high", "S2_low_only", "S3_peer_reviewed", "S4_code",
            "S5_seeds_ge3"]
    df[cols].to_csv(OUT_CSV, index=False)

    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("# Analysis dataset report — Paper 02 Phase 9 (9.1)\n\n")
        fh.write(f"- Studies: {len(df)}; with gap: {gap.notna().sum()}; "
                 f"LOR: {lor.notna().sum()}; Cohen's d: {df['cohens_d'].notna().sum()}; "
                 f"gap SE: {df['gap_se'].notna().sum()}\n")
        fh.write(f"- Gap distribution: mean {gap.mean():.3f}, sd {gap.std():.3f}, "
                 f"min {gap.min():.3f}, max {gap.max():.3f}\n")
        fh.write(f"- Outliers (|z|>3): {len(outliers)}\n")
        fh.write(f"- Interventional studies: {int(df['interventional'].sum())} "
                 f"(S046)\n")
        fh.write(f"- LOR check (skewness): {lor.skew():.2f}; gap normality "
                 f"(skew): {gap.skew():.2f}\n")
        for s in ["S0", "S1_not_high", "S2_low_only", "S3_peer_reviewed", "S4_code",
                  "S5_seeds_ge3"]:
            fh.write(f"- {s}: n={int(df[s].sum())}, gap k="
                     f"{int((df[s] & gap.notna()).sum())}\n")
    print(f"analysis-data.csv written ({len(df)} rows, {len(cols)} cols)")
    print(f"report written: {OUT_MD.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
