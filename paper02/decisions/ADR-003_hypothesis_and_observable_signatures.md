# ADR-003: Scientific Hypotheses Formulation & Observable Bifurcation Signatures

**Date:** 2026-08-23  
**Status:** Approved  
**Phase:** P02  
**Deciders:** Principal Investigator & AI Agent  

---

## 1. Context & Problem Statement
In Phase 02 (Task 2.1), we established the mathematical reduction of task and substitution-consistency losses to the two-subspace continuous gradient flow ODE system:
$$\dot{u} = a_S (\theta_S - u) - \lambda b_S u$$
$$\dot{v} = v (\lambda a_C - b_C) - \kappa v^2$$
which analytically predicts a supercritical transcritical bifurcation at critical compositional pressure $\lambda_{\text{crit}} = b_C / a_C$.

To elevate this mathematical reduction into an empirical scientific discovery for deep neural networks (Transformers on SCAN, COGS, H-Bar), we must formulate exact, falsifiable hypotheses ($H_0$, $H_{\text{null}}$, $H_{\text{alt}}$) and define unambiguous, machine-measurable dynamical signatures capable of isolating the true underlying mechanism in the Phase 03 Gate experiment.

---

## 2. Decision Drivers
- **Driver 1 (Falsifiability & Mechanism Isolation):** The hypothesis must be sharply differentiated from standard smooth dose-response curves and scale-only phenomenologies.
- **Driver 2 (Machine-Measurable Signatures):** Signatures must be operationalized with explicit mathematical formulas and empirical thresholds.
- **Driver 3 (Experimental Feasibility):** Signatures must be measurable in standard PyTorch transformer training runs without requiring intractable Hessian inversions at every step.

---

## 3. Hypotheses Taxonomy

### 3.1 Central Hypothesis ($H_0$ — Critical Compositional Pressure & Transcritical Bifurcation)
**Formal Statement:**  
In deep neural architectures trained under joint task loss $\mathcal{L}_{\text{task}}$ and primitive-substitution equivalence loss $\mathcal{L}_{\text{comp}}$ parameterized by pressure $\lambda$, the transition from shortcut-entrapment ($E_S$, where schema coherence $v = 0$ and OOD accuracy $\approx 0\%$) to compositionally coherent generalisation ($E_C$, where $v > 0$ and OOD accuracy $\to 100\%$) is governed by a **supercritical transcritical bifurcation** at a finite critical threshold:
$$\lambda_{\text{crit}} = \frac{b_C}{a_C} > 0$$

Under $H_0$:
- For $\lambda < \lambda_{\text{crit}}$, $E_S$ is a stable attractor with transverse Lyapunov exponent $\mu_\perp < 0$; the system remains trapped indefinitely in the $\sigma$-trap ($P(\text{escape} \mid \lambda) = 0$).
- For $\lambda > \lambda_{\text{crit}}$, $E_S$ becomes unstable ($\mu_\perp > 0$), and representations escape towards $E_C$ in finite latency $\tau(\lambda) \propto (\lambda - \lambda_{\text{crit}})^{-1}$.

---

### 3.2 Competing Null & Alternative Hypotheses

#### Null Hypothesis ($H_{\text{null}}$ — Smooth Dose-Response Drift)
**Statement:**  
Out-of-distribution (OOD) compositional generalization is a smooth, continuous, differentiable sigmoid function of pressure $\lambda$:
$$\text{Acc}_{\text{OOD}}(\lambda) = \frac{1}{1 + e^{-k(\lambda - \lambda_0)}}$$
Under $H_{\text{null}}$, there is no non-differentiable phase boundary ($\lambda_{\text{crit}}$ does not represent a stability exchange), no infinite-time entrapment separatrix, and small perturbations around $\lambda = 0$ yield continuous marginal gains without qualitative changes in internal representation geometry.

#### Alternative Hypothesis ($H_{\text{alt}}$ — Scale-Only / No Structural Threshold)
**Statement:**  
Compositional failure and recovery depend solely on raw model capacity ($N_{\text{params}}$) and token dataset size ($D_{\text{tokens}}$) via empirical scaling laws $\text{Acc}_{\text{OOD}} \propto N^{-\alpha_N} D^{-\alpha_D}$. Under $H_{\text{alt}}$, explicit compositional pressure $\lambda$ does not exhibit a non-zero threshold law ($\lambda_{\text{crit}} \to 0$ or undefined), and architecture scale alone guarantees emergence without structural regularization.

---

## 4. Observable Dynamical Signatures & Falsification Criteria

To empirically discriminate $H_0$ against $H_{\text{null}}$ and $H_{\text{alt}}$, we specify three distinct, observable signatures:

```
                          ┌───────────────────────────────────────────────────┐
                          │   Observable Signatures of Bifurcation Law        │
                          └───────────────────────────────────────────────────┘
                                   │                   │                   │
         ┌─────────────────────────┴─────────┐         │         ┌─────────┴────────────────────────┐
         ▼                                   ▼         ▼         ▼                                  ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐ ┌──────────────────────────────────────┐
│ Signature 1: Separatrix       │ │ Signature 2: Late-Onset Escape│ │ Signature 3: Critical Slowing Down   │
│ P(escape | λ) Step Function   │ │ Destabilization at t_switch   │ │ τ(λ) ∝ (λ - λ_crit)^(-1) Divergence  │
└───────────────────────────────┘ └───────────────────────────────┘ └──────────────────────────────────────┘
```

### 4.1 Signature 1: Step-Function Escape Probability ($P(\text{escape} \mid \lambda)$)
- **Mathematical Prediction:**  
  Across multi-seed training ensembles, the asymptotic probability of escaping the shortcut state $E_S$ satisfies a Heaviside step function:
  $$P(\text{escape} \mid \lambda, T_{\max}) = \begin{cases} 0 & \text{if } \lambda < \lambda_{\text{crit}} \\ 1 & \text{if } \lambda > \lambda_{\text{crit}} \end{cases}$$
- **Falsification Metric:**  
  The transition sharpness index $S = \left. \frac{d P(\text{escape})}{d \lambda} \right|_{\lambda_{\text{crit}}}$.  
  - If $S \to \infty$ (finite-sample steepness exceeds sigmoid bound by $> 5\times$), $H_0$ is supported.
  - If $P(\text{escape})$ increases smoothly across a broad span $\Delta \lambda$, $H_{\text{null}}$ is favored.

### 4.2 Signature 2: Late-Onset Destabilization & Rescue
- **Mathematical Prediction:**  
  Let a model be trained with $\lambda_1 < \lambda_{\text{crit}}$ up to step $t_{\text{switch}} \ge 1000$, ensuring complete entrapment at $E_S$ ($\sigma_A \approx 0$, ID $\ge 99\%$, OOD $\approx 0\%$). Abruptly increasing pressure to $\lambda_2 > \lambda_{\text{crit}}$ at $t = t_{\text{switch}}$ immediately renders $E_S$ linearly unstable ($\mu_\perp > 0$), inducing rapid exponential divergence away from $E_S$ and convergence to $E_C$.
- **Falsification Metric:**  
  $\left. \frac{d v}{dt} \right|_{t = t_{\text{switch}}^+} > 0$. If the model remains permanently trapped despite $\lambda_2 > \lambda_{\text{crit}}$ (e.g. irreversibly locked by dead neurons/frozen optimizer momentum), or if recovery requires full retraining from scratch, $H_0$ is modified/falsified.

### 4.3 Signature 3: Monotonic Rate Ordering & Critical Slowing Down
- **Mathematical Prediction:**  
  For supercritical pressures $\lambda > \lambda_{\text{crit}}$, the escape latency $\tau(\lambda)$ (steps required to achieve $90\%$ schema coherence) strictly decreases monotonically with $(\lambda - \lambda_{\text{crit}})$, diverging near the critical point:
  $$\tau(\lambda) = \frac{1}{\lambda a_C - b_C} \ln\left(\frac{C}{v_0}\right) \propto (\lambda - \lambda_{\text{crit}})^{-1}$$
- **Falsification Metric:**  
  - Spearman rank correlation $\rho(\tau(\lambda), \lambda) = -1.0$.
  - Log-log linearity $\ln \tau \sim -\beta \ln(\lambda - \lambda_{\text{crit}})$ with exponent $\beta \approx 1.0 \pm 0.2$.

---

## 5. Summary Decision & Gate Linkage
- **Primary Mechanism Gate (Phase 03):** Designates Signature 1 ($P(\text{escape} \mid \lambda)$ step sharpness) and Signature 2 (late-onset destabilization) as the strict non-negotiable exit criteria for the Phase 03 Gate.
- **Traceability:** Mapped to claims `CLM-003` ($P(\text{escape})$ separatrix), `CLM-004` (late-onset recovery), and `CLM-005` (rate ordering).

---

## 6. Multi-Variable Risk Scoring Matrix & Gate Allocation

To rigorously isolate theoretical vulnerabilities and enforce the principle that *evidence gates ambition*, all key theoretical assumptions are scored and bound to concrete mitigation phases:

| Rank | Assumption | Failure Mechanism | Probability (1–5) | Impact (1–5) | Risk Score (P $\times$ I) | Mitigation / Gate Assignment |
|:---:|---|---|:---:|:---:|:---:|---|
| **1** | Deep Transformer OOD transition exhibits a sharp supercritical separatrix $P(\text{escape} \mid \lambda) \in \{0, 1\}$. | Finite-size smoothing makes transition indistinguishable from a gradual dose-response curve. | 3 | 5 | **15 (High)** | **Designated as Phase 03 Mechanism Gate Target** (`gate-result.md`) |
| **2** | Continuous gradient flow accurately bounds discrete SGD transition timing. | High stochastic learning rate noise destroys deterministic phase boundary. | 2 | 4 | **8 (Med)** | Diffrax stochastic SDE analysis in P05 |
| **3** | CKA representation geometry acts as a true leading order parameter. | CKA changes concurrently with or after OOD accuracy. | 3 | 3 | **9 (Med)** | Granger lead-lag evaluation in P07 |
| **4** | $\lambda_{\text{crit}}$ is invariant across syntactic benchmark families. | Grammar-specific shortcut correlations shift $\lambda_{\text{crit}}$ unpredictably. | 2 | 4 | **8 (Med)** | Cross-benchmark sweep (SCAN, COGS, H-Bar) in P06 |

### Governance Binding:
1. **Risk #1 Binding:** No downstream manuscript drafting (P08) or large-scale multi-benchmark sweep (P06) will commence until the Phase 03 Gate evaluates 450 seeds across Arms A & B and records an unambiguous **PASS** in `paper02/planning/gate-result.md`.
2. **Mitigation Traceability:** Every risk rank 2–4 maps to an explicit diagnostic subtask in Phases 05, 06, and 07, ensuring complete experimental coverage before final submission.
