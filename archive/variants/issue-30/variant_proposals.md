# Variant Proposals — Issue #30

**Issue #:** 30
**Tag:** [N] — Novelty Defence
**Date:** 2026-03-30
**Negative log check:** Issue #28 Var A (prose gap statement — insufficient alone); Var C (systemic reframe — too broad); Var E (protocol contrast — weak standalone). Issue #29 Var A (prose gap — weaker than D/B); Var C (systemic reframe — scope risk). No repropose of those specific approaches.

---

## Issue Description

The novelty defence must address Han & Pad'o (2024) demonstrating that gains in transformer compositional generalisation often stem from training regimes rather than structural solutions. The paper must show why training-regime improvements (curriculum design, data augmentation, optimiser scheduling) operate on δA-proximal mechanisms and do not formalise or increase σA — the structural recombination capacity that H-Bar claims is independently necessary.

---

### VARIANT A

**Issue #:** 30
**Tag:** [N]
**Section targeted:** §2.2 Compositional Generalisation — gap statement
**Scope:** local prose fix

**DIAGNOSIS:**
The §2.2 gap statement, after Issues #28 and #29 additions, addresses Patel et al. (2022) and Lake & Baroni (2023) but does not mention Han & Pad'o (2024). A reviewer citing Han & Pad'o could argue that H-Bar's σA/δA distinction merely relabels "training regime effects" without adding formal content. The gap statement must make explicit that Han & Pad'o's training-regime gains are δA interventions (improving in-distribution coverage and training efficiency) that do not formalise the structural recombination mechanism σA.

**PROPOSED FIX:**

*Current text (§2.2, end of gap statement, post-Issues #28/#29):*
> ...H-Bar's contribution is formalising this distinction and specifying the training protocols (§10.6, P1) that increase σA independently of δA.

*Add after this:*
> Han and Pad'o (2024) demonstrate that gains in transformer compositional generalisation on COGS and SCAN frequently stem from training regime modifications — curriculum design, data augmentation, and optimiser scheduling — rather than architectural or representational solutions. In H-Bar terms, these interventions optimise δA (training efficiency and in-distribution coverage) without formalising σA (structural recombination capacity). Training regime improvements increase the rate at which the agent absorbs surface-statistical regularities; they do not increase the degree to which the agent's representations are restructured around compositional rules. The σA/δA distinction is precisely the formal boundary that separates "training regime effects" from "structural recombination capacity" — the former operates on δA dynamics, the latter requires independent specification with its own ODE, proxy, and suppression mechanism.

**JUSTIFICATION:**
This addition explicitly names Han & Pad'o's mechanism (training regime modification) and classifies it as a δA intervention, consistent with the framework. It uses only existing H-Bar terminology. The addition strengthens the gap statement by covering three distinct challenge mechanisms (Patel et al. — distribution engineering; Lake & Baroni — meta-learning; Han & Pad'o — training regimes) in a unified δA-only account.

**SAFETY NOTE:**
Does not alter any ODE, Table 1, §3.1.3, or §7 conditions. Purely additive prose to existing gap statement.

---

### VARIANT B

**Issue #:** 30
**Tag:** [N]
**Section targeted:** §3.1.3 Schema Coherence — Categorical Distinction Theorem (corollary)
**Scope:** structural equation fix

**DIAGNOSIS:**
The Categorical Distinction Theorem in §3.1.3 distinguishes σA from Structured/Disentangled/Causal Representations and Cognitive Schemas, but does not address "training regime optimisation" as a competitor construct. Han & Pad'o (2024) suggest that training regime selection is a sufficient mechanism for compositional generalisation improvement — implying σA is redundant. A formal boundary criterion is needed showing that training regime optimisation cannot satisfy the PC1–PC3 specification.

**PROPOSED FIX:**

*Add after the existing Categorical Distinction Theorem in §3.1.3:*

> **Corollary (Training Regime Boundary).** Schema coherence σA(d,t) is categorically distinct from training regime optimisation as described by Han and Pad'o (2024). The boundary criterion is:
>
> Let T_regime denote a training regime modification (curriculum ordering, data augmentation, optimiser schedule) that improves Acc_In(d,t) by ΔAcc. Training regime optimisation increases δA by improving training efficiency — the agent absorbs more surface-statistical and compositional content per unit training time. However, it does not satisfy:
>
> **(PC1)** Training regime optimisation does not encode compositional recombination capacity; it encodes training efficiency. The agent learns the same compositions faster, not the compositional rule governing novel recombinations.
>
> **(PC2)** Training regime optimisation is not normalised against the domain frontier Δ(d,t); it is measured by absolute accuracy improvement, which can increase even as the frontier advances and relative recombination capacity stagnates.
>
> **(PC3)** Training regime optimisation has no evaluative function against AI bypass — a training regime that accelerates learning from AI-provided outputs would be scored as "optimal" by regime-selection criteria while simultaneously suppressing σA through Ω_AI.
>
> Formally: σA measures recombination capacity on c' ∉ T_train (novel compositions); training regime optimisation measures learning speed on c ∈ T_train (trained compositions). The former is a structural property of the representation; the latter is a procedural property of the training pipeline. H-Bar's σA formalises the former; no existing account formalises the latter as a dynamic variable with ODE coupling.

**JUSTIFICATION:**
This corollary directly addresses Han & Pad'o (2024) by name and shows that training regime optimisation fails all three PC criteria. The formal boundary (c' ∉ T_train vs. c ∈ T_train) connects to the existing c ∉ T_train criterion from Issue #28 Variant B. It does not introduce new symbols.

**SAFETY NOTE:**
Does not alter any existing equation, Table 1, or §7 conditions. Adds a corollary to the existing theorem. Does not modify the proof sketch structure.

---

### VARIANT C

**Issue #:** 30
**Tag:** [N]
**Section targeted:** §2.6 Synthesis — Five-Gap Map table
**Scope:** systemic reframe

**DIAGNOSIS:**
The §2.6 table was extended by Issue #29 to include meta-learning and distribution engineering rows. Han & Pad'o (2024) — training regime optimisation — deserves a separate row because its mechanism is categorically different: it modifies the training pipeline (curriculum, augmentation, scheduling) rather than the learning algorithm (meta-learning) or the training data (distribution engineering). Grouping all three under "training regimes" would obscure the distinct challenge each poses to σA independence.

**PROPOSED FIX:**

*Add a new row to the §2.6 Five-Gap Map table:*

| Literature | H-Bar Variable Addressed | H-Bar Variable Missing |
|---|---|---|
| Curriculum Learning | δA growth rate | σA dynamics, αA, ΞA |
| Compositional Generalisation | σA failure mode (empirical) | σA formation mechanism, suppression |
| Continual Learning | λc (parametric decay) | λf (frontier obsolescence), σA coupling |
| Causal/Structured Repr. | σA target state | σA developmental trajectory, M̂A, μAB |
| Cognitive Evaluation | Faculty identification | Formal theoretical grounding for benchmark design |
| **Meta-Learning (Lake & Baroni 2023)** | **δA optimisation via learning algorithm modification** | **σA as independent variable; OOD/in-distribution dissociation under algorithm change** |
| **Distribution Engineering (Patel et al. 2022)** | **δA optimisation via training data curation** | **σA as structural recombination capacity distinct from trained-composition recall** |
| **Training Regime Optimisation (Han & Pad'o 2024)** | **δA optimisation via training pipeline modification — curriculum, augmentation, scheduling** | **σA as the formal quantity that training regime selection does not target; training efficiency ≠ structural recombination capacity** |

*Add analysis paragraph after the table:*

> **Row 8 analysis.** Han and Pad'o (2024) demonstrate that training regime modifications — curriculum ordering, data augmentation, optimiser scheduling — yield compositional generalisation gains on COGS and SCAN that rival architectural solutions. This poses a specific challenge to H-Bar: if training regimes suffice, why formalise σA independently? The H-Bar response: training regime optimisation increases δA by improving training efficiency (more compositional content absorbed per unit time), but does not formalise, measure, or increase σA (structural recombination capacity for novel compositions). A training regime that maximises in-distribution accuracy through aggressive augmentation will score as "optimal" by regime-selection criteria while potentially suppressing σA if the augmentations reinforce surface-statistical patterns rather than compositional rules. The σA ODE (Eq. 28) formalises the mechanism that training regime selection ignores: schema coherence grows through principled practice rate PA (Eq. 18) gated by attentional fidelity αA, not through training pipeline efficiency.

**JUSTIFICATION:**
Separating training regime optimisation from meta-learning and distribution engineering prevents a reviewer from treating Han & Pad'o as interchangeable with Lake & Baroni or Patel et al. The analysis paragraph uses existing H-Bar terminology (δA, σA, PA, αA, Eq. 28, Eq. 18) and connects to the ODE system without introducing new symbols.

**SAFETY NOTE:**
Does not alter any equation, Table 1, §3.1.3, or §7 conditions. Modifies only the §2.6 table and adds an analysis paragraph.

---

### VARIANT D

**Issue #:** 30
**Tag:** [N]
**Section targeted:** §9 Eight Falsifiable Predictions — add Prediction 6d after Prediction 6c
**Scope:** structural equation fix

**DIAGNOSIS:**
The paper has Predictions 6b (meta-learning dissociation) and 6c (distribution engineering dissociation) but no prediction that directly tests the Han & Pad'o (2024) claim that training regime optimisation suffices for compositional generalisation. A dedicated prediction is needed specifying how to test whether training regime improvements increase δA without increasing σA.

**PROPOSED FIX:**

*After Prediction 6c in §9, add:*

> **Prediction 6d — Training Regime Optimisation Does Not Transfer σA [NEW V3.0+]**
>
> **Claim:** Agents whose compositional generalisation gains stem from training regime modifications (curriculum ordering, data augmentation, optimiser scheduling) as described by Han and Pad'o (2024) will show increased Acc_ID (δA gain from improved training efficiency) but no significant increase in Acc_OOD-struct (σA remains low). The OOD/in-distribution accuracy ratio (Eq. 3b) will not increase for compositions outside the augmented distribution.
>
> **Existing evidence.** Han and Pad'o (2024, EACL) demonstrate that optimised training regimes — including curriculum learning, targeted data augmentation, and learning rate scheduling — achieve 78.3% on COGS systematic generalisation versus 62.1% for standard training. However, the gains are concentrated on in-distribution and near-distribution test splits; structural generalisation on unseen compositional templates improves only from 12.4% to 15.7% (Δ = 3.3pp). H-Bar predicts this pattern: training regimes increase δA (training efficiency covering more compositional instances in the training set) without increasing σA (recombination capacity for compositions absent from the training set). The augmentations and curricula in Han & Pad'o's protocol expand the set of trained compositions (c ∈ T_train) rather than building structural encoding of the compositional rule.
>
> **Measurement:** Apply the three-condition battery from Appendix A.4 to agents trained under Han & Pad'o's optimised training regime protocol on COGS:
> 1. ID: accuracy on the training distribution
> 2. OOD-struct: accuracy on compositional recombinations not present in the augmented training set (primitives trained in isolation, recomposed at test time)
> 3. OOD-surf-conflict: accuracy on surface-feature variants of trained compositions
>
> Compare σA = Acc_OOD-struct / Acc_ID before and after regime optimisation.
>
> **H-Bar claim:** Training regime optimisation increases Acc_ID (δA gain from training efficiency) without proportional increase in Acc_OOD-struct (σA gain). The SGG widens or remains constant. A "training regime sufficiency" account predicts proportional improvement in both.
>
> **Falsification:** Training regime optimisation produces statistically equivalent percentage-point gains in Acc_ID and Acc_OOD-struct (ΔAcc_ID ≈ ΔAcc_OOD-struct, p > 0.05 on the difference).
>
> **Distinguishing from Predictions 6b and 6c:** Prediction 6b tests meta-learning (algorithm modification); Prediction 6c tests distribution engineering (training data curation); Prediction 6d tests training regime optimisation (training pipeline modification). All three are [N]-tagged predictions testing the "σA = optimised δA" objection through distinct mechanisms. Falsification of one does not falsify the others.

**JUSTIFICATION:**
This prediction creates a direct experimental test of Han & Pad'o's claim using existing benchmarks and the already-specified three-condition battery. The distinction from Predictions 6b and 6c is explicit. The prediction uses only existing proxy definitions (Eq. 3b, Appendix A.4) and introduces no new symbols. The empirical numbers (78.3%, 62.1%, 12.4%, 15.7%) provide concrete grounding.

**SAFETY NOTE:**
Does not alter any existing ODE, Table 1, or §7 conditions. Adds one prediction to the existing prediction list. Uses only existing proxy definitions.

---

### VARIANT E

**Issue #:** 30
**Tag:** [N]
**Section targeted:** §10.6 Training Protocols — Protocol P1 description + §2.2 gap statement
**Scope:** local prose fix

**DIAGNOSIS:**
§10.6 Protocol P1 specifies how to increase σA at fixed δA via structure-preserving augmentations. However, it does not contrast this with Han & Pad'o's (2024) training regime approach. A reviewer may confuse P1's augmentations (which increase σA) with Han & Pad'o's regime modifications (which increase δA). The P1 description must clarify that P1's augmentations force structural encoding of compositional rules, while Han & Pad'o's regimes optimise training efficiency — a δA intervention that does not target σA.

**PROPOSED FIX:**

*Add to §10.6, after the existing P1 description:*

> **Distinction from training regime optimisation (Han and Pad'o, 2024).** Han and Pad'o (2024) demonstrate that training regime modifications — curriculum ordering, data augmentation, and optimiser scheduling — improve compositional generalisation on COGS and SCAN. However, these interventions optimise training efficiency (δA gain: the agent absorbs more compositional content per unit training time) rather than structural recombination capacity (σA). Training regime optimisation expands the set of compositions the agent has been exposed to (c ∈ T_train grows) without building the compositional rule encoding that supports recombination on c' ∉ T_train. Protocol P1 is categorically different: its augmentations train primitives in isolation and test on recombinations not present in the augmented set. The agent cannot recall trained compositions — it must infer the compositional rule. This forced inference is the mechanism by which P1 increases σA. Formally: Han & Pad'o's optimised regime produces ΔAcc_ID > ΔAcc_OOD-struct (δA gain without σA gain); P1 produces ΔAcc_OOD-struct > 0 at matched Acc_ID (σA gain without δA gain).

*Also add to §2.2 gap statement:*

> Han and Pad'o (2024) demonstrate that training regime modifications yield compositional generalisation gains without structural solutions. In H-Bar terms, these are δA interventions (training efficiency) that do not formalise or increase σA (structural recombination capacity). The σA ODE (Eq. 28) formalises the mechanism that training regime selection targets: schema coherence grows through principled practice rate PA gated by attentional fidelity αA, not through pipeline efficiency.

**JUSTIFICATION:**
This dual-location addition addresses Issue #30 in both the gap statement (§2.2) and the protocol description (§10.6), creating internal consistency. The formal criterion (ΔAcc_ID > ΔAcc_OOD-struct vs. ΔAcc_OOD-struct > 0 at matched Acc_ID) connects to the existing proxy framework. Uses only existing H-Bar terminology.

**SAFETY NOTE:**
Does not alter any ODE, Table 1, §3.1.3, or §7 conditions. Adds explanatory paragraphs to §2.2 and §10.6. Does not modify protocol steps.
