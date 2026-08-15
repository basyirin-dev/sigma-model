# Datasheet: COGS Dataset

## Description
COGS (Compositional Generalization Challenge) is a semantic parsing dataset testing lexical and structural compositionality.

## Source
Kim, N., & Linzen, T. (2020). COGS: A Compositional Generalization Challenge. *Proceedings of EMNLP 2020*.

## Access
Archived in `/hackathon/COGS/` (zip archive). Extracted directory is gitignored.

## Splits Used
- **train:** Training examples
- **dev:** Validation
- **test:** Standard test
- **gen:** OOD generalization split

## Modifications for Σ-Model
- **H-MCB:** Self-model elicitation protocol (Stage 1 prediction + Stage 2 performance)
- **H-DCB:** RAG wrapper injected with retrieval density sweep (rho levels)
- **H-STB:** Dyadic communication protocol with Schema/Fact/Mixed conditions

## License
Original dataset released under MIT License.

## References
- Kim & Linzen (2020): https://doi.org/10.18653/v1/2020.emnlp-main.693
