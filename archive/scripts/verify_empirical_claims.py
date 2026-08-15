#!/usr/bin/env python3
"""Verify empirical claims in manuscript.tex against all_results.pkl.

Checks key numerical claims from the body text, tables, and figure captions.
Reports PASS/FAIL for each claim with tolerance bands.

Usage:
    python scripts/verify_empirical_claims.py [--pkl PATH]
"""

import argparse
import pickle
import sys
from pathlib import Path

import numpy as np


TOL = {
    "accuracy": 1.0,   # ±1% for accuracy values
    "effect": 0.5,     # ±0.5 for Cohen's d and t-stats
    "pvalue": 0.01,    # generous for p-value order checks
}


def load_results(pkl_path: str) -> dict:
    with open(pkl_path, "rb") as f:
        return pickle.load(f)


def check(label: str, actual: float, expected: float, tol: float, tol_type: str = "abs") -> bool:
    if tol_type == "abs":
        ok = abs(actual - expected) <= tol
    elif tol_type == "rel":
        ok = abs(actual - expected) / max(abs(expected), 1e-9) <= tol
    else:
        ok = False
    icon = "✅" if ok else "❌"
    print(f"  {icon} {label}: actual={actual:.4f}, expected={expected:.4f}, tol={tol}")
    return ok


def verify(pkl_path: str) -> bool:
    all_results = load_results(pkl_path)
    all_ok = True

    # ── Table 5 Claims (Section 4.2.5 / Table 5) ──────────────────────
    print("\n=== TABLE 5: Results Summary ===")

    for cond, expected in {
        "baseline":      {"id": (90.15, 2.27), "ood": (44.53, 4.72)},
        "additive":      {"id": (97.02, 1.65), "ood": (97.01, 6.67)},
        "multiplicative": {"id": (97.43, 1.89), "ood": (94.08, 7.96)},
    }.items():
        runs = all_results.get(cond)
        if runs is None:
            print(f"  ❌ Missing condition: {cond}")
            all_ok = False
            continue
        id_accs = [r["final"]["acc_id"] for r in runs]
        ood_accs = [r["final"]["acc_ood"] for r in runs]
        print(f"\n  --- {cond} (n={len(runs)}) ---")
        all_ok &= check("ID mean", np.mean(id_accs), expected["id"][0], TOL["accuracy"])
        all_ok &= check("ID std", np.std(id_accs), expected["id"][1], TOL["accuracy"])
        all_ok &= check("OOD mean", np.mean(ood_accs), expected["ood"][0], TOL["accuracy"])
        all_ok &= check("OOD std", np.std(ood_accs), expected["ood"][1], TOL["accuracy"])

    # ── Body-text Claims ───────────────────────────────────────────────
    print("\n=== BODY TEXT: Key Claims ===")

    # Claim: Baseline compositional gap = 45.6%
    bl_id = np.mean([r["final"]["acc_id"] for r in all_results["baseline"]])
    bl_ood = np.mean([r["final"]["acc_ood"] for r in all_results["baseline"]])
    gap = bl_id - bl_ood
    all_ok &= check("Baseline compositional gap", gap, 45.6, TOL["accuracy"])

    # Claim: Additive OOD gap ≈ 0.0pp
    add_ood = np.mean([r["final"]["acc_ood"] for r in all_results["additive"]])
    add_gap = np.mean([r["final"]["acc_id"] for r in all_results["additive"]]) - add_ood
    all_ok &= check("Additive OOD gap", add_gap, 0.0, TOL["accuracy"])

    # ── Statistical Test Claims ────────────────────────────────────────
    print("\n=== STATISTICAL TESTS: t-test claims ===")
    from scipy import stats

    # Baseline vs Additive (OOD)
    bl_oods = [r["final"]["acc_ood"] for r in all_results["baseline"]]
    add_oods = [r["final"]["acc_ood"] for r in all_results["additive"]]
    mult_oods = [r["final"]["acc_ood"] for r in all_results["multiplicative"]]

    t_bl_add, p_bl_add = stats.ttest_ind(bl_oods, add_oods, equal_var=False)
    all_ok &= check("Baseline vs Additive t-stat", t_bl_add, -24.034, TOL["effect"])
    print(f"  {'✅' if p_bl_add < 0.001 else '❌'} Baseline vs Additive p < 0.001: p={p_bl_add:.6f}")

    # Baseline vs Multiplicative (OOD)
    t_bl_mul, p_bl_mul = stats.ttest_ind(bl_oods, mult_oods, equal_var=False)
    all_ok &= check("Baseline vs Mult t-stat", t_bl_mul, -20.0, 2.0)
    print(f"  {'✅' if p_bl_mul < 0.001 else '❌'} Baseline vs Mult p < 0.001: p={p_bl_mul:.6f}")

    # Additive vs Multiplicative (OOD)
    t_add_mul, p_add_mul = stats.ttest_ind(add_oods, mult_oods, equal_var=False)
    all_ok &= check("Add vs Mult t-stat", t_add_mul, 1.06, 0.5)
    print(f"  {'✅' if p_add_mul > 0.05 else '❌'} Add vs Mult not significant: p={p_add_mul:.4f}")

    # ── Sigma Trajectory Claims ────────────────────────────────────────
    print("\n=== SIGMA TRAJECTORIES ===")
    for cond in ["additive", "multiplicative"]:
        runs = all_results[cond]
        final_sigmas = [r["sigma_tilde"][-1] for r in runs if len(r["sigma_tilde"]) > 0]
        if final_sigmas:
            mean_sigma = np.mean(final_sigmas)
            print(f"  {cond}: final sigma_A mean = {mean_sigma:.3f}")

    # ── Summary ────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    if all_ok:
        print("✅ All verifiable claims match within tolerance.")
    else:
        print("❌ Some claims differ — review output above.")
    return all_ok


def main():
    parser = argparse.ArgumentParser(description="Verify empirical claims against all_results.pkl")
    parser.add_argument("--pkl", default="output/results/all_results.pkl",
                        help="Path to all_results.pkl")
    args = parser.parse_args()

    pkl_path = Path(args.pkl)
    if not pkl_path.exists():
        print(f"File not found: {pkl_path}")
        print("Usage: python scripts/verify_empirical_claims.py --pkl PATH_TO/all_results.pkl")
        sys.exit(1)

    ok = verify(str(pkl_path))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
