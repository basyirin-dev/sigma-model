"""Σ-Model H-Bar experiment logic (Phase 04 mechanism gate).

Ported from the canonical pilot notebook ``archive/experiments/h-bar-experiment.ipynb``
(cells 1–5), keeping the training dynamics verbatim for parity with the archived
results, and adding the measured Stage-1 proxy (GCA + RGA) for the σ-leading
indicator test.

Modules:
- ``hbar_data``  — benchmark generators + dataset/loader plumbing
- ``hbar_model`` — ``HBarTransformer`` seq2seq model (+ ``encode()`` for probing)
- ``hbar_train`` — training harness (baseline / fixed_weight / additive / multiplicative)
"""
