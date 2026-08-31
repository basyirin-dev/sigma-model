# Research Roadmap & Phase Execution Plan (RPF v2.0)

- **Date:** 2026-08-24
- **Status:** Active / Execution
- **Decision Context:** Formalizing the $\Sigma$-Model research programme into a 15-phase lifecycle under RPF v2.0 governance.
- **Triggering Event:** Transition from exploratory prototypes to rigorous, publication-grade empirical and theoretical validation.
- **Chosen Strategy:** Phased gate-governed execution with artifact-first evidence tracking, stiff numerical solvers, and double-blind verification.
- **Constraints:** Compute budget $\le 500$ GPU hours, deterministic reproducibility across clean-room Docker targets, strict claim discipline.

---

## Phase Dependency Graph

```text
[P00: Repo & Environment Setup]
        │
        ▼
[P01: Literature Audit & Claim Framing]
        │
        ▼
[P02: Theoretical Foundations & ODE Derivations]
        │
        ▼
[P03: Gate Formulation & Preregistration] ──► [HUMAN-GATE 1]
        │
        ▼
[P04: Experimental Matrix & Statistical Protocol]
        │
        ▼
[P05: Computational Kernel & Harness Implementation]
        │
        ▼
[P06: Production Data Generation & Sweep Execution] ──► [Tag: p06-data-complete]
        │
        ▼
[P07: Analysis, Geometry Diagnostics & CKA]
        │
        ▼
[P08: Manuscript Drafting & Figures (Quarto)] ──► [HUMAN-GATE 2]
        │
        ▼
[P09: Adversarial Red-Team & Statistical Audit]
        │
        ▼
[P10: Clean-Room Docker Verification & Smoke Pass]
        │
        ▼
[P11: Submission Packaging & Anonymization] ──► [HUMAN-GATE 3]
        │
        ▼
[P12: Reviewer Rebuttal & Revision Matrix]
        │
        ▼
[P13: Camera-Ready & Open-Source Artifact Release]
        │
        ▼
[P14: Post-Publication Archival & Long-Term Maintenance]
```

---

## Phase Milestone Schedule

| Phase | Description | Deliverable Artifacts | Gate / Review |
|---|---|---|---|
| **P00** | Repository & Toolchain Setup | Scaffolding, `meta/`, `.pi/` ecosystem, Dockerfile, scripts | Automated exit check |
| **P01** | Literature & Claim Taxonomy | `literature/screening-log.csv`, `literature-audit.md` | Internal audit |
| **P02** | Theoretical Foundations | ODE formulation, stability analysis, bifurcation proofs | Proof verification |
| **P03** | Gate Formulation | `preregistration.md`, `gate-result.md` structure | **[HUMAN-GATE 1]** |
| **P04** | Experimental Design | Multi-benchmark configs, power analysis, sample sizes | Design review |
| **P05** | Implementation & Kernels | Solvers, PyHessian, CKA engines, unit tests | CI smoke pass |
| **P06** | Data Generation & Sweeps | Raw results, manifests, checksums | `p06-data-complete` |
| **P07** | Diagnostic Analysis | Inflection curves, geometric curvature, summary tables | Matrix audit |
| **P08** | Manuscript Drafting | `writing/manuscript/index.qmd`, publication figures | **[HUMAN-GATE 2]** |
| **P09** | Hostile Red-Team Review | 4-persona audit reports, statistical power checks | Red-team sign-off |
| **P10** | Clean-Room Verification | Docker smoke build, environment diff, SHA-256 match | Verification report |
| **P11** | Submission Packaging | Anonymized manuscript bundle, supplementary archive | **[HUMAN-GATE 3]** |
| **P12** | Rebuttal & Revisions | Rebuttal response matrix, revised experimental delta | Decision gate |
| **P13** | Camera-Ready Release | De-anonymized PDF, open-source code/weights release | Release sign-off |
| **P14** | Post-Publication Archival | Long-term DOI snapshot, Zenodo repository archive | Post-mortem |
