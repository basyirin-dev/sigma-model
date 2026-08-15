# Phase 0.5 — Scope Lock: Claim Ledger + Roadmap

**Duration**: 1 day (complete)
**Deadline**: 2026-08-16 ✅
**Dependencies**: Phase 00
**Output**: `paper/planning/claim-ledger.md`, `paper/planning/roadmap.md`
**Executor**: Agent
**Status**: ✅ Done — commit `438b2c5`

## Purpose

Enumerate every formal result, prediction, and framework component of the current
manuscript and tag each with a disposition (keep-in-narrow / move-to-companion / cut /
defer / decide-at-P05). This ledger is the single source of truth that drives phases
06–10, and is re-checked at Phase 11.

## Tasks & subtasks (as executed)

1. **Inventory mathematical results** — Propositions 3.1–4.5, Theorems 4.1–4.2, Lemma 4.2
   (claim markers C-021…C-038 in `paper/manuscript.tex`)
   - Tag each: core bifurcation results → keep; proxy/estimator results (3.6–3.7) → companion;
     faculty-validity/algebra → companion; noise/stability → cut or companion
2. **Inventory predictions** — Predictions 1–9, Hypotheses 6.1–6.3, Meta-Prediction M1
   - Prediction 9 (Phase-2 entry inflection) → keep (flagship); all others → companion
3. **Inventory framework components** — §§3.1–8 + appendices (three dimensions, proxy
   architecture, Ψ_A, D*, phases 0–5, benchmark protocol, SDE/IMEX)
4. **Inventory empirical numbers** — baseline OOD 44.5 ± 4.7, coupled 94–97, d = 9.08/7.57
   → re-verify at P04 (reproduction)
5. **List claims to delete outright** — "origin" language, "convert every depth-accumulating
   agent…", "know more, understand better", unqualified "bifurcation phenomenon, not a
   capacity or data problem", "necessary and sufficient" Phase-2 phrasing
6. **Write roadmap.md** — deliverables D1–D12, per-phase exit criteria, six non-negotiables

## Expected outputs

- `paper/planning/claim-ledger.md` (sections A–E: results, predictions, components, empirical, deletions)
- `paper/planning/roadmap.md` (phase roadmap with exit criteria)

## Decisions

- Claim-level disposition defaults chosen; three items flagged `decide` for P05:
  Prop 3.3 (Fenichel), Prediction 6, SDE/IMEX appendices

## Exit criteria (met)

- Ledger + roadmap committed (438b2c5) ✅
