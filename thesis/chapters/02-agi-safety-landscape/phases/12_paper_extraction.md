# Phase 12 — Paper Extraction (optional)

**Duration**: 2 weeks (Month 6)
**Deadline**: 2026-12-31
**Dependencies**: Phase 11 (chapter manuscript ready)
**Output**: Submission-ready paper extracted from the chapter and submitted to target venue

---

### Task 12.1: Venue Finalization

- [ ] 12.1.1: Confirm target venue — **resolved 2026-08-14: Artificial Intelligence Review first** (P2 analysis: lowest desk-rejection risk for scoping reviews, faster handling, solo-author + LLM-pipeline friendly, Scopus/SCIE-indexed; ACM Computing Surveys as the prestige fallback accepting a ~12-month timeline)
- [ ] 12.1.2: Download and read venue's author guidelines
- [ ] 12.1.3: Check page/word limits, formatting requirements, abstract limits
- [ ] 12.1.4: Check LaTeX class file and template requirements (AI Review uses Springer's `sn-jnl.cls`; the current manuscript is `acmart`/`acmsmall` — a template conversion is required)
- [ ] 12.1.5: Satisfy CC.6.2 — abstract length confirmed

### Task 12.2: Formatting Pass

- [ ] 12.2.1: Apply venue's LaTeX document class
- [ ] 12.2.2: Adjust formatting: margins, fonts, section heading style, reference format
- [ ] 12.2.3: Ensure all figures meet venue's file format and DPI requirements
- [ ] 12.2.4: Ensure supplementary materials are packaged per venue requirements
- [ ] 12.2.5: Satisfy CC.6.1 — manuscript compiles with venue's template

### Task 12.3: Metadata and Author Information

- [ ] 12.3.1: Confirm author names, affiliations, and ORCIDs
- [ ] 12.3.2: Write acknowledgments (funding sources, reviewer thanks, etc.)
- [ ] 12.3.3: Write author contributions statement
- [ ] 12.3.4: Write data availability statement
- [ ] 12.3.5: Write code availability statement (if applicable)
- [ ] 12.3.6: Write competing interests statement
- [ ] 12.3.7: Satisfy CC.6.5 — license and copyright forms prepared
- [ ] 12.3.8: Satisfy CC.6.6 — ORCID and affiliations confirmed

### Task 12.4: arXiv Preprint Pass (Optional)

- [ ] 12.4.1: If submitting to arXiv: prepare arXiv-compatible source (PDF or TeX bundle)
- [ ] 12.4.2: Check arXiv categories (e.g., cs.AI, cs.LG, cs.CY)
- [ ] 12.4.3: Write arXiv abstract (may differ from journal abstract)
- [ ] 12.4.4: Ensure all hyperlinks, cross-refs, and bibliographies render correctly in arXiv compilation
- [ ] 12.4.5: Submit to arXiv

### Task 12.5: Peer-Reviewed Submission

- [ ] 12.5.1: Create submission account (if new) or log in to existing account
- [ ] 12.5.2: Upload manuscript PDF
- [ ] 12.5.3: Upload supplementary materials (if any)
- [ ] 12.5.4: Fill in metadata (author list, abstract, keywords, subject areas)
- [ ] 12.5.5: Verify submission preview is correct
- [ ] 12.5.6: Submit
- [ ] 12.5.7: Record submission date, manuscript ID, and any confirmation details in `README.md`

### Task 12.6: Post-Submission Documentation

- [ ] 12.6.1: Archive the submitted version in `research/submitted-version/` (relative to this chapter: `thesis/chapters/02-agi-safety-landscape/research/submitted-version/`)
- [ ] 12.6.2: Update `README.md` (this chapter's README: `thesis/chapters/02-agi-safety-landscape/README.md`) with submission status and manuscript ID
- [ ] 12.6.3: Satisfy CC.6.1 — submitted version compiles and is archived

---

**Phase 12 Exit Criteria**:
- [ ] Manuscript formatted per venue guidelines
- [ ] All author metadata finalized
- [ ] arXiv preprint submitted (if applicable)
- [ ] Peer-reviewed manuscript submitted
- [ ] Submitted version archived
- [ ] README.md updated with submission status
- [ ] CC.6.1, CC.6.2, CC.6.3, CC.6.4, CC.6.5, CC.6.6 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

---

## Phase 12 preparation notes (2026-08, from the Phase-12 addendum review)

### Cover-letter bullet points (draft, for the editor)

Do not mention the 9-paper thesis arc; present the paper as a standalone contribution.

1. **Scale and rigour**: a PRISMA-ScR scoping review of 1,268 included records (1,136 unique studies after collapsing 132 duplicate versions; 5,191 records → 2,867 screened → 1,278 full-text) across six databases plus grey literature, with a prospectively registered OSF protocol and no amendments.
2. **The contribution**: the first credibility-stratified map of the AGI-safety landscape — an eight-subdomain taxonomy (7 named subdomains + other), a methods/formalism census, and the treatment of internal representation structure, in one reproducible evidence map (prior reviews map at most one of these; see Table 1).
3. **The headline finding**: the credibility inversion — the field's largest empirical strand (evaluation; 251 studies) is among the least credible (17.9% tier A+B), while the most credible strands are the least empirical. This is field-level, not thesis-specific.
4. **A structural gap mapped**: only 48 studies use compositional-generalisation vocabulary, of which 8 intersect with σ-trap language ("goal misgeneralization" appears in none) — mapped as a vocabulary finding with the appropriate caveats.
5. **Transparency**: hybrid extraction with a 20% consistency sample (extraction ICC 0.930; credibility scoring κ 0.924–1.000, composite ICC 0.947) and human re-adjudication samples (screening 74% raw agreement, κ 0.48; σ-relevance 80%, κ 0.72), plus a search-sensitivity analysis showing the headline results are robust to the targeted search families.
6. **Positioning**: schema coherence is used strictly as a heuristic search lens, not as a conclusion; the review is an evidence baseline for testing any structural account.

### Phase-12 checklist additions (thesis-specific)

- [ ] **Stranger test** (manual): give the manuscript to someone who knows nothing about the Σ-Align thesis; ask "does this read like an objective map of AI safety, or like an argument for a specific theory?" Apply the voice-separation edits if the latter.
- [ ] **Preprint strategy**: if posting to arXiv while under review, ensure the arXiv abstract matches the standalone journal abstract (no thesis-chapter framing).
- [ ] **Supplementary data schema lock**: `research/charted-data.csv` and `research/quality-scores.csv` are the ingestible base for Papers 05–07 — do not change the schema after submission without a versioned note.
- [ ] **Placeholder metadata**: convert the manuscript from `acmart` (acmsmall, screen, review) to Springer `sn-jnl.cls` for AI Review (see Task 12.1.4); replace placeholders (journal, DOI, article number) with real values at submission.
- [ ] **DOI/URL verification**: verify all DOIs/URLs in the reference list resolve.
- [ ] **Venue finalisation**: **resolved 2026-08-14 — Artificial Intelligence Review first** (Task 12.1.1); ACM Computing Surveys as fallback. No further venue decision needed before formatting.
- [ ] **Acknowledgments**: no external reviewers to thank this round (single-author, self-funded); state "no external funding" (already in the manuscript).
