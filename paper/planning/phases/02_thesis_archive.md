# Phase 02 — Thesis Archive & Project Re-centering

**Duration**: 1 day (complete)
**Deadline**: 2026-08-16 ✅
**Dependencies**: Phase 01
**Output**: `archive/thesis/`, `archive/Σ-Align/`; docs re-centered on the paper
**Executor**: Agent
**Status**: ✅ Done — commit `9772494`

## Purpose

Remove the thesis monograph and the AGI-safety decision pipeline from the active
workspace (reversibly) and re-center all project documentation on the σ-Trap paper.

## Tasks & subtasks (as executed)

1. **Move** — `git mv thesis/ archive/thesis/` and `git mv "Σ-Align" "archive/Σ-Align/"`
   (562 staged renames, fully reversible)
2. **Update pointers**
   - `Makefile`: drop `monograph`/`paper01`/`paper02`; `all` → `paper06`
   - `README.md`: re-write (repo structure, status, build commands, new citation)
   - `AGENTS.md`: re-center (thesis commands/architecture removed; scope L/C/W)
   - `.gitignore`: re-point thesis patterns to `archive/thesis/...`
   - `paper/planning/cross-cutting.md`: source reference → `archive/thesis/cross-cutting.md`
3. **Verify build** — `make paper06` → pdflatex 0 errors, 47 pages
4. **Archive stale memory fact** — "Paper 1 & 2 Phase Status" forgotten (papers archived)
5. **Commit** `[R][W][Δ]` archive commit

## Expected outputs

- `archive/thesis/` (monograph, 10 chapters, Papers 01/02, planning docs)
- `archive/Σ-Align/` (MCDAs, desk-rejection response, methodology)
- Re-centered README/AGENTS/Makefile

## Decisions

- Archive (reversible) rather than delete — git history plus working-tree copy
- Project name/package keep the Σ-Model identity; only scope/framing re-centered

## Exit criteria (met)

- `make paper06` builds; no `thesis/` or `Σ-Align/` references in active docs; commit ✅
