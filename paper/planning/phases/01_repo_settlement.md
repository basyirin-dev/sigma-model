# Phase 01 — Repo Settlement & Working-Tree Cleanup

**Duration**: 2 days (complete)
**Deadline**: 2026-08-16 ✅
**Dependencies**: Phase 00
**Output**: Clean committed working tree; `sigma_align` package ruff-clean
**Executor**: Agent
**Status**: ✅ Done — commit `2c26fae`

## Purpose

Reconcile the long-uncommitted working tree (157 deletions, 47 untracked entries,
5 modified files) into one coherent refactor commit so the repo is a consistent base
for the paper pipeline.

## Tasks & subtasks (as executed)

1. **Audit the working tree**
   - 157 tracked deletions: old `code/sigma/`, `artifacts/`, `variants/`, root files
     (CITATION.cff, Dockerfile, HARDWARE.md, checkpoint docs)
   - 47 untracked entries: `code/sigma_align/`, `archive/` contents (incl. 3.3G datasets),
     `Σ-Align/` docs, `LICENSE`, `paper/jair.cls` family, workflow doc, vendor templates
   - 5 modified: `pyproject.toml`, `paper/Makefile`, `paper/bibliography.bib`,
     `paper/manuscript.tex`, `opencode.json`
2. **Verify the `sigma` → `sigma_align` rename** — `ode/equations.py` byte-identical to HEAD;
   entry point `sigma-evaluate` → `sigma_align.monitoring.evaluation:main`; zero stale
   `from sigma.` imports; dropped subpackages (models/, benchmarks/, visualization/)
   preserved in `archive/code/sigma/sigma/`
3. **Lint & smoke** — `ruff check code/sigma_align/` 26 errors → fixed (F401/F841/F541/E741/E501);
   package, config, ODE, solver, evaluation imports OK
4. **Harden `.gitignore`** — exclude `archive/data/` (3.3G), `archive/hackathon/` (2.0G),
   `archive/**/*.pkl`, `archive/**/*.pdf`, `paper/templates/`, `__MACOSX/`, `.reasonix/`,
   `.ruff_cache/`; unstage archived build PDFs (15.2MB → 7.7MB staged)
5. **Commit** `[R][C][Δ]` refactor (322 files; renames detected)

## Expected outputs

- Commit `2c26fae`; `git status` clean; `ruff check` passes

## Decisions

- Archived datasets/build outputs are never committed (CC.7.2)
- Vendor JAIR author kit (`paper/templates/`) gitignored — `jair.cls` family at `paper/` root
  remains tracked until the P09 format switch to TMLR

## Exit criteria (met)

- `git status` clean; ruff passes; rename verified ✅
