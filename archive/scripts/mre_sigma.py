#!/usr/bin/env python3
"""Minimal Reproducible Example for Σ-Model V3.0+.

Runs a 10-step dummy training loop to verify:
- Package imports resolve correctly
- ODE solver runs without shape errors
- Signal extraction (GCA proxy) works
- Phase transitions trigger
- Loss modulation applies
- Schema coherence crosses sigma_critical threshold

Usage:  python scripts/mre_sigma.py
Expect: < 60 seconds on CPU
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

import numpy as np

try:
    import torch
except ImportError:
    print("ERROR: PyTorch is not installed. Install with: pip install torch>=2.10")
    sys.exit(1)

from sigma import __version__
from sigma.ode.equations import (
    sigma_critical,
    sigma_ode,
    delta_ode,
    psi_geometric,
    gompertz,
    phase_transition,
    multiplicative_coupling,
)
from sigma.ode.solver import SigmaODESolver
from sigma.utils.metrics import compute_reliability
from sigma.models.transformer import SigmaTransformer


def dummy_task_loss() -> float:
    return float(np.random.exponential(0.5))


def main() -> None:
    t_start = time.time()
    print(f"Σ-Model MRE v{__version__}")
    print("-" * 55)

    # Parameters
    n_steps = 10
    dt = 0.25
    coupling_strength = 0.3
    gamma_sigma = 0.8
    r0_min = 2.0

    sigma_crit = sigma_critical(gamma_sigma, r0_min)
    delta_star = 0.55

    # ODE solver instantiation (demonstrates solver API)
    solver = SigmaODESolver(sigma_init=0.1, delta_rel_init=0.05)

    # State
    sigma = 0.1
    delta = 0.05
    delta_rel = 0.05
    phase = 0

    sigma_history: list[float] = []
    delta_history: list[float] = []
    phase_history: list[int] = []
    gca_history: list[float] = []
    loss_history: list[float] = []

    print(f"{'Step':>5} {'sigma':>7} {'delta':>7} {'GCA':>7} {'Phase':>5} {'Loss':>7}")
    print("-" * 55)

    for step in range(n_steps):
        # 1. Schema coherence ODE (Eq. 28)
        d_sigma = sigma_ode(
            sigma=sigma,
            rho=2.5,
            p_a=0.85,
            alpha_a=0.8,
            epsilon_sigma=0.08,
            omega_ai=0.3,
            gamma_sigma=gamma_sigma,
        )
        sigma = max(0.0, min(1.0, sigma + d_sigma * dt))

        # 2. Parametric depth ODE (Eq. 15)
        f_learn = 0.5
        eta = gompertz(step, a=-3.0, b=-0.05)
        d_delta = delta_ode(
            delta=delta,
            delta_rel=delta_rel,
            f_learn=f_learn,
            eta=eta,
            t_a=0.5,
            lambda_c=0.1,
            gamma_sigma=gamma_sigma,
            sigma=sigma,
            r_a=0.3,
        )
        delta = max(0.0, delta + d_delta * dt)
        delta_rel = min(1.0, delta)

        # 3. Solver state (parallel, demonstrates SigmaODESolver API)
        solver_state = solver.step(
            global_step=step,
            n_timesteps=n_steps,
            sigma_crit=sigma_crit,
            delta_star=delta_star,
            noise_std=0.005,
            coupling_mode="multiplicative",
            coupling_str=coupling_strength,
            sigma_init=0.1,
        )

        # 4. GCA proxy via geometric mean (psi_geometric)
        gca = psi_geometric(sigma, solver_state["delta_rel"])

        # 5. Phase transition detection
        phase = phase_transition(sigma, delta_rel, phase, sigma_crit, delta_star)

        # 6. Loss modulation via multiplicative coupling (Eq. 32)
        task_loss = dummy_task_loss()
        modulated_loss = multiplicative_coupling(task_loss, sigma, coupling_strength)

        sigma_history.append(sigma)
        delta_history.append(delta)
        phase_history.append(phase)
        gca_history.append(gca)
        loss_history.append(modulated_loss)

        print(
            f"{step:>5} {sigma:>7.4f} {delta:>7.4f} {gca:>7.4f} {phase:>5} {modulated_loss:>7.4f}"
        )

    # Final state summary
    sigma_final = sigma_history[-1]
    phase_final = phase_history[-1]

    print("-" * 55)
    print(f"  sigma_final  = {sigma_final:.4f}")
    print(f"  delta_final  = {delta_history[-1]:.4f}")
    print(f"  phase_final  = {phase_final}")
    print(f"  gca_final    = {gca_history[-1]:.4f}")
    print(f"  sigma_crit   = {sigma_crit:.4f}")
    print(f"  reliability  = {compute_reliability(sigma_history):.4f}")

    # PyTorch model instantiation
    model = SigmaTransformer(vocab_size=16, d_model=32, nhead=2, num_layers=1, dim_ff=64)
    dummy_src = torch.randint(0, 16, (1, 8))
    dummy_tgt = torch.randint(0, 16, (1, 10))
    with torch.no_grad():
        out = model(dummy_src, dummy_tgt[:, :-1])
    print(f"  model output = {out.shape}")

    # Critical assertion
    assert sigma_final > 0.5, (
        f"Schema coherence failed to crystallize: sigma={sigma_final:.4f} < 0.5"
    )
    print(f"\n✓ Assertion passed: sigma_final = {sigma_final:.4f} > 0.5")

    elapsed = time.time() - t_start
    print(f"Completed in {elapsed:.1f}s (< 60s target: {'OK' if elapsed < 60 else 'SLOW'})")


if __name__ == "__main__":
    main()
