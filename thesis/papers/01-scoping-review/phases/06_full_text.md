# Phase 6 — Full-Text Retrieval & Review

**Duration**: 2 weeks (Month 3)
**Deadline**: 2026-09-17
**Dependencies**: Phase 5 (final included-papers list)
**Output**: Full-text PDFs for all included papers; final eligibility decisions after full-text review

---

### Task 6.1: Full-Text Retrieval

- [ ] 6.1.1: Retrieve full-text PDFs for all `Include` and `Uncertain` papers from Phase 5:
  - Papers with DOIs: download via DOI resolver (Unpaywall, Sci-Hub as last resort)
  - Papers on arXiv: download directly from arXiv
  - Papers from ACM/IEEE: access via institutional subscription
  - Grey literature: retrieve from original source URLs
  - Books/book chapters: retrieve relevant sections
- [ ] 6.1.2: Record retrieval status for each paper: retrieved, not accessible, requires purchase, no DOI
- [ ] 6.1.3: For inaccessible papers (behind paywall, no institutional access), try:
  - Author copy (ResearchGate, personal webpage)
  - Preprint version for comparison
  - Inter-library loan
- [ ] 6.1.4: Organize PDFs in `research/pdfs/` named by first author + year

### Task 6.2: Full-Text Eligibility Check

- [ ] 6.2.1: Read each full text to confirm eligibility against inclusion/exclusion criteria
- [ ] 6.2.2: For papers flagged `Uncertain` during abstract screening, make final decision
- [ ] 6.2.3: For papers that pass eligibility: confirm inclusion, assign paper ID (P001–PXXX)
- [ ] 6.2.4: For papers now excluded at full-text stage: record specific reason (e.g., "full text reveals no AGI safety content despite abstract suggesting it")
- [ ] 6.2.5: Update PRISMA flow diagram with full-text exclusion numbers and reasons

### Task 6.3: Second Validation

- [ ] 6.3.1: Second screener (or AI) reviews 20% random sample of full-text decisions
- [ ] 6.3.2: Calculate Cohen's kappa for full-text eligibility decisions
- [ ] 6.3.3: Resolve any disagreements through discussion
- [ ] 6.3.4: Satisfy CC.1.6 — dual screening at full-text stage on validation sample

### Task 6.4: Full-Text Annotation

- [ ] 6.4.1: For each included paper, annotate the PDF with highlights of key elements:
  - Research question / thesis statement
  - Methodology used
  - Key findings
  - Formal framework or mathematical approach (if any)
  - Limitations stated
  - Relevance to schema coherence / σ-trap (1–5 scale)
- [ ] 6.4.2: Add annotations as PDF comments or extract highlights to separate notes file
- [ ] 6.4.3: Create summary document: `research/full-text-inventory.md` with paper ID, title, annotation key points, page count

### Task 6.5: Final Included-Studies List

- [ ] 6.5.1: Compile final list of included studies with assigned paper IDs
- [ ] 6.5.2: Export as CSV and BibTeX to `research/included-studies.bib`
- [ ] 6.5.3: Document the retrieval-to-inclusion pipeline statistics:
  - Total sought for retrieval
  - Total retrieved
  - Total excluded after full-text review (with breakdown of reasons)
  - Total included for data extraction
- [ ] 6.5.4: Satisfy CC.1.2 — PRISMA flow diagram updated with full-text data

---

**Phase 6 Exit Criteria**:
- [ ] Full-texts retrieved for all accessible papers
- [ ] Final eligibility decisions made for all papers
- [ ] Full-text exclusion reasons documented
- [ ] PRISMA flow diagram updated with full-text stage
- [ ] Final included-studies list with paper IDs
- [ ] CC.1.2, CC.1.6 satisfied
- [ ] CC.5.3 satisfied — phase completion committed
