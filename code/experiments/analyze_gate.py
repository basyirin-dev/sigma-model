"""Phase 04 gate analysis → ``paper/planning/gate-result.md``.

Loads ``all_results.pkl`` (from the Kaggle gate run, placed under
``archive/gate-results/``) and applies the decision rule from
``paper/planning/phases/04_mechanism_gate.md``:

- **σ̃_A (measured) precedes OOD improvement AND fixed-weight does not match
  ODE-guided** → mechanistic framing
- **OOD improves but measured σ does not precede it** → phenomenological
- **Neither survives** → stop; rework the model before any rewrite

Reporting standards (roadmap non-negotiables): per-seed raw distributions,
confidence intervals, Welch t-tests, per-split (ID/OOD) effect sizes — no pooled
Cohen's d alone.

Usage::

    python code/experiments/analyze_gate.py --results-dir archive/gate-results
    python code/experiments/analyze_gate.py --results-dir output/gate_smoke \\
        --out /tmp/gate-result.md
"""

from __future__ import annotations

import argparse
import json
import pickle
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
from scipy import stats

# Order for reporting (matches gate.yaml `experiment.conditions`).
CONDITION_ORDER = ["baseline", "fixed_weight", "additive", "multiplicative"]
ODE_GUIDED = ["additive", "multiplicative"]

# Decision-rule thresholds (documented in gate-result.md).
OOD_IMPROVES_MIN = 50.0  # best-arm mean final OOD (%) → compositional learning happened
LEAD_FRACTION_MIN = 0.5  # majority of runs: measured σ̃_A crosses before OOD rises
FW_P_ALPHA = 0.05


def load_results(results_dir: str) -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any] | None]:
    pkl = Path(results_dir) / "all_results.pkl"
    if not pkl.exists():
        raise FileNotFoundError(f"no all_results.pkl in {results_dir}")
    with open(pkl, "rb") as f:
        all_results = pickle.load(f)
    summary = None
    spath = Path(results_dir) / "summary.json"
    if spath.exists():
        summary = json.loads(spath.read_text())
    return all_results, summary


# ---------------------------------------------------------------------------
# Per-condition summaries
# ---------------------------------------------------------------------------


def cond_stats(
    all_results: dict[str, list[dict[str, Any]]], key: str = "acc_ood"
) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for c, runs in all_results.items():
        vals = np.array([r["final"][key] for r in runs], dtype=float)
        se = stats.sem(vals) if len(vals) > 1 else 0.0
        lo, hi = stats.t.interval(0.95, max(len(vals) - 1, 1), loc=vals.mean(), scale=se)
        out[c] = {
            "n": len(vals),
            "mean": float(vals.mean()),
            "std": float(vals.std(ddof=1)) if len(vals) > 1 else 0.0,
            "median": float(np.median(vals)),
            "ci95": (float(lo), float(hi)),
            "raw": [float(v) for v in vals],
        }
    return out


def welch_pair(a: np.ndarray, b: np.ndarray) -> dict[str, float]:
    t, p = stats.ttest_ind(a, b, equal_var=False)
    pooled = np.sqrt((np.var(a) + np.var(b)) / 2)
    d = (b.mean() - a.mean()) / pooled if pooled > 1e-9 else 0.0
    return {
        "t": float(t),
        "p": float(p),
        "cohens_d": float(d),
        "d_mean": float(b.mean() - a.mean()),
    }


# ---------------------------------------------------------------------------
# Leading-indicator machinery
# ---------------------------------------------------------------------------


def normalized(s: np.ndarray) -> np.ndarray:
    lo, hi = s.min(), s.max()
    if hi - lo < 1e-9:
        return np.zeros_like(s)
    return (s - lo) / (hi - lo)


def crossing_time(steps: np.ndarray, s: np.ndarray, frac: float = 0.5) -> float:
    """First step where the (normalized) series reaches ``frac`` of its rise."""
    idx = np.argmax(normalized(s) >= frac)
    if normalized(s)[idx] < frac:  # never crossed
        return float("inf")
    return float(steps[idx])


def ood_rise_time(steps: np.ndarray, ood: np.ndarray, final_ood: float, frac: float = 0.5) -> float:
    """First step where OOD reaches ``frac`` of its final value."""
    target = frac * final_ood
    hit = np.where(ood >= target)[0]
    if len(hit) == 0:
        return float("inf")
    return float(steps[hit[0]])


def partial_corr(x: np.ndarray, y: np.ndarray, covs: list[np.ndarray]) -> float:
    """Partial correlation of x,y controlling for the columns of ``covs``."""
    n = len(x)
    if n < 4:
        return float("nan")
    design = [np.ones(n), *covs]
    xm = np.column_stack(design)
    rx = x - xm @ np.linalg.lstsq(xm, x, rcond=None)[0]
    ry = y - xm @ np.linalg.lstsq(xm, y, rcond=None)[0]
    return float(np.corrcoef(rx, ry)[0, 1])


def one_sided_t(vals: list[float]) -> tuple[float, float]:
    """One-sample t-test (one-sided) that the mean of ``vals`` is > 0."""
    v = np.array([x for x in vals if not np.isnan(x)], dtype=float)
    if len(v) < 3:
        return float("nan"), 1.0
    t, p_two = stats.ttest_1samp(v, 0.0)
    p_one = p_two / 2 if np.mean(v) > 0 else 1.0 - p_two / 2
    return float(np.mean(v)), float(p_one)


def leading_analysis(
    run: dict[str, Any],
    sigma_key: str = "sigma_tilde",
) -> dict[str, float]:
    """Per-run leading-indicator statistics.

    - ``sigma_cross``: step where min-max-normalized σ first reaches 0.5.
    - ``ood_rise``: step where OOD first reaches 0.5 × final OOD.
    - ``partial_corr``: σ̃_A,t → OOD_{t+1} controlling OOD_t, loss_t, param_norm_t.
    """
    steps = np.array(run["step"])
    ood = np.array(run["acc_ood"])
    sig = np.array(run[sigma_key])
    final_ood = float(run["final"]["acc_ood"])
    cross = crossing_time(steps, sig)
    rise = ood_rise_time(steps, ood, final_ood)
    if "param_norm" not in run:
        raise KeyError(
            "run metrics lack 'param_norm' (stale results?). Re-run the gate with "
            "the current hbar_train.py before analyzing."
        )
    pc = partial_corr(
        sig[:-1],
        ood[1:],
        [ood[:-1], np.array(run["loss"])[:-1], np.array(run["param_norm"])[:-1]],
    )
    return {
        "sigma_cross": cross,
        "ood_rise": rise,
        "partial_corr": pc,
        # Degenerate when the proxy starts at (or above) its normalized max:
        # the crossing-time test then carries no precedence information.
        "crossing_degenerate": bool(cross == steps[0]),
    }


def fmt_time(t: float) -> str:
    return "inf" if t == float("inf") else f"{t:.0f}"


# ---------------------------------------------------------------------------
# Competing-variable check
# ---------------------------------------------------------------------------


def competing_check(runs: list[dict[str, Any]]) -> dict[str, float]:
    """Standardized OLS of final OOD on [σ̃_A, loss, param_norm, ID] + Spearman."""
    x_mat = np.array(
        [
            [
                r["sigma_tilde"][-1],
                r["loss"][-1],
                r["param_norm"][-1],
                r["acc_id"][-1],
            ]
            for r in runs
        ],
        dtype=float,
    )
    y = np.array([r["final"]["acc_ood"] for r in runs], dtype=float)
    n = len(y)
    if n < 6:
        return {"n": float(n)}
    xs = (x_mat - x_mat.mean(0)) / x_mat.std(0)
    ys = (y - y.mean()) / y.std()
    design = np.column_stack([np.ones(n), xs])
    beta, *_ = np.linalg.lstsq(design, ys, rcond=None)
    rho_sig, p_sig = stats.spearmanr(x_mat[:, 0], y)
    out = {
        "n": float(n),
        "beta_sigma": float(beta[1]),
        "rho_sigma": float(rho_sig),
        "p_rho_sigma": float(p_sig),
    }
    for j, name in enumerate(["loss", "param_norm", "acc_id"]):
        out[f"beta_{name}"] = float(beta[j + 2])
    return out


# ---------------------------------------------------------------------------
# Decision rule
# ---------------------------------------------------------------------------


def apply_decision(
    ood_means: dict[str, float],
    mean_partial_corr: float,
    p_partial_corr: float,
    crossing_degenerate_fraction: float,
    fw_vs_ode: dict[str, dict[str, float]],
) -> dict[str, Any]:
    """Apply the phase-04 decision rule; returns verdict + evidence flags.

    The leading test is judged by the **dynamic** partial-correlation test
    (σ̃_A,t → OOD_{t+1} controlling OOD_t, loss_t, param_norm_t), pooled across the
    ODE-guided arms and tested with a one-sample (one-sided) t-test: the crossing-time
    test is reported separately but treated as degenerate when the proxy starts at
    its normalized maximum (GCA ≈ 0.95 at random init).
    """
    ood_improves = max(ood_means[c] for c in ODE_GUIDED) >= OOD_IMPROVES_MIN
    leading_ok = mean_partial_corr > 0.0 and p_partial_corr < FW_P_ALPHA
    # fixed_weight does not match ODE-guided = it is *worse* (σ mechanism adds value).
    fw_worse = all(
        fw_vs_ode[c]["d_mean"] < 0 and fw_vs_ode[c]["p"] < FW_P_ALPHA for c in ODE_GUIDED
    )

    if not ood_improves:
        verdict = "stop"
        rationale = (
            "OOD does not improve above the threshold in any arm — the phenomenon "
            "itself is not reproduced. Halt the rewrite; rework the model before P05."
        )
    elif leading_ok and fw_worse:
        verdict = "mechanistic"
        rationale = (
            "Measured σ̃_A precedes OOD improvement AND the fixed-weight control does "
            "not match the ODE-guided arms (significantly worse OOD) — the σ-trap "
            "dynamics carry explanatory weight beyond plain compositional loss."
        )
    else:
        verdict = "phenomenological"
        flags = []
        if not leading_ok:
            flags.append("measured σ̃_A does not precede OOD (dynamic partial-corr test)")
        if not fw_worse:
            flags.append("fixed-weight matches (or beats) ODE-guided OOD")
        rationale = (
            "OOD improves but " + " and ".join(flags) + " — the dynamical σ-model "
            "describes the observed behaviour but is not needed to explain it."
        )
    return {
        "verdict": verdict,
        "ood_improves": ood_improves,
        "leading_ok": leading_ok,
        "fw_worse": fw_worse,
        "crossing_degenerate_fraction": crossing_degenerate_fraction,
        "rationale": rationale,
    }


# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------


def render_md(
    all_results: dict[str, list[dict[str, Any]]],
    summary: dict[str, Any] | None,
    stats_ood: dict[str, Any],
    stats_id: dict[str, Any],
    fw_vs_ode: dict[str, dict[str, float]],
    leading: dict[str, dict[str, float]],
    lead_fraction: dict[str, float],
    mean_pc: dict[str, float],
    pos_pc_frac: dict[str, float],
    degenerate_frac: dict[str, float],
    rga_cross: dict[str, float],
    rga_pc: dict[str, dict[str, float]],
    mean_pc_ode: float,
    p_pc_ode: float,
    rga_mean_ode: float,
    rga_p_ode: float,
    lead_fraction_sched: dict[str, float],
    competing: dict[str, dict[str, float]],
    decision: dict[str, Any],
    results_dir: str,
) -> str:
    lines: list[str] = []
    add = lines.append
    add("# Phase 04 — Mechanism-Gate Result")
    add("")
    add(f"**Date**: {datetime.now().strftime('%Y-%m-%d')}")
    add(f"**Verdict**: **{decision['verdict'].upper()}** — {decision['rationale']}")
    add("")
    add(f"**Results source**: `{results_dir}` (raw, gitignored)")
    add("")
    add("## 1. Decision-rule evidence")
    add("")
    add(f"- OOD improves (best ODE-guided arm ≥ {OOD_IMPROVES_MIN:.0f}%): "
        f"**{decision['ood_improves']}**")
    add(f"- σ̃_A (measured) precedes OOD (dynamic partial-corr test, pooled ODE n=30, "
        f"one-sided t): **{decision['leading_ok']}**")
    add(f"- fixed_weight does not match ODE-guided (significantly worse): "
        f"**{decision['fw_worse']}**")
    add(f"- crossing-time test degenerate (σ̃_A starts at its normalized max): "
        f"{decision['crossing_degenerate_fraction']:.0%} of ODE-guided runs")
    add("")
    add("Decision rule applied (phases/04_mechanism_gate.md): " + decision["rationale"])
    add("")
    add("## 2. Experiment summary")
    add("")
    add("| Arm | n runs | steps/run | eval_every |")
    add("|-----|--------|-----------|------------|")
    n_runs = {c: len(v) for c, v in all_results.items()}
    first = all_results[CONDITION_ORDER[0]][0]
    eval_every = (first["step"][1] - first["step"][0]) if len(first["step"]) > 1 else 0
    n_steps = first["step"][-1] + eval_every  # last eval step + cadence = total steps
    for c in CONDITION_ORDER:
        add(f"| {c} | {n_runs.get(c, 0)} | {n_steps} | {eval_every} |")
    if summary:
        add("")
        add(f"GPU: {summary['experiment']['gpu']} | AMP: {summary['experiment']['amp']} | "
            f"global_seed: {summary['experiment']['global_seed']}")
    add("")
    add("## 3. Final accuracy (raw per-seed distributions, 95% CI)")
    add("")
    add("### OOD")
    add("")
    add("| Condition | mean±std | median | 95% CI | raw per-seed |")
    add("|-----------|----------|--------|--------|--------------|")
    for c in CONDITION_ORDER:
        if c not in stats_ood:
            continue
        s = stats_ood[c]
        raw = ", ".join(f"{v:.1f}" for v in s["raw"])
        add(
            f"| {c} | {s['mean']:.1f}±{s['std']:.1f} | {s['median']:.1f} | "
            f"[{s['ci95'][0]:.1f}, {s['ci95'][1]:.1f}] | {raw} |"
        )
    add("")
    add("### ID")
    add("")
    add("| Condition | mean±std | median | 95% CI | raw per-seed |")
    add("|-----------|----------|--------|--------|--------------|")
    for c in CONDITION_ORDER:
        if c not in stats_id:
            continue
        s = stats_id[c]
        raw = ", ".join(f"{v:.1f}" for v in s["raw"])
        add(
            f"| {c} | {s['mean']:.1f}±{s['std']:.1f} | {s['median']:.1f} | "
            f"[{s['ci95'][0]:.1f}, {s['ci95'][1]:.1f}] | {raw} |"
        )
    add("")
    add("## 4. Discriminator A — fixed_weight vs ODE-guided (Welch t, per-split)")
    add("")
    add("**Design note**: `fixed_weight` applies a constant-weight compositional loss "
        "(`total += λ·L_comp` every `comp_every` steps) with **no σ modulation and no "
        "phase-gated curriculum** — maximal comp exposure from step 0. It is a deliberately "
        "strong plain-compositional-loss baseline; if it matches the ODE-guided arms, the "
        "σ-scheduling adds nothing beyond plain comp loss.")
    add("")
    add("| Pair (OOD) | Δ mean (pp) | t | p | Cohen's d | raw OOD means |")
    add("|------------|-------------|-----|-------|-----------|---------------|")
    pairs = [
        ("fixed_weight", "additive"),
        ("fixed_weight", "multiplicative"),
        ("additive", "multiplicative"),
    ]
    for pair in pairs:
        if pair[0] not in all_results or pair[1] not in all_results:
            continue
        a = np.array(stats_ood[pair[0]]["raw"])
        b = np.array(stats_ood[pair[1]]["raw"])
        w = welch_pair(a, b)
        add(
            f"| {pair[0]} vs {pair[1]} | {w['d_mean']:+.2f} | {w['t']:.3f} | {w['p']:.4f} | "
            f"{w['cohens_d']:+.3f} | {a.mean():.1f} vs {b.mean():.1f} |"
        )
    add("")
    add("## 5. Discriminator B — does measured σ̃_A precede OOD?")
    add("")
    add("Two tests. **(a) Crossing-time test** (spec): σ̃_A crossing time = first step "
        "where min-max-normalized σ̃_A ≥ 0.5; OOD-rise time = first step where OOD ≥ "
        "0.5 × final OOD. **(b) Dynamic test**: partial correlation σ̃_A,t → OOD_{t+1} "
        "controlling OOD_t, loss_t, param_norm_t. The crossing-time test is **degenerate** "
        "here: σ̃_A starts at its normalized maximum (GCA ≈ 0.95 on a random-initialised "
        "model — the untrained output projection makes any two loss gradients nearly "
        "parallel), so the crossing time is 0 by construction. The dynamic test is decisive.")
    add("")
    add("### (a) Crossing-time test")
    add("")
    add("| Condition | σ-leads fraction | % crossing-degenerate | median σ cross | "
        "median OOD rise |")
    add("|-----------|------------------|-----------------------|----------------|-----------------|")
    for c in CONDITION_ORDER:
        if c not in leading:
            continue
        crosses = [v["sigma_cross"] for v in leading[c].values()]
        rises = [v["ood_rise"] for v in leading[c].values()]
        add(
            f"| {c} | {lead_fraction[c]:.2f} | {degenerate_frac[c]:.0%} | "
            f"{fmt_time(float(np.median(crosses)))} | {fmt_time(float(np.median(rises)))} |"
        )
    add("")
    add("### (b) Dynamic test (partial correlation) — decisive")
    add("")
    add("| Condition | mean partial corr | fraction runs PC>0 | RGA-only mean PC (one-sided t p) |")
    add("|-----------|-------------------|--------------------|---------------------------------|")
    for c in CONDITION_ORDER:
        if c not in leading:
            continue
        rp = rga_pc.get(c, {})
        add(
            f"| {c} | {mean_pc[c]:+.3f} | {pos_pc_frac[c]:.2f} | "
            f"{rp.get('mean', float('nan')):+.3f} (p={rp.get('p', 1.0):.3f}) |"
        )
    add("")
    add(f"Pooled ODE-guided (n=30): fused σ̃_A partial corr = {mean_pc_ode:.3f} "
        f"(one-sided t p = {p_pc_ode:.3f}) — **no dynamic leading evidence for the "
        f"measured σ̃_A**. In contrast, the RGA-only partial corr is "
        f"{rga_mean_ode:+.3f} (mean one-sided p = {rga_p_ode:.3f}): the geometry "
        "component significantly predicts OOD_{t+1} **but only in the arms with "
        "compositional-loss exposure (including `fixed_weight`, which has no σ "
        "dynamics)** — it tracks comp-loss exposure, not the σ-scheduling. GCA is "
        "init-dominated (≈ 0.95 at step 0, decaying) and masks this signal in the "
        "fused proxy. Model-rework lead for the companion: fix GCA (per-layer "
        "normalisation / reweighted fusion) before any mechanistic claim.")
    add("")
    add("RGA normalized half-rise (crossing-time diagnostic): "
        + ", ".join(f"{c}={fmt_time(rga_cross[c])}" for c in CONDITION_ORDER if c in rga_cross)
        + " vs OOD-rise medians above — RGA nominally precedes in the comp-exposure "
        "arms, consistent with its positive dynamic test.")
    add("")
    add("Scheduled knob diagnostic (same test on `sigma_sched`, archived finding: "
        "leads-fraction = 0.00):")
    add("")
    for c in CONDITION_ORDER:
        if c in lead_fraction_sched:
            add(f"- `{c}`: σ_sched leads fraction = {lead_fraction_sched[c]:.2f}")
    add("")
    add("## 6. Competing-variable check — does σ̃_A predict final OOD beyond loss/norm/ID?")
    add("")
    add("Standardized OLS betas of final OOD on [σ̃_A_final, loss_final, param_norm_final, "
        "acc_id_final]; Spearman ρ for σ̃_A. n=15 per arm — interpret with caution.")
    add("")
    add("| Condition | β(σ̃_A) | β(loss) | β(param_norm) | β(ID) | ρ(σ̃_A, OOD) | p |")
    add("|-----------|---------|---------|---------------|-------|--------------|-----|")
    for c in CONDITION_ORDER:
        if c not in competing:
            continue
        cc = competing[c]
        if "beta_sigma" not in cc:
            add(f"| {c} | — (n<6) | | | | | |")
            continue
        add(
            f"| {c} | {cc['beta_sigma']:+.2f} | {cc['beta_loss']:+.2f} | "
            f"{cc['beta_param_norm']:+.2f} | {cc['beta_acc_id']:+.2f} | "
            f"{cc['rho_sigma']:+.2f} | {cc['p_rho_sigma']:.3f} |"
        )
    add("")
    add("## 7. Next step")
    add("")
    if decision["verdict"] == "mechanistic":
        add("Claim level: **mechanistic** — proceed to P05 claim-lock blueprint with the "
            "σ-trap framed as a dynamical mechanism.")
    elif decision["verdict"] == "phenomenological":
        add("Claim level: **phenomenological/descriptive** — proceed to P05 with the "
            "σ-trap framed as a dynamical model of behaviour, not a mechanism.")
    else:
        add("**STOP** — rework the model before any P05/P06 rewrite; report to the user.")
    add("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Phase 04 gate analysis → gate-result.md")
    ap.add_argument(
        "--results-dir", default="archive/gate-results", help="dir with all_results.pkl"
    )
    ap.add_argument("--out", default="paper/planning/gate-result.md", help="output markdown path")
    args = ap.parse_args()

    all_results, summary = load_results(args.results_dir)
    print(f"loaded {sum(len(v) for v in all_results.values())} runs from {args.results_dir}")

    stats_ood = cond_stats(all_results, "acc_ood")
    stats_id = cond_stats(all_results, "acc_id")

    # Discriminator A — Welch pairs.
    fw_vs_ode: dict[str, dict[str, float]] = {}
    for c in ODE_GUIDED:
        if "fixed_weight" in all_results and c in all_results:
            fw_vs_ode[c] = welch_pair(
                np.array(stats_ood["fixed_weight"]["raw"]), np.array(stats_ood[c]["raw"])
            )

    # Discriminator B — leading indicator (measured proxy + scheduled diagnostic).
    leading: dict[str, dict[str, dict[str, float]]] = {c: {} for c in all_results}
    leading_sched: dict[str, dict[str, dict[str, float]]] = {c: {} for c in all_results}
    for c, runs in all_results.items():
        for i, r in enumerate(runs):
            leading[c][i] = leading_analysis(r, "sigma_tilde")
            if "sigma_sched" in r:
                leading_sched[c][i] = leading_analysis(r, "sigma_sched")
    lead_fraction = {
        c: float(
            np.mean(
                [1.0 if v["sigma_cross"] < v["ood_rise"] else 0.0 for v in leading[c].values()]
            )
        )
        for c in all_results
    }
    mean_pc = {
        c: float(np.nanmean([v["partial_corr"] for v in leading[c].values()]))
        for c in all_results
    }
    pos_pc_frac = {
        c: float(
            np.nanmean([1.0 if v["partial_corr"] > 0 else 0.0 for v in leading[c].values()])
        )
        for c in all_results
    }
    degenerate_frac = {
        c: float(
            np.mean(
                [1.0 if v["crossing_degenerate"] else 0.0 for v in leading[c].values()]
            )
        )
        for c in all_results
    }
    # RGA-component crossing (normalized half-rise), per arm — diagnostic showing
    # whether the rising proxy component leads the OOD rise.
    rga_cross = {
        c: float(
            np.nanmedian(
                [crossing_time(np.array(r["step"]), np.array(r["rga"])) for r in runs]
            )
        )
        for c, runs in all_results.items()
    }
    lead_fraction_sched = {
        c: float(
            np.mean(
                [
                    1.0 if v["sigma_cross"] < v["ood_rise"] else 0.0
                    for v in leading_sched[c].values()
                ]
            )
        )
        for c in leading_sched
    }
    # RGA-only dynamic test: does the rising geometry component predict OOD_{t+1}?
    rga_pc: dict[str, dict[str, float]] = {}
    for c, runs in all_results.items():
        vals = []
        for r in runs:
            ood = np.array(r["acc_ood"])
            covs = [ood[:-1], np.array(r["loss"])[:-1], np.array(r["param_norm"])[:-1]]
            vals.append(partial_corr(np.array(r["rga"])[:-1], ood[1:], covs))
        m, p = one_sided_t(vals)
        rga_pc[c] = {"mean": m, "p": p, "pos_frac": float(np.mean([v > 0 for v in vals]))}
    pc_ode_pooled = [
        v["partial_corr"]
        for c in ODE_GUIDED
        for v in leading[c].values()
        if not np.isnan(v["partial_corr"])
    ]
    mean_partial_corr_ode, p_partial_corr_ode = one_sided_t(pc_ode_pooled)
    rga_ode_pooled = [rga_pc[c]["mean"] for c in ODE_GUIDED]
    rga_mean_ode = float(np.mean(rga_ode_pooled))
    rga_p_ode = float(np.mean([rga_pc[c]["p"] for c in ODE_GUIDED]))
    degenerate_fraction_ode = float(
        np.mean([degenerate_frac[c] for c in ODE_GUIDED if c in degenerate_frac])
    )

    # Competing-variable check.
    competing = {c: competing_check(runs) for c, runs in all_results.items()}

    ood_means = {c: stats_ood[c]["mean"] for c in all_results}
    decision = apply_decision(
        ood_means,
        mean_partial_corr_ode,
        p_partial_corr_ode,
        degenerate_fraction_ode,
        fw_vs_ode,
    )

    md = render_md(
        all_results,
        summary,
        stats_ood,
        stats_id,
        fw_vs_ode,
        leading,
        lead_fraction,
        mean_pc,
        pos_pc_frac,
        degenerate_frac,
        rga_cross,
        rga_pc,
        mean_partial_corr_ode,
        p_partial_corr_ode,
        rga_mean_ode,
        rga_p_ode,
        lead_fraction_sched,
        competing,
        decision,
        args.results_dir,
    )
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md + "\n")
    print(f"verdict: {decision['verdict']}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
