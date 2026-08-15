# Variant Proposals — Issue #11

**Issue #:** 11
**Tag:** [Ψ]
**Status:** OPEN
**Cycle:** Phase 3, Issue #11

---

### VARIANT A
**Issue #:** 11
**Tag:** [Ψ]
**Section targeted:** §3.5 (Intersection Activation ΨA) — prose surrounding Equation 21
**Scope:** local
**DIAGNOSIS:** Equation 21 asserts a multiplicative (geometric mean) form for ΨA without first-principles justification. The current prose states: "The geometric mean √(q₁·q₂) is bounded in [0,1], symmetric, and cannot be inflated by one domain compensating for another." This is a list of desirable properties, not a derivation. The reader has no formal reason to accept the product over any other symmetric, bounded, non-compensating form (e.g., harmonic mean, minimum function, or parameterised power mean). The absence of derivation weakens the theoretical core of the framework, as the multiplicative σA·σA dependence is the mechanism behind Prediction 6.
**PROPOSED FIX:**
Add the following paragraph after the existing three-sentence justification of the geometric mean in §3.5 (after "This is **Prediction 6**."):

> **First-principles justification.** Intersection discovery requires that two domains independently contribute their schema-coherent representations to a novel composition. Under the formal assumption that domain contributions are conditionally independent given the intersection potential — i.e., the quality of domain 1's contribution does not statistically depend on the quality of domain 2's contribution once both are directed at the same problem — the joint probability of productive intersection is the product of the marginal probabilities: ΨA ∝ P(d₁ contributes) · P(d₂ contributes) ∝ qA(d₁,t) · qA(d₂,t). The geometric mean √(q₁·q₂) is the normalised form (ensuring ΨA ∈ [0,1] under unit scaling). An additive form (q₁+q₂)/2 would implicitly assume a pooling of domain resources rather than independent causal contributions, which is inconsistent with the ΨA formalism: an intersection is not a weighted average of domains but a product of their independent structural readiness. The multiplicative form is therefore not merely convenient but structurally required by the conditional independence assumption inherent in the two-domain activation condition (Eq. 19).

**JUSTIFICATION:** This fix adds the missing derivation without changing Equation 21 or any other equation. It grounds the multiplicative form in a well-understood probability principle (conditional independence → product rule) and explicitly contrasts with the additive alternative. The fix is consistent with the existing boundedness and symmetry properties already stated. It touches no other section — the cross-references to Prediction 6 and Eq. 19 remain valid.
**SAFETY NOTE:** Does not change Equation 21, Equation 19, or any ODE. Does not alter the ΨA boundedness argument in Appendix A.7. Does not touch any protected element.

---

### VARIANT B
**Issue #:** 11
**Tag:** [Ψ]
**Section targeted:** §3.5 — Equation 21 and surrounding derivational structure
**Scope:** structural
**DIAGNOSIS:** The geometric mean √(q₁·q₂) is asserted as a closed form without derivation from a more primitive object. The paper would be stronger if ΨA were derived from a joint discovery probability that is itself defined before being simplified to the geometric mean. Currently the reader jumps from the activation condition (Eq. 19) directly to the final form (Eq. 21) with no intermediate step showing where the product originates.
**PROPOSED FIX:**
Replace the text block between Equation 20 and Equation 21 (starting "Discovery rate" and ending with the current Eq. 21 + its one-line explanation) with:

> **Discovery rate.** Define the joint intersection probability as the product of each domain's marginal contribution probability, conditional on both being above θI:
>
> $$P_{\text{joint}}(d_1,d_2,t) = P(d_1 \text{ contributes} \mid \delta_A(d_1)>\theta_I) \cdot P(d_2 \text{ contributes} \mid \delta_A(d_2)>\theta_I) \tag{21a}$$
>
> Under the assumption that domain contributions are conditionally independent (the structural readiness of domain 1 does not depend on domain 2's readiness once both exceed θI), each marginal probability is proportional to its effective mastery quality: P(d contributes) ∝ qA(d,t). Substituting:
>
> $$P_{\text{joint}} = c \cdot q_A(d_1,t) \cdot q_A(d_2,t) \tag{21b}$$
>
> Normalising to [0,1] via the geometric mean and incorporating domain structural similarity:
>
> $$\Psi_A(d_1,d_2,t) = \Psi_0 \cdot \phi(d_1,d_2) \cdot \sqrt{q_A(d_1,t) \cdot q_A(d_2,t)} \tag{21}$$
>
> The geometric mean √(q₁·q₂) is bounded in [0,1], symmetric, and cannot be inflated by one domain compensating for another. The multiplicative σA·σA dependence is the mechanism's theoretical core: an agent with high δA but low σA in one mastery domain shows disproportionately lower ΨA than an additive model predicts. This is **Prediction 6**.

**JUSTIFICATION:** This fix introduces a two-step derivation (joint probability → normalised form) that makes the multiplicative structure formally traceable to the conditional independence assumption. The new intermediate equations (21a, 21b) are labelled and cross-referenceable. The final Equation 21 is unchanged, preserving all existing cross-references. The fix is more rigorous than Variant A's prose-only addition because it creates formal intermediate objects.
**SAFETY NOTE:** Does not change the final Equation 21 (same form). Does not alter any other equation. Does not touch protected elements. Equation numbering adjusts only within §3.5 (21a, 21b are new intermediates, 21 is preserved).

---

### VARIANT C
**Issue #:** 11
**Tag:** [Ψ]
**Section targeted:** New subsection in §3.5 or §12 (Mathematical Appendix) — Intersection Discovery Theorem
**Scope:** systemic
**DIAGNOSIS:** The multiplicative form is currently justified by assertion and desirable properties. A full systemic treatment would introduce a formal theorem with explicit axioms, making the derivation self-contained and independently verifiable. This goes beyond local prose repair or equation restructuring by creating a new formal object — a theorem — that anchors the entire ΨA mechanism.
**PROPOSED FIX:**
Add a new subsection **"3.5.1 Intersection Discovery Theorem"** after the existing §3.5 content (before §3.6), containing:

> **Axiom 1 (Domain Independence).** The quality of domain d₁'s contribution to an intersection is statistically independent of domain d₂'s quality, conditional on both exceeding θI.
>
> **Axiom 2 (Symmetry).** ΨA(d₁,d₂,t) = ΨA(d₂,d₁,t) — the discovery rate is invariant to domain ordering.
>
> **Axiom 3 (Monotonicity).** ΨA is non-decreasing in each qA(dᵢ,t) independently.
>
> **Axiom 4 (Boundedness).** ΨA(d₁,d₂,t) ∈ [0, Ψ₀ · max ϕ(d₁,d₂)] for all d₁, d₂, t.
>
> **Axiom 5 (Non-compensation).** No finite value of qA(d₁) can compensate for qA(d₂) = 0; i.e., ΨA(d₁, d₂, t) = 0 if either qA = 0.
>
> **Theorem (Multiplicative Necessity).** Under Axioms 1–5, the unique (up to the scaling constant Ψ₀ and the normalisation to [0,1]) functional form for ΨA is:
> $$\Psi_A(d_1,d_2,t) = \Psi_0 \cdot \phi(d_1,d_2) \cdot \sqrt{q_A(d_1,t) \cdot q_A(d_2,t)}$$
>
> *Proof sketch.* Axiom 1 (conditional independence) implies the joint probability factorises as a product of marginals (standard probability theory). Axiom 2 requires symmetry, which the geometric mean satisfies. Axiom 3 requires monotonicity, satisfied by the product q₁·q₂. Axiom 4 bounds the product via the geometric mean normalisation. Axiom 5 (non-compensation) is the key constraint: it excludes all additive forms (q₁+q₂)/2, weighted sums, and harmonic means, because for any w ∈ (0,1), the form w·q₁ + (1−w)·q₂ > 0 when q₁ > 0 even if q₂ = 0. The product q₁·q₂ = 0 whenever either factor is zero, making it the unique symmetric, monotonic, bounded form satisfying Axiom 5. The geometric mean √(q₁·q₂) is the [0,1]-normalised variant.

**JUSTIFICATION:** This fix provides a rigorous, self-contained derivation that makes the multiplicative form the unique solution to a well-posed axiomatic problem. It is the strongest possible answer to the issue's concern. The theorem is referenced from §3.5 prose as "derived in §3.5.1" rather than asserted. However, it adds a new subsection to the paper and creates formal overhead. The proof sketch should be expanded in the Appendix if space permits.
**SAFETY NOTE:** Does not change Equation 21 or any existing equation. Adds a new subsection (§3.5.1) and five axioms. Does not touch protected elements. The axioms are stated in formal language consistent with the paper's mathematical register.

---

### VARIANT D
**Issue #:** 11
**Tag:** [Ψ]
**Section targeted:** §9 (Eight Falsifiable Predictions) — Prediction 6, with cross-reference back to §3.5
**Scope:** local
**DIAGNOSIS:** Rather than deriving the multiplicative form from first principles, an alternative justification is empirical: the multiplicative form makes a specific, testable prediction (Prediction 6) that no additive form can produce. If this prediction is confirmed, the multiplicative form is empirically justified even without a first-principles derivation. The issue can be resolved by strengthening the empirical justification pathway and adding cross-reference to §3.5.
**PROPOSED FIX:**
In §3.5, after "This is **Prediction 6**.", add:

> **Empirical justification.** The multiplicative form is not merely asserted but generates a specific falsifiable prediction (§9, Prediction 6) that distinguishes it from all additive alternatives: an agent with high qA in one domain and low qA in the other will show disproportionately lower ΨA than any additive model (arithmetic mean, harmonic mean, or weighted average) predicts. Confirmation of Prediction 6 provides indirect empirical support for the multiplicative form. A full first-principles derivation from conditional independence is provided in §3.5.1 [if Variant C is also applied] or is deferred as a refinement target.

In §9, Prediction 6, after "Falsification: An additive model fits cross-domain discovery data as well as or better than the multiplicative model.", add:

> **Justification for multiplicative form.** The multiplicative √(q₁·q₂) form in Eq. 21 was chosen because it is the unique symmetric, bounded, non-compensating function of two variables. No additive form (q₁+q₂)/2, minimum(q₁,q₂), or harmonic mean 2q₁q₂/(q₁+q₂) satisfies non-compensation — each allows one high-quality domain to partially compensate for one low-quality domain. The geometric mean is the only common symmetric mean that reaches zero when either input is zero. This structural property is what makes Prediction 6 a clean test: if the multiplicative form is correct, the compensation prediction of additive models will fail.

**JUSTIFICATION:** This fix takes the least invasive approach: it adds cross-referencing between §3.5 and §9, and provides an alternative justification (empirical rather than axiomatic) for the multiplicative form. It does not change any equation. It is compatible with Variants A, B, or C as complementary additions.
**SAFETY NOTE:** Does not change Equation 21. Does not alter any ODE. Does not touch protected elements. Adds prose only to §3.5 and §9.

---

### VARIANT E
**Issue #:** 11
**Tag:** [Ψ]
**Section targeted:** §3.5 — new comparative table and justification block
**Scope:** structural
**DIAGNOSIS:** The current text asserts the geometric mean without comparing it to alternatives on formal grounds. A systematic comparison table would make the choice of multiplicative form transparent and defensible by showing exactly which properties each candidate form satisfies or violates.
**PROPOSED FIX:**
Add the following table and explanatory paragraph after the current Eq. 21 justification (after "This is **Prediction 6**."):

> **Formal comparison of candidate ΨA functional forms.** The table below evaluates five candidate symmetric, two-variable forms against five formal properties required by the H-Bar framework:
>
> | Form | Formula | Symmetric | Bounded [0,1] | Monotonic | Non-compensating | Zero-at-boundary |
> |------|---------|-----------|---------------|-----------|------------------|------------------|
> | Geometric mean | √(q₁q₂) | ✓ | ✓ | ✓ | ✓ | ✓ |
> | Arithmetic mean | (q₁+q₂)/2 | ✓ | ✓ | ✓ | ✗ | ✗ |
> | Harmonic mean | 2q₁q₂/(q₁+q₂) | ✓ | ✓ | ✓ | ✗ | ✓* |
> | Minimum | min(q₁,q₂) | ✓ | ✓ | ✓ | ✓ | ✓ |
> | Product (unnormalised) | q₁·q₂ | ✓ | ✗ | ✓ | ✓ | ✓ |
>
> *Harmonic mean reaches zero only in the limit as one input → 0; for any q₁ > 0, the harmonic mean > 0 even if q₂ = 0.*
>
> **Non-compensation** is the key property: it ensures that a domain with qA = 0 (zero effective mastery quality) drives ΨA to zero regardless of the partner domain's quality. This is required by the formal structure of Eq. 19 (both domains must independently exceed θI). The arithmetic mean and harmonic mean both violate non-compensation. The minimum function satisfies non-compensation but is non-differentiable at q₁ = q₂, making it unsuitable for ODE integration. The unnormalised product satisfies all properties except boundedness. The geometric mean is therefore the unique form satisfying all five properties simultaneously — it is not merely convenient but structurally necessary.

**JUSTIFICATION:** This fix provides an exhaustive comparative justification without introducing new axioms (Variant C) or formal theorems. The table makes the choice of multiplicative form transparent and independently verifiable by the reader. It does not change Equation 21 but adds rigorous justification. The non-compensation property is highlighted as the key discriminator, directly addressing why a product is necessary over a sum.
**SAFETY NOTE:** Does not change Equation 21 or any other equation. Does not alter any ODE. Does not touch protected elements. Adds a table and explanatory prose to §3.5 only.
