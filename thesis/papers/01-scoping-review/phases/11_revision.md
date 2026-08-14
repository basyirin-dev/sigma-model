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

---

## Execution log — third revision round (2026-08, consolidated Reviews #1-#3)

Three structured reviews (FastTrack 8.5/10; referee 3.5/5; prior FastTrack 7.1/10) were consolidated; all substantive items accepted.

**Voice, COI, framing (Phase A)**
- Positionality/COI statement added after the title block (author = author of the σ-trap hypothesis; independent evidence map; mitigations cited).
- Manuscript fully de-thesisfied: 0 standalone "thesis"/"thesis-by-publication"/"Paper 09"; Discussion+Conclusion neutral; Relation-to-Programme rewritten to the referee's PEER version; theme/search labels renamed (schema-coherence/theory-oriented).
- Framing sentence ("ingredients of a schema-coherence account") deduplicated to 1 (Abstract); hedges propagated (heuristic-signal coding-rule caveat + RQ2 vocabulary-artefact caveat in Abstract/§4.5/§5/§6); "least-validated methods" → "lowest scores on the source-and-rigour composite used here"; inversion promoted in Abstract.
- Intro σ-trap condensed to two sentences; RQ1-RQ3 as a numbered list.

**Methods transparency (Phase B)**
- §3.5.1 LLM pipeline disclosure (model not fixed across batches; prompts archived; validation = scripted, pipeline-internal); §3.5.2 human-adjudicated spot-check (30 records vs full texts: subdomains 80%, methodology 93%, formal framework 83%, relevance 87%) — the non-pipeline anchor.
- §3.4 eligibility-stage screening validation: 15% seeded re-screen (n=430), kappa 0.39, abstract-stage 72%; screening ratio explained (liberal screen, 44.6% carried to full text).
- Credibility: E-tier boundary fixed (D 0.8-1.59, E 0.0-0.79 per rubric); D1-D2/-0.16 non-redundancy; D6 time-discounting specified; AI-Forum inclusion rule specified; 2026 partial-year flagged in Results.

**Gap demonstration (Phase C)**
- Prior-review comparison table (tab:prior-reviews) — gap demonstrated, not asserted.
- Supplementary S4 (48 CG studies), S5 (8 intersection studies, §4.5.1 characterisation: vocabulary-level, not programme-level), S6 (gaps pre-specified vs confirmed; the 3 new gaps marketed as independently discovered).

**Compression/presentation (Phase D)**
- Venue-country proxy cut from main text (supplementary pointer); §4.3 compressed ~66%; 71.8%/72.6% denominator clarified; evidence-landscape figure regenerated (legibility) + fig-graphical-abstract created; two longest sentences split.

**Cleanup (Phase E)**
- Bibliography artefacts stripped: all 1,268 "Paper 01 study; source: ..." note fields removed from included-studies.bib (provenance retained in the CSV); 0 artefacts in the compiled PDF.

**Verification**: `make paper01` clean from scratch — 0 errors, 0 undefined citations, 0 undefined references; abstract 248 ≤ 250; main text ~7,909 words; exhibits 3 figures + 5 tables (4 main-text + 1 appendix; prior-review table per review request); 50 cited keys; voice audit 0 thesis references; framing sentence ×1; hedges present in Abstract; ruff clean on all new scripts (spot_check, screening_validation, evidence_landscape, search_sensitivity).

---

## Execution log — Review #17 major-revision round (2026-08, adjudication + signal fix)

Four structured reviews now consolidated (two FastTrack, two referee reports). This round implemented the major-revision items of Review #17 with the author acting as the human second reviewer.

**Human-judgment layer (Review #17 Concerns 1/2/4/7)**
- Author adjudicated three seeded samples (original decisions hidden): screening 100 (74% raw, κ=0.48 vs mechanical κ=0.39), σ-trap relevance 30 (80% exact-scale κ=0.72; 100% membership κ=1.00), borderline 15 (80% vs final status). Folded into §3.4, §3.5.2, §3.2, and the Limitations; instruments + full disagreement logs in `research/charting/adjudication/`.
- These are now the review's only "validation" numbers; all pipeline statistics were renamed to consistency checks (0 "validation" occurrences remain).

**Claim-tempering (priorities 1–2)**
- Abstract/conclusion reframed to "a provisional credibility-stratified map"; three-layer separation (descriptive / reviewer-defined heuristic / theoretical) made explicit; intersection restated as vocabulary-level absence; inversion framed as rubric-dependent.

**Credibility rubric (Concern 3, priority 4)**
- Renamed source-and-rigour index in the appendix; new no-D2/D6 sensitivity (A+B 24.7%→30.6%; inversion persists, governance 33.3%→40.9%); weights + grey-literature penalty discussed.

**Signal-definition correction (found via the author's Round-4 notes)**
- The Phase 7 export conflated "final ≥ 4" with "AI-revised" (70 extra rows). Corrected signal = final ≥ 4: **464 (40.8%)** (was 534/47.0%), renumbered through the manuscript, abstract, discussion, sensitivity (49.5% A+B subset), submission artifacts, and research docs (gap-analysis, results-draft, thematic-synthesis, keyword-dictionary).
- Round-4 keyword critique verified: 2 external-AI claims rejected (no `reward missecif` typo; `sigma-trap` already in Theme 13); false-positive flags confirmed; synonym deltas + safe-token adoption documented in `keyword-dictionary.md`.

**Consistency fixes (minors 4.1/4.2/4.5/4.6/4.8/4.9)**
- arXiv 18.0%→15.5%; figure baseline 24.7% + label-rendering fix; theme-size caveat at Table 4; AI-Forum record handling; goal-misgen search-scope statement; new 8-intersection Table; keyword dictionary published as supplementary.

**Verification**: `make paper01` clean — 0 errors, 0 undefined, 23 pages; abstract 250; framing ×1; stale-number sweep clean (0 remaining 534/47.0/587/46.3/18.0 references); ruff-clean. Commits: `f14b111` (part 1), `bab6256` (adjudication + signal fix).
