# Phase 09 — Notation, Proofs, Format & Build Pipeline

**Duration**: 2–3 days
**Deadline**: after P08
**Dependencies**: P07–P08 draft
**Output**: buildable TMLR-format manuscript (0 errors, 0 undefined refs)
**Executor**: Agent

## Purpose

Make the manuscript technically clean and buildable in TMLR format: pruned notation,
proofs in the appendix, `jair.cls` → `tmlr.sty` switch, stale path fixes, and a verified
build.

## Tasks & subtasks

1. **Prune the Notation Reference appendix** — only symbols actually used in the narrow
   paper (addresses the JAIR "unclear notation" ground directly)
2. **Move full proofs to a proofs appendix** — local existence, forward invariance,
   equilibria, bifurcation; main text states results
3. **Decide SDE/IMEX appendices** (P05 decision): default SDE → companion; IMEX-RK → keep
   compressed as numerical-rigour defence (or companion if space forces it)
4. **Format switch** — `jair.cls` → `tmlr.sty` (already in `paper/`):
   - Remove JAIR-specific preamble: `\documentclass[manuscript,screen]{jair}` → tmlr class,
     `\acmDOI`, `\received`, `\JAIRAE{}`, `\JAIRTrack{}`, `\settopmatter`, `\citestyle`,
     ACM-Reference-Format bibliography style
   - Update `paper/Makefile` (drop `JAIR_CLS` deps; TMLR build), `.gitignore` if needed
5. **Bibliography prune** — remove dead/unused entries; ensure TMLR reference formatting
6. **Fix stale reproducibility paths** — the Reproducibility/Data-Availability statements
   reference root `experiments/`, `scripts/`, `tests/` which now live under `code/` /
   `archive/`; re-point to live locations (and the P04 gate scripts)
7. **Build & verify** — `make pdf`: 0 LaTeX errors, 0 undefined references/citations,
   clean log; page budget within blueprint targets

## Expected outputs

- TMLR-format `paper/manuscript.tex`; updated `paper/Makefile`; pruned bibliography;
  clean build

## Decisions

- Any residual JAIR-format artifacts are removed, not kept "just in case" (the venue
  decision is arXiv → TMLR)

## Exit criteria

- `make pdf` passes with 0 errors / 0 undefined references; format is pure TMLR
