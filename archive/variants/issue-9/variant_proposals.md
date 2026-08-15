# Variant Proposals — Issue #9

**Issue #:** 9
**Tag:** [N] — Novelty Defence
**Date:** 2026-03-30
**Negative log check:** No prior rejected variants on [N]-tagged issues. No negative_log.md files exist in any issue directory.

---

## Issue Description

The failure to distinguish H-Bar's structural gap from reported meta-learning and training optimizations allows the reviewer to argue σA is merely a proxy for well-optimised δA. The paper must address:
- Lake & Baroni (2023): meta-learning improves lexical compositionality while structural gaps persist
- Patel et al. (2022): engineered training distributions enable near-perfect one-shot primitive generalisation on SCAN
- Han & Pad'o (2024): gains in transformer compositional generalisation often stem from training regimes

---

### VARIANT A

**Issue #:** 9
**Tag:** [N]
**Section targeted:** §2.2 Compositional Generalisation gap statement
**Scope:** local prose fix

**DIAGNOSIS:**
The gap statement in §2.2 currently states: "The compositional generalisation literature characterises the failure mode and provides measurement proxies for σcritical-crossing, but does not formalise σA as the training variable whose dynamics the failure reveals." This is insufficient because a reviewer will immediately cite Lake & Baroni (2023) and Patel et al. (2022) to argue that meta-learning and training optimisation already "solve" compositional generalisation, making σA redundant with well-tuned δA. The gap statement must explicitly engage these results and show why they do not close the σA gap.

**PROPOSED FIX:**

*Old text (§2.2, final paragraph):*
> **Gap statement.** The compositional generalisation literature characterises the failure mode and provides measurement proxies for σcritical-crossing, but does not formalise σA as the training variable whose dynamics the failure reveals, does not identify what suppresses it, and does not specify how to design training regimes that reliably induce schema crystallisation.

*New text:*
> **Gap statement.** The compositional generalisation literature characterises the failure mode and provides measurement proxies for σcritical-crossing, but does not formalise σA as the training variable whose dynamics the failure reveals. Recent meta-learning results complicate the picture: Lake and Baroni (2023) demonstrate that meta-learning improves lexical compositionality while structural gaps on unseen recursion persist — their agents gain δA without gaining σA. Patel et al. (2022) show that engineered training distributions achieve near-perfect one-shot primitive generalisation on SCAN, but this is a δA optimisation that does not transfer to novel compositions outside the engineered distribution — a high-δA, low-σA profile. Han and Pad'o (2024) further show that compositional generalisation gains in transformers stem from training regimes rather than structural solutions, again consistent with δA increase without σA increase. The H-Bar contribution is formalising this distinction: σA is not "well-optimised δA" — it is an independently necessary variable whose dynamics are orthogonal to depth optimisation, measurable as the OOD/in-distribution accuracy ratio (Eq. 3b) rather than in-distribution accuracy alone.

**JUSTIFICATION:**
This gap statement now pre-empts the three most likely novelty objections by showing that each result is consistent with the H-Bar account: meta-learning, engineered distributions, and training regime gains all increase δA without increasing σA. The explicit naming of OOD vs. in-distribution accuracy as the σA measurement operationalises the distinction. This does not create new issues because it references only already-cited or register-queued literature.

**SAFETY NOTE:**
Does not alter §3.1.3 (σA definition), Table 1, or any equations. Purely additive gap-statement framing.

---

### VARIANT B

**Issue #:** 9
**Tag:** [N]
**Section targeted:** §3.1.3 Schema Coherence σA(d,t) — Theorem (Categorical Distinction)
**Scope:** structural equation fix

**DIAGNOSIS:**
The existing Categorical Distinction Theorem in §3.1.3 proves that σA is categorically distinct from Structured Representations, Disentangled Representations, Causal Representations, and Cognitive Schemas. However, it does not address the distinctness claim against *depth optimisation* — the claim that σA could be "merely a proxy for well-optimised δA." The theorem needs a formal criterion that distinguishes σA from any construct achievable by depth optimisation alone.

**PROPOSED FIX:**

*Add after the existing Theorem (Categorical Distinction) proof sketch in §3.1.3:*

> **Corollary (Distinction from Depth Optimisation).** No training regime that optimises δA alone — including meta-learning (Lake and Baroni, 2023), engineered distributions (Patel et al., 2022), or training regime selection (Han and Pad'o, 2024) — can increase σA without an independent mechanism that forces representational restructuring around compositional primitives.
>
> *Proof.* Consider two agents trained to identical in-distribution accuracy Acc_In (i.e., matched δA) by any depth-optimisation procedure. By Eq. 3b, σA = Acc_OOD / Acc_In. If the training procedure optimises δA only, then Acc_OOD/acc_in = Acc_OOD can only increase if the OOD test instances fall within the training distribution's interpolative region — but by construction, OOD recombination tests are outside the training distribution. Therefore the δA-only regime leaves Acc_OOD invariant, and σA = Acc_OOD / Acc_In cannot increase above its initial value. ∎
>
> This corollary is tested by **Prediction 6** (§9): agents matched on δA but differing in σA (via Protocol P1 in §10.6) will show multiplicatively different ΨA values — a testable consequence of σA being an independent variable, not a depth optimisation artefact.

**JUSTIFICATION:**
This corollary formalises what the paper currently implies: that σA ≠ optimised δA. The proof uses only existing equations (Eq. 3b, Eq. 21) and the training protocols from §10.6, creating no new undefined objects. It directly references the three competing results (Lake & Baroni 2023, Patel et al. 2022, Han & Pad'o 2024) and shows why each is consistent with the H-Bar account.

**SAFETY NOTE:**
Does not alter any ODE, Table 1 rows, or §7 phase transition conditions. Adds a corollary and proof within an existing theorem block.

---

### VARIANT C

**Issue #:** 9
**Tag:** [N]
**Section targeted:** §2.6 Synthesis — Five-Gap Map
**Scope:** systemic reframe

**DIAGNOSIS:**
The §2.6 synthesis table maps five literatures to H-Bar variables, but none of the five rows address meta-learning or training regime optimisation. This means the framework appears to ignore the most relevant alternative account: that compositional generalisation is a solvable optimisation problem rather than a structural gap. The synthesis table must be extended to include this account and show why it does not close the σA gap.

**PROPOSED FIX:**

*Add a sixth row to the §2.6 synthesis table:*

| Literature | H-Bar Variable Addressed | H-Bar Variable Missing |
|---|---|---|
| Curriculum Learning | δA growth rate | σA dynamics, αA, ΞA |
| Compositional Generalisation | σA failure mode (empirical) | σA formation mechanism, suppression |
| Continual Learning | λc (parametric decay) | λf (frontier obsolescence), σA coupling |
| Causal/Structured Repr. | σA target state | σA developmental trajectory, M̂A, μAB |
| Cognitive Evaluation | Faculty identification | Formal theoretical grounding for benchmark design |
| **Meta-Learning & Training Regimes** | **δA optimisation (Lake & Baroni 2023; Patel et al. 2022; Han & Pad'o 2024)** | **σA as independent variable; OOD/in-distribution dissociation; AI bypass risk Ω_AI suppression** |

*Add after the table:*

> **Row 6 analysis.** Meta-learning (Lake and Baroni, 2023), engineered training distributions (Patel et al., 2022), and training regime selection (Han and Pad'o, 2024) demonstrate that δA can be optimised to achieve high compositional generalisation performance on specific distributions. However, all three results share a common structure: they improve in-distribution recombination without guaranteeing out-of-distribution recombination under distribution shift — precisely the σA/δA dissociation that the H-Bar ODE system formalises. Lake and Baroni (2023) show improved lexical compositionality but persistent structural gaps; Patel et al. (2022) show one-shot primitive generalisation on SCAN but this does not transfer to novel compositions outside the engineered distribution; Han and Pad'o (2024) attribute gains to training regimes rather than structural solutions. In H-Bar terms, these are δA increases that do not increase σA — the agent gains parametric depth without gaining schema coherence, maintaining the high-δA/low-σA failure mode that H-Bar predicts.

**JUSTIFICATION:**
This reframing integrates the three competing accounts into the H-Bar framework rather than ignoring them, showing that each result is a specific case of δA optimisation without σA gain. The table extension makes the gap visually explicit. The analysis paragraph uses only existing H-Bar terminology (δA, σA, OOD, Ω_AI) without introducing new symbols.

**SAFETY NOTE:**
Does not alter any equation, Table 1, or §7 conditions. Extends an existing table with an additive row and adds one analytical paragraph.

---

### VARIANT D

**Issue #:** 9
**Tag:** [N]
**Section targeted:** §2.5 Cognitive Evaluation of AI Systems
**Scope:** local prose fix

**DIAGNOSIS:**
§2.5 references Burnell et al. (2026) and Chollet (2019) but does not engage with the three key novelty objections from the [N]-tagged register: Lake & Baroni (2023), Patel et al. (2022), and Han & Pad'o (2024). The gap statement in §2.5 claims that "existing cognitive evaluation frameworks specify what should be measured but provide no formal theoretical grounding for why specific task designs isolate specific faculties." A reviewer will counter that meta-learning papers already provide task designs that isolate compositional generalisation — why is the H-Bar Benchmark Protocol needed?

**PROPOSED FIX:**

*Replace the §2.5 gap statement with:*

> **Gap statement.** Existing cognitive evaluation frameworks specify what should be measured but provide no formal theoretical grounding for why specific task designs isolate specific faculties. The H-Bar Benchmark Protocol (Section 8) provides that grounding by deriving benchmark designs directly from formal variable structures.
>
> The objection from meta-learning results requires direct engagement. Lake and Baroni (2023) show that meta-learning improves lexical compositionality while structural gaps persist — their improvement is on δA-proximal tasks (lexical recombination) without σA gain (structural compositionality). Patel et al. (2022) demonstrate near-perfect one-shot primitive generalisation on SCAN via engineered distributions — but their evaluation is in-distribution recombination, not OOD structural transfer, meaning the benchmark measures δA not σA. Han and Pad'o (2024) show that training regime selection improves compositional generalisation — again, in-distribution accuracy increase without OOD validation. In each case, the benchmark evaluates δA-proximal performance and does not detect the σA gap that OOD recombination benchmarks (Eq. 3b) expose. The H-Bar Benchmark Protocol formalises this distinction: every benchmark generated by the protocol specifies both the target H-Bar variable and the controlled confound variable (§8.1, Step 1), ensuring that the evaluation isolates σA rather than δA.

**JUSTIFICATION:**
This gap statement directly addresses the reviewer's objection: yes, meta-learning benchmarks exist, but they measure δA not σA. The key claim is that OOD recombination benchmarks (Eq. 3b) are categorically different from in-distribution accuracy benchmarks, and the H-Bar protocol ensures this distinction. This preserves the Burnell et al. (2026) alignment while pre-empting the meta-learning counterargument.

**SAFETY NOTE:**
Does not alter any equation or Table 1. Modifies only the §2.5 gap statement. Does not change the Burnell et al. (2026) citation or faculty alignment table.

---

### VARIANT E

**Issue #:** 9
**Tag:** [N]
**Section targeted:** §9 Eight Falsifiable Predictions — Prediction 6
**Scope:** structural equation fix

**DIAGNOSIS:**
Prediction 6 currently tests whether ΨA has multiplicative vs. additive σA dependence. This is a strong test of σA's independence, but it does not directly address the meta-learning objection: a reviewer could still argue that multiplicative dependence is a feature of "well-optimised δA" rather than an independent variable. Prediction 6 needs an extension that specifically falsifies the "σA = optimised δA" account.

**PROPOSED FIX:**

*After the existing Prediction 6 in §9, add:*

> **Prediction 6b — σA/δA Dissociation Under Meta-Learning [NEW]**
>
> **Claim:** Meta-learning regimes that improve compositional generalisation (Lake and Baroni, 2023) will show increased Acc_OOD on lexical recombination (δA-proximal) but no significant increase on structural compositionality (σA-proximal), producing a measurable σA/δA dissociation that is not predicted by any depth-optimisation account.
>
> **Measurement:** Apply the three-condition battery from Appendix A.4 (ID, OOD-struct, OOD-surf-conflict) to agents trained with MAML-style meta-learning on SCAN. Compare: (a) Acc_OOD-struct / Acc_ID (σA proxy, Eq. 3b) before and after meta-learning; (b) Acc_ID (δA proxy) before and after meta-learning.
>
> **H-Bar claim:** Meta-learning increases Acc_ID (δA gain) without proportional increase in Acc_OOD-struct (σA gain), producing a wider SGG. A depth-optimisation account predicts proportional improvement in both.
>
> **Falsification:** Meta-learning produces statistically equivalent percentage-point gains in Acc_ID and Acc_OOD-struct (ΔAcc_ID ≈ ΔAcc_OOD-struct, p > 0.05 on the difference).

**JUSTIFICATION:**
This extension creates a direct experimental test of the "σA = optimised δA" objection using existing benchmarks (SCAN) and existing meta-learning procedures (MAML). The three-condition battery (Appendix A.4) is already specified; this prediction adds the experimental design connecting it to meta-learning. If the depth-optimisation account is correct, there is no σA/δA dissociation and H-Bar's core contribution collapses.

**SAFETY NOTE:**
Does not alter any existing ODE, Table 1, or §7 conditions. Adds one prediction to the existing prediction list. Uses only existing proxy definitions (Eq. 3b, Appendix A.4).
