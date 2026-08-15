#!/usr/bin/env python3
"""
Paper 01 — Phase 5 Screening Rules Configuration

Encodes the Phase 1 protocol inclusion/exclusion criteria (I1-I5, E1-E6)
and the 21-subdomain controlled vocabulary (§B.1 of protocol draft) as
machine-checkable rules for the deterministic screening pass.
"""

from __future__ import annotations

# ── I2: Date window ───────────────────────────────────────────────────
DATE_MIN = 2015          # AlphaGo / modern deep-learning safety (inclusive)
DATE_MAX = 2026          # March 2026 cutoff; year-level granularity only

# ── I1/E2: Language ───────────────────────────────────────────────────
# Non-Latin script ranges (CJK, Cyrillic, Arabic, Greek, etc.)
NON_LATIN_RANGES = [
    (0x4E00, 0x9FFF),   # CJK Unified Ideographs
    (0x3040, 0x30FF),   # Hiragana + Katakana
    (0x0400, 0x04FF),   # Cyrillic
    (0x0600, 0x06FF),   # Arabic
    (0x0370, 0x03FF),   # Greek
    (0x0590, 0x05FF),   # Hebrew
    (0xAC00, 0xD7AF),   # Hangul
    (0x0E00, 0x0E7F),   # Thai
]

# ── I3: 21-subdomain controlled vocabulary (§B.1) ─────────────────────
SUBDOMAINS = {
    # Level 1 — General
    "AGI Safety": ["agi safety", "agi risk", "artificial general intelligence safety",
                   "general intelligence safety", "existential risk from ai",
                   "existential risk from artificial intelligence", "xrisk",
                   "existential safety", "ai safety", "long-term ai safety",
                   "long-term artificial intelligence safety"],
    "AI Alignment": ["ai alignment", "alignment of ai", "alignment research",
                     "alignment problem", "aligning ai", "aligning artificial"],
    "Value Alignment": ["value alignment", "value-aligned", "value alignment problem",
                        "aligned values", "aligning values"],
    # Level 2 — Technical Alignment
    "Inner Alignment": ["inner alignment", "inner misalignment"],
    "Outer Alignment": ["outer alignment", "outer misalignment"],
    "Mesa-optimisation": ["mesa-optimization", "mesa-optimisation", "mesa optimization",
                          "mesa optimizers", "mesa-optimizer", "learned optimization",
                          "risks from learned optimization"],
    "Deceptive Alignment": ["deceptive alignment", "deceptive misalignment", "alignment faking",
                            "sleeper agent", "sleeper agents", "scheming", "deception in llms"],
    "Corrigibility": ["corrigibility", "corrigible", "off-switch", "off switch game",
                      "shutdown problem", "shutdownable", "interruptibility",
                      "incorrigibility", "incorrigible"],
    "Goal Preservation": ["goal preservation", "goal misgeneralization", "goal misgeneralisation",
                          "goal preservation in", "preserving goals"],
    # Level 3 — Diagnostic
    "Interpretability (Mechanistic)": ["mechanistic interpretability", "interpretability",
                                       "interpretable", "interpretability research",
                                       "circuit analysis", "superposition", "feature geometry",
                                       "toy models of", "sparse autoencoder", "activation patching",
                                       "representation engineering"],
    "Robustness": ["robustness", "robust ai", "robustness to", "distribution shift",
                   "out-of-distribution", "out of distribution", "ood generalization",
                   "adversarial robustness", "robust generalization"],
    "Specification Gaming": ["specification gaming", "specification game", "reward hacking"],
    "Reward Hacking": ["reward hacking", "reward hacks", "reward model hacking",
                       "reward over-optimization", "reward overoptimisation"],
    # Level 4 — Value Specification
    "Coherent Extrapolated Volition": ["coherent extrapolated volition", "cev", "extrapolated volition"],
    "Indirect Normativity": ["indirect normativity", "normativity", "normative uncertainty"],
    # Level 5 — Bridging Concepts
    "Schema Coherence": ["schema coherence", "coherence of representations", "representational coherence",
                         "schematic coherence", "coherent schema"],
    "Compositional Generalisation": ["compositional generalization", "compositional generalisation",
                                     "systematic generalization", "systematic generalisation",
                                     "compositional learning", "compositional zero-shot"],
    "Internal Representation Structure": ["internal representation", "representation structure",
                                          "representational structure", "latent structure",
                                          "latent space structure", "internal structure of"],
    "Natural Abstractions": ["natural abstraction", "natural abstractions"],
    "Latent Ontology": ["latent ontology", "ontological crisis", "ontology of", "latent world model"],
    "Feature Geometry": ["feature geometry", "feature geometry of", "linear representation",
                         "representational geometry"],
}

# ── I5: Structural safety framing terms ───────────────────────────────
STRUCTURAL_SAFETY_TERMS = [
    "alignment", "aligning", "corrigib", "mesa-optim", "deceptive", "goal misgeneraliz",
    "goal preservation", "specification gaming", "reward hacking", "reward model",
    "mechanistic interpretab", "interpretability", "superposition", "inner alignment",
    "outer alignment", "off-switch", "shutdown", "safety", "risk", "existential",
    "robustness", "robust", "representation", "schema", "coherence", "coherent",
    "compositional", "systematic generalization", "value", "normativ", "volition",
    "abstraction", "ontology", "misalignment", "misaligned", "alignment-faking",
]

# ── Precision gate: core AGI-safety indicators (necessary for Include) ─
# High-precision terms essentially unique to AGI-safety / alignment discourse.
CORE_INDICATORS = [
    # Level 2 — technical alignment (near-unique)
    "mesa-optim", "mesa optim", "learned optimization",
    "deceptive alignment", "alignment faking", "sleeper agent", "sleeper agents",
    "corrigib", "incorrigib", "off-switch", "off switch", "shutdown problem", "shutdownable",
    "inner alignment", "outer alignment", "goal misgeneraliz", "goal preservation",
    # Level 3 — diagnostic (near-unique in safety sense)
    "reward hacking", "specification gaming", "coherent extrapolated volition",
    "reward model over-optimization", "reward model overoptimisation",
    # Level 4 — value specification
    "indirect normativity",
    # Level 5 — bridging (schema-coherence vocabulary)
    "schema coherence", "representational coherence", "coherent schema",
    # General / frontier
    "agi safety", "artificial general intelligence", "agi risk", "superintelligence",
    "superintelligent", "existential risk from", "x-risk", "existential safety",
    "transformative ai", "frontier model", "frontier ai", "general intelligence",
    "alignment problem", "alignment research", "misalignment", "misaligned",
    "ai alignment", "aligning ai", "value alignment", "value-aligned",
    "mechanistic interpretab", "interpretability", "rlhf", "reward model",
    "reward models", "constitutional ai", "scalable oversight", "weak-to-strong",
    "specification game", "reward hacking",
]

# AI context terms: co-occurrence required for ambiguous core indicators.
# High-precision AI terms (multi-word or unambiguous); word-boundary matched.
AI_CONTEXT_TERMS = [
    "ai", "ml", "gpt", "artificial intelligence", "machine learning", "deep learning", "neural network",
    "neural networks", "reinforcement learning", "rlhf", "large language model",
    "large language models", "language model", "language models", "foundation model",
    "foundation models", "frontier model", "frontier models", "llm", "llms",
    "chatgpt", "gpt-4", "gpt-3", "transformer", "transformers",
    "ai system", "ai systems", "ai agent", "ai agents", "agent", "agents",
    "autonomous", "robot", "robots", "robotic", "autonomous system",
    "reward model", "reward models", "world model", "world models",
    "deep learning model", "ml model",
]

# Terms whose word-boundary is required (avoid substring false positives like "ai" in "sustainability")
AI_SHORT_TERMS = ["ai", "ml", "gpt", "llm", "llms", "ode"]

# Narrow domain markers (management / psychology / medicine / business):
# if present AND the only core evidence is ambiguous value-language, exclude as narrow.
NARROW_DOMAIN_TERMS = [
    "employee", "employees", "leadership", "wellness", "nursing", "csr",
    "happiness", "engagement", "stakeholder", "stakeholders", "hospitality",
    "physician", "physicians", "student", "students", "university", "hrm",
    "burnout", "organizational", "organisational", "workplace", "human resource",
    "human resources", "sustainability", "supply chain", "marketing", "consumer",
    "consumers", "retention", "recruitment", "tourism", "hotel", "work engagement",
    "job satisfaction", "acculturation", "management", "business", "firm",
    "firms", "entrepreneur", "career", "workforce", "talent",
    "juvenile", "criminal", "court", "constitutional", "law", "legal",
    "land administration", "land registry", "healthcare", "medicine", "clinical",
    "chemical", "process safety", "industrial", "factory", "manufacturing",
    "power grid", "electricity", "traffic", "recommendation system",
    "recommender", "advertising", "recruitment platform",
]

# ── E1: Narrow AI safety patterns (exclusion) ─────────────────────────
NARROW_SAFETY_PATTERNS = [
    "bias", "fairness", "privacy", "medical imaging", "autonomous vehicle",
    "self-driving", "credit scoring", "recidivism", "algorithmic fairness",
    "hate speech detection", "content moderation", "facial recognition",
    "cybersecurity", "ransomware", "phishing", "data protection",
    "gdpr", "surveillance", "ai ethics committee", "robot ethics",
]

# ── E5: Capability-only patterns (exclusion without safety framing) ───
CAPABILITY_ONLY_PATTERNS = [
    "scaling law", "scaling laws", "benchmark", "state-of-the-art", "sota",
    "outperforms", "surpasses", "image classification", "object detection",
    "speech recognition", "machine translation", "language modeling perplexity",
    "training efficiency", "inference speed", "model compression", "knowledge distillation",
    "few-shot accuracy", "zero-shot accuracy", "sota results",
]

# ── E3: Opinion-piece patterns (flag for possible exclusion) ──────────
OPINION_PATTERNS = [
    "reflections on", "thoughts on", "a call for", "manifesto", "open letter",
    "why we should", "why we must", "the case for", "my view on",
]

# ── I4: Publication type markers ──────────────────────────────────────
PUBLICATION_TYPE_HINTS = {
    "peer-reviewed": ["journal", "proceedings", "transactions", "review", "ieee",
                      "acm", "springer", "elsevier", "nature", "science"],
    "preprint": ["arxiv", "preprint", "ssrn"],
    "technical-report": ["technical report", "working paper", "white paper"],
    "forum-post": ["lesswrong", "alignment forum", "ea forum", "forum"],
}

# ── Scoring thresholds ────────────────────────────────────────────────
SUBJECT_HITS_REQUIRED = 1     # I3: ≥1 subdomain hit
STRUCTURAL_TERMS_REQUIRED = 1  # I5: ≥1 structural safety term

# Decision labels
INCLUDE = "Include"
EXCLUDE = "Exclude"
UNCERTAIN = "Uncertain"

# Reason codes (aligned to protocol criteria)
REASON_CODES = {
    "R-DATE": "Outside date range (I2: 2015-2026)",
    "R-LANG": "Not in English (E2)",
    "R-SUBJ": "No AGI safety subdomain engagement (I3)",
    "R-STRUCT": "Not structural AGI safety / narrow-only (I5/E1)",
    "R-OPIN": "Pure opinion without substantive content (E3)",
    "R-CAP": "Capability-only without safety framing (E5)",
    "R-DUP": "Duplicate/overlapping publication (E4)",
    "R-PRED": "Predatory or questionable venue (E6)",
    "R-YEAR": "Publication year missing (I2 unverifiable)",
}
