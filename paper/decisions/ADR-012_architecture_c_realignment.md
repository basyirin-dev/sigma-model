# ADR-012: Architecture C Realignment to Gated Recurrent Seq2Seq (GRU)

## 1. Context & Status
- **Status:** **APPROVED (Ratified by PI Directive 2026-08-27)**
- **Date:** 2026-08-27
- **Deciders:** Principal Investigator, Lead Research Agent
- **Phase:** Pre-Phase 06 Governance Remediation
- **Framework:** RPF v2.0.0
- **Supersedes:** Legacy Mamba/SSM configuration entries in `matrix_p04.yaml`.

---

## 2. Decision: Designation of Architecture C as GRU Seq2Seq Baseline

### 2.1 Scientific Rationale
The scientific objective of Architecture C in Paper 02 is to evaluate the cross-architecture universality of the Two-Subspace Critical Pressure Law ($\lambda_{\text{crit}} = b_C / a_C$) beyond multi-head self-attention mechanisms.

While State-Space Models (Mamba / S4) were originally considered during early planning, they introduce complex CUDA-level compiled dependencies that impair CPU-only smoke testing, clean-room Docker builds (CC.1.8), and standalone Kaggle kernel portability.

A standard 2-layer Gated Recurrent Unit (GRU) encoder-decoder:
1. Eliminates multi-head self-attention, providing a strict test of non-attention compositional dynamics.
2. Runs seamlessly across CPU, local GPU, and Kaggle environments without specialized C++ extensions.
3. Is fully implemented in `paper/src/models/recurrent.py` (`RecurrentSeq2Seq`) and covered by unit tests in `paper/tests/test_recurrent.py`.

### 2.2 Formal Specification
```yaml
arch_c_recurrent_gru:
  family: "recurrent"
  name: "Gated Recurrent Seq2Seq (GRU)"
  model_class: "RecurrentSeq2Seq"
  rnn_type: "GRU"
  d_model: 128
  d_hidden: 128
  num_layers: 2
  dropout: 0.1
  max_seq_len: 64
```

---

## 3. Consequences & Governance
- `matrix_p04.yaml` replaces `arch_c_ssm_mamba` with `arch_c_recurrent_gru`.
- All exploratory Architecture C runs in Tier 2 use `RecurrentSeq2Seq`.
- Deprecates Mamba-specific fields (`d_state`, `d_conv`, `expand`).
