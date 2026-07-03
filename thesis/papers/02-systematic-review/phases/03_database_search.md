# Phase 3 — Database Search Execution

**Duration**: 1 week (Month 2)
**Deadline**: 2026-08-14
**Dependencies**: Phase 2 (search strings finalized)
**Output**: Raw search results from all databases exported to `research/search-results/`

---

### Task 3.1: Run Academic Database Searches

- [ ] 3.1.1: Execute search on Scopus — export results as RIS/BibTeX to `research/search-results/scopus-YYYY-MM-DD.ris`
- [ ] 3.1.2: Execute search on Web of Science — export results as RIS/BibTeX to `research/search-results/wos-YYYY-MM-DD.ris`
- [ ] 3.1.3: Execute search on ACM Digital Library — export results to `research/search-results/acm-YYYY-MM-DD.ris`
- [ ] 3.1.4: Execute search on IEEE Xplore — export results to `research/search-results/ieee-YYYY-MM-DD.ris`
- [ ] 3.1.5: Execute search on arXiv via API — export results as JSON/CSV to `research/search-results/arxiv-YYYY-MM-DD.json`
- [ ] 3.1.6: Execute search on PsycINFO — export results to `research/search-results/psycinfo-YYYY-MM-DD.ris`
- [ ] 3.1.7: Record for each search: date executed, exact search string, number of results, any errors or adjustments
- [ ] 3.1.8: Satisfy CC.4.1 — search execution logs stored in `research/search-logs.md`

### Task 3.2: Supplementary Source Searching

- [ ] 3.2.1: Search Google Scholar (first 300 results by relevance) — export as CSV
- [ ] 3.2.2: Search OpenAlex via API — export results
- [ ] 3.2.3: Search Semantic Scholar — export results
- [ ] 3.2.4: Record search dates, proxies used (if any), and result counts

### Task 3.3: Grey Literature Collection

- [ ] 3.3.1: Retrieve technical reports from DeepMind, Anthropic, OpenAI, Google Brain, MIRI, ARC on compositional generalization or OOD topics
- [ ] 3.3.2: Retrieve relevant posts from AI Alignment Forum, LessWrong (search for "compositional generalization", "OOD failure", "shortcut learning")
- [ ] 3.3.3: Retrieve workshop papers from relevant NeurIPS/ICML/ICLR workshops (2020–2026)
- [ ] 3.3.4: Retrieve PhD theses on compositional generalization (via ProQuest or institutional repositories)
- [ ] 3.3.5: Record sources, retrieval dates, and any access restrictions

### Task 3.4: Citation Chaining

- [ ] 3.4.1: Compile final list of 15-20 seminal papers for citation chaining from Phase 2
- [ ] 3.4.2: Perform backward citation chaining — extract and deduplicate references from all seminal papers
- [ ] 3.4.3: Perform forward citation chaining — use Semantic Scholar or Connected Papers to find all papers citing each seminal paper
- [ ] 3.4.4: Record chaining paths and new papers identified in `research/citation-chaining-log.md`
- [ ] 3.4.5: Add newly identified papers to the search results pool

### Task 3.5: Export and Archive

- [ ] 3.5.1: Convert all exports to a unified format (RIS or BibTeX)
- [ ] 3.5.2: Archive all raw exports in `research/search-results/`
- [ ] 3.5.3: Create summary table: database, date, string, hits, notes
- [ ] 3.5.4: Calculate total unique records before deduplication
- [ ] 3.5.5: Satisfy CC.4.1 — raw data committed to repo (or OSF if too large, with `.gitkeep` placeholder)
- [ ] 3.5.6: Satisfy CC.4.2 — screening data structure prepared for Phase 4

---

**Phase 3 Exit Criteria**:
- [ ] All six primary databases searched
- [ ] Supplementary sources (Google Scholar, OpenAlex, Semantic Scholar) searched
- [ ] Grey literature collected
- [ ] Citation chaining completed
- [ ] All raw exports archived in `research/search-results/`
- [ ] Search log documented with dates, strings, and hit counts
- [ ] Total unique records counted
- [ ] CC.4.1, CC.4.2 satisfied
- [ ] CC.5.3 satisfied — phase completion committed
