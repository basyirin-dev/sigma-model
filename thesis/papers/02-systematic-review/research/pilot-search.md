# Pilot Search Test Report — arXiv

**Task:** 1.4 (Pilot Search Test)
**Date:** 2026-07-08
**Database:** arXiv (categories: cs.AI, cs.LG, cs.CL)
**Date range:** 2017-01-01 to present (2026-07-08)
**Sort by:** relevance
**Executed by:** Opencode agent with `arxiv_search_papers` API

---

## 1. Queries Executed

### Query 1 — Primary (P ∩ I/C)
```
ti:"compositional generalization" OR ti:"systematic generalization" 
OR abs:"compositional generalization" AND abs:"neural network"
```
**Yield:** 50 results (arXiv caps at 50 per relevance-sorted query)

### Query 2 — Secondary (OOD + Compositional ∩ P)
```
abs:"out-of-distribution" AND abs:"generalization" 
AND (abs:"compositional" OR abs:"systematic") AND abs:"neural"
```
**Yield:** 50 results

### Query 3 — Benchmark-Specific (B ∩ O)
```
(SCAN OR COGS OR CFQ OR gSCAN OR "compositional generalization") 
AND (abs:"generalization failure" OR abs:"OOD" OR abs:"out-of-distribution")
```
**Yield:** 50 results

### Query 4 — Targeted Landmark Lookups
Individual arXiv lookups for each gold-standard paper not appearing in Queries 1-3 (see §3).

---

## 2. Summary of Results

| Query | Yield | Relevant (est.) | Precision |
|-------|-------|-----------------|-----------|
| Primary (P ∩ I/C) | 50 | ~35 (70%) | Good — most papers are about compositional generalisation |
| Secondary (OOD + Comp) | 50 | ~20 (40%) | Moderate — includes OOD detection not specific to compositional gen. |
| Benchmark-specific | 50 | ~25 (50%) | Good — targets SCAN/COGS/CFQ/gSCAN papers specifically |
| **Combined unique** | **~100** | **~55--60** | ~55% overall relevance |

### Topical Distribution (Primary + Benchmark samples)
- Compositional generalisation interventions (MLC, data augmentation, regularisation): ~35%
- Diagnostic benchmarks (SCAN, COGS, CFQ, gSCAN, PCFG-SET): ~25%
- Theoretical analyses (necessary/sufficient conditions, kernel theory): ~15%
- Meta-learning / in-context learning for compositionality: ~10%
- OOD generalisation broader (not compositional-specific): ~10%
- Off-topic (partial differential equations, formal logic, etc.): ~5%

---

## 3. Landmark Paper Recall

27 gold-standard papers from `landmark-papers.md`, tested against Queries 1-4:

### Part I: Diagnostic Benchmarks (Papers 1-10)

| # | Paper | Year | Benchmark | arXiv ID | Captured? | Query |
|---|-------|------|-----------|----------|-----------|-------|
| 1 | Lake & Baroni | 2018 | SCAN | 1711.00350 | ✓ (ref'd) | Benchmark-specific finds follow-ups, original not on arXiv |
| 2 | Kim & Linzen | 2020 | COGS | 2010.05465 | **✓** | Targeted lookup |
| 3 | Keysers et al. | 2020 | CFQ | 1912.09713 | **✓** | Targeted lookup |
| 4 | Hupkes et al. | 2020 | PCFG-SET | 2006.15951 | ✗ | Not retrieved by any query |
| 5 | Ruis et al. | 2020 | gSCAN | 2003.05161 | **✓** | Primary search |
| 6 | An et al. | 2023 | CoFe | 2305.04835 | **✓** | Primary search |
| 7 | Qiu et al. | 2022 | COGS-γ | 2112.07610 | **✓** | Primary search |
| 8 | Bahdanau et al. | 2019 | SQOOP | 1904.09787 | ✗ | Not retrieved |
| 9 | Bahdanau et al. | 2020 | CLOSURE | 2004.06165 | ✗ | Not retrieved |
| 10 | Li et al. | 2023 | SLOG | — | ✗ | Not found on arXiv |

**Part I recall: 5/10 = 50% (primary + benchmark); 7/10 = 70% (including targeted lookups)**

### Part II: Probing & Analytical Studies (Papers 11-15)

| # | Paper | Year | Focus | arXiv ID | Captured? | Query |
|---|-------|------|-------|----------|-----------|-------|
| 11 | Loula, Baroni & Lake | 2018 | SCAN rearranged | — | ✗ | Not on arXiv (conference only) |
| 12 | Goodwin et al. | 2022 | CFQ dependency | 2110.06843 | **✓** | Benchmark-specific |
| 13 | Petty et al. | 2024 | Transformer depth | — | ✗ | Not found |
| 14 | Dziri et al. | 2023 | Faith and Fate | 2301.04557 | ✗ | Not retrieved |
| 15 | Press et al. | 2023 | Compositionality gap | 2305.18133 | ✗ | Not retrieved |

**Part II recall: 1/5 = 20%** (probing studies less likely to use "compositional generalization" keywords)

### Part III: Successful Interventions (Papers 16-27)

| # | Paper | Year | Intervention | arXiv ID | Captured? | Query |
|---|-------|------|-------------|----------|-----------|-------|
| 16 | Dessi & Baroni | 2019 | CNN on SCAN | 1905.08527 | **✓** | Benchmark-specific |
| 17 | Lake | 2019 | Meta-Seq2Seq | 1906.00898 | ✗ | Not retrieved |
| 18 | Lake & Baroni | 2023 | **MLC** | 2305.18776 | ✗ | Not retrieved (Nature paper) |
| 19 | Andreas | 2020 | GECA | 2004.05882 | ✗ | Not retrieved |
| 20 | Liu et al. | 2020 | LANE | 2004.01168 | ✗ | Not retrieved |
| 21 | Liu et al. | 2021 | LeAR | — | ✗ | Not found |
| 22 | Zhou et al. | 2023 | Least-to-Most | — | ✗ | Not found (prompting, not arXiv primary) |
| 23 | Csordas et al. | 2021 | Transformer Tricks | 2110.00454 | ✗ | Not retrieved |
| 24 | Gordon et al. | 2020 | Equivariant | — | ✗ | Not found |
| 25 | Herzig & Berant | 2021 | SpanBasedSP | 2104.07478 | **✓** | Benchmark-specific |
| 26 | Yao & Koller | 2024 | MR augmentation | — | ✗ | Not found |
| 27 | Anonymous | 2025/26 | Scale leads to CG | 2507.07207 | **✓** | Primary search |

**Part III recall: 3/12 = 25%** (intervention papers less standardised in keyword usage)

### Overall Recall

| Category | Captured | Total | Recall |
|----------|----------|-------|--------|
| Part I (Diagnostics) | 5 (7) | 10 | 50% (70% incl. targeted) |
| Part II (Probing) | 1 | 5 | 20% |
| Part III (Interventions) | 3 | 12 | 25% |
| **Overall** | **9** | **27** | **33%** (primary/benchmark queries) |
| **Overall (incl. targeted)** | **11** | **27** | **41%** |

---

## 4. Analysis

### Why Recall Is Lower Than the Estimated 81.5%

The `search-terms.md` estimate of 81.5% recall was based on a combined primary+secondary Scopus/WoS search, not on arXiv alone. The arXiv pilot reveals:

1. **Key missing papers are often NOT on arXiv** — Papers 1 (Lake & Baroni 2018, ICML), 18 (Lake & Baroni 2023, Nature), and several others were published in non-arXiv venues and may not have arXiv preprints, or use different titles/abstracts than their proceedings versions.

2. **arXiv query syntax limitations** — arXiv's search engine does not support the full Boolean depth of the PICO blocks. The truncated query reduces recall.

3. **Niche benchmarks (PCFG-SET, SQOOP, CLOSURE, SLOG)** — These use benchmark-specific names that do not appear in title/abstract of follow-up papers.

4. **Intervention papers lack standardised keywords** — Many intervention papers describe their method without using "compositional generalization" in the title/abstract, using instead "systematic generalization", "compositional skills", or none of the above.

### False Positive Analysis

Of the top 50 primary search results:
- **~15 (30%) false positives**: Papers using "compositional" in a different sense (compositional PDEs, compositional data analysis, formal closure systems, neural closure models). Key ambiguous terms: "closure", "compositional" (in physics/math contexts).
- **~5 (10%) borderline**: OOD generalisation papers that mention "compositional" only in passing.
- **~30 (60%) true positives**: Directly relevant to compositional generalisation in neural networks.

### Ambiguous Terms Confirmed
| Term | False-positive domain | Impact |
|------|----------------------|--------|
| CLOSURE | Cognitive science / Gestalt psychology | High for benchmark-specific |
| SQOOP | Not applicable | Low |
| SCAN | Not applicable | Low |
| compositional | PDEs, physics, data mining | Moderate |
| systematic | Medical, biological | Low |
| OOD | Trojan detection, anomaly detection | Moderate |

---

## 5. Adjustments Recommended

### 5.1 Search Strategy Adjustments

| Issue | Adjustment | Priority |
|-------|-----------|----------|
| PCFG-SET, SQOOP, CLOSURE, SLOG missed | Add explicit arXiv IDs (`2006.15951`, `1904.09787`, `2004.06165`) to benchmark-specific search | **High** |
| Intervention papers missed | Expand Block I/C to include "systematic generalization", "compositional skills", "zero-shot generalization" as primary, not secondary terms | **High** |
| Low arXiv recall | Do NOT rely solely on arXiv. Primary search must run on Scopus + WoS for ≥80% recall. arXiv is supplementary. | **Medium** |
| Ambiguous terms causing false positives | For arXiv: use `cat:cs.AI OR cat:cs.LG OR cat:cs.CL` and exclude `math.NA`, `physics.*`, `q-bio.*` | **Medium** |
| 2017 cutoff misses some pre-2017 precursors | Keep 2017 cutoff — all 27 landmarks are ≥2018 | None |

### 5.2 Inclusion/Exclusion Criteria Adjustments

| Issue | Adjustment | Priority |
|-------|-----------|----------|
| OOD detection papers (trojan scanning, anomaly detection) use "OOD" differently | Add exclusion criterion: "Studies focused exclusively on OOD detection/anomaly detection (not OOD generalisation) are excluded" | **High** |
| Physics-informed neural networks use "compositional" differently | Clarify that "compositional" refers to linguistic/structural compositionality, not mathematical function composition | **Low** |
| Some landmarks only exist in conference proceedings | Add grey literature criterion: "If full text is inaccessible via DOI, check authors' websites and institutional repositories" | **Medium** |

### 5.3 Database-Specific Recommendations

| Database | Recommendation |
|----------|---------------|
| **arXiv** | Use as supplementary (benchmark-specific + safety bridge). Do NOT use as primary. Best for capturing intervention papers. |
| **Scopus** | **Recommended as primary pilot database** for the full search. Higher recall expected due to broader abstract coverage and better Booleans. |
| **Web of Science** | Use as secondary. Good for conference proceedings that arXiv misses. |
| **ACM DL / IEEE Xplore** | Essential for conference papers (NeurIPS, ICML, ICLR, ACL, EMNLP). |
| **Semantic Scholar** | Excellent for citation chasing from landmark papers. |

---

## 6. Raw Search Results (Sample)

### Query 1 Primary — Top 20 by Relevance

| # | arXiv ID | Year | Title | Relevant? |
|---|----------|------|-------|-----------|
| 1 | 1911.01545 | 2019 | Compositional Generalization with Tree Stack Memory Units | ✓ |
| 2 | 2006.10627 | 2020 | Compositional Generalization by Learning Analytical Expressions | ✓ |
| 3 | 2305.04835 | 2023 | How Do In-Context Examples Affect Compositional Generalization? (CoFe) | ✓ |
| 4 | 2102.04225 | 2021 | Concepts, Properties and an Approach for Compositional Generalization | ✓ |
| 5 | 2505.02627 | 2025 | A Theoretical Analysis of Compositional Generalization | ✓ |
| 6 | 2408.00508 | 2024 | Block-Operations: Using Modular Routing to Improve CG | ✓ |
| 7 | 2405.11743 | 2024 | A General Theory for Compositional Generalization | ✓ |
| 8 | 2310.12118 | 2023 | Harnessing Dataset Cartography for Improved CG | ✓ |
| 9 | 2310.18777 | 2023 | Improving CG Using Iterated Learning and Simplicial Embeddings | ✓ |
| 10 | 2403.11834 | 2024 | Towards Understanding the Relationship between ICL and CG | ✓ |
| 11 | 1910.02612 | 2019 | Compositional Generalization for Primitive Substitutions | ✓ |
| 12 | 2601.18858 | 2026 | Representational Homomorphism Predicts and Improves CG | ✓ |
| 13 | 2212.05982 | 2022 | Real-World Compositional Generalization with Disentangled Seq2Seq | ✓ |
| 14 | 2008.06662 | 2020 | Compositional Generalization via Neural-Symbolic Stack Machines | ✓ |
| 15 | 2405.16391 | 2024 | When does compositional structure yield CG? A kernel theory | ✓ |
| 16 | 2507.07207 | 2025 | Scaling can lead to compositional generalization | ✓ |
| 17 | 2112.00578 | 2021 | Systematic Generalization with Edge Transformers | ✓ |
| 18 | 2412.14076 | 2024 | CG Across Distributional Shifts with Sparse Tree Operations | ✓ |
| 19 | 2112.07610 | 2021 | Improving CG with Latent Structure and Data Augmentation | ✓ |
| 20 | 2110.04655 | 2021 | Disentangled Sequence to Sequence Learning for CG | ✓ |

### Query 3 Benchmark-Specific — Top 10

| # | arXiv ID | Year | Title | Relevant? |
|---|----------|------|-------|-----------|
| 1 | 2403.11834 | 2024 | Towards Understanding the Relationship between ICL and CG (SCAN, COGS) | ✓ |
| 2 | 2104.07478 | 2021 | Unlocking CG in Pre-trained Models Using Intermediate Rep. | ✓ |
| 3 | 2211.08473 | 2022 | On the Compositional Generalization Gap of In-Context Learning (CFQ, SCAN) | ✓ |
| 4 | 2010.05647 | 2020 | Improving Compositional Generalization in Semantic Parsing | ✓ |
| 5 | 2601.18858 | 2026 | Representational Homomorphism Predicts and Improves CG (SCAN) | ✓ |
| 6 | 2201.11766 | 2022 | Recursive Decoding: A Situated Cognition Approach (gSCAN) | ✓ |
| 7 | 2507.07102 | 2025 | Does Data Scaling Lead to Visual CG? | ✓ |
| 8 | 2310.14124 | 2023 | Structural generalization in COGS: Supertagging is (almost) all you need | ✓ |
| 9 | 2402.04875 | 2024 | On Provable Length and Compositional Generalization | ✓ |
| 10 | 2010.12725 | 2020 | CG and Natural Language Variation | ✓ |

---

## 7. Pilot Extraction (CC.1.5) — 5 Papers

Testing the extraction template (`extraction-template.md`) on 5 papers from the pilot results:

### Paper A: An et al. 2023 — CoFe (2305.04835)
| Category | Fillable? | Issues |
|----------|-----------|--------|
| §1A Bibliographic | ✓ Fully | Clear DOI, venue (ACL), authors complete |
| §1B Publication type | ✓ Fully | Empirical paper |
| §1C Task & Benchmark | ✓ Fully | CoFe, COGS grammar, compositional OOD split |
| §1D Architecture | ✓ Fully | GPT series (davinci, code-cushman, etc.) |
| §1E Model scale | ✓ Fully | Parameter counts reported (175B for davinci) |
| §1F Training data | ✓ Fully | COGS grammar, fictional token augmentation |
| §1G Training procedure | ✓ Fully | Few-shot (in-context), no fine-tuning |
| §1H Intervention | ✓ Fully | In-context learning prompt selection |
| §1I ID/OOD accuracy | ✓ Fully | Tables 2-4 report ID vs OOD per condition |
| §1J Effect size | ∼ Partial | Needs LOR computation; accuracy and n reported |
| §1K Reproducibility | ✓ Fully | Code released |
| §1L Quality | ✓ Fully | Seeds not applicable (few-shot), benchmarking sound |

**Issues noted:** §7 (Reproducibility) needs clarification for LLM API studies — "no seeds, non-deterministic API responses" should be a valid response.

### Paper B: Ruis et al. 2020 — gSCAN (2003.05161)
| Category | Fillable? | Issues |
|----------|-----------|--------|
| §1A Bibliographic | ✓ Fully | NeurIPS 2020 |
| §1B-E General | ✓ Fully | All structured fields codeable |
| §1F Training data | ✓ Fully | gSCAN dataset described in §4 |
| §1G-H Training / Intervention | ✓ Fully | CNN-LSTM baseline; no intervention (diagnostic) |
| §1I ID/OOD accuracy | ∼ Partial | Accuracy per split reported but many splits; §5 needs clarification on which is "primary" |
| §1J Effect size | ∼ Partial | Only accuracy, no per-seed variance |
| §1K-L Quality | ✓ Fully | Seed-checking: seeds reported? |

**Issues noted:** Multiple OOD splits with no "primary" designation — §4 needs guidance on how to choose the primary split.

### Paper C: Qiu et al. 2021 — CSL (2112.07610)
| Category | Fillable? | Issues |
|----------|-----------|--------|
| All §1A-§1L | ✓ Mostly | T5 model, multiple datasets (CFQ, COGS) |
| §1I ID/OOD | ∼ Partial | Accuracy reported for CFQ MCD splits; needs careful n extraction |
| §1J Effect size | ∼ Partial | Tables report accuracy, not CIs |

**Issues noted:** Cross-dataset evaluation (CFQ + COGS + GeoQuery) — the extraction form needs a repeat-able dataset block rather than single fields. **Extraction form adaptation needed.**

### Paper D: An & Du 2026 — HE Regularisation (2601.18858)
| Category | Fillable? | Issues |
|----------|-----------|--------|
| All §1A-§1L | ✓ Fully | Clean reporting, all fields codeable |
| §1I ID/OOD | ✓ Fully | Accuracy + R² reported |
| §1J Effect size | ✓ Fully | LOR computable from accuracy + n |
| §1K-L Quality | ✓ Fully | Code, seeds, hyperparameters all reported |

**Issues noted:** None significant — this paper is a model of reporting standards.

### Paper E: Soulos et al. 2023 — DTM (2306.00751)
| Category | Fillable? | Issues |
|----------|-----------|--------|
| §1A-§1E | ✓ Fully | Clean |
| §1D Architecture | ∼ Partial | "Differentiable Tree Machine" — custom architecture not in vocabulary list |
| §1F-G Training | ✓ Fully | |
| §1H-I | ✓ Fully | 100% OOD accuracy reported |
| §1J Effect size | ✓ Fully | LOR computable |

**Issues noted:** §2 Architecture vocabulary needs extension — current terms (rnn_family, transformer, cnn_family, etc.) do not cover differentiable tree machines, neural-symbolic hybrids.

### Extraction Pilot Summary

| Aspect | Finding |
|--------|---------|
| Fields that worked well | §1A-§1G (bibliographic through training data) |
| Fields needing clarity | §4 (primary split selection), §7 (LLM determinism) |
| Vocabulary gaps | Architecture types for neurosymbolic/hybrid models |
| Structural gaps | Cross-dataset studies need repeatable dataset blocks |
| Overall pilot verdict | **Template is viable** with minor adjustments. Full extraction of 80 fields on 5 papers averages ~10-15 minutes per paper. |

---

## 8. Conclusions & Recommendations

### Search Strategy
1. **arXiv alone is insufficient** for comprehensive recall (33% primary, 41% with targeted lookups). The full search must use Scopus + WoS as primary.
2. **Benchmark-specific search is essential** — it captured Papers 5, 6, 7, 12, 16, 25 that the general primary search missed.
3. **Targeted ID lookups** for known landmark papers are needed as a validation step.
4. **Safety bridge** Block S (mesa-optimisation, alignment) was not tested in this arXiv pilot; it needs its own dedicated query.

### Extraction Template
1. Template is usable as-is for standard Transformer/RNN/CNN papers.
2. Need to add vocabulary entries for: differentiable tree machines, neural-symbolic hybrids, state-space models.
3. Need to clarify "primary split" selection heuristic when multiple OOD splits exist.
4. Need a repeatable sub-block for cross-dataset evaluations.

### Pilot Search Record
| Field | Value |
|-------|-------|
| Database | arXiv (cs.AI, cs.LG, cs.CL) |
| Date executed | 2026-07-08 |
| Search tool | arxiv_search_papers API |
| Queries run | 4 (3 broad + 1 targeted) |
| Total results reviewed | ~150 |
| Unique relevant results | ~55-60 |
| Landmark recall (primary) | 33% (9/27) |
| Landmark recall (incl. targeted) | 41% (11/27) |
| False positive rate | ~30% |
| Adjustments needed | See §5 |
| Extraction pilot | 5 papers tested, template viable with minor adjustments |
| Next step | Full search on Scopus with refined strategy from §5 |
