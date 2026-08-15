# Phase 00 — Cross-Cutting Standards (Standalone Paper)

**Duration**: 1 day (complete)
**Deadline**: 2026-08-16 ✅
**Dependencies**: None
**Output**: `paper/planning/cross-cutting.md`
**Executor**: Agent
**Status**: ✅ Done — commit `438b2c5`

## Purpose

Adapt the archived monograph standards (`archive/thesis/cross-cutting.md`, CC.1–CC.8) to
a standalone paper, explicitly dropping monograph-only rules and recording the deltas so
the paper pipeline has a self-contained compliance matrix.

## Tasks & subtasks (as executed)

1. **Adapt standards CC.1–CC.8 to the standalone paper**
   - Keep CC.1 (writing/formatting, TMLR format), CC.2 (reproducibility, seeds + YAML configs),
     CC.3 (methodology/claim discipline), CC.5 (code quality), CC.6 (publication readiness),
     CC.7 (git hygiene) — adapted wording
   - Drop CC.4 (monograph coherence: thesis citations, chapter cross-refs, shared glossary)
   - Drop PRISMA rules (CC.3.1–3.3) — no review content in the narrow paper
   - Add CC.3.x: phenomenological-model discipline, three-layer claim separation, circularity
     statement, claim-status table, competing-hypotheses requirement
2. **Record deltas** in an explicit table (rule → disposition → rationale)
3. **Exit criteria** in `../roadmap.md`; commit

## Expected outputs

- `paper/planning/cross-cutting.md` — standards + delta table
- `paper/planning/roadmap.md` — deliverable list D1–D12, per-phase exit criteria P00–P13,
  six non-negotiables (self-containment, no "SGD creates the trap" claim, mechanism-level
  title, foundational hypothesis only as research programme, circularity stated, per-seed
  reporting)

## Decisions

- TMLR format chosen as the build target (desk-rejection analysis + venue-fit consensus)
- Scope tag for commits narrowed to L(LaTeX)/C(Code)/W(Workflow) — no T(Thesis)

## Exit criteria (met)

- cross-cutting.md + claim-ledger.md + roadmap.md committed (438b2c5) ✅
