# Phase 10 — Independent Verification & Three-Way Binding

**RPF v2.0:** Git tag `p10-verified` · Duration 1–2d · GPU 2 · RACI: Agent **R** / PI **A** (GO/NO-GO; fallback NO-GO) · Abort: any non-negotiable FAIL or reproducibility failure → halt · Acceptance: `verification-report.md` + `reproducibility-report.md` (clean-room rebuild, hash match), 0 ledger↔artifact discrepancies · *Pending.*

**Phase ID:** P10  
**Phase Title:** Structurally Independent Verification, Three-Way Binding Audit (Ledger ↔ Code ↔ Manuscript), and Non-Negotiables Verification  
**Status:** Pending  
**Duration:** 1–2 Days  
**Dependencies:** P09  
**Executor:** Agent (90%) / Human-Gate (10%)  
**Deliverables:** `paper/planning/verification-report.md`, `paper/decisions/ADR-010_verification_signoff.md`

---

## 1. Purpose & Scope
Execute a structurally independent, end-to-end verification pass that re-executes all computational scripts from clean state, audits the non-negotiables, verifies the three-way binding between **Ledger ↔ Code/Data ↔ Manuscript**, and emits the final Verification Report governing external submission.

---

## 2. Exhaustive Tasks & Subtasks

### Task 10.1: Independent Computational Re-Execution & Spot-Check
1. **Clean Re-Execution from Scratch:**
   - Execute `make clean` in `paper/`.
   - Run reproduction script `paper/src/analysis/reproduce_all_figures.py` asserting that all 5 figures in `writing/figures/` are generated from `data/processed/` without error.
2. **Numerical Value Exactness Check:**
   - Script automated extraction of all numbers reported in `writing/manuscript.tex` (e.g., means, 95% CIs, $p$-values, $t$-statistics, $\hat{\lambda}_{\text{crit}}$).
   - Assert exact match ($< 10^{-4}$ tolerance) against raw data in `data/processed/pairwise_welch_tost.csv` and `inflection_breakpoints.csv`.

### Task 10.2: Non-Negotiables Verification Checklist
Audit and verify each of the 6 non-negotiable rules from `paper/planning/roadmap.md`:
- [ ] **NN-1:** No downstream work began before P03 Gate verdict was committed with a PASS.
- [ ] **NN-2:** Every computational result is reproducible from pinned code and explicit seeds.
- [ ] **NN-3:** Every manuscript claim traces directly to `planning/ledger.md` or a cited reference.
- [ ] **NN-4:** Raw data in `data/raw/` is write-protected and identical to original generation hashes.
- [ ] **NN-5:** Verification pass was executed independently.
- [ ] **NN-6:** Project concludes by drafting and committing the Paper 03 roadmap.

### Task 10.3: Three-Way Binding Audit (Ledger ↔ Code ↔ Manuscript)
1. Verify that every mathematical theorem in the manuscript is backed by a formal proof in Appendix B.
2. Verify that every empirical table in the manuscript matches the data logs.
3. Verify that every claim in `planning/ledger.md` is tagged `shipped` or `deferred-to-v3`.

### Task 10.4: Verification Report Emission
1. Compile and commit `paper/planning/verification-report.md`:
   - Summary of computational spot-checks (100% PASS).
   - Non-negotiables audit (6/6 PASS).
   - Final verdict: **READY FOR SUBMISSION / NOT READY (list blockers)**.
2. Emit `paper/decisions/ADR-010_verification_signoff.md`.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator reads `planning/verification-report.md` and issues the formal **GO / NO-GO** directive for pre-submission packaging.

---

## 4. Machine-Checkable Exit Criteria
- [ ] `paper/planning/verification-report.md` committed with verdict = **READY FOR SUBMISSION**.
- [ ] All 6 non-negotiables marked PASS.
- [ ] 100% of computational re-execution scripts exit code 0.
- [ ] `paper/decisions/ADR-010_verification_signoff.md` committed.
- [ ] `[HUMAN-GATE]` GO directive received.

---

## 5. Deliverables & Artifacts
- Verification report: `paper/planning/verification-report.md`
- Decision record: `paper/decisions/ADR-010_verification_signoff.md`
