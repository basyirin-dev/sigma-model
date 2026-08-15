## Complete Tag Reference (V3.0+)

| Tag | Meaning |
|-----|---------|
| [D] | Definitional weakness — σA or adjacent construct boundary |
| [O] | ODE / mathematical inconsistency — equations, couplings, closure |
| [P] | Phase transition — transition conditions not observable without proxy |
| [N] | Novelty claim — δA-only alternative not excluded |
| [Ψ] | ΨA multiplicative form — justification or falsifiability gap |
| [Δ] | Delegation scope — single vs. multi-agent blurring |
| [B] | Human-cognitive bridge — scope discipline violation |
| [L] | Limitation — absent or understated |
| [R] | Missing reference from Phase 1 Falcon sweep |
| [α] | Attentional fidelity — αA coupling or ODE issues |
| [Ξ] | Executive control — ΞA formalisation or integration |
| [M] | Metacognitive self-model — M̂A, ζA dynamics or scope |
| [S] | Social cognition — μAB, τA, ΣA,B coupling or scope |
| [Θ] | Cross-modal transfer — ΘA, ω(m1,m2) formalisation |
| [V] | Benchmark validity — VA, CI, FD, DG, RA issues |
| [I] | Integration seam — cross-version coherence issues |
| [T] | Score trajectory table — §1.3 methodology framing |

---

## TIER 1A — ODE System Closure

All `[O]`-tagged issues + all integration_map.md rows where Consistency Verified = NO. Priority order: (1) rA(d,t) functional form and σA coupling, (2) all V2.0 ODE closures, (3) all V3.0/V3.0+ ODE closures.

## ISSUE #4
**Tag:** [O]
**Severity:** HIGH
**Description:** The parametric decay term λc incorrectly references σA via the rehearsal engagement rate rA, which is defined using only elapsed time without structural coupling.
**Status:** RESOLVED — Variant E, 2026-03-30

## ISSUE #5
**Tag:** [α]
**Severity:** HIGH
**Description:** The attentional fidelity ODE relies on surface-reward pressure which lacks a formal definition, proxy identification, or calibration procedure.
**Status:** RESOLVED — Variant E, 2026-03-30

## ISSUE #6
**Tag:** [Ξ]
**Severity:** HIGH
**Description:** The optimal sub-state values for the executive control ODE are not formally defined for each of the five training phases.
**Status:** RESOLVED — Variant D, 2026-03-30

## ISSUE #22
**Tag:** [V]
**Severity:** HIGH
**Description:** The benchmark reliability function can theoretically return negative values when the coefficient of variation exceeds one, violating the bounded validity requirement.
**Status:** RESOLVED — Variant D, 2026-03-30

## ISSUE #23
**Tag:** [M]
**Severity:** HIGH
**Description:** The metacognitive self-model ODE lacks a formal guarantee that values remain bounded when distorted by the AI bypass term.
**Status:** RESOLVED — Variant E, 2026-03-30

---

## TIER 1B — Definitional and Novelty Boundaries

All `[D]`-tagged issues + all `[α]`, `[Ξ]`, `[M]`, `[S]`, `[Θ]`, `[V]` issues involving definitional distinctness.

## ISSUE #1
**Tag:** [D]
**Severity:** HIGH
**Description:** The primary definition of schema coherence relies on rhetorical cognitive psychology vocabulary rather than rigorous mathematical grounding with an operationalisable proxy.
**Status:** RESOLVED — Variant E, 2026-03-30

## ISSUE #2
**Tag:** [D]
**Severity:** HIGH
**Description:** The latent variable σA is treated as an operative state variable throughout the framework without providing a formalised computational proxy independent of downstream benchmark results.
**Status:** RESOLVED — Variant C, 2026-03-30

## ISSUE #3
**Tag:** [D]
**Severity:** HIGH
**Description:** The distinctions in the Excess column of the σA mapping table are based on temporal dynamics rather than categorical differences in representational content.
**Status:** RESOLVED — Variant E, 2026-03-30

---

## TIER 2 — Novelty Defence and Falsifiability

Priority: all `[N]`-tagged issues, then `[P]`, then `[Ψ]`, then `[R]`.

## ISSUE #7
**Tag:** [P]
**Severity:** MEDIUM
**Description:** The Phase 2 transition is triggered by an unobservable latent variable and lacks a formalised differential proxy signal for external verification.
**Status:** RESOLVED — Variant C, 2026-03-30

## ISSUE #8
**Tag:** [P]
**Severity:** MEDIUM
**Description:** The paper lacks a mathematical criterion such as sensitivity analysis to demonstrate which growth-limiting variable is dominant at any given threshold.
**Status:** RESOLVED — Variant C, 2026-03-30

## ISSUE #9
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The failure to distinguish Σ-Model's structural gap from reported meta-learning and training optimizations allows the reviewer to argue σ is merely a proxy for well-optimised δ.
**Status:** RESOLVED — Variant E, 2026-03-30

## ISSUE #10
**Tag:** [P]
**Severity:** MEDIUM
**Description:** The empirical prediction requires matching agents on δA while varying σA but does not specify a protocol to independently increase schema coherence without increasing depth.
**Status:** RESOLVED — Variant C, 2026-03-30

## ISSUE #11
**Tag:** [Ψ]
**Severity:** MEDIUM
**Description:** The multiplicative dependence for intersection discovery is asserted without a first-principles derivation showing why a product is necessary over a non-linear sum.
**Status:** RESOLVED — Variant D, 2026-03-30

## ISSUE #12
**Tag:** [R]
**Severity:** MEDIUM
**Description:** The paper claims empirical motivation from model-merging for its discovery rate mechanism but provides no citations to support the synergistic emergence claim.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added citations to Lu et al. (2024), Akiba et al. (2024), Yadav et al. (2024), and Sung et al. (2023) in §3.5.

## ISSUE #28
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The gap statement must address how engineered training distributions allow standard seq2seq models to achieve near-perfect one-shot primitive generalisation on SCAN as reported by Patel et al. (2022).
**Status:** RESOLVED — Variant D, 2026-03-30

## ISSUE #29
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The framework must engage with the finding from Lake & Baroni (2023) that meta-learning improves lexical compositionality while structural gaps persist.
**Status:** RESOLVED — Variant D, 2026-03-30

## ISSUE #30
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The novelty defence must address Han & Pad'o (2024) demonstrating that gains in transformer compositional generalisation often stem from training regimes rather than structural solutions.
**Status:** RESOLVED — Variant D, 2026-03-30

## ISSUE #31
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The paper must differentiate the structural σA gap from the Mirage model's symbolic System-2 requirement for solving compositionality as noted by Noviello et al. (2025).
**Status:** RESOLVED — Batch R2, 2026-03-30. Added differentiation paragraph in §2.2.1 citing σA ODE (Eq. 28) and σ_critical bifurcation (Eq. 51) as neural-substrate alternatives to Mirage's symbolic module requirement.

## ISSUE #32
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The gap statements must incorporate the SLOG benchmark results from Li et al. (2023) which foreground persistent failures on unseen recursion.
**Status:** RESOLVED — Batch R2, 2026-03-30. Added differentiation paragraph in §2.2.1 citing σA ODE (Eq. 28), SGG proxy (Eq. 3b), and Ψ_A geometric mean (Eq. 21) to characterise SLOG recursion failures as Phase 1 diagnostic.

## ISSUE #33
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The framework must address Bruns (2025) which uses RASP to prove structural representability exists in transformers even when learnability fails.
**Status:** RESOLVED — Batch R2, 2026-03-30. Added differentiation paragraph in §2.2.1 citing αA ODE (Eq. 29) and R_A^surface as the formal learnability mechanism complementing Bruns' representability proof.

## ISSUE #34
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The paper must acknowledge that mutual exclusivity training pushed COGS lexical scores higher while structural splits remained below 1% in Jiang et al. (2022).
**Status:** RESOLVED — Batch R2, 2026-03-30. Added differentiation paragraph in §2.2.1 citing σA ODE (Eq. 28) αA gating and Ψ_A multiplicative form (Eq. 21) to characterise ME training as δA/σA dissociation instantiating the High-δA/Low-σA diagnostic cell.

## ISSUE #35
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The novelty defence needs to address how dataset cartography curricula yield gains without closing structural compositionality gaps as observed by Ince et al. (2023).
**Status:** RESOLVED — Batch R2, 2026-03-30. Added differentiation paragraph in §2.2.1 citing η Gompertz (Eq. 13) and σA ODE (Eq. 28) to characterise cartography as δA-only accelerator that does not address the αA gating mechanism required for σ_critical-crossing.

## ISSUE #36
**Tag:** [N]
**Severity:** MEDIUM
**Description:** The gap statement should note that large pretrained models still exhibit lag on deeper recursion and unseen structures according to Zhou et al. (2023).
**Status:** RESOLVED — Batch R2, 2026-03-30. Added differentiation paragraph in §2.2.1 citing Γ_AI breadth growth (Eq. 16), σA ODE (Eq. 28), and Phase 1 characterisation to explain pretrained models' recursion lag as high-δA/low-σA regime with suppressed αA from high R_A^surface.

## ISSUE #37
**Tag:** [R]
**Severity:** LOW
**Description:** Add a citation to Lu et al. (2024) to support the claim that merged models exhibit emergent capabilities that surpass individual parent contributions.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Lu et al. (2024) to §3.5 body text and §13 References.

## ISSUE #38
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Akiba et al. (2024) regarding evolutionary model merging recipes that yield emergent cross-domain skills.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Akiba et al. (2024) to §3.5 body text and §13 References.

## ISSUE #39
**Tag:** [R]
**Severity:** LOW
**Description:** Provide citation for Yadav et al. (2024) establishing that merging capable experts systematically improves zero-shot generalisation.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Yadav et al. (2024) to §3.5 body text and §13 References.

## ISSUE #40
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Sung et al. (2023) as evidence for synergistic multimodal cross-task model merging.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Sung et al. (2023) to §3.5 body text and §13 References.

## ISSUE #41
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Liu et al. (2025) to document that low-quality source domains can suppress target performance in multi-agent RL.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Liu et al. (2025) to §4.2 body text and §13 References.

## ISSUE #42
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Guo et al. (2022) to support the existence of interaction-sensitive effects in cross-domain recommendation systems.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Guo et al. (2022) to §4.2 body text and §13 References.

## ISSUE #43
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Serrano et al. (2024) to acknowledge review evidence that poorly matched sources harm cross-domain learning.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Serrano et al. (2024) to §4.2 body text and §13 References.

## ISSUE #44
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Sui et al. (2024) to support the αA motivation regarding the separation of causal from shortcut features in attention.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Sui et al. (2024) to §4.1 body text and §13 References.

## ISSUE #45
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Oren et al. (2020) to ground the claim that attention alignment to token-rule structure improves compositional generalisation.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Oren et al. (2020) to §4.1 body text and §13 References.

## ISSUE #46
**Tag:** [R]
**Severity:** LOW
**Description:** Provide citation for Li et al. (2025) showing that hierarchical attention patterns predict behaviour on unseen OOD data.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Li et al. (2025) to §4.1 body text and §13 References.

## ISSUE #47
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Liao et al. (2025) as precedent for using attention sharpness to ensure weights favour invariant structural components.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Liao et al. (2025) to §4.1 body text and §13 References.

## ISSUE #48
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Jones & Fuhg (2025) as a precedent for attention-based gating inside a neural ODE framework.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Jones & Fuhg (2025) to §4.1 body text and §13 References.

## ISSUE #49
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Robertazzi et al. (2022) as motivation for formal inhibition variables in brain-inspired meta-RL.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Robertazzi et al. (2022) to §4.3 body text and §13 References.

## ISSUE #50
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Piray & Daw (2021) to ground the formal modelling of planning and cognitive control costs in RL.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Piray & Daw (2021) to §4.3 body text and §13 References.

## ISSUE #51
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Rmus et al. (2020) regarding the role of executive function in defining state and action spaces for reinforcement learning.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Rmus et al. (2020) to §4.3 body text and §13 References.

## ISSUE #52
**Tag:** [R]
**Severity:** LOW
**Description:** Provide citation for Nair et al. (2023) which models response inhibition as a meta-parameter in unified cognitive architectures.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Nair et al. (2023) to §4.3 body text and §13 References.

## ISSUE #53
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Dunovan et al. (2017) regarding the adjustment of inhibitory boundaries in response to performance feedback.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Dunovan et al. (2017) to §4.3 body text and §13 References.

## ISSUE #54
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Wenxuan et al. (2024) to support the ΘA motivation concerning the measurement of modality knowledge discrepancy.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Wenxuan et al. (2024) to §5.1 body text and §13 References.

## ISSUE #55
**Tag:** [R]
**Severity:** LOW
**Description:** Cite the multimodal alignment and fusion survey by Li & Tang (2024) as prior work for cross-modal transfer logic.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Li & Tang (2024) to §5.1 body text and §13 References.

## ISSUE #56
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Lin et al. (2025) for their work on contrastive modality-disentangled learning and shared stream enforcement.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Lin et al. (2025) to §5.1 body text and §13 References.

## ISSUE #57
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Lu et al. (2025) regarding the Platonic Representation Hypothesis and the emergent alignment potential across modalities.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Lu et al. (2025) to §5.1 body text and §13 References.

## ISSUE #58
**Tag:** [R]
**Severity:** LOW
**Description:** Add a citation to Griot et al. (2025) regarding the MetaMedQA benchmark to support the novelty of the H-MCB calibration protocol.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Griot et al. (2025) to §4.4 body text and §13 References.

## ISSUE #59
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Kim et al. (2025) concerning the ObjexMT benchmark and its treatment of jailbreak scenarios in metacognitive calibration.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Kim et al. (2025) to §4.4 body text and §13 References.

## ISSUE #60
**Tag:** [R]
**Severity:** LOW
**Description:** Provide a citation for Kaijing et al. (2024) establishing KOR-Bench as a relevant precedent for knowledge-orthogonal reasoning tasks.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Kaijing et al. (2024) to §4.4 body text and §13 References.

## ISSUE #61
**Tag:** [R]
**Severity:** LOW
**Description:** Cite Mishra et al. (2022) regarding LILA mathematical reasoning tasks as an existing source for robust out-of-distribution evaluation splits.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Mishra et al. (2022) to §4.4 body text and §13 References.

## ISSUE #62
**Tag:** [R]
**Severity:** LOW
**Description:** Add a citation to the DMC framework by Wang et al. (2025) to ground the formal decoupling of cognitive and metacognitive abilities.
**Status:** RESOLVED — Batch R1, 2026-03-30. Added Wang et al. (2025) to §4.4 body text and §13 References.

---

## CHECKPOINT LOG

### Checkpoint A — After 9 Approved Edits (Issues #1–#6, #10, #22, #23)
**Date:** 2026-03-30
**Sections reviewed:** §3.1.3, §3.3, §4.1, §4.3, §4.4, §6.1, §10.6, Appendix A.1–A.9
**Result:** No new issues introduced. All 12 dimensions PASS or PARTIAL PASS. Issue #17 (parameter calibration) validated as persistent concern. A.8 formula/table discrepancy noted (pre-existing, not a regression).
**Hackathon tracks updated:** track_learning.md (Issue #10), track_attention.md (Issue #5), track_executive.md (Issue #6)

### Checkpoint B — After All Tier 1A Issues Resolved
**Date:** 2026-03-30
**Trigger:** All `[O]`-tagged issues resolved (#4); integration map Tier 1A rows confirmed YES
**Scope:** Complete Mathematical Appendix (§12), Equations A.1–A.13
**Result:** No new `[O]` issues created. ODE system functionally closed. Threshold conditions consistent. rA-σA coupling formally correct. Constants NOT consolidated in §10 (validates Issue #17). A.8 formula/table inconsistency flagged.
**Recommendation:** Proceeding to Tier 2 is safe. No blockers from checkpoint reviews.

---

## TIER 3 — Scope, Framing, and Completeness

Priority: all `[Δ]`, `[B]`, `[L]`, `[I]`, `[T]` issues. The `[T]` issue (score trajectory table) is Tier 3 Priority 1.

## ISSUE #13
**Tag:** [Δ]
**Severity:** MEDIUM
**Description:** The definition of AI depth is ambiguous as to whether it represents a global state-of-the-art benchmark or a specific system instance available to the agent.
**Status:** RESOLVED — Final Integration Sweep, 2026-03-30. Added δ_AI agent-independence clarification in §3.6.

## ISSUE #14
**Tag:** [Δ]
**Severity:** MEDIUM
**Description:** The mechanism by which an agent strategically redirects effort away from delegatable tasks lacks formalisation within the system ODEs.
**Status:** RESOLVED — Final Integration Sweep, 2026-03-30. δ_AI scoped as agent-independent global baseline; delegation gradient formalised as single-agent comparison against shared δ_AI(s,t).

## ISSUE #15
**Tag:** [B]
**Severity:** LOW
**Description:** The use of anthropomorphic labels for the executive control sub-components imports psychological baggage that exceeds the formal agent-training state variables.
**Status:** RESOLVED — Final Integration Sweep, 2026-03-30. Added scoping disclaimers in §4.3.1 and §4.4.1 clarifying labels are borrowed for descriptive precision, not cognitive equivalence claims.

## ISSUE #16
**Tag:** [B]
**Severity:** LOW
**Description:** Concluding prescriptions for curriculum design and human interaction drift into advisory language for practitioners rather than staying within the formal scope.
**Status:** RESOLVED — Final Integration Sweep, 2026-03-30. §4.3.1 and §4.4.1 scoping disclaimers anchor label usage to formal ODE system scope.

## ISSUE #17
**Tag:** [L]
**Severity:** MEDIUM
**Description:** Multiple rate constants and parameters used in the ODE system are currently neither operationalised nor measurable, rendering the full system non-simulatable.
**Status:** RESOLVED — Batch R3, 2026-03-30. Added §10.7 Parameter Calibration acknowledging unoperationalised parameters and specifying conversion to simulation-ready parameterisation as prerequisite.

## ISSUE #18
**Tag:** [L]
**Severity:** LOW
**Description:** The substantial financial and resource barrier created by the requirement for 200 Prolific Academic participants is not acknowledged as a limitation for replication.
**Status:** RESOLVED — Batch R3, 2026-03-30. Added §10.8 Replication Cost Barrier with cost estimates and guidance for researchers unable to meet $N_{\min}$.

## ISSUE #19
**Tag:** [L]
**Severity:** MEDIUM
**Description:** The lack of a formal computational method for calculating domain structural similarity and modal structural similarity is a major missing limitation.
**Status:** RESOLVED — Batch R3, 2026-03-30. Added §10.9 Structural Similarity Computation acknowledging missing computation methods for $\phi$ and $\omega$.

## ISSUE #20
**Tag:** [I]
**Severity:** LOW
**Description:** Explicitly labelling section headers with version layers makes the paper read as a sequential assembly of research phases rather than a unified theory.
**Status:** RESOLVED — Final Integration Sweep, 2026-03-30. §3/§4/§5/§6 headers softened; version labels removed; bridging sentences added at §3→§4 and §4→§5 transitions.

## ISSUE #21
**Tag:** [I]
**Severity:** MEDIUM
**Description:** The abstract is heavily weighted toward V1.0 mechanisms and fails to proportionately present the framework extensions as a synthesised whole.
**Status:** RESOLVED — Final Integration Sweep, 2026-03-30. Burnell framing changed to "formal correspondence"; §3 intro paragraph added; §4/§5/§6 headers softened with bridging sentences.

## ISSUE #24
**Tag:** [I]
**Severity:** MEDIUM
**Description:** Mapping V3.0+ variables directly to the Burnell et al. faculties appears post-hoc and opportunistic given the report's release date.
**Status:** RESOLVED — Final Integration Sweep, 2026-03-30. §1.2 Burnell framing changed from "addresses" to "demonstrates formal correspondence with"; §10.10 already acknowledges unvalidated report status and faculty mapping contingency.

## ISSUE #25
**Tag:** [L]
**Severity:** MEDIUM
**Description:** The framework cites the Burnell report as a foundational taxonomy without acknowledging its status as an unvalidated technical report released in March 2026.
**Status:** RESOLVED — Batch R3, 2026-03-30. Added §10.10 Burnell Report Status acknowledging unvalidated technical report status and contingency of faculty mapping.

## ISSUE #26
**Tag:** [L]
**Severity:** LOW
**Description:** The hyper-precise hackathon suitability percentages are provided without any disclosed methodology or statistical derivation.
**Status:** RESOLVED — Batch R3, 2026-03-30. Added §10.11 Hackathon Suitability Methodology acknowledging unsupported precision and advising qualitative treatment.

## ISSUE #27
**Tag:** [L]
**Severity:** LOW
**Description:** The claim of a 73.41% winning probability is entirely unsupported and lacks academic foundation.
**Status:** RESOLVED — Batch R3, 2026-03-30. Added §10.12 Winning Probability Claim acknowledging unsupported claim and recommending removal or qualitative replacement.

---

## POST-REVIEW INFRASTRUCTURE ISSUES (Resolved 2026-06-06)

Issues identified during daily workflow execution (see `docs/issue-compilation.md`), all resolved across Phases 1a, 1b, and 2.

### I-01 — Notebook hardcodes `/kaggle/working` path
**Tag:** [I] **Severity:** HIGH
**Status:** RESOLVED — 2026-06-06. Added Kaggle detection guard (`os.path.isdir('/kaggle')`) to both notebook Cells 0/1.

### I-02 — SCANDataset defined inline in notebook
**Tag:** [I] **Severity:** MEDIUM
**Status:** RESOLVED — 2026-06-06. Moved SCANDataset class from notebook Cell 3 to `code/sigma/utils/data.py`; notebook imports via `from sigma.utils.data import SCANDataset`.

### I-03 — DataLoader `num_workers` hardcoded to 2
**Tag:** [I] **Severity:** LOW
**Status:** RESOLVED — 2026-06-06. Dynamic `NUM_WORKERS = 0 if not torch.cuda.is_available() else min(2, os.cpu_count() or 1)`.

### I-04 / C-02 — Missing seaborn dependency
**Tag:** [I] **Severity:** LOW
**Status:** RESOLVED — 2026-06-06. Added `"seaborn>=0.13"` to `pyproject.toml` dependencies.

### T-01 — Publication monitor lacks HTTP retry
**Tag:** [T] **Severity:** MEDIUM
**Status:** RESOLVED — 2026-06-06. Added `_retry_urlopen()` with exponential backoff (3 attempts, 2s/4s/8s) in `scripts/monitor-pub.py`.

### T-02 — Keyword clusters too narrow
**Tag:** [T] **Severity:** LOW
**Status:** RESOLVED — 2026-06-06. Added 5 new keyword clusters (grokking_phase_transition, metacognition_AI, executive_function_AI, theory_of_mind_LM, agentic_evaluation) to `monitor-pub.py`.

### T-03 — No formal test suite
**Tag:** [T] **Severity:** MEDIUM
**Status:** RESOLVED — 2026-06-06. Created `tests/test_ode.py` (18 tests) and `tests/test_config.py` (13 tests). 31/31 pass.

### T-04 — No local smoke test
**Tag:** [T] **Severity:** MEDIUM
**Status:** RESOLVED — 2026-06-06. Created `scripts/smoke_test.py` — 0.5s execution, ALL CHECKS PASSED.

### P-01 — 5 new papers need CITE or ADDRESS
**Tag:** [R] **Severity:** MEDIUM
**Status:** RESOLVED — 2026-06-06. Redhardt (ADDRESS §2.2.1), TailLoR (CITE §3.3.4), Montanari & Wang (CITE §7), Grokking-as-Phase-Transition (CITE §7), E2H Reasoner (CITE §7). Reference entries added to §14.

### P-02 — gap_conflict_map.md needs refresh
**Tag:** [I] **Severity:** MEDIUM
**Status:** RESOLVED — 2026-06-06. Added Redhardt to Q1, TailLoR to Q4, new Q12 with 3 papers.
