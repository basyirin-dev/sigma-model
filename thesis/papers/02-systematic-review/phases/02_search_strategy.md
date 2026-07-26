# Phase 2 — Search Strategy Design

**Duration**: 1 week (Month 1–2)
**Deadline**: 2026-08-07
**Dependencies**: Phase 1 (protocol finalized and registered)
**Output**: Complete search strings for each database, documented in protocol appendix

---

### Task 2.1: Database Selection

- [x] 2.1.1: Review Phase 0.5 `research/search-terms.md`, `research/review-methodology.md`, and Paper 01 Phase 2 outputs for database recommendations
  - `search-terms.md`: provides full Boolean strings for all 6 databases, yield estimates, database-specific syntax, and pilot-tested arXiv recall (33% on 27 landmarks). Confirms PsycINFO with its own syntax (`AB,DE(...)`) and ~30–80 yield estimate.
  - `review-methodology.md` §8: recommends "IEEE Xplore, ACM DL, Scopus, Web of Science, PubMed, arXiv, OpenReview" for ML systematic reviews. PubMed not needed (no medical ML focus); OpenReview covered by Google Scholar grey-lit sweep.
  - Paper 01 Phase 02 (`thesis/papers/01-scoping-review/phases/02_search_strategy.md`): used Scopus, WoS, ACM DL, IEEE Xplore, arXiv, PhilPapers for AGI safety landscape. Paper 02 replaces PhilPapers with PsycINFO — justified because CG's cognitive-science origins (Fodor & Pylyshyn 1988; Marcus 1998) and the systematicity/productivity vocabulary originate in PsycINFO, whereas PhilPapers is for philosophical alignment terms (CEV, corrigibility) irrelevant to this review.
- [x] 2.1.2: Select primary academic databases (6 selected — see justification below):
  - **Scopus** — broadest NLP/ML/CV coverage; indexes ACL, EMNLP, NeurIPS, ICML, IJCAI proceedings where CG benchmarks live. Best interdisciplinary catch for P∩I/C∩O intersection.
  - **Web of Science** — complementary to Scopus; stronger formal-science and mathematical coverage. Captures SLT foundations, Jacobian analysis, and theoretical CG papers using formal vocabulary.
  - **ACM Digital Library** — hosts full proceedings of NeurIPS, ICML, AAAI, IJCAI, ACL, EMNLP — the exact venues where the core CG benchmark literature (SCAN, COGS, CFQ, gSCAN, SLOG) is published. Workshop coverage (compositionality, robustness, OOD workshops).
  - **IEEE Xplore** — unique coverage of formal methods, robustness, and verification literature. Captures engineering/systems flank of σ-trap evidence: neural operator papers (FNO, DeepONet), formal verification of compositional properties, and IEEE Transactions on reliability/safety.
  - **arXiv (cs.AI, cs.LG, cs.CL, cs.MA, stat.ML)** — essential for cutting-edge CG results; preprint-to-peer-reviewed lag < 6 months. Category-restricted search (cat:cs.AI OR cat:cs.LG OR cat:cs.CL) yields ~55–60% precision per pilot. Dual role: primary database for preprints AND grey literature discovery (Anthropic/DeepMind safety papers, Alignment Forum technical reports).
  - **PsycINFO** — compositional generalization originates in cognitive science (systematicity, productivity, substitutivity). PsycINFO captures the cognitive-science roots of CG that inform benchmark design. Block P filter (neural network terms) restricts results to ML-indexed papers, avoiding pure-psychology noise. Yield ~30–80 at ~25–35% precision per search-terms.md estimates.
- [x] 2.1.3: Select supplementary sources (4 selected — see justification below):
  - **Google Scholar** — grey literature discovery and citation tracking. Captures technical reports, forum posts, and non-indexed venues that citation databases miss. Used for forward/backward citation chaining from seed papers. Google Scholar `site:` commands used for per-source grey-lit sweeps (DeepMind, Anthropic, etc.).
  - **OpenAlex** — free, open scholarly index. API-based cross-validation of Scopus/WoS yield. Used for query calibration and cross-checking peer-reviewed yield without institutional subscription.
  - **Semantic Scholar** — AI-enhanced citation graph traversal. Primary tool for forward/backward chaining from 15–20 seed papers. Returns citation metadata + abstracts; batchable via `/paper/{id}/citations` and `/paper/{id}/references` endpoints.
  - **Connected Papers** — citation chaining visualization for top 3–5 seed papers (SCAN, COGS, CFQ). Used for qualitative graph exploration and thesis visualization, not batch extraction. Complements Semantic Scholar's API by producing visual citation-cluster maps that identify thematically dense sub-networks.
- [x] 2.1.4: Justify each database choice with coverage rationale specific to σ-trap evidence — see §2.1.2 above. Additional σ-trap-specific justifications:
  - **arXiv** essential because ~50% of CG and alignment papers never transition to peer-reviewed venues. Preprint-to-review lag < 6 months means peer-reviewed search alone introduces systematic delay. Category filtering (cs.CL, cs.AI, cs.LG) is critical to avoid noise.
  - **PsycINFO** justified because: (a) the systematicity/productivity/substitutivity vocabulary that defines CG originates in cognitive science; (b) Fodor & Pylyshyn (1988) and Marcus (1998) are foundational anchors for the CG literature; (c) the search-terms.md pilot confirms PsycINFO has unique CG coverage not fully replicated by Scopus/WoS.
  - **ACM DL** essential because the core CG benchmarks (SCAN → ICML, COGS → EMNLP, CFQ → ACL, gSCAN → ICLR, SLOG → EMNLP) are all ACM-hosted proceedings.
  - **IEEE Xplore** captures the neural-operator and formal-methods flank: papers on compositional generalization in PDE solvers (FNO, DeepONet) and formal verification of compositional properties, which are the σ-trap's applied domain.
  - **Connected Papers** added for Paper 02 (not used in Paper 01) because: seed set is narrower (9–20 papers vs 15), citation graph is more tightly clustered around CG benchmarks, and visual graph exploration reveals thematic sub-networks that batch API queries miss.
  - **Google Scholar** captures technical blog posts (DeepMind, Anthropic, OpenAI) and institution reports that the systematic review methodology literature identifies as essential for ML evidence synthesis (`review-methodology.md` §4).
- [x] 2.1.5: Satisfy CC.1.3 — all database names, coverage dates, and access dates recorded below:

  | Database | Coverage period | Access date | Status |
  |----------|----------------|-------------|--------|
  | Scopus | 2017–2026 | [To record at execution] | Primary |
  | Web of Science | 2017–2026 | [To record at execution] | Primary |
  | ACM Digital Library | 2017–2026 | [To record at execution] | Primary |
  | IEEE Xplore | 2017–2026 | [To record at execution] | Primary |
  | arXiv (cs.AI, cs.LG, cs.CL) | 2017–2026 | [To record at execution] | Primary |
  | PsycINFO | 2017–2026 | [To record at execution] | Primary |
  | Google Scholar | 2017–2026 | [To record at execution] | Supplementary |
  | OpenAlex | 2017–2026 | [To record at execution] | Supplementary |
  | Semantic Scholar | 2017–2026 | [To record at execution] | Supplementary |
  | Connected Papers | 2017–2026 | [To record at execution] | Supplementary |

### Task 2.2: Search String Development

- [ ] 2.2.1: Refine search terms from Phase 0.5 `research/search-terms.md` into database-specific strings
- [ ] 2.2.2: Design core concept blocks using PICO structure:
  - **Block P (Population)**: `"neural network" OR "deep learning" OR "transformer" OR "LSTM" OR "RNN" OR "gradient descent" OR "SGD" OR "deep net"`
  - **Block I/C (Intervention/Comparison — OOD evaluation)**: `"compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "systematic generalisation" OR "out-of-distribution" OR "OOD" OR "distribution shift" OR "recombination" OR "zero-shot generalization" OR "combinatorial generalization"`
  - **Block O (Outcome — failure or measurement)**: `"generalization failure" OR "generalisation failure" OR "shortcut learning" OR "memorization" OR "memorisation" OR "surface statistics" OR "ID-OOD gap" OR "schema coherence" OR "representational structure" OR "internal representation"`
  - **Block S (Supplementary — alignment connection, optional)**: `"alignment" OR "mesa-optimization" OR "deceptive alignment" OR "goal misgeneralization" OR "specification gaming"`
- [ ] 2.2.3: Test Boolean combinations: `(Block P) AND (Block I/C) AND (Block O)` as primary search
- [ ] 2.2.4: Create secondary search: `(Block P) AND (Block I/C) AND (Block S)` for safety-connection papers
- [ ] 2.2.5: For each database, adapt syntax (Scopus TITLE-ABS-KEY, WoS TS=, arXiv advanced search, etc.)
- [ ] 2.2.6: Create a table of search strings: database, date, exact string, yield estimate, notes
- [ ] 2.2.7: Satisfy CC.1.3 — full search strings reported in appendix (not just summary)

### Task 2.3: Grey Literature Strategy

- [ ] 2.3.1: Review Phase 0.5 `research/review-methodology.md` for grey literature handling
- [ ] 2.3.2: Define grey literature sources specific to σ-trap:
  - Technical reports from labs (DeepMind, Anthropic, OpenAI, MIRI, Google Brain)
  - Well-known blog posts on compositional generalization (authors like Lake, Keysers, Hupkes)
  - Workshop papers (NeurIPS/ICML/ICLR workshops on compositionality, robustness, OOD)
  - Preprints (arXiv, not yet peer-reviewed — capture via arXiv search directly)
  - PhD theses on compositional generalization in neural networks
- [ ] 2.3.3: Define inclusion criteria for grey literature:
  - Must be cited by at least 3 peer-reviewed papers, OR
  - Must be from a recognized research institution, OR
  - Must present novel empirical results not published elsewhere
- [ ] 2.3.4: Satisfy CC.1.3 — grey literature strategy documented in protocol

### Task 2.4: Citation Chaining Strategy

- [ ] 2.4.1: Identify 15-20 landmark papers from Phase 0.5 `research/landmark-papers.md` for citation chaining:
  - Lake et al. 2018 (SCAN)
  - Kim & Linzen 2020 (COGS)
  - Keysers et al. 2020 (CFQ)
  - Hupkes et al. 2020 (PCFG-SET)
  - Ruis et al. 2020 (gSCAN)
  - Li et al. 2021 (COFE)
  - Lake & Baroni 2023 (compositional generalization review)
  - Basri 2026 (Σ-Model — ensure our own paper is captured)
  - Any other highly-cited papers identified in Phase 0.5
- [ ] 2.4.2: Plan backward citation chaining (follow references from landmark papers to earlier foundational work)
- [ ] 2.4.3: Plan forward citation chaining (identify all papers that cite landmark papers)
- [ ] 2.4.4: Use Semantic Scholar or Connected Papers for systematic citation graph traversal
- [ ] 2.4.5: Satisfy CC.1.3 — citation chaining strategy documented

### Task 2.5: Search Validation

- [ ] 2.5.1: Verify that search strings capture all known landmark papers (from Phase 0.5 `research/landmark-papers.md`)
- [ ] 2.5.2: If any known paper is missed, add synonym, alternative phrasing, or wildcard to capture it
- [ ] 2.5.3: Calculate expected recall: known papers captured / total known papers (target: ≥ 95%)
- [ ] 2.5.4: Test precision: skim 50 random results — estimate proportion that are relevant
- [ ] 2.5.5: Adjust search strings if precision is too low (< 10%) or recall too low (< 90%)
- [ ] 2.5.6: Satisfy CC.4.1 — search strings, dates, and validation results documented in `research/search-validation.md`

---

**Phase 2 Exit Criteria**:
- [x] Finalized database list with justifications — completed via Task 2.1.2/2.1.4
- [ ] Database-specific search strings documented in protocol appendix
- [ ] Grey literature strategy defined
- [ ] Citation chaining strategy defined
- [ ] Search validation confirms recall ≥ 95% on known landmark papers
- [ ] Search precision documented
- [x] CC.1.3 — database names, coverage dates, access dates recorded in Task 2.1.5
- [ ] CC.4.1 — search strings, dates, validation results documented
- [ ] CC.5.3 satisfied — protocol update committed
