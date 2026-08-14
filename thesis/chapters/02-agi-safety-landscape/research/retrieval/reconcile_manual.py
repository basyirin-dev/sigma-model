#!/usr/bin/env python3
"""
Paper 01 — Phase 6 reconciliation of user manual downloads.

1. Parse the user's pasted download list (99 titles, some duplicated)
2. Match each title to included studies (normalized match)
3. Detect duplicate PDFs in research/pdfs/ (same study, multiple files)
4. Update retrieval-status.csv:
   - user-downloaded records -> retrieved-manual
   - confirmed-paywalled records -> paywalled-confirmed
"""

from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
PDF_DIR = BASE / "research" / "pdfs"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
OUT_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"

# User's pasted download list (verbatim, 99 entries; duplicates kept to count them)
PASTED_TITLES = """Artificial Superintelligence: Computational Pathways, Architectures, and Safety Constraints
Beyond Step Pruning: Information Theory Based Step-level Optimization for Self-Refining Large Language Models
The Many Faces of AI Alignment
Will power-seeking AGIs harm human society?
Could We Control Superintelligent AI?
Procedural Compliance, Substantive Transgression: Uncovering How Alignment Failures in the Doubao System Drive Boundary Violations in Professional Contexts
LA-EDPO: Length-Aware Effect-Enhanced Direct Preference Optimization
MIRA: An LLM-Driven Dual-Loop Architecture for Metacognitive Reward Design
XAI2Brain: A Perspective on Mechanistic Interpretability for Brain–AI Alignment
Toward Constitutional Autonomy in AI Systems: A Theoretical Framework for Aligned Agentic Intelligence
A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents
Reinforcement Learning from X-Feedback: Recent Advances and Future Prospects
Machines that halt resolve the undecidability of artificial intelligence alignment
For example, recent instances of ‘reward hacking’ reveal how AI systems can exploit scoring loopholes in tasks assigned by users to maximize rewards—knowingly deviating from user intent—highlighting the dangers of emergent misalignment even in systems capable of understanding their own deception: ‘Recent frontier models are reward hacking
The economics of p(doom): Scenarios of existential risk and economic growth in the age of transformative AI
Step-GRPO: Enhancing Reasoning Quality and Efficiency via StructurePRM-Based Reinforcement Learning
Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction
Intrinsic Barriers and Practical Pathways for Human-AI Alignment: An Agreement-Based Complexity Analysis
Incomplete Contracting and Al Alignment
Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment
Step-GRPO: Enhancing Reasoning Quality and Efficiency via Structured PRM-Based Reinforcement Learning
Beyond Step Pruning: Information Theory Based Step-level Optimization for Self-Refining Large Language Models
Aligning Large Multimodal Models with Factually Augmented RLHF
SEAL: Systematic Error Analysis for Value ALignment
Taming Simulators: Challenges, Pathways and Vision for the Alignment of Large Language Models
Transparent by Design: Ensuring Safety in Agentic AI Through Decision Traceability
Flow-Multi: A Flow-Matching Multi-Reward Framework for Text-to-Image Generation
Hierarchical process-level generative reward modeling with adaptive long-horizon reasoning for robust LLM alignment
Neurodivergent influenceability in agentic AI as a contingent solution to the AI alignment problem
Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction
Testing Obedience and Control in AGI: Exploring Irrational Commands and the AI Control Problem
From Clicks to Preference: A Multi-stage Alignment Framework for Generative Query Suggestion in Conversational System
Mechanistic Interpretability: A New Trend in Interpretability Research
Building Robust Artificial Intelligence Through Multi-Agent Debate
Artificial General Intelligence: Current Progress, Safety Considerations, and Ethical Imperatives
Artificial superintelligence alignment in healthcare
Navigating the Ethics of Artificial Intelligence
Is superintelligence necessarily moral?
Harnessing Metacognition for Safe and Responsible AI
Helpful, harmless, honest? Sociotechnical limits of AI alignment and safety through Reinforcement Learning from Human Feedback
From Human Mind to Artificial Intelligence: Advancing AI Value Alignment Through Psychological Theories
Reward Model Interpretability via Optimal and Pessimal Tokens
Towards Value Alignment for Opaque Agents Through Concept Analysis and Inter-Agent Value Modelling
METAETHICAL FOUNDATIONS OF ARTIFICIAL INTELLIGENCE ALIGNMENT METHODOLOGICAL APPROACHES AND THEIR LIMITATIONS
Reward Hacking in Reinforcement Learning and RLHF: A Multidisciplinary Examination of Vulnerabilities, Mitigation Strategies, and Alignment Challenges
Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment
SEAL: Systematic Error Analysis for Value ALignment
Counter-productivity and suspicion: two arguments against talking about the AGI control problem
CARMO: Dynamic Criteria Generation for Context Aware Reward Modelling
AI welfare risks
Normative conflicts and shallow AI alignment
Value-aligned but misguided: a dilemma in AI and AGI decision making
Refusal Behavior in Large Language Models: A Nonlinear Perspective
From Principle to Practice: Value Alignment in AI Ethics and Governance
EXISTENTIAL RISK FROM TRANSFORMATIVE AI: AN ECONOMIC PERSPECTIVE
IWPO: Sample Importance Weight-Based Human Preference Optimization for Large Language Models
Misalignment or misuse? The AGI alignment tradeoff
Existentialist risk and value misalignment
Adversarial Preference Learning for Robust LLM Alignment
Aesthetic Value and the AI Alignment Problem
Designing AI Systems with Value Alignment Mechanisms
AI alignment is all your need for future drug discovery
A timing problem for instrumental convergence
Focus-N-Fix: Region-Aware Fine-Tuning for Text-to-Image Generation
Personalized Constitutionally-Aligned Agentic Superego: Secure AI Behavior Aligned to Diverse Human Values
The Neglect of Qualia and Consciousness in AI Alignment Research
HicAgent: Hierarchical Iterative Cooperative Learning Reward Generation Guided by a Large Model
A Phase-Based Ethical Alignment Framework for Mitigating In-Context Scheming Behaviour in Superintelligent Systems
AI Alignment Versus AI Ethical Treatment: 10 Challenges
Artificial Intelligence: Approaches to Safety
Removing Prompt-template Bias in Reinforcement Learning from Human Feedback
Augmented utilitarianism for AGI safety
Value Cores for Inner and Outer Alignment: Simulating Personality Formation via Iterated Policy Selection and Preference Learning with Self-World Modeling Active Inference Agents
Aligning Large Multimodal Models with Factually Augmented RLHF
Global solutions vs. Local solutions for the ai safety problem
A short introduction to the ethics of artificial intelligence
Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts
Alleviating Action Hallucination for LLM-based Embodied Agents via Inner and Outer Alignment
Taking into Account Sentient Non-Humans in AI Ambitious Value Learning: Sentientist Coherent Extrapolated Volition
Hybrid strategies towards safe "self-aware" superintelligent systems
Current cases of AI misalignment and their implications for future risks
Enhancing Reinforcement Learning Finetuned Text-to-Image Generative Model Using Reward Ensemble
Towards agi agent safety by iteratively improving the utility function
Friendly Superintelligent AI: All You Need Is Love
A functional contextual, observer-centric, quantum mechanical, and neuro-symbolic approach to solving the alignment problem of artificial general intelligence: safe AI through intersecting computational psychological neuroscience and LLM architecture for emergent theory of mind
Orthogonality-based disentanglement of responsibilities for ethical intelligent systems
Multiparty dynamics and failure modes for machine learning and artificial intelligence
Challenges of aligning artificial intelligence with human values
Taming Simulators: Challenges, Pathways and Vision for the Alignment of Large Language Models
Design principles for integrated AI alignment
The End of History? Envisioning the Economy at Technological Singularity
School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs
Reward Hacking as Equilibrium under Finite Evaluation
Understanding Reward Hacking in Text-to-Image Reinforcement Learning
Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds
Natural Emergent Misalignment from Reward Hacking in Production RL
Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking
Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking
Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction""".splitlines()

# Confirmed paywalled by user
CONFIRMED_PAYWALLED = {
    "The Many Faces of AI Alignment",
    "Could We Control Superintelligent AI?",
}
CONFIRMED_IDS = {"P01_2387", "P01_0460", "P01_0539", "P01_0597", "P01_0992",
                 "P01_1216", "P01_1305"}


def norm(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    # Load included studies
    with open(INCLUDED_CSV, "r", encoding="utf-8") as f:
        included = list(csv.DictReader(f))
    title_idx = {}
    for r in included:
        key = norm(r.get("title", ""))
        title_idx[key] = r

    # Load status
    with open(STATUS_CSV, "r", encoding="utf-8") as f:
        status_rows = list(csv.DictReader(f))
    status_by_id = {r["id"]: r for r in status_rows}

    # 1. Match pasted titles
    print("=== Pasted download list reconciliation ===\n")
    matched = 0
    unmatched = []
    seen = set()
    dup_pastes = 0
    for raw in PASTED_TITLES:
        t = raw.strip()
        if not t:
            continue
        key = norm(t)
        if key in seen:
            dup_pastes += 1
        seen.add(key)
        rec = title_idx.get(key)
        if not rec:
            unmatched.append(t)
            continue
        matched += 1
        st = status_by_id.get(rec["id"], {})
        print(f"  {rec.get('study_id','?'):6s} rel={rec.get('ft_reason','')} "
              f"status={st.get('status','?'):20s} {rec['title'][:55]}")

    print(f"\nMatched: {matched}/{len(set(norm(t) for t in PASTED_TITLES if t.strip()))}")
    print(f"Duplicate entries in paste: {dup_pastes}")
    if unmatched:
        print(f"Unmatched ({len(unmatched)}):")
        for t in unmatched:
            print(f"  - {t[:80]}")

    # 2. Detect duplicate PDFs in research/pdfs/
    print("\n=== PDF duplicate detection ===\n")
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    print(f"Total PDFs: {len(pdfs)}")
    # group by normalized filename stem (surname_year)
    groups = {}
    for p in pdfs:
        stem = norm(p.stem)  # e.g. "aliman_2019" for "Aliman_2019_arxiv.pdf"
        m = re.match(r"([a-z]+)_(\d{4})", stem)
        if m:
            key = f"{m.group(1)}_{m.group(2)}"
            groups.setdefault(key, []).append(p.name)
    dup_groups = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"Filename-collision groups (same surname_year, >1 file): {len(dup_groups)}")
    for k, v in sorted(dup_groups.items())[:30]:
        print(f"  {k}: {v}")

    # 3. Update statuses: user-downloaded -> retrieved-manual; confirmed -> paywalled-confirmed
    print("\n=== Status updates ===\n")
    # find user-downloaded: PDFs not created by the automated run (no _arxiv/_oa suffix
    # and newer than the automated batch) OR matching pasted titles already retrieved
    manual_pdf_names = [p.name for p in pdfs if "_arxiv" not in p.name and "_oa" not in p.name]
    print(f"User-style PDFs (no _arxiv/_oa suffix): {len(manual_pdf_names)}")

    n_manual = 0
    for r in included:
        rec = title_idx.get(norm(r.get("title", "")))
        if rec is None:
            continue
        # match a user-style pdf by firstauthor_year
        st = status_by_id.get(rec["id"])
        if not st or st.get("status", "").startswith("retrieved"):
            continue
        # crude: any pdf whose stem surname_year matches
        for pname in manual_pdf_names:
            if norm(pname).split("_")[0] in norm(rec.get("authors", "")).lower() and \
               norm(pname).split("_")[1] == str(rec.get("year", "")):
                st["status"] = "retrieved-manual"
                st["pdf_path"] = f"research/pdfs/{pname}"
                n_manual += 1
                break

    for pid in CONFIRMED_IDS:
        st = status_by_id.get(pid)
        if st:
            st["status"] = "paywalled-confirmed"
    for t in CONFIRMED_PAYWALLED:
        rec = title_idx.get(norm(t))
        if rec:
            st = status_by_id.get(rec["id"])
            if st:
                st["status"] = "paywalled-confirmed"

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(status_rows[0].keys()))
        w.writeheader()
        w.writerows(status_rows)

    from collections import Counter
    print(f"\nUpdated {n_manual} records to retrieved-manual; "
          f"{len(CONFIRMED_IDS) + len(CONFIRMED_PAYWALLED)} to paywalled-confirmed")
    print("New status distribution:", dict(Counter(r["status"] for r in status_rows)))


if __name__ == "__main__":
    main()
