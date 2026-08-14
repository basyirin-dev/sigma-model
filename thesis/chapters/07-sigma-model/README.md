# Chapter 7: The Σ-Model — Compositional Generalisation Failure

**Source**: Paper 06 — *Σ-Model: Schema-Coherence Suppression as the Origin of Compositional Generalisation Failure* (Empirical #1)
**Status**: 🟢 Source complete — chapter adaptation pending; extracted Paper 06 desk-rejected by JAIR 2026-07-15, pivoting to TMLR (see `Σ-Align/10-jair-desk-rejection-response.md`)
**Venue manuscript**: `paper/` (root; symlinked from `thesis/publications/06-sigma-model/manuscript`)
**Timeline**: Months 1–12
**Role**: The **flagship empirical chapter** (external assessment F4/F11). The thesis's core
claim stands or falls here.

## Flagship Question

> **Can a minimal learning system exhibit a transition from compositional to non-compositional learning that is predicted by an independently measurable schema-coherence variable?**

## σcrit Dynamical-Systems Checklist (required)

1. Multiple equilibria / qualitatively distinct regimes.
2. A parameter controlling the transition (σcrit).
3. Hysteresis or basin structure, if claimed.
4. Stability analysis.
5. Reproducibility across initial conditions.
6. Robustness to parameterisation.
7. **σ-causes-vs-accompanies distinction**: evidence that σ is causally implicated in the
   bifurcation, not merely a quantity that changes alongside it.

## Non-Toy Validation (required — assessment A2/F8)

The TMLR revision must address the JAIR desk-rejection grounds (exposition, overbroad claims,
scope) **and** validate the bifurcation on at least one modern non-toy architecture (e.g. a
small Transformer or SSM), not only the phenomenological ODE / small-MLP setting — so that
examiners cannot dismiss the result as a toy-model artefact. Alternative explanations
(competing-hypotheses section, CC.4.8) must be explicitly ruled out.

See `phases/` for chapter phase roadmaps (to be created).
