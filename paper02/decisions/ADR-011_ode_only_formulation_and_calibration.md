# ADR-011: Deterministic ODE-Only Formulation and Parameter Calibration

## 1. Context & Status
- **Status:** **APPROVED (Ratified by PI Directive 2026-08-27)**
- **Date:** 2026-08-27
- **Deciders:** Principal Investigator, Lead Research Agent
- **Phase:** Pre-Phase 06 Governance Remediation
- **Framework:** RPF v2.0.0
- **Supersedes:** Legacy references to "Diffrax SDE", "stochastic Langevin diffusion", and uncalibrated toy ODE defaults.

---

## 2. Decision: Ratification of Deterministic ODE Continuous Reference Model

### 2.1 Formal Formulation (Option A Ratification)
The formal theoretical reference model for Paper 02 is strictly a deterministic two-subspace continuous gradient flow ODE dynamical system:
$$\frac{du}{dt} = a_S (\theta_S - u) - \lambda b_S u$$
$$\frac{dv}{dt} = v (\lambda a_C - b_C) - \kappa v^2$$

- **State Variables:**
  - $u(t) \in [0, 1.5]$: Alignment of network representations with the shortcut subspace $\mathcal{U}_S$.
  - $v(t) \in [0, 1.5]$: Alignment of network representations with the schema / compositional subspace $\mathcal{V}_C$.
- **Superseded Formulations:** All references to stochastic differential equations (SDEs), Brownian motion ($dW_t$), or stochastic Diffrax integrators are formally superseded. No stochastic diffusion term is required for Paper 02 claims.

---

## 3. Parameter Calibration to Locked Empirical Critical Pressure

### 3.1 Empirical Anchor
The empirical Mechanism Gate (Phase 03 / Phase 03.1) locked the empirical critical supervision pressure:
$$\hat{\lambda}_{\text{crit}} = 0.025 \pm 0.005$$

### 3.2 ODE Parameter Calibration
Under continuous gradient flow, the theoretical transcritical bifurcation occurs at:
$$\lambda_{\text{crit}} = \frac{b_C}{a_C}$$

To maintain exact numerical and visual alignment between theoretical phase portraits and empirical learning dynamics:
- $a_C = 1.0$ (Schema alignment gain)
- $b_C = 0.025$ (Schema damping under shortcut-dominated task loss)
- $\lambda_{\text{crit}} = \frac{0.025}{1.0} = 0.025$

### 3.3 Default Parameter Set (`TwoSubspaceParams`)
```python
a_S: float = 1.0
theta_S: float = 1.0
b_S: float = 0.5
a_C: float = 1.0
b_C: float = 0.025  # Calibrated to locked lambda_crit = 0.025
kappa: float = 1.0
lambda_val: float = 0.0
```

---

## 4. Consequences & Governance
- `two_subspace_ode.py` and `solver.py` default to calibrated $\lambda_{\text{crit}} = 0.025$.
- Unit tests verify `sys.lambda_crit == 0.025`.
- Theoretical bifurcation diagrams directly match empirical transition curves without heuristic scaling.
