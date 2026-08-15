# Paper 06 v2 — Cross-Cutting Standards (Standalone Paper)

**Duration**: Ongoing (applies to all phases of the σ-Trap paper rewrite)
**Dependencies**: None
**Output**: Standards matrix enforced across all phases 00–13 of the Paper 06 v2 roadmap
**Status**: Adapted 2026-08-16 from the archived monograph `thesis/cross-cutting.md` (CC.1–CC.8); deltas recorded at the end of this document.

These requirements apply to **every** phase of the Paper 06 v2 pipeline (see `paper/planning/roadmap.md`). All phases must comply unless explicitly exempted.

---

## CC.1: Writing & Formatting Consistency

- [ ] CC.1.1: The narrow manuscript uses the TMLR format (`tmlr.sty`, already in `paper/`); the companion technical report uses the same preamble family
- [ ] CC.1.2: Consistent notation across the narrow paper and the companion — shared symbol definitions; a symbol is defined before first use and used after definition
- [ ] CC.1.3: Both documents cite from `paper/bibliography.bib`; no duplicated or dead entries
- [ ] CC.1.4: Equation numbering follows the TMLR/paper convention; no cross-file equation references
- [ ] CC.1.5: Prose is journal-style — no monograph or venue-format artifacts; the narrow paper is fully self-contained
- [ ] CC.1.6: Abstract written in structured form (Problem, Method, Results, Conclusion) within the venue word limit (≤250 words)

## CC.2: Reproducibility & Transparency

- [ ] CC.2.1: Every experiment declares random seeds via `torch.manual_seed(run_id * 42 + 7)` + `cudnn.deterministic = True`; per-seed results reported
- [ ] CC.2.2: Experiment configs stored as YAML in `code/experiments/configs/`, never hardcoded
- [ ] CC.2.3: Data availability statement present in the narrow manuscript
- [ ] CC.2.4: Code availability statement with link to the repository
- [ ] CC.2.5: All figures reproducible from `code/sigma_align/` scripts
- [ ] CC.2.6: Version log (Python, PyTorch, key libraries) recorded for each experiment batch in `paper/planning/version-log.md`

## CC.3: Methodology & Claim Discipline

- [ ] CC.3.1: The model is explicitly presented as **phenomenological** (posited ODEs, not derived from SGD); the SGD↔ODE mapping is stated as an explicit Conjecture
- [ ] CC.3.2: Three-layer claim separation maintained throughout: *model theorem* (what follows from the ODEs) / *empirical observation* (what the pilot and gate experiment show) / *scientific interpretation* (what we argue it means)
- [ ] CC.3.3: Schema coherence σ_A is operationally specified: construct; unit of measurement; the mathematical metric; the range (σ ∈ [0,1]); and invariance properties. A representation-space metric that changes under a latent-basis rotation is not measuring a meaningful model property
- [ ] CC.3.4: The circularity of the Stage-2 diagnostic (σ̂_A = Acc_OOD / Acc_ID) is stated plainly wherever the diagnostic is used; Stage-1 proxies (GCA/RGA/AC) are used for training-time signals and referenced to the companion
- [ ] CC.3.5: Empirical sections include the fixed-weight vs ODE-guided ablation (mechanism gate), per-seed reporting, confidence intervals, and effect sizes by benchmark (not pooled)
- [ ] CC.3.6: Sample size justification / power note provided for the pilot (n = 15 per condition) — the massive effect sizes (d ≈ 9.08 / 7.57) are reported transparently with raw distributions
- [ ] CC.3.7: A claim-status table (§12) separates *proven in model* / *proven under assumptions* / *empirically supported in pilot* / *open* / *not established* for every central claim
- [ ] CC.3.8: Competing-hypotheses discipline: grokking, lazy-to-rich phase transitions, singular learning theory, shortcut learning, sharpness/flatness, and lottery-ticket accounts are addressed in §2 with an explicit distinction (see `paper/planning/novelty-audit.md`)
- [ ] CC.3.9: Limitations are stated before implications; no "optimal path to safe AGI" or grand-theory claims in the narrow paper — the foundational hypothesis appears only as a labeled research programme in the Discussion

## CC.5: Code Quality

- [ ] CC.5.1: `ruff check code/sigma_align/` passes with zero errors
- [ ] CC.5.2: All public functions have type annotations
- [ ] CC.5.3: No hardcoded paths, secrets, or API keys in code
- [ ] CC.5.4: Experiment launch scripts use YAML configs (not positional args)
- [ ] CC.5.5: Config YAML files have inline comments for non-obvious parameters

## CC.6: Publication Readiness

- [ ] CC.6.1: Manuscript and companion compile with their own `make pdf` without errors or undefined references
- [ ] CC.6.2: Abstract length within venue limits (≤250 words)
- [ ] CC.6.3: References formatted per TMLR style; bibliography pruned of dead entries
- [ ] CC.6.4: Figures at correct DPI (300+ for print, 150 for arXiv); all figures reproducible
- [ ] CC.6.5: arXiv bundle excludes `jair.cls`; includes `tmlr.sty` + `.bbl` + figures + companion
- [ ] CC.6.6: Author name, affiliation, ORCID confirmed for the submission package

## CC.7: Git Hygiene

- [ ] CC.7.1: Commit format: `[Tag][Scope][Δ] Description` — Tag=I(Impl)/B(Bugfix)/R(Refactor)/V(Validation), Scope=L(LaTeX)/C(Code)/W(Workflow)
- [ ] CC.7.2: No large artifacts (datasets, model weights, raw results) committed — gitignored; raw experiment outputs stay out of git
- [ ] CC.7.3: Each phase completion committed with a descriptive message
- [ ] CC.7.4: Decision records and planning docs live in `paper/planning/`

---

## CC.8: Phase Compliance Matrix (Paper 06 v2)

| Phase | CC.1 (Writing) | CC.2 (Reprod) | CC.3 (Claim) | CC.5 (Code) | CC.6 (Publish) | CC.7 (Git) |
|:------|:---------------|:--------------|:-------------|:------------|:---------------|:-----------|
| 00 (Scope lock) | — | — | Required | — | — | Required |
| 01 (Repo settle) | — | — | — | Required | — | Required |
| 02 (Thesis archive) | — | — | — | — | — | Required |
| 03 (Novelty audit) | — | — | Required | — | — | Required |
| 04 (Gate experiment) | — | Required | Required | Required | — | Required |
| 05 (Claim lock) | — | — | Required | — | — | Required |
| 06 (Front half) | Required | — | Required | — | — | Required |
| 07 (Empirical sections) | Required | Required | Required | — | — | Required |
| 08 (Epistemology pass) | Required | — | Required | — | — | Required |
| 09 (Notation/format/build) | Required | — | — | — | Required | Required |
| 10 (Companion) | Required | — | — | — | Required | Required |
| 11 (Verification) | Required | Required | Required | Required | Required | Required |
| 12 (Release/submit) | — | — | — | — | Required | Required |
| 13 (Post-submission) | — | — | — | — | — | Required |

---

## Deltas from the archived monograph `cross-cutting.md`

| Monograph rule | Disposition | Rationale |
|:---------------|:------------|:----------|
| CC.1.1–1.6 (shared monograph preamble, shared bib, chapter prose) | **Adapted** | Single standalone paper + companion, not chapters; shared preamble/bib retained at `paper/` level |
| CC.3.1–3.3 (PRISMA-ScR / PRISMA 2020 / PRISMA-MA) | **Dropped** | No review/meta-analysis content in the narrow paper |
| CC.3.4 (σ operational specification) | **Retained** (CC.3.3) | Directly addresses the JAIR "unclear notation" ground |
| CC.3.7 (LLM-assisted pipeline disclosure) | **Dropped** | No screening/extraction pipeline in the narrow paper |
| CC.4 (monograph coherence: thesis-statement citations, chapter cross-references, shared glossary/notation registry, bookends) | **Dropped** | Monograph-only; replaced by claim separation (CC.3.2) and the claim-status table (CC.3.7) |
| CC.4.8 (competing-hypotheses section) | **Retained** (CC.3.8) | Now required in §2 — the "this is just grokking" objection is the top reviewer risk |
| CC.6 (publication readiness, was Phase-12-only) | **Elevated** | Now a standing requirement: the paper IS the deliverable, not an extraction byproduct |
| CC.7.2 (branch prefixes, PR-based) | **Dropped** (solo workflow) | Single-author repo, commits directly to `main`; CC.7.1 format retained |

The claim-evidence ledger discipline (monograph CC.4.9) is retained in adapted form as `paper/planning/claim-ledger.md` (Phase 00 output) — every result tagged keep-in-narrow / move-to-companion / cut / defer, and re-checked at Phase 11.
