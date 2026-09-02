# ADR 0005: The Defining Paper (was "Paper 02") is the Single Active Deliverable

**Date:** 2026 (repository restructure)
**Status:** Accepted
**Author:** Principal Investigator + repository maintenance

## Context

The Σ-Model research programme evolved through a sequence of manuscripts. The σ-Trap manuscript (historically "Paper 06 v2", then "Paper 01 v2") was submitted to TMLR on OpenReview and **rejected**. Its content — the low-schema-coherence σ-trap equilibrium, the phenomenological ODEs, and the associated figure set — was subsequently **absorbed into a broader, ultimately defining manuscript**: *"Critical Compositional Pressure: A Phase-Boundary Framework for Compositional Representation Formation in Neural Networks"* (formerly labelled "Paper 02").

The repository still reflected the superseded structure: `AGENTS.md` named "Paper 01 v2" as the active deliverable, the root `Makefile` defaulted to `make paper01`, and `paper01/` sat alongside `paper/` as if it were a peer, active project. The README led with the defining paper while the build entry points and agent instructions pointed at the rejected one — an internal inconsistency.

## Decision

1. **The defining paper is the single active deliverable.** It lives under `paper/`. It is no longer referred to as "Paper 02" (a subordinate label); it is the capstone manuscript that absorbed the σ-Trap results.
2. **Paper 01 is superseded and archived.** The rejected σ-Trap manuscript (source, companion, figures, submission package) is moved to `archive/paper01/` and treated as read-only historical reference. It is not edited and not re-served as a peer deliverable.
3. **Build targets and docs follow the defining paper.** The root `Makefile` default (`paper`), `AGENTS.md`, and `README.md` all target `paper/`. The old `paper01`, `companion`, and `paper01`-specific `arxiv` targets are removed.
4. **`paper/src/` is the canonical code tree** for the defining paper. The legacy `sigma_align` package under `code/` is retained for now but flagged for retirement (superseded by `paper/src/`).
5. **Authoritative metrics identifiers are untouched.** Git tags and commit anchors referenced by the scientific record (e.g. `v2.0-paper02`, `p02.5-preregistered`, `69e1f57b`, `540c992`) are immutable provenance and are preserved verbatim; only the *path* `paper02/` is renamed to `paper/`.

## Consequences

- The rejected manuscript is preserved as read-only history and remains recoverable from `archive/paper01/` (and git history), while the live tree now has a single, coherent deliverable.
- Contributors can no longer be misled into editing, building, or citing the superseded manuscript as the active paper.
- The defining paper is free to present the full programme (phenomenological ODEs **plus** the absorbed σ-Trap results), replacing the narrower scoping that constrained the rejected σ-Trap paper.
- Follow-up consolidation (dependency unification, CI, retiring `code/`, ledger merge) builds on this flattened, single-paper layout.

## Follow-ups

- Merge the superseded σ-Trap claim ledger into the defining paper's `paper/planning/ledger.md`.
- Retire the legacy `code/sigma_align` package in favour of `paper/src/`.
- Migrate CI from `.antigravity/ci/` to `.github/workflows/` and pin the Python environment to the project's declared matrix.
