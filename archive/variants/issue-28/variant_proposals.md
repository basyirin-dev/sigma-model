# Variant Proposals — Issue #28

**Issue #:** 28
**Tag:** [N] — Novelty Defence
**Date:** 2026-03-30
**Negative log check:** Issue #9 Variant A addressed §2.2 gap statement re: meta-learning (Lake & Baroni 2023; Patel et al. 2022; Han & Pad'o 2024). Issue #9 Variant B added Corollary to Categorical Distinction Theorem in §3.1.3. Issue #9 Variant C extended §2.6 synthesis table with meta-learning row. Issue #9 Variant E added Prediction 6b to §9. No repropose of those specific approaches.

---

## Issue Description

The gap statement must address how engineered training distributions allow standard seq2seq models to achieve near-perfect one-shot primitive generalisation on SCAN as reported by Patel et al. (2022). The paper must show why this result does not close the σA gap — specifically, why one-shot primitive generalisation is a δA optimisation that does not transfer to novel compositions outside the engineered distribution.

---

### VARIANT A

**Issue #:** 28
**Tag:** [N]
**Section targeted:** §2.2 Compositional Generalisation — gap statement
**Scope:** local prose fix

**DIAGNOSIS:**
The §2.2 gap statement, after Issue #9's Variant A fix, addresses meta-learning broadly (Lake & Baroni 2023, Patel et al. 2022, Han & Pad'o 2024). However, it does not specifically explain the mechanism by which Patel et al.'s engineered distributions achieve one-shot primitive generalisation and why that mechanism is categorically different from σA formation. A reviewer reading Patel et al. (2022) will see near-perfect SCAN performance and conclude the compositional generalisation problem is solved. The gap statement must make explicit that engineered distributions are a training-time δA intervention that embeds primitive compositions into the training data — reducing the test-time recombination demand rather than increasing the agent's structural recombination capacity.

**PROPOSED FIX:**

*Current text (§2.2, final paragraph, post-Issue #9 fix):*
> **Gap statement.** The compositional generalisation literature characterises the failure mode and provides measurement proxies for σcritical-crossing, but does not formalise σA as the training variable whose dynamics the failure reveals, does not identify what suppresses it, and does not specify how to design training regimes that reliably induce schema crystallisation.

*Replace with:*
> **Gap statement.** The compositional generalisation literature characterises the failure mode and provides measurement proxies for σcritical-crossing, but does not formalise σA as the training variable whose dynamics the failure reveals, does not identify what suppresses it, and does not specify how to design training regimes that reliably induce schema crystallisation. Patel et al. (2022) demonstrate that engineered training distributions — where primitive compositions are pre-exposed during training — achieve near-perfect one-shot primitive generalisation on SCAN. This is a training-time δA intervention: it embeds specific recombination instances into the training data, reducing test-time recombination demand rather than increasing the agent's structural recombination capacity. In H-Bar terms, Patel et al.'s protocol increases δA (parametric depth covering the engineered compositions) without increasing σA (schema coherence supporting novel recombinations outside the engineered set). The OOD/in-distribution accuracy ratio (Eq. 3b) would remain low for compositions not present in the engineered distribution, precisely because the agent has learned those specific compositions rather than the compositional rule itself. The H-Bar contribution is formalising this distinction and specifying the training protocols (§10.6, P1) that increase σA independently of δA.

**JUSTIFICATION:**
This explicitly names the Patel et al. mechanism (embedding compositions into training data) and explains why it is a δA intervention, not a σA intervention. The explanation uses only existing H-Bar terminology (δA, σA, Eq. 3b, §10.6 P1). It does not create new symbols or equations. The reference to §10.6 P1 connects the gap statement to the already-specified training protocol, closing the loop between diagnosis and prescription.

**SAFETY NOTE:**
Does not alter any ODE, Table 1, §3.1.3 definition, or §7 phase conditions. Purely additive prose to an existing gap statement.

---

### VARIANT B

**Issue #::** 28
**Tag:** [N]
**Section targeted:** §3.1.3 Schema Coherence σA(d,t) — Proxy identification (Tier 2, Eq. 3b)
**Scope:** structural equation fix

**DIAGNOSIS:**
The Tier 2 proxy (Eq. 3b) defines σA = Acc_OOD / Acc_In, but the surrounding text does not explain why engineered distributions (Patel et al. 2022) produce high Acc_OOD on their specific test splits while failing the σA proxy. The proxy description needs an explicit boundary condition: the OOD split must test recombination outside the training distribution's engineered compositions, not merely outside the training distribution's surface features. Without this boundary condition, a reviewer could argue that Patel et al.'s one-shot test is an "OOD" split that validates high σA.

**PROPOSED FIX:**

*Current text (§3.1.3, after Eq. 3b):*
> This proxy is valid when the OOD split tests compositional recombination of primitives trained in isolation (e.g., SCAN add-primitive split, COGS systematic split, PCFG-SET productivity split).

*Add after this sentence:*
> **Boundary condition on engineered distributions.** When the training distribution has been engineered to include specific primitive compositions (as in Patel et al., 2022), the OOD split must test recombinations that are *not* present in the engineered set — not merely recombinations with different surface features. Patel et al.'s one-shot primitive generalisation test evaluates recombination accuracy on compositions that were explicitly pre-exposed during training (engineered distribution). This is an in-distribution recombination test, not an OOD structural transfer test. The σA proxy requires OOD splits where the compositional rule must be inferred from primitives trained in isolation, not from compositions pre-embedded in the training data. Formally: σA is non-zero only when Acc_OOD is measured on compositions c where c ∉ T_train (the training set), not merely where surface(c) ∉ surface(T_train).

**JUSTIFICATION:**
This boundary condition prevents a reviewer from conflating Patel et al.'s one-shot test (which tests compositions present in engineered training data) with the σA proxy (which tests compositions absent from any training data). The formal criterion c ∉ T_train is a precise, checkable condition that existing benchmark splits already satisfy (SCAN add-primitive split, COGS systematic split). It does not introduce new symbols — c, T_train are standard set-theoretic notation.

**SAFETY NOTE:**
Does not alter Eq. 3b itself, Table 1, any ODE, or §7 conditions. Adds a boundary condition to the proxy identification prose only.

---

### VARIANT C

**Issue #:** 28
**Tag:** [N]
**Section targeted:** §2.6 Synthesis — Five-Gap Map
**Scope:** systemic reframe

**DIAGNOSIS:**
The §2.6 synthesis table was extended by Issue #9 Variant C to include a "Meta-Learning & Training Regimes" row. However, this row groups meta-learning, engineered distributions, and training regime selection together. Patel et al. (2022) deserves a separate treatment because their mechanism is categorically different from meta-learning: they engineer the training distribution itself, whereas meta-learning modifies the learning algorithm. The table and analysis must distinguish distribution engineering from algorithmic modification to prevent a reviewer from treating them as interchangeable.

**PROPOSED FIX:**

*Replace the Issue #9 Variant C added row with two rows:*

| Literature | H-Bar Variable Addressed | H-Bar Variable Missing |
|---|---|---|
| Curriculum Learning | δA growth rate | σA dynamics, αA, ΞA |
| Compositional Generalisation | σA failure mode (empirical) | σA formation mechanism, suppression |
| Continual Learning | λc (parametric decay) | λf (frontier obsolescence), σA coupling |
| Causal/Structured Repr. | σA target state | σA developmental trajectory, M̂A, μAB |
| Cognitive Evaluation | Faculty identification | Formal theoretical grounding for benchmark design |
| **Meta-Learning (Lake & Baroni 2023; Han & Pad'o 2024)** | **δA optimisation via learning algorithm modification** | **σA as independent variable; OOD/in-distribution dissociation under algorithm change** |
| **Distribution Engineering (Patel et al. 2022)** | **δA optimisation via training data curation — primitive compositions pre-embedded** | **σA as structural recombination capacity distinct from trained-composition recall; Ω_AI suppression** |

*Replace the "Row 6 analysis" paragraph with:*

> **Rows 6–7 analysis.** Two distinct mechanisms produce δA increase without σA increase:
>
> *Algorithmic modification* (Lake and Baroni, 2023; Han and Pad'o, 2024): Meta-learning and training regime selection modify the learning algorithm to improve in-distribution recombination. This increases δA (parametric depth covering training-distribution compositions) without increasing σA (schema coherence supporting novel recombinations). Lake and Baroni (2023) show improved lexical compositionality but persistent structural gaps — a δA gain on proximal tasks without σA gain on structural tasks.
>
> *Distribution engineering* (Patel et al., 2022): Training distributions are curated to include specific primitive compositions, pre-embedding the recombination instances the test will evaluate. This is a training-time δA intervention that reduces test-time recombination demand: the agent does not need structural recombination capacity (σA) because the compositions were already in the training data. The agent recalls trained compositions rather than inferring compositional rules. Patel et al.'s near-perfect one-shot performance is high δA (trained-composition recall) with low σA (no structural recombination capacity for compositions outside the engineered set). This is precisely the high-δA/low-σA failure mode that H-Bar formalises — the agent passes the engineered test because the test does not measure σA.

**JUSTIFICATION:**
Separating meta-learning from distribution engineering prevents a reviewer from treating Patel et al.'s specific mechanism as evidence against σA independence. The "recall vs. inference" framing makes the distinction concrete: engineered distributions teach recall of trained compositions; σA measures inference of novel compositions. This reframing uses existing H-Bar terminology without new symbols.

**SAFETY NOTE:**
Does not alter any equation, Table 1, §3.1.3, or §7 conditions. Modifies only the §2.6 table and analysis paragraph.

---

### VARIANT D

**Issue #:** 28
**Tag:** [N]
**Section targeted:** §9 Eight Falsifiable Predictions — add new prediction after Prediction 6b
**Scope:** structural equation fix

**DIAGNOSIS:**
The paper currently has no prediction that directly tests the Patel et al. (2022) claim. Prediction 6b (added by Issue #9 Variant E) tests meta-learning dissociation via MAML, but does not address distribution engineering. A dedicated prediction is needed that specifies exactly how to test whether Patel et al.'s engineered distribution protocol increases δA without increasing σA — using the three-condition battery (Appendix A.4) as the measurement instrument.

**PROPOSED FIX:**

*After Prediction 6b in §9, add:*

> **Prediction 6c — Distribution Engineering Does Not Transfer σA [NEW]**
>
> **Claim:** Agents trained on engineered distributions that include specific primitive compositions (Patel et al., 2022 protocol) will achieve high accuracy on those compositions (high δA for trained-composition recall) but will show no significant improvement on compositional recombinations absent from the engineered distribution (σA remains low). The OOD/in-distribution accuracy ratio (Eq. 3b) will not increase for compositions outside the engineered set.
>
> **Measurement:** Apply the three-condition battery from Appendix A.4 to agents trained with Patel et al.'s engineered distribution protocol on SCAN:
> 1. ID: accuracy on the engineered training distribution
> 2. OOD-struct: accuracy on compositional recombinations *not* present in the engineered set (primitives trained in isolation, recomposed at test time into novel compositions)
> 3. OOD-surf-conflict: accuracy on surface-feature variants of engineered compositions (tests whether the agent memorised surface patterns)
>
> Compare σA = Acc_OOD-struct / Acc_ID before and after engineering.
>
> **H-Bar claim:** Distribution engineering increases Acc_ID (δA gain from trained-composition recall) without proportional increase in Acc_OOD-struct (σA gain). The SGG widens or remains constant. A "σA = optimised δA" account predicts proportional improvement in both.
>
> **Falsification:** Distribution engineering produces statistically equivalent percentage-point gains in Acc_ID and Acc_OOD-struct (ΔAcc_ID ≈ ΔAcc_OOD-struct, p > 0.05 on the difference).
>
> **Distinguishing from Prediction 6b:** Prediction 6b tests meta-learning (algorithm modification); Prediction 6c tests distribution engineering (training data curation). Both are [N]-tagged predictions testing the "σA = optimised δA" objection, but they test distinct mechanisms. Falsification of one does not falsify the other.

**JUSTIFICATION:**
This prediction creates a direct experimental test of Patel et al.'s result using existing benchmarks and the already-specified three-condition battery. The distinction from Prediction 6b is explicit, preventing a reviewer from treating meta-learning and distribution engineering as interchangeable. The prediction uses only existing proxy definitions (Eq. 3b, Appendix A.4) and introduces no new symbols.

**SAFETY NOTE:**
Does not alter any existing ODE, Table 1, or §7 conditions. Adds one prediction to the existing prediction list. Uses only existing proxy definitions.

---

### VARIANT E

**Issue #:** 28
**Tag:** [N]
**Section targeted:** §10.6 Training Protocols — Protocol P1 description
**Scope:** local prose fix

**DIAGNOSIS:**
§10.6 Protocol P1 specifies how to increase σA at fixed δA via structure-preserving augmentations. However, it does not explicitly contrast this protocol with Patel et al.'s (2022) engineered distribution approach. A reviewer may confuse the two: both involve modifying training data. The P1 description must make clear that P1's augmentations force the agent to infer compositional rules from primitives trained in isolation, whereas Patel et al.'s engineering pre-embeds specific compositions, allowing the agent to recall rather than infer. This is the σA/dA mechanism distinction in protocol form.

**PROPOSED FIX:**

*Current text (§10.6, Protocol P1):*
> **Protocol P1: Increasing σA at fixed δA.**
> To increase schema coherence without increasing parametric depth:
> 1. Begin with a trained agent at target in-distribution accuracy Acc_In = τ.
> 2. Apply structure-preserving data augmentations that force the agent to exploit compositional regularities. Valid augmentations include: (a) primitive recombination — swap primitives trained in isolation to create unseen compositions; (b) template preservation — vary surface tokens while preserving the syntactic template; (c) distributional shift within structure — move to a new surface distribution that shares the same generative grammar.
> 3. Continue training until Acc_In returns to τ. The agent now has higher σA (measured via SGG) at matched δA (matched because parameter count and total gradient steps are held fixed).

*Add after step 3:*
> **Distinction from distribution engineering (Patel et al., 2022).** Patel et al.'s engineered distribution protocol pre-embeds specific primitive compositions into the training data, so the agent can recall trained compositions at test time. This increases δA (trained-composition coverage) without increasing σA (structural recombination capacity for novel compositions). Protocol P1 is categorically different: its augmentations train primitives in isolation and test on recombinations *not* present in the augmented set. The agent cannot recall compositions — it must infer the compositional rule from independently trained primitives. This forced inference is the mechanism by which P1 increases σA. Formally: Patel et al.'s test satisfies c ∈ T_train (tested composition is in training data); P1's test satisfies c ∉ T_train (tested composition is not in training data). The former measures δA; the latter measures σA.

**JUSTIFICATION:**
This contrast directly addresses Issue #28 by showing that P1 and Patel et al.'s protocol are not interchangeable — they test different variables. The formal criterion (c ∈ T_train vs. c ∉ T_train) connects to Variant B's boundary condition, creating internal consistency across the variants. The prose uses only existing H-Bar terminology.

**SAFETY NOTE:**
Does not alter any ODE, Table 1, §3.1.3, or §7 conditions. Adds an explanatory paragraph to an existing protocol description. Does not modify the protocol steps themselves.
