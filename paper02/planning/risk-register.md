# Risk Register — RPF v2.0

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** RPF v2.0.0 — reference: `paper02/meta/RPF_v2.0.md`
**Status:** Active (seeded P02, updated 2026-08-23 with the in-flight P03 gate)
**Scoring:** Probability 1–5 × Impact 1–5 (see ledger §2 matrix); Score = P×I.

---

| ID | Description | Prob | Impact | Score | Owner | Due | Mitigation | Trigger | Contingency | Status |
|----|-------------|:----:|:------:|:-----:|-------|-----|-----------|---------|-------------|--------|
| R001 | **Gate underpowered / insufficient signal:** n=30 seeds per cell fails to resolve the escape step-function (Criterion 1) or the λ̂_crit band. | 2 | 5 | 10 | Agent | P02.5 | Pre-registered power/effect-size justification in `preregistration.md`; escalation to n=60 only via ADR + gate re-run | Criterion 1 p > α or effect < minimum | Redesign cell (λ resolution) or trigger P03.1 sub-gate; report INCONCLUSIVE | Open |
| R002 | **Compute overrun:** 450-run grid (10×30 + 5×30) exceeds the P03 budget (2 GPU hrs) or 2× abort threshold. | 3 | 4 | 12 | Agent | P03 | Batch scheduling; smoke-tested runner (`run_gate.py`) already validated on 10 runs; abort threshold 2× budget | Cumulative compute > 80 % budget | Halt grid at 100 %; request human approval; shrink λ grid to high-signal levels | Open |
| R003 | **Numerical failure:** NaN/Inf loss, solver non-convergence, or checkpoint corruption invalidates runs. | 2 | 4 | 8 | Agent | P03 | Pre-registered exclusion criteria (CC.4.6); numerical sanity checks (CC.2.6); deterministic seeds | Any run produces NaN/Inf | Exclude + log `NEGATIVE`; re-run excluded cells with new seeds from `seeds.yaml` | Open |
| R004 | **λ̂_crit estimate falls outside the pre-registered band** (e.g., ≥ 0.35), weakening the "supercritical" claim. | 2 | 4 | 8 | Agent | P03 | Pre-registered decision rule (Criterion 1 threshold separation at λ ≤ 0.10 / ≥ 0.50) keeps the verdict binary | λ̂_crit ∉ [0.20, 0.35] | Report honestly; binding constraint reformulated via ADR + PI directive | Open |
| R005 | **TOST parity failure:** supercritical arms differ > ±2.5 % (Criterion 3), contradicting fixed-weight parity. | 2 | 5 | 10 | Agent | P03 | TOST margins pre-registered (CC.2.3); fixed-weight arm already shown equivalent in Paper 01 v2 (§1.2) | t₁/t₂ p > 0.05 or CI outside margin | If only λ=2.0 drifts, report as boundary condition; if systematic, RE-GATE | Open |
| R006 | **Reproducibility gap:** environment drift (PyTorch/JAX versions) between smoke runs and full grid. | 2 | 3 | 6 | Agent | P03–P06 | `meta/ENVIRONMENT.md` pinned; manifests per run (CC.1.4); deterministic flags (CC.1.2) | Manifest hash mismatch across runs | Freeze environment; re-run affected cells; record in verification report | Open |
| R007 | **Novelty challenge at review:** "already known" (grokking/SLT/EOS) objection. | 3 | 4 | 12 | Agent | P01→P09 | Row-cited differentiation (§8/§9 of `literature-audit.md`); scoped novelty proposition; ADR-004 positioning | Reviewer raises cluster-conflation | Deploy ADR-004 O1+O3 rebuttals; P09 red-team pre-tested | Open |
| R008 | **Tool unavailability:** Consensus / NotebookLM / Semantic Scholar outage stalls literature work. | 2 | 2 | 4 | Agent | P0.5–P09 | RPF v2.0 fallback table (§XI.7) | Tool down > 24h | Fallback per table; flag in audit doc | Closed (P0.5/P01) |
| R009 | **HUMAN-GATE SLA stall:** PI unavailable > 48h at a gate. | 2 | 3 | 6 | Agent | all | SLA + escalation path (RPF §XI.2); conservative fallbacks (RE-GATE / NO-GO) | Gate wait > 48h | Escalate Agent → PI → Dept head (>7d); apply fallback | Open |
| R010 | **Cross-benchmark generality failure:** threshold law does not transfer from H-Bar to SCAN/COGS (CLM-007). | 3 | 4 | 12 | Agent | P06 | CLM-007 flagged `keep` with P06 verification; benchmark choice pre-registered in P04 | P06 transfer results contradict CLM-001 | Scope claim to H-Bar via ADR; report boundary condition | Open |
| R011 | **Deadline / wall-clock slippage** vs. 45-day budget. | 3 | 2 | 6 | Agent | all | `budget.md` tracking; +20 % slack; 80 % alert | Any phase > 120 % estimate | Re-scope non-critical phases; inform PI | Open |

**Abort / escalation triggers (RPF §XI.1):** same exit criteria failing 3× · compute >20 % over · output contradicting gate binding constraints · ledger↔artifact mismatch >3 · gate SLA exceeded without fallback · critical CVE.
