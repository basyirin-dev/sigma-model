# Human Gate Decision Record — Template (RPF v2.0 §11.3)

**Directory:** `paper02/decisions/human-gates/` — one file per gate decision: `<phase>_<gate-id>.md`. Every `[HUMAN-GATE]` in a phase brief produces a record here (CC.6.5).

| Field | Value |
|-------|-------|
| Phase | *(e.g., P03)* |
| Gate ID | *(e.g., HG-P03-001)* |
| Decision | *(PROCEED / RE-GATE / ABORT / GO / NO-GO / Approved / Revisions Required)* |
| Rationale | *(e.g., gate metric exceeds threshold; secondary metrics consistent)* |
| Date | *YYYY-MM-DD* |
| Decision-maker | *Principal Investigator* |
| Consequences | *(e.g., unlocks P04–P12; binding constraints applied)* |
| Sign-off | *[Digital signature / typed name]* |
| Agent state at gate | *experiments/agent-state/<phase>_checkpoint.json* |

---

## P03 Gate Directive (in use)

| Field | Value |
|-------|-------|
| Phase | P03 |
| Gate ID | HG-P03-001 |
| Decision | [PROCEED / RE-GATE / ABORT] |
| Rationale | *(PI: based on `planning/gate-result.md` verdict and pre-registered criteria)* |
| Date | [YYYY-MM-DD] |
| Decision-maker | Principal Investigator |
| Consequences | PROCEED → unlocks P04–P12 (binding constraints from gate-result §3 apply). RE-GATE → refine resolution, re-run P03. ABORT / PIVOT → halt; reassess hypothesis at P02. |
| Sign-off | [ ] |
| Agent state at gate | `experiments/agent-state/P03_checkpoint.json` |

**SLA:** 48h response; reminder at 24h; fallback at 48h = **RE-GATE** (conservative).
