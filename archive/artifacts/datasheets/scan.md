# Datasheet: SCAN Dataset

## Description
SCAN (Semantic Cognition and Compositional Generalisation) is a synthetic command->action dataset. Commands like "jump twice" map to action sequences like "JUMP X2".

## Source
Lake, B. M., & Baroni, M. (2018). Generalization without systematicity. *Proceedings of the National Academy of Sciences*.

## Access
Archived in `/hackathon/SCAN/` (zip archive). Extracted directory is gitignored.

## Splits Used
- **train:** Standard simple split training examples
- **test:** Standard simple split test examples
- **add-primitive:** OOD evaluation split

## Modifications for Σ-Model
- **H-AFB:** Surface confound (colour token) injected for OOD-Surface-Conflict condition
- New primitives added: "look", "opposite"

## License
Original dataset released under CC BY 4.0.

## References
- Lake & Baroni (2018): https://doi.org/10.1073/pnas.1809542115
