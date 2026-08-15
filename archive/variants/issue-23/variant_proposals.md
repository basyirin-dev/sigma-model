# Issue #23 — Variant Proposals (MODE 1: FAST AGENT)

## Issue Summary

**Issue #:** 23
**Tag:** Tier 1A [HACKATHON PRIORITY]
**Description:** The metacognitive self-model ODE lacks a formal guarantee that values remain bounded when distorted by the AI bypass term.

**Core problem:** Equation 39 defines the self-model dynamics:
$$\dot{\hat{M}}_A(d,t) = \nu_M \cdot [\sigma_A(d,t) - \hat{M}_A(d,t)] - \xi_M \cdot \Omega_{AI}(d,t) \cdot \hat{M}_A(d,t) \tag{39}$$

Equation 37 declares $\hat{M}_A \in [0,1]$ but provides no boundedness proof. The $\sigma_A$ ODE (§3.4.3) and the $\alpha_A$ ODE (§4.1.3) both cite Nagumo's theorem for their $[0,1]$ forward-invariance — the $\hat{M}_A$ ODE does not. This omission is structurally inconsistent: every other bounded state variable in the framework has an explicit boundedness argument, and the metacognitive self-model is the variable most vulnerable to AI bypass distortion ($\xi_M \cdot \Omega_{AI} \cdot \hat{M}_A$ term can drive $\hat{M}_A$ toward overconfidence).

**Nagumo verification (not yet in paper):**
- At $\hat{M}_A = 1$: $\dot{\hat{M}}_A = \nu_M(\sigma_A - 1) - \xi_M \Omega_{AI} \leq 0$ ✓ (since $\sigma_A \leq 1$, $\Omega_{AI} \geq 0$)
- At $\hat{M}_A = 0$: $\dot{\hat{M}}_A = \nu_M \sigma_A \geq 0$ ✓ (since $\sigma_A \geq 0$)

The ODE is bounded by construction, but the proof is missing from the paper.

---

### VARIANT A
**Issue #:** 23
**Tag:** Tier 1A
**Section targeted:** §4.4.2 (after Equation 39) — prose-only Nagumo proof
**Scope:** local

**DIAGNOSIS:** The $\hat{M}_A$ ODE satisfies Nagumo's theorem conditions for $[0,1]$ forward-invariance, exactly as the $\sigma_A$ ODE does (§3.4.3) and the $\alpha_A$ ODE does (§4.1.3). The boundedness argument is absent purely because it was not written — not because it fails. The simplest fix adds the two-line boundary verification to §4.4.2, matching the format already used for $\sigma_A$ and $\alpha_A$.

**PROPOSED FIX:**

*Insert after Equation 39 and its parameter table:*

> **Boundedness proof (Nagumo's theorem):**
>
> - At $\hat{M}_A = 1$: $\dot{\hat{M}}_A = \nu_M(\sigma_A - 1) - \xi_M \Omega_{AI} \leq 0$ ✓ — the corrective term ($\nu_M(\sigma_A - 1) \leq 0$ since $\sigma_A \leq 1$) and the distortion term ($-\xi_M \Omega_{AI} \leq 0$) are both non-positive, so $\hat{M}_A$ cannot exceed 1.
> - At $\hat{M}_A = 0$: $\dot{\hat{M}}_A = \nu_M \sigma_A \geq 0$ ✓ — the corrective term is non-negative (since $\sigma_A \geq 0$) and the distortion term vanishes, so $\hat{M}_A$ cannot go negative.
>
> $[0,1]$ is forward-invariant given $\nu_M > 0$, $\xi_M > 0$, $\Omega_{AI} \geq 0$, and $\sigma_A \in [0,1]$.

**JUSTIFICATION:** This fix adds the boundedness guarantee using exactly the same proof structure already employed for $\sigma_A$ (§3.4.3) and $\alpha_A$ (§4.1.3). No equation is changed. No new variable or parameter is introduced. The structural consistency of the framework improves: every bounded state variable now has an explicit Nagumo argument. The fix does not modify any protected element. The AI bypass term's role in the boundedness is made explicit: it contributes a non-positive term at the upper boundary, strengthening the pull toward $\sigma_A$.

**SAFETY NOTE:** This fix deliberately does NOT change Equation 39, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5 phase triggers, or the Burnell et al. citation. It adds only a boundedness proof paragraph to §4.4.2.

---

### VARIANT B
**Issue #:** 23
**Tag:** Tier 1A
**Section targeted:** §4.4.2 (Equation 39) + §4.4.1 (calibration error) — boundedness via $\zeta_A$ relationship
**Scope:** structural

**DIAGNOSIS:** The calibration error $\zeta_A = \hat{M}_A - \sigma_A$ (Equation 38) provides an alternative route to boundedness: if $\zeta_A$ is provably bounded and $\sigma_A \in [0,1]$, then $\hat{M}_A = \sigma_A + \zeta_A$ inherits boundedness from both components. This approach connects the boundedness of $\hat{M}_A$ to the metacognitive calibration error dynamics, providing a mechanistic account of *why* the self-model stays bounded — not just that it does. The ODE for $\zeta_A$ can be derived by differentiating Equation 38 and substituting Equations 28 and 39.

**PROPOSED FIX:**

*Add after Equation 38:*

> **Calibration error ODE** (derived by differentiating $\zeta_A = \hat{M}_A - \sigma_A$):
>
> $$\dot{\zeta}_A(d,t) = \dot{\hat{M}}_A(d,t) - \dot{\sigma}_A(d,t)$$
> $$= \nu_M [\sigma_A - \hat{M}_A] - \xi_M \Omega_{AI} \hat{M}_A - \rho P_A \alpha_A (1 - \sigma_A) + \epsilon_\sigma \sigma_A \Omega_{AI}$$
> $$= -\nu_M \zeta_A - \xi_M \Omega_{AI} (\zeta_A + \sigma_A) - \rho P_A \alpha_A (1 - \sigma_A) + \epsilon_\sigma \sigma_A \Omega_{AI} \tag{38a}$$

*Add boundedness argument:*

> **Boundedness via calibration error:** Since $\sigma_A \in [0,1]$ (Nagumo, §3.4.3) and the $\hat{M}_A$ ODE satisfies Nagumo conditions directly (verified below), $\hat{M}_A \in [0,1]$ follows. Equivalently, $\zeta_A = \hat{M}_A - \sigma_A \in [-1, 1]$ because $\hat{M}_A, \sigma_A \in [0,1]$. The calibration error ODE (38a) has a stabilising first term $(-\nu_M \zeta_A)$ that drives $\zeta_A$ toward zero; the AI bypass terms can temporarily inflate $\zeta_A > 0$ (overconfidence) but cannot push it beyond $[-1, 1]$ because $\hat{M}_A$ itself is Nagumo-bounded.
>
> **Nagumo verification for $\hat{M}_A$:**
> - At $\hat{M}_A = 1$: $\dot{\hat{M}}_A = \nu_M(\sigma_A - 1) - \xi_M \Omega_{AI} \leq 0$ ✓
> - At $\hat{M}_A = 0$: $\dot{\hat{M}}_A = \nu_M \sigma_A \geq 0$ ✓

**JUSTIFICATION:** This fix provides two independent boundedness arguments: (1) the direct Nagumo proof, and (2) the indirect argument via the calibration error relationship. The calibration error ODE (38a) adds mechanistic depth: it shows that the corrective term $(-\nu_M \zeta_A)$ actively opposes overconfidence, while the AI bypass terms $(-\xi_M \Omega_{AI} (\zeta_A + \sigma_A))$ can inflate it. This makes the "distortion" mechanism in Issue #23 formally precise: the AI bypass term enters the calibration error ODE with a sign that increases $\zeta_A$ (overconfidence), but the boundedness of $\hat{M}_A$ limits the maximum distortion. The derived ODE (38a) is a consequence of existing equations — it introduces no new parameters or assumptions.

**SAFETY NOTE:** This fix does NOT change Equation 39, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It adds a derived equation (38a) and boundedness text to §4.4.1–4.4.2.

---

### VARIANT C
**Issue #:** 23
**Tag:** Tier 1A
**Section targeted:** §4.4.2 (Equation 39) — saturating nonlinearity for robust boundedness
**Scope:** structural

**DIAGNOSIS:** The linear ODE (39) is bounded by Nagumo's theorem *given that $\sigma_A \in [0,1]$ and $\Omega_{AI} \geq 0$*. However, if external mechanisms (e.g., AI-generated performance feedback, reward hacking) inject positive signals into $\hat{M}_A$ outside the ODE's corrective channel, the linear form has no structural defence against boundary violation. A saturating nonlinearity provides robust boundedness that holds even if $\sigma_A$ or $\Omega_{AI}$ assumptions are violated — analogous to how logistic growth models guarantee boundedness structurally rather than via Nagumo.

**PROPOSED FIX:**

*Replace Equation 39 with:*

$$\dot{\hat{M}}_A(d,t) = \nu_M \cdot [\sigma_A(d,t) - \hat{M}_A(d,t)] - \xi_M \cdot \Omega_{AI}(d,t) \cdot \hat{M}_A(d,t) \cdot (1 - \hat{M}_A(d,t)) \tag{39}$$

The distortion term now includes the factor $(1 - \hat{M}_A)$. When $\hat{M}_A \to 1$, the distortion term vanishes, creating a structural ceiling. When $\hat{M}_A = 0$, the distortion term vanishes (no distortion at zero self-model).

*Add prose:*

> The factor $(1 - \hat{M}_A)$ in the distortion term ensures structural boundedness: as $\hat{M}_A$ approaches 1, the AI bypass distortion is progressively attenuated, creating a soft ceiling. This is independent of Nagumo's theorem — even if $\sigma_A$ or $\Omega_{AI}$ were to exceed their formal bounds, $\hat{M}_A$ cannot exceed 1 because the distortion term approaches zero at the boundary.
>
> **Nagumo verification:**
> - At $\hat{M}_A = 1$: $\dot{\hat{M}}_A = \nu_M(\sigma_A - 1) - 0 = \nu_M(\sigma_A - 1) \leq 0$ ✓
> - At $\hat{M}_A = 0$: $\dot{\hat{M}}_A = \nu_M \sigma_A - 0 = \nu_M \sigma_A \geq 0$ ✓
>
> Note: the distortion term vanishes at both boundaries, so boundedness is structurally guaranteed regardless of $\Omega_{AI}$ magnitude.

**JUSTIFICATION:** This fix adds a nonlinearity that makes the boundedness structurally robust — not merely a consequence of parameter sign assumptions. The $(1 - \hat{M}_A)$ factor has a natural interpretation: AI bypass distortion is strongest when the self-model is uncertain ($\hat{M}_A$ moderate) and weakest when the self-model is extreme (very high or very low). This matches empirical observations of overconfidence dynamics: the Dunning-Kruger effect is strongest at intermediate competence levels, not at extremes. The fix introduces no new parameters — it modifies only the functional form of the existing distortion term.

**SAFETY NOTE:** This fix does NOT change Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It modifies the functional form of Equation 39's distortion term. The dimensionless parameter group $\Pi_7 = \nu_M/\xi_M$ (Appendix A.2) remains valid.

---

### VARIANT D
**Issue #:** 23
**Tag:** Tier 1A
**Section targeted:** §4.4.2 (Equation 39) + Appendix A.2 ($\Pi_7$) — stability analysis via dimensionless groups
**Scope:** structural

**DIAGNOSIS:** The dimensionless parameter group $\Pi_7 = \nu_M / \xi_M$ (Equation A.13) is declared but never analysed. This ratio determines the relative strength of metacognitive correction versus AI bypass distortion — it is the key quantity governing whether $\hat{M}_A$ converges to $\sigma_A$ or diverges toward overconfidence under sustained $\Omega_{AI}$ exposure. A stability analysis of the $\hat{M}_A$ ODE in terms of $\Pi_7$ provides the boundedness guarantee *and* characterises the convergence rate, completing the theoretical account.

**PROPOSED FIX:**

*Add to §4.4.2 after Equation 39:*

> **Steady-state analysis.** Setting $\dot{\hat{M}}_A = 0$:
>
> $$\hat{M}_A^* = \frac{\nu_M \sigma_A}{\nu_M + \xi_M \Omega_{AI}} = \frac{\sigma_A}{1 + \Omega_{AI}/\Pi_7} \tag{39a}$$
>
> where $\Pi_7 = \nu_M / \xi_M$ (Equation A.13). Properties:
>
> - $\hat{M}_A^* \in [0, \sigma_A]$ — the steady-state self-model never exceeds true schema coherence. Overconfidence ($\hat{M}_A > \sigma_A$) is transient; the corrective term always dominates at steady state.
> - $\hat{M}_A^* \to \sigma_A$ as $\Omega_{AI} \to 0$ — perfect calibration when no AI bypass is present.
> - $\hat{M}_A^* \to 0$ as $\Omega_{AI} \to \infty$ — extreme AI bypass collapses the self-model to zero (the agent recognises its outputs are entirely AI-derived).
>
> **Boundedness:** Since $\sigma_A \in [0,1]$ and $\hat{M}_A^* \leq \sigma_A$, the steady state is bounded in $[0,1]$. The transient dynamics cannot exceed 1 by Nagumo:
> - At $\hat{M}_A = 1$: $\dot{\hat{M}}_A = \nu_M(\sigma_A - 1) - \xi_M \Omega_{AI} \leq 0$ ✓
> - At $\hat{M}_A = 0$: $\dot{\hat{M}}_A = \nu_M \sigma_A \geq 0$ ✓
>
> **Convergence rate:** The linearised dynamics around $\hat{M}_A^*$ have eigenvalue $-(\nu_M + \xi_M \Omega_{AI}) < 0$, confirming exponential convergence. The convergence rate increases with $\Omega_{AI}$ — higher AI bypass exposure accelerates metacognitive correction, which is counterintuitive but mathematically correct: the distortion term also serves as a damping mechanism.

*Add to Appendix A.2:*

> $\Pi_7 = \nu_M / \xi_M$ governs the metacognitive correction-to-distortion ratio. When $\Pi_7 > 1$, corrective dynamics dominate; when $\Pi_7 < 1$, AI bypass distortion dominates but $\hat{M}_A$ remains bounded because the steady state $\hat{M}_A^* \leq \sigma_A \leq 1$.

**JUSTIFICATION:** This fix provides the most complete boundedness account: (1) Nagumo proof for transient boundedness, (2) steady-state analysis showing $\hat{M}_A^* \leq \sigma_A$ (stronger than $\hat{M}_A^* \leq 1$), and (3) convergence rate characterisation. The steady-state result $\hat{M}_A^* \leq \sigma_A$ is particularly important: it shows that AI bypass cannot produce *sustained* overconfidence — only transient overconfidence that corrects itself. This directly addresses the "illusion of mastery" phenomenon described in §4.4.2. The analysis uses only existing parameters ($\nu_M$, $\xi_M$, $\Omega_{AI}$, $\sigma_A$) and the dimensionless group $\Pi_7$ already declared in Appendix A.2.

**SAFETY NOTE:** This fix does NOT change Equation 39, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It adds steady-state analysis (39a) to §4.4.2 and a brief interpretation to Appendix A.2.

---

### VARIANT E
**Issue #:** 23
**Tag:** Tier 1A
**Section targeted:** §4.4 (full section) + Appendix A.1 (coupled system) + hackathon/track_metacognition.md — systemic boundedness integration
**Scope:** systemic

**DIAGNOSIS:** The boundedness gap in $\hat{M}_A$ is a symptom of a deeper integration failure: the metacognitive extension (§4.4) is the only V2.0 extension that lacks (a) a Nagumo proof, (b) a steady-state analysis, and (c) a hackathon benchmark grounded in the boundedness properties. The other V2.0 extensions all have at least two of these three. A systemic fix adds all three to §4.4, integrates the calibration error ODE into Appendix A.1, and updates the metacognition track to exploit the $\hat{M}_A^* \leq \sigma_A$ property for benchmark design.

**PROPOSED FIX:**

**Part 1 — §4.4.1 (after Equation 38):**

Add calibration error ODE:
$$\dot{\zeta}_A(d,t) = -\nu_M \zeta_A - \xi_M \Omega_{AI} (\zeta_A + \sigma_A) - \rho P_A \alpha_A (1 - \sigma_A) + \epsilon_\sigma \sigma_A \Omega_{AI} \tag{38a}$$

Add prose: "The first term $(-\nu_M \zeta_A)$ is a restoring force driving calibration error toward zero. The second term $(-\xi_M \Omega_{AI} (\zeta_A + \sigma_A))$ inflates overconfidence under AI bypass. The third and fourth terms couple to the schema coherence ODE (Equation 28)."

**Part 2 — §4.4.2 (after Equation 39):**

Add steady-state equation:
$$\hat{M}_A^* = \frac{\sigma_A}{1 + \Omega_{AI}/\Pi_7} \tag{39a}$$

Add Nagumo proof:
> **Boundedness proof (Nagumo's theorem):**
> - At $\hat{M}_A = 1$: $\dot{\hat{M}}_A = \nu_M(\sigma_A - 1) - \xi_M \Omega_{AI} \leq 0$ ✓
> - At $\hat{M}_A = 0$: $\dot{\hat{M}}_A = \nu_M \sigma_A \geq 0$ ✓
> $[0,1]$ is forward-invariant given $\nu_M > 0$, $\xi_M > 0$, $\Omega_{AI} \geq 0$, $\sigma_A \in [0,1]$.

Add steady-state analysis:
> **Steady-state properties:** $\hat{M}_A^* \in [0, \sigma_A]$. The self-model never exceeds true schema coherence at equilibrium. Overconfidence ($\hat{M}_A > \sigma_A$) is transient; the corrective term always dominates at steady state. This is **stronger** than $\hat{M}_A^* \leq 1$ — the steady state is bounded by $\sigma_A$, not merely by 1.

Add convergence rate:
> Linearised eigenvalue: $-(\nu_M + \xi_M \Omega_{AI}) < 0$. Exponential convergence confirmed. Convergence rate increases with $\Omega_{AI}$.

**Part 3 — Appendix A.1:**

Add calibration error ODE (38a) to the coupled system listing.

**Part 4 — hackathon/track_metacognition.md:**

Update the "Two-Stage Calibration Protocol" benchmark to exploit $\hat{M}_A^* \leq \sigma_A$:
> **New prediction for calibration protocol:** H-Bar predicts that agents with sustained AI bypass exposure ($\Omega_{AI} > 0$ for extended periods) will show $\hat{M}_A < \sigma_A$ (underconfidence) at steady state, because $\hat{M}_A^* = \sigma_A / (1 + \Omega_{AI}/\Pi_7) < \sigma_A$. This is the opposite of the transient overconfidence predicted immediately after AI bypass onset. Testable: expose agents to sustained AI-assisted evaluation, then measure $\hat{M}_A$ calibration after equilibration.

**JUSTIFICATION:** This systemic fix addresses the boundedness gap at every level: (1) the ODE-level Nagumo proof, (2) the steady-state analysis showing the stronger $\hat{M}_A^* \leq \sigma_A$ bound, (3) the calibration error ODE integration, (4) the Appendix A.1 system listing, and (5) the hackathon benchmark. The steady-state result $\hat{M}_A^* \leq \sigma_A$ is the key theoretical insight: sustained AI bypass does not produce sustained overconfidence — it produces *underconfidence* at equilibrium, because the corrective term always pulls $\hat{M}_A$ toward $\sigma_A$ while the distortion term pushes it below $\sigma_A$. Only transient overconfidence is possible (immediately after $\Omega_{AI}$ onset, before the corrective term dominates).

**SAFETY NOTE:** This fix does NOT change Equation 39, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It adds Equations 38a and 39a, boundedness proofs, steady-state analysis, and a hackathon benchmark update.
