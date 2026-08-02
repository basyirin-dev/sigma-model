#!/usr/bin/env python3
"""
Paper 01 — Phase 6: apply the user's authoritative Batch-A download list.

The 46 titles the user downloaded are ground truth. For each title ->
study, locate the actual file (first-author surname + year among
user-style files, preferring non-_oa/_arxiv), and set has_pdf=yes.
P575/P596 (inaccessible) stay as-is.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
PDF_DIR = BASE / "research" / "pdfs"
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
QUEUE_CSV = BASE / "research" / "retrieval" / "download-queue.csv"

BATCH_A_TITLES = [
    "Reinforcement Learning With Verifier Guidance and Penalty Shaping for Vietnamese Summarization Using Small Language Models",
    "Bridging Human and Artificial Intelligence: Modeling Human Learning with Explainable AI Tools",
    "Collective Constitutional AI: Aligning a Language Model with Public Input",
    "Is Blockchain the Future of AI Alignment? Developing a Framework and a Research Agenda Based on a Systematic Literature Review",
    "Psychopathia Machinalis: A Nosological Framework for Understanding Pathologies in Advanced Artificial Intelligence",
    "Choice Vectors: Streamlining Personal AI Alignment Through Binary Selection",
    "Franz Kafka, Artificial Intelligence and the Paradoxical Recognition of Selfhood",
    "Safe Reinforcement Learning for Arm Manipulation with Constrained Markov Decision Process",
    "Anthropology for AI",
    "Vision Paper: Advancing of AI Explainability for the Use of ChatGPT in Government Agencies - Proposal of A 4-Step Framework",
    "Safe artificial general intelligence via distributed ledger technology",
    "AI ethics and value alignment for nonhuman animals",
    "Addressing the Value Alignment Problem Through Online Institutions",
    "Action Guidance and AI Alignment",
    "An Enactive Approach to Value Alignment in Artificial Intelligence: A Matter of Relevance",
    "From homo sapiens to robo sapiens: The evolution of intelligence",
    "Provably safe artificial general intelligence via interactive proofs",
    "Machines learning values",
    "ACT: A Conceptual Framework for Understanding and Controlling Trustworthiness in Controllable AI",
    "On Algorithmic Ethics: Examining AI Decision-Making Mechanisms From the Perspective of Kant's Moral Philosophy",
    "Governing Generative AI for Healthy Ageing: A Normative Conceptual Framework for Societal Alignment, Epistemic Authority, and Value Convergence in Geriatric Care",
    "The Bateson Game: A Model of Strategic Ambiguity, Frame Uncertainty, and Pathological Learning",
    "An Explainable HCI-Based Decision Support Framework for Human-AI Co-Design",
    "Adaptive Quine Structures for Metacognitive Evolution in Large Language Models: A Functional Framework with Gödelian Bounds and Illustrative Applications",
    "Evaluating Generative AI as a Triage Tool in Aligned Yet Divergent Investment Decision-Making",
    "User Experience Design Professionals' Perceptions of Generative Artificial Intelligence",
    "Large Language Model-Powered Automated Assessment: A Systematic Review",
    "When AI possesses personality: Roles of good and evil personalities influence moral judgment in large language models",
    "Bringing AI participation down to scale",
    "Comparing and Evaluating Human and Computationally Derived Representations of Non-Semantic Design Information",
    "Towards an End-to-End Personal Fine-Tuning Framework for AI Value Alignment",
    "Autonomous Weapons Systems and the ai Alignment Problem",
    "Computational Frameworks for Human Care",
    "Potential for near-term AI risks to evolve into existential threats in healthcare",
    "A First Look at AI Trends in Value-Aligned Software Engineering Publications: Human-LLM Insights",
    "Large Language Models in Human Subject Research, and the Presence of Idiosyncratic Human Behaviors",
    "Better Understanding of Humans for Cooperative AI through Clustering",
    "Transformers discover an elementary calculation system exploiting local attention and grid-like problem representation",
    "Domesticating Artificial Intelligence",
    "A survey of the potential long-Term impacts of ai: How ai could lead to long-Term changes in science, cooperation, power, epistemics and values",
    "A Cautionary Tale About AI-Generated Goal Suggestions",
    "Survey on multi-agent reinforcement learning methods from the perspective of population",
    "Nicolas de Condorcet and the first intelligence explosion hypothesis",
    "Superintelligence as superethical",
    "Inhuman Vectors",
    "Towards functional social cognition in machines: comparing human and AI attribution of mental states from facial cues",
]

INACCESSIBLE = {"P575", "P596"}


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))
    idx = {}
    for r in annot:
        idx.setdefault(norm(r["title"]), r)

    pdf_names = sorted(p.name for p in PDF_DIR.glob("*.pdf"))
    user_pdfs = [p for p in pdf_names if "_arxiv" not in p and "_oa" not in p]

    fixed = 0
    unresolved = []
    for t in BATCH_A_TITLES:
        rec = idx.get(norm(t))
        if not rec:
            unresolved.append(("NO-STUDY", t))
            continue
        sid = rec["study_id"]
        if sid in INACCESSIBLE:
            continue  # leave as inaccessible
        if rec["has_pdf"] == "yes":
            continue  # already matched
        # find file: surname + year among user-style files
        authors = (rec.get("authors") or "")
        year = (rec.get("year") or "").strip()
        surname = authors.split(";")[0].split(",")[0].strip().split()[-1].lower()
        cands = [p for p in user_pdfs
                 if Path(p).stem.lower().replace("_", " ").startswith(surname) and year in p]
        if len(cands) >= 1:
            rec["has_pdf"] = "yes"
            rec["needs_download"] = "no"
            rec["pdf_status"] = "retrieved-manual"
            rec["pdf_path"] = "thesis/papers/01-scoping-review/research/pdfs/" + cands[0]
            fixed += 1
        else:
            unresolved.append((sid, t[:60]))

    with open(ANNOT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(annot[0].keys()))
        w.writeheader()
        w.writerows(annot)

    print(f"Batch A ground-truth applied: {fixed} studies marked has_pdf=yes")
    if unresolved:
        print("Unresolved:")
        for sid, t in unresolved:
            print(f"  {sid}: {t}")


if __name__ == "__main__":
    main()
