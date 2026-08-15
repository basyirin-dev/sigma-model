# Datasheet: PCFG-SET Dataset

## Description
PCFG-SET (Probabilistic Context-Free Grammar – Systematicity Evaluation Test) tests three dimensions of compositionality: productivity, systematicity, and substitutivity.

## Source
Hupkes, D., et al. (2020). Compositionality decomposed: How do neural networks generalise? *Journal of Artificial Intelligence Research*.

## Access
Archived in `/hackathon/am-i-compositional/` (zip archive). Extracted directory is gitignored.

## Splits Used
- **train:** Standard training split
- **test:** Standard test split
- **systematicity:** OOD systematicity evaluation

## Modifications for Σ-Model
- **H-PTB:** Four training conditions (A–D), contrastive pairs for structure-targeted training

## License
Original dataset released under Apache 2.0.

## References
- Hupkes et al. (2020): https://doi.org/10.1613/jair.1.11974
