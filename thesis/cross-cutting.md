# Monograph Cross-Cutting Concerns

**Duration**: Ongoing (applies to all chapters)
**Dependencies**: None
**Output**: Standards matrix enforced across all chapters and phases

These requirements apply to **every** chapter in the monograph. Each chapter's `00_cross_cutting.md` may refine or extend these. All phases must comply unless explicitly exempted.

---

### CC.1: Writing & Formatting Consistency

- [ ] CC.1.1: All chapters use the same LaTeX preamble, document class (`report`), and bibliography style
- [ ] CC.1.2: Consistent notation across chapters (shared glossary, same symbol definitions)
- [ ] CC.1.3: All chapters cite from a shared `thesis/bibliography.bib` to avoid duplication
- [ ] CC.1.4: Equation numbering follows a convention consistent with the monograph compilation
- [ ] CC.1.5: Chapter prose is continuous monograph style — no venue-format artifacts (page limits, journal section structure) inside chapters
- [ ] CC.1.6: Chapter abstracts/summaries written in structured format (Background, Methods, Results, Conclusions) where applicable

### CC.2: Reproducibility & Transparency (empirical chapters)

- [ ] CC.2.1: Every empirical chapter declares random seeds via `torch.manual_seed(run_id * 42 + 7)` + `cudnn.deterministic = True`
- [ ] CC.2.2: Experiment configs stored as YAML in the chapter folder, never hardcoded
- [ ] CC.2.3: Data availability statement present in every empirical chapter
- [ ] CC.2.4: Code availability statement with DOI/link to repository
- [ ] CC.2.5: All figures reproducible from `code/sigma_align/` scripts
- [ ] CC.2.6: Version log (Python, PyTorch, key libraries) recorded for each experiment batch

### CC.3: Methodology Adherence

- [ ] CC.3.1: Scoping-review chapters follow PRISMA-ScR checklist (Ch 2, Ch 9)
- [ ] CC.3.2: Systematic-review chapters follow PRISMA 2020 checklist (Ch 3)
- [ ] CC.3.3: Meta-analysis chapters follow PRISMA-MA reporting standards, including heterogeneity and publication-bias assessment (Ch 6)
- [ ] CC.3.4: Conceptual chapters provide formal definitions for all key constructs (Ch 4). Schema coherence σ must be **operationally specified**: construct; unit of measurement (neuron / layer / representation / latent space / model / task-conditioned representation / trajectory); the mathematical metric; the range (e.g. σ ∈ [0,1] vs ℝ); and invariance properties (rotation, permutation, scaling, reparameterisation, basis change). A representation-space metric that changes under a latent-basis rotation is not measuring a meaningful model property.
- [ ] CC.3.5: Empirical chapters include ablation studies, hyperparameter sensitivity, and failure analysis (Ch 7, Ch 8)
- [ ] CC.3.6: Pilot-study chapters include power analysis or justification of sample size (Ch 5)
- [ ] CC.3.7: LLM-assisted pipelines (Ch 3 screening/extraction, Ch 5 analysis, Ch 6 meta-analysis) must report independent human adjudication samples and sensitivity analyses (e.g. conclusions re-run on the high-quality subset); AI assistance is disclosed, not a substitute for independent review
- [ ] CC.3.8: Chapters that draw implications from evidence (esp. Ch 9) must state limitations *before* implications; bounded "candidate component" wording — no "optimal path to safe AGI" claims

### CC.4: Monograph Coherence

- [ ] CC.4.1: Every chapter explicitly cites the overarching thesis statement in its introduction
- [ ] CC.4.2: Every chapter includes a "Relation to Other Chapters" section
- [ ] CC.4.3: Shared notation registry maintained at `thesis/back-matter/notation-registry.md`
- [ ] CC.4.4: Shared glossary maintained at `thesis/back-matter/glossary.md`
- [ ] CC.4.5: Chapters cross-reference each other (e.g., "this builds on Chapter 2's findings")
- [ ] CC.4.6: No contradiction between chapters — any differences in assumptions/findings explicitly noted
- [ ] CC.4.7: Every chapter opens and closes with "What this chapter establishes / does not establish" bookends
- [ ] CC.4.8: Chapters making causal or mechanistic claims (Ch 5, 7, 8) include an explicit competing-hypotheses section (ruling out simpler explanations)
- [ ] CC.4.9: Claims tracked in `thesis/claim-evidence-ledger.md`; no claim cited as established in a later chapter before its establishing chapter has produced the evidence (ledger updated at each phase completion)

### CC.5: Code Quality (for empirical chapters)

- [ ] CC.5.1: `ruff check code/sigma_align/` passes with zero errors
- [ ] CC.5.2: All public functions have type annotations
- [ ] CC.5.3: No hardcoded paths, secrets, or API keys in code
- [ ] CC.5.4: Experiment launch scripts use `argparse` or YAML configs (not positional args)
- [ ] CC.5.5: Config YAML files have inline comments for non-obvious parameters

### CC.6: Publication Readiness (Phase 12 — paper extraction only)

Applies when a submission-ready paper is extracted from a chapter; not required for the chapter itself.

- [ ] CC.6.1: Extracted manuscript compiles with its own `make pdf` without errors or warnings
- [ ] CC.6.2: Abstract length within venue limits
- [ ] CC.6.3: References formatted per venue style (checked via `bibexport`)
- [ ] CC.6.4: All figures at correct DPI (300+ for print, 72 for arXiv)
- [ ] CC.6.5: License and copyright transfer forms prepared
- [ ] CC.6.6: ORCID and author affiliations confirmed

### CC.7: Git Hygiene

- [ ] CC.7.1: Commit format: `[Tag][Scope][Δ] Description` — Tag=I(Impl)/B(Bugfix)/R(Refactor)/V(Validation), Scope=T(Thesis)/L(LaTeX)/C(Code)/W(Workflow)
- [ ] CC.7.2: Branch names prefixed by type — `chapter/`, `code/`, `docs/`
- [ ] CC.7.3: No direct pushes to `main` — all changes via PR
- [ ] CC.7.4: Each chapter phase completion committed with descriptive message
- [ ] CC.7.5: Large artifacts (datasets, model weights) gitignored; use DOIs/symlinks

---

### CC.8: Phase Compliance Matrix

| Phase | CC.1 (Writing) | CC.2 (Reprod) | CC.3 (Method) | CC.4 (Coherence) | CC.5 (Code) | CC.6 (Publish) | CC.7 (Git) |
|:------|:---------------|:--------------|:--------------|:-----------------|:------------|:--------------|:-----------|
| 00_repo | Required | — | — | — | — | — | Required |
| 00_5 | — | — | — | — | — | — | Required |
| 01–06 | Required | Required | Required | Required | — | — | Required |
| 07 | Required | Required | Required | Required | — | — | Required |
| 08–09 | Required | — | — | Required | — | — | Required |
| 10–11 | Required | Required | Required | Required | — | — | Required |
| 12 (paper extraction) | — | — | — | Required | — | Required | Required |
| 99 | — | — | — | Required | — | — | Required |
