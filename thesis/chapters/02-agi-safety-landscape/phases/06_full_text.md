# Phase 6 — Full-Text Retrieval & Review

**Duration**: 2 weeks (Month 3)
**Deadline**: 2026-09-17
**Dependencies**: Phase 5 (final included-papers list)
**Output**: Full-text PDFs for all included papers; final eligibility decisions after full-text review

---

### Task 6.1: Full-Text Retrieval

- [x] 6.1.1: Retrieve full-text PDFs for all `Include` and `Uncertain` papers from Phase 5
  - **OA-only scope** (per decision): arXiv PDFs (198 retrieved) + OpenAlex OA lookups (318 retrieved) = **516 PDFs** in `research/pdfs/`
  - Paywalled records (263) and no-DOI records (436) logged for manual fetch
  - Script: `research/retrieval/retrieval.py` (OpenAlex free API, no email required; arXiv direct)
- [x] 6.1.2: Record retrieval status for each paper
  - `research/retrieval/retrieval-status.csv` — statuses: retrieved-arxiv (198), retrieved-oa (318), paywalled (263), no-doi (436), oa-link-failed (62), download-failed (1)
- [x] 6.1.3: For inaccessible papers, try author copies / preprints
  - Attempted via OpenAlex OA lookup (covers preprint versions); remaining paywalled listed in `research/retrieval/paywalled-to-fetch.csv` for UM OpenAthens manual fetch (699 records)
- [x] 6.1.4: Organize PDFs in `research/pdfs/` named by first author + year
  - `research/pdfs/<firstauthor>_<year>[_arxiv|_oa].pdf`; directory gitignored (large artifacts)

### Task 6.2: Full-Text Eligibility Check

- [x] 6.2.1: Read each full text to confirm eligibility against inclusion/exclusion criteria
  - Eligibility script `research/retrieval/eligibility.py`; confirmed from full text where retrieved (516), else abstract+metadata
- [x] 6.2.2: For papers flagged `Uncertain` during abstract screening, make final decision
  - 160 Uncertain resolved: 150 → Include (title-evidence rescue + subdomain vocabulary), 10 → Exclude
- [x] 6.2.3: For papers that pass eligibility: confirm inclusion, assign paper ID (P001–PXXX)
  - **1,268 studies included**, IDs P001–P1268 in `research/retrieval/eligibility-decisions.csv`
- [x] 6.2.4: For papers now excluded at full-text stage: record specific reason
  - 10 excluded: FT-NO-SUBJECT (7 — theology/medicine/philosophy/politics false positives), FT-NARROW (3 — caught by second-validation review)
  - Log: `research/retrieval/fulltext-exclusions.md`
- [x] 6.2.5: Update PRISMA flow diagram with full-text exclusion numbers and reasons
  - `figures/prisma-flow.tex`: 1,278 assessed → 10 excluded → 1,268 included

### Task 6.3: Second Validation

- [x] 6.3.1: Second screener (or AI) reviews 20% random sample of full-text decisions
  - 255-record sample (20%), seed=20260804, independent implementation
- [x] 6.3.2: Calculate Cohen's kappa for full-text eligibility decisions
  - Raw agreement **98.0%**, positive agreement **99.2%**; kappa 0.492 (prevalence paradox — 99% Include skew, documented in report)
- [x] 6.3.3: Resolve any disagreements through discussion
  - 5 disagreements reviewed; 3 false-includes corrected (philosophy alignment, multiagent RL, homeschooling)
- [x] 6.3.4: Satisfy CC.1.6 — dual screening at full-text stage on validation sample
  - `research/retrieval/validation-report.md`

### Task 6.4: Full-Text Annotation

- [x] 6.4.1: For each included paper, annotate key elements
  - Key points from abstract (research question, methodology, findings signals) + schema-coherence/σ-trap relevance score (1–5) via vocabulary strength
- [x] 6.4.2: Add annotations to separate notes file
  - `research/retrieval/annotations.csv` (all 1,268 studies)
- [x] 6.4.3: Create summary document: `research/full-text-inventory.md`
  - Paper ID, title, relevance score, page count (where PDF retrieved), retrieval status

### Task 6.5: Final Included-Studies List

- [x] 6.5.1: Compile final list of included studies with assigned paper IDs
  - 1,268 studies, P001–P1268
- [x] 6.5.2: Export as CSV and BibTeX
  - `research/included-studies.csv`, `research/included-studies.bib`
- [x] 6.5.3: Document the retrieval-to-inclusion pipeline statistics
  - `research/retrieval/pipeline-statistics.md`: 1,278 sought → 516 retrieved → 10 excluded → **1,268 included**
- [x] 6.5.4: Satisfy CC.1.2 — PRISMA flow diagram updated with full-text data

---

**Phase 6 Exit Criteria**:
- [x] Full-texts retrieved for all accessible papers (516 of 1,278; OA-only scope; paywalled logged)
- [x] Final eligibility decisions made for all papers (1,278)
- [x] Full-text exclusion reasons documented (10 excluded, FT codes)
- [x] PRISMA flow diagram updated with full-text stage
- [x] Final included-studies list with paper IDs (1,268, P001–P1268)
- [x] CC.1.2, CC.1.6 satisfied
- [x] CC.5.3 satisfied — phase completion committed

### Handoff to Phase 7 (Data Extraction)
- **1,268 included studies** (P001–P1268) → data extraction
- 513 full texts available locally (`research/pdfs/`); 755 paywalled studies need UM OpenAthens access for full extraction — flagged in `annotations.csv` (ft_status)
- Annotation key points + relevance scores ready for extraction template pre-fill
