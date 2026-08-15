# Phase 12 — arXiv Release & TMLR Submission Package

**Duration**: 2–3 days
**Deadline**: after P11
**Dependencies**: P11 verification
**Output**: arXiv bundle + TMLR submission package
**Executor**: Agent (prep) + **user** (uploads/submits)

## Purpose

Produce a ready-to-upload arXiv bundle and a complete TMLR submission package,
including the narrative that addresses the JAIR desk rejection directly.

## Tasks & subtasks

1. **arXiv bundle** — `make arxiv` (update `paper/Makefile` at P09):
   - `manuscript.tex` + `manuscript.bbl` + figures + `tmlr.sty` + companion
     (NO `jair.cls`); verify the bundle compiles standalone from a clean directory
2. **arXiv metadata** — title (P08-finalised), ≤250-word abstract, subjects
   `cs.LG` / `cs.NE`, companion as linked upload; author name/ORCID confirmed (CC.6.6)
3. **TMLR package** — `paper/submission/`:
   - Anonymized PDF per TMLR guidelines; main-text length check vs blueprint
   - **Cover letter**: addresses the JAIR desk-rejection (2026-07-15) and the editor's
     "a series of small steps" recommendation — this paper is that small step; the
     extended framework is the arXiv companion
   - **"How the paper changed" summary** for reviewers (one page): scope narrowed from a
     5-faculty framework to a two-variable mechanism; phenomenological framing;
     claim-status table; the discriminating experiment
4. **Commit** `[I][W][Δ]` submission artifacts (bundle kept out of git if large;
   the `.tex`/`.bib` sources are tracked)

## Expected outputs

- `arxiv-submission/` bundle (verified standalone-compiling)
- `paper/submission/` cover letter + reviewer summary + checklist

## Decisions

- Post to arXiv after the gate experiment is integrated (never before — no major-revision
  arXiv version)
- No workshop detour (user decision): arXiv → direct TMLR

## Exit criteria

- Bundle compiles standalone; submission package complete; user has upload-ready files
