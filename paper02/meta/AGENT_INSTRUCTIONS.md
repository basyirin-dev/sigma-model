# Paper 02 — Agent Instructions & Operating Manual

> **Framework:** The Research Planning Framework (RPF v1.0.0)  
> **Execution Ratio:** 90% Autonomous Agent / 10% Human-in-the-Loop  
> **Governance:** Zero writing without committed evidence. Strict compliance with `paper02/planning/standards.md`.

---

## 1. Operating Rules & Guardrails

1. **Activate Virtual Environment:**
   Always ensure `hbar_env` is active:
   ```bash
   source hbar_env/bin/activate
   ```
2. **Evidence Gates Ambition (RPF Principle 1):**
   Under no circumstances should the agent draft manuscript sections (P08) or run multi-benchmark sweeps (P06) before `paper02/planning/gate-result.md` has been committed with an approved **PASS** verdict.
3. **Artifact-Gated Commits:**
   Every technical decision must produce an ADR in `paper02/decisions/`.
   Every claim must trace to a row in `paper02/planning/ledger.md`.
4. **Git Commit Format (CC.6.1):**
   ```
   [Tag][Scope][Δ] Description
   ```
   - **Tag:** `P00` | `P0.5` | `PCC` | `P01` | `P02` | `P03` | `P04` | `P05` | `P06` | `P07` | `P08` | `P09` | `P10` | `P11` | `P12` | `ADR` | `META` | `FIX`
   - **Scope:** `Roadmap` | `Standards` | `Ledger` | `Gate` | `Impl` | `Analysis` | `Writing` | `Packaging`
   - **$\Delta$:** `Δ` (modifications) | `INIT` (initial creation) | `HOTFIX` (critical bugfix)

---

## 2. Directory Governance

| Path | Purpose & Rules |
|---|---|
| `paper02/planning/` | Phase briefs, temporal roadmap, cross-cutting standards, claim ledger. Immutable structure. |
| `paper02/decisions/` | Numbered Architecture Decision Records (`ADR-00X_...`). |
| `paper02/src/` | Pure Python/JAX/PyTorch implementation modules. All custom numerical kernels must have unit tests. |
| `paper02/data/raw/` | Raw tensor outputs from experimental runs. **Immutable after P06 data generation.** |
| `paper02/data/processed/` | Derived tidy parquet/csv files generated exclusively by idempotent scripts. |
| `paper02/writing/` | LaTeX source files for the manuscript, TikZ vector figures, and supplementary materials. |
| `paper02/meta/` | Operational guidelines, environment specifications, and project README. |

---

## 3. Human-Gate Escalation Protocol

Whenever a phase hits a marked `[HUMAN-GATE]`, the agent MUST pause execution, summarize the findings/artifacts, and request user review.
The 14 Human-Gate checkpoints:
- **P00:** Repository visibility & compute environments.
- **P0.5:** Inherited evidence completeness.
- **PCC:** Standards registry approval.
- **P01:** Gap novelty confirmation.
- **P02:** Hypothesis & gate target approval.
- **P03:** PROCEED / RE-GATE / ABORT directive.
- **P04:** Full experimental protocol sign-off.
- **P06:** Numerical anomaly review.
- **P07:** Scientific interpretation sign-off.
- **P08:** Manuscript narrative & tone review.
- **P09:** Final revision approval.
- **P10:** Final GO / NO-GO directive.
- **P11:** Submission package approval.
- **P12:** Final OpenReview submission execution.

---

## 4. Quality & Build Verification

- **Linting:** `ruff check paper02/src/`
- **Unit Tests:** `pytest paper02/tests/`
- **Manuscript Build:** `make -C paper02 pdf` (Must yield 0 errors, 0 undefined citations).
