#!/usr/bin/env python3
"""
Σ-Model V3.0+ local smoke test.
Verifies imports, ODE math, configs, and model instantiation.
Runs in <10 seconds on CPU. No GPU required.

Usage:
    PYTHONPATH=code:$PYTHONPATH python scripts/smoke_test.py
"""

import time

import torch
from sigma.config import load_config, merge_configs
from sigma.models import SigmaTransformer
from sigma.ode import (
    additive_coupling,
    multiplicative_coupling,
    phase_transition,
    psi_geometric,
    sigma_critical,
    sigma_ode,
)
from sigma.ode.solver import SigmaODESolver
from sigma.utils.metrics import compute_construct_isolation, compute_reliability

start = time.perf_counter()

print("=" * 50)
print("Σ-Model V3.0+ Smoke Test")
print("=" * 50)

# ── 1. Imports ────────────────────────────────────────────────────────────
print("\n[1/5] Checking imports ...")
print("  ✅ All imports resolved")


# ── 2. ODE Math ───────────────────────────────────────────────────────────
print("\n[2/5] Testing ODE functions ...")

ds = sigma_ode(sigma=0.1, rho=1.0, p_a=0.9, alpha_a=1.0, epsilon_sigma=0.01, omega_ai=0.5)
assert ds > 0, "sigma_ode: growth should dominate at low sigma"

ds = sigma_ode(sigma=0.9, rho=0.1, p_a=0.1, alpha_a=0.1, epsilon_sigma=1.0, omega_ai=1.0)
assert ds < 0, "sigma_ode: decay should dominate at high sigma + low growth"

p = psi_geometric(0.5, 0.5, psi_0=1.0, phi=1.0)
assert abs(p - 0.5) < 1e-6, f"psi_geometric: expected 0.5, got {p}"

sc = sigma_critical(gamma_sigma=2.0, r0_min=2.0)
assert sc > 0, f"sigma_critical: expected >0, got {sc}"

pt = phase_transition(sigma=0.0, delta_rel=0.0, phase=0, sigma_crit=0.15, delta_star=0.55)
assert pt == 0, f"phase_transition: expected 0, got {pt}"

ac = additive_coupling(task_loss=1.0, sigma=0.3, coupling_strength=0.2)
assert ac > 1.0, f"additive_coupling: expected >1.0, got {ac}"

mc = multiplicative_coupling(task_loss=1.0, sigma=0.5, coupling_strength=0.2)
assert 1.09 < mc < 1.11, f"multiplicative_coupling: expected ~1.1, got {mc}"

print("  ✅ All ODE math checks passed")


# ── 3. ODE Solver ─────────────────────────────────────────────────────────
print("\n[3/5] Testing ODE solver ...")

solver = SigmaODESolver(sigma_init=0.1, delta_rel_init=0.05)
assert solver.sigma == 0.1
assert solver.delta_rel == 0.05
assert solver.phase == 0

result = solver.step(global_step=100, n_timesteps=2000, coupling_mode=None)
assert "sigma" in result and "delta_rel" in result and "phase" in result
assert 0.0 <= result["sigma"] <= 1.0
assert 0.0 <= result["delta_rel"] <= 1.0

solver2 = SigmaODESolver()
r2 = solver2.step(global_step=500, n_timesteps=2000, coupling_mode="additive", coupling_str=0.2)
assert r2["phase"] >= 0

print("  ✅ ODE solver checks passed")


# ── 4. Config Parsing ─────────────────────────────────────────────────────
print("\n[4/5] Testing config loading ...")

configs = ["base.yaml", "h-ptb.yaml", "h-afb.yaml", "h-mcb.yaml", "h-dcb.yaml", "h-stb.yaml"]
for name in configs:
    cfg = load_config(f"experiments/configs/{name}")
    assert isinstance(cfg, dict) and len(cfg) > 0, f"Config {name} is empty"
print(f"  ✅ All {len(configs)} configs parsed successfully")

merged = merge_configs({"a": 1, "b": {"c": 2}}, {"b": {"c": 99}})
assert merged["b"]["c"] == 99
print("  ✅ Config merge works")


# ── 5. Model + Metrics ────────────────────────────────────────────────────
print("\n[5/5] Testing model instantiation ...")

model = SigmaTransformer(vocab_size=50, d_model=32, nhead=2, num_layers=1, dim_ff=64)
assert model.count_parameters() > 0, "Model has zero parameters"

x = torch.randint(0, 50, (2, 10))
y = torch.randint(0, 50, (2, 12))
out = model(x, y)
assert out.shape == (2, 12, 50), f"Expected (2, 12, 50), got {out.shape}"
print(f"  ✅ Model instantiation OK ({model.count_parameters():,} params)")

print("\n[5/5] Testing metrics (continued) ...")

reliability = compute_reliability([0.5, 0.6, 0.55])
assert 0.0 <= reliability <= 1.0, f"compute_reliability out of range: {reliability}"

ci = compute_construct_isolation([0.5, 0.6], [0.65, 0.60], [0.95, 0.96])
assert 0.0 <= ci <= 1.0, f"compute_construct_isolation out of range: {ci}"

print("  ✅ Metrics checks passed")


# ── Summary ───────────────────────────────────────────────────────────────
elapsed = time.perf_counter() - start
print(f"\n{'=' * 50}")
print(f"✅ ALL CHECKS PASSED  ({elapsed:.1f}s)")
print(f"{'=' * 50}")
