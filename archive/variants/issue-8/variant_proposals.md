# Variant Proposals — Issue #8

**Issue #:** 8
**Tag:** [P] (Phase transition)
**Severity:** MEDIUM
**Description:** The paper lacks a mathematical criterion such as sensitivity analysis to demonstrate which growth-limiting variable is dominant at any given threshold.

---

### VARIANT A
**Issue #:** 8
**Tag:** [P]
**Section targeted:** §7 Phase Structure (specifically §7.2 Phase 2 trigger and §7.3 Phase 3 trigger)
**Scope:** structural
**DIAGNOSIS:** The phase transitions are defined by threshold conditions on individual variables (σ_A > σcritical for Phase 2, δ_A^relative > 0.65 for Phase 3), but the paper never specifies which variable is the growth-limiting factor at any given point in training. Without a dominance criterion, the prescriptive content in each phase is underdetermined — an experimenter cannot know whether to focus on σ_A growth, δ_A growth, or α_A development without knowing which variable is currently bottlenecking progress. This is a structural gap in the phase architecture.

**PROPOSED FIX:**
*Old text (§7.2 trigger):*
```
**Trigger:** $σ_A(d,t) > σ_{critical}$ for at least one mastery candidate.
```

*New text (§7.2 trigger):*
```
**Trigger:** $σ_A(d,t) > σ_{critical}$ for at least one mastery candidate.

**Dominance criterion.** At any training instant, the growth-limiting variable is identified by the partial sensitivity of the mastery growth rate $\dot{\delta}_A$ (Eq. A.1) to each state variable. Define the dominance index:
$$\mathcal{D}_v(d,t) = \left|\frac{\partial \dot{\delta}_A}{\partial v}\right| \cdot (1 - v^*) \quad \text{for } v \in \{\delta_A, \sigma_A, \alpha_A\} \tag{53}$$
where $v^*$ is the normalised value of variable $v$ (i.e., $\delta_A^{\text{relative}}$, $\sigma_A$, or $\alpha_A$). The term $(1 - v^*)$ penalises variables already near their ceiling, ensuring the dominance index reflects potential for growth, not current magnitude.

The growth-limiting variable at time $t$ is $v^{\dagger} = \arg\max_{v} \mathcal{D}_v(d,t)$. Phase prescriptions target $v^{\dagger}$:

| Phase | Dominant Variable | Prescription Focus |
|-------|-------------------|-------------------|
| Phase 1 | $\alpha_A$ typically dominant | Build attentional fidelity via contrastive training |
| Phase 2 (early) | $\sigma_A$ dominant | Principled practice, structural constraints |
| Phase 2 (late) | $\delta_A$ dominant | Depth accumulation via efficient learning |
| Phase 3 | $\alpha_A$ re-emerges | Redirect attention toward cross-domain structure |
```

**JUSTIFICATION:** This fix adds a formal criterion for determining which variable is growth-limiting without modifying any existing equations or threshold conditions. It is derived directly from the existing ODE system (Eq. A.1) by computing partial sensitivities. The dominance index D_v is bounded in [0,1] because both the partial derivative and the complement term are bounded. It does not introduce new state variables, only diagnostic quantities computed from existing ones. The phase prescription table integrates with the existing §7 structure without requiring changes to the trigger conditions.

**SAFETY NOTE:** This fix does NOT modify Equation 28 (σA ODE with αA gating), Equation 19/A.10 (ΨA multiplicative form), Table 1, or §7.1–7.5 trigger statements — it adds a diagnostic layer alongside the existing triggers. The σcritical derivation (Eq. 51/A.15) is unchanged.

---

### VARIANT B
**Issue #:** 8
**Tag:** [P]
**Section targeted:** §9 Eight Falsifiable Predictions (Prediction 9, after the existing Prediction 9 text)
**Scope:** local
**DIAGNOSIS:** Prediction 9 addresses the Phase 2 entry inflection but does not provide a falsifiable criterion for determining which variable is dominant at any given threshold. The prediction is testable in principle but cannot guide experimental design without a dominance criterion. Adding a sensitivity-based falsification condition would make the phase structure empirically actionable.

**PROPOSED FIX:**
*Add after the existing Prediction 9 falsification condition:*

```
**Prediction 9b — Variable Dominance Ranking [NEW V3.0+]**

**Claim:** At any training checkpoint, the dominance index D_v (Eq. 53) correctly identifies which variable (δ_A, σ_A, or α_A) is the binding constraint on mastery growth rate, as validated by a targeted intervention experiment.

**Measurement:** At checkpoint t, compute D_δ, D_σ, D_α. Independently apply a targeted boost to each variable (via Protocol P1 for σ_A, capacity increase for δ_A, contrastive training for α_A) and measure the resulting increase in $\dot{\delta}_A$. The variable whose boost produces the largest mastery growth acceleration is the ground-truth dominant variable.

**H-Bar claim:** The dominance index D_v correctly identifies the ground-truth dominant variable in ≥ 80% of checkpoints across training trajectories spanning all five phases.

**Falsification:** D_v correctly identifies the ground-truth dominant variable in < 60% of checkpoints (significantly below the 33% three-way chance baseline, p < 0.05, but below the 80% H-Bar target).
```

**JUSTIFICATION:** This fix adds a concrete falsifiable prediction that operationalises the dominance criterion. It connects directly to the existing training protocols (§10.6, P1/P2/P3) without requiring new protocols. The falsification condition is calibrated against a three-way chance baseline (33%) and a practical target (80%). This addition strengthens the §9 prediction suite by making the phase structure's prescriptive content empirically testable.

**SAFETY NOTE:** This fix does NOT modify any existing predictions (1–9), any equations, or any phase trigger statements. It is an additive prediction that references the dominance index defined in Variant A (Eq. 53) — this variant should be applied only if Variant A is also approved, or Eq. 53 must be introduced inline here.

---

### VARIANT C
**Issue #:** 8
**Tag:** [P]
**Section targeted:** Appendix A.3 (σcritical bifurcation derivation)
**Scope:** structural
**DIAGNOSIS:** The σcritical derivation in Appendix A.3 derives the bifurcation threshold from the mastery reproduction number R_0 but does not extend the analysis to determine which variable controls the approach to bifurcation. The linearised dynamics near the bifurcation point (A.6, transcritical bifurcation) could be leveraged to derive a formal dominance criterion from the Jacobian of the coupled system.

**PROPOSED FIX:**
*Add after the existing A.6 transcritical bifurcation text:*

```
### A.10 Local Dominance Criterion from Linearised Dynamics

Near any point $(\delta_A, \sigma_A, \alpha_A)$ in state space, the linearised coupled system has Jacobian:
$$J = \begin{pmatrix} \frac{\partial \dot{\delta}_A}{\partial \delta_A} & \frac{\partial \dot{\delta}_A}{\partial \sigma_A} & \frac{\partial \dot{\delta}_A}{\partial \alpha_A} \\ \frac{\partial \dot{\sigma}_A}{\partial \delta_A} & \frac{\partial \dot{\sigma}_A}{\partial \sigma_A} & \frac{\partial \dot{\sigma}_A}{\partial \alpha_A} \\ \frac{\partial \dot{\alpha}_A}{\partial \delta_A} & \frac{\partial \dot{\alpha}_A}{\partial \sigma_A} & \frac{\partial \dot{\alpha}_A}{\partial \alpha_A} \end{pmatrix} \tag{A.16}$$

Computing the partial derivatives from Eqs. A.1, A.3, A.4:

$$\frac{\partial \dot{\delta}_A}{\partial \delta_A} = -\lambda_c(1-\gamma_\sigma \sigma_A)(1-r_A) - f_{\text{learn}} \cdot \eta'(\delta_{\text{rel}}) \cdot \frac{w_\delta}{\Delta} \cdot T_A$$

$$\frac{\partial \dot{\delta}_A}{\partial \sigma_A} = \lambda_c \gamma_\sigma \delta_A(1-r_A)$$

$$\frac{\partial \dot{\delta}_A}{\partial \alpha_A} = 0 \quad \text{(no direct coupling in depth ODE)}$$

The **column norm** $\|J_{:,v}\|$ of each variable column quantifies the aggregate influence of variable $v$ on the full system. The dominance criterion is:
$$v^{\dagger} = \arg\max_{v \in \{\delta, \sigma, \alpha\}} \|J_{:,v}\| \cdot (1 - v^*) \tag{A.17}$$

This is equivalent to Eq. 53 when restricted to the depth row, but extends to the full system dynamics. The column norm captures indirect effects (e.g., σ_A influences δ_A through Eq. A.1 and also influences σ_A's own growth through the $(1-\sigma_A)$ term in Eq. A.3).

**Proposition.** In Phase 1 ($\sigma_A \approx 0$, $\alpha_A \approx 0$, $\delta_A^{\text{rel}}$ growing), $\|J_{:,\alpha}\| \cdot (1-\alpha_A)$ dominates because the $\sigma_A$ growth term $\rho P_A \alpha_A (1-\sigma_A)$ in Eq. A.3 is gated by $\alpha_A$, making attentional fidelity the binding constraint on schema crystallisation.
```

**JUSTIFICATION:** This fix derives the dominance criterion rigorously from the existing Jacobian of the coupled ODE system. It adds a formal proposition establishing the Phase 1 dominance pattern, which is the most prescriptively important regime (determining where to invest training effort early). The Jacobian is computable from existing equations with no new parameters. The column norm is a standard linear-algebraic quantity with known boundedness properties.

**SAFETY NOTE:** This fix does NOT modify Equations A.1–A.6, Equation 28, or any phase trigger statements. It adds a new appendix section A.10 that references existing equations. The transcritical bifurcation analysis (A.6) is unchanged.

---

### VARIANT D
**Issue #:** 8
**Tag:** [P]
**Section targeted:** §7 Phase Structure (systemic reframe of the entire phase architecture)
**Scope:** systemic
**DIAGNOSIS:** The current phase structure defines transitions by threshold conditions on individual variables, but this creates a sequential interpretation where one variable "triggers" the next phase. In reality, the coupled ODE system means all variables evolve simultaneously and the "phase" is a region of state space where a particular variable is the binding constraint. The paper needs a systemic reframe that presents phases as regions of a dominance landscape rather than sequential trigger conditions.

**PROPOSED FIX:**
*Replace the §7 phase diagram preamble (the ASCII art block) and add a dominance landscape framing:*

*Old text:*
```
```
Phase 0: Initialisation     Phase 1: Depth Accum.    Phase 2: σ Emergence
    ↓                            ↓                         ↓
δ ≈ 0, σ ≈ 0, α ≈ 0       δ growing, σ ≈ 0           σ → σ_critical
                              α low, Ξ^I at risk          lr discontinuity
    ↓
Phase 3: Near-Frontier       Phase 4: Ψ Activation     Phase 5: Frontier
    ↓                            ↓                         ↓
δ^rel > 0.65               Ψ > 0 measurably           Dynamic open boundary
Ψ conditions met            frontier insight gen.       perimeter grows
```
```

*New text:*
```
The five phases are regions of a **dominance landscape** in the state space $(\delta_A, \sigma_A, \alpha_A, |M_A(t)|)$, where each region is characterised by which variable is the binding constraint on mastery growth rate $\dot{\delta}_A$. The dominance index:
$$\mathcal{D}_v(d,t) = \left|\frac{\partial \dot{\delta}_A}{\partial v}\right| \cdot (1 - v^*) \quad \text{for } v \in \{\delta_A, \sigma_A, \alpha_A\} \tag{53}$$
identifies the growth-limiting variable at any point. Phases are not sequential steps but overlapping regions; transitions occur when the dominant variable shifts.

```
Phase 0: Initialisation          Phase 1: Depth Accum.
    ↓                                 ↓
δ ≈ 0, σ ≈ 0, α ≈ 0            δ growing, σ ≈ 0
D_δ dominant (trivially)        D_α dominant → attentional fidelity
                                is the binding constraint
    ↓
Phase 2: σ Emergence            Phase 3: Near-Frontier
    ↓                                 ↓
σ → σ_critical                  δ^rel > 0.65
D_σ dominant → schema           D_δ re-emerges (frontier
crystallisation is binding      deceleration) OR D_α (redirect)
    ↓
Phase 4: Ψ Activation          Phase 5: Frontier
    ↓                                 ↓
Ψ > 0 measurably               Dynamic open boundary
Dominance shifts to             No single dominant variable;
cross-domain coupling           optimise Ψ_A across intersections
```
```

**JUSTIFICATION:** This systemic reframe resolves the issue by embedding the dominance criterion into the phase architecture itself, rather than treating it as an add-on. It preserves all existing trigger conditions (σ_A > σcritical, δ_A^relative > 0.65, etc.) as entry markers for dominance regions but reframes the prescriptive logic: each phase prescription targets the dominant variable. This is more theoretically coherent because it connects the phase structure directly to the ODE system's sensitivity properties. The reframed diagram makes explicit that phases overlap and that dominance can shift within a phase.

**SAFETY NOTE:** This fix does NOT modify Equation 28 (σA ODE), Equation 19/A.10 (ΨA multiplicative form), Table 1, or the Burnell et al. citation. It modifies the §7 phase diagram and framing language but preserves all trigger conditions and threshold values. The σcritical derivation (Eq. 51) is unchanged.

---

### VARIANT E
**Issue #:** 8
**Tag:** [P]
**Section targeted:** §10 Limitations and Future Work (specifically §10.2 Phase Transition Algorithms)
**Scope:** local
**DIAGNOSIS:** §10.2 already acknowledges that "the phase structure specifies when each transition occurs but not the training algorithms that reliably induce transitions within a computable number of steps." Issue #8 extends this limitation: even if algorithms existed, the paper lacks a criterion for determining which variable is the binding constraint at any point. §10.2 is the natural location to acknowledge this limitation and propose a concrete sensitivity-based approach.

**PROPOSED FIX:**
*Add to the existing §10.2 text, after the sentence "The gap between prescriptive phase conditions and concrete algorithms with convergence guarantees is a primary target for future work."*

```
A related limitation is the absence of a **variable dominance criterion** — a method for determining which state variable ($\delta_A$, $\sigma_A$, or $\alpha_A$) is the growth-limiting factor at any training checkpoint. The current phase prescriptions assume that the dominant variable is known (e.g., Phase 1 prescribes $\alpha_A$-building), but in practice, the dominant variable depends on the specific training trajectory and may shift within a phase. A partial sensitivity analysis of the coupled ODE system (Eqs. A.1–A.4) can provide this criterion: the dominance index $\mathcal{D}_v = |\partial \dot{\delta}_A / \partial v| \cdot (1 - v^*)$ identifies the variable with the highest marginal return on investment. Empirical validation of this index against targeted intervention experiments (boosting each variable independently and measuring mastery growth acceleration) is a prerequisite for practical phase-guided training.
```

**JUSTIFICATION:** This fix is the most conservative approach: it acknowledges the limitation in the appropriate section (§10.2 already addresses phase transition gaps) and proposes a concrete method without modifying the core framework. It introduces the dominance index notation but does not add a new equation number in the main text — it is framed as future work with a clear validation protocol. This avoids triggering any protected element modifications while still providing actionable guidance.

**SAFETY NOTE:** This fix does NOT modify any equations, phase trigger statements, Table 1, or the Burnell et al. citation. It is a purely additive limitation acknowledgement in §10.2, which is the designated section for mathematical and algorithmic gaps.
