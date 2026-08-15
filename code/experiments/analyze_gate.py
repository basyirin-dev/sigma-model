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
    return {"sigma_cross": cross, "ood_rise": rise, "partial_corr": pc}


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
    lead_fraction_ode: float,
    mean_partial_corr: float,
    fw_vs_ode: dict[str, dict[str, float]],
) -> dict[str, Any]:
    """Apply the phase-04 decision rule; returns verdict + evidence flags."""
    ood_improves = max(ood_means[c] for c in ODE_GUIDED) >= OOD_IMPROVES_MIN
    leading_ok = lead_fraction_ode >= LEAD_FRACTION_MIN and mean_partial_corr > 0.0
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
            flags.append("measured σ̃_A does not precede OOD improvement")
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
    add(f"- σ̃_A (measured) precedes OOD: **{decision['leading_ok']}**")
    add(f"- fixed_weight does not match ODE-guided (significantly worse): "
        f"**{decision['fw_worse']}**")
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
    add("Per run: σ̃_A crossing time = first step where min-max-normalized σ̃_A ≥ 0.5; "
        "OOD-rise time = first step where OOD ≥ 0.5 × final OOD. Partial correlation: "
        "σ̃_A,t → OOD_{t+1} controlling OOD_t, loss_t, param_norm_t.")
    add("")
    add("| Condition | σ-leads fraction | mean partial corr | median σ cross | median OOD rise |")
    add("|-----------|------------------|-------------------|----------------|-----------------|")
    for c in CONDITION_ORDER:
        if c not in leading:
            continue
        crosses = [v["sigma_cross"] for v in leading[c].values()]
        rises = [v["ood_rise"] for v in leading[c].values()]
        add(
            f"| {c} | {lead_fraction[c]:.2f} | {mean_pc[c]:+.3f} | "
            f"{fmt_time(float(np.median(crosses)))} | {fmt_time(float(np.median(rises)))} |"
        )
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
    lead_fraction_ode = float(np.mean([lead_fraction[c] for c in ODE_GUIDED if c in lead_fraction]))
    mean_partial_corr_ode = float(np.nanmean([mean_pc[c] for c in ODE_GUIDED if c in mean_pc]))

    # Competing-variable check.
    competing = {c: competing_check(runs) for c, runs in all_results.items()}

    ood_means = {c: stats_ood[c]["mean"] for c in all_results}
    decision = apply_decision(ood_means, lead_fraction_ode, mean_partial_corr_ode, fw_vs_ode)

    md = render_md(
        all_results,
        summary,
        stats_ood,
        stats_id,
        fw_vs_ode,
        leading,
        lead_fraction,
        mean_pc,
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
