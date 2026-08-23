# Phase 12 — Submission, Archival & Paper 03 Seeding

**RPF v2.0:** Git tag `p12-submitted` + `v1.0-submitted` (freeze) · Duration 1d · GPU 0 · RACI: Agent **R** (prepare) / PI **R** (execute submission) · Abort: portal error >3 → manual fallback · Acceptance: freeze tag + locked branch, post-mortem ADR with ≥3 standards change proposals, v2 roadmap mapping every `defer` row · *Pending.*

**Phase ID:** P12  
**Phase Title:** OpenReview Submission Execution, Git Release Tagging, Post-Mortem ADR, and Paper 03 Roadmap Seeding  
**Status:** Pending  
**Duration:** 1 Day  
**Dependencies:** P11  
**Executor:** Agent (70%) / Human-Gate (30%)  
**Deliverables:** OpenReview submission receipt, `paper02/decisions/ADR-012_post_mortem.md`, `paper02/planning/roadmap_v3_draft.md`, closed `paper02/planning/ledger.md`

---

## 1. Purpose & Scope
Formally execute the submission of Paper 02 on OpenReview (NeurIPS / ICLR track), tag and freeze the release branch, compile the final post-mortem ADR, close the scope ledger, and seed the research roadmap for Paper 03 (*Autonomous Schema Induction & Continual Reasoning*).

---

## 2. Exhaustive Tasks & Subtasks

### Task 12.1: OpenReview Submission Execution & Logging
1. **Submission Steps (Executed by PI with Agent Verification):**
   - Upload camera-ready PDF and anonymized supplementary ZIP (`paper02-code-data.zip`) to OpenReview.
   - Enter title, author list, abstract ($\le 250$ words), keywords, and subject areas (*Learning Theory, Representation Learning, Compositionality*).
2. **Log Submission Metadata:**
   - Record forum URL, paper ID, submission timestamp, and SHA-256 hash of submitted PDF in `paper02/planning/submission_receipt.md`.

### Task 12.2: Git Release Tagging & Branch Freeze
1. **Tag Versioned Release:**
   - Create annotated Git tag:
     ```bash
     git tag -a v2.0-paper02-submitted -m "Paper 02 submitted to OpenReview [P12][Release][INIT]"
     ```
2. **Freeze Directory Permissions:**
   - Set read-only flags on `paper02/data/` and `paper02/writing/` to prevent post-submission drift.

### Task 12.3: Comprehensive Post-Mortem ADR
1. Write and commit `paper02/decisions/ADR-012_post_mortem.md`:
   - Evaluate effectiveness of the RPF v1.0.0 framework (15 phases, CC.N.M rules, Mechanism Gate).
   - Document computational performance of JAX/Diffrax continuous solvers vs. discrete PyTorch sweeps.
   - Document unexpected empirical findings (e.g., sharpness interaction at $\lambda_{\text{crit}}$).
   - Document reviewer feedback preparedness and rebuttal strategy.

### Task 12.4: Seed Paper 03 Roadmap (`Autonomous Schema Induction`)
1. Draft and commit `paper02/planning/roadmap_v3_draft.md`:
   - **Title:** *Autonomous Schema Induction: Self-Supervised Invariant Extraction and Continual Reasoning*
   - **Core Research Question:** *How can a neural agent discover primitive substitutions and structural invariances autonomously without handcrafted $\mathcal{L}_{\text{comp}}$ supervision, and preserve them across sequential task domains?*
   - **Phase 03 Gate for Paper 03:** Empirical validation of contrastive mutual-information clustering for zero-supervision grammar discovery.

### Task 12.5: Claims Ledger Final Closure
1. Close all entries in `paper02/planning/ledger.md`:
   - Verify that all claims are tagged `shipped` or `deferred-to-v3`.
   - Freeze `ledger.md`.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator submits manuscript on OpenReview, confirms receipt, and approves the Paper 03 draft roadmap.

---

## 4. Machine-Checkable Exit Criteria
- [ ] `paper02/planning/submission_receipt.md` exists with OpenReview forum URL and PDF hash.
- [ ] Git tag `v2.0-paper02-submitted` verified.
- [ ] `paper02/decisions/ADR-012_post_mortem.md` committed.
- [ ] `paper02/planning/roadmap_v3_draft.md` committed.
- [ ] `paper02/planning/ledger.md` 100% closed and frozen.
- [ ] `[HUMAN-GATE]` Submission signed off.

---

## 5. Deliverables & Artifacts
- Submission receipt: `paper02/planning/submission_receipt.md`
- Git release tag: `v2.0-paper02-submitted`
- Post-mortem record: `paper02/decisions/ADR-012_post_mortem.md`
- Next-paper roadmap: `paper02/planning/roadmap_v3_draft.md`
