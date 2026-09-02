# Phase 13 — Post-submission Revision Loop (Conditional; RPF v2.0)

| Field | Value |
|-------|-------|
| Tasks / Subtasks | **8 / 6** |
| Duration | 5–15 days (reviewer-dependent) |
| Compute | 4 GPU hrs (re-runs if needed) |
| Git tag on close | `p13-revision-N` (per round) |
| Manuscript branch | `revision/round-1`, `revision/round-2`, … (not main) |
| Status | ⬜ Template — triggered by reviewer response |

**RACI:** Agent R / PI A / Reviewers I.

**Tasks:** T1 Receive comments; create branch `revision/round-N` (S1) · T2 Comment triage: claim-changing / analysis / clarity / formatting (S2 triage log) · T3 Claim-changing → impact assessment, new ADR + ledger update (S3 ADR per claim change) · T4 Analysis → re-run affected analyses, update figures, verify reproducibility (S4 re-run logs) · T5 Revise manuscript + update ledger · T6 Re-run P10 verification on changed claims only (S5 targeted verification passes) · T7 Point-by-point response letter (S6 every comment addressed) · T8 Commit to revision branch; tag `p13-revision-N`.

**Human gates:** `[HUMAN-GATE]` PI approves revision and response letter. SLA 72h.

**Exit criteria:** branch created · triage log · ADR for each claim change · re-run logs · targeted verification passes · every comment addressed · revision tagged.

**Transition checklist:** git tag `p13-revision-N` · commit `[P13][Revision][INIT] Round N`.
