#!/usr/bin/env python3
"""
Paper 01 — Phase 6: rebuild annotations download flags from
AUTHORITATIVE sources only:

  1. retrieval-status.csv pdf_path where the file exists on disk
     (download-time assignments: retrieved-arxiv/oa/manual)
  2. Batch A ground truth (44 user-downloaded titles)
  3. Title-verified matches (resolve_unconventional output)

Everything else -> has_pdf=no / needs_download=yes.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
PDF_DIR = BASE / "research" / "pdfs"
PDF_PREFIX = "thesis/papers/01-scoping-review/research/pdfs/"

# Title-verified matches from resolve_unconventional.py
TITLE_VERIFIED = {
    "P886": "Aliman_2019_arxiv.pdf", "P611": "Bereska_2023.pdf",
    "P977": "Cannon_2022.pdf", "P960": "Carroll_2024_arxiv.pdf",
    "P1072": "Yao_2026_arxiv.pdf", "P907": "Gabriel_2021_arxiv.pdf",
    "P1149": "Hadfield_Menell_2018_arxiv.pdf", "P1208": "Li_2026_Step-GRPO.pdf",
    "P898": "Mechergui_2024_oa.pdf", "P919": "Micha_2025_oa.pdf",
    "P891": "Pan_2024_arxiv.pdf", "P953": "Skalse_2022_arxiv.pdf",
    "P852": "Wang_2024_arxiv.pdf", "P1220": "Zhao_2026.pdf",
    "P1250": "Zhao_2026_oa.pdf",
}

# Batch A ground truth (44 downloaded; P575/P596 inaccessible)
BATCH_A = ["Reinforcement Learning With Verifier Guidance and Penalty Shaping for Vietnamese Summarization Using Small Language Models",
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
    "Superintelligence as superethical", "Inhuman Vectors",
    "Towards functional social cognition in machines: comparing human and AI attribution of mental states from facial cues"]


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    with open(INCLUDED_CSV, "r", encoding="utf-8") as f:
        included = list(csv.DictReader(f))
    # id -> study_id, normalized title -> study
    id_to_sid = {r["id"]: r["study_id"] for r in included}
    title_to_sid = {}
    for r in included:
        title_to_sid.setdefault(norm(r["title"]), r["study_id"])

    # authoritative assignments: study_id -> pdf filename
    assignment: dict[str, str] = {}

    # 1. status pdf_path with existing file
    with open(STATUS_CSV, "r", encoding="utf-8") as f:
        for st in csv.DictReader(f):
            p = st.get("pdf_path") or ""
            if p and (BASE.parent.parent.parent / p).exists():
                sid = id_to_sid.get(st["id"])
                if sid:
                    assignment[sid] = Path(p).name

    # 2. title-verified matches
    for sid, fname in TITLE_VERIFIED.items():
        if (PDF_DIR / fname).exists():
            assignment[sid] = fname

    # 3. Batch A ground truth (find file by surname+year)
    user_files = [p.name for p in PDF_DIR.glob("*.pdf")
                  if "_arxiv" not in p.name and "_oa" not in p.name]
    for t in BATCH_A:
        sid = title_to_sid.get(norm(t))
        if not sid or sid in assignment:
            continue
        rec = next((r for r in included if r["study_id"] == sid), None)
        if not rec:
            continue
        authors = rec.get("authors") or ""
        year = (rec.get("year") or "").strip()
        surname = authors.split(";")[0].split(",")[0].strip().split()[-1].lower()
        cands = [f for f in user_files
                 if Path(f).stem.lower().replace("_", " ").startswith(surname) and year in f]
        if cands:
            assignment[sid] = cands[0]

    # rebuild annotations
    with open(ANNOT_CSV, "r", encoding="utf-8") as f:
        annot = list(csv.DictReader(f))
    for r in annot:
        sid = r["study_id"]
        if sid in assignment:
            r["has_pdf"] = "yes"
            r["needs_download"] = "no"
            r["pdf_status"] = "retrieved-file"
            r["pdf_path"] = PDF_PREFIX + assignment[sid]
        else:
            r["has_pdf"] = "no"
            r["needs_download"] = "yes"
            if (r.get("pdf_status") or "").startswith("retrieved"):
                r["pdf_status"] = "no-pdf"
            r["pdf_path"] = ""

    with open(ANNOT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(annot[0].keys()))
        w.writeheader()
        w.writerows(annot)

    # keep the 8 foreign/no-pdf statuses intact? they are not has_pdf anyway.
    print(f"Authoritative assignments: {len(assignment)}")
    print("Annotations:", dict(Counter(r["has_pdf"] for r in annot)))


if __name__ == "__main__":
    main()
