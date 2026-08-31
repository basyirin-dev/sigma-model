# Plain-Language Summary: The $\Sigma$-Model & The $\sigma$-Trap

## What is this research about?
Modern AI systems like Large Language Models often memorize patterns exceptionally well on familiar examples but fail when required to combine known rules in brand-new ways (compositional reasoning). This project investigates the mathematical and dynamical reasons why AI models fall into this failure mode during training.

## What is the $\sigma$-trap?
We model the training process as a dynamical system with two competing forces:
1. **Depth/Syntax processing ($D$):** Learning superficial structural patterns.
2. **Schema coherence ($S$):** Internalizing compositional, reusable rules.

Standard gradient descent often falls into an equilibrium we term the **$\sigma$-trap**, where the model rapidly accumulates depth while suppressing schema coherence. As a result, the model performs near 100% on standard benchmark tests but drops sharply on out-of-distribution reasoning.

## Why does it matter?
Understanding the dynamical phase boundaries and bifurcation conditions allows researchers to design targeted interventions, specialized architectures, and training curriculums that guide neural networks toward true compositional generalization.
