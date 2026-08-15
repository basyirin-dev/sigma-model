# Phase 11 — Verification & Internal Review

**Duration**: 2–3 days
**Deadline**: after P09–P10
**Dependencies**: P09 manuscript, P10 companion, P00 ledger, P03 audit
**Output**: `paper/planning/verification-report.md`
**Executor**: Agent + user stranger-test

## Purpose

Catch defects before arXiv/TMLR: self-containment, claim-vs-evidence consistency,
notation consistency, and a clean build — plus a fresh literature re-scan (P03 residual
risk) and an independent review of the diff.

## Tasks & subtasks

1. **Stranger-test / self-containment audit** — a reader with only the narrow paper can
   follow every claim; map each §2–§13 paragraph to its supporting evidence
   (one-line table in the report)
2. **Claim audit vs ledger** — every abstract/intro claim has evidence; nothing exceeds
   the locked claim level; no ledger-`cut` item reintroduced
3. **Notation-consistency sweep** — every symbol defined before first use; no unused
   notation; no symbol collisions with the companion
4. **Rebuild & page budget** — `make pdf`: 0 errors, 0 undefined references; page count
   within blueprint targets (both narrow paper and companion)
5. **Literature re-scan** — refresh the P03 audit against 2025–26 grokking/phase-transition
   work (fast arXiv search); confirm no equivalent order-parameter claim emerged
6. **Independent review** — run the built-in `review` skill on the manuscript/companion
   diff for correctness/robustness issues; action or record each finding
7. **Write verification-report.md**; commit

## Expected outputs

- `paper/planning/verification-report.md` (paragraph→evidence map, claim audit, notation
  sweep, build record, re-scan note, review findings)

## Decisions

- Any open blocker → P06–P09 re-entry before P12; no submission with open blockers

## Exit criteria

- Verification report committed; no open blockers; user sign-off on readiness
