# Paper 06 v2 — Phase Documents (Thesis-Style)

This directory mirrors the thesis paper-phase convention (`archive/thesis/chapters/XX/phases/`):
one numbered phase document per phase, each with Duration / Deadline / Dependencies /
Output / Executor, a task breakdown with subtasks, expected outputs, decisions, and exit
criteria. The pipeline implements the approved decision (2026-08-16):

> **One narrow σ-Trap paper for submission (TMLR) + a full arXiv companion**,
> experiment-gated (P04), arXiv → direct TMLR. Thesis monograph and AGI-safety
> pipeline archived. See `../roadmap.md` (phase list + exit criteria) and
> `../claim-ledger.md` (result disposition tags).

## Pipeline map

| # | Phase doc | Title | Status (2026-08-16) |
|:--|:----------|:------|:---------------------|
| 00 | `00_cross_cutting.md` | Cross-cutting standards | ✅ Done (`paper/planning/cross-cutting.md`, commit 438b2c5) |
| 0.5 | `00_5_scope_lock.md` | Scope lock: claim ledger + roadmap | ✅ Done (commit 438b2c5) |
| 01 | `01_repo_settlement.md` | Repo settlement & cleanup | ✅ Done (commit 2c26fae) |
| 02 | `02_thesis_archive.md` | Thesis archive & re-centering | ✅ Done (commit 9772494) |
| 03 | `03_novelty_audit.md` | Novelty audit & literature positioning | ✅ Done (commit 5bfeeec) |
| 04 | `04_mechanism_gate.md` | Mechanism-gate experiment | ⬜ Pending — user runs on Kaggle |
| 05 | `05_claim_lock_blueprint.md` | Claim-level lock & paper blueprint | ⬜ Pending |
| 06 | `06_front_half_rewrite.md` | Narrow manuscript, front half (§§1–3, 7, 9) | ⬜ Pending |
| 07 | `07_empirical_rebuild.md` | Empirical sections rebuild (§§10–13) | ⬜ Pending |
| 08 | `08_epistemology_framing.md` | Epistemology & framing pass | ⬜ Pending |
| 09 | `09_notation_format_build.md` | Notation, proofs, format, build | ⬜ Pending |
| 10 | `10_companion_report.md` | arXiv companion technical report | ⬜ Pending |
| 11 | `11_verification_review.md` | Verification & internal review | ⬜ Pending |
| 12 | `12_release_submit.md` | arXiv release & TMLR submission package | ⬜ Pending |
| 13 | `13_post_submission.md` | Post-submission docs & follow-up roadmap | ⬜ Pending |
| 99 | `99_finale.md` | Pipeline closeout | ⬜ Pending |

## How to read a phase doc

Each pending phase doc contains: **Purpose** (one paragraph), **Duration / Deadline /
Dependencies / Output / Executor** (metadata block), **Tasks** (numbered, each with
subtasks), **Expected outputs**, **Decisions** (the forks that gate the phase), and
**Exit criteria** (verifiable conditions, re-checked at P11). Executor labels:
`agent` = the coding agent can execute; `user` = requires the human (compute, venue
accounts, final sign-off); `user+agent` = user provides resource, agent analyses.

## Status legend

- ✅ Done — phase executed and committed (commit hash in the table)
- ⬜ Pending — phase specified below; not started
- 🔶 In progress — partially done
