# Phase 00 — Repo & LaTeX Setup

**Duration**: 1 week (Month 1)
**Deadline**: 2026-07-10
**Dependencies**: Thesis repo exists (root-level `thesis/` structure), Paper 01 templates available as reference
**Output**: Paper 02 directory with compilable LaTeX skeleton and bibliography

---

### Task 0.1: Paper Directory Structure

- [x] 0.1.1: Ensure `thesis/papers/02-systematic-review/` exists with `phases/`, `research/`, `manuscript/`, `figures/` subdirectories
- [x] 0.1.2: Create `research/search-results/` subdirectory for raw search exports
- [x] 0.1.3: Create `research/screening-decisions/` subdirectory for screening logs
- [x] 0.1.4: Create `research/analysis/` subdirectory for meta-analysis scripts and outputs
- [x] 0.1.5: Satisfy CC.5.1 — initial commit with phase structure

### Task 0.2: LaTeX Template Initialization

- [x] 0.2.1: Create paper-specific preamble (`manuscript/preamble.tex`) adapted from Paper 01 but referencing PRISMA 2020 checklist instead of PRISMA-ScR
- [x] 0.2.2: Create `manuscript.tex` with systematic review section structure:
  - `\section{Introduction}`
  - `\section{Methods}`
    - `\subsection{Protocol and Registration}`
    - `\subsection{Eligibility Criteria}`
    - `\subsection{Information Sources}`
    - `\subsection{Search Strategy}`
    - `\subsection{Study Selection}`
    - `\subsection{Data Collection Process}`
    - `\subsection{Data Items}`
    - `\subsection{Risk of Bias Assessment}`
    - `\subsection{Synthesis Methods}`
  - `\section{Results}`
    - `\subsection{Study Selection}`
    - `\subsection{Study Characteristics}`
    - `\subsection{Risk of Bias within Studies}`
    - `\subsection{Results of Individual Studies}`
    - `\subsection{Results of Syntheses}`
  - `\section{Discussion}`
    - `\subsection{Summary of Evidence}`
    - `\subsection{Limitations}`
    - `\subsection{Implications}`
  - `\section{Conclusion}`
- [x] 0.2.3: Verify compilation: `make pdf` from `thesis/papers/02-systematic-review/manuscript/`
- [x] 0.2.4: Add structured abstract template (Background, Methods, Results, Discussion, Registration)
- [x] 0.2.5: Set up `\todo` and `\annote` macros for inline notes during drafting
- [x] 0.2.6: Satisfy CC.2.2 — consistent formatting with thesis preamble

### Task 0.3: Bibliography Setup

- [x] 0.3.1: Add Paper 02 entries to shared `thesis/bibliography.bib`
- [x] 0.3.2: Configure `natbib` with target venue style (Springer *Artificial Intelligence Review* style)
- [x] 0.3.3: Test citation: `\cite{page2021prisma2020}` renders correctly in compiled PDF
- [x] 0.3.4: Add PRISMA 2020 reporting guideline citation to bibliography

### Task 0.4: PRISMA 2020 Template

- [x] 0.4.1: Create PRISMA 2020 27-item checklist LaTeX template
- [x] 0.4.2: Add PRISMA 2020 flow diagram TikZ placeholder (to be filled in Phase 3/4)
- [x] 0.4.3: Add PICO framework template to Methods section (to be filled in Phase 1)
- [x] 0.4.4: Create empty PRISMA 2020 checklist appendix in `manuscript.tex`
- [x] 0.4.5: Satisfy CC.1.1 — PRISMA 2020 checklist template placed in appendix

### Task 0.5: Local Tooling

- [x] 0.5.1: Update root `Makefile` or create paper-local `Makefile` for per-paper builds
- [x] 0.5.2: Verify `ruff check` — no Paper 02 code references; pre-existing errors in `code/sigma_align/` are unrelated
- [x] 0.5.3: Install R or Python packages for meta-analysis if not already present (metafor in R, or meta/statistics in Python)
- [x] 0.5.4: Satisfy CC.5.1 — initial commit with "Phase 00 complete"

---

**Phase 00 Exit Criteria**:
- [x] `manuscript.tex` compiles with zero errors (via `latexmk -pdf`)
- [x] Bibliography renders with at least one test citation
- [x] PRISMA 2020 checklist appendix exists
- [x] PICO template exists in Methods section
- [x] Meta-analysis tooling verified
- [x] CC.1.1, CC.2.2, CC.2.3, CC.5.1 satisfied
