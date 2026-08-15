# Code Notation Alignment Plan — Σ-Model V3.0+

This document inventories every divergence between LaTeX mathematical notation
(in `paper/manuscript.tex` and proof-reconstruction files) and Python identifier
names (in `code/sigma/`). Each divergence is assessed for whether a rename is
safe, desirable, or better left for a future refactor.

## Current Mapping (LaTeX → Python)

### ODE Parameters

| LaTeX | Python | File(s) | Aligned? |
|-------|--------|---------|----------|
| `σ_A` | `sigma` | `ode/solver.py:19`, `ode/equations.py:20,47,58,75` | Partial — `_A` dropped |
| `δ_A` | `delta` | `ode/equations.py:51,68,82` | Partial — `_A` dropped |
| `δ_A^{\text{relative}}` | `delta_rel` | `ode/solver.py:20,67`, `ode/equations.py:52,69` | OK — `rel` short for `relative` |
| `σ_{\text{critical}}` | `sigma_crit`, `sigma_critical_val` | `ode/solver.py:27`, `ode/equations.py:4`, `models/training.py:121` | OK — naming is consistent across code |
| `δ^*` | `delta_star`, `delta_star_val` | `ode/solver.py:28`, `models/training.py:122` | OK |
| `ρ` | `rho` | `ode/equations.py:21,36` | OK |
| `P_A` | `p_a` | `ode/equations.py:22,37` | OK |
| `α_A` | `alpha_a` | `ode/equations.py:23,38` | OK |
| `ϵ_σ` | `epsilon_sigma` | `ode/equations.py:24,39` | OK |
| `Ω_{SL}` | **`omega_ai`** | `ode/equations.py:25,40` | **NO** — should be `omega_sl` |
| `γ_σ` | `gamma_sigma` | `ode/equations.py:4,26,41,57,75` | OK |
| `T_A` | `t_a` | `ode/equations.py:55,72` | OK |
| `λ_c` | `lambda_c` | `ode/equations.py:56,73` | OK |
| `r_A` | `r_a` | `ode/equations.py:59,76` | OK |
| `Ψ_A` | `psi_geometric()` | `ode/equations.py:85` | OK — function name is descriptive |
| `Ψ_0` | `psi_0` | `ode/equations.py:85` | OK |
| `φ(d_1,d_2)` | `phi` | `ode/equations.py:85` | OK — argument name |
| `η` | `eta` | `ode/equations.py:54,71` | OK |
| `a, b` (Gompertz) | `a, b` | `ode/equations.py:89` | OK |
| `R_0` | `r0_min` | `ode/equations.py:11` | OK — `r0_min` for "minimum R₀ at bifurcation" |

### Training / Config

| LaTeX | Python | File(s) | Aligned? |
|-------|--------|---------|----------|
| `\tilde{σ}_A` | `sigma_tilde` | `models/training.py:116` | OK |
| `σ_A` (ODE state) | `ode_state["sigma"]` | `models/training.py:165` | OK |
| Phase | `ode_state["phase"]` | `models/training.py:209` | OK |
| `Acc_ID` | `acc_id` | `models/training.py:114` | OK |
| `Acc_OOD` | `acc_ood` | `models/training.py:115` | OK |
| `η_{\text{effective}}` | `effective_lr` | `models/training.py:157` | OK — different concept but LR is the mechanism |
| Coupling mode | `coupling_mode` | `models/training.py:126-137` | OK |
| Coupling strength | `coupling_str` | `models/training.py:127` | Partial — `str` could be `strength` |

### Config YAML keys

| LaTeX | YAML Key | File | Aligned? |
|-------|----------|------|----------|
| `σ_{\text{critical}}` | `ode.sigma_critical` | `base.yaml:27` | OK |
| `δ^*` | `ode.delta_star` | `base.yaml:28` | OK |
| Noise ν | `ode.noise_std` | `base.yaml:29` | OK |
| `a` (Gompertz) | `ode.gompertz_a` | `base.yaml:30` | OK |
| `b` (Gompertz) | `ode.gompertz_b` | `base.yaml:31` | OK |

## Divergence Inventory

### D1: `omega_ai` → should rename to `omega_sl` (MEDIUM priority)

| Detail | Value |
|--------|-------|
| **Location** | `code/sigma/ode/equations.py:25,40` (function signature + docstring) |
| **LaTeX target** | `Ω_{SL}(d,t)` — shortcut-learning pressure |
| **Current name** | `omega_ai` |
| **Correct name** | `omega_sl` |
| **Rationale** | The suffix `ai` is an unmotivated abbreviation with no counterpart in the manuscript. The LaTeX subscript is `SL` (shortcut learning), so `omega_sl` is the direct transliteration. |
| **Downstream consumers** | Function is called from `sigma_ode()` which is called by the ODE solver; currently no caller passes `omega_ai` from config (the simplified solver in `solver.py` skips the equation path). |
| **Risk** | Low — parameter is only in the equation definition, not serialised or config-driven yet. |
| **Dependencies** | Must update docstring example also. |

### D2: `_A` subscript truncation convention — document only (LOW priority)

| Detail | Value |
|--------|-------|
| **Location** | `ode/solver.py:19-20`, `ode/equations.py:20,51` |
| **Current state** | `sigma` not `sigma_a`, `delta` not `delta_a` |
| **Proposal** | Document this as an intentional convention: top-level ODE variables drop the `_A` subscript because `A` is implied (all variables are agent-relative), but sub-parameters retain it (`p_a`, `alpha_a`, `t_a`, `r_a`). Do not rename. |
| **Risk** | None — purely documentation. |
| **Status** | Add note to module docstrings. |

### D3: `delta_rel` → would be `delta_relative` — defer (LOW priority)

| Detail | Value |
|--------|-------|
| **Location** | `ode/equations.py:52`, `ode/solver.py:20,67` |
| **Current name** | `delta_rel` |
| **Proposed name** | `delta_relative` |
| **Rationale** | `rel` is an abbreviation where the LaTeX uses `^{\text{relative}}` — full word is clearer. However, the abbreviation is idiomatic in code (cf. `rel_path`, `rel_error`). |
| **Risk** | Moderate — used in solver state (`self.delta_rel` → 3 occurrences), function parameter, and training loop metrics. Requires coordinated rename. |
| **Recommendation** | Defer unless other renames are already required in the same files. |

### D4: `coupling_str` → `coupling_strength` (LOW priority)

| Detail | Value |
|--------|-------|
| **Location** | `models/training.py:132,137,179,181` |
| **Current name** | `coupling_str` |
| **Proposed name** | `coupling_strength` |
| **Rationale** | `str` is ambiguous (could mean "string" type); `strength` is unambiguous and matches the paper's description. |
| **Risk** | Low — local variable scoped to `train_sigma_model()`. |

### D5: `r0_min` → `r_0` (LOW priority)

| Detail | Value |
|--------|-------|
| **Location** | `ode/equations.py:4,11,16` |
| **Current name** | `r0_min` |
| **Proposed name** | `r_0` or `r0` |
| **Rationale** | LaTeX uses `R_0` — the `_min` suffix was added descriptively but the parameter literally is the threshold R₀ = 1. |
| **Risk** | Low — only used in `sigma_critical()` which has one call site. |

## Dependency Graph

```
D1 (omega_ai → omega_sl)
  └── No downstream blocks — references only in equations.py

D2 (document _A convention)
  └── No code changes — add docstring in solver.py + equations.py

D3 (delta_rel → delta_relative)
  ├── equations.py:52 (parameter name)
  ├── solver.py:20,67 (state variable)
  └── solver.py:28 (parameter name in phase_transition call) → equations.py:94

D4 (coupling_str → coupling_strength)
  ├── training.py:132,137 (variable assignment)
  └── training.py:179,181 (variable use)

D5 (r0_min → r_0)
  └── equations.py:4,11 (function signature + docstring)
```

## Implementation Order (Recommended)

| Order | Item | Action | Files | Safe to batch? |
|-------|------|--------|-------|----------------|
| 1 | D1 | Rename `omega_ai` → `omega_sl` | `ode/equations.py:25,40` | Yes |
| 2 | D5 | Rename `r0_min` → `r_0` | `ode/equations.py:4,11` | Yes (same file as D1) |
| 3 | D4 | Rename `coupling_str` → `coupling_strength` | `models/training.py:132,137,179,181` | Yes |
| 4 | D2 | Add docstring notes on `_A` convention | `ode/solver.py`, `ode/equations.py` | Yes |
| 5 | D3 | Deferred — rename `delta_rel` → `delta_relative` | `ode/solver.py`, `ode/equations.py` | No — needs test updates |

## Verification

After completing any rename:
1. Run `ruff check code/sigma/` — lint pass
2. Run `pytest tests/` — all tests pass
3. Run `PYTHONPATH=code:$PYTHONPATH python scripts/smoke_test.py` — smoke test passes
4. Grep for old name: `grep -r 'OLD_NAME' code/sigma/` — zero matches

## Non-Goals

The following are intentionally out of scope for this alignment plan:

- Renaming `sigma` → `sigma_a` or `delta` → `delta_a` in the solver (D2 documents why)
- Aligning figure-label Unicode (e.g., `"σ̃_A"` in `visualization/interactive.py`) — these are display labels, not identifiers
- Adding new type annotations beyond what currently exists

---

# Implementation Plan — Σ-Model Code Alignment

## Overview

The manuscript describes a sophisticated ODE-based cognitive model with:
- Coupled ODE system (Eqs. 28–30) for `(δ_A, σ_A, α_A)`
- IMEX adaptive-step numerical integration (Algorithm 3.1)
- Multi-signal estimation framework (GCA, RGA, AC fusion — Algorithm 3.2)
- Phase classification with hysteresis

The current `code/sigma/` package and experiment notebooks **do not implement any of this**. They use phenomenological curves (linear/Gompertz + noise, not the ODE) and hard `np.clip` for bounds. Duration estimate: **~9.5 hours total**.

## Phase I — Solver Rewrite (~4h)

### I-a: `code/sigma/ode/equations.py` — `compute_rhs()` (1h)

Replace the standalone `sigma_ode()`, `delta_ode()`, `alpha_ode()` functions with a single vector-valued RHS:

```python
def compute_rhs(t: float, state: np.ndarray, params: dict) -> np.ndarray:
    """RHS of the coupled ODE system.
    
    state = [delta, sigma, alpha]  (the fast subsystem)
    
    Returns [d_delta, d_sigma, d_alpha] computed from
    Eqs. (28)–(30) of the manuscript.
    """
    delta, sigma, alpha = state
    
    # Unpack parameters (with LaTeX-aligned names)
    rho = params["rho"]
    p_a = params["p_a"]
    alpha_a = alpha  # attentional fidelity = current alpha state
    epsilon_sigma = params["epsilon_sigma"]
    omega_sl = params["omega_sl"]      # ← renamed from omega_ai
    gamma_sigma = params["gamma_sigma"]
    eta_max = params["eta_max"]
    lambda_c = params["lambda_c"]
    t_a = params["t_a"]
    r_a = params["r_a"]
    theta_i = params["theta_i"]
    theta_0 = params["theta_0"]
    nu_m = params["nu_m"]
    kappa_p = params["kappa_p"]
    kappa_i = params["kappa_i"]
    kappa_f = params["kappa_f"]
    
    # Depth ODE (Eq. 28)
    psi = psi_geometric(sigma, params)
    eta_effective = eta_max * (1.0 - t_a / (t_a + r_a))
    d_delta = eta_effective * (1.0 - delta) * psi - lambda_c * gamma_sigma * sigma * delta
    
    # Sigma ODE (Eq. 29)
    bracket = rho * p_a * alpha * (1.0 - gamma_sigma * sigma) - epsilon_sigma * omega_sl
    d_sigma = sigma * bracket  # invariant manifold at sigma=0
    
    # Alpha ODE (Eq. 30)
    d_alpha = nu_m * (1.0 - alpha) - kappa_p * alpha * (delta + sigma) \
              + kappa_i * (1.0 - delta) * (1.0 - sigma) - kappa_f * alpha * sigma
    
    return np.array([d_delta, d_sigma, d_alpha])
```

Keep `sigma_ode()`, `delta_ode()`, `alpha_ode()` as wrappers calling `compute_rhs()` for backward compatibility (or deprecate them with a docstring note).

### I-b: `code/sigma/ode/solver.py` — IMEX Solver (2h)

Replace the phenomenological `SigmaODESolver` with a proper IMEX integrator:

```python
class SigmaODESolver:
    """Adaptive-step IMEX Runge-Kutta solver for the Σ-Model ODE system.
    
    Implements Algorithm 3.1 from the manuscript.
    Fast subsystem (delta, sigma, alpha): explicit RK
    Slow subsystem (M, Xi): implicit (trapezoidal)
    """
    
    def __init__(self, params: dict, dt0: float = 0.01, 
                 atol: float = 1e-6, rtol: float = 1e-8):
        self.params = params
        self.dt = dt0
        self.atol = atol
        self.rtol = rtol
        self.state = np.array([
            params.get("delta_init", 0.05),
            params.get("sigma_init", 0.05),
            params.get("alpha_init", 0.5)
        ])
        self.t = 0.0
    
    def _explicit_stage(self, state, dt):
        """Explicit RK4 stage for fast subsystem."""
        k1 = compute_rhs(self.t, state, self.params)
        k2 = compute_rhs(self.t + dt/2, state + dt/2 * k1, self.params)
        k3 = compute_rhs(self.t + dt/2, state + dt/2 * k2, self.params)
        k4 = compute_rhs(self.t + dt, state + dt * k3, self.params)
        return state + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    def _compute_jacobian(self, state):
        """Analytical Jacobian of fast subsystem (for stiffness detection).
        
        3×3 matrix J where J[i,j] = ∂f_i/∂x_j
        Used for condition number monitoring (Prop 3.5).
        """
        # ... compute partial derivatives of compute_rhs w.r.t state ...
        pass
    
    def step(self, t_target):
        """Advance state to t_target with adaptive step size control."""
        while self.t < t_target:
            dt = min(self.dt, t_target - self.t)
            
            # Embedded error estimation (RK4 + Heun)
            state_full = self._explicit_stage(self.state, dt)
            state_heun = self.state + dt/2 * (
                compute_rhs(self.t, self.state, self.params) 
                + compute_rhs(self.t + dt, state_full, self.params)
            )
            
            error = np.max(np.abs(state_full - state_heun))
            tol = self.atol + self.rtol * np.max(np.abs(state_full))
            
            if error > tol and dt > 1e-10:
                self.dt *= 0.5  # halve step
                continue
            
            self.state = np.clip(state_full, 0.0, 1.0)  # boundary enforcement
            self.t += dt
            
            # Stiffness monitoring (Prop 3.5)
            # J = self._compute_jacobian(self.state)
            # kappa = np.linalg.cond(J)
            # if kappa > 1e6: warn or switch to implicit
            
            # Adaptive step size (PI controller)
            self.dt *= min(2.0, 0.9 * (tol / max(error, 1e-15)) ** 0.2)
        
        return self.state
    
    def integrate(self, t_span, dt_out=1.0):
        """Integrate over t_span, returning samples every dt_out."""
        times = []
        states = []
        for t in np.arange(0, t_span, dt_out):
            self.step(t)
            times.append(self.t)
            states.append(self.state.copy())
        return np.array(times), np.array(states)
```

### I-c: Config Alignment (0.5h)

Update `experiments/configs/base.yaml` to support the ODE solver:

```yaml
ode:
  sigma_critical: 0.35
  delta_star: 0.54
  noise_std: 0.012
  gompertz_a: 10.0
  gompertz_b: 0.3
  # New ODE solver parameters
  solver:
    method: imex-rk4
    dt_init: 0.01
    atol: 1e-6
    rtol: 1e-8
    dt_min: 1e-10
    dt_max: 0.1
    clip: [0.0, 1.0]
```

Update `sigma/config/schema.py` to validate the new fields.

### I-d: Deprecation Wrapper (0.5h)

Keep the old phenomenological path working for comparison experiments:

```python
class PhenomSolver(SigmaODESolver):
    """Legacy phenomenological solver — wraps old linear/Gompertz curves.
    
    Deprecated. Will be removed in a future release.
    Use SigmaODESolver (IMEX) instead.
    """
    def step(self, t_target):
        # old linear/Gompertz + noise logic
        warnings.warn("PhenomSolver is deprecated", DeprecationWarning, stacklevel=2)
        ...
```

## Phase II — Estimation Framework (~3.5h)

### II-a: Signal Extraction Module — `code/sigma/estimation/` (2h)

Create new subpackage matching Algorithm 3.2:

```
code/sigma/estimation/
├── __init__.py
├── gca.py          # Gradient-Composition Alignment
├── rga.py          # Representational-Geometry Alignment  
├── ac.py           # Augmentation Consistency
└── fusion.py       # Weighted fusion + recalibration
```

**`gca.py`** — GCA signal:
```python
def compute_gca(model, probe_batch, task_gradients) -> float:
    """Pearson correlation between task and compositional gradients.
    
    Parameters
    ----------
    model : nn.Module  — trained model
    probe_batch : torch.Tensor — compositional probe samples
    task_gradients : dict — gradients w.r.t. task loss
    
    Returns
    -------
    g_A : float — GCA signal in [0, 1]
    
    Reference: Manuscript Algorithm 3.2, Phase 2
    """
    ...
```

**`rga.py`** — RGA signal:
```python
def compute_rga(model, representations, structural_dissimilarity) -> float:
    """Spearman correlation between representational and structural 
    dissimilarity matrices (RDMs).
    
    Returns
    -------
    r_A : float — RGA signal in [0, 1]
    """
    ...
```

**`ac.py`** — AC signal:
```python
def compute_ac(model, x, augmentations) -> float:
    """Mean cosine similarity of representations across augmentations.
    
    Returns
    -------
    c_A : float — AC signal in [0, 1]
    """
    ...
```

**`fusion.py`** — Weighted fusion:
```python
def fuse_signals(g_A, r_A, c_A, weights=None) -> float:
    """Fuse GCA, RGA, AC signals into operative sigma proxy.
    
    sigma_tilde = w_g * g_A + w_r * r_A + w_c * c_A
    
    If |sigma_tilde - sigma_hat| > 0.15, recalibrate weights
    via ridge regression (Algorithm 3.2, Phase 4).
    """
    ...

def recalibrate_weights(sigma_tilde, sigma_hat, g_A, r_A, c_A):
    """Ridge regression recalibration of fusion weights."""
    ...
```

### II-b: Integration into Training Loop (1h)

In `code/sigma/models/training.py`:

1. After each evaluation epoch, call `compute_gca()`, `compute_rga()`, `compute_ac()` on the validation set
2. Pass `(g_A, r_A, c_A)` to `fuse_signals()` → `sigma_tilde`
3. Store both `sigma_hat = acc_ood / acc_id` and `sigma_tilde` in metrics
4. If `|sigma_tilde - sigma_hat| > 0.15`, call `recalibrate_weights()`

This is the **default path**. The old `ode_state["sigma"]` assignment becomes a fallback when probe data is unavailable.

### II-c: Config Updates (0.5h)

Add to `base.yaml`:
```yaml
estimation:
  fusion_weights:
    gca: 0.4
    rga: 0.35
    ac: 0.25
  recalibration:
    threshold: 0.15
    method: ridge
    alpha: 1.0
  probe:
    batch_size: 128
    n_batches: 10
```

## Phase III — Notebook Dedup (~1.5h)

### III-a: Transfer Inline Code → Package Imports (1h)

`experiments/h-bar-experiment.ipynb` Cell 4 and `experiments/kaggle-pilot-optimised.ipynb` lines 491–678 both reimplement the training loop inline.

Replace with imports:
```python
from sigma.ode.solver import SigmaODESolver
from sigma.models.training import train_sigma_model
from sigma.config import load_config

config = load_config("experiments/configs/base.yaml", "experiments/configs/h-ptb.yaml")
solver = SigmaODESolver(config["ode"])
results = train_sigma_model(model, dataloaders, solver, config)
```

### III-b: Remove Dead Code (0.5h)

After confirming notebooks work with imports:
1. Remove the inline `train_hbar_model()` from both notebooks
2. Remove the inline `SigmaODESolver` clone from notebooks
3. Verify all outputs reproduce within numerical tolerance

## Test Plan

### New Unit Tests

| Test | File | What it verifies |
|------|------|------------------|
| `test_compute_rhs` | `tests/test_ode.py` | `compute_rhs()` matches analytical expectations: zero at sigma=0, positive bracket → d_sigma > 0 |
| `test_imex_solver_basic` | `tests/test_ode.py` | Solver runs to completion, state stays in [0,1], monotonicity for simple params |
| `test_imex_adaptive_step` | `tests/test_ode.py` | dt is reduced when error > tol, increased when error << tol |
| `test_jacobian_condition` | `tests/test_ode.py` | kappa(J) < 1e6 for typical params (Prop 3.5) |
| `test_invariant_manifold` | `tests/test_ode.py` | sigma=0 init stays at 0 (Prop 3.2 fix) |
| `test_fusion_pipeline` | `tests/test_estimation.py` | fuse_signals() returns convex combination |
| `test_recalibration` | `tests/test_estimation.py` | Ridge adjustment reduces |sigma_tilde - sigma_hat| |
| `test_gca_basic` | `tests/test_estimation.py` | GCA returns value in [0,1] |
| `test_rga_basic` | `tests/test_estimation.py` | RGA returns value in [0,1] |
| `test_ac_basic` | `tests/test_estimation.py` | AC returns value in [0,1] |

### Verification Workflow

```bash
# After each phase:
source hbar_env/bin/activate
ruff check code/sigma/          # no new warnings
pytest tests/ -v                # all pass
PYTHONPATH=code:$PYTHONPATH python scripts/smoke_test.py

# Full verification after Phase III:
jupyter nbconvert --to notebook --execute experiments/h-bar-experiment.ipynb
jupyter nbconvert --to notebook --execute experiments/h-bar-v3-cognitive-evaluation-benchmark-suite.ipynb
```

## Implementation Order

| Phase | Step | Description | Est. Time |
|-------|------|-------------|-----------|
| I-a | compute_rhs() | Vector RHS replacing standalone ODE functions | 1h |
| I-b | IMEX solver | Adaptive RK4 + Heun embedded error estimation | 2h |
| I-c | Config alignment | YAML + schema for solver params | 0.5h |
| I-d | Deprecation wrapper | PhenomSolver legacy path | 0.5h |
| II-a | Estimation module | GCA/RGA/AC + fusion subpackage | 2h |
| II-b | Training integration | Hooks in train_sigma_model() | 1h |
| II-c | Config updates | YAML for estimation params | 0.5h |
| III-a | Notebook dedup | Replace inline code with imports | 1h |
| III-b | Dead code removal | Strip inline training loops | 0.5h |
| **Total** | | | **~9.5h** |

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| IMEX solver diverges for extreme params | Medium | High | Stiffness monitoring + clipping; fall back to PhenomSolver |
| GCA requires gradient computation per probe batch | Medium | Low | Use existing task_gradients from training loop; cache when possible |
| Notebook outputs change after dedup | Low | Medium | Compare key metrics (final sigma, phase, OOD gap) within tolerance |
| Recalibration triggers too frequently | Low | Low | Tune threshold via config; add cooldown period |
| Existing tests break from rename | Low | Medium | Grep for old names post-rename; run full test suite |
