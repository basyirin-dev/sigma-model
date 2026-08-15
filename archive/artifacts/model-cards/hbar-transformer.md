# Model Card: HBarTransformer

## Model Details
- **Architecture:** 2-layer, 4-head Transformer (seq2seq)
- **Embedding dim:** 128
- **Feedforward dim:** 512
- **Dropout:** 0.1
- **Positional encoding:** Sinusoidal, max length 500
- **Parameters:** ~1.2M (vocab-size dependent)

## Intended Use
Baseline model for Σ-Model ODE validation experiments. Trained on synthetic SCAN-like compositional data.

## Training Details
- **Optimizer:** Adam (lr=0.001)
- **Batch size:** 64
- **Steps:** 2000
- **Gradient clipping:** 1.0
- **Mixed precision:** FP16 on CUDA

## Evaluation
- **ID accuracy:** >99% on random splits (target)
- **OOD accuracy:** Varies by condition (baseline ~2%, additive/multiplicative up to ~30%)
- **Metrics:** OOD gap, sigma_A trajectory, phase transition timing

## Limitations
- Small model, not intended for production deployment
- Synthetic data only (SCAN-like primitives)
- 2000-step training does not reach full convergence

## References
- Paper: `/paper/paper.md` §11.1
- Source: `/code/sigma/models/transformer.py`
- Config: `/experiments/configs/base.yaml`
