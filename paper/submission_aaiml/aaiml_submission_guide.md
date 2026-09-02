# AAIML Submission Guide & Portal Package

**Journal:** *Advances in Artificial Intelligence and Machine Learning (AAIML)*  
**ISSN:** 2582-9793  
**Publisher / Indexing:** Scopus, Web of Science, Google Scholar, CrossRef (Open Access, Zero APC)  
**Editor-in-Chief:** Prof. Anca Ralescu (University of Cincinnati)  
**Review Model:** Standard asynchronous written peer review (6–10 weeks) — *No synchronous meetings or video conferences*  
**Submission Portal:** `https://www.oajaiml.com/author/menupage` (or direct editorial submission portal)

---

## 1. Submission Package Contents

| File | Purpose |
|---|---|
| `manuscript_journal.pdf` | Streamlined 15-page main research article (Sections 1–8, Figures 1–5, Tables 1–5, References) |
| `supplementary_materials.pdf` | Standalone Supplementary Materials (15 pages, Appendices A–F with proofs, dataset cards, VAR tables) |
| `manuscript.pdf` | Comprehensive 35-page research monograph with fully integrated appendices |
| `cover_letter.pdf` | Official cover letter to Prof. Anca Ralescu and Editorial Board with AI disclosure |
| `cover_letter.tex` | LaTeX source for cover letter |
| `supplementary_materials.zip` | Reproducibility bundle: complete `src/`, `tests/`, processed data summaries, and figure sources |
---

## 2. Manuscript Metadata for Portal Forms

- **Article Title:** Critical Compositional Pressure: A Phase-Boundary Framework for Compositional Representation Formation in Neural Networks
- **Running Title / Short Title:** Critical Compositional Pressure
- **Author:** Basyirin Amsyar Basri
- **Affiliation:** Independent Researcher, Kuala Lumpur, Malaysia
- **Corresponding Email:** `basyirinbasri@gmail.com`
- **Article Type:** Original Research Article
- **Subject Category / Field:** Machine Learning Theory / Dynamical Systems / Representation Learning
- **Keywords:** `compositional generalization`, `continuous gradient flow`, `phase transition`, `shortcut learning`, `transcritical bifurcation`

---

## 3. Abstract (for Portal Text Field)

Standard empirical risk minimization (ERM) in deep neural networks consistently defaults to brittle, memorized shortcuts ($E_S$) rather than systematic compositional rules, despite achieving near-zero training risk. We formulate the Two-Subspace Phase-Boundary Framework, establishing that the transition between shortcut entrapment and systematic compositional generalization is governed by an analytical transcritical bifurcation of continuous gradient flow. When structural compositional pressure $\lambda$ crosses the critical threshold $\lambda_{\text{crit}} = b_C / a_C$ (formalized via the non-dimensional threshold ratio $R_0 = \lambda a_C / b_C = 1$), the shortcut equilibrium loses stability to a coherent representation attractor $E_C$. We rigorously prove this bifurcation for continuous gradient flow (Level 1), establish its structural stability under Center Manifold perturbations and AdamW preconditioning, and empirically validate it across 960 multi-seed runs spanning four benchmark suites ($\hbar$, SCAN, COGS, PCFG-SET) and three architecture families (Levels 2 \& 3). Non-linear change-point fitting reveals an exceptionally sharp empirical separatrix ($k \in [58.2, 72.4] \gg 15.0, R^2 > 0.91$), decisively falsifying smooth dose-response regularizers. Furthermore, vector autoregressive (VAR) econometric testing confirms that internal representation alignment ($t_{50\%} \approx 250$) predictively precedes behavioral out-of-distribution recovery ($t_{50\%} \approx 400$) by $\Delta t \approx 150$ steps ($F = 3.716, p < 0.01$), while late-onset interventional experiments corroborate causal agency. Finally, matrix-free Lanczos Hessian measurements show that training under supercritical pressure remains strictly bounded below the Edge of Stability ceiling ($\lambda_{\text{max}} \le 1680.4 \ll 2/\eta = 2000.0$). While structural pressure is provided here via explicit substitution constraints, unsupervised grammar discovery without explicit pairs is formally cataloged as Level 4 deferred scope.
---

## 4. Suggested Reviewers / Domain Expertise

1. **Area 1: Dynamical Systems & Phase Transitions in Neural Networks**
   - Expertise: Loss landscape bifurcations, Edge of Stability, continuous gradient flow, singular learning theory.
2. **Area 2: Compositional Generalization & Representation Geometry**
   - Expertise: Sequence-to-sequence evaluation, SCAN/COGS benchmarks, Centered Kernel Alignment (CKA), shortcut learning.
3. **Area 3: Theoretical Machine Learning & Curriculum Learning**
   - Expertise: Optimization dynamics, learning phase boundaries, structural regularizers.

---

## 5. Contingency Plan & Cascade Venues (Zero Cost / Open Access)

All backup venues strictly satisfy zero APC, full open access, and standard written peer review only:

1. **Backup 1: Foundations of Computing and Decision Sciences (FCDS)**
   - *ISSN:* 2300-3405 | *Publisher:* Poznań University of Technology / Sciendo (De Gruyter)
   - *Indexing:* Scopus, Web of Science (ESCI), IF 1.8, Q3.
   - *Submission Portal:* Sciendo Editorial Manager.
   - *Fit:* Strong theoretical and mathematical modeling scope; natural fit for bifurcation and ODE systems in computing.
2. **Backup 2: Computational Linguistics (MIT Press)**
   - *ISSN:* 1530-9312 | *Publisher:* MIT Press / Association for Computational Linguistics
   - *Indexing:* Scopus, WoS (SCIE), IF 3.7, Q1 (Diamond Open Access).
   - *Fit:* Deep focus on compositional generalization in linguistic and sequence architectures.
