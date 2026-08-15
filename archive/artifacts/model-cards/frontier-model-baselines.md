# Model Card: Frontier Model Baselines

## Models
| Model | Provider | Version | Access |
|-------|----------|---------|--------|
| GPT-4 | OpenAI | Latest (2026) | Kaggle SDK |
| Claude 3.5 Opus | Anthropic | Latest (2026) | Kaggle SDK |
| Gemini 1.5 Pro | Google DeepMind | Latest (2026) | Kaggle SDK |

## Evaluation Protocol
- **Temperature:** 0.0 (greedy decoding) for all scoring runs
- **Runs per model:** 5
- **Platform:** Kaggle Community Benchmarks SDK

## Benchmarks Evaluated
- H-PTB (Learning)
- H-AFB (Attention)
- H-MCB (Metacognition)
- H-DCB (Executive Functions)
- H-STB (Social Cognition)

## Status
Evaluation pending Kaggle deployment. Results expected post-June 1, 2026.

## References
- Protocol: `/experiments/configs/` (per benchmark)
- Payload generation: `/code/sigma/benchmarks/payload.py`
