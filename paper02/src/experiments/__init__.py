"""Experiment runners and pipeline orchestration for Paper 02."""

from paper02.src.experiments.run_gate import GateRunConfig, run_gate_suite, train_gate_run
from paper02.src.experiments.trainer import (
    TrainingRunConfig,
    TrainingRunResult,
    evaluate_accuracy,
    run_training_experiment,
)

__all__: list[str] = [
    "GateRunConfig",
    "TrainingRunConfig",
    "TrainingRunResult",
    "evaluate_accuracy",
    "run_gate_suite",
    "run_training_experiment",
    "train_gate_run",
]
