# ADR 0003: Claim-to-Evidence Tracking System

**Date:** 2026-03-30  
**Status:** Accepted  
**Author:** Infrastructure Setup (Phase 0)

## Context

Quantitative claims in the paper had no traceability to experimental evidence. 19 cells in Tables 12.2 and 12.3 contain `[INSERT]` placeholders. No mechanism existed to determine whether a given claim was supported, pending, or falsified, or which config file and commit hash produced the supporting data.

## Decision

Implement a two-part tracking system:

1. **Inline anchors** — `<!-- CLAIM:C-001 -->` comment tokens placed directly after each quantitative claim in `paper.md`. Invisible in rendered output; machine-extractable with `grep '<!-- CLAIM:' paper.md`.

2. **Claims registry** — `docs/claims-registry.md` is a structured table mapping every Claim ID to:
   - Line numbers in `paper.md`
   - Claim text
   - Status (DESIGNED / PENDING / COLLECTED / FALSIFIED)
   - Config file path
   - Experiment run ID
   - Commit hash
   - Notebook cell reference

A CI script verifies the bijection: every anchor has a registry entry and every entry has an anchor.

## Consequences

- Any researcher can determine the evidential status of any claim by reading the registry
- Kaggle results map directly to claim IDs
- Future paper revisions can cleanly distinguish confirmed vs. pending claims
- The registry serves as a pre-registration document for the pending experiments
