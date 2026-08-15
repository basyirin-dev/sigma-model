#!/usr/bin/env python3
"""Verify Table 5 (Results Summary) against all_results.pkl.

Usage:
    python scripts/verify_table5.py [--pkl PATH]

Reads the experiment pickle and recomputes Table 5 values, comparing them
against the published manuscript values.
"""

import argparse
import pickle
import sys
from pathlib import Path

import numpy as np


PAPER_VALUES = {
    "baseline":      {"id_mean": 90.15, "id_std": 2.27, "ood_mean": 44.53, "ood_std": 4.72, "n": 15},
    "additive":      {"id_mean": 97.02, "id_std": 1.65, "ood_mean": 97.01, "ood_std": 6.67, "n": 15},
    "multiplicative": {"id_mean": 97.43, "id_std": 1.89, "ood_mean": 94.08, "ood_std": 7.96, "n": 15},
}

ABS_TOL = 1.0  # Allow ±1% tolerance for floating-point rounding


def verify(pkl_path: str) -> bool:
    with open(pkl_path, "rb") as f:
        all_results = pickle.load(f)

    all_match = True
    print(f"{'Condition':<20} {'Acc_ID (paper)':>18} {'Acc_ID (data)':>18} {'Match':>6}")
    print(f"{'':20} {'Acc_OOD (paper)':>18} {'Acc_OOD (data)':>18} {'Match':>6}")
    print("-" * 70)

    for cond, expected in PAPER_VALUES.items():
        runs = all_results.get(cond)
        if runs is None:
            print(f"  MISSING condition: {cond}")
            all_match = False
            continue

        # Handle both list-of-dicts and list-of-metrics formats
        id_accs = [r["final"]["acc_id"] for r in runs]
        ood_accs = [r["final"]["acc_ood"] for r in runs]

        calc_id_mean = np.mean(id_accs)
        calc_id_std = np.std(id_accs)
        calc_ood_mean = np.mean(ood_accs)
        calc_ood_std = np.std(ood_accs)
        calc_n = len(runs)

        id_match = abs(calc_id_mean - expected["id_mean"]) < ABS_TOL and \
                   abs(calc_id_std - expected["id_std"]) < ABS_TOL
        ood_match = abs(calc_ood_mean - expected["ood_mean"]) < ABS_TOL and \
                    abs(calc_ood_std - expected["ood_std"]) < ABS_TOL
        n_match = calc_n == expected["n"]

        id_icon = "✅" if id_match else "❌"
        ood_icon = "✅" if ood_match else "❌"
        n_icon = "✅" if n_match else "❌"

        print(f"{cond:<20} {expected['id_mean']:>7.2f}±{expected['id_std']:<7.2f} "
              f"{calc_id_mean:>7.2f}±{calc_id_std:<7.2f}  {id_icon}")
        print(f"{'':20} {expected['ood_mean']:>7.2f}±{expected['ood_std']:<7.2f} "
              f"{calc_ood_mean:>7.2f}±{calc_ood_std:<7.2f}  {ood_icon}")
        print(f"{'n_runs':20} {expected['n']:>16} {calc_n:>16}  {n_icon}")

        if not (id_match and ood_match and n_match):
            all_match = False

    print()
    if all_match:
        print("✅ Table 5 verified: all values match within tolerance.")
    else:
        print("❌ Table 5 MISMATCH: some values differ from the manuscript.")
    return all_match


def main():
    parser = argparse.ArgumentParser(description="Verify Table 5 against all_results.pkl")
    parser.add_argument("--pkl", default="output/results/all_results.pkl",
                        help="Path to all_results.pkl")
    args = parser.parse_args()

    pkl_path = Path(args.pkl)
    if not pkl_path.exists():
        print(f"File not found: {pkl_path}")
        print("Usage: python scripts/verify_table5.py --pkl PATH_TO/all_results.pkl")
        sys.exit(1)

    ok = verify(str(pkl_path))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
