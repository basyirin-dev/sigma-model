# Claims Registry — Σ-Model Model V3.0+

Every quantitative claim in `paper/paper.md` is tracked here.  
Each claim ID appears as an inline anchor <!-- CLAIM:C-NNN --> in the paper.

| Claim ID | Lines | Claim Text | Status | Config | Run ID | Commit | Notebook Cell |
|----------|-------|------------|--------|--------|--------|--------|--------------|
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

## Status Legend
- **LITERATURE:** Claim cites published result (no experiment needed)
- **DESIGNED:** Benchmark/config exists, data not yet collected
- **PENDING:** Data collection planned (Kaggle post-June 1 2026, Prolific N=200)
- **COLLECTED:** Data collected and verified
- **FALSIFIED:** Experiment completed, claim not supported

## Verification
Run `grep '<!-- CLAIM:' paper/paper.md | sort > /tmp/anchors.txt` and compare against claim IDs above. Every anchor must have a registry entry and vice versa.
