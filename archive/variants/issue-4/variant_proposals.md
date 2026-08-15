# Issue #4 — Variant Proposals (MODE 1: FAST AGENT)

## Issue Summary

**Issue #:** 4
**Tag:** Tier 1A
**Description:** The parametric decay term $\lambda_c$ incorrectly references $\sigma_A$ via the rehearsal engagement rate $r_A$, which is defined in Equation 8 using only elapsed time.

**Core inconsistency:** The prose in §3.3.1 after Equation 8 states "Higher $\sigma_A$ raises $r_A$ through schema-reconstruction, reducing effective decay," but Equation 8 defines $r_A(d,t) = r_{\text{max}} \cdot \exp(-\mu_r \cdot \tau_A(d,t))$ with no $\sigma_A$ dependence. Meanwhile, Equation A.1 in the Appendix contains the *intended* form: $\lambda_c(1 - \gamma_\sigma \cdot \sigma_A) \cdot \delta_A \cdot (1 - r_A)$, where $\sigma_A$ modulates the decay constant directly — not through $r_A$.

---

### VARIANT A
**Issue #:** 4
**Tag:** Tier 1A
**Section targeted:** §3.3.1 (Equations 7–8, prose after Equation 8)
**Scope:** local

**DIAGNOSIS:** The prose makes a claim ("Higher $\sigma_A$ raises $r_A$ through schema-reconstruction") that Equation 8 does not support. The equation defines $r_A$ as a pure exponential decay in elapsed time. The simplest fix is to correct the prose so it matches the equations as written. The $\sigma_A$-to-decay coupling would then exist only via the $P_A$ term in Equation 17 (schema coherence growth is faster when engagement is recent), which is an indirect mechanism but at least consistent with the stated equations.

**PROPOSED FIX:**

*Old text (after Equation 8):*
> Higher $σ_A$ raises $r_A$ through schema-reconstruction, reducing effective decay. This $σ_A$-coupling is absent from all EWC and replay-based accounts.

*New text:*
> Rehearsal engagement rate $r_A$ decays exponentially with elapsed time since last engagement. Schema coherence $σ_A$ does not directly modulate $r_A$; instead, higher $σ_A$ slows parametric decay indirectly by increasing the principled practice rate $P_A(d,t)$ (Equation 18), which drives depth growth that offsets decay losses. This indirect coupling mechanism — depth growth rate scaling with $σ_A$ rather than decay rate scaling with $σ_A$ — is absent from all EWC and replay-based accounts.

**JUSTIFICATION:** This fix eliminates the false claim without changing any equation. The existing Equations 7, 8, 17, and 18 remain internally consistent. The mechanism described (schema coherence → higher principled practice → faster depth growth → net decay offset) is a real and defensible coupling pathway, even though it is indirect rather than the direct decay-rate modulation the original prose implied. No downstream equation is affected.

**SAFETY NOTE:** This fix deliberately does NOT change Equations 7, 8, 17, 18, or A.1. It only corrects the prose interpretation. Equation 28 (updated σA ODE with αA gating) is untouched. Table 1 is untouched.

---

### VARIANT B
**Issue #:** 4
**Tag:** Tier 1A
**Section targeted:** §3.3.1 (Equation 7) — align main text with Appendix A.1
**Scope:** structural

**DIAGNOSIS:** The main text (Equation 7) and the Appendix (Equation A.1) are inconsistent. Equation A.1 contains the intended $\sigma_A$-decay coupling: $\lambda_c(1 - \gamma_\sigma \cdot \sigma_A)$. Equation 7 lacks it. The paper's design intent — as stated in the prose and the summary table after Equation 8 — is that schema coherence reduces parametric decay rate. The fix is to propagate the Appendix form into the main text so Equation 7 matches Equation A.1 and the prose becomes accurate.

**PROPOSED FIX:**

*Old Equation 7:*
$$\dot{\delta}_A(d,t)|_{\text{decay}} = -\lambda_c \cdot \delta_A(d,t) \cdot (1 - r_A(d,t)) \tag{7}$$

*New Equation 7:*
$$\dot{\delta}_A(d,t)|_{\text{decay}} = -\lambda_c \cdot (1 - \gamma_\sigma \cdot \sigma_A(d,t)) \cdot \delta_A(d,t) \cdot (1 - r_A(d,t)) \tag{7}$$

*Add after Equation 7:* "The factor $(1 - \gamma_\sigma \cdot \sigma_A)$ modulates the effective decay rate: higher $\sigma_A$ reduces parametric loss, formalising the schema-reconstruction mechanism. $\gamma_\sigma \in (0, 1)$ is the schema-decay coupling strength (dimensionless parameter group $\Pi_4$)."

*Equation 8 remains unchanged.* The prose after Equation 8 ("Higher $\sigma_A$ raises $r_A$") should be updated to: "Higher $\sigma_A$ reduces the effective $\lambda_c$ via the $(1 - \gamma_\sigma \cdot \sigma_A)$ factor, slowing parametric decay. Additionally, recent engagement raises $r_A$ independently."

**JUSTIFICATION:** This brings the main text into consistency with the Appendix (A.1), which already contains the intended form. The boundedness argument for $\sigma_A$ (Nagumo's theorem, §3.4.3) does not reference Equation 7, so it is unaffected. The depth ODE (Equation 12) currently uses the old Equation 7 form for the decay term — it must also be updated to include $(1 - \gamma_\sigma \cdot \sigma_A)$ for full consistency. This propagates to Equation A.1 which already has it.

**SAFETY NOTE:** This fix does NOT change the $\sigma_A$ ODE (Equation 17/28), the $Ψ_A$ multiplicative functional form (Equation 19/A.10), Table 1, the phase transition trigger statements (§7.1–7.5), or the Burnell et al. citation. It modifies only the depth decay mechanism in §3.3.1 and its propagation to Equation 12.

---

### VARIANT C
**Issue #:** 4
**Tag:** Tier 1A
**Section targeted:** §3.3.1 (Equation 8) — embed $\sigma_A$ coupling into $r_A$
**Scope:** structural

**DIAGNOSIS:** The prose claims $\sigma_A$ raises $r_A$. An alternative to modifying Equation 7 (as in Variant B) is to modify Equation 8 so that $r_A$ itself depends on both elapsed time AND schema coherence. This makes the prose literally correct: higher $\sigma_A$ directly raises the rehearsal engagement rate, which then reduces effective decay via Equation 7.

**PROPOSED FIX:**

*Old Equation 8:*
$$r_A(d,t) = r_{\text{max}} \cdot \exp(-\mu_r \cdot \tau_A(d,t)) \tag{8}$$

*New Equation 8:*
$$r_A(d,t) = r_{\text{max}} \cdot \exp(-\mu_r \cdot \tau_A(d,t)) \cdot (1 + \kappa_\sigma \cdot \sigma_A(d,t)) \tag{8}$$

Where $\kappa_\sigma > 0$ is the schema-engagement coupling constant. When $\sigma_A = 0$, $r_A$ reduces to the original exponential form. When $\sigma_A = 1$, $r_A$ is amplified by factor $(1 + \kappa_\sigma)$.

*Equation 7 remains unchanged.* Prose after Equation 8 updated to: "The factor $(1 + \kappa_\sigma \cdot \sigma_A)$ formalises schema-reconstruction: higher $\sigma_A$ raises the rehearsal engagement rate, reducing effective parametric decay."

**JUSTIFICATION:** This is the variant most faithful to the original prose's intent — $\sigma_A$ directly modulates $r_A$, and $r_A$ feeds into Equation 7. The mechanism is: schema-coherent representations are easier to reconstruct from partial cues (lower retrieval threshold), so elapsed time erodes engagement less rapidly for high-$\sigma_A$ agents. This is a defensible cognitive analogy. The boundedness of $r_A$ is maintained: $r_A \in [r_{\text{max}}, r_{\text{max}}(1 + \kappa_\sigma)]$ for $\sigma_A \in [0,1]$ at $\tau_A = 0$. Equation A.1 in the Appendix would need updating to remove the redundant $(1 - \gamma_\sigma \cdot \sigma_A)$ factor, since the coupling is now through $r_A$ rather than through $\lambda_c$ directly.

**SAFETY NOTE:** This fix does NOT change the $\sigma_A$ ODE (Equation 17/28), the $Ψ_A$ multiplicative functional form (Equation 19/A.10), Table 1, the phase transition triggers (§7.1–7.5), or the Burnell et al. citation. It modifies Equation 8 and requires a corresponding simplification of Equation A.1.

---

### VARIANT D
**Issue #:** 4
**Tag:** Tier 1A
**Section targeted:** §3.3.1 (between Equations 7 and 8) — add an independent $\sigma_A$-decay term
**Scope:** structural

**DIAGNOSIS:** Rather than coupling $\sigma_A$ through $r_A$ or through $\lambda_c$, a cleaner mechanistic separation is to add an independent decay-modulation term that operates alongside the engagement-based decay. This preserves Equation 7 and Equation 8 as written, while adding a separate term that formalises schema-reconstruction as a distinct physical process.

**PROPOSED FIX:**

*Equations 7 and 8 remain unchanged.*

*Insert new equation after Equation 8:*

**Schema-mediated decay reduction:**
$$\dot{\delta}_A(d,t)|_{\text{schema-reconstruction}} = +\lambda_\sigma \cdot \sigma_A(d,t) \cdot \delta_A(d,t) \cdot (1 - r_A(d,t)) \tag{8a}$$

*Updated total depth decay (replacing Equation 7's application):*
$$\dot{\delta}_A(d,t)|_{\text{decay net}} = \dot{\delta}_A|_{\text{decay}} + \dot{\delta}_A|_{\text{schema-reconstruction}} = -(\lambda_c - \lambda_\sigma \cdot \sigma_A) \cdot \delta_A \cdot (1 - r_A) \tag{7+8a}$$

Where $\lambda_\sigma > 0$ is the schema-reconstruction rate. Net effective decay rate: $\lambda_c^{\text{eff}} = \lambda_c - \lambda_\sigma \cdot \sigma_A$. When $\sigma_A > \lambda_c / \lambda_\sigma$, decay is fully offset (schema-reconstruction exceeds parametric loss).

*Prose:* "Schema coherence generates a reconstruction process (Equation 8a) that partially offsets parametric decay. The net decay rate $\lambda_c - \lambda_\sigma \cdot \sigma_A$ decreases linearly with $\sigma_A$, formalising the intuition that principled representations are self-maintaining."

**JUSTIFICATION:** This variant preserves both existing equations exactly, adding a new term rather than modifying existing ones. The mechanism is physically motivated: schema-coherent representations contain redundant structural information that enables reconstruction even after partial decay — analogous to error-correcting codes. The sign is correct: Equation 8a is a positive (recovery) term opposing the negative (decay) term in Equation 7. Boundedness: net decay is non-negative as long as $\lambda_c \geq \lambda_\sigma \cdot \sigma_A$, which holds if $\lambda_c \geq \lambda_\sigma$ (the base decay rate exceeds the maximum reconstruction rate). The Appendix A.1 would need to be updated to incorporate Equation 8a.

**SAFETY NOTE:** This fix does NOT change the $\sigma_A$ ODE (Equation 17/28), the $Ψ_A$ multiplicative functional form (Equation 19/A.10), Table 1, the phase transition triggers (§7.1–7.5), or the Burnell et al. citation. It adds a new equation (8a) and a combined decay expression. The Boundedness proof in §3.4.3 for $\sigma_A$ does not reference the decay term, so it is unaffected.

---

### VARIANT E
**Issue #:** 4
**Tag:** Tier 1A
**Section targeted:** §3.3 (full subsection restructure) + §12 (Appendix A.1)
**Scope:** systemic

**DIAGNOSIS:** The underlying problem is deeper than a single equation mismatch. Section 3.3 defines decay as two mechanisms (parametric decay and frontier obsolescence) but does not clearly separate three distinct processes: (1) passive engagement decay ($r_A$ from elapsed time), (2) schema-mediated decay reduction (the intended $\sigma_A$ coupling), and (3) frontier obsolescence ($\lambda_f$). The current structure conflates (1) and (2) in the prose while keeping them separate in the equations. A systemic fix restructures §3.3 to define three named decay processes with clear coupling channels, then shows how Equations 7 and 8 are special cases.

**PROPOSED FIX:**

*Current §3.3 structure:*
```
3.3 Two-Mechanism Decay
  3.3.1 Parametric Decay λc (Eq. 7, 8)
  3.3.2 Frontier Obsolescence λf (Eq. 9, 10, 11)
  3.3.3 Two-Mechanism vs. Prior Frameworks (comparison table)
```

*Proposed §3.3 structure:*
```
3.3 Decay Architecture

  3.3.1 Engagement Decay (passive)
    r_A(d,t) = r_max · exp(−μ_r · τ_A(d,t))           [Eq. 8, unchanged]
    Decay from elapsed time since last engagement.
    No σ_A dependence.

  3.3.2 Schema-Mediated Decay Reduction (active)
    Effective decay rate: λ_c^eff = λ_c · (1 − γ_σ · σ_A(d,t))
    [Parameter: γ_σ ∈ (0, 1); dimensionless group Π_4]
    Higher σ_A directly reduces the rate at which depth is lost.
    Distinct from engagement: schema-coherent representations
    resist decay even when engagement rate is low.

  3.3.3 Combined Depth Decay
    δ̇_A|_decay = −λ_c · (1 − γ_σ · σ_A) · δ_A · (1 − r_A)  [Eq. 7 revised]
    Three-factor product: base rate × schema modulation × engagement modulation.

  3.3.4 Frontier Obsolescence
    [Eqs. 9, 10, 11 — unchanged]

  3.3.5 Decay Architecture vs. Prior Frameworks
    [Updated comparison table with three mechanisms]
```

*Updated Equation 7:*
$$\dot{\delta}_A(d,t)|_{\text{decay}} = -\lambda_c \cdot (1 - \gamma_\sigma \cdot \sigma_A(d,t)) \cdot \delta_A(d,t) \cdot (1 - r_A(d,t)) \tag{7}$$

*Equation 8 unchanged.* Prose rewritten to clearly separate engagement decay from schema-mediated decay reduction.

*Appendix A.1 updated:* Equation A.1 should now reference the revised Equation 7 directly (they are now identical), and the dimensionless parameter group $\Pi_4 = \gamma_\sigma$ should be cross-referenced to §3.3.2.

**JUSTIFICATION:** This is the most architecturally clean fix. It separates two processes that the current text conflates: (a) engagement-based decay (time-dependent, no $\sigma_A$) and (b) schema-mediated decay reduction ($\sigma_A$-dependent, time-independent). The three-factor product in the revised Equation 7 is transparent: each factor has a clear physical interpretation and a single coupling channel. The comparison table in §3.3.5 is updated to show three mechanisms instead of two, improving the framework's differentiation from prior work. This fix also resolves the notation ambiguity by keeping $\tau_A(d,t)$ as elapsed time in §3.3 and reserving $\tau_A(B,d,t)$ (theory of mind coupling) for §4.2, where it belongs.

**SAFETY NOTE:** This fix does NOT change the $\sigma_A$ ODE (Equation 17/28), the $Ψ_A$ multiplicative functional form (Equation 19/A.10), Table 1, the phase transition triggers (§7.1–7.5), or the Burnell et al. citation. It restructures §3.3 prose and revises Equation 7, but preserves all other equations. The boundedness proof (§3.4.3) is unaffected because it concerns $\sigma_A$, not $\delta_A$.
