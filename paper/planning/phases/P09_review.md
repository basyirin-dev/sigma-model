# Phase 09 — Internal Review, Adversarial Red-Team & Compliance Audit

**RPF v2.0:** Git tag `p09-reviewed` · Duration 2–3d · GPU 0 · RACI: Agent **R** / PI **A** (72h gate) · Abort: >10 unresolved red-team issues after 2 passes → halt · Acceptance: 4 persona reports, reviewer-response draft ≥10 concerns, compliance linter 0 violations, ledger↔manuscript 0 orphans · *Pending.*

**Phase ID:** P09  
**Phase Title:** Adversarial Multi-Reviewer Simulation, Cross-Cutting Standards Compliance Sweep, and Manuscript Hardening  
**Status:** Pending  
**Duration:** 2 Days  
**Dependencies:** P08  
**Executor:** Agent (80%) / Human-Gate (20%)  
**Deliverables:** `paper/planning/phases/P09_review.md` (populated report), revised `paper/writing/manuscript.tex`, `paper/decisions/ADR-009_review_hardening.md`

---

## 1. Purpose & Scope
Conduct an adversarial red-team review simulating top-tier peer review across 3 distinct reviewer archetypes (Theory Purist, Empirical Skeptic, Occam's-Razor Critic). Execute a 100% compliance audit against `standards.md`, run bidirectional ledger synchronization checks, and apply targeted text/proof hardening revisions.

---

## 2. Exhaustive Tasks & Subtasks

### Task 9.1: Multi-Archetype Adversarial Peer Review Simulation
1. **Simulate Reviewer 1 (The Theory Purist):**
   - *Target Weaknesses:* Is the two-subspace orthogonal decomposition overly idealized? What happens under non-linear feature couplings? Does continuous gradient flow faithfully approximate discrete SGD with non-zero learning rates $\eta$?
   - *Audit Target:* Scrutinize the proof of Theorem 1 in Appendix B and adiabatic timescale assumptions in Section 3.
2. **Simulate Reviewer 2 (The Empirical Skeptic):**
   - *Target Weaknesses:* Is the sharp phase boundary an artifact of small 2-layer Transformers? Does $\lambda_{\text{crit}}$ hold on complex natural language splits, or only synthetic grammars? Is there any subtle data leakage in the primitive substitution generator?
   - *Audit Target:* Scrutinize SCAN/COGS/PCFG-SET results in Section 6 and zero-leakage data cards in Appendix D.
3. **Simulate Reviewer 3 (The Occam's-Razor Critic):**
   - *Target Weaknesses:* Why do we need dynamical systems bifurcation terminology? Can't the transition simply be described as an empirical curve fit? Does this framework offer actionable algorithmic control?
   - *Audit Target:* Scrutinize the causal probe framing in Section 1 and model-selection AIC comparisons in Section 4.

### Task 9.2: Cross-Cutting Standards (CC.N.M) Compliance Audit
1. Audit every rule in `paper/planning/standards.md` applicable to P08–P09:
   - CC.1.1–CC.1.3 (Reproducibility & Provenance)
   - CC.2.1–CC.2.3 (Numerical Integrity & TOST Equivalence)
   - CC.3.1–CC.3.3 (Abstract $\le 250$ words, Vector Figures, Tripartite Claims)
   - CC.4.1–CC.4.2 (Data Immutability & Zero-Leakage)
   - CC.5.1–CC.5.2 (Self-Contained & Double-Blind)
   - CC.6.1–CC.6.2 (Conventional Commits & Artifact Integrity)
   - CC.7.1 (Broader Impact Statement)
2. Log all findings in the compliance audit table with status: `Compliant / Actioned / Exception`.

### Task 9.3: Bidirectional Ledger ↔ Manuscript Reconciliation
1. Run automated cross-reference script:
   - Verify that every claim ID in `planning/ledger.md` (`CLM-001` through `CLM-009`) appears in `manuscript.tex` with matching tagged status.
   - Verify that no quantitative empirical numbers appear in `manuscript.tex` without a corresponding ledger entry.

### Task 9.4: Text Hardening & Revision Pass
1. Apply targeted revisions to `writing/manuscript.tex` to resolve all high- and medium-severity items from the red-team review:
   - Add explicit adiabatic timescale bounds in Section 3.4.
   - Strengthen the zero-leakage formal guarantees in Section 4 and Appendix D.
   - Clarify the physical meaning of negative $\lambda_{\text{crit}}$ when $R_0 < 1$.
2. Recompile manuscript and verify 0 warnings.
3. Emit `paper/decisions/ADR-009_review_hardening.md`.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator reviews the red-team evaluation report and approves the text-hardening revisions.

---

## 4. Machine-Checkable Exit Criteria
- [ ] Adversarial review report committed with all 3 reviewer archetypes scored.
- [ ] Compliance audit shows 100% compliance across all CC.N.M rules (0 unresolved violations).
- [ ] Bidirectional Ledger ↔ Manuscript audit passes with 0 orphan items.
- [ ] `paper/decisions/ADR-009_review_hardening.md` committed.
- [ ] `[HUMAN-GATE]` Revisions approved.

---

## 5. Deliverables & Artifacts
- Review report: `paper/planning/phases/P09_review.md` (populated)
- Hardened manuscript: `paper/writing/manuscript.tex`
- Decision record: `paper/decisions/ADR-009_review_hardening.md`
