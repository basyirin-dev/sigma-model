# ADR-010: Computational Kernels, Modular Models, and Whitened GCA Engine

## 1. Context & Status
- **Status:** **APPROVED**
- **Date:** 2026-08-25
- **Deciders:** Principal Investigator, Lead Research Agent
- **Phase:** Phase 05 (Computational Implementation & Unit-Tested Kernels)
- **Framework:** RPF v2.0.0 — Tasks 5.1–5.4
- **Prerequisites:**
  - `paper02/decisions/ADR-007_multi_benchmark_experimental_matrix.md`
  - `paper02/decisions/ADR-008_diagnostic_toolchain_and_analysis_engines.md`
  - `paper02/decisions/ADR-009_statistical_power_and_protocol.md`

---

## 2. Mathematical Formalizations & Decisions

### 2.1 Whitened Gradient Cosine Alignment (GCA)
In standard neural sequence models, input token embedding matrices $E \in \mathbb{R}^{V \times D}$ share massive gradient alignment at step 0 ($g_A(0) \approx 0.95$) purely due to shared token co-occurrence in batches, creating an artificial initialization artifact.

To isolate true task vs compositional gradient alignment in intermediate layers:
$$g_A^{\text{proj}}(t) = \text{CosSim}\left( (I - P_{\text{emb}}) \nabla_\theta \mathcal{L}_{\text{comp}}, \; (I - P_{\text{emb}}) \nabla_\theta \mathcal{L}_{\text{train}} \right)$$
where $P_{\text{emb}}$ is the orthogonal projection operator onto the parameter subspace of token embeddings.
- **Invariant:** At random initialization, $g_A^{\text{proj}}(0) \approx 0.0 \pm 0.05$.
- **Transcritical Signature:** When $\lambda > \lambda_{\text{crit}}$, $g_A^{\text{proj}}(t) > 0.5$ in encoder/decoder self-attention layers.

### 2.2 Continuous Solver Invariants & Tolerances
- **Integrators:** Stiff `Kvaerno5` and adaptive `Tsit5` / `Radau` integrators.
- **Tolerances:** Absolute tolerance $\text{atol} = 10^{-8}$, Relative tolerance $\text{rtol} = 10^{-8}$.
- **Invariant Assertions:** State space clipping and assertion: $u(t) \in [0, 1]$, $v(t) \in [0, 1]$ for all $t \ge 0$.

### 2.3 Modular Architecture Specifications
- **Architecture A (2-Layer Transformer):** $d_{\text{model}} = 128, n_{\text{heads}} = 4, n_{\text{layers}} = 2, d_{\text{ff}} = 512$.
- **Architecture B (4-Layer Transformer):** $d_{\text{model}} = 256, n_{\text{heads}} = 8, n_{\text{layers}} = 4, d_{\text{ff}} = 1024$.
- **Architecture C (Recurrent Seq2Seq):** $d_{\text{model}} = 128, d_{\text{hidden}} = 128, n_{\text{layers}} = 2$ GRU/SSM.

---

## 3. Consequences & Governance
- All models, dataloaders, and diagnostic engines must be unit-tested ($\ge 3$ tests per kernel per CC.2.2).
- Completes all requirements of Phase 05.
