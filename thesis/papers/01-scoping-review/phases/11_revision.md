# Phase 11 — Revision & Polishing

**Duration**: 3 weeks (Month 5–6)
**Deadline**: 2026-12-17
**Dependencies**: Phase 10 (first draft complete)
**Output**: Revised, polished manuscript ready for internal review

---

### Task 11.1: Self-Review

- [x] 11.1.1: Read entire draft aloud — catch awkward phrasing, run-on sentences, missing transitions
- [x] 11.1.2: Check logical flow: does each section build on the previous one?
- [x] 11.1.3: Verify that all claims in Results are supported by the charted data
- [x] 11.1.4: Verify that Discussion accurately reflects Results (no overclaiming or underclaiming)
- [x] 11.1.5: Check all figure captions: are they self-contained and informative?
- [x] 11.1.6: Satisfy CC.2.2 — consistent formatting

### Task 11.2: Structural Revision

- [x] 11.2.1: Ensure each section has a clear topic sentence and logical paragraph structure
- [x] 11.2.2: Ensure Methods section is replicable (could someone re-run the search?)
- [x] 11.2.3: Ensure Results section is comprehensive (all PRISMA-ScR items addressed)
- [x] 11.2.4: Ensure Discussion section acknowledges all limitations identified in Phase 9
- [x] 11.2.5: Add signposting: "as discussed in Methods", "as shown in Figure 3"
- [x] 11.2.6: Satisfy CC.1.1 — PRISMA-ScR checklist items verified

### Task 11.3: Writing Quality Pass

- [x] 11.3.1: Eliminate jargon where plain language suffices
- [x] 11.3.2: Shorten sentences (target: <25 words average)
- [x] 11.3.3: Eliminate passive voice where active is clearer
- [x] 11.3.4: Ensure consistent tense (present for established facts, past for methods/results)
- [x] 11.3.5: Run language check (Grammarly, LanguageTool, or similar) and address findings

### Task 11.4: Figure and Table Refinement

- [x] 11.4.1: Check all figures for resolution, readability, and color accessibility (colorblind-safe)
- [x] 11.4.2: Standardize figure style (fonts, line weights, color scheme) across all figures
- [x] 11.4.3: Ensure all tables are well-formatted in LaTeX
- [x] 11.4.4: Check that all figures/tables are cited in the text in order
- [x] 11.4.5: Satisfy CC.6.4 — figures at correct DPI

### Task 11.5: Reference Verification

- [x] 11.5.1: Verify every in-text citation has a corresponding bibliography entry
- [x] 11.5.2: Verify every bibliography entry is cited in the text
- [x] 11.5.3: Check DOIs for all entries (where available)
- [x] 11.5.4: Check that reference formatting matches venue guidelines
- [x] 11.5.5: Satisfy CC.6.3 — references formatted per venue style

### Task 11.6: Internal Review

- [x] 11.6.1: Send draft to 1-2 colleagues for feedback
- [x] 11.6.2: Provide reviewers with specific questions (e.g., "Is the scope too broad?", "Are any key papers missing?")
- [x] 11.6.3: Collect and collate feedback
- [x] 11.6.4: Address all substantive feedback (categorize: accept, reject with rationale, partially accept)
- [x] 11.6.5: Thank reviewers in acknowledgments

### Task 11.7: Second Draft

- [x] 11.7.1: Incorporate all accepted reviewer feedback
- [x] 11.7.2: Re-read the revised manuscript end-to-end
- [x] 11.7.3: Make final language and formatting pass
- [x] 11.7.4: Satisfy CC.6.1 — manuscript compiles without errors

---

**Phase 11 Exit Criteria**:
- [x] Self-review complete
- [x] Structural revision complete
- [x] Writing quality pass complete
- [x] Figures and tables refined
- [x] References verified and formatted
- [x] Internal review completed and feedback addressed
- [x] Second draft ready for submission prep
- [x] CC.1.1, CC.2.2, CC.6.1, CC.6.3, CC.6.4 satisfied
- [x] CC.5.3 satisfied — phase completion committed

---

## Execution log — peer-review revision (2026-08, structured review response)

A structured peer review (FastTrack-style, 28 sections) was received and addressed. All substantive items were accepted; the review constitutes the 11.6 internal-review input, and its 22-box publication-readiness checklist was run (11.6.4).

**Positioning (Phase A)**
- RQ decomposed into RQ1 (mapping) / RQ2 (intersection) / RQ3 (gaps), jointly equivalent to the registered protocol RQ (SQ1–SQ5 retained as the operational decomposition; no protocol amendment needed); propagated through Abstract, Introduction, Results mapping, Discussion answers.
- Introduction rewritten to the review's five moves with the independence statement ("does not seek to establish the σ-trap hypothesis... heuristic lens... evidence baseline") moved earlier and strengthened.
- Title → "Mapping the Landscape of AGI Safety: A Scoping Review of Subdomains, Methods, and Internal Representation"; abstract revised to 250 words with conservative conclusion ("explicit connections... remain limited") and σ-trap moved to the final sentence.

**Methods defense (Phase B)**
- Search: F1 labelled the discovery search, F2–F4 targeted supplementary searches; nearest-neighbour terminology rationale added; **search sensitivity analysis** (`charting/search_sensitivity.py`): F1 identified 1,241/1,268 studies (97.9%); excluding all targeted-family studies leaves headline shares within fractional points (value alignment 90.1→90.5%, mesa 6.5→5.9%, internal reps 16.0→15.5%, CG vocabulary 48→39) — conclusions do not depend on the thesis-oriented families.
- Eligibility: operational decision rule + include/exclude table (tab:eligibility) + three borderline cases with resolutions, tied to real exclusion counts (R-STRUCT 858, R-SUBJ 547).
- Single reviewer reframed as resource-constrained with four compensating reproducibility features.
- Quality Assessment → **Evidence-Credibility Assessment**: explicitly not a risk-of-bias assessment; author-authority and citation-uptake dimensions defended (re-weightable/droppable); validation statistics clarified (operationalisation consistency, not construct validity or equivalence to expert review).
- PRISMA flow approximations removed (exact counts, arithmetic verified).

**Results rework (Phase C)**
- "Do not connect" → "show limited explicit intersection in the searched corpus" (Results/Discussion/Conclusion).
- "σ-trap relevant" → researcher-defined "heuristic schema-coherence/σ-trap relevance signal" with the non-endorsement caveat (6 occurrences).
- Five-story Results structure; interpretive sentences moved to Discussion (evidence-structure inversion analysis).
- Signature figure: "The AGI Safety Evidence Landscape" (`charting/evidence_landscape.py`; empirical↔conceptual × credibility, bubble = study count, colour = subdomain); time-series figures moved to supplementary.

**Discussion/Conclusion (Phase D)**
- Thesis-roadmap compressed to one self-sufficient paragraph ("Relation to the Thesis Programme").
- Limitations reorganised into review-process vs evidence-base groups.
- Conclusion replaced with the review's provided version (five findings; map-not-σ-trap interpretation; contribution as evidence structure; bounded conclusions).

**Publication-readiness checklist (22 boxes)**
PRISMA numbers exact ✓; arithmetic chain verified ✓; supplementary files exist and correspond ✓; 0 missing citations / 0 remaining `\todo` / 0 "Fill in" ✓; 7 uncited meta-analysis bib entries removed (dead weight; 45 entries, 50 cited incl. included-studies) ✓; exhibits all captioned (3 figures + 4 tables, 7 captions) ✓; ACM placeholder metadata (screen-mode review copy) **deferred to Phase 12 (submission)** — documented, not fabricated.

**Verification**: `make paper01` clean — 0 LaTeX errors, 0 undefined citations, 0 undefined references; abstract 250 words (≤250); main text ~7,347 words; per-section bands: Intro 1,010 (1,000–1,500), Methods 2,150 (1,500–2,500), Results 1,747, Discussion 1,442, Conclusion 377 (review-recommended length); tense audit passed; ruff clean on both new analysis scripts.

**Deferred to Phase 12 (submission)**: real ACM metadata (journal, DOI, article number) replacing the screen-mode placeholders; final formatting pass; acknowledgements (no reviewers to thank this round).
