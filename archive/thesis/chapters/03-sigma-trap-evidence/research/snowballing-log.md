# Snowballing / Citation Chasing Log

**Date:** 2026-07-08
**Method:** Semantic Scholar citation graph + targeted DOI lookups
**Status:** Partial (rate-limited; manual follow-up recommended)

---

## Seed Papers Attempted

| Seed paper | Direction | Results | Notes |
|------------|-----------|---------|-------|
| Lake & Baroni 2023 (MLC) — DOI:10.1038/s41586-023-06668-3 | Forward | 20 citations | Mostly off-topic (materials science, engineering) — Semantic Scholar no longer provides field-of-study filtering |
| Hupkes et al. 2020 (PCFG-SET) — DOI:10.1613/jair.1.11674 | Forward | 20 citations | Some relevant CG papers mixed with noise |
| Lake & Baroni 2018 (SCAN) — arXiv:1711.00350 | Forward | Rate limited (429) | Retry later |

---

## Papers Found via Snowballing

These are papers NOT yet in our result set that were discovered via citation chasing:

| Paper | Year | Found via | Notes |
|-------|------|-----------|-------|
| Herzig & Berant 2021 (SpanBasedSP) — arXiv:2104.07478 | 2021 | MLC citations | Already captured by benchmark-specific search |
| Jarvis et al. — "Compositionality and systematicity emerge from iterated learning in deep linear networks" — PNAS 2026, DOI:10.1073/pnas.2509739123 | 2026 | PCFG-SET citations | Directly relevant — theory of compositionality emergence |
| Fu & Liu — "RL for Compositional Generalization with Outcome-Level Optimization" — arXiv:2605.04920 | 2026 | PCFG-SET citations | Intervention study — RL-based CG optimisation |
| Lu et al. — "Adversarial Concept Search: Predicting Compositional Errors From Feature Geometry" — arXiv:2606.13934 | 2026 | PCFG-SET citations | Probing study — predicting CG failures from representations |
| Cheng & Lippl — "A mathematical theory of balancing relational generalization and memorization" — arXiv:2605.22972 | 2026 | PCFG-SET citations | Theory paper on relational generalisation |

---

## Recommended Follow-Up

1. Retry snowballing after 60s (Semantic Scholar rate limit reset)
2. Use OpenAlex instead for better field-of-study filtering
3. Prioritise backward snowballing (references of landmark papers) — more targeted than forward
4. Key papers for backward snowballing:
   - Lake & Baroni 2018 (references seminal CG work)
   - Hupkes et al. 2020 (references pre-2020 CG evaluations)
   - Geirhos et al. 2020 (references shortcut learning research)
