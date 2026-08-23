# ADR-004: Literature Positioning & Novelty Scoping

**Date:** 2026-08-23
**Status:** Proposed *(pending `[HUMAN-GATE]` novelty approval — Gap-Analysis Memo §9.6)*
**Phase:** P01
**Deciders:** Principal Investigator & AI Agent

---

## 1. Context & Problem Statement

Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*) must enter review with a defensible novelty claim. Paper 01 reviewers attacked the phenomenological *positing* of the macro-ODE (A5/A6: threshold and decay posited, not derived; A7: microscopic↔macroscopic bridge unproven; A8: manifold geometry ambiguous — see `planning/literature-audit.md` §5). Paper 02 answers by *deriving* the threshold from continuous gradient flow (ADR-001), but the derivation sits at the intersection of five crowded literatures (bifurcations/phase transitions, grokking, Singular Learning Theory, Edge of Stability, compositional generalization), each of which could be used by a reviewer to argue "this is already known."

P01 produced the evidence needed to choose a positioning: a 60-entry curated survey (`survey_table.csv`), a consensus sweep (§6 of the audit), and a row-cited comparative clustering (Task 1.3 → `methodological-clustering.md`, `literature-audit.md` §8). This ADR records the **decision** on how Paper 02 frames its novelty, which cluster is its primary citation neighborhood, how SLT/EOS relations are handled, and the exact scope guards on the Novelty Proposition.

## 2. Decision Drivers

- **Driver 1 (Derivation, not positing):** The positioning must foreground that $\lambda_{\text{crit}} = b_C/a_C$ is *derived from continuous gradient flow* in a two-subspace reduction (ADR-001, CLM-001), directly answering reviewers A5–A8.
- **Driver 2 (Falsifiability):** The claim must be testable at the P03 Mechanism Gate (escape-probability phase boundary, late-onset recovery, TOST parity — CLM-003/004).
- **Driver 3 (Review defense):** The differentiation against Grokking, SLT, and EOS must be explicit and row-cited, so "already known" objections have a documented, evidence-based rebuttal.
- **Driver 4 (Scope honesty / CC.3.3):** No grand-theory, origin, or priority claims; the proposition must be scoped by its own terms so it is *easier* to verify than to refute.

## 3. Considered Options

- **Option 1 (Bifurcation-Continuation Framing):** Position Paper 02 as the direct continuation of the bifurcation/phase-transition program (primary citation neighborhood: r1–r11 — Ziyin & Ueda r2, Li & Arora r10, Biroli et al. r4, Montanari & Wang r5, Wang r11). *Pros:* maximal formal continuity; the rows' own `Limitation_Identified` fields document the missing pieces (task-vs-schema decomposition r2/r10; closed-form supervision thresholds r1/r11; compositional sequence architectures r4/r5). *Cons:* must differentiate from toy/generic-landscape scope of r2/r10; the transcritical-bifurcation term invites comparison with r2.
- **Option 2 (Grokking-Adjacent Framing):** Position Paper 02 as "the stable-OOD counterpart to grokking." *Pros:* high visibility; engages the grokking community. *Cons:* risk of conflating i.i.d. delayed generalization with zero-shot OOD failure — the exact discriminator (§8.2) would have to be argued on every page; the σ-trap is *stable* where grokking is *metastable*, so the framing invites more confusion than insight.
- **Option 3 (SLT/EOS-Complementary Framing):** Position Paper 02 as complementary to diagnostics (LLC/RLCT, r25/r26) and optimizer-stability (EOS, r37/r38): SLT and EOS characterize *statistical complexity* and *step-size stability*; Paper 02 characterizes *loss-composition stability* in representation space. *Pros:* safe; avoids priority disputes; the complementarity is already row-grounded (r26, r37 limitations). *Cons:* risks appearing incremental if used as the *only* framing.
- **Option 4 (No Explicit Novelty Claim):** Omit the proposition and rely on the derivation's self-evidence. *Pros:* safest possible posture. *Cons:* fails P01 exit criterion 4 (`[HUMAN-GATE]` novelty positioning) and leaves the related-work narrative undefined; reviewers then define the contribution themselves.

## 4. Decision Outcome & Mathematical/Empirical Rationale

**Chosen Option:** **Option 1 + Option 3 hybrid**, with Option 2's grokking differentiation retained *as a negative-space argument* (what the trap is **not**), and Option 4 rejected.

- **Primary framing (O1):** Paper 02 continues the bifurcation/phase-transition program in the compositional setting. Related-work opens with the bifurcations cluster (r1–r11), states the three row-documented gaps (decomposition, closed-form threshold, sequence architectures), and presents the two-subspace transcritical analysis (CLM-001) as their resolution.
- **Complementarity guards (O3):** Dedicated, row-cited paragraphs (memo §9.2; `methodological-clustering.md` §2.2–2.3) state complementarity with SLT (LLC remains a valid post-hoc diagnostic; RLCT asymptotics undisputed) and EOS (orthogonal stability objects; same modified-continuous-flow family as r38).
- **Grokking (O2 as negative space):** One explicit paragraph (memo §9.2) distinguishing i.i.d. metastable grokking (r13) from stable zero-shot OOD failure, preventing conflation without adopting grokking-adjacent framing.
- **Novelty Proposition (retained verbatim, scoped):**
  > *"No existing framework derives a closed-form critical supervision threshold for compositional representation formation from continuous gradient flow, nor characterizes the resulting transcritical stability exchange."*
  Scope guards (per Task 1.3): delimited by its own terms — *closed-form threshold*, *continuous gradient flow*, *transcritical stability exchange* (two-subspace formalism, ADR-001/CLM-001); asserts neither absence of related work nor priority over SLT/EOS diagnostics; supported by the surveyed rows' `Limitation_Identified` fields as row-cited in Gap-Analysis Memo §9.2 (identifier resolution of all cited rows verified programmatically, Task 1.3).

### Positive Consequences
- Every "already known" objection has a row-cited rebuttal (differentiation matrix, §8.2).
- The claim's falsifiability is concrete: P03 gate criteria (CLM-003/004) decide it.
- Alignment with reviewers A5–A8: the derivation answers the exact critiques §5 records.

### Negative Consequences / Trade-offs
- Reviewers anchored in grokking/SLT/EOS may expect those literatures to *lead* the related work; mitigation: the complementarity paragraphs and the negative-space grokking argument keep all three visible without letting them set the frame.
- The transcritical-bifurcation vocabulary invites direct comparison with r2 (Ziyin & Ueda); mitigation: the §2.5/§8.2 discriminator (toy weight-symmetry vs. two-subspace compositional representation) is stated in the same paragraph.
- Scope guards make the proposition narrower than a casual reader might expect; mitigation: §9.4 states the scope *before* the proposition is asserted, and §9.5 lists non-claims.

## 5. Compliance & Traceability

- **Ledger Impact:** Frames CLM-001 (two-subspace stability exchange, T), CLM-002 ($R_0 = 1$ isomorphism, T), CLM-003/004 (P03-testable predictions, E, `decide-at-P03`), CLM-007 (cross-benchmark scope, E). No new ledger claims introduced.
- **Standards Cross-Reference:** CC.3.3 (tripartite separation; no grand-theory claims), CC.6.1 (commit format), CC.6.2 (additive decision record; supersedes nothing).
- **Evidence Artifacts:** Gap-Analysis Memo (`literature-audit.md` §9) · comparative clustering (`methodological-clustering.md`, `literature-audit.md` §8) · survey (`survey_table.csv`, 60 rows) · consensus sweep (`literature-audit.md` §6) · reviewer critique table (`literature-audit.md` §5) · derivation decision (ADR-001).
- **Gate Dependency:** This ADR becomes **Approved** upon `[HUMAN-GATE]` sign-off in Gap-Analysis Memo §9.6.
