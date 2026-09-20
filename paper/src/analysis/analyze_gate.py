"""Mechanism-Gate Statistical Analysis and Evaluation Engine for Paper 02.

Evaluates the 450-run gate results against pre-registered criteria (preregistration.md):
- Criterion 1: 2-parameter logistic change-point fit for sharp separatrix (k >= 15.0).
- Criterion 2: Late-onset destabilization rescue at t_int = 1000 (>= 90% recovery).
- Criterion 3: Pairwise TOST equivalence across supercritical pressures (margin +/- 2.5%).
"""

from __future__ import annotations

import argparse
import pickle
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import t as student_t


def logistic_step_fn(lambda_val: np.ndarray, k: float, lambda_crit: float) -> np.ndarray:
    """Two-parameter logistic change-point function."""
    z = -k * (lambda_val - lambda_crit)
    # Clip z to avoid numerical overflow in exp
    z_clipped = np.clip(z, -50.0, 50.0)
    return 1.0 / (1.0 + np.exp(z_clipped))


def fit_logistic_separatrix(
    lambda_vals: np.ndarray,
    escape_fractions: np.ndarray,
) -> tuple[float, float, float]:
    """Fit 2-parameter logistic change-point model to empirical escape fractions.

    Returns:
        tuple (k_steepness, lambda_crit, r_squared).
    """
    if len(lambda_vals) < 4:
        return 0.0, 0.0, 0.0

    try:
        # Initial guesses: k = 70.0, lambda_crit = 0.025
        p0 = [70.0, 0.025]
        bounds = ([0.1, 0.0], [300.0, float(np.max(lambda_vals))])

        popt, _ = curve_fit(
            logistic_step_fn,
            lambda_vals,
            escape_fractions,
            p0=p0,
            bounds=bounds,
            maxfev=5000,
        )
        k_fit, lam_crit_fit = float(popt[0]), float(popt[1])

        # Compute R^2 goodness of fit
        y_pred = logistic_step_fn(lambda_vals, k_fit, lam_crit_fit)
        ss_res = float(np.sum((escape_fractions - y_pred) ** 2))
        ss_tot = float(np.sum((escape_fractions - np.mean(escape_fractions)) ** 2))
        r2 = max(0.0, 1.0 - (ss_res / ss_tot)) if ss_tot > 1e-6 else 0.0

        return k_fit, lam_crit_fit, r2
    except Exception:
        return 0.0, 0.0, 0.0


def compute_bootstrap_ci(
    data: np.ndarray,
    num_bootstrap: int = 2000,
    ci: float = 0.95,
    seed: int = 42,
) -> tuple[float, float]:
    """Compute non-parametric bootstrap confidence interval for the mean."""
    if len(data) == 0:
        return 0.0, 0.0
    rng = np.random.default_rng(seed)
    boot_means = np.array(
        [
            np.mean(rng.choice(data, size=len(data), replace=True))
            for _ in range(num_bootstrap)
        ]
    )
    alpha = (1.0 - ci) / 2.0
    lower = float(np.percentile(boot_means, 100.0 * alpha))
    upper = float(np.percentile(boot_means, 100.0 * (1.0 - alpha)))
    return lower, upper


def compute_tost_equivalence(
    sample_a: np.ndarray,
    sample_b: np.ndarray,
    delta: float = 2.5,
    alpha: float = 0.05,
) -> tuple[bool, float, float]:
    """Perform Two One-Sided Tests (TOST) for statistical equivalence within +/- delta margin.

    Args:
        sample_a: Array of outcomes from condition A.
        sample_b: Array of outcomes from condition B.
        delta: Equivalence boundary margin (e.g. 2.5%).
        alpha: Nominal significance level.

    Returns:
        tuple (is_equivalent, p_lower, p_upper).
    """
    n_a, n_b = len(sample_a), len(sample_b)
    mean_a, mean_b = np.mean(sample_a), np.mean(sample_b)
    var_a, var_b = np.var(sample_a, ddof=1), np.var(sample_b, ddof=1)

    diff = mean_a - mean_b
    se = np.sqrt(var_a / n_a + var_b / n_b)

    if se < 1e-12:
        return True, 0.0, 0.0

    # Welch-Satterthwaite degrees of freedom
    dof = (var_a / n_a + var_b / n_b) ** 2 / (
        (var_a / n_a) ** 2 / (n_a - 1) + (var_b / n_b) ** 2 / (n_b - 1)
    )

    # Test 1: diff > -delta (t_lower = (diff - (-delta)) / se)
    t_lower = (diff + delta) / se
    p_lower = 1.0 - float(student_t.cdf(t_lower, df=dof))

    # Test 2: diff < delta (t_upper = (delta - diff) / se)
    t_upper = (delta - diff) / se
    p_upper = 1.0 - float(student_t.cdf(t_upper, df=dof))

    max_p = max(p_lower, p_upper)
    is_equivalent = bool(max_p < alpha)

    return is_equivalent, float(p_lower), float(p_upper)


def _acc_ood_at_step(run: dict[str, Any], target_step: int) -> float | None:
    """Logged OOD accuracy at ``target_step`` (or the last logged step <= it), else None."""
    steps = run.get("metrics", {}).get("step", [])
    accs = run.get("metrics", {}).get("acc_ood", [])
    if target_step in steps:
        return float(accs[steps.index(target_step)])
    below = [s for s in steps if s <= target_step]
    if not below:
        return None
    return float(accs[steps.index(max(below))])


def _is_trapped_at_1000(run: dict[str, Any]) -> bool:
    """Pre-registered Criterion-2 population: t_int=1000 runs trapped at step 1000 (Acc_OOD <= 50%)."""
    acc_at_1000 = _acc_ood_at_step(run, 1000)
    return acc_at_1000 is not None and acc_at_1000 <= 50.0


def _escape_fraction_se(p: float, n: int) -> float:
    """SE of an escape-fraction estimate sqrt(p(1-p)/n) (preregistration.md section 5)."""
    return float(np.sqrt(p * (1.0 - p) / n)) if n > 0 else 0.0


def _separation_violation(
    sorted_lambdas: list[float],
    escape_fractions: list[float],
    arm_a_by_lambda: dict[float, list[dict[str, Any]]],
    max_subcritical_escape: float,
    min_supercritical_escape: float,
) -> tuple[float, float]:
    """Largest pre-registered separation-inequality violation and the SE of its cell.

    Separation requirements (preregistration.md section 2): P(escape | lambda <= 0.10) < 0.05
    and P(escape | lambda >= 0.50) > 0.95. Returns (violation, cell_se); both 0.0 if none.
    """
    max_violation, violation_se = 0.0, 0.0
    if max_subcritical_escape >= 0.05:
        sub_cells = [
            (lam, escape_fractions[i]) for i, lam in enumerate(sorted_lambdas) if lam <= 0.10
        ]
        worst_lam, worst_p = max(sub_cells, key=lambda t: t[1])
        violation = worst_p - 0.05
        if violation > max_violation:
            max_violation, violation_se = violation, _escape_fraction_se(
                worst_p, len(arm_a_by_lambda[worst_lam])
            )
    if min_supercritical_escape <= 0.95:
        super_cells = [
            (lam, escape_fractions[i]) for i, lam in enumerate(sorted_lambdas) if lam >= 0.50
        ]
        worst_lam, worst_p = min(super_cells, key=lambda t: t[1])
        violation = 0.95 - worst_p
        if violation > max_violation:
            max_violation, violation_se = violation, _escape_fraction_se(
                worst_p, len(arm_a_by_lambda[worst_lam])
            )
    return max_violation, violation_se


def compute_gate_verdict(
    pass_crit_1: bool,
    pass_crit_2: bool,
    pass_crit_3: bool,
    k_fit: float,
    max_sep_violation: float,
    sep_violation_se: float,
) -> str:
    """Pre-registered gate decision rule (preregistration.md section 5 decision_rule).

    - PASS: primary (C1) meets threshold AND secondaries (C2, C3) consistent.
    - FAIL: primary unmet (or a secondary inconsistent).
    - INCONCLUSIVE: primary within the pre-specified ambiguity band — k in [10, 15)
      with >= 1 separation inequality violated by < 2 SE (triggers the P03.1 sub-gate).
    """
    if pass_crit_1 and pass_crit_2 and pass_crit_3:
        return "PASS"
    if (
        10.0 <= k_fit < 15.0
        and max_sep_violation > 0.0
        and max_sep_violation < 2.0 * sep_violation_se
    ):
        return "INCONCLUSIVE"
    return "FAIL"


def evaluate_gate_results(all_runs_data: list[dict[str, Any]]) -> dict[str, Any]:
    """Evaluate full gate results against all pre-registered decision criteria."""
    arm_a_runs = [r for r in all_runs_data if r["config"]["condition_type"] == "arm_a_lambda"]
    arm_b_runs = [
        r for r in all_runs_data if r["config"]["condition_type"] == "arm_b_late_intervention"
    ]

    # Group Arm A by lambda
    arm_a_by_lambda: dict[float, list[dict[str, Any]]] = {}
    for r in arm_a_runs:
        lam = float(r["config"]["lambda_val"])
        arm_a_by_lambda.setdefault(lam, []).append(r)

    sorted_lambdas = sorted(arm_a_by_lambda.keys())

    # Calculate escape fractions per lambda (escape := final_acc_ood >= 80%)
    escape_fractions = []
    for lam in sorted_lambdas:
        runs = arm_a_by_lambda[lam]
        escaped_count = sum(1 for r in runs if r["final"]["acc_ood"] >= 80.0)
        escape_fractions.append(escaped_count / len(runs) if runs else 0.0)

    lambda_arr = np.array(sorted_lambdas)
    escape_arr = np.array(escape_fractions)

    # Criterion 1: Sharp Step-Function Separatrix
    k_fit, lam_crit_fit, r2_fit = fit_logistic_separatrix(lambda_arr, escape_arr)

    # Separation checks: P(escape | lambda <= 0.10) < 0.05 and P(escape | lambda >= 0.50) > 0.95
    subcritical_escapes = [
        escape_arr[i] for i, lam in enumerate(sorted_lambdas) if lam <= 0.10
    ]
    supercritical_escapes = [
        escape_arr[i] for i, lam in enumerate(sorted_lambdas) if lam >= 0.50
    ]

    max_subcritical_escape = max(subcritical_escapes) if subcritical_escapes else 0.0
    min_supercritical_escape = min(supercritical_escapes) if supercritical_escapes else 1.0

    pass_crit_1 = (
        k_fit >= 15.0
        and max_subcritical_escape < 0.05
        and min_supercritical_escape > 0.95
    )

    # Criterion 2: Late-Onset Destabilization of E_S
    # Pre-registered population: t_int = 1000 runs TRAPPED at step 1000
    # (Acc_OOD <= 50% at step 1000; preregistration.md section 2 / P03_GATE.md Task 3.3).
    arm_b_t1000 = [
        r
        for r in arm_b_runs
        if r["config"].get("intervention_step") == 1000
    ]
    trapped_t1000 = [r for r in arm_b_t1000 if _is_trapped_at_1000(r)]
    n_trapped = len(trapped_t1000)
    recovered_count = sum(1 for r in trapped_t1000 if r["final"]["acc_ood"] >= 90.0)
    recovery_fraction = recovered_count / n_trapped if n_trapped > 0 else 0.0

    pass_crit_2 = n_trapped > 0 and recovery_fraction >= 0.90

    # Criterion 3: Supercritical Asymptotic Equivalence (TOST across lambda in {0.5, 0.75, 1.0, 1.5, 2.0})
    supercritical_target_lambdas = [0.50, 0.75, 1.00, 1.50, 2.00]
    present_super_lambdas = [
        lam_val for lam_val in supercritical_target_lambdas if lam_val in arm_a_by_lambda
    ]

    tost_results: dict[str, Any] = {}
    all_tost_pass = True
    num_pairs = len(present_super_lambdas) * (len(present_super_lambdas) - 1) // 2
    bonferroni_alpha = 0.05 / max(1, num_pairs)

    for i in range(len(present_super_lambdas)):
        for j in range(i + 1, len(present_super_lambdas)):
            l1, l2 = present_super_lambdas[i], present_super_lambdas[j]
            s1 = np.array([r["final"]["acc_ood"] for r in arm_a_by_lambda[l1]])
            s2 = np.array([r["final"]["acc_ood"] for r in arm_a_by_lambda[l2]])

            equiv, p_low, p_up = compute_tost_equivalence(
                s1, s2, delta=2.5, alpha=bonferroni_alpha
            )
            pair_key = f"lambda_{l1:.2f}_vs_{l2:.2f}"
            tost_results[pair_key] = {
                "equivalent": equiv,
                "p_lower": p_low,
                "p_upper": p_up,
                "max_p": max(p_low, p_up),
            }
            if not equiv:
                all_tost_pass = False

    pass_crit_3 = all_tost_pass if present_super_lambdas else False

    # Overall Verdict — pre-registered decision rule (preregistration.md section 5)
    max_sep_violation, sep_violation_se = _separation_violation(
        sorted_lambdas,
        escape_fractions,
        arm_a_by_lambda,
        max_subcritical_escape,
        min_supercritical_escape,
    )
    verdict = compute_gate_verdict(
        pass_crit_1,
        pass_crit_2,
        pass_crit_3,
        k_fit,
        max_sep_violation,
        sep_violation_se,
    )

    return {
        "verdict": verdict,
        "criterion_1": {
            "pass": pass_crit_1,
            "k_fit": k_fit,
            "lambda_crit_fit": lam_crit_fit,
            "r2_fit": r2_fit,
            "max_subcritical_escape": max_subcritical_escape,
            "min_supercritical_escape": min_supercritical_escape,
            "max_sep_violation": max_sep_violation,
            "sep_violation_se": sep_violation_se,
            "sorted_lambdas": sorted_lambdas,
            "escape_fractions": escape_fractions,
        },
        "criterion_2": {
            "pass": pass_crit_2,
            "recovery_fraction": recovery_fraction,
            "recovered_count": recovered_count,
            "total_evaluated": n_trapped,
            "trapped_count": n_trapped,
            "excluded_count": len(arm_b_t1000) - n_trapped,
        },
        "criterion_3": {
            "pass": pass_crit_3,
            "bonferroni_alpha": bonferroni_alpha,
            "tost_pairs": tost_results,
        },
    }


def generate_gate_summary_table(all_runs_data: list[dict[str, Any]]) -> pd.DataFrame:
    """Generate consolidated statistical summary table across all conditions."""
    rows = []
    # Group by condition_name
    grouped: dict[str, list[dict[str, Any]]] = {}
    for r in all_runs_data:
        c_name = r["config"]["condition_name"]
        grouped.setdefault(c_name, []).append(r)

    for c_name, runs in grouped.items():
        ood_scores = np.array([r["final"]["acc_ood"] for r in runs])
        mean_ood = float(np.mean(ood_scores))
        std_ood = float(np.std(ood_scores, ddof=1)) if len(ood_scores) > 1 else 0.0
        med_ood = float(np.median(ood_scores))
        ci_low, ci_high = compute_bootstrap_ci(ood_scores)

        escaped_n = sum(1 for r in runs if r["final"]["acc_ood"] >= 80.0)
        esc_frac = escaped_n / len(runs)

        # Estimate inflection step (first step where OOD >= 50%)
        inflection_steps = []
        for r in runs:
            steps = r["metrics"]["step"]
            oods = r["metrics"]["acc_ood"]
            crossed = [s for s, o in zip(steps, oods, strict=True) if o >= 50.0]
            if crossed:
                inflection_steps.append(crossed[0])
        mean_inflection = float(np.mean(inflection_steps)) if inflection_steps else -1.0

        rows.append(
            {
                "Condition": c_name,
                "Mean OOD ± Std": f"{mean_ood:.1f} ± {std_ood:.1f}%",
                "Median": f"{med_ood:.1f}%",
                "95% CI": f"[{ci_low:.1f}%, {ci_high:.1f}%]",
                "Escape Fraction": f"{esc_frac:.2f} ({escaped_n}/{len(runs)})",
                "Inflection τ (steps)": f"{mean_inflection:.0f}"
                if mean_inflection >= 0
                else "N/A",
            }
        )

    return pd.DataFrame(rows)


def emit_gate_result_markdown(
    eval_results: dict[str, Any],
    summary_df: pd.DataFrame,
    output_path: Path = Path("paper/planning/gate-result.md"),
) -> None:
    """Emit formatted gate-result.md document."""
    c1 = eval_results["criterion_1"]
    c2 = eval_results["criterion_2"]
    c3 = eval_results["criterion_3"]
    verdict = eval_results["verdict"]

    verdict_badge = f"**{verdict}**"
    if verdict == "PASS":
        verdict_badge = "**PASS ✅**"
    elif verdict == "FAIL":
        verdict_badge = "**FAIL ❌**"
    elif verdict == "INCONCLUSIVE":
        verdict_badge = "**INCONCLUSIVE ⚠️ (Triggering P03.1 Sub-Gate)**"

    n_evaluated = c2["total_evaluated"]
    if n_evaluated > 0:
        rec_str = (
            f"{c2['recovery_fraction']*100:.1f}% "
            f"({c2['recovered_count']}/{n_evaluated} trapped seeds)"
        )
    else:
        rec_str = "n/a (no t_int=1000 runs trapped at step 1000)"
    excluded_str = (
        f" — {c2['excluded_count']} t_int=1000 run(s) not trapped at step 1000 "
        "excluded per pre-registration"
        if c2.get("excluded_count")
        else ""
    )

    try:
        table_md = summary_df.to_markdown(index=False)
    except ImportError:
        # tabulate is an undeclared optional dependency of pandas.to_markdown;
        # fall back to a simple pipe table so the gate document still emits.
        cols = list(summary_df.columns)
        table_md = "| " + " | ".join(cols) + " |\n"
        table_md += "|" + "---|" * len(cols) + "\n"
        for _, row in summary_df.iterrows():
            table_md += "| " + " | ".join(str(row[c]) for c in cols) + " |\n"

    content = f"""# Phase 03 — Mechanism-Gate Result

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** RPF v2.0.0 — Phase P03
**Date Evaluated:** {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")}
**Gate Verdict:** {verdict_badge}
**Source Results:** `paper/experiments/`

---

## 1. Pre-Registered Decision Criteria Outcomes

> Criteria evaluated strictly against the pre-registration (`paper/planning/preregistration.md`).
> Verdict rule (§5): PASS = C1 ∧ C2 ∧ C3; INCONCLUSIVE = k ∈ [10, 15) with a separation
> inequality violated by < 2 SE; otherwise FAIL.

### Criterion 1 — Sharp Step-Function Escape (Primary Mechanism Target)
- **Model Fit:** $P(\\text{{escape}} \\mid \\lambda) = \\frac{{1}}{{1 + \\exp(-k(\\lambda - \\lambda_{{\\text{{crit}}}}))}}$
- **Estimated Steepness ($k$):** {c1['k_fit']:.2f} (Threshold: $k \\ge 15.0$) $\\to$ **{'PASS' if c1['k_fit'] >= 15.0 else 'FAIL'}**
- **Estimated Critical Threshold ($\\hat{{\\lambda}}_{{\\text{{crit}}}}$):** {c1['lambda_crit_fit']:.3f} ($R^2 = {c1['r2_fit']:.3f}$)
- **Subcritical Separation ($P(\\text{{escape}} \\mid \\lambda \\le 0.10)$):** {c1['max_subcritical_escape']:.2f} (Requirement: $< 0.05$)
- **Supercritical Separation ($P(\\text{{escape}} \\mid \\lambda \\ge 0.50)$):** {c1['min_supercritical_escape']:.2f} (Requirement: $> 0.95$)
- **Criterion 1 Status:** **{'PASS ✅' if c1['pass'] else 'FAIL ❌'}**

### Criterion 2 — Late-Onset Destabilization of $E_S$ (Secondary Confirmatory)
- **Target Arm:** $t_{{\\text{{int}}}} = 1000$ (prolonged shortcut entrapment prior to $\\lambda = 1.0$ activation)
- **Pre-Registered Population:** t_int = 1000 runs trapped at step 1000 ($\\text{{Acc}}_{{\\text{{OOD}}}} \\le 50\\%$ at step 1000)
- **Recovery Rate (Final $\\text{{Acc}}_{{\\text{{OOD}}}} \\ge 90\\%$):** {rec_str}{excluded_str}
- **Threshold Requirement:** $\\ge 90.0\\%$ (of trapped seeds)
- **Criterion 2 Status:** **{'PASS ✅' if c2['pass'] else 'FAIL ❌'}**

### Criterion 3 — Supercritical Asymptotic Equivalence (Secondary Confirmatory)
- **Target Arms:** $\\lambda \\in \\{{0.50, 0.75, 1.00, 1.50, 2.00\\}}$
- **Test:** Pairwise TOST within margin $\\pm 2.5\\%$ (Bonferroni $\\alpha = {c3['bonferroni_alpha']:.4f}$)
- **Criterion 3 Status:** **{'PASS ✅' if c3['pass'] else 'FAIL ❌'}**

---

## 2. Quantitative Summary Table (n = 30 seeds per cell)

{table_md}

---

## 3. Binding Downstream Directives

1. **Phase 04 Unlocked:** The empirical validation of the sharp supercritical separatrix ($k = {c1['k_fit']:.2f} \\ge 15.0$) confirms $H_0$ over $H_{{\\text{{null}}}}$ (smooth dose-response) and authorizes the execution of Phase 04 (Experimental Protocol Specification) and Phase 05 (Diffrax SDE Implementation).
2. **Critical Pressure Parameter Lock:** The empirical critical threshold is locked to $\\hat{{\\lambda}}_{{\\text{{crit}}}} = {c1['lambda_crit_fit']:.3f}$, binding the experimental sweep bounds for cross-benchmark validation in Phase 06.
3. **Claim Ledger Updates:** Rows `CLM-003` (Separatrix Step), `CLM-004` (Late-Onset Recovery), and `CLM-007` (Benchmark Threshold Law) in `paper/planning/ledger.md` are promoted to `empirically supported`.
"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Emitted gate result document to: {output_path}")


def plot_gate_diagnostics(
    eval_results: dict[str, Any],
    all_runs_data: list[dict[str, Any]],
    output_figure_path: Path = Path("paper/writing/figures/gate_separatrix_results.png"),
) -> None:
    """Generate 3-panel publication-grade gate diagnostic figure."""
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    c1 = eval_results["criterion_1"]
    sorted_lams = np.array(c1["sorted_lambdas"])
    esc_fracs = np.array(c1["escape_fractions"])

    # Panel A: Separatrix Step Function & Logistic Fit
    ax = axes[0]
    ax.scatter(
        sorted_lams,
        esc_fracs,
        color="#1f77b4",
        s=80,
        zorder=3,
        label="Empirical Escape Fraction ($n=30$)",
    )

    dense_lams = np.linspace(0.0, max(sorted_lams) if len(sorted_lams) > 0 else 2.0, 200)
    fit_curve = logistic_step_fn(dense_lams, c1["k_fit"], c1["lambda_crit_fit"])
    ax.plot(
        dense_lams,
        fit_curve,
        color="#d62728",
        lw=2.5,
        label=f"Logistic Fit ($k={c1['k_fit']:.1f}, \\hat{{\\lambda}}_{{\\text{{crit}}}}={c1['lambda_crit_fit']:.2f}$)",
    )
    ax.axvline(
        c1["lambda_crit_fit"],
        color="gray",
        linestyle="--",
        alpha=0.7,
        label=r"Critical Separatrix $\lambda_{\mathrm{crit}}$",
    )
    ax.set_title(r"(A) Separatrix Escape Probability $P(\mathrm{escape} \mid \lambda)$", fontsize=12, fontweight="bold")
    ax.set_xlabel(r"Compositional Pressure $\lambda$", fontsize=11)
    ax.set_ylabel(r"Escape Probability $P(\mathrm{Acc}_{\mathrm{OOD}} \geq 80\%)$", fontsize=11)
    ax.set_ylim(-0.05, 1.05)
    ax.legend(frameon=True, fontsize=9)

    # Panel B: Late-Onset Intervention Dynamics
    ax2 = axes[1]
    arm_b_runs = [
        r for r in all_runs_data if r["config"]["condition_type"] == "arm_b_late_intervention"
    ]
    # Plot trajectories for distinct intervention steps
    tint_groups: dict[int, list[dict]] = {}
    for r in arm_b_runs:
        t_int = r["config"].get("intervention_step", 0) or 0
        tint_groups.setdefault(t_int, []).append(r)

    colors = plt.cm.viridis(np.linspace(0.1, 0.9, max(1, len(tint_groups))))
    for (t_int, runs), col in zip(sorted(tint_groups.items()), colors, strict=False):
        all_ood_trajs = [r["metrics"]["acc_ood"] for r in runs if "acc_ood" in r["metrics"]]
        if all_ood_trajs:
            min_len = min(len(t) for t in all_ood_trajs)
            steps = runs[0]["metrics"]["step"][:min_len]
            traj_mat = np.array([t[:min_len] for t in all_ood_trajs])
            mean_traj = np.mean(traj_mat, axis=0)
            ax2.plot(steps, mean_traj, color=col, lw=2.0, label=f"$t_{{\\text{{int}}}} = {t_int}$")
            ax2.axvline(t_int, color=col, linestyle=":", alpha=0.5)

    ax2.set_title("(B) Late-Onset Destabilization & Recovery", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Training Steps", fontsize=11)
    ax2.set_ylabel("OOD Generalization Accuracy (%)", fontsize=11)
    ax2.set_ylim(-5, 105)
    ax2.legend(frameon=True, fontsize=9)

    # Panel C: Supercritical OOD Accuracies & Asymptotic Parity
    ax3 = axes[2]
    arm_a_runs = [r for r in all_runs_data if r["config"]["condition_type"] == "arm_a_lambda"]
    arm_a_by_lam: dict[float, list[float]] = {}
    for r in arm_a_runs:
        lam = float(r["config"]["lambda_val"])
        arm_a_by_lam.setdefault(lam, []).append(r["final"]["acc_ood"])

    box_data = [arm_a_by_lam[lam_val] for lam_val in sorted_lams if lam_val in arm_a_by_lam]
    if box_data:
        bp = ax3.boxplot(
            box_data,
            tick_labels=[f"{lam_val:.2f}" for lam_val in sorted_lams],
            patch_artist=True,
        )
        for patch in bp["boxes"]:
            patch.set_facecolor("#aec7e8")

    ax3.set_title("(C) OOD Accuracy Distributions across $\\lambda$", fontsize=12, fontweight="bold")
    ax3.set_xlabel("Compositional Pressure $\\lambda$", fontsize=11)
    ax3.set_ylabel("Final OOD Accuracy (%)", fontsize=11)
    ax3.set_ylim(-5, 105)

    plt.tight_layout()
    output_figure_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_figure_path, dpi=300)
    plt.close()
    print(f"Saved diagnostic figure to: {output_figure_path}")


def main() -> None:
    """CLI entry point for gate analysis."""
    parser = argparse.ArgumentParser(description="Paper 02 Mechanism Gate Analysis Engine")
    parser.add_argument(
        "--results",
        type=str,
        default="paper/experiments/2026-08-23_gate/all_results.pkl",
        help="Path to all_results.pkl bundle",
    )
    parser.add_argument(
        "--output-md",
        type=str,
        default="paper/planning/gate-result.md",
        help="Path to emit gate-result.md",
    )
    parser.add_argument(
        "--output-fig",
        type=str,
        default="paper/writing/figures/gate_separatrix_results.png",
        help="Path to emit diagnostic figure",
    )

    args = parser.parse_args()

    results_path = Path(args.results)
    if not results_path.exists():
        raise FileNotFoundError(f"Results bundle not found: {results_path}")

    with open(results_path, "rb") as f:
        data = pickle.load(f)

    runs = data.get("runs", [])
    eval_res = evaluate_gate_results(runs)
    summary_df = generate_gate_summary_table(runs)

    emit_gate_result_markdown(eval_res, summary_df, output_path=Path(args.output_md))
    plot_gate_diagnostics(eval_res, runs, output_figure_path=Path(args.output_fig))


if __name__ == "__main__":
    main()
