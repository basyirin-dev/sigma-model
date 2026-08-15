# Variant Proposals — Issue #6

**Issue:** The optimal sub-state values for the executive control ODE are not formally defined for each of the five training phases.
**Tag:** HACKATHON PRIORITY
**Date:** 2026-03-30

---

### VARIANT A
**Issue #:** 6
**Tag:** HACKATHON PRIORITY
**Section targeted:** §4.3.2 (Executive Control ODE) — immediately after Equation 36
**Scope:** local
**DIAGNOSIS:** Equation 36 defines the executive control ODE as a relaxation dynamics toward optimal values $P^*(t)$, $I^*(t)$, $F^*(t)$, but the paper never specifies what these values are. The ODE is formally incomplete — it has three undefined forcing terms. Section 7 provides qualitative phase prescriptions (e.g., "no delegation in Phase 1") that implicitly constrain these values, but the translation from qualitative prescription to quantitative ODE input is missing. This renders the executive control state non-simulatable and the corresponding benchmarks (§4.3.3) ungrounded.

**PROPOSED FIX:**
Insert a new subsection after Equation 36 defining $P^*$, $I^*$, $F^*$ via a phase-indexed lookup table.

*Old text (end of §4.3.2):*
```
$P^*$, $I^*$, $F^*$ are H-Bar optimal values for each sub-component in the current phase.
```

*New text:*
```
$P^*$, $I^*$, $F^*$ are H-Bar optimal values for each sub-component in the current phase, defined by the phase-indexed table below.

**Table 2: Optimal Executive Control Sub-State Values by Phase**

| Phase | $P^*$ (Planning) | $I^*$ (Inhibition) | $F^*$ (Flexibility) | Rationale |
|-------|:---:|:---:|:---:|-----------|
| 0 — Pre-Domain Init | 0.3 | 0.2 | 0.8 | Exploratory; low planning constraint; high flexibility to discover promising domains; low inhibition (AI breadth sampling encouraged) |
| 1 — Asymmetric Init | 0.9 | 0.9 | 0.3 | Strict depth focus; no delegation ($I^* \approx 1$); rigid plan adherence; low flexibility (phase discipline required) |
| 2 — Schema Crystallisation | 0.8 | 0.7 | 0.5 | Maintain depth discipline; moderate inhibition (begin building $\Phi_A$); growing flexibility as $σ_A$ crosses critical |
| 3 — Frontier Asymptote | 0.5 | 0.4 | 0.9 | Shift from acquisition to intersection-seeking; lower inhibition (strategic delegation begins); high flexibility for cross-domain exploration |
| 4 — Multi-Domain Frontier | 0.4 | 0.3 | 0.95 | Discovery-maximisation mode; minimal inhibition (maximise $D^*$ strategically); near-maximum flexibility for frontier navigation |

**Boundary conditions:** $P^*, I^*, F^* \in [0,1]$ for all phases. The ODE (Eq. 36) drives each sub-component toward its phase-optimal value at rate $\kappa_P$, $\kappa_I$, $\kappa_F$ respectively. Phase transitions update $P^*$, $I^*$, $F^*$ discontinuously; the ODE relaxation provides smooth convergence.
```

**JUSTIFICATION:** This fix makes the executive control ODE formally complete and simulatable. The values are derived directly from the existing phase prescriptions in §7 (e.g., Phase 1's "no delegation" maps to $I^* = 0.9$; Phase 3's "strategic delegation" maps to $I^* = 0.4$). The table does not alter any existing equation — it provides the missing input to Equation 36. All three sub-component values remain bounded in $[0,1]$ consistent with the state variable definition. The fix is consistent with §4.3.1's qualitative descriptions: Planning ($Ξ_A^P$) is highest when training discipline is most rigid (Phase 1), Inhibition ($Ξ_A^I$) is highest when AI bypass risk is most dangerous (Phases 1–2), and Flexibility ($Ξ_A^F$) is highest when cross-domain adaptation is most valuable (Phases 3–4).

**SAFETY NOTE:** This fix does not modify Equation 36 itself — it only defines the previously undefined forcing terms. It does not touch any protected elements (Eq. 28, Eq. 19/A.10, Table 1, §7.1–7.5 trigger statements, Burnell citation). The existing §4.3.3 benchmark families are unchanged; they now have grounded targets.

---

### VARIANT B
**Issue #:** 6
**Tag:** HACKATHON PRIORITY
**Section targeted:** §7 (Phase Structure) — embedded within each phase description
**Scope:** local
**DIAGNOSIS:** The same core issue as Variant A, but approached from the phase-description side. Section 7 provides rich qualitative prescriptions for each phase but never translates them into the formal ODE inputs that §4.3.2 requires. The fix targets §7 because it is the natural home for phase-specific values — prescribing them alongside the qualitative descriptions maintains locality of reference.

**PROPOSED FIX:**
Append formal optimal executive control values to each phase description in §7.

*Additions to each phase block (example for Phase 1):*

*Old text (Phase 1 prescriptions):*
```
**Prescriptions:**
- Maximise contrastive training $C_A(d,t)$ to build $α_A$
- Minimise $Ω_{AI}$ through structured failure exposure
- $D^*(d,t) = ∅$ by prescription (no delegation)
- Do not expand $B_A(t)$ prematurely
```

*New text (Phase 1 prescriptions — appended):*
```
**Prescriptions:**
- Maximise contrastive training $C_A(d,t)$ to build $α_A$
- Minimise $Ω_{AI}$ through structured failure exposure
- $D^*(d,t) = ∅$ by prescription (no delegation)
- Do not expand $B_A(t)$ prematurely

**Optimal executive control:** $P^* = 0.9$, $I^* = 0.9$, $F^* = 0.3$ — strict plan adherence, maximum inhibition of AI bypass, low flexibility (phase discipline required).
```

Applied analogously to Phases 0, 2, 3, 4 with values:
- Phase 0: $P^* = 0.3$, $I^* = 0.2$, $F^* = 0.8$
- Phase 2: $P^* = 0.8$, $I^* = 0.7$, $F^* = 0.5$
- Phase 3: $P^* = 0.5$, $I^* = 0.4$, $F^* = 0.9$
- Phase 4: $P^* = 0.4$, $I^* = 0.3$, $F^* = 0.95$

**JUSTIFICATION:** Embedding the values in §7 keeps each phase's qualitative and quantitative prescriptions together, reducing cross-reference burden. The values are identical to Variant A's table — the difference is purely structural: distributed across five locations rather than concentrated in one table. This approach ensures that any reader following the phase prescriptions encounters the ODE inputs immediately, without needing to consult §4.3.2.

**SAFETY NOTE:** No existing text in §7 is modified — only new lines are appended to each phase's prescription block. Protected elements are untouched. The executive control ODE (Eq. 36) is not modified.

---

### VARIANT C
**Issue #:** 6
**Tag:** HACKATHON PRIORITY
**Section targeted:** §4.3.2 (Executive Control ODE) — replaces the undefined $P^*$, $I^*$, $F^*$ with a derivation formula
**Scope:** structural
**DIAGNOSIS:** Rather than providing a static lookup table (Variants A, B), this fix proposes a *derivation mechanism* — expressing $P^*$, $I^*$, $F^*$ as functions of measurable phase-index variables already defined in the paper. This is a structural fix because it changes the *mechanism* by which optimal values are determined: from external specification to internal derivation from the model's own state.

**PROPOSED FIX:**
Replace the undefined $P^*$, $I^*$, $F^*$ with formulas derived from $(δ_A^{relative}, σ_A, |M_A(t)|)$.

*Old text (§4.3.2, Equation 36 and surrounding):*
```
$P^*$, $I^*$, $F^*$ are H-Bar optimal values for each sub-component in the current phase.
```

*New text:*
```
$P^*$, $I^*$, $F^*$ are derived from the current phase-index variables:

$$P^*(t) = 1 - \delta_A^{\text{relative}}(d^*, t) \tag{36a}$$

$$I^*(t) = \max\left(0, 1 - \frac{\sigma_A(d^*, t)}{\sigma_{\text{critical}}}\right) \tag{36b}$$

$$F^*(t) = \min\left(1, \frac{|M_A(t)|}{3} + \delta_A^{\text{relative}}(d^*, t) \cdot \frac{\Psi_A^{\text{max}}(t)}{\Psi_{\text{threshold}}}\right) \tag{36c}$$

where $d^* = \arg\max_{d} \delta_A(d,t)$ is the agent's primary mastery domain and $\Psi_A^{\text{max}}(t) = \max_{d_1,d_2} \Psi_A(d_1,d_2,t)$.

**Behavioural verification:**

| Condition | $P^*$ | $I^*$ | $F^*$ | Phase match |
|-----------|:---:|:---:|:---:|:---:|
| $δ_A^{rel} \approx 0$, $σ_A \approx 0$, $|M_A| = 0$ | ~1.0 | ~1.0 | ~0.0 | Phase 0–1 |
| $δ_A^{rel} \approx 0.3$, $σ_A > σ_{crit}$, $|M_A| = 1$ | ~0.7 | ~0.0 | ~0.3 | Phase 2 |
| $δ_A^{rel} \approx 0.7$, $σ_A > σ_{crit}$, $|M_A| = 2$ | ~0.3 | ~0.0 | ~0.9 | Phase 3 |
| $δ_A^{rel} \approx 0.9$, $σ_A > σ_{crit}$, $|M_A| ≥ 3$ | ~0.1 | ~0.0 | ~1.0 | Phase 4 |

These values are consistent with the qualitative phase prescriptions in §7.
```

**JUSTIFICATION:** This fix makes the executive control ODE *self-contained* — the optimal values are derived from the model's own state variables rather than externally specified. This is stronger than a lookup table because the transition between phases is smooth (ODE-driven) rather than discontinuous (phase-boundary jump). The formulas are monotonic in the expected directions: $P^*$ decreases as depth accumulates (less rigid planning needed), $I^*$ decreases as schema coherence grows (bypass risk diminishes with schema maturity), and $F^*$ increases as mastery domains and intersections grow (more adaptation capacity needed). The fix is consistent with all existing phase descriptions and does not introduce new undefined symbols.

**SAFETY NOTE:** Equation 36's relaxation structure is preserved — only the forcing terms are now formally defined. No protected elements are modified. The derivation uses only variables already defined in the paper ($δ_A^{relative}$, $σ_A$, $|M_A|$, $Ψ_A$, $σ_{critical}$).

---

### VARIANT D
**Issue #:** 6
**Tag:** HACKATHON PRIORITY
**Section targeted:** §4.3.2 (Executive Control ODE) — defines $P^*$, $I^*$, $F^*$ with a bifurcation-aware mechanism
**Scope:** structural
**DIAGNOSIS:** Variant C derives $P^*$, $I^*$, $F^*$ monotonically from phase-index variables. This variant proposes a *non-monotonic* derivation that respects the bifurcation structure already present in the paper. Specifically, $I^*$ should show a sharp transition at $σ_{critical}$ (matching the Phase 2 trigger), not a smooth decrease. This connects the executive control ODE to the bifurcation analysis in Appendix A.3.

**PROPOSED FIX:**
Replace the undefined $P^*$, $I^*$, $F^*$ with bifurcation-aware formulas.

*Old text (§4.3.2):*
```
$P^*$, $I^*$, $F^*$ are H-Bar optimal values for each sub-component in the current phase.
```

*New text:*
```
$P^*$, $I^*$, $F^*$ are derived from the phase-index variables with bifurcation-aware step functions:

$$P^*(t) = \begin{cases} 0.9 & \text{if } \delta_A^{\text{relative}}(d^*, t) < 0.65 \\ 0.5 - 0.3 \cdot \frac{\delta_A^{\text{relative}}(d^*, t) - 0.65}{0.35} & \text{if } 0.65 \leq \delta_A^{\text{relative}}(d^*, t) \leq 1.0 \end{cases} \tag{36a}$$

$$I^*(t) = \begin{cases} 0.9 & \text{if } \sigma_A(d^*, t) < \sigma_{\text{critical}} \\ 0.4 & \text{if } \sigma_A(d^*, t) \geq \sigma_{\text{critical}} \end{cases} \tag{36b}$$

$$F^*(t) = \begin{cases} 0.3 & \text{if } |M_A(t)| < 2 \text{ AND } \Psi_A^{\max}(t) = 0 \\ 0.9 & \text{otherwise} \end{cases} \tag{36c}$$

where $d^* = \arg\max_{d} \delta_A(d,t)$.

The step discontinuity in $I^*$ at $σ_{critical}$ mirrors the Phase 2 transition trigger (§7, Eq. 51). The executive control state converges smoothly through the ODE relaxation (rates $\kappa_P$, $\kappa_I$, $\kappa_F$), so the step in forcing terms produces a smooth transition in the state variable.
```

**JUSTIFICATION:** This fix preserves the discrete phase structure that the paper already relies on. The $I^*$ step function at $σ_{critical}$ directly connects to the bifurcation analysis: inhibition is maximal (0.9) before schema crystallisation (when AI bypass is most dangerous) and drops sharply after (when schema coherence provides intrinsic protection against bypass). This is more faithful to the paper's existing logic than a smooth monotonic formula, and it preserves the interpretability of the phase transitions. The executive control ODE relaxation ensures that even a step discontinuity in $P^*$, $I^*$, $F^*$ produces smooth convergence in $Ξ_A$.

**SAFETY NOTE:** The executive control ODE (Eq. 36) is unchanged. The new definitions use only variables already in the paper ($δ_A^{relative}$, $σ_A$, $|M_A|$, $Ψ_A$, $σ_{critical}$). Protected elements are untouched. The bifurcation at $σ_{critical}$ is already derived in Appendix A.3 (Eq. A.15).

---

### VARIANT E
**Issue #:** 6
**Tag:** HACKATHON PRIORITY
**Section targeted:** §4.3 (Executive Control) and Appendix A.1 — systemic reframe removing the standalone executive control ODE
**Scope:** systemic
**DIAGNOSIS:** The deeper problem is that the executive control ODE (Eq. 36) is architecturally anomalous: it is the *only* ODE in the system that depends on externally-specified optimal values $P^*$, $I^*$, $F^*$. Every other ODE ($δ_A$, $β_A$, $σ_A$, $α_A$, $\hat M_A$) is self-contained — driven by internal state and coupling terms. The executive control ODE requires a lookup table or derivation formula *because* its architecture is wrong. A systemic fix replaces the relaxation-type ODE with a self-contained coupling-driven ODE that derives executive control from the same state variables that define the phases.

**PROPOSED FIX:**
Replace Equation 36 with a coupling-driven ODE. Remove the $P^*$, $I^*$, $F^*$ abstraction entirely.

*Old text (§4.3.2, Equation 36):*
```
$$\dot{\Xi}_A(t) = \kappa_P \cdot [P^*(t) - \Xi_A^P(t)] + \kappa_I \cdot [I^*(t) - \Xi_A^I(t)] + \kappa_F \cdot [F^*(t) - \Xi_A^F(t)] \tag{36}$$

$P^*$, $I^*$, $F^*$ are H-Bar optimal values for each sub-component in the current phase.
```

*New text:*
```
$$
\begin{aligned}
\dot{\Xi}_A^P(t) &= \kappa_P \cdot \left[\left(1 - \bar{\delta}_A^{\text{relative}}(t)\right) - \Xi_A^P(t)\right] \\
\dot{\Xi}_A^I(t) &= \kappa_I \cdot \left[\left(1 - \bar{\sigma}_A(t)/\sigma_{\text{critical}}\right) - \Xi_A^I(t)\right] \cdot \mathbb{1}[\bar{\sigma}_A(t) < \sigma_{\text{critical}}] \\
&\quad + \kappa_I \cdot \left[0.4 - \Xi_A^I(t)\right] \cdot \mathbb{1}[\bar{\sigma}_A(t) \geq \sigma_{\text{critical}}] \\
\dot{\Xi}_A^F(t) &= \kappa_F \cdot \left[\min\left(1, \frac{|M_A(t)|}{2} + \bar{\Psi}_A(t)\right) - \Xi_A^F(t)\right]
\end{aligned}
\tag{36}
$$

where $\bar{\delta}_A^{\text{relative}}(t) = \frac{1}{|D|} \sum_d \delta_A^{\text{relative}}(d,t)$, $\bar{\sigma}_A(t) = \frac{1}{|D|} \sum_d \sigma_A(d,t)$, and $\bar{\Psi}_A(t) = \frac{\Psi_A^{\max}(t)}{\Psi_{\text{threshold}}}$.

Each sub-component's optimal value is now derived directly from the coupled ODE system state:
- **Planning** $Ξ_A^P$ relaxes toward $(1 - \barδ_A^{relative})$: rigid planning when depth is low, relaxed when near frontier.
- **Inhibition** $Ξ_A^I$ relaxes toward $(1 - \barσ_A/σ_{critical})$ below critical (maximum inhibition when schema is immature), drops to 0.4 above critical (strategic delegation permitted). The indicator function $\mathbb{1}[\cdot]$ enforces the bifurcation.
- **Flexibility** $Ξ_A^F$ relaxes toward $\min(1, |M_A|/2 + \barΨ_A)$: grows with mastery count and intersection activity.
```

Also update Appendix A.1 to replace the old Equation A.6 with the new form.

**JUSTIFICATION:** This fix eliminates the architectural anomaly. The executive control ODE becomes self-contained like every other ODE in the system — driven by internal state ($δ_A^{relative}$, $σ_A$, $|M_A|$, $Ψ_A$) rather than external specification. The $P^*$, $I^*$, $F^*$ abstraction is removed entirely, which resolves the issue at its root: there is no longer an undefined quantity. The bifurcation at $σ_{critical}$ is preserved via the indicator function, maintaining connection to the Phase 2 trigger. The phase descriptions in §7 remain valid as *qualitative interpretations* of the ODE behaviour but are no longer the sole source of the executive control forcing terms.

**SAFETY NOTE:** This fix modifies Equation 36 (which is not a protected element) and its surrounding text. It does not modify any protected elements. The new ODE uses only variables already defined in the system. The qualitative phase prescriptions in §7.1–7.5 are unchanged — they now serve as interpretive descriptions of the ODE dynamics rather than as the sole specification of executive control targets. This fix *strengthens* the connection between §4.3 and §7 by making the phase structure emergent from the ODE rather than externally imposed.
