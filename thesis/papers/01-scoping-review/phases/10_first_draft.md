# Phase 10 — First Draft

**Duration**: 3 weeks (Month 5)
**Deadline**: 2026-11-26
**Dependencies**: Phase 9 (thematic synthesis complete)
**Output**: Complete first draft of manuscript — `manuscript/manuscript.tex` (ACM Computing Surveys, acmart) + `manuscript/figures/` + appendices (PRISMA-ScR checklist, search strings, study list, quality summary, charted-data summary)

---

### Operationalizations (Phase A)

Locked before drafting; governs the whole manuscript.

- **Venue & format**: ACM Computing Surveys (per `manuscript/preamble.tex`, acmart `acmsmall,screen,review`); structured abstract ≤ 250 words (10.7.4, CC.2.1).
- **Citation policy (10.7.2)**: methods/context references from `thesis/bibliography.bib` (29 entries); representative included studies cited by their existing keys in `research/included-studies.bib` (P001–P1268, `@misc`); full study list → appendix/supplementary (10.8.3). Manuscript bibliography = `\bibliography{../../../bibliography,../research/included-studies}`. Density targets (checklist IV-G): Intro 10–20, Methods 15–25, Results 5–15, Discussion 20–35; paragraph rule 2–3 sources.
- **Selected figure set (10.4.5)**: PRISMA flow (`figures/prisma-flow.tex`, numbers populated) + 7 key figures staged under `manuscript/figures/` (publication type, subdomain bars, subdomain×year, co-occurrence, formal-vs-conceptual, theme trajectories, quality distribution) — vector PDF where available, PNG otherwise. Not "all figures".
- **Appendix scope (10.8.3–10.8.5)**: summary tables in the PDF; full 1,268-study list and charted data as supplementary pointers (CC.5.2 large-artifact policy).
- **Anti-JAIR guardrails (CC.9 spirit, from `Σ-Align/10-jair-desk-rejection-response.md`)**:
  1. *Clarity* — plain, active prose; acronyms defined on first use; one claim per paragraph; no opaque notation.
  2. *One claim* — the manuscript's single testable claim: **"the AGI-safety literature maps to 8 subdomains and 13 themes with a credibility distribution and a confirmed gap structure"** (a landscape map + gap stocktake — NOT a theory of safety). Stated once (contribution statement) and echoed consistently in Abstract, Introduction, Discussion (checklist V-B-02–04).
  3. *Incremental significance* — framed as one systematic step in the field's zone of proximal development (PRISMA-ScR map), with explicit "So What?" in Introduction and Abstract conclusions.
- **Writing conventions (checklist IV-A…IV-G, V-C)**: verb tenses per section (Methods/Results past; Discussion/Conclusion present for interpretation; future only for future work); funnel-model Introduction with research questions near the end; Results = the map only (zero interpretation, V-C-22); Discussion interprets without restating (V-C-23); Conclusion synthesizes without new ideas (V-C-24); recommendations specific + evidence-tied (IV-D-28–32); contribution statement in abstract + introduction + discussion (V-B); abstract written last, self-contained, concrete numbers.
- **CC numbering (Paper-01 convention)**: CC.1.1 = PRISMA-ScR checklist followed; CC.2.1 = structured abstract; CC.3.2 = thesis coherence; CC.3.3 = "Relation to Other Chapters"; CC.5.3 = phase completion committed. (Differs from global `cross-cutting.md` numbering; Paper-01 meanings used here.)
- **Section → source map**: 10.1 ← `01_protocol.md`, `landscape-boundary.md`, `existing-reviews.md`, `gap-analysis.md`; 10.2 ← `chronological-development.md`, subdomain surveys, `schema-coherence-mapping.md`; 10.3 ← phases 01–06 docs + `extraction-template.md`, `quality-criteria.md`; 10.4 ← `results-draft.md`, `phase9-summary.md`, `theme-stats.md`, `quality-report.md`; 10.5 ← `existing-reviews.md`, `gap-analysis.md`, `key-institutions.md`; 10.8 ← `prisma-scr-checklist.tex`, `search-terms.md`, `included-studies.csv`, `quality-scores.csv`.

---

### Task 10.1: Draft Introduction

- [x] 10.1.1: Write opening paragraph framing AGI safety as an urgent research area
- [x] 10.1.2: State the overarching thesis and how this scoping review fits into the larger project
- [x] 10.1.3: Define AGI safety and distinguish from narrow AI safety
- [x] 10.1.4: Summarize the state of the field in 2-3 paragraphs
- [x] 10.1.5: State the research question(s) and objectives explicitly
- [x] 10.1.6: Explain why a scoping review is needed now (cite existing reviews and their gaps from Phase 0.5)
- [x] 10.1.7: Outline the paper structure
- [x] 10.1.8: Satisfy CC.3.2 — thesis coherence: reference overarching statement

### Task 10.2: Draft Background

- [x] 10.2.1: Define key AGI safety concepts for readers new to the field
- [x] 10.2.2: Present the development timeline (from Phase 0.5 `research/chronological-development.md`)
- [x] 10.2.3: Introduce the core safety subdomains with brief definitions
- [x] 10.2.4: Introduce schema coherence and the σ-trap as a lens for organizing the literature
- [x] 10.2.5: Satisfy CC.3.2 — connect background to overarching thesis

### Task 10.3: Draft Methods

- [x] 10.3.1: Follow PRISMA-ScR checklist for Methods reporting
- [x] 10.3.2: Describe the protocol and OSF registration
- [x] 10.3.3: Describe eligibility criteria (inclusion/exclusion) with justification
- [x] 10.3.4: Describe all databases and search strategies (full strings in appendix)
- [x] 10.3.5: Describe the screening process (title → abstract → full-text)
- [x] 10.3.6: Describe the data extraction process and template
- [x] 10.3.7: Describe the quality assessment approach
- [x] 10.3.8: Describe the synthesis approach (descriptive + thematic)
- [x] 10.3.9: Satisfy CC.1.1 — PRISMA-ScR checklist followed

### Task 10.4: Draft Results

- [x] 10.4.1: Write descriptive numerical summary from Phase 9 findings
- [x] 10.4.2: Write subdomain-by-subdomain results
- [x] 10.4.3: Write cross-cutting themes results
- [x] 10.4.4: Write gaps results
- [x] 10.4.5: Insert all figures (PRISMA flow diagram, bar charts, time series, etc.)
- [x] 10.4.6: Ensure all results are traceable to specific papers or summary statistics

### Task 10.5: Draft Discussion

- [x] 10.5.1: Summarize main findings in 1-2 paragraphs
- [x] 10.5.2: Interpret findings in the context of the overarching thesis
- [x] 10.5.3: Compare with existing reviews (from Phase 0.5 `research/existing-reviews.md`)
- [x] 10.5.4: Discuss implications for AGI safety research and practice
- [x] 10.5.5: Discuss implications for the thesis project (Papers 02, 03, 09)
- [x] 10.5.6: Write limitations section (including grey literature, fast-moving field, single-reviewer limitations)
- [x] 10.5.7: Satisfy CC.3.3 — "Relation to Other Chapters" section

### Task 10.6: Draft Conclusion

- [x] 10.6.1: Restate the key contributions of the review
- [x] 10.6.2: State 3-5 specific takeaways for AGI safety researchers
- [x] 10.6.3: Outline priority directions for future research
- [x] 10.6.4: Connect back to the thesis arc

### Task 10.7: Draft Abstract and References

- [x] 10.7.1: Write structured abstract (Background, Methods, Results, Conclusions)
- [x] 10.7.2: Compile references from the shared `.bib` file
- [x] 10.7.3: Verify all citations are present and correctly formatted
- [x] 10.7.4: Check abstract length against venue limits (e.g., ACM Computing Surveys: 250 words)
- [x] 10.7.5: Satisfy CC.2.1 — structured abstract

### Task 10.8: Appendix and Supplementary Materials

- [x] 10.8.1: Include PRISMA-ScR checklist as appendix
- [x] 10.8.2: Include full search strings for all databases
- [x] 10.8.3: Include full list of included studies with paper IDs
- [x] 10.8.4: Include quality assessment rubric and scores summary
- [x] 10.8.5: Include charted data summary (top-level, full data as supplementary online)
- [x] 10.8.6: Satisfy CC.1.1 — PRISMA-ScR checklist

---

**Phase 10 Exit Criteria**:
- [x] Complete first draft of all sections (Introduction through Conclusion)
- [x] Abstract within venue word limit (≤ 250, ACM CS)
- [x] All appendices drafted
- [x] All figures placed
- [x] References compiled and verified
- [x] Manuscript compiles with zero LaTeX errors
- [x] CC.1.1 (PRISMA-ScR), CC.2.1 (structured abstract), CC.3.2/CC.3.3 (thesis coherence) satisfied
- [x] Anti-JAIR guardrail pass recorded (clarity, one claim, incremental significance)
- [x] CC.5.3 satisfied — phase completion committed

---

## Execution log (Phase A–E, 2026-08)

**Phase A — architecture locked.** Skeleton verified (`make paper01` clean rebuild, 0 errors). Phase doc patched with operationalizations: venue (ACM CS, 250-word abstract), citation policy (`thesis/bibliography.bib` + `research/included-studies.bib` P001–P1268; density targets per checklist IV-G), selected figure set (8 + PRISMA flow), appendix scope (summary tables + supplementary pointers), **Anti-JAIR guardrails** (clarity / one-claim / incremental significance), writing conventions (tenses, funnel, RQs placement, results-wall, contribution statement in 3 places), Paper-01 CC annotations, section→source map. 8 figures staged under `manuscript/figures/` (3 PNG + 5 vector PDF).

**Tasks 10.1–10.3 (Phase B).** Introduction drafted (funnel: urgency → AGI-vs-narrow → field state → why-now vs existing reviews → RQ + 5 sub-questions near end → roadmap; 16 citations; one-claim framing; CC.3.2 thesis-fit paragraph). Background drafted (concept definitions, three development waves, σ-trap/schema-coherence lens). Methods drafted per PRISMA-ScR (protocol/OSF osf.io/ntuh2, PCC eligibility, 6 databases + supplementary, screening numbers 5,191→2,867→1,278→1,268, hybrid extraction with LLM pass + ICC 0.930, D1–D8 quality rubric with kappa/ICC + sensitivity 46.3 vs 50.2%, descriptive+thematic synthesis). 3 existing-review entries added to `thesis/bibliography.bib` (gyevnar2025aisafety, shen2024bidirectional, triantafyllopoulos2026value).

**Task 10.4 (Phase C).** Results drafted from the number-verified `results-draft.md`: descriptive overview, 7 by-subdomain subsections, 13-theme table + 4 cross-cutting clusters, gaps G1–G5 + NG1–NG3; 8 figures placed with captions/cross-refs; paper-ID citations (P688, P007, P128, P1097, P864) resolving from `included-studies.bib`; zero interpretation (results = the map).

**Tasks 10.5–10.7 (Phase D).** Discussion drafted (findings → guarded thesis interpretation → existing-review comparison → 3 research-practice implications → 7-item limitations → CC.3.3 Relation to Other Chapters). Conclusion drafted (4 takeaways, 3 prioritized directions, thesis-arc bookend). Structured abstract written last: **205 words** (≤ 250, CC.2.1), concrete numbers, past/present tense split. References compile and all citations verified (0 undefined).

**Task 10.8 (Phase E).** Appendices drafted: PRISMA-ScR 22-item checklist with section mappings filled (`prisma-scr-checklist.tex`); full search strings appendix with exemplar Scopus F2/F3 strings (all 14 strings → supplementary); included-studies summary (year table + supplementary pointers); quality rubric appendix with correct D1–D8 dimensions/weights and tier cutoffs (A 3.2–4.0 / B 2.4–3.19 / C 1.6–2.39 / D <1.6). Funding statement added (checklist item 22): "This research received no external funding."

**Anti-JAIR guardrail pass (recorded):**
- *Clarity*: plain-language audit — acronyms defined on first body use (AGI, OOD, ICC, PRISMA-ScR, RLHF/DPO in table caption, LLM expanded); one claim per paragraph; no notation beyond σ_A which is defined.
- *One claim*: the claim ("the AGI-safety literature maps to 8 subdomains and 13 themes with a credibility distribution and a confirmed gap structure") stated consistently in Abstract (Conclusions), Introduction (P6), Discussion (P2), Conclusion (P3) — verified wording-consistent, no section claims more.
- *Incremental significance*: framed explicitly ("contribution is deliberately narrower and incremental"; "bound the claims the thesis can make") in Introduction and Discussion.

**Methodology-checklist subset (V-C) verified:** tense consistency per section (Methods/Results past; Discussion/Conclusion present); citation completeness (0 undefined, DOI/URL policy per bib); figures (8) and tables (3) all labelled with captions + \ref; abstract 205 ≤ 250 words self-contained; contribution statement present in abstract + introduction + discussion.

**Exit criteria (CC.5.3 — phase completion committed):**
- [x] Complete first draft of all sections (Introduction through Conclusion) — 0 remaining `\todo`
- [x] Abstract within venue word limit (205 ≤ 250, ACM CS)
- [x] All appendices drafted (checklist, search strings, studies, quality)
- [x] All figures placed (8 + PRISMA flow)
- [x] References compiled and verified (0 undefined citations)
- [x] Manuscript compiles with zero LaTeX errors (15 pages, clean log)
- [x] CC.1.1 (PRISMA-ScR checklist complete), CC.2.1 (structured abstract), CC.3.2/CC.3.3 (thesis coherence) satisfied
- [x] Anti-JAIR guardrail pass recorded (clarity, one claim, incremental significance)
- [x] CC.5.3 satisfied — phase completion committed
