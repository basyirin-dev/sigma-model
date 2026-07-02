# Phase 0 — Repo & LaTeX Setup

**Duration**: 1 week (Month 1)
**Deadline**: 2026-07-09
**Dependencies**: Thesis repo exists (root-level `thesis/` structure)
**Output**: Paper 01 directory with compilable LaTeX skeleton and bibliography

---

### Task 0.1: Paper Directory Structure

- [x] 0.1.1: Ensure `thesis/papers/01-scoping-review/` exists with `phases/` and `research/` subdirectories
- [x] 0.1.2: Create `manuscript/` directory for LaTeX source
- [x] 0.1.3: Create `figures/` directory for manuscript figures
- [x] 0.1.4: Satisfy CC.5.1 — initial commit with phase structure

### Task 0.2: LaTeX Template Initialization

- [x] 0.2.1: Create paper-specific preamble (`manuscript/preamble.tex`)
- [x] 0.2.2: Create `manuscript.tex` with section structure:
  - `\section{Introduction}`
  - `\section{Background}`
  - `\section{Methods}`
  - `\section{Results}`
  - `\section{Discussion}`
  - `\section{Conclusion}`
- [x] 0.2.3: Verify compilation: `make pdf` from `paper/` or `thesis/papers/01-scoping-review/manuscript/`
- [x] 0.2.4: Add structured abstract template (Background, Methods, Results, Conclusions)
- [x] 0.2.5: Set up `\todo` and `\annote` macros for inline notes during drafting
- [x] 0.2.6: Satisfy CC.2.2 — consistent formatting with thesis preamble

### Task 0.3: Bibliography Setup

- [x] 0.3.1: Add Paper 01 entries to shared `thesis/bibliography.bib`
- [x] 0.3.2: Configure `natbib` with target venue style (ACM for *Computing Surveys*)
- [x] 0.3.3: Test citation: `\cite{tricco2018prismascr}` renders correctly in compiled PDF
- [x] 0.3.4: Switch `bibliography.bib` path to thesis-level shared bib

### Task 0.4: PRISMA-ScR Template

- [x] 0.4.1: Create PRISMA-ScR 22-item checklist LaTeX template
- [x] 0.4.2: Add PRISMA flow diagram TikZ placeholder (to be filled in Phase 3)
- [x] 0.4.3: Create empty PRISMA checklist appendix in `manuscript.tex`
- [x] 0.4.4: Satisfy CC.1.1 — PRISMA-ScR checklist template placed in appendix

### Task 0.5: Local Tooling

- [x] 0.5.1: Create root `Makefile` for per-paper builds
- [x] 0.5.2: Verify `ruff check` — no Paper 01 code references; 26 pre-existing errors in `code/sigma_align/` (unrelated)
- [x] 0.5.3: Satisfy CC.5.1 — initial commit with "Phase 0 complete"

---

**Phase 0 Exit Criteria**:
- [x] `manuscript.tex` compiles with zero errors (via `latexmk -pdf`)
- [x] Bibliography renders with at least one test citation
- [x] PRISMA-ScR checklist appendix exists
- [x] CC.2.2, CC.5.1 satisfied
