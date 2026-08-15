# Σ-Model — Schema-Coherence Suppression & Compositional Generalisation Failure

A dynamical-systems framework for compositional generalisation failure. Core idea:
standard gradient-based training drives agents into a stable low-schema-coherence
equilibrium (the **σ-trap**) — high in-distribution accuracy coexists with
systematic out-of-distribution compositional failure because depth accumulates
while schema coherence is suppressed.

The active deliverable is a single narrow manuscript (the **σ-Trap paper**,
targeting TMLR after the JAIR desk-rejection) plus an arXiv companion technical
report preserving the extended framework (proxy architecture, cognitive
extensions, multimodal coverage, benchmark protocol).

---

## Repository Structure

| Path | Contents |
|:-----|:---------|
| `paper/` | σ-Trap manuscript (TMLR format) + arXiv companion (`paper/companion/`) + planning docs (`paper/planning/`) |
| `code/sigma_align/` | Reusable Python package (ODE, config, utils, monitoring, evaluation) |
| `archive/` | Read-only historical artifacts: thesis monograph (`archive/thesis/`), decision docs (`archive/Σ-Align/`), old code, datasets, experiment results. Do not modify. |
| `docs/adrs/` | Architecture Decision Records |
| `hbar_env/` | Python virtual environment |

## Current Status

- Paper 06 (Σ-Model) was desk-rejected by JAIR (2026-07-15) on exposition/notation,
  overbroad claims, and scope grounds. Pivoting: **narrow σ-Trap paper → arXiv → TMLR**,
  experiment-gated. See `paper/planning/roadmap.md` for the phase plan.
- The thesis monograph (10 chapters) and AGI-safety publication pipeline are
  **archived** (reversible via git) — the project is re-centered on the
  dynamical-systems account of compositional generalisation failure.

## Build

| Task | Command |
|:-----|:--------|
| Build the paper PDF | `make paper06` (from root) or `make pdf` (from `paper/`) |
| Lint | `ruff check code/sigma_align/` |
| Run evaluation | `PYTHONPATH=code:$PYTHONPATH python -m sigma_align.monitoring.evaluation` |
| CLI | `sigma-evaluate` (installed via `pip install -e .`) |

Activate the venv first: `source hbar_env/bin/activate`.

## Citation

```bibtex
@misc{sigma-model2026,
  title={The {$\Sigma$}-Model: Schema-Coherence Suppression as a Dynamical
         Mechanism of Compositional Generalisation Failure},
  author={{Basyirin Amsyar Basri}},
  year={2026}
}
```

## License

MIT
