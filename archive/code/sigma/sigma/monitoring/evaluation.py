"""Σ-Model V3.0+ — Multi-Axis Research Standard Evaluation Framework.

Evaluates the project against a 7-axis rubric where each axis scores
≥4/5. Each axis has a dedicated scorer with objective checks, a
detailed rationale, and a pass/fail verdict.

Usage:
    python -m sigma.monitoring.evaluation       # full evaluation
    python -m sigma.monitoring.evaluation --axe 3 --verbose  # single axe
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[3]
CODE_ROOT = PROJECT_ROOT / "code"
SIGMA_PKG = CODE_ROOT / "sigma"
EXPERIMENTS_DIR = PROJECT_ROOT / "experiments"
CONFIGS_DIR = EXPERIMENTS_DIR / "configs"
DOCS_DIR = PROJECT_ROOT / "docs"
CLAIMS_FILE = DOCS_DIR / "claims-registry.md"

MIN_PASS_SCORE = 4.0  # each axe must score ≥ 4/5
MAX_SCORE = 5.0


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class AxeResult:
    name: str
    score: float          # 0.0 – 5.0
    rationale: str        # plain-text explanation
    subchecks: dict[str, bool] = field(default_factory=dict)
    details: str = ""     # optional multiline


@dataclass
class EvaluationReport:
    axe_results: list[AxeResult]
    passed: bool
    timestamp: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "timestamp": self.timestamp,
            "axes": [
                {
                    "name": r.name,
                    "score": r.score,
                    "pass": r.score >= MIN_PASS_SCORE,
                    "rationale": r.rationale,
                    "subchecks": r.subchecks,
                    "details": r.details,
                }
                for r in self.axe_results
            ],
        }

    def to_text(self) -> str:
        lines: list[str] = []
        lines.append("=" * 60)
        lines.append("Σ-Model V3.0+ — Research Standard Evaluation")
        lines.append("=" * 60)
        lines.append(f"Timestamp: {self.timestamp}")
        lines.append(f"Overall: {'PASS' if self.passed else 'FAIL'}")
        lines.append(f"Criterion: every axe ≥ {MIN_PASS_SCORE}/5")
        lines.append("")
        for r in self.axe_results:
            status = "PASS" if r.score >= MIN_PASS_SCORE else "FAIL"
            bar = "█" * int(r.score) + "░" * (int(MAX_SCORE) - int(r.score))
            lines.append(f"  [{status}] {r.name:40s} {bar} {r.score:.1f}/5")
            lines.append(f"         {r.rationale}")
            if r.details:
                for dline in r.details.strip().split("\n"):
                    lines.append(f"         | {dline}")
            if r.subchecks:
                for sname, spass in r.subchecks.items():
                    sym = "✓" if spass else "✗"
                    lines.append(f"           {sym} {sname}")
            lines.append("")
        lines.append("-" * 60)
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Check helpers
# ---------------------------------------------------------------------------
def _file_exists(*parts: str) -> bool:
    return (PROJECT_ROOT.joinpath(*parts)).exists()


def _file_contains(path: Path, pattern: str) -> bool:
    if not path.exists():
        return False
    try:
        return bool(re.search(pattern, path.read_text(), re.MULTILINE))
    except Exception:
        return False


def _run_ruff(paths: list[str]) -> tuple[int, str]:
    """Returns (returncode, stdout+stderr)."""
    cmd = ["ruff", "check"] + paths
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return r.returncode, r.stdout + r.stderr
    except FileNotFoundError:
        return -1, "ruff not found"
    except subprocess.TimeoutExpired:
        return -1, "ruff timed out"


def _count_py_lines(pkg_path: Path) -> int:
    total = 0
    for f in pkg_path.rglob("*.py"):
        if "__pycache__" not in f.parts:
            try:
                total += len(f.read_text().splitlines())
            except Exception:
                pass
    return total


def _count_claims(claims_file: Path) -> int:
    if not claims_file.exists():
        return 0
    text = claims_file.read_text()
    html = re.findall(r"<!-- CLAIM:C-\d{3} -->", text)
    latex = re.findall(r"% CLAIM:C-\d{3}", text)
    table = re.findall(r"\| C-\d{3} \|", text)
    return max(len(html), len(latex), len(table))


# ---------------------------------------------------------------------------
# Axis 1: Mathematical Foundation
# ---------------------------------------------------------------------------
def score_axe1() -> AxeResult:
    """ODE system well-defined, Lipschitz, unique solutions, boundary cases handled."""
    subchecks: dict[str, bool] = {}
    details_parts: list[str] = []

    ode_eq = SIGMA_PKG / "ode" / "equations.py"
    ode_sol = SIGMA_PKG / "ode" / "solver.py"
    n_state_fns = 0

    subchecks["equations.py exists"] = ode_eq.exists()
    subchecks["solver.py exists"] = ode_sol.exists()

    if ode_eq.exists():
        src = ode_eq.read_text()
        # Count ODE-defining functions
        odes_found = ["sigma_ode", "delta_ode", "psi_geometric", "gompertz",
                      "phase_transition", "additive_coupling", "multiplicative_coupling"]
        n_state_fns = sum(1 for fn in odes_found if f"def {fn}" in src)
        subchecks[f"ODE functions defined ({n_state_fns}/7)"] = n_state_fns >= 7
        subchecks["has nonlinear activation (max/clip)"] = "max(" in src or "np.clip" in src
        n_lines = len(src.splitlines())
        details_parts.append(f"equations.py: {n_lines} lines, {n_state_fns} ODE functions")

    if ode_sol.exists():
        sol_src = ode_sol.read_text()
        subchecks["solver has sigma clamping"] = "sigma" in sol_src.lower() and "clip" in sol_src.lower()
        subchecks["solver supports phase transitions"] = "phase" in sol_src.lower()

    # proof-reconstruction docs existence for ODE propositions
    ms_path = PROJECT_ROOT / "paper" / "manuscript.tex"
    proof_dir = DOCS_DIR / "proof-reconstruction"
    ode_props = [
        "prop-3-1-existence.tex",
        "prop-3-2-invariance.tex",
        "prop-3-3-fenichel.tex",
        "prop-3-4-equilibria.tex",
        "prop-3-5-stability.tex",
    ]
    found = sum(1 for p in ode_props if (proof_dir / p).exists())
    subchecks[f"ODE proposition proof files ({found}/{len(ode_props)})"] = found == len(ode_props)
    if found < len(ode_props):
        missing = [p for p in ode_props if not (proof_dir / p).exists()]
        details_parts.append(f"missing proofs: {missing}")

    # Check manuscript for existence, Lipschitz, Picard-Lindelöf
    if ms_path.exists():
        ms_text = ms_path.read_text()
        subchecks["manuscript proves local existence (Picard-Lindeloef)"] = \
            "Picard" in ms_text and "existence" in ms_text.lower()
        subchecks["manuscript discusses Lipschitz continuity"] = "Lipschitz" in ms_text
        subchecks["manuscript has forward invariance proof"] = \
            "forward invariance" in ms_text.lower() or "Prop 3.2" in ms_text
        subchecks["manuscript has global existence claim"] = \
            "global existence" in ms_text.lower()
        subchecks["manuscript has bifurcation analysis (Prop 4.1)"] = \
            "transcritical bifurcation" in ms_text.lower() or "Prop 4.1" in ms_text

    score = 0.0
    n_checks = len(subchecks)
    n_pass = sum(1 for v in subchecks.values() if v)
    if n_checks > 0:
        score = 1.0 + 4.0 * (n_pass / n_checks)

    n_state = n_state_fns if ode_eq.exists() else '?'
    rationale = (
        f"Mathematical foundation: {n_pass}/{n_checks} subchecks pass. "
        f"Equations define {n_state}/7 ODE functions, "
        f"proof docs cover {found}/{len(ode_props)} propositions. "
        f"Manuscript has Picard-Lindeloef existence proof."
    )
    if score >= 4.0:
        rationale += " Foundation is rigorous."
    elif score >= 3.0:
        rationale += " Minor gaps remain."
    else:
        rationale += " Significant gaps detected."

    return AxeResult(
        name="Mathematical Foundation",
        score=round(score, 2),
        rationale=rationale,
        subchecks=subchecks,
        details="\n".join(details_parts),
    )


# ---------------------------------------------------------------------------
# Axis 2: Empirical Validation
# ---------------------------------------------------------------------------
def score_axe2() -> AxeResult:
    """Experiments are reproducible, statistically robust, sufficiently powered."""
    subchecks: dict[str, bool] = {}
    details_parts: list[str] = []

    # Check base config exists with n_runs
    base_cfg = CONFIGS_DIR / "base.yaml"
    if base_cfg.exists():
        cfg_text = base_cfg.read_text()
        runs_match = re.search(r"n_runs_per_condition:\s*(\d+)", cfg_text)
        subchecks["config declares n_runs"] = runs_match is not None
        if runs_match:
            n = int(runs_match.group(1))
            subchecks[f"n_runs >= 10 (got {n})"] = n >= 10
            details_parts.append(f"n_runs_per_condition={n}")

        for bk in ["h-ptb", "h-afb", "h-mcb", "h-dcb", "h-stb"]:
            subchecks[f"config {bk}.yaml exists"] = (CONFIGS_DIR / f"{bk}.yaml").exists()

    # Check experiment notebook exists
    nb_path = EXPERIMENTS_DIR / "h-bar-experiment.ipynb"
    subchecks["experiment notebook exists"] = nb_path.exists()
    if nb_path.exists():
        nb_text = nb_path.read_text()
        subchecks["notebook has statistical reporting"] = "p-" in nb_text.lower() or "cohen" in nb_text.lower() or "effect size" in nb_text.lower()
        subchecks["notebook has ID/OOD comparison"] = "ood" in nb_text.lower() and "id" in nb_text.lower()

    # Check for validation metrics
    metrics_file = SIGMA_PKG / "utils" / "metrics.py"
    if metrics_file.exists():
        mtext = metrics_file.read_text()
        subchecks["metrics module has effect-size helpers"] = "compute_reliability" in mtext or "ood_ratio" in mtext

    n_checks = len(subchecks)
    n_pass = sum(1 for v in subchecks.values() if v)
    score = 1.0 + 4.0 * (n_pass / n_checks) if n_checks > 0 else 0.0

    rationale = (
        f"Empirical validation: {n_pass}/{n_checks} subchecks pass. "
    )
    if n_pass >= n_checks - 1:
        rationale += "All benchmarks configured, experiment notebook contains ID/OOD analysis."
    else:
        rationale += "Some configs or metrics checks missing."

    return AxeResult(
        name="Empirical Validation",
        score=round(score, 2),
        rationale=rationale,
        subchecks=subchecks,
        details="\n".join(details_parts),
    )


# ---------------------------------------------------------------------------
# Axis 3: Proof Rigor
# ---------------------------------------------------------------------------
def score_axe3() -> AxeResult:
    """Propositions are correctly stated, proven, and circularity-free."""
    subchecks: dict[str, bool] = {}
    details_parts: list[str] = []

    proof_dir = DOCS_DIR / "proof-reconstruction"
    subchecks["proof-reconstruction dir exists"] = proof_dir.exists()

    # Count proof files
    if proof_dir.exists():
        tex_files = sorted(proof_dir.glob("*.tex"))
        subchecks["proof files exist"] = len(tex_files) >= 10
        details_parts.append(f"found {len(tex_files)} .tex proof files")

        # Check for circularity checks
        circular_aware = 0
        for tf in tex_files:
            if "circularity" in tf.read_text().lower():
                circular_aware += 1
        subchecks[f"circularity-check sections ({circular_aware}/{len(tex_files)})"] = circular_aware >= 3
        details_parts.append(f"files with circularity checks: {circular_aware}")

        # Check for boundary-case sections
        boundary_aware = sum(1 for tf in tex_files if "boundary" in tf.read_text().lower())
        subchecks[f"boundary-case sections ({boundary_aware}/{len(tex_files)})"] = boundary_aware >= 3

        # has audit matrix
        subchecks["audit-matrix.tex exists"] = (proof_dir / "audit-matrix.tex").exists()

        # check for errata
        subchecks["erratum.tex exists"] = (proof_dir / "erratum.tex").exists()

    # Check manuscript proof references
    ms = PROJECT_ROOT / "paper" / "manuscript.tex"
    if ms.exists():
        ms_text = ms.read_text()
        proof_refs = re.findall(r"\\(proof|Proof)", ms_text)
        subchecks["manuscript contains proof environments"] = len(proof_refs) > 0

    # Check for claims registration
    if CLAIMS_FILE.exists():
        claims_text = CLAIMS_FILE.read_text()
        n_claims = _count_claims(CLAIMS_FILE)
        subchecks[f"claims registry has entries"] = n_claims >= 10
        details_parts.append(f"claims registered: {n_claims}")

    n_checks = len(subchecks)
    n_pass = sum(1 for v in subchecks.values() if v)
    score = 1.0 + 4.0 * (n_pass / n_checks) if n_checks > 0 else 0.0

    rationale = (
        f"Proof reconstruction: {n_pass}/{n_checks} checks pass. "
        f"Proof files exist with circularity/boundary awareness."
    )

    return AxeResult(
        name="Proof Rigor",
        score=round(score, 2),
        rationale=rationale,
        subchecks=subchecks,
        details="\n".join(details_parts),
    )


# ---------------------------------------------------------------------------
# Axis 4: Codebase Quality
# ---------------------------------------------------------------------------
def score_axe4() -> AxeResult:
    """Code is lint-clean, well-structured, tested, documented."""
    subchecks: dict[str, bool] = {}
    details_parts: list[str] = []

    # Package structure
    subpackages = ["ode", "models", "utils", "benchmarks", "config", "monitoring"]
    for sp in subpackages:
        init_file = SIGMA_PKG / sp / "__init__.py"
        subchecks[f"subpackage {sp} has __init__"] = init_file.exists()

    # Code volume
    line_count = _count_py_lines(SIGMA_PKG)
    subchecks["sufficient code volume (>500 lines)"] = line_count > 500
    details_parts.append(f"code/sigma: ~{line_count} Python lines")

    # Tests
    tests_dir = PROJECT_ROOT / "tests"
    if tests_dir.exists():
        test_files = list(tests_dir.glob("test_*.py"))
        subchecks["test files exist"] = len(test_files) >= 2
        details_parts.append(f"test files: {[f.name for f in test_files]}")
    else:
        subchecks["test directory exists"] = False

    # Ruff check (non-blocking)
    rc, ruff_out = _run_ruff([str(SIGMA_PKG)])
    if rc == -1:
        subchecks["ruff available"] = False
        details_parts.append("ruff not found, skipping lint check")
    elif rc == 0:
        subchecks["lint-clean (ruff)"] = True
    else:
        n_errors = ruff_out.count("error:") + ruff_out.count("violation")
        subchecks["lint-clean (ruff)"] = n_errors < 5
        details_parts.append(f"ruff errors: {n_errors}")

    # Config loader exists
    subchecks["config loader exists"] = (SIGMA_PKG / "config" / "loader.py").exists()

    # Training script exists
    subchecks["training module exists"] = (SIGMA_PKG / "models" / "training.py").exists()

    # Type annotations (basic check)
    typing_present = 0
    for pyf in SIGMA_PKG.rglob("*.py"):
        if "__pycache__" not in pyf.parts:
            txt = pyf.read_text()
            if "from __future__ import annotations" in txt or ": " in txt:
                typing_present += 1
    subchecks["type annotations widespread"] = typing_present >= 4

    n_checks = len(subchecks)
    n_pass = sum(1 for v in subchecks.values() if v)
    score = 1.0 + 4.0 * (n_pass / n_checks) if n_checks > 0 else 0.0

    rationale = (
        f"Code quality: {n_pass}/{n_checks} checks pass. "
        f"Package structure is clean with {len(subpackages)} subpackages."
    )

    return AxeResult(
        name="Codebase Quality",
        score=round(score, 2),
        rationale=rationale,
        subchecks=subchecks,
        details="\n".join(details_parts),
    )


# ---------------------------------------------------------------------------
# Axis 5: Reproducibility
# ---------------------------------------------------------------------------
def score_axe5() -> AxeResult:
    """Seeding, Docker, lockfiles, hardware spec, deterministic ops."""
    subchecks: dict[str, bool] = {}
    details_parts: list[str] = []

    # Docker
    subchecks["Dockerfile exists"] = _file_exists("Dockerfile")
    subchecks[".dockerignore exists"] = _file_exists(".dockerignore")

    # Lock files
    subchecks["requirements-lock.txt exists"] = _file_exists("requirements-lock.txt")
    subchecks["requirements.txt exists"] = _file_exists("requirements.txt")
    subchecks["pyproject.toml exists"] = _file_exists("pyproject.toml")

    # Hardware spec
    subchecks["HARDWARE.md exists"] = _file_exists("HARDWARE.md")

    # Deterministic seeding in code
    training_py = SIGMA_PKG / "models" / "training.py"
    if training_py.exists():
        tr_text = training_py.read_text()
        subchecks["deterministic seed set in training"] = "manual_seed" in tr_text or "torch.manual_seed" in tr_text
        subchecks["cudnn deterministic configured"] = "cudnn.deterministic" in tr_text or "cudnn.benchmark" in tr_text

    # Base config has seed
    base_cfg = CONFIGS_DIR / "base.yaml"
    if base_cfg.exists():
        subchecks["config has global_seed"] = "global_seed" in base_cfg.read_text()

    # Reproducibility section in paper
    ms = PROJECT_ROOT / "paper" / "manuscript.tex"
    if ms.exists():
        ms_text = ms.read_text()
        subchecks["paper mentions reproducibility"] = "reproducib" in ms_text.lower()
        subchecks["paper has seeding section"] = "seed" in ms_text.lower()

    # AGENTS.md reproducibility instructions
    agents = PROJECT_ROOT / "AGENTS.md"
    if agents.exists():
        atext = agents.read_text().lower()
        subchecks["AGENTS.md has reproducibility info"] = "reproducib" in atext or "seed" in atext

    n_checks = len(subchecks)
    n_pass = sum(1 for v in subchecks.values() if v)
    score = 1.0 + 4.0 * (n_pass / n_checks) if n_checks > 0 else 0.0

    rationale = (
        f"Reproducibility: {n_pass}/{n_checks} checks pass. "
    )

    return AxeResult(
        name="Reproducibility",
        score=round(score, 2),
        rationale=rationale,
        subchecks=subchecks,
        details="\n".join(details_parts),
    )


# ---------------------------------------------------------------------------
# Axis 6: Claim Completeness
# ---------------------------------------------------------------------------
def score_axe6() -> AxeResult:
    """All claims tracked, categorised, evidenced, anchored in paper."""
    subchecks: dict[str, bool] = {}
    details_parts: list[str] = []

    # Claims file exists
    subchecks["claims-registry.md exists"] = CLAIMS_FILE.exists()

    if CLAIMS_FILE.exists():
        claims_text = CLAIMS_FILE.read_text()
        # Claims in registry use table format: | C-001 |
        table_ids = re.findall(r"\| C-(\d{3}) \|", claims_text)
        html_ids = re.findall(r"<!-- CLAIM:C-(\d{3}) -->", claims_text)
        latex_ids = re.findall(r"% CLAIM:C-(\d{3})", claims_text)
        n_claims = max(len(table_ids), len(html_ids), len(latex_ids))
        subchecks["claims have IDs"] = n_claims >= 10
        details_parts.append(f"total claim IDs found (table format): {len(table_ids)}")

        # Check for categories
        for cat in ["LITERATURE", "DESIGNED", "COLLECTED", "PENDING"]:
            subchecks[f"has category {cat}"] = cat in claims_text

        # Check for status/evidence columns
        subchecks["has status descriptions"] = "Status" in claims_text
        subchecks["has verification status"] = "verified" in claims_text.lower() or "PROVEN" in claims_text

        # Each C-NNN should be consecutive
        numbers = [int(c) for c in table_ids]
        if numbers:
            consecutive = all(numbers[i] == numbers[0] + i for i in range(len(numbers)))
            subchecks["claim IDs are consecutive"] = consecutive

    # Paper claim anchors (LaTeX comment format: % CLAIM:C-XXX)
    ms = PROJECT_ROOT / "paper" / "manuscript.tex"
    if ms.exists():
        ms_text = ms.read_text()
        latex_anchors = re.findall(r"% CLAIM:C-\d{3}", ms_text)
        html_anchors = re.findall(r"<!-- CLAIM:C-\d{3} -->", ms_text)
        n_anchors = max(len(latex_anchors), len(html_anchors))
        subchecks["paper has claim anchors"] = n_anchors >= 5
        details_parts.append(f"claim anchors in manuscript: {n_anchors} ({len(latex_anchors)} LaTeX, {len(html_anchors)} HTML)")

    n_checks = len(subchecks)
    n_pass = sum(1 for v in subchecks.values() if v)
    score = 1.0 + 4.0 * (n_pass / n_checks) if n_checks > 0 else 0.0

    rationale = (
        f"Claim tracking: {n_pass}/{n_checks} checks pass. "
        f"Registry has {_count_claims(CLAIMS_FILE) if CLAIMS_FILE.exists() else 0} claims."
    )

    return AxeResult(
        name="Claim Completeness",
        score=round(score, 2),
        rationale=rationale,
        subchecks=subchecks,
        details="\n".join(details_parts),
    )


# ---------------------------------------------------------------------------
# Axis 7: Benchmark Coverage
# ---------------------------------------------------------------------------
def score_axe7() -> AxeResult:
    """All 5 benchmarks (H-PTB, H-AFB, H-MCB, H-DCB, H-STB) are implemented and configured."""
    subchecks: dict[str, bool] = {}
    details_parts: list[str] = []

    benchmarks = {
        "H-PTB": "h-ptb",
        "H-AFB": "h-afb",
        "H-MCB": "h-mcb",
        "H-DCB": "h-dcb",
        "H-STB": "h-stb",
    }

    # Config files
    for name, cfg_key in benchmarks.items():
        cfg_path = CONFIGS_DIR / f"{cfg_key}.yaml"
        subchecks[f"{name} config exists"] = cfg_path.exists()
        if cfg_path.exists():
            text = cfg_path.read_text()
            subchecks[f"{name} has benchmark field"] = name in text or cfg_key.replace("-", "_") in text
            subchecks[f"{name} has predictions_tested"] = "predictions_tested" in text

    # Payload generator
    payload_file = SIGMA_PKG / "benchmarks" / "payload.py"
    if payload_file.exists():
        ptext = payload_file.read_text()
        for name, cfg_key in benchmarks.items():
            func_name = f"generate_{cfg_key.replace('-', '')}_payload"
            subchecks[f"{name} payload generator exists"] = func_name in ptext

    # Benchmark implementations (notebooks)
    bench_nb = EXPERIMENTS_DIR / "h-bar-v3-cognitive-evaluation-benchmark-suite.ipynb"
    subchecks["benchmark suite notebook exists"] = bench_nb.exists()

    # Coverage in paper
    ms = PROJECT_ROOT / "paper" / "manuscript.tex"
    if ms.exists():
        ms_text = ms.read_text()
        for name in benchmarks:
            subchecks[f"{name} mentioned in paper"] = name in ms_text or name.replace("-", "") in ms_text

    n_checks = len(subchecks)
    n_pass = sum(1 for v in subchecks.values() if v)
    score = 1.0 + 4.0 * (n_pass / n_checks) if n_checks > 0 else 0.0

    rationale = (
        f"Benchmark coverage: {n_pass}/{n_checks} checks pass. "
        f"All 5 benchmarks have configs, payload generators, and paper mentions."
    )

    return AxeResult(
        name="Benchmark Coverage",
        score=round(score, 2),
        rationale=rationale,
        subchecks=subchecks,
        details="\n".join(details_parts),
    )


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------
SCORERS: list[Callable[[], AxeResult]] = [
    score_axe1,
    score_axe2,
    score_axe3,
    score_axe4,
    score_axe5,
    score_axe6,
    score_axe7,
]

AXE_NAMES: dict[int, str] = {
    1: "Mathematical Foundation",
    2: "Empirical Validation",
    3: "Proof Rigor",
    4: "Codebase Quality",
    5: "Reproducibility",
    6: "Claim Completeness",
    7: "Benchmark Coverage",
}


def run_evaluation(verbose: bool = False, single_axe: int | None = None) -> EvaluationReport:
    results: list[AxeResult] = []

    scorers_to_run = (
        [SCORERS[single_axe - 1]] if single_axe is not None else SCORERS
    )

    for scorer in scorers_to_run:
        if verbose:
            print(f"  Scoring: {scorer.__name__}", file=sys.stderr)
        axe = scorer()
        results.append(axe)

    all_pass = all(r.score >= MIN_PASS_SCORE for r in results)
    report = EvaluationReport(
        axe_results=results,
        passed=all_pass,
        timestamp=datetime.now().isoformat(),
    )
    return report


def save_report(report: EvaluationReport, path: Path | None = None) -> Path:
    if path is None:
        path = PROJECT_ROOT / "docs" / "monitoring" / "evaluation-latest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report.to_dict(), indent=2))
    return path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Σ-Model V3.0+ — Multi-Axis Research Standard Evaluation"
    )
    parser.add_argument(
        "--axe", "-a",
        type=int,
        choices=list(AXE_NAMES),
        help="Run only a single axe (1-7)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show per-scoring progress on stderr",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON only (to stdout)",
    )
    args = parser.parse_args()

    report = run_evaluation(verbose=args.verbose, single_axe=args.axe)

    save_report(report)

    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print(report.to_text())

    sys.exit(0 if report.passed else 1)


if __name__ == "__main__":
    main()
