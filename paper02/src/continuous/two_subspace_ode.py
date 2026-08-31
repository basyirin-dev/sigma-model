"""Two-Subspace Continuous Gradient Flow ODE System for Paper 02.

This module provides the analytical and numerical reference implementation for the
two-subspace dynamical reduction:
    du/dt = a_S * (theta_S - u) - lambda * b_S * u
    dv/dt = v * (lambda * a_C - b_C) - kappa * v^2

Key Theoretical Invariants:
    - Critical compositional pressure: lambda_crit = b_C / a_C
    - Transverse Jacobian eigenvalue at shortcut equilibrium E_S: mu_perp = lambda * a_C - b_C
    - Longitudinal Jacobian eigenvalue: mu_parallel = -(a_S + lambda * b_S) < 0
    - Transcritical bifurcation: Stability exchange between E_S and E_C at lambda = lambda_crit
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

if TYPE_CHECKING:
    from matplotlib.figure import Figure


@dataclass(frozen=True)
class TwoSubspaceParams:
    """Parameters governing the two-subspace continuous gradient flow system.

    Attributes:
        a_S: Shortcut curvature / learning speed from task loss (a_S > 0).
        theta_S: Target shortcut weight alignment under task loss (theta_S > 0).
        b_S: Shortcut invariance penalty under substitution loss (b_S >= 0).
        a_C: Schema alignment gain under substitution loss (a_C > 0).
        b_C: Schema damping under shortcut-dominated task loss (b_C > 0).
        kappa: Capacity saturation quadratic damping (kappa > 0).
        lambda_val: Compositional pressure multiplier (lambda >= 0).
    """

    a_S: float = 1.0  # noqa: N815
    theta_S: float = 1.0  # noqa: N815
    b_S: float = 0.5  # noqa: N815
    a_C: float = 1.0  # noqa: N815
    b_C: float = 0.025  # noqa: N815 (Calibrated to locked lambda_crit = 0.025)
    kappa: float = 1.0
    lambda_val: float = 0.0

    def __post_init__(self) -> None:
        """Validate parameter domain constraints."""
        if self.a_S <= 0:
            raise ValueError(f"a_S must be positive, got {self.a_S}")
        if self.theta_S <= 0:
            raise ValueError(f"theta_S must be positive, got {self.theta_S}")
        if self.b_S < 0:
            raise ValueError(f"b_S must be non-negative, got {self.b_S}")
        if self.a_C <= 0:
            raise ValueError(f"a_C must be positive, got {self.a_C}")
        if self.b_C <= 0:
            raise ValueError(f"b_C must be positive, got {self.b_C}")
        if self.kappa <= 0:
            raise ValueError(f"kappa must be positive, got {self.kappa}")
        if self.lambda_val < 0:
            raise ValueError(f"lambda_val must be non-negative, got {self.lambda_val}")


@dataclass(frozen=True)
class EquilibriumPoint:
    """Represents an equilibrium point in (u, v) phase space."""

    name: str
    u: float
    v: float
    is_physical: bool
    mu_parallel: float
    mu_perp: float
    is_stable: bool


class TwoSubspaceSystem:
    """Continuous dynamical system and analytical solver for the Two-Subspace Reduction."""

    def __init__(self, params: TwoSubspaceParams) -> None:
        self.params = params

    @property
    def lambda_crit(self) -> float:
        """Calculate the exact analytical critical threshold lambda_crit = b_C / a_C."""
        return self.params.b_C / self.params.a_C

    @property
    def mu_perp(self) -> float:
        """Transverse eigenvalue at shortcut equilibrium E_S."""
        return self.params.lambda_val * self.params.a_C - self.params.b_C

    @property
    def mu_parallel(self) -> float:
        """Longitudinal eigenvalue along shortcut direction u."""
        return -(self.params.a_S + self.params.lambda_val * self.params.b_S)

    def vector_field(self, _t: float, state: np.ndarray | tuple[float, float]) -> np.ndarray:
        """Evaluate the continuous vector field [du/dt, dv/dt]."""
        u, v = float(state[0]), float(state[1])
        p = self.params
        du_dt = p.a_S * (p.theta_S - u) - p.lambda_val * p.b_S * u
        dv_dt = v * (p.lambda_val * p.a_C - p.b_C) - p.kappa * (v**2)
        return np.array([du_dt, dv_dt], dtype=float)

    def jacobian(self, _u: float, v: float) -> np.ndarray:
        """Evaluate the 2x2 Jacobian matrix J(u, v)."""
        p = self.params
        dfu_du = -(p.a_S + p.lambda_val * p.b_S)
        dfu_dv = 0.0
        dfv_du = 0.0
        dfv_dv = (p.lambda_val * p.a_C - p.b_C) - 2.0 * p.kappa * v
        return np.array([[dfu_du, dfu_dv], [dfv_du, dfv_dv]], dtype=float)

    def fixed_points(self) -> tuple[EquilibriumPoint, EquilibriumPoint]:
        """Compute the two equilibria E_S and E_C with stability classifications."""
        p = self.params
        u_star = (p.a_S * p.theta_S) / (p.a_S + p.lambda_val * p.b_S)

        # Shortcut equilibrium E_S = (u_star, 0)
        v_s = 0.0
        j_es = self.jacobian(u_star, v_s)
        mu_par_es = float(j_es[0, 0])
        mu_perp_es = float(j_es[1, 1])
        stable_es = (mu_par_es < 0) and (mu_perp_es < 0)
        e_s = EquilibriumPoint(
            name="E_S (Shortcut)",
            u=u_star,
            v=v_s,
            is_physical=True,
            mu_parallel=mu_par_es,
            mu_perp=mu_perp_es,
            is_stable=stable_es,
        )

        # Coherent equilibrium E_C = (u_star, (lambda * a_C - b_C) / kappa)
        v_c = (p.lambda_val * p.a_C - p.b_C) / p.kappa
        j_ec = self.jacobian(u_star, v_c)
        mu_par_ec = float(j_ec[0, 0])
        mu_perp_ec = float(j_ec[1, 1])
        is_phys_ec = v_c >= 0.0
        stable_ec = is_phys_ec and (mu_par_ec < 0) and (mu_perp_ec < 0)
        e_c = EquilibriumPoint(
            name="E_C (Coherent)",
            u=u_star,
            v=v_c,
            is_physical=is_phys_ec,
            mu_parallel=mu_par_ec,
            mu_perp=mu_perp_ec,
            is_stable=stable_ec,
        )

        return e_s, e_c

    def analytical_solution(
        self, t: np.ndarray, u0: float, v0: float
    ) -> tuple[np.ndarray, np.ndarray]:
        """Compute the exact closed-form analytical trajectories u(t) and v(t).

        For u(t):
            u(t) = u_star + (u0 - u_star) * exp(-(a_S + lambda * b_S) * t)

        For v(t) (Bernoulli equation dv/dt = mu_perp * v - kappa * v^2):
            - If mu_perp == 0: v(t) = v0 / (1 + kappa * v0 * t)
            - If mu_perp != 0: v(t) = (mu_perp * v0) / (kappa * v0 + (mu_perp - kappa * v0) * exp(-mu_perp * t))
        """
        p = self.params
        u_star = (p.a_S * p.theta_S) / (p.a_S + p.lambda_val * p.b_S)
        decay_u = p.a_S + p.lambda_val * p.b_S
        u_t = u_star + (u0 - u_star) * np.exp(-decay_u * t)

        mu = self.mu_perp
        if np.isclose(mu, 0.0, atol=1e-12):
            # Critical bifurcation line: algebraic decay
            v_t = v0 / (1.0 + p.kappa * v0 * t)
        else:
            denom = p.kappa * v0 + (mu - p.kappa * v0) * np.exp(-mu * t)
            v_t = (mu * v0) / denom

        return u_t, v_t

    def numerical_solution(
        self,
        t_span: tuple[float, float],
        u0: float,
        v0: float,
        t_eval: np.ndarray | None = None,
        method: str = "RK45",
        rtol: float = 1e-9,
        atol: float = 1e-12,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Solve the continuous ODE numerically with high-order adaptive Runge-Kutta."""
        sol = solve_ivp(
            fun=self.vector_field,
            t_span=t_span,
            y0=[u0, v0],
            t_eval=t_eval,
            method=method,
            rtol=rtol,
            atol=atol,
        )
        if not sol.success:
            raise RuntimeError(f"ODE integration failed: {sol.message}")
        return sol.t, sol.y[0], sol.y[1]

    def escape_time(self, v0: float, alpha: float = 0.9) -> float | None:
        """Compute the analytical time required to reach fraction alpha of coherent state v*.

        Returns None if lambda <= lambda_crit (no escape from E_S) or if v0 <= 0.
        """
        if self.params.lambda_val <= self.lambda_crit or v0 <= 0:
            return None
        v_star = self.mu_perp / self.params.kappa
        if v0 >= alpha * v_star:
            return 0.0
        # v(t) = v_star / (1 + ((v_star - v0)/v0) * exp(-mu * t)) = alpha * v_star
        # => 1 + ((v_star - v0)/v0) * exp(-mu * t) = 1 / alpha
        # => exp(-mu * t) = (1 - alpha) / alpha * (v0 / (v_star - v0))
        # => t = (1 / mu) * ln((alpha / (1 - alpha)) * ((v_star - v0) / v0))
        ratio = (alpha / (1.0 - alpha)) * ((v_star - v0) / v0)
        return float((1.0 / self.mu_perp) * np.log(ratio))


def generate_bifurcation_diagram(
    params_base: TwoSubspaceParams,
    lambda_range: tuple[float, float] = (0.0, 1.5),
    num_points: int = 300,
    save_path: str | Path | None = None,
) -> Figure:
    """Generate a publication-grade transcritical bifurcation diagram."""
    lambdas = np.linspace(lambda_range[0], lambda_range[1], num_points)
    lambda_crit = params_base.b_C / params_base.a_C

    # Branches
    e_s_v = np.zeros_like(lambdas)
    e_c_v = (lambdas * params_base.a_C - params_base.b_C) / params_base.kappa

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)

    # Subplot 1: Transcritical Bifurcation Diagram
    sub_mask = lambdas < lambda_crit
    super_mask = lambdas >= lambda_crit

    # E_S branch (v = 0)
    ax1.plot(
        lambdas[sub_mask],
        e_s_v[sub_mask],
        "b-",
        linewidth=2.5,
        label=r"$E_S$ Stable ($\sigma$-Trap)",
    )
    ax1.plot(
        lambdas[super_mask],
        e_s_v[super_mask],
        "b--",
        linewidth=2.0,
        label=r"$E_S$ Unstable Saddle",
    )

    # E_C branch (v = (lambda*a_C - b_C)/kappa)
    ax1.plot(
        lambdas[sub_mask],
        e_c_v[sub_mask],
        "r--",
        linewidth=2.0,
        label=r"$E_C$ Unstable (Unphysical $v < 0$)",
    )
    ax1.plot(
        lambdas[super_mask],
        e_c_v[super_mask],
        "r-",
        linewidth=2.5,
        label=r"$E_C$ Stable Coherent Node",
    )

    ax1.axvline(
        lambda_crit,
        color="black",
        linestyle=":",
        linewidth=1.5,
        label=rf"$\lambda_{{\text{{crit}}}} = {lambda_crit:.2f}$",
    )
    ax1.axhline(0, color="gray", linestyle="-", linewidth=0.5, alpha=0.5)

    ax1.set_xlabel(r"Compositional Pressure $\lambda$", fontsize=12)
    ax1.set_ylabel(r"Equilibrium Schema Weight $v^*$", fontsize=12)
    ax1.set_title("Transcritical Stability Exchange ($v^*$ vs $\\lambda$)", fontsize=13)
    ax1.grid(True, linestyle="--", alpha=0.4)
    ax1.legend(loc="upper left", fontsize=10)
    ax1.set_ylim(-0.6, 1.2)

    # Subplot 2: Transverse Eigenvalue mu_perp vs lambda
    mu_perps = lambdas * params_base.a_C - params_base.b_C
    ax2.plot(
        lambdas, mu_perps, color="purple", linewidth=2.5, label=r"$\mu_\perp = \lambda a_C - b_C$"
    )
    ax2.axhline(0, color="black", linestyle="-", linewidth=0.8)
    ax2.axvline(lambda_crit, color="black", linestyle=":", linewidth=1.5)
    ax2.fill_between(
        lambdas,
        mu_perps,
        0,
        where=(lambdas < lambda_crit),
        color="blue",
        alpha=0.15,
        label=r"Subcritical $\mu_\perp < 0$ (Stable Trap)",
    )
    ax2.fill_between(
        lambdas,
        mu_perps,
        0,
        where=(lambdas >= lambda_crit),
        color="red",
        alpha=0.15,
        label=r"Supercritical $\mu_\perp > 0$ (Escape)",
    )

    ax2.set_xlabel(r"Compositional Pressure $\lambda$", fontsize=12)
    ax2.set_ylabel(r"Transverse Eigenvalue $\mu_\perp$", fontsize=12)
    ax2.set_title(r"Jacobian Transverse Spectrum at $E_S$", fontsize=13)
    ax2.grid(True, linestyle="--", alpha=0.4)
    ax2.legend(loc="upper left", fontsize=10)

    plt.tight_layout()

    if save_path:
        out_path = Path(save_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, dpi=300, bbox_inches="tight")

    return fig


def generate_phase_portraits(
    save_path: str | Path | None = None,
) -> Figure:
    """Generate side-by-side phase portraits for subcritical, critical, and supercritical regimes."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), dpi=300)
    cases = [
        (r"\text{Subcritical } (\lambda = 0.2 < \lambda_{\text{crit}})", 0.2, "blue"),
        (r"\text{Critical } (\lambda = 0.5 = \lambda_{\text{crit}})", 0.5, "darkgreen"),
        (r"\text{Supercritical } (\lambda = 1.0 > \lambda_{\text{crit}})", 1.0, "crimson"),
    ]

    u_grid = np.linspace(0.0, 1.2, 20)
    v_grid = np.linspace(0.0, 1.0, 20)
    u_grid_2d, v_grid_2d = np.meshgrid(u_grid, v_grid)

    for ax, (title, l_val, col) in zip(axes, cases, strict=False):
        params = TwoSubspaceParams(
            a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=l_val
        )
        sys = TwoSubspaceSystem(params)

        # Vector field grid
        du = params.a_S * (params.theta_S - u_grid_2d) - l_val * params.b_S * u_grid_2d
        dv = v_grid_2d * (l_val * params.a_C - params.b_C) - params.kappa * (v_grid_2d**2)
        speed = np.sqrt(du**2 + dv**2)
        speed[speed == 0] = 1.0
        ax.quiver(
            u_grid_2d,
            v_grid_2d,
            du / speed,
            dv / speed,
            speed,
            cmap="viridis",
            alpha=0.6,
            scale=25,
        )

        # Sample trajectories
        t_eval = np.linspace(0, 15, 300)
        init_states = [(0.1, 0.05), (0.2, 0.4), (0.8, 0.8), (1.1, 0.2), (0.1, 0.7)]
        for u0, v0 in init_states:
            u_t, v_t = sys.analytical_solution(t_eval, u0, v0)
            ax.plot(u_t, v_t, color=col, linewidth=1.5, alpha=0.85)
            ax.plot(u0, v0, "o", color=col, markersize=4)

        # Plot equilibria
        es, ec = sys.fixed_points()
        if es.is_stable:
            ax.plot(es.u, es.v, "bo", markersize=9, label=r"Stable $E_S$ (Trap)")
        else:
            ax.plot(es.u, es.v, "bx", markersize=9, markeredgewidth=2, label=r"Unstable $E_S$")

        if ec.is_physical:
            if ec.is_stable:
                ax.plot(ec.u, ec.v, "ro", markersize=9, label=r"Stable $E_C$ (Coherent)")
            else:
                ax.plot(ec.u, ec.v, "rx", markersize=9, markeredgewidth=2, label=r"Unstable $E_C$")

        ax.set_xlabel(r"Shortcut Parameter $u$", fontsize=11)
        ax.set_ylabel(r"Schema Parameter $v$", fontsize=11)
        ax.set_title(rf"${title}$", fontsize=11)
        ax.set_xlim(-0.05, 1.25)
        ax.set_ylim(-0.05, 1.05)
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout()

    if save_path:
        out_path = Path(save_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, dpi=300, bbox_inches="tight")

    return fig


def main() -> None:
    """Execute reference simulations and save publication diagnostic figures."""
    print("=" * 70)
    print("Σ-Model Paper 02: Two-Subspace Reduction Reference Simulation")
    print("=" * 70)

    base_params = TwoSubspaceParams(
        a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=0.0
    )
    sys = TwoSubspaceSystem(base_params)
    print(f"Base Configuration: a_S={base_params.a_S}, b_S={base_params.b_S},")
    print(
        f"                   a_C={base_params.a_C}, b_C={base_params.b_C}, kappa={base_params.kappa}"
    )
    print(f"Analytical Critical Threshold lambda_crit: {sys.lambda_crit:.4f}")
    print("-" * 70)

    for l_val in [0.2, 0.5, 1.0]:
        p = TwoSubspaceParams(
            a_S=1.0, theta_S=1.0, b_S=0.5, a_C=1.0, b_C=0.5, kappa=1.0, lambda_val=l_val
        )
        s = TwoSubspaceSystem(p)
        es, ec = s.fixed_points()
        print(f"lambda = {l_val:.2f} (mu_perp = {s.mu_perp:+.2f}):")
        print(f"  E_S: u*={es.u:.4f}, v*={es.v:.4f} | Stable={es.is_stable}")
        print(
            f"  E_C: u*={ec.u:.4f}, v*={ec.v:.4f} | Physical={ec.is_physical}, Stable={ec.is_stable}"
        )
        if s.mu_perp > 0:
            t_esc = s.escape_time(v0=0.01, alpha=0.9)
            print(f"  Escape time from v0=0.01 to 90% v*: t_esc = {t_esc:.4f}")
        print()

    # Generate figures
    fig_bif = "paper02/writing/figures/two_subspace_bifurcation.png"
    fig_phase = "paper02/writing/figures/two_subspace_phase_portraits.png"
    generate_bifurcation_diagram(base_params, save_path=fig_bif)
    generate_phase_portraits(save_path=fig_phase)
    print(f"Saved bifurcation diagram to: {fig_bif}")
    print(f"Saved phase portraits to:     {fig_phase}")
    print("=" * 70)


if __name__ == "__main__":
    main()
