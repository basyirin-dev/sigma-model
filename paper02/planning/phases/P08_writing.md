# Phase 08 — Manuscript Writing & Section Assembly

**RPF v2.0:** Git tag `p08-draft-v1` · Duration 3–5d · GPU 0 · RACI: Agent **R** / PI **A** (narrative; 72h gate) · Abort: >5 `keep` claims missing after 2 passes → halt · Acceptance: abstract ≤250 words, overclaim detector 0 flags, code/data availability statements, ledger fully cross-referenced · *Pending (locked by P03 gate).*

**Phase ID:** P08  
**Phase Title:** Complete Manuscript Assembly in NeurIPS/ICLR LaTeX Format, Mathematical Appendix Formulation, and Bibliography Verification  
**Status:** Complete (Draft Assembly Finished; Pending PI Gate Review)  
**Duration:** 3–4 Days  
**Dependencies:** P07  
**Executor:** Agent (85%) / Human-Gate (15%)  
**Deliverables:** `paper02/writing/manuscript.tex`, `paper02/writing/manuscript.pdf`, `paper02/writing/bibliography.bib`, `paper02/decisions/ADR-008_manuscript_framing.md`

---

## 1. Purpose & Scope
Draft the complete, self-contained manuscript in NeurIPS/ICLR LaTeX format. Synthesize the theoretical derivation, continuous gradient flow stability proofs, empirical phase boundary discoveries, and representation geometry order parameters into a cohesive, high-impact scientific narrative. Ensure strict claim discipline (CC.3.3) and clean LaTeX builds.

---

## 2. Exhaustive Tasks & Subtasks

### Task 8.1: Section-by-Section Manuscript Drafting
1. **Title & Header:**
   - Title: *Critical Compositional Pressure: A Phase-Boundary Law for Neural Representation Formation*
   - Keywords: *compositional generalization, learning dynamics, phase transitions, continuous gradient flow, representation geometry*.
2. **Abstract ($\le 250$ Words, CC.3.1):**
   - Frame the representation selection dilemma under ERM ($E_S$ shortcut entrapment).
   - State the Two-Subspace Critical Pressure Law: $\lambda_{\text{crit}} = b_C / a_C \iff R_0 = 1$.
   - Highlight empirical validation across 750 multi-seed runs (H-Bar, SCAN, COGS, PCFG-SET).
   - Explicitly declare claim levels (analytical model theorem + empirical bifurcation verification).
3. **Section 1 — Introduction:**
   - The generalization mystery: Why ERM fails at out-of-distribution recombination despite achieving near-zero training risk.
   - Paradigmatic shift: Compositional competence as a phase-boundary control problem rather than a curriculum trajectory optimization problem.
   - Summary of Contributions (Tripartite: (1) Analytical Two-Subspace Law, (2) Empirical Separatrix Validation, (3) Geometric Order Parameters).
4. **Section 2 — Related Work & Theoretical Positioning:**
   - Rigorous contrast against Grokking (metastable unguided escape vs. supercritical stability exchange).
   - Rigorous contrast against Singular Learning Theory / LLC (complexity singular strata vs. continuous deterministic vector fields).
   - Rigorous contrast against Edge of Stability (global representation subspaces vs. scalar learning-rate sharpness ceilings).
5. **Section 3 — Theoretical Foundations: The Two-Subspace Law:**
   - Orthogonal parameter decomposition $w = (u, v)$.
   - Loss formulations: Task loss $\mathcal{L}_{\text{task}}$ and substitution loss $\mathcal{L}_{\text{comp}}$.
   - Continuous gradient flow equations: $\dot{u} = a_S (\theta_S - u) - \lambda b_S u$, $\dot{v} = v (\lambda a_C - b_C) - \kappa v^2$.
   - Theorem 1 (Transcritical Bifurcation of Representation Space): Full formal theorem statement with proof sketch.
6. **Section 4 — Empirical Phase Boundary & Separatrix:**
   - Experimental methodology (750 runs, $n=30$ seeds per cell).
   - Sigmoid escape probability fit: $P(\text{escape} \mid \lambda)$, extracting empirical $\hat{\lambda}_{\text{crit}}$.
   - Late-onset intervention results confirming $E_S$ destabilization.
7. **Section 5 — Geometric Order Parameters & Internal Circuits:**
   - CKA representation geometry trajectory flows.
   - Granger causality proving $\Delta \text{CKA}_t \to \Delta \text{OOD}_{t+1}$.
   - Resolution of the GCA initialization artifact via subspace projection.
8. **Section 6 — Benchmark Generalization:**
   - Cross-benchmark validation on SCAN (jump & length splits), COGS, and PCFG-SET.
9. **Section 7 — Discussion, Limitations & Future Horizons:**
   - Boundary between continuous ODE approximations and discrete SGD noise.
   - Open questions: Autonomous grammar discovery (Paper 03) and multi-task manifold retention (Paper 03).
10. **Broader Impact & Ethical Considerations (CC.7.1).**

### Task 8.2: Comprehensive Mathematical Appendices
1. **Appendix A (Notation Reference):** Complete table of symbols, dimensions, and operational definitions.
2. **Appendix B (Proof of Theorem 1):** Complete, uncompromised mathematical proof of the transcritical bifurcation and Lyapunov stability of $E_C$.
3. **Appendix C (Diffrax Numerical Scheme & Stability Analysis):** Stiff solver convergence, step size adaptivity, and A-stability proof.
4. **Appendix D (Data Cards & Zero-Leakage Audits):** Complete grammar generation rules, token frequencies, and disjoint support proofs (CC.4.2).
5. **Appendix E (Raw Per-Seed Tables & Statistics):** Full per-seed metrics, standard deviations, Welch $t$-test tables, and TOST sensitivity grids.

### Task 8.3: Bibliography Compilation & Formatting
1. Curate verified BibTeX entries in `paper02/writing/bibliography.bib`.
2. Format in official `neurips_2026.sty` / `iclr2026.sty` template.
3. Verify compilation via `make -C paper02 pdf` asserting 0 errors, 0 undefined citations (`[?]`), and 0 undefined references (`[??]`).

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator conducts a full authorial review of the complete manuscript draft, evaluating narrative coherence, technical precision, and tone.

---

## 4. Machine-Checkable Exit Criteria
- [x] Manuscript compiles cleanly via `make -C paper02 pdf` (exit code 0).
- [x] Abstract $\le 250$ words (CC.3.1) [Actual: 220 words].
- [x] Every claim in the text links bi-directionally to a row in `planning/ledger.md` (Table 4 / CLM-001--CLM-007).
- [x] 0 undefined references (`??`) and 0 undefined citations (`?`) in LaTeX build log.
- [ ] `[HUMAN-GATE]` Full draft approved for red-team review.

---

## 5. Deliverables & Artifacts
- Manuscript sources: `paper02/writing/manuscript.tex`, `paper02/writing/bibliography.bib`
- Compiled PDF: `paper02/writing/manuscript.pdf`
- Decision record: `paper02/decisions/ADR-008_manuscript_framing.md`
