"""Data generators, synthetic compositionality splits, and dataset loaders."""

from paper.src.data.audit_leakage import (
    SplitAuditResult,
    ZeroLeakageAuditReport,
    audit_dataset_suite,
    audit_split_pair,
)
from paper.src.data.hbar import (
    HBarDataGenerator,
    HBarGrammar,
    HBarSplitSuite,
)
from paper.src.data.hbar_dataset import (
    HBarDataset,
    HBarDataSplits,
    create_hbar_dataloaders,
    generate_hbar_splits,
)
from paper.src.data.loaders import (
    Seq2SeqDataset,
    collate_seq2seq,
    create_dataloader,
    generate_substitution_pairs,
)

__all__: list[str] = [
    "HBarDataGenerator",
    "HBarDataSplits",
    "HBarDataset",
    "HBarGrammar",
    "HBarSplitSuite",
    "Seq2SeqDataset",
    "SplitAuditResult",
    "ZeroLeakageAuditReport",
    "audit_dataset_suite",
    "audit_split_pair",
    "collate_seq2seq",
    "create_dataloader",
    "create_hbar_dataloaders",
    "generate_hbar_splits",
    "generate_substitution_pairs",
]
