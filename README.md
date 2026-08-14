# Σ-Align: Schema Coherence Framework for AI Alignment and AGI Safety

**Core thesis:** *Compositional generalization failure and AI alignment failure are the same phenomenon — a bifurcation in the agent's internal schema coherence (the σ-trap) — and solving one solves the other.*

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
| 9 | Implications: Schema-Coherent Training for Safe AGI | Paper 09 (Final Scoping) | ⚪ Pending |
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
