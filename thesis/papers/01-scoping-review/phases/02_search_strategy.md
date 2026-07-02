# Phase 2 — Search Strategy Design

**Duration**: 1 week (Month 2)
**Deadline**: 2026-08-06
**Dependencies**: Phase 1 (protocol finalized and registered)
**Output**: Complete search strings for each database, documented in protocol appendix

---

### Task 2.1: Database Selection

- [ ] 2.1.1: Review Phase 0.5 `research/publication-venues.md` and `research/search-terms.md` for database recommendations
- [ ] 2.1.2: Select primary academic databases:
  - Scopus (broadest coverage, best for inter-disciplinary AGI safety)
  - Web of Science (complementary to Scopus, stronger in formal sciences)
  - ACM Digital Library (for CS/AI safety papers)
  - IEEE Xplore (for formal methods, robustness, verification)
  - arXiv (cs.AI, cs.LG, cs.CY — preprints, field moves fast)
  - PhilPapers (for philosophical/ethical dimensions of AGI safety)
- [ ] 2.1.3: Select supplementary sources:
  - Google Scholar for grey literature and citation tracking
  - OpenAlex for API-based search
  - Semantic Scholar for AI-relevant paper discovery
- [ ] 2.1.4: Justify each database choice with coverage rationale
- [ ] 2.1.5: Satisfy CC.1.3 — all database names, coverage dates, and access dates recorded

### Task 2.2: Search String Development

- [ ] 2.2.1: Refine search terms from Phase 0.5 `research/search-terms.md` into database-specific strings
- [ ] 2.2.2: Design core concept blocks:
  - Block A: AGI / transformative AI / advanced AI
  - Block B: Safety / alignment / risk / governance
  - Block C: Formal methods / framework / approach
- [ ] 2.2.3: Test Boolean combinations: `(Block A) AND (Block B) AND (Block C)`
- [ ] 2.2.4: For each database, adapt syntax (Scopus uses TITLE-ABS-KEY, WoS uses TS=, etc.)
- [ ] 2.2.5: Create a table of search strings: database, date, exact string, yield estimate, notes
- [ ] 2.2.6: Satisfy CC.1.3 — full search strings reported in appendix (not just summary)

### Task 2.3: Grey Literature Strategy

- [ ] 2.3.1: Review Phase 0.5 research on grey literature importance in AGI safety
- [ ] 2.3.2: Define grey literature sources:
  - Technical reports (DeepMind, Anthropic, OpenAI, MIRI, ARC)
  - Well-known blog posts (LessWrong, EA Forum, AI Alignment Forum)
  - Workshop papers (NeurIPS/ICML/AAAI safety workshops)
  - Preprints (arXiv, not yet peer-reviewed)
- [ ] 2.3.3: Decide inclusion criteria for grey literature (e.g., must be cited by 5+ peer-reviewed papers, or from recognized institution)
- [ ] 2.3.4: Satisfy CC.1.3 — grey literature strategy documented in protocol

### Task 2.4: Citation Chaining Strategy

- [ ] 2.4.1: Identify 10-15 seminal papers from Phase 0.5 research (especially from `research/key-institutions.md` and `research/value-alignment-survey.md`)
- [ ] 2.4.2: Plan backward citation chaining (follow references from seminal papers)
- [ ] 2.4.3: Plan forward citation chaining (papers that cite seminal papers)
- [ ] 2.4.4: Use Semantic Scholar or Connected Papers for citation graph traversal
- [ ] 2.4.5: Satisfy CC.1.3 — citation chaining strategy documented

### Task 2.5: Search Validation

- [ ] 2.5.1: Verify that search strings capture all known landmark papers (from Phase 0.5 research)
- [ ] 2.5.2: If any known paper is missed, add synonym/alternative term to capture it
- [ ] 2.5.3: Calculate expected recall: known papers captured / total known papers
- [ ] 2.5.4: Satisfy CC.4.1 — search strings, dates, and validation documented

---

**Phase 2 Exit Criteria**:
- [ ] Finalized database list with justification
- [ ] Database-specific search strings documented in protocol appendix
- [ ] Grey literature strategy defined
- [ ] Citation chaining strategy defined
- [ ] Search validation confirms recall of known landmark papers
- [ ] CC.1.3, CC.4.1 satisfied
- [ ] CC.5.3 satisfied — protocol update committed
