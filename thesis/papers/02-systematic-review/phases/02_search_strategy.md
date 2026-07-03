# Phase 2 — Search Strategy Design

**Duration**: 1 week (Month 1–2)
**Deadline**: 2026-08-07
**Dependencies**: Phase 1 (protocol finalized and registered)
**Output**: Complete search strings for each database, documented in protocol appendix

---

### Task 2.1: Database Selection

- [ ] 2.1.1: Review Phase 0.5 `research/search-terms.md`, `research/review-methodology.md`, and Paper 01 Phase 2 outputs for database recommendations
- [ ] 2.1.2: Select primary academic databases:
  - **Scopus** (broadest coverage, best for interdisciplinary ML + cog sci + safety)
  - **Web of Science** (complementary to Scopus, stronger in formal sciences)
  - **ACM Digital Library** (for CS/AI/ML papers)
  - **IEEE Xplore** (for formal methods, robustness, verification)
  - **arXiv** (cs.AI, cs.LG, cs.CL — preprints, field moves fast)
  - **PsycINFO** (for cognitive science / compositional generalization literature)
- [ ] 2.1.3: Select supplementary sources:
  - **Google Scholar** for grey literature and citation tracking
  - **OpenAlex** for API-based search
  - **Semantic Scholar** for AI-relevant paper discovery and citation graph
  - **Connected Papers** for citation chaining visualization
- [ ] 2.1.4: Justify each database choice with coverage rationale specific to σ-trap evidence:
  - arXiv essential for cutting-edge ML results (preprint-to-review time < 6 months)
  - PsycINFO added because compositional generalization is originally a cognitive science concept
  - Google Scholar captures technical blog posts and institution reports
- [ ] 2.1.5: Satisfy CC.1.3 — all database names, coverage dates, and access dates recorded

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
- [ ] Finalized database list with justifications
- [ ] Database-specific search strings documented in protocol appendix
- [ ] Grey literature strategy defined
- [ ] Citation chaining strategy defined
- [ ] Search validation confirms recall ≥ 95% on known landmark papers
- [ ] Search precision documented
- [ ] CC.1.3, CC.4.1 satisfied
- [ ] CC.5.3 satisfied — protocol update committed
