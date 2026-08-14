# Σ-Align: Schema Coherence Framework for AI Alignment and AGI Safety

**Core thesis (three-tier, cumulative):** *Schema coherence is a measurable property of learned representation structure whose deterioration can produce a stable low-coherence regime (the σ-trap) associated with systematic generalisation failure.* The same mechanism provides a testable account of some safety-relevant forms of objective divergence, and — if it persists in more capable systems — schema-coherent training may be a candidate component of alignment strategy. (Identity formulation "CG failure = alignment failure" is documented but not the working claim.)

---

## Repository Structure

| Path | Contents |
|:-----|:---------|
| `paper/` | Sigma-Model manuscript (Paper 06, JAIR → TMLR) |
| `thesis/` | Monograph — 10 chapters, front/back matter, publications, planning docs |
| `code/sigma_align/` | Reusable Python package (ODE, config, utils, monitoring) |
| `Σ-Align/` | Decision documentation (MCDAs, audit trails, errata, methodology) |
| `docs/adrs/` | Architecture Decision Records |
| `archive/` | Protein-domain artifacts (read-only historical reference) |
| `hbar_env/` | Python virtual environment |

## Monograph (Chapters)

The thesis is written as a **monograph** (chapter-based prose). Completed publications
are adapted into chapters; their venue manuscripts are archived in `thesis/publications/`.

| Ch | Chapter | Source | Status |
|:--:|:--------|:-------|:-------|
| 1 | Introduction | original | 🟢 Drafted |
| 2 | The Landscape of AGI Safety | Paper 01 (Scoping Review) | 🟡 Adapting |
| 3 | Schema Coherence and the σ-Trap | Paper 02 (Systematic Review) | 🟡 Pending |
| 4 | The Σ-Align Framework | Paper 03 (Conceptual) | ⚪ Pending |
| 5 | σ-Coupling Interventions | Paper 04 (Pilot Study) | ⚪ Pending |
| 6 | Quantifying the σ-Trap | Paper 05 (Meta-Analysis) | ⚪ Pending |
| 7 | The Σ-Model | Paper 06 (Empirical #1) | 🟢 Source complete |
| 8 | Mesa-Optimization via Schema Coherence | Paper 07 (Empirical #2) | ⚪ Pending |
| 9 | What Schema Coherence Can and Cannot Tell Us About Alignment | Paper 09 (Final Scoping) | ⚪ Pending |
| 10 | Conclusion | original | ⚪ Pending |

Build the monograph with `make monograph` (from repo root).

See [`thesis/narrative.md`](thesis/narrative.md) for the full arc and roadmap.

## Citation

```bibtex
@misc{sigma-align2026,
  title={{\Sigma}-Align: Schema Coherence and the {$\sigma$}-Trap
         in {AGI} Safety and Alignment},
  author={{Basyirin Amsyar Basri}},
  howpublished={PhD thesis (monograph)},
  year={2026}
}
```

## License

MIT
