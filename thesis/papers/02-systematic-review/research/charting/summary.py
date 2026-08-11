#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.5.3/7.5.4): summary statistics + figures.

Reads research/charted-data.csv (long format) and produces:
  - research/charting/summary-statistics.md
  - research/charting/figures/*.png
      01_pub_type.png       bar: publication type (study design)
      02_benchmark.png      bar: top benchmarks (task_primary)
      03_architecture.png   bar: architecture family
      04_intervention.png   bar: train regime (intervention type)
      05_year.png           bar: publication year distribution
      06_id_ood_swarm.png   swarm/paired: ID vs OOD accuracy per sub-experiment
      07_id_ood_timeseries.png  line: mean ID/OOD/gap by year

Only rows with non-empty numeric id/ood accuracy contribute to accuracy
statistics (noted in the report).
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
CHARTED_CSV = BASE / "research" / "charted-data.csv"
OUT_MD = BASE / "research" / "charting" / "summary-statistics.md"
FIG_DIR = BASE / "research" / "charting" / "figures"

# sub-experiment-level accuracy columns in the long format
SUBEXP_ACC = ("id_acc_mean", "ood_acc_mean", "id_acc_sd", "ood_acc_sd",
              "id_acc_n_seeds", "ood_acc_n_seeds", "id_ood_gap")


def num(v: str) -> float | None:
    try:
        x = float(v)
        return x if x == x else None
    except (TypeError, ValueError):
        return None


def plot_bar(ax, labels, counts, title, xlabel, rotate=45, limit=25) -> None:
    if len(labels) > limit:  # aggregate the long tail
        keep = labels[:limit - 1]
        rest = sum(counts[limit - 1:])
        labels, counts = keep + ["other"], counts[:limit - 1] + [rest]
    ax.bar(range(len(labels)), counts, color="#4C72B0")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=rotate, ha="right", fontsize=8)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("count")


def main() -> None:
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    n_rows = len(rows)
    studies = sorted({r["study_id"] for r in rows}, key=lambda s: int(s[1:]))
    n_studies = len(studies)

    pub = Counter(r["pub_type"] for r in rows)
    venue = Counter(r["pub_venue_type"] for r in rows)
    bench = Counter(r["task_primary"] for r in rows)
    arch = Counter(r["arch_family"] for r in rows)
    regime = Counter(r["train_regime"] for r in rows)
    year = Counter(r["year"] for r in rows)

    acc_rows = [r for r in rows
                if num(r["id_acc_mean"]) is not None and num(r["ood_acc_mean"]) is not None]
    id_means = [num(r["id_acc_mean"]) for r in acc_rows]
    ood_means = [num(r["ood_acc_mean"]) for r in acc_rows]
    gaps = [i - o for i, o in zip(id_means, ood_means)]

    def fmt(x: float | None) -> str:
        return "—" if x is None else f"{x:.4f}"

    mean_id = float(np.mean(id_means)) if id_means else None
    mean_ood = float(np.mean(ood_means)) if ood_means else None
    mean_gap = float(np.mean(gaps)) if gaps else None

    FIG_DIR.mkdir(exist_ok=True)

    # 01-05 bar charts
    fig, ax = plt.subplots(figsize=(8, 5))
    plot_bar(ax, [k for k, _ in pub.most_common()], [v for _, v in pub.most_common()],
             "Publication type (study design)", "pub_type")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "01_pub_type.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    plot_bar(ax, [k for k, _ in bench.most_common()], [v for _, v in bench.most_common()],
             "Primary task/benchmark", "task_primary")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "02_benchmark.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    plot_bar(ax, [k for k, _ in arch.most_common()], [v for _, v in arch.most_common()],
             "Architecture family", "arch_family")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "03_architecture.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    plot_bar(ax, [k for k, _ in regime.most_common()], [v for _, v in regime.most_common()],
             "Training regime (intervention type)", "train_regime")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "04_intervention.png", dpi=150)
    plt.close(fig)

    years = sorted(year)
    fig, ax = plt.subplots(figsize=(8, 5))
    plot_bar(ax, [str(y) for y in years], [year[y] for y in years],
             "Publication year", "year", rotate=0)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "05_year.png", dpi=150)
    plt.close(fig)

    # 06 paired swarm: ID vs OOD per sub-experiment
    fig, ax = plt.subplots(figsize=(8, 5))
    xs = np.array([0] * len(id_means) + [1] * len(ood_means))
    ys = np.array(id_means + ood_means)
    rng = np.random.default_rng(7)
    ax.scatter(xs + rng.normal(0, 0.04, len(xs)), ys, s=12, alpha=0.35,
               color="#C44E52")
    ax.plot([0, 1], [mean_id, mean_ood], "k-", linewidth=2,
            label=f"mean ID={fmt(mean_id)} / OOD={fmt(mean_ood)}")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["ID", "OOD"])
    ax.set_ylabel("accuracy (proportion)")
    ax.set_title(f"ID vs OOD accuracy, {len(acc_rows)} sub-experiments")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "06_id_ood_swarm.png", dpi=150)
    plt.close(fig)

    # 07 time series: mean ID/OOD/gap by year
    by_year: dict[int, list[tuple[float, float]]] = {}
    for r in acc_rows:
        try:
            y = int(r["year"])
        except (TypeError, ValueError):
            continue
        by_year.setdefault(y, []).append((num(r["id_acc_mean"]), num(r["ood_acc_mean"])))
    if by_year:
        ys_ = sorted(by_year)
        mid = [float(np.mean([p[0] for p in by_year[y]])) for y in ys_]
        mood = [float(np.mean([p[1] for p in by_year[y]])) for y in ys_]
        mgap = [float(np.mean([p[0] - p[1] for p in by_year[y]])) for y in ys_]
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(ys_, mid, "o-", label="mean ID accuracy")
        ax.plot(ys_, mood, "s-", label="mean OOD accuracy")
        ax.plot(ys_, mgap, "d--", label="mean ID-OOD gap")
        ax.set_xlabel("year")
        ax.set_ylabel("accuracy (proportion)")
        ax.set_title("Mean ID/OOD accuracy and gap by publication year")
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIG_DIR / "07_id_ood_timeseries.png", dpi=150)
        plt.close(fig)

    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("# Summary statistics — Paper 02 Phase 7 (Task 7.5.3)\n\n")
        fh.write(f"- Studies charted: **{n_studies}**\n")
        fh.write(f"- Long-format rows (study x split x arch x intervention): **{n_rows}**\n")
        fh.write(f"- Sub-experiments with ID+OOD accuracy: **{len(acc_rows)}**\n")
        fh.write(f"- Mean ID accuracy: **{fmt(mean_id)}**\n")
        fh.write(f"- Mean OOD accuracy: **{fmt(mean_ood)}**\n")
        fh.write(f"- Mean ID-OOD gap: **{fmt(mean_gap)}**\n\n")
        fh.write("## Distribution by publication type\n\n")
        for k, v in pub.most_common():
            fh.write(f"- {k}: {v}\n")
        fh.write("\n## Distribution by publication venue type\n\n")
        for k, v in venue.most_common():
            fh.write(f"- {k}: {v}\n")
        fh.write("\n## Distribution by benchmark (task_primary)\n\n")
        for k, v in bench.most_common():
            fh.write(f"- {k}: {v}\n")
        fh.write("\n## Distribution by architecture family\n\n")
        for k, v in arch.most_common():
            fh.write(f"- {k}: {v}\n")
        fh.write("\n## Distribution by training regime (intervention)\n\n")
        for k, v in regime.most_common():
            fh.write(f"- {k}: {v}\n")
        fh.write("\n## Distribution by year\n\n")
        for y in years:
            fh.write(f"- {y}: {year[y]}\n")

    print(f"wrote {OUT_MD.name}: {n_studies} studies, {n_rows} long rows, "
          f"{len(acc_rows)} with ID+OOD accuracies")
    print(f"mean ID {fmt(mean_id)} / OOD {fmt(mean_ood)} / gap {fmt(mean_gap)}")
    print(f"figures -> {FIG_DIR}")


if __name__ == "__main__":
    sys.exit(main())
