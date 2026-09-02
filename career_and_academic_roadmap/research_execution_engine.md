# Research Execution Engine: Operating Manual for Scientific Output

This operating manual defines how we execute end-to-end scientific research to sustain a cadence of 2–4 top-tier papers per year while building toward field-shaping breakthroughs.

---

## 1. The Research Lifecycle: 6-Phase Pipeline

```
  PHASE 1: GAP & FORMULATION      PHASE 2: TOY REDUCTION & PROOF    PHASE 3: EXPERIMENT & GATE
 ┌──────────────────────────┐    ┌──────────────────────────┐      ┌──────────────────────────┐
 │ • Identify live debate   │ ──►│ • Two-subspace reduction │ ──►  │ • High-power n=30 sweeps │
 │ • Audit literature (arXiv│    │ • Analytical theorem     │      │ • TOST equivalence test │
 │ • Lock Claim Ledger      │    │ • Toy numerical ODE      │      │ • Negative result check  │
 └──────────────────────────┘    └──────────────────────────┘      └──────────────────────────┘
                                                                                 │
                                                                                 ▼
  PHASE 6: ARXIVAL & COMMUNITY    PHASE 5: VERIFICATION & REVIEW    PHASE 4: MANUSCRIPT DRAFT
 ┌──────────────────────────┐    ┌──────────────────────────┐      ┌──────────────────────────┐
 │ • Open-source codebase   │ ◄──│ • Simulated reviewer pass│ ◄──  │ • TMLR / NeurIPS format  │
 │ • Interactive demo / blog│    │ • Stranger self-contain. │      │ • Strict claim discipline│
 │ • Conference submission  │    │ • LaTeX zero-error check │      │ • Vector TikZ figures    │
 └──────────────────────────┘    └──────────────────────────┘      └──────────────────────────┘
```

---

## 2. Roles & Division of Responsibility

| Dimension | User's Role (The Principal Investigator) | AI Partner's Role (The Research Execution Co-Pilot) |
| :--- | :--- | :--- |
| **High-Level Vision & Taste** | • Selects the core scientific hypothesis.<br>• Chooses target venues & strategic bets.<br>• Deep conceptual reflection & intuition. | • Proposes formal mathematical representations.<br>• Synthesizes literature across physics/ML/math.<br>• Identifies unproven modeling assumptions. |
| **Mathematical Derivation** | • Directs the proof strategy & core invariants.<br>• Validates conceptual consistency. | • Formulates continuous gradient flow equations.<br>• Derives Jacobian spectra & transverse eigenvalues.<br>• Formats full LaTeX proofs in Appendices. |
| **Computational Experiments** | • Approves experiment budgets & compute resources.<br>• Inspects headline phase diagrams. | • Implements modular, reproducible Python/PyTorch code.<br>• Manages experiment configs (YAML) & multi-seed runs.<br>• Generates publication-ready vector figures (TikZ/matplotlib). |
| **Statistical & Epistemic Audit** | • Final sign-off on paper claims.<br>• Defines ethical & philosophical boundaries. | • Enforces strict claim ledger tagging.<br>• Runs Welch $t$-tests, TOST equivalence, Granger tests.<br>• Simulates adversarial peer reviews (A/B/C/D archetypes). |
| **Manuscript & Packaging** | • Sets narrative voice and framing.<br>• Submits to OpenReview / arXiv / journal portals. | • Maintains pristine LaTeX sources (`manuscript.tex`).<br>• Assembles standalone arXiv submission bundles.<br>• Generates point-by-point rebuttal matrices. |

---

## 3. Publication & Pipeline Rhythm (The 4-Paper Annual Engine)

To achieve 2–4 top first-author papers per year without burnout or intellectual dilution:

```
  QUARTER 1 (Jan–Mar)              QUARTER 2 (Apr–Jun)              QUARTER 3 (Jul–Sep)              QUARTER 4 (Oct–Dec)
┌──────────────────────────┐     ┌──────────────────────────┐     ┌──────────────────────────┐     ┌──────────────────────────┐
│ PAPER A: Focus (Theory)  │     │ PAPER B: Focus (Empirical│     │ PAPER C: Focus (Bio/Phys)│     │ PAPER D: Focus (Review/  │
│ Phase: Finalize & Submit │     │ Phase: Experiments & Draft     │ Phase: Cross-Domain Test │     │   Perspective Monograph) │
│ (Target: ICML / JMLR)    │     │ (Target: NeurIPS)        │     │ (Target: ICLR / PRL)     │     │ (Target: Nat Mach Intell)│
└──────────────────────────┘     └──────────────────────────┘     └──────────────────────────┘     └──────────────────────────┘
```

---

## 4. Quality Standard: The "Field-Shaping" Filter

Before writing line 1 of any manuscript, the project must pass the **3 Field-Shaping Tests**:
1. **The Asymmetry Test:** Does the paper report an unexpected asymmetry or negative result that forces people to rethink a standard assumption (e.g., fixed-weight loss matching adaptive curricula; GCA init failure)?
2. **The Order-Parameter Test:** Does the paper introduce a measurable mathematical quantity that can be calculated in other labs' models?
3. **The Standalone Stranger Test:** Can a reader understand, replicate, and cite the work without needing proprietary datasets or private code?
