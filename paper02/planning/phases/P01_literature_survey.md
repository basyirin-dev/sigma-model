# Phase 01 — Literature Survey & Systematic Gap Identification

**Phase ID:** P01  
**Phase Title:** Multi-Domain Systematic Literature Survey, Taxonomy Clustering & Theoretical Gap Isolation  
**Status:** Tasks 1.1–1.4 complete; `[HUMAN-GATE]` novelty approval pending  
**Duration:** 2 Days  
**Dependencies:** PCC  
**Executor:** Agent (90%) / Human-Gate (10%)  
**Deliverables:** `paper02/experiments/literature/survey_table.csv`, `paper02/planning/literature-audit.md` (appended Gap Memo), `paper02/decisions/ADR-004_literature_positioning.md`

---

## 1. Purpose & Scope
Execute an exhaustive, agent-driven literature survey across 5 adjacent fields: (i) Dynamical systems and phase transitions in learning, (ii) Grokking and delayed generalization, (iii) Singular Learning Theory (SLT) and geometry, (iv) Edge of Stability (EOS) and sharpness dynamics, and (v) Compositional generalization in neural networks. Cluster retrieved papers into a structured matrix and isolate the exact unaddressed theoretical gap.

---

## 2. Exhaustive Tasks & Subtasks

### Task 1.1: Multi-Domain API Query Execution
1. **Define Targeted Search Queries across Semantic Scholar API, arXiv API, and OpenAlex:**
   - *Cluster 1 (Phase Transitions & Bifurcations in ML):*
     - `"bifurcation" AND "gradient descent" AND "neural network"`
     - `"transcritical bifurcation" AND "loss landscape"`
     - `"phase transition" AND "representation learning" AND "order parameter"`
   - *Cluster 2 (Grokking & Delayed Generalization):*
     - `"grokking" AND "phase transition" AND "weight decay"`
     - `"representation formation" AND "delayed generalization"`
     - `"circuit efficiency" AND "grokking" AND "mechanistic"`
   - *Cluster 3 (Singular Learning Theory & Geometry):*
     - `"singular learning theory" AND "local learning coefficient" AND "phase"`
     - `"loss landscape geometry" AND "singularities" AND "generalization"`
   - *Cluster 4 (Edge of Stability & Hessian Dynamics):*
     - `"edge of stability" AND "Hessian top eigenvalue" AND "Cohen"`
     - `"sharpness-aware minimization" AND "spectral dynamics"`
   - *Cluster 5 (Compositional Generalization & Inductive Biases):*
     - `"compositional generalization" AND "inductive bias" AND "SCAN"`
     - `"systematic generalization" AND "representation geometry"`
2. **Execute Ingestion Script:**
   - Query APIs, deduplicate entries by DOI/arXiv ID, and filter for papers published between 2018 and 2026.

### Task 1.2: Literature Matrix Extraction (`survey_table.csv`)
**Status:** ✅ Complete (2026-08-23) — `survey_table.csv` contains 60 curated entries (12 per cluster × 5 clusters); build script `paper02/experiments/literature/build_survey_table.py`.
1. For each retrieved paper ($\ge 50$ papers), extract and populate:
   - `Title`, `Authors`, `Year`, `Venue`, `ArXiv_ID`, `DOI`.
   - `Primary_Cluster` (Bifurcations / Grokking / SLT / EOS / Compositionality).
   - `Core_Claim` (The main theoretical or empirical assertion).
   - `Mathematical_Formalism` (e.g., Continuous ODE, Mean-Field, Langevin, Discrete SGD, None).
   - `Empirical_Benchmark` (e.g., Modular Addition, SCAN, COGS, ImageNet, Synthetic).
   - `Order_Parameter_Used` (e.g., Sharpness, LLC, CKA, Norm, GCA, None).
   - `Limitation_Identified` (Why this work does NOT solve the Paper 02 problem).
2. Save to `paper02/experiments/literature/survey_table.csv`.

### Task 1.3: Methodological Clustering & Comparative Positioning
**Status:** ✅ Complete (2026-08-23) — full row-cited, claim-tagged synthesis in `paper02/planning/methodological-clustering.md`; condensed pointer in `paper02/planning/literature-audit.md` §8. Claim-audited (skill:claim-auditor + independent review; CC.3.3 tags; CLM-001–007 ledger mapping).
1. **Synthesize Structural Distinctions:**
   - *Vs. Grokking (Power et al., Nanda et al.):* Grokking involves spontaneous unguided escape from a metastable plateau over $10^4$--$10^5$ steps on i.i.d. splits. The $\Sigma$-Trap is an asymptotically stable equilibrium under standard loss; escape requires crossing a supercritical structural pressure threshold ($\lambda > \lambda_{\text{crit}}$).
   - *Vs. Singular Learning Theory (Watanabe, Lau et al.):* SLT characterizes statistical complexity via the Local Learning Coefficient (LLC) across singularity strata. Paper 02 models the deterministic transverse stability exchange of representation manifolds under competing gradient vector fields.
   - *Vs. Edge of Stability (Cohen et al.):* EOS tracks progressive sharpening until the top Hessian eigenvalue hits $2/\eta$. Paper 02 tracks the stability exchange of orthogonal representation subspaces ($S$ vs $C$).
   - *Vs. Standard Compositional Literature (Lake & Baroni, Kim & Linzen):* Prior work documents empirical failure or proposes heuristic architectures. Paper 02 derives the exact critical threshold condition from gradient flow.

### Task 1.4: Draft Formal Gap-Analysis Memo
**Status:** ✅ Complete (2026-08-23) — Gap-Analysis Memo appended as `paper02/planning/literature-audit.md` §9; `paper02/decisions/ADR-004_literature_positioning.md` emitted (Status: Proposed, pending `[HUMAN-GATE]` §9.6). Claim-audited + independently reviewed (verbatim proposition, P03-gate-aligned falsifiability, CC.3.3 tags).
1. Draft a 3-page rigorous Gap-Analysis Memo and append to `paper02/planning/literature-audit.md`.
2. Formulate the **Novelty Proposition:**
   > *"No existing framework derives a closed-form critical supervision threshold for compositional representation formation from continuous gradient flow, nor characterizes the resulting transcritical stability exchange."*
3. Emit `paper02/decisions/ADR-004_literature_positioning.md`.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator verifies that the gap analysis is bulletproof and that no relevant 2025–2026 preprints are missed.

---

## 4. Machine-Checkable Exit Criteria
- [x] `paper02/experiments/literature/survey_table.csv` contains $\ge 50$ curated entries across the 5 clusters. *(60 entries, 12 per cluster — verified 2026-08-23)*
- [x] Gap-analysis memo appended to `planning/literature-audit.md` with explicit differentiation against Grokking, SLT, and EOS. *(Done 2026-08-23: §9 Gap-Analysis Memo + §8 clustering, row-cited and claim-tagged)*
- [x] `paper02/decisions/ADR-004_literature_positioning.md` committed. *(Emitted 2026-08-23; committed with the Task 1.4 commit)*
- [ ] `[HUMAN-GATE]` Novelty positioning approved. *(Open — approval block at `literature-audit.md` §9.6; ADR-004 Status: Proposed)*

---

## 5. Deliverables & Artifacts
- Extraction table: `paper02/experiments/literature/survey_table.csv`
- Appended memo: `paper02/planning/literature-audit.md`
- Decision record: `paper02/decisions/ADR-004_literature_positioning.md`
