#!/usr/bin/env python3
"""
Paper 02 — Phase 5 Screening Rules Configuration

Encodes the Phase 1 PICO inclusion/exclusion criteria and the σ-trap
lexicon (compositional generalization / OOD failure) as machine-checkable
rules for the deterministic screening passes.

Exclusion reason codes (per Phase 5 protocol):
  E1: Not about neural network models
  E2: Not about OOD / compositional generalization
  E3: No empirical results (opinion only)
  E4: Duplicate (missed in Phase 4)
  E5: Not in English
  E6: Outside date range (2017-2026)
  E7: Other (specify)
"""

from __future__ import annotations

# ── I: Date window ────────────────────────────────────────────────────
DATE_MIN = 2017   # SCAN preprint year (Lake & Baroni 2018 benchmark)
DATE_MAX = 2026

# ── I: PICO operationalization ────────────────────────────────────────
# Population: NN models trained on compositional/OOD tasks
# Intervention: OOD/CG performance on held-out recombination split
# Comparison: baseline (SGD) or ID accuracy alongside
# Outcome: quantitative ID + OOD accuracy

# ── Exclusion reason codes ────────────────────────────────────────────
REASON_CODES = {
    "E1": "Not about neural network models (population)",
    "E2": "Not about OOD / compositional generalization (intervention/outcome)",
    "E3": "No empirical results / opinion only (study design)",
    "E4": "Duplicate publication (keep most complete)",
    "E5": "Not in English (language)",
    "E6": "Outside date range 2017-2026 (date)",
    "E7": "Other (see notes)",
}

# Decision labels
INCLUDE = "Include"
EXCLUDE = "Exclude"
UNCERTAIN = "Uncertain"

# ── P: Neural-network population markers ──────────────────────────────
NN_TERMS = [
    "neural network", "neural networks", "neural net", "deep learning",
    "deep net", "transformer", "transformers", "lstm", "rnn", "gru",
    "cnn", "mlp", "encoder-decoder", "encoder decoder", "seq2seq",
    "sequence-to-sequence", "attention", "language model", "language models",
    "llm", "llms", "gpt", "bert", "roberta", "bart", "t5", "word2vec",
    "gradient descent", "sgd", "adam", "backpropagation", "back-propagation",
    "feedforward", "feed-forward", "convolutional", "recurrent",
    "reinforcement learning", "policy gradient", "ppo", "dqn", "ddqn",
    "model training", "fine-tun", "finetun", "pretrain", "pre-train",
    "embedding", "encoder", "decoder", "hidden state", "representations",
    "parameter", "weights", "architecture", "layers", "activation",
    "neurons", "perceptron", "resnet", "vit", "vae", "gan", "diffusion model",
    "graph neural", "gnn", "bayesian neural",
]

# ── I: Compositional / OOD generalization vocabulary ──────────────────
# TIGHTENED per calibration: only compositional/systematic generalization
# (σ-trap target). Domain generalization, bare OOD, flat-minima, corruption
# robustness, and transfer learning are NOT compositional -> E2.
CG_TERMS = [
    # Core concepts (compositional / systematic)
    "compositional generalization", "compositional generalisation",
    "systematic generalization", "systematic generalisation",
    "structural generalization", "structural generalisation",
    "combinatorial generalization", "combinatorial generalisation",
    "algebraic generalization", "algebraic generalisation",
    "compositional learning", "systematicity", "productivity",
    "compositional skills", "compositional zero-shot", "compositional understanding",
    "novel composition", "novel combinations", "compositional structure",
    "recombina", "primitive recombination", "length generalization",
    "length generalisation", "compound divergence", "compositional split",
    "systematic zero-shot", "compositional generalization accuracy",
    "compositional generalisation accuracy", "compositional accuracy",
    # OOD family (only when tied to generalization performance, not detection)
    "out-of-distribution generalization", "out-of-distribution generalisation",
    "ood generalization", "ood generalisation", "ood accuracy",
    "ood performance", "id-ood gap", "ood gap", "distribution shift generalization",
    # Failure modes (compositional / shortcut)
    "generalization failure", "generalisation failure", "compositional failure",
    "shortcut learning", "spurious correlation", "spurious feature",
    "non-causal feature", "clever hans", "dataset bias exploitation",
    # Benchmarks (compositional generalization diagnostics)
    "scan benchmark", "scan dataset", "scan task", "cogs", "recogs",
    "cfq", "gscan", "pcfg-set", "pcfg set", "closure", "slog",
    "sqoop", "cofe", "geoquery", "multiscan", "metalscan",
    "semantic parsing", "text-to-sql", "compositional semantic",
]

# Terms that look like OOD/CG but are NOT compositional (calibration):
# domain generalization, domain adaptation, OOD detection, corruption
# robustness, flat minima, transfer learning, cross-domain few-shot.
NON_COMPOSITIONAL_TERMS = [
    "domain generalization", "domain generalisation", "domain adaptation",
    "domain shift", "cross-domain", "cross domain", "domain-invariant",
    "ood detection", "out-of-distribution detection", "anomaly detection",
    "novelty detection", "outlier detection", "open-set", "open set",
    "corruption", "image corruption", "perturbation robustness",
    "weather", "noise robustness", "adversarial robustness",
    "flat minima", "sharpness-aware", "sharpness aware", "loss landscape",
    "transfer learning", "few-shot", "meta-learning", "multi-task learning",
    "semi-supervised", "self-supervised", "contrastive learning",
    "lottery ticket", "model compression", "knowledge distillation",
    "quantization", "pruning", "sparsity", "neural architecture search",
    "interatomic", "molecular", "materials", "physics-informed",
    "fault diagnosis", "plant", "crop", "remote sensing", "medical",
    "clinical", "tumor", "lesion", "skin lesion", "fraud", "intrusion",
    "macroeconomic", "financial", "weather forecasting", "blast wave",
    "lip sync", "video interpolation", "face verification", "recognition system",
]

# ── O: Quantitative-outcome markers ───────────────────────────────────
QUANT_TERMS = [
    "accuracy", "error rate", "performance", "f1", "exact match",
    "precision", "recall", "bleu", "perplexity", "success rate",
    "generalization accuracy", "test accuracy", "o od accuracy",
    "empirical", "experiment", "results", "evaluation", "evaluate",
    "benchmark", "dataset", "accuracy of", "report", "we show",
]

# ── E2-disambiguation: OOD-detection / anomaly (exclude) ──────────────
OOD_DETECTION_TERMS = [
    "ood detection", "out-of-distribution detection", "anomaly detection",
    "novelty detection", "outlier detection", "anomaly score",
    "open-set recognition", "unknown detection", "adversarial detection",
    "trojan detection", "backdoor detection", "ood detector",
    "distribution shift detection", "drift detection", "concept drift",
]

# ── E1-exclusion: not-neural-network domains ──────────────────────────
NON_NN_DOMAINS = [
    "biological neural", "human brain", "cognitive model of",
    "behavioral economics", "supply chain", "logistics optimization",
    "portfolio optimization", "scheduling problem", "genetic algorithm",
    "swarm intelligence", "fuzzy logic system", "expert system",
    "control theory of", "aerospace", "mechanical", "materials",
]

# ── E3-exclusion: opinion / non-empirical markers ─────────────────────
OPINION_TERMS = [
    "opinion", "perspective", "viewpoint", "commentary", "reflections on",
    "thoughts on", "a call for", "position paper", "manifesto",
    "open letter", "letter to the editor", "editorial",
]

# ── E5: non-Latin scripts ─────────────────────────────────────────────
NON_LATIN_RANGES = [
    (0x4E00, 0x9FFF), (0x3040, 0x30FF), (0x0400, 0x04FF),
    (0x0600, 0x06FF), (0x0370, 0x03FF), (0x0590, 0x05FF),
    (0xAC00, 0xD7AF), (0x0E00, 0x0E7F),
]

# ── Narrow/off-topic application domains (E7 / E2) ────────────────────
OFF_TOPIC_DOMAINS = [
    "face recognition", "medical image segmentation", "tumor detection",
    "traffic sign", "self-driving perception", "video surveillance",
    "recommender system", "recommendation system", "fraud detection",
    "credit scoring", "spam detection", "sentiment analysis of product",
    "stock prediction", "weather forecasting", "speaker verification",
    "speech enhancement", "image super-resolution", "image denoising",
    "colorization", "style transfer of", "text-to-speech",
]
