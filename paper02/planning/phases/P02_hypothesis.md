# Phase 02 — Hypothesis Formulation, Mathematical Reduction & Risk Scoring

**Phase ID:** P02  
**Phase Title:** Formal Theoretical Reduction, Analytical Bifurcation Derivation, and Multi-Variable Risk Scoring  
**Status:** ✅ Complete (RPF v1, migrated to v2.0) — feeds P02.5 preregistration  
**Duration:** 1–2 Days  
**Dependencies:** P01  
**Executor:** Agent (70%) / Human-Gate (30%)  
**Deliverables:** `paper02/decisions/ADR-001_two_subspace_formulation.md` (formalized), updated `paper02/planning/ledger.md`, `paper02/src/continuous/two_subspace_ode.py` (analytical prototype)

**RPF v2.0:** Git tag `p02-hypothesis` · RACI: Agent **R** / PI **A** (hypothesis + gate target approval; no autonomous fallback) · Abort: none · Acceptance: ADR-003 with H₀/H₁/falsification criterion, `planning/risk-register.md`, `decide-at-P03` ledger rows · **Closed under v1.0.0, migrated 2026-08-23; hypothesis + observable signatures in `decisions/ADR-003_hypothesis_and_observable_signatures.md`; risk register seeded (v2.0).**

---

## 1. Purpose & Scope
Formulate the central scientific hypothesis $H_0$ of Paper 02 in exact, uncompromised mathematical terms. Derive the continuous gradient flow equations in the two-subspace reduction, calculate the transverse Jacobian eigenvalue $\mu_\perp$, score the riskiest assumptions, and designate the empirical Phase 03 Gate target.

---

## 2. Exhaustive Tasks & Subtasks

### Task 2.1: Mathematical Derivation of the Two-Subspace Reduction
1. **Define Parameter & Feature Spaces:**
   - Input decomposition: $x = (s, c) \in \mathbb{R}^{d_S} \times \mathbb{R}^{d_C}$, where $s$ is the task shortcut feature and $c$ is the compositional feature.
   - Student network parameters: $w = (u, v) \in \mathbb{R}^{d_S} \times \mathbb{R}^{d_C}$, output $f_w(x) = u^\top s + v^\top c$.
2. **Formulate Continuous Loss Gradients:**
   - Task loss: $\mathcal{L}_{\text{task}}(u, v) = \frac{1}{2} \mathbb{E}_{(s,c,y) \sim \mathcal{D}_{\text{ID}}} [(u^\top s + v^\top c - y)^2]$.
     - Shortcut gradient: $\nabla_u \mathcal{L}_{\text{task}} = a_S (u - \theta_S)$.
     - Schema gradient under shortcut-learning pressure: $\nabla_v \mathcal{L}_{\text{task}} = b_C v + \mathcal{O}(v^2)$ with $b_C > 0$.
   - Compositional loss under primitive substitution $\mathcal{D}_{\text{equiv}}$:
     $\mathcal{L}_{\text{comp}}(u, v) = \frac{1}{2} \mathbb{E}_{(x,x') \sim \mathcal{D}_{\text{equiv}}} [(f_w(x) - f_w(x'))^2]$.
     - Shortcut invariance penalty: $\nabla_u \mathcal{L}_{\text{comp}} = b_S u$.
     - Schema alignment pressure: $\nabla_v \mathcal{L}_{\text{comp}} = -a_C v + \kappa v^2$.
3. **Continuous Gradient Flow System:**
   $$\dot{u} = a_S (\theta_S - u) - \lambda b_S u$$
   $$\dot{v} = v (\lambda a_C - b_C) - \kappa v^2$$
4. **Jacobian Transverse Spectrum & Stability Exchange:**
   - Shortcut equilibrium: $E_S = (u_S^*, 0) = \left( \frac{a_S \theta_S}{a_S + \lambda b_S}, \, 0 \right)$.
   - Transverse eigenvalue at $E_S$:
     $$\mu_\perp = \left. \frac{\partial \dot{v}}{\partial v} \right|_{v=0} = \lambda a_C - b_C$$
   - Critical threshold:
     $$\lambda_{\text{crit}} = \frac{b_C}{a_C}$$
   - **Transcritical Stability Exchange:**
     - For $\lambda < \lambda_{\text{crit}}$: $\mu_\perp < 0 \implies E_S$ is asymptotically stable ($\sigma$-trap).
     - For $\lambda > \lambda_{\text{crit}}$: $\mu_\perp > 0 \implies E_S$ is unstable; non-trivial coherent equilibrium $E_C = (u^*, v^*)$ emerges:
       $$v^* = \frac{\lambda a_C - b_C}{\kappa} > 0$$

### Task 2.2: Hypotheses & Observable Signatures
1. **Central Hypothesis ($H_0$):**
   *Statement:* In deep neural networks optimizing task loss alongside substitution-consistency supervision, the transition from shortcut-mastery ($E_S$) to compositional schema coherence ($E_C$) is governed by a supercritical transcritical bifurcation at a finite critical threshold $\lambda_{\text{crit}}$.
2. **Competing / Null Hypotheses:**
   - *Null Hypothesis ($H_{\text{null}}$ - Smooth Dose-Response):* OOD generalization is a continuous, smooth sigmoid function of $\lambda$ with no non-differentiable phase boundary and no bistable separatrix.
   - *Alternative Hypothesis ($H_{\text{alt}}$ - Scale-Only / No Threshold):* OOD generalization depends solely on model capacity and dataset size; no non-zero $\lambda_{\text{crit}}$ exists.
3. **Observable Predicted Signatures:**
   - *Signature 1 (Step Function Escape Probability):* $P(\text{escape} \mid \lambda) \approx 0$ for $\lambda < \lambda_{\text{crit}}$ and $P(\text{escape} \mid \lambda) \approx 1$ for $\lambda > \lambda_{\text{crit}}$.
   - *Signature 2 (Late-Onset Destabilization):* Introducing $\lambda > \lambda_{\text{crit}}$ at step $t_{\text{int}} = 1000$ (after full entrapment) triggers rapid escape from $E_S$.
   - *Signature 3 (Monotonic Rate Ordering):* $\hat{\tau}(\lambda)$ decreases monotonically as $\lambda - \lambda_{\text{crit}}$ increases.

### Task 2.3: Multi-Variable Risk Scoring & Gate Isolation
1. **Build the Quantitative Risk Matrix:**
   | Rank | Assumption | Failure Mechanism | Probability (1–5) | Impact (1–5) | Risk Score (P $\times$ I) | Mitigation / Gate Assignment |
   |:---:|---|---|:---:|:---:|:---:|---|
   | **1** | Deep Transformer OOD transition exhibits a sharp supercritical separatrix $P(\text{escape} \mid \lambda) \in \{0, 1\}$. | Finite-size smoothing makes transition indistinguishable from a gradual dose-response curve. | 3 | 5 | **15 (High)** | **Designated as Phase 03 Gate Target** |
   | **2** | Continuous gradient flow accurately bounds discrete SGD transition timing. | High stochastic learning rate noise destroys deterministic phase boundary. | 2 | 4 | **8 (Med)** | Diffrax stochastic SDE analysis in P05 |
   | **3** | CKA representation geometry acts as a true leading order parameter. | CKA changes concurrently with or after OOD accuracy. | 3 | 3 | **9 (Med)** | Granger lead-lag evaluation in P07 |
   | **4** | $\lambda_{\text{crit}}$ is invariant across syntactic benchmark families. | Grammar-specific shortcut correlations shift $\lambda_{\text{crit}}$ unpredictably. | 2 | 4 | **8 (Med)** | Cross-benchmark sweep in P06 |

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator formally approves $H_0$, the analytical derivation in ADR-001, and the designation of Risk #1 as the Phase 03 Gate target.

---

## 4. Machine-Checkable Exit Criteria
- [x] `paper02/decisions/ADR-001_two_subspace_formulation.md` contains the complete analytical proof of $\lambda_{\text{crit}} = b_C / a_C$.
- [x] `paper02/planning/ledger.md` populated with CLM-001 through CLM-007.
- [x] Risk scoring table complete with all 4 assumptions quantified.
- [x] Prototype ODE simulation script `paper02/src/continuous/two_subspace_ode.py` executes and plots theoretical bifurcation diagram.
- [ ] `[HUMAN-GATE]` Hypothesis approval signed off.

---

## 5. Deliverables & Artifacts
- Decision record: `paper02/decisions/ADR-001_two_subspace_formulation.md`
- Decision record: `paper02/decisions/ADR-003_hypothesis_and_observable_signatures.md`
- Prototype ODE solver: `paper02/src/continuous/two_subspace_ode.py`
- Observable signatures module: `paper02/src/continuous/observable_signatures.py`
- Diagnostic figures: `paper02/writing/figures/two_subspace_bifurcation.png`, `paper02/writing/figures/observable_signatures.png`
- Scope updates: `paper02/planning/ledger.md`
