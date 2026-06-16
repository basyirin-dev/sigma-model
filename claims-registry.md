# Claims Registry — Σ-Model V3.0+

Every quantitative claim in `paper/manuscript.tex` is tracked here.
Each claim ID appears as an inline anchor `<!-- CLAIM:C-NNN -->` in the paper.

| Claim ID | Lines | Claim Text | Status | Config / Proof | Run ID | Commit | Notebook Cell |
|----------|-------|------------|--------|----------------|--------|--------|--------------|
| C-001 | 54 | SCAN: >99% ID, <2% add-primitive | LITERATURE | — | — | 3947e83 | — |
| C-002 | 54 | COGS: 96-99% ID, 16-35% compositional | LITERATURE | — | — | 3947e83 | — |
| C-003 | 100 | ME training: structural splits <1% | LITERATURE | — | — | 3947e83 | — |
| C-004 | 207 | theta_delta ≈ 0.7 (reference mastery) | DESIGNED | base.yaml | — | 3947e83 | — |
| C-005 | 227 | gamma_sigma ∈ (0,1) | DESIGNED | base.yaml | — | 3947e83 | — |
| C-006 | 475 | P*(t) forcing function thresholds | DESIGNED | base.yaml | — | 3947e83 | Cell 4 |
| C-007 | 712-716 | Validity thresholds (CI>0.60, FD>0.55, DG>0.40, R_A>0.75, V_A>0.20) | DESIGNED | base.yaml | — | a155c7a | Cell 4 (NB2) |
| C-008 | 1556--1586 | High-delta/Low-sigma OOD gap ≥30pp, d≥0.5 | COLLECTED | base.yaml | kaggle-2026-06-06 | — | §12.0 |
| C-009 | 1259-1263 | Benchmark validity scores (Table 12.1) | DESIGNED | h-*.yaml | — | a155c7a | NB2 Cell 4 |
| C-010 | 1277 | H-PTB OOD ratio at tau* (GPT-4) | PENDING | h-ptb.yaml | — | — | — |
| C-011 | 1278 | H-PTB OOD ratio at tau* (Claude 3.5) | PENDING | h-ptb.yaml | — | — | — |
| C-012 | 1279 | H-PTB OOD ratio at tau* (Gemini 1.5) | PENDING | h-ptb.yaml | — | — | — |
| C-013 | 1280 | H-AFB alpha_hat at s=0.80 (GPT-4) | PENDING | h-afb.yaml | — | — | — |
| C-014 | 1281 | H-AFB Delta_surf | PENDING | h-afb.yaml | — | — | — |
| C-015 | 1282 | H-MCB zeta_hat overall | PENDING | h-mcb.yaml | — | — | — |
| C-016 | 1284 | H-DCB beta_1_hat slope | PENDING | h-dcb.yaml | — | — | — |
| C-017 | 1285 | H-DCB BCR at rho=1.0 | PENDING | h-dcb.yaml | — | — | — |
| C-018 | 1286 | H-STB ROI_Schema | PENDING | h-stb.yaml | — | — | — |
| C-019 | 1287 | H-STB mu_hat_AB | PENDING | h-stb.yaml | — | — | — |
| C-020 | 1299-1306 | Human baseline N=200 results | PENDING | h-*.yaml | — | — | — |
| C-021 | ~595 | Lemma 3.1: σ_A latent from δ trajectory | PROVEN | docs/proof-reconstruction/lemma-3-1.tex | — | — | — |
| C-022 | ~840 | Prop 3.1: Local existence/uniqueness | PROVEN | docs/proof-reconstruction/prop-3-1.tex | — | — | — |
| C-023 | ~862 | Prop 3.2: Forward invariance + boundedness | PROVEN | docs/proof-reconstruction/prop-3-2.tex | — | — | — |
| C-024 | ~904 | Prop 3.3: Fast-slow decomposition (Fenichel) | PROVEN | docs/proof-reconstruction/prop-3-3.tex | — | — | — |
| C-025 | ~934 | Prop 3.4: Single-domain equilibria | PROVEN | docs/proof-reconstruction/prop-3-4.tex | — | — | — |
| C-026 | ~969 | Prop 3.5: Numerical stability (condition number) | PROVEN | docs/proof-reconstruction/prop-3-5.tex | — | — | — |
| C-027 | ~684 | Prop 3.6: Estimator consistency (σ̂_A convergence) | PROVEN | docs/proof-reconstruction/prop-3-6.tex | — | — | — |
| C-028 | ~702 | Prop 3.7: Error propagation (Delta method) | PROVEN | docs/proof-reconstruction/prop-3-7.tex | — | — | — |
| C-029 | ~1139 | Thm 4.1: SGD-induced σ-suppression | PROVEN | docs/proof-reconstruction/theorem-4-1.tex | — | — | — |
| C-030 | ~1351 | Prop 4.1: σ_critical derivation (transcritical bifurcation) | PROVEN | docs/proof-reconstruction/prop-4-1.tex | — | — | — |
| C-031 | ~1377 | Prop 4.2: Depth threshold δ* derivation | PROVEN | docs/proof-reconstruction/prop-4-2.tex | — | — | — |
| C-032 | ~1397 | Prop 4.3: Hysteresis and reverse transitions | PROVEN | docs/proof-reconstruction/prop-4-3.tex | — | — | — |
| C-033 | ~1413 | Prop 4.4: Noise sensitivity (Gaussian tail) | PROVEN | docs/proof-reconstruction/prop-4-4.tex | — | — | — |
| C-034 | ~1449 | Thm 4.2: Faculty-validity correspondence | PROVEN | docs/proof-reconstruction/theorem-4-2.tex | — | — | — |
| C-035 | ~1480 | Lemma 4.2: Faculty omission penalty (geometric mean) | PROVEN | docs/proof-reconstruction/lemma-4-2.tex | — | — | — |
| C-036 | ~1489 | Prop 4.5: Compensation analysis (α_A vs σ_A) | PROVEN | docs/proof-reconstruction/prop-4-5.tex | — | — | — |
| C-037 | ~1405 | Phase 6: Circular dependency (Filippov formulation) | PROVEN | docs/proof-reconstruction/phase-6-hybrid.tex | — | — | — |
| C-038 | ~1084 | Σ-Model training adds 31.6% computational overhead | DESIGNED | base.yaml | — | — | — |

## Status Legend
- **LITERATURE:** Claim cites published result (no experiment needed)
- **DESIGNED:** Benchmark/config exists, data not yet collected
- **PENDING:** Data collection planned (Kaggle post-June 1 2026, Prolific N=200)
- **COLLECTED:** Data collected and verified
- **FALSIFIED:** Experiment completed, claim not supported
- **RECONSTRUCTED:** Claim backed by formal proof in `docs/proof-reconstruction/`
- **PROVEN:** Fully verified mathematical statement with complete derivation

## Verification
Run `grep '<!-- CLAIM:' paper/manuscript.tex | sort > /tmp/anchors.txt` and compare against claim IDs above. Every anchor must have a registry entry and vice versa.
