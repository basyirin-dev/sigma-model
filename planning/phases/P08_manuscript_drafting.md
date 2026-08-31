# Phase P08: Manuscript Drafting & Quarto Rendering

## 1. Objective
Draft the complete scientific manuscript (`writing/manuscript/index.qmd`), render publication-ready vector figures, and execute Human Gate 2 (`HG-02`).

## 2. Inputs & Dependencies
- `P07` diagnostic analysis complete.

## 3. Required Deliverables
- Quarto manuscript compiling cleanly to PDF and HTML.
- Programmatically generated figures in `writing/figures/`.
- Updated `writing/plain-language-summary.md`.
- State checkpoint `experiments/agent-state/P08_checkpoint.json`.
- Draft Human Gate 2 review `decisions/human-gates/P08_HG.md`.

## 4. Exit Criteria & Definition of Done
- All text claims mapped 1:1 to `planning/ledger.md`.
- CC.3 claim discipline verified (no unproved universal statements).
- `python scripts/check_phase_exit.py P08` returns `PASS`.
