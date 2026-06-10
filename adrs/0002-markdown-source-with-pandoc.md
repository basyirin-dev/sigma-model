# ADR 0002: Markdown Source with Pandoc-Generated LaTeX

**Date:** 2026-03-30  
**Status:** Accepted  
**Author:** Infrastructure Setup (Phase 0)

## Context

The paper existed in two forms: `paper/paper.md` (canonical) and `arxiv-submission/manuscript.tex` (LaTeX rendering). Keeping them in sync manually was error-prone. The `.tex` file was in a gitignored directory, making it untracked and unreviewable.

## Decision

1. `paper/paper.md` remains the single source of truth
2. `paper/manuscript.tex` is generated from `paper.md` via pandoc with a custom LaTeX template
3. `paper/Makefile` provides `make tex`, `make pdf`, `make arxiv` targets
4. `arxiv-submission/` remains a build artifact directory for arXiv packaging
5. The pandoc template in `paper/templates/` handles equation cross-references, bibliography, and custom commands

## Consequences

- Single diff-friendly source file for all paper edits
- LaTeX generation is a build step, not a manual sync
- CI can verify that `make tex` produces a consistent `.tex` from `paper.md`
- Custom Lua filters handle claim-extraction and cross-referencing
