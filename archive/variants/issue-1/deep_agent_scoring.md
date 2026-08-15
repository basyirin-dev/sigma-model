# DEEP AGENT SCORING — ISSUE #1

**Issue:** The primary definition of schema coherence relies on rhetorical cognitive psychology vocabulary rather than rigorous mathematical grounding.

---

## VARIANT A — MDL compression ratio definition

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 8 | MDL ratio is compatible with existing ODE (Eq 28) because it defines σ_A at a point in time, not its dynamics. However, introduces new quantities (L_struct, L_surface) not used elsewhere in the ODE system, creating a slight formal disconnect between definition and dynamics. |
| C2 — Novelty Defence | 9 | Compression-based framing sharply distinguishes σ_A from Structured/Disentangled/Causal representations (none have MDL-based definitions). Also cleanly separates σ_A from Cognitive Schema. |
| C3 — Falsifiability | 6 | MDL definition is theoretically grounded but doesn't directly connect to measurable proxies. Improves falsifiability indirectly by providing a more precise definition, but doesn't add observable test conditions. |
| C4 — Scope Discipline | 10 | Single-agent boundary maintained (MDL is per-agent). Cognitive bridge boundary maintained (no psychological language). Version boundary maintained (V1.0 only). |
| C5 — Hackathon Relevance | 3 | Tangentially related; doesn't directly improve any hackathon track protocol. |
| C6 — Version Integration | 5 | Version-neutral; doesn't improve or worsen cross-version integration. |
| **Composite** | **6.83** | |

---

## VARIANT B — Replace "Cognitive Schema" in uniqueness table

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 9 | No equations changed; purely a table column replacement. Full ODE system coherence maintained. |
| C2 — Novelty Defence | 8 | Removing "Cognitive Schema" eliminates the primary conflation risk. "Compressed Residual Code" is a well-defined MDL term that σ_A is clearly distinct from. |
| C3 — Falsifiability | 4 | Minimal impact on falsifiability. The table is explanatory, not predictive. |
| C4 — Scope Discipline | 10 | Single-agent boundary maintained. Cognitive bridge boundary maintained (removes psychological vocabulary). Version boundary maintained. |
| C5 — Hackathon Relevance | 1 | No hackathon relevance; purely a definitional cleanup. |
| C6 — Version Integration | 5 | Version-neutral. |
| **Composite** | **6.17** | |

---

## VARIANT C — Systemic reframe (Abstract + §1.1 + §3.1.3)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 9 | No equations changed; only prose replaced. Full ODE system coherence maintained. |
| C2 — Novelty Defence | 9 | "Compression by exploiting generative structure" is a sharper framing than "restructured around deep governing principles." Actively distinguishes σ_A from all adjacent constructs by grounding it in information theory. |
| C3 — Falsifiability | 7 | "Generative structure" is more testable than "governing principles" because it refers to a formal property (the generating distribution) that can be operationalised through OOD benchmarks. Doesn't add new predictions but makes existing ones more precise. |
| C4 — Scope Discipline | 10 | Single-agent boundary maintained. Cognitive bridge boundary maintained (removes psychological vocabulary from three key locations). Version boundary maintained. |
| C5 — Hackathon Relevance | 3 | Tangentially related; cleaner framing helps benchmark design but doesn't directly improve protocols. |
| C6 — Version Integration | 6 | Slightly improves integration by making the abstract frame consistent with V1.0 through V3.0+ terminology. |
| **Composite** | **7.33** | |

---

## VARIANT D — Axiomatized definition (3 axioms in §3.1.3)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 8 | Axioms define σ_A at a point in time; ODE specifies temporal evolution. Complementary. However, Axiom 1 introduces max_f OOD(f) which is not directly used in the ODE, creating a slight formal disconnect. |
| C2 — Novelty Defence | 10 | Strongest possible differentiation: σ_A is defined by an explicit formula involving OOD accuracy, which no adjacent construct has. Actively sharpens the boundary. |
| C3 — Falsifiability | 9 | Axiom 1 directly connects σ_A to OOD accuracy, making Predictions 1, 2, and 8 more testable by grounding the variable in observable quantities. |
| C4 — Scope Discipline | 10 | Single-agent boundary maintained. Cognitive bridge boundary maintained (no psychological language). Version boundary maintained. |
| C5 — Hackathon Relevance | 6 | Axiomatization improves Learning track benchmark design by providing a formal definition that benchmark protocols can target directly. |
| C6 — Version Integration | 7 | Grounds V1.0 σ_A in the same measurement framework used by V2.0/V3.0+ (SGG proxy), improving integration. |
| **Composite** | **8.33** | |

---

## VARIANT E — Proxy identification (SGG) in §3.1.3

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 9 | Proxy equation (3b) is a normalisation of SGG already defined in the paper. No new quantities introduced. Full ODE coherence maintained. |
| C2 — Novelty Defence | 8 | Anchoring σ_A to the SGG proxy sharpens its distinction from adjacent constructs by connecting it to a measurable quantity. Slightly weaker than Variant D because it retains the rhetorical prose definition. |
| C3 — Falsifiability | 10 | Directly connects σ_A to Acc_OOD/Acc_In, making all eight §9 predictions more testable. The proxy identification is the strongest falsifiability improvement of all variants. |
| C4 — Scope Discipline | 10 | Single-agent boundary maintained. Cognitive bridge boundary maintained. Version boundary maintained. |
| C5 — Hackathon Relevance | 8 | Proxy identification directly enables Learning track benchmark protocols by providing the exact formula for computing σ_A from benchmark results. Improves existing SCAN/COGS/PCFG-SET protocols. |
| C6 — Version Integration | 9 | Integrates the §3.1.3 definition with the §8/Appendix A.4 measurement protocol, closing a version seam between V1.0 core and V3.0+ benchmark validity. |
| **Composite** | **9.00** | |

---

## RANKING

| Rank | Variant | Composite | Flags |
|------|---------|-----------|-------|
| 1 | **E** | **9.00** | [HACKATHON PRIORITY] [INTEGRATION PRIORITY] |
| 2 | **D** | **8.33** | — |
| 3 | **C** | **7.33** | — |
| 4 | **A** | **6.83** | — |
| 5 | **B** | **6.17** | — |

All variants scored ≥ 6.0. No variants suppressed.

---

## TOP 2 VARIANTS — FULL SCORING BREAKDOWN

### 🥇 VARIANT E (Composite: 9.00) — [HACKATHON PRIORITY] [INTEGRATION PRIORITY]

**Section targeted:** §3.1.3
**Scope:** Structural equation fix
**Mechanism:** Integrate the existing SGG proxy identification (Eq. 3b) into the primary definition, adding a formal proxy equation and updating the prose definition to reference it.

| Criterion | Score |
|-----------|-------|
| C1 — ODE System Coherence | 9 |
| C2 — Novelty Defence | 8 |
| C3 — Falsifiability | 10 |
| C4 — Scope Discipline | 10 |
| C5 — Hackathon Relevance | 8 |
| C6 — Version Integration | 9 |

**Why this variant leads:** It closes the definitional gap by connecting the primary definition to the measurement protocol that already exists in the paper. The proxy equation (σ_A = Acc_OOD / Acc_In) makes σ_A directly computable from benchmark results, which simultaneously improves falsifiability (C3=10), enables hackathon protocols (C5=8), and closes the version seam between V1.0 core definition and V3.0+ benchmark validity (C6=9).

---

### 🥈 VARIANT D (Composite: 8.33)

**Section targeted:** §3.1.3
**Scope:** Structural equation fix
**Mechanism:** Add a three-axiom formalization grounded in OOD accuracy (Axiom 1: representation fidelity formula; Axiom 2: monotonicity; Axiom 3: boundary conditions).

| Criterion | Score |
|-----------|-------|
| C1 — ODE System Coherence | 8 |
| C2 — Novelty Defence | 10 |
| C3 — Falsifiability | 9 |
| C4 — Scope Discipline | 10 |
| C5 — Hackathon Relevance | 6 |
| C6 — Version Integration | 7 |

**Why this variant is strong:** It provides the strongest novelty defence (C2=10) by defining σ_A through an explicit axiomatization that no adjacent construct has. However, it scores lower than Variant E on hackathon relevance (6 vs 8) and version integration (7 vs 9) because the axiomatic formulation introduces new quantities (max_f OOD(f)) that are not directly used in the existing ODE system or benchmark protocols.

---

## HACKATHON UPDATE:

**Variant E:** The proxy identification (σ_A = Acc_OOD / Acc_In) directly enables Learning track benchmark protocols. Specifically:
- `/hackathon/track_learning.md` should be updated to reference Equation 3b as the primary operationalisation of σ_A for benchmark scoring, replacing any indirect proxies currently used.

**Variant D:** The axiomatization improves the theoretical grounding of the Learning track but doesn't require direct protocol changes. No hackathon update needed.

---

## INTEGRATION UPDATE:

**Variant E:** Update `integration_map.md` to add a row:
- Row: "§3.1.3 Definition ↔ §8 Protocol" → Status: CLOSED (proxy identification Eq. 3b integrates definition and measurement)

**Variant D:** Update `integration_map.md` to add a row:
- Row: "§3.1.3 Definition ↔ SGG Proxy" → Status: PARTIAL (axiomatization references OOD accuracy but doesn't explicitly integrate the proxy equation)

---

## NEGATIVE LOG:

- **Issue #1, Variant B:** Purely cosmetic table-column replacement; minimal mathematical grounding (C1=9, C3=4); no hackathon or integration impact. Patch rather than principled fix.
- **Issue #1, Variant A:** MDL compression ratio introduces new unlinked quantities (L_struct, L_surface); no proxy connection; no hackathon relevance. Theoretically clean but operationally disconnected.
- **Issue #1, Variant C:** Systemic reframe is broad but shallow; improves prose framing without adding mathematical grounding (no new equations). Good scope discipline but limited falsifiability improvement.

---

## CHECKPOINT RECOMMENDATION:

Not yet at Checkpoint threshold. Edit count: 0 approved edits.
