# Pilot Search Results — Paper 01 Scoping Review

**Date**: 2026-07-04
**Executor**: Automated pilot (arXiv API + OpenAlex API)
**Purpose**: Calibrate search sensitivity/specificity before Phase 2 formal execution

---

## 1. Database Coverage

### 1.1 arXiv (CS.AI, CS.LG, CS.CL, stat.ML)

| Query | Papers Retrieved | Relevant to AGI Safety | Notes |
|-------|-----------------|------------------------|-------|
| `"AI alignment" AND "generalization"` | ~30 | ~5-8 | Many results use "alignment" in RLHF/multimodal sense, not AGI safety |
| `"compositional generalization" AND ("alignment" OR "safety")` | 20 | 2-3 | Most CG papers use "alignment" for text-image feature alignment; AGI safety intersection is sparse |
| `"goal misgeneralization"` | Smaller set | Good | Langosco et al. and follow-ups present |

**Yield assessment**: F2 estimate was 80-150. The "AI alignment" AND "generalization" query retrieved ~30, but specificity is low — most results are about applied alignment (RLHF, multimodal) rather than structural AGI safety. For F2 to reach its 80-150 estimate, the broad safety block (`"AI alignment" OR "AGI safety" OR "mesa-optimization"...`) must use the wider union.

### 1.2 OpenAlex (Peer-Reviewed + Preprint Index)

| Query | Papers Retrieved | Relevant to AGI Safety | Notes |
|-------|-----------------|------------------------|-------|
| `"deceptive alignment" OR "inner alignment" OR "mesa-optimization"` | 20 | 15-18 | High precision. Includes Hubinger (2019), Carlsmith (2023), recent alignment faking work |
| `"compositional generalization" AND "AI safety"` | 20 | 2-3 | Near-zero intersection outside explicit CG-safety bridge papers |
| `"goal misgeneralization"` | 10 (smart search) | 5-7 | Good recall; includes RLHF-based mitigation approaches |
| `"schema coherence" neural network OR alignment OR safety` | 10 | 0 | **Zero relevant results.** Confirms "near-zero yield" prediction |

**Yield assessment**: OpenAlex performs well for the AGI safety terms (deceptive alignment, mesa-opt, etc.) but the CG × safety intersection is extremely thin in both peer-reviewed and preprint indexes.

---

## 2. Sensitivity Check: Known Key Papers

| Key Paper | Retrieval Status | Source |
|-----------|-----------------|--------|
| Hubinger et al. (2019) — "Risks from Learned Optimization" | ✅ Found | OpenAlex (deceptive alignment query) |
| Langosco et al. (2022) — "Goal Misgeneralization in Deep RL" | ✅ Found | OpenAlex (goal misgeneralization smart search) |
| Carlsmith (2023) — "Scheming AIs" | ✅ Found | OpenAlex (deceptive alignment query) |
| Pepin Lehalleur et al. (2025) — "You Are What You Eat" | ✅ Found | arXiv ("AI alignment" AND "generalization") |
| Wang & Murfet (2026) — "Patterning" | ❌ Not found | Requires citation chaining from anchor papers (gap-analysis.md G3 target) |
| Greenblatt et al. (2024) — "Alignment Faking" | ✅ Found (via related work) | OpenAlex (alignment faking variants) |
| Shen et al. (2024) — "Towards Bidirectional Human-AI Alignment" | ✅ Found | arXiv + OpenAlex |
| Siddiqui et al. (2026) — "Capability Control Should Be Separate Goal" | ✅ Found | arXiv ("compositional generalization" AND "alignment") |

**Recall rate**: ~7/8 known key papers retrieved via primary search. Wang & Murfet (2026) requires citation chaining as anticipated.

---

## 3. Specificity Assessment

### Relevant (AGI safety) results from OpenAlex queries:
- Hubinger (2019) — Risks from Learned Optimization (mesa-opt framework)
- Carlsmith (2023) — Scheming AIs (deceptive alignment analysis)
- Arfeen (2026) — Detecting Performed Alignment (alignment faking detection)
- von Oswald et al. (2023) — Uncovering mesa-optimization in Transformers
- Koorndijk (2025) — Empirical Evidence for Alignment Faking
- Shen et al. (2023) — Large Language Model Alignment: A Survey
- Bereska & Gavves (2023) — Taming Simulators

### False positives from arXiv queries:
- Many CV/NLP CG papers using "alignment" for feature/attention alignment
- Medical imaging fairness papers using "alignment" for demographic parity
- Text-to-image generation papers (image-text alignment)

### Conclusion: Specificity is acceptable for F2/F3 queries but degraded for any query without the AGI safety anchor terms. The F1 (safety block only) would produce ~80% false positives from non-AGI-safety "alignment" usage.

---

## 4. Adjustments Recommended

### 4.1 Search String Adjustments

| Issue | Proposed Adjustment |
|-------|-------------------|
| "alignment" alone in CG query captures too many multimodal/feature-alignment papers | When used in CG queries, pair with explicit AGI safety qualifiers (e.g., NOT "text-image") |
| arXiv F2 under-specified for CG safety | Add "goal misgeneralization" and "specification gaming" to the safety block for better CG-safety sensitivity |
| "schema coherence" exact phrase yields zero | Confirms plan: use proximity patterns (W/5, NEAR) and citation chaining, not exact phrase |

### 4.2 I/E Criteria Adjustments

| Issue | Proposed Adjustment |
|-------|-------------------|
| Papers using "alignment" in multimodal/CV sense are false positives for I3 | I3 criterion already requires explicit AGI safety subdomain — no change needed, screening will handle this |
| CG papers without safety framing are correctly excluded by I5 | I5 (structural AGI safety relevance) already handles this — confirm it's sufficient |

**No changes to I/E criteria needed** — the existing criteria already exclude the false positive types observed.

### 4.3 Yield Estimate Recalibration

| Query | Previous Estimate | Pilot Observation | Revised Estimate |
|-------|-----------------|-------------------|-----------------|
| arXiv F2 (safety ∩ generalisation) | 80-150 | ~30-50 (with filter); ~80-120 (without) | 60-100 (peer-reviewed DBs); 100-180 (arXiv) |
| OpenAlex F2 | 30-80 | ~15-25 (safety-only); ~5-10 (intersection) | 20-40 |
| F3 (narrow ∩ structure) | 5-20 | ~2-5 (direct); plus citation-chaining supplement | 5-15 |

---

## 5. Extraction Template Pilot

### 5.1 Test Papers Selected

| # | Paper | Reason for Selection |
|---|-------|---------------------|
| P1 | Hubinger et al. (2019) — "Risks from Learned Optimization" | Foundational paper; tests all template sections |
| P2 | Pepin Lehalleur et al. (2025) — "You Are What You Eat" | Directly relevant to schema coherence thesis |
| P3 | Siddiqui et al. (2026) — "Capability Control Should Be Separate Goal" | Tests CG-alignment bridge classification |

### 5.2 Extraction Notes

**P1: Hubinger et al. (2019)**
- **Paper type**: Theoretical + Position
- **Subdomains**: Mesa-optimisation (primary), Deceptive Alignment, Inner Alignment
- **Framework**: Optimisation theory, RL theory
- **Evidence**: Formal argument, thought experiment
- **Template adequacy**: Excellent fit. All Phase 1 fields (A, B, C, E, H) populated fully. Section G (schema coherence) correctly flags `discusses_internal_structure: Yes` but `discusses_schema_coherence: No`. No issues found.

**P2: Pepin Lehalleur et al. (2025)**
- **Paper type**: Position
- **Subdomains**: Schema Coherence (bridging concept), Internal Representation Structure, AI Alignment
- **Framework**: Statistical learning theory, dynamical systems implicit
- **Evidence**: Informal argument, thought experiment
- **Template adequacy**: Good fit. The "bridging concepts" vocabulary in Level 5 correctly captures this paper. `relation_to_thesis: Directly supports`. Section G captures the key content. Suggestion: add "developmental interpretability" to the controlled vocabulary.

**P3: Siddiqui et al. (2026)**
- **Paper type**: Position
- **Subdomains**: AI Alignment (general), Robustness
- **Framework**: None (argumentative)
- **Evidence**: Informal argument
- **Template adequacy**: Mostly adequate. The paper discusses CG as an "open challenge" within safety but does not deeply engage internal structure. `relation_to_thesis: Indirectly supports`. Section G note: `structure_safety_link: Implicit`.

### 5.3 Template Adjustment Recommendations

| Field | Issue | Recommendation |
|-------|-------|---------------|
| Section C subdomains | "Developmental interpretability" missing from vocabulary | Add to Level 3 (Diagnostic) or Level 5 (Bridging Concepts) |
| Section G `structure_safety_link` | "Implicit" is too coarse for CG papers | Add "Explicit (CG-safety)" and "Explicit (structure-safety)" sub-options |
| Section J `relevance_to_review` | No guidance on when "High" applies | Add rule: "High = discusses both CG/schema AND safety in the same paper" |

---

## 6. Decision Log

| Decision | Rationale |
|----------|-----------|
| **No I/E criteria changes needed** | Existing criteria correctly handle false positive types observed |
| **F2 search confirmed as primary extraction query** | Good balance; false positive rate manageable through screening |
| **F3 narrow query remains secondary supplement** | Too few direct hits; citation chaining from anchor papers essential |
| **Extraction template validated with minor adjustments** | 3 additions: developmental interpretability, CG-safety sub-option, relevance rules |
| **"schema coherence" exact phrase → proximity/citation only** | Zero-yield confirmed in OpenAlex; plan remains correct |
| **OpenAlex confirmed as free Scopus substitute** | Good coverage; includes both peer-reviewed and preprint content |

---

## 7. Next Steps

1. Apply extraction template adjustments (add developmental interpretability, refine G/J fields)
2. Proceed to Phase 2 (Search Strategy Design) — F2 queries across all 6 databases
3. Citation chain from Pepin Lehalleur (2025), Wang & Murfet (2026), Hubinger (2019)
4. Grey literature manual sweep (LessWrong, Alignment Forum, AISI, Timaeus)
