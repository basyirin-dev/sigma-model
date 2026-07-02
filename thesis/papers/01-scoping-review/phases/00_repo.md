# Phase 0 — Repo & LaTeX Setup

**Duration**: 1 week (Month 1)
**Deadline**: 2026-07-09
**Dependencies**: Thesis repo exists (root-level `thesis/` structure)
**Output**: Paper 01 directory with compilable LaTeX skeleton and bibliography

---

### Task 0.1: Paper Directory Structure

- [ ] 0.1.1: Ensure `thesis/papers/01-scoping-review/` exists with `phases/` and `research/` subdirectories
- [ ] 0.1.2: Create `manuscript/` directory for LaTeX source
- [ ] 0.1.3: Create `figures/` directory for manuscript figures
- [ ] 0.1.4: Satisfy CC.5.1 — initial commit with phase structure

### Task 0.2: LaTeX Template Initialization

- [ ] 0.2.1: Copy thesis preamble (`thesis/preamble.tex`) or create paper-specific preamble
- [ ] 0.2.2: Create `manuscript.tex` with section structure:
  - `\section{Introduction}`
  - `\section{Background}`
  - `\section{Methods}`
  - `\section{Results}`
  - `\section{Discussion}`
  - `\section{Conclusion}`
- [ ] 0.2.3: Verify compilation: `make pdf` from `paper/` or `thesis/papers/01-scoping-review/manuscript/`
- [ ] 0.2.4: Add structured abstract template (Background, Methods, Results, Conclusions)
- [ ] 0.2.5: Set up `\todo` or `\comment` macros for inline notes during drafting
- [ ] 0.2.6: Satisfy CC.2.2 — consistent formatting with thesis preamble

### Task 0.3: Bibliography Setup

- [ ] 0.3.1: Add Paper 01 entries to shared `thesis/bibliography.bib`
- [ ] 0.3.2: Configure `biblatex` or `natbib` with target venue style (ACM for *Computing Surveys*)
- [ ] 0.3.3: Test citation: `\cite{key}` renders correctly in compiled PDF
- [ ] 0.3.4: Add `bibliography.bib` path to paper's local `manuscript.tex`

### Task 0.4: PRISMA-ScR Template

- [ ] 0.4.1: Download PRISMA-ScR 22-item checklist PDF/TeX template
- [ ] 0.4.2: Add PRISMA flow diagram placeholder (to be filled in Phase 3)
- [ ] 0.4.3: Create empty PRISMA checklist appendix in `manuscript.tex`
- [ ] 0.4.4: Satisfy CC.1.1 — PRISMA-ScR checklist template placed in appendix

### Task 0.5: Local Tooling

- [ ] 0.5.1: Create `paper-01.Makefile` or extend root `Makefile` for per-paper builds
- [ ] 0.5.2: Verify `ruff check` passes on any existing code references
- [ ] 0.5.3: Satisfy CC.5.1 — initial commit with "Phase 0 complete"

---

**Phase 0 Exit Criteria**:
- [ ] `manuscript.tex` compiles with zero errors (via `latexmk -pdf`)
- [ ] Bibliography renders with at least one test citation
- [ ] PRISMA-ScR checklist appendix exists
- [ ] CC.2.2, CC.5.1 satisfied
