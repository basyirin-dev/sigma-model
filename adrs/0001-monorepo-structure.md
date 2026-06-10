# ADR 0001: Monorepo Structure

**Date:** 2026-03-30  
**Status:** Accepted  
**Author:** Infrastructure Setup (Phase 0)

## Context

The Σ-Model Model V3.0+ repository had grown organically with files in flat directories. Paper source, experiments, and documentation were interleaved. To support maintenance, versioning, and collaboration, a strict monorepo structure was needed.

## Decision

Adopt a six-directory top-level layout:

| Directory | Purpose |
|-----------|---------|
| `/paper` | Canonical paper source (Markdown + LaTeX), version-controlled with Git tags |
| `/code` | Modular Python package (`sigma`), installed via pip, imported by notebooks |
| `/experiments` | Notebooks that import from `/code` and read configs from `configs/` |
| `/docs` | ADRs, lab notebooks, errata logs |
| `/artifacts` | Model cards, datasheets, demo links |
| `/scripts` | Automation scripts (monitoring, CI) |

Existing directories (`hackathon/`, `variants/`, `documentation/`, `arxiv-submission/`) are preserved but the new structure is canonical.

## Consequences

- Paper edits go in `/paper/paper.md`; LaTeX is generated via pandoc
- All hardcoded experiment parameters moved to `/experiments/configs/*.yaml`
- Notebooks become thin orchestration layers importing from `/code/sigma/`
- ADRs provide an auditable decision trail
