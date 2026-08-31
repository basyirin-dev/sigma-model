# Gate Result Record & Human Decision Log (RPF v2.0)

This document records the formal evaluations and decisions at major human-in-the-loop and automated research gates.

---

## Gate Summary Table

| Gate ID | Target Phase | Trigger / Milestone | Evaluator | Decision Verdict | Execution Timestamp | ADR Reference |
|---|---|---|---|---|---|---|
| `HG-01` | `P03` | Preregistration and Statistical Protocol Sign-off | Lead Investigator | PENDING | -- | `decisions/human-gates/P03_HG.md` |
| `HG-02` | `P08` | Manuscript First Complete Draft & Figure Review | Lead Investigator | PENDING | -- | `decisions/human-gates/P08_HG.md` |
| `HG-03` | `P11` | Clean-Room Verification & Final Submission Bundle | Lead Investigator | PENDING | -- | `decisions/human-gates/P11_HG.md` |

---

## Historical Gate Evaluations

### Gate HG-01: Preregistration Sign-Off (P03)
- **Status:** Pending Entry
- **Evaluation Criteria:** Preregistered hypotheses in `planning/preregistration.md` are mutually exclusive, statistically powered ($1-\beta \ge 0.90$ at $\alpha=0.01$), and bound to explicit falsification criteria.

### Gate HG-02: Manuscript Draft Sign-Off (P08)
- **Status:** Pending Entry
- **Evaluation Criteria:** All manuscript claims match `planning/ledger.md`; zero orphan claims; figure generation code is 100% reproducible.

### Gate HG-03: Final Submission Sign-Off (P11)
- **Status:** Pending Entry
- **Evaluation Criteria:** Clean-room Docker build succeeds; all SHA-256 checksums match; double-blind requirements satisfied.
