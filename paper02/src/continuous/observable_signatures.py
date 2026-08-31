"""Observable Dynamical Signatures for Paper 02 Transcritical Bifurcation.

This module simulates and visualizes the three primary empirical signatures predicting the
critical compositional pressure law:
    - Signature 1 (Separatrix): Step-function escape probability P(escape | lambda).
    - Signature 2 (Late-Onset Destabilization): Supercritical intervention rescue after entrapment.
    - Signature 3 (Rate Ordering & Critical Slowing Down): Monotonic scaling tau(lambda) ~ (lambda - lambda_crit)^(-1).
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np

try:
    from paper02.src.continuous.two_subspace_ode import (
        TwoSubspaceParams,
        TwoSubspaceSystem,
    )
except ImportError:
    import sys

    # Add workspace root to sys.path
    _workspace_root = str(Path(__file__).resolve().parents[3])
    if _workspace_root not in sys.path:
        sys.path.insert(0, _workspace_root)
    try:
        from paper02.src.continuous.two_subspace_ode import (
            TwoSubspaceParams,
            TwoSubspaceSystem,
        )
    except ImportError:
        from two_subspace_ode import (  # type: ignore[no-redef]
            TwoSubspaceParams,
            TwoSubspaceSystem,
        )

if TYPE_CHECKING:
    from matplotlib.figure import Figure


def simulate_escape_probability(
    params_base: TwoSubspaceParams,
    lambdas: np.ndarray,
    n_seeds: int = 50,
    v0_mean: float = 1e-3,
    v0_std: float = 2e-4,
    t_max: float = 80.0,
    coherence_threshold: float = 0.05,
    random_seed: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """Simulate empirical escape probability across multi-seed ensembles.

    Returns:
        lambdas: Evaluated compositional pressure values.
        p_escape: Fraction of trials escaping the shortcut state (v(t_max) >= threshold).
    """
    rng = np.random.default_rng(random_seed)
    p_escape = np.zeros_like(lambdas, dtype=float)

    for i, l_val in enumerate(lambdas):
        p = TwoSubspaceParams(
            a_S=params_base.a_S,
            theta_S=params_base.theta_S,
            b_S=params_base.b_S,
            a_C=params_base.a_C,
            b_C=params_base.b_C,
            kappa=params_base.kappa,
            lambda_val=float(l_val),
        )
        sys = TwoSubspaceSystem(p)
        escaped_count = 0

        for _ in range(n_seeds):
            v0 = float(np.clip(rng.normal(v0_mean, v0_std), 1e-6, 1.0))
            u0 = 0.5
            _, v_ana = sys.analytical_solution(np.array([t_max]), u0, v0)
            if v_ana[0] >= coherence_threshold:
                escaped_count += 1

        p_escape[i] = escaped_count / n_seeds

    return lambdas, p_escape


def simulate_late_onset_destabilization(
    params_base: TwoSubspaceParams,
    lambda_pre: float = 0.2,
    lambda_post: float = 1.0,
    t_switch: float = 50.0,
    t_total: float = 100.0,
    u0: float = 0.1,
    v0: float = 0.05,
    n_points_per_phase: int = 300,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Simulate late-onset destabilization where supercritical pressure is activated after entrapment."""
    # Phase 1: Subcritical entrapment
    p_pre = TwoSubspaceParams(
        a_S=params_base.a_S,
        theta_S=params_base.theta_S,
        b_S=params_base.b_S,
        a_C=params_base.a_C,
        b_C=params_base.b_C,
        kappa=params_base.kappa,
        lambda_val=lambda_pre,
    )
    sys_pre = TwoSubspaceSystem(p_pre)
    t1 = np.linspace(0.0, t_switch, n_points_per_phase)
    u1, v1 = sys_pre.analytical_solution(t1, u0, v0)

    # Phase 2: Supercritical rescue
    p_post = TwoSubspaceParams(
        a_S=params_base.a_S,
        theta_S=params_base.theta_S,
        b_S=params_base.b_S,
        a_C=params_base.a_C,
        b_C=params_base.b_C,
        kappa=params_base.kappa,
        lambda_val=lambda_post,
    )
    sys_post = TwoSubspaceSystem(p_post)
    t2_rel = np.linspace(0.0, t_total - t_switch, n_points_per_phase)
    u_init_post = float(u1[-1])
    v_init_post = max(float(v1[-1]), 1e-4)  # Small residual perturbation
    u2, v2 = sys_post.analytical_solution(t2_rel, u_init_post, v_init_post)

    t_all = np.concatenate([t1, t_switch + t2_rel])
    u_all = np.concatenate([u1, u2])
    v_all = np.concatenate([v1, v2])

    return t_all, u_all, v_all, t_switch


def simulate_rate_ordering(
    params_base: TwoSubspaceParams,
    delta_lambdas: np.ndarray,
    v0: float = 1e-4,
    alpha: float = 0.9,
) -> tuple[np.ndarray, np.ndarray]:
    """Calculate escape latency tau(lambda) across supercritical distance delta = lambda - lambda_crit."""
    lambda_crit = params_base.b_C / params_base.a_C
    tau_vals = np.zeros_like(delta_lambdas, dtype=float)

    for i, delta in enumerate(delta_lambdas):
        p = TwoSubspaceParams(
            a_S=params_base.a_S,
            theta_S=params_base.theta_S,
            b_S=params_base.b_S,
            a_C=params_base.a_C,
            b_C=params_base.b_C,
            kappa=params_base.kappa,
            lambda_val=lambda_crit + float(delta),
        )
        sys = TwoSubspaceSystem(p)
        t_esc = sys.escape_time(v0=v0, alpha=alpha)
        tau_vals[i] = t_esc if t_esc is not None else np.nan

    return delta_lambdas, tau_vals


def generate_observable_signatures_figure(
    params_base: TwoSubspaceParams | None = None,
    save_path: str | Path | None = None,
) -> Figure:
    """Generate a comprehensive 3-panel publication figure displaying all three observable signatures."""
    if params_base is None:
        params_base = TwoSubspaceParams(
            a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=0.0
        )

    lambda_crit = params_base.b_C / params_base.a_C
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5), dpi=300)

    # -------------------------------------------------------------
    # Panel 1: Signature 1 — Step-Function Escape Probability
    # -------------------------------------------------------------
    lambdas_grid = np.linspace(0.1, 1.0, 45)
    _, p_escape = simulate_escape_probability(
        params_base, lambdas_grid, n_seeds=60, t_max=80.0, coherence_threshold=0.05
    )

    # Synthetic smooth dose-response comparison (H_null)
    p_null = 1.0 / (1.0 + np.exp(-10.0 * (lambdas_grid - lambda_crit)))

    ax1.plot(
        lambdas_grid,
        p_escape,
        "ro-",
        linewidth=2.2,
        markersize=5,
        label=r"$H_0$ Bifurcation ($P(\text{escape})$)",
    )
    ax1.plot(
        lambdas_grid,
        p_null,
        "k--",
        linewidth=1.8,
        alpha=0.75,
        label=r"$H_{\text{null}}$ Smooth Dose-Response",
    )
    ax1.axvline(
        lambda_crit,
        color="blue",
        linestyle=":",
        linewidth=1.8,
        label=rf"$\lambda_{{\text{{crit}}}} = {lambda_crit:.2f}$",
    )

    ax1.fill_between(
        lambdas_grid,
        0,
        1,
        where=(lambdas_grid < lambda_crit),
        color="blue",
        alpha=0.08,
    )
    ax1.fill_between(
        lambdas_grid,
        0,
        1,
        where=(lambdas_grid >= lambda_crit),
        color="red",
        alpha=0.08,
    )

    ax1.set_xlabel(r"Compositional Pressure $\lambda$", fontsize=11)
    ax1.set_ylabel(r"Escape Probability $P(\text{escape})$", fontsize=11)
    ax1.set_title(r"Signature 1: Separatrix Step Function", fontsize=12)
    ax1.set_ylim(-0.05, 1.05)
    ax1.grid(True, linestyle="--", alpha=0.4)
    ax1.legend(loc="center left", fontsize=9)

    # -------------------------------------------------------------
    # Panel 2: Signature 2 — Late-Onset Destabilization
    # -------------------------------------------------------------
    t_all, u_all, v_all, t_sw = simulate_late_onset_destabilization(
        params_base,
        lambda_pre=0.2,
        lambda_post=1.0,
        t_switch=40.0,
        t_total=90.0,
        u0=0.2,
        v0=0.05,
    )

    ax2.plot(t_all, u_all, color="tab:blue", linewidth=2.2, label=r"Shortcut Parameter $u(t)$")
    ax2.plot(t_all, v_all, color="tab:red", linewidth=2.5, label=r"Schema Coherence $v(t)$")
    ax2.axvline(
        t_sw,
        color="darkgreen",
        linestyle="--",
        linewidth=2.0,
        label=rf"Intervention ($t_{{\text{{switch}}}} = {t_sw:.0f}$)",
    )

    # Annotate phases
    ax2.text(
        t_sw / 2.0,
        0.8,
        "Phase 1: Subcritical\n" r"$\lambda = 0.2 < \lambda_{\text{crit}}$" "\n(Trapped at $E_S$)",
        ha="center",
        va="center",
        fontsize=9,
        bbox={"boxstyle": "round", "facecolor": "lightblue", "alpha": 0.3},
    )
    ax2.text(
        (t_sw + 90.0) / 2.0,
        0.8,
        "Phase 2: Supercritical\n"
        r"$\lambda = 1.0 > \lambda_{\text{crit}}$"
        "\n(Rapid Escape to $E_C$)",
        ha="center",
        va="center",
        fontsize=9,
        bbox={"boxstyle": "round", "facecolor": "salmon", "alpha": 0.3},
    )

    ax2.set_xlabel(r"Continuous Training Step $t$", fontsize=11)
    ax2.set_ylabel(r"Parameter Magnitudes", fontsize=11)
    ax2.set_title(r"Signature 2: Late-Onset Destabilization", fontsize=12)
    ax2.set_ylim(-0.05, 1.05)
    ax2.grid(True, linestyle="--", alpha=0.4)
    ax2.legend(loc="center right", fontsize=9)

    # -------------------------------------------------------------
    # Panel 3: Signature 3 — Monotonic Rate Ordering & Slowing Down
    # -------------------------------------------------------------
    deltas = np.logspace(-2.5, 0.0, 35)  # delta = lambda - lambda_crit
    _, tau_vals = simulate_rate_ordering(params_base, deltas, v0=1e-4, alpha=0.9)

    ax3.loglog(
        deltas,
        tau_vals,
        "mo-",
        linewidth=2.2,
        markersize=4,
        label=r"Escape Latency $\tau(\lambda)$",
    )

    # Theoretical ~ 1/delta reference slope
    ref_scale = float(tau_vals[len(tau_vals) // 2] * deltas[len(deltas) // 2])
    tau_ref = ref_scale / deltas
    ax3.loglog(
        deltas,
        tau_ref,
        "k:",
        linewidth=1.8,
        label=r"Theoretical Scaling $\propto (\lambda - \lambda_{\text{crit}})^{-1}$",
    )

    ax3.set_xlabel(r"Supercritical Distance $\lambda - \lambda_{\text{crit}}$", fontsize=11)
    ax3.set_ylabel(r"Escape Latency $\tau$ (Steps to $90\% v^*$)", fontsize=11)
    ax3.set_title(r"Signature 3: Critical Slowing Down ($\tau \propto \Delta\lambda^{-1}$)", fontsize=12)
    ax3.grid(True, which="both", linestyle="--", alpha=0.4)
    ax3.legend(loc="upper right", fontsize=9)

    plt.tight_layout()

    if save_path:
        out_path = Path(save_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, dpi=300, bbox_inches="tight")

    return fig


def main() -> None:
    """Simulate observable signatures and output diagnostic figures."""
    print("=" * 70)
    print("Σ-Model Paper 02: Observable Bifurcation Signatures Simulation")
    print("=" * 70)

    params = TwoSubspaceParams(
        a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=0.0
    )
    lambda_crit = params.b_C / params.a_C
    print(f"Base Parameters: a_S={params.a_S}, b_S={params.b_S}, a_C={params.a_C}, b_C={params.b_C}")
    print(f"Critical Threshold: lambda_crit = {lambda_crit:.4f}")
    print("-" * 70)

    # Generate figure
    out_fig = "paper02/writing/figures/observable_signatures.png"
    generate_observable_signatures_figure(params, save_path=out_fig)
    print(f"Saved observable signatures diagnostic figure to: {out_fig}")
    print("=" * 70)


if __name__ == "__main__":
    main()
