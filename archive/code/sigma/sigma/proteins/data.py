"""Protein data loading, preprocessing, and augmentation."""

from __future__ import annotations

import functools
import gzip
import hashlib
import os
import re
import time
from typing import Optional

import numpy as np
import pandas as pd

try:
    import torch
    from torch.utils.data import Dataset
    TORCH_AVAILABLE = True
except ImportError:
    torch = None
    Dataset = object
    TORCH_AVAILABLE = False
from tqdm import tqdm

try:
    from Bio import Align
    BIO_AVAILABLE = True
except ImportError:
    BIO_AVAILABLE = False

try:
    import pyhmmer
    from pyhmmer.easel import Randomness
    from pyhmmer.hmmer import hmmpress, hmmscan
    from pyhmmer.plan7 import HMMFile
    PYHMMER_AVAILABLE = True
except ImportError:
    PYHMMER_AVAILABLE = False


SPECIAL_TOKENS = {
    "<PAD>": 0,
    "<SOS>": 1,
    "<EOS>": 2,
    "<MASK>": 3,
    "<UNK>": 4,
}
PFAM_FTP_BASE = "https://ftp.ebi.ac.uk/pub/databases/Pfam"
SEQUENCE_ID_RE = re.compile(r"^(?P<protein_id>.+?)/(?P<start>\d+)-(?P<end>\d+)$")


def parse_stockholm(
    filepath: str,
    max_records: Optional[int] = None,
) -> list[dict]:
    """Parse a Stockholm-format file.

    Uses ``Bio.Align.parse()`` for files containing sequence alignments,
    falls back to a lightweight line-by-line parser for metadata-only
    Stockholm files (e.g., ``Pfam-A.hmm.dat``).

    Args:
        filepath: Path to a Stockholm-format file (optionally ``.gz``).
        max_records: Maximum number of Stockholm records to parse. ``None`` = no limit.

    Returns:
        list[dict]: Each dict has keys:
        ``accession``, ``identifier``, ``description``, ``type``,
        ``clan``, ``seq_count``, ``sequences`` (list of dicts with
        ``id``, ``accession``, ``start``, ``end``, ``species``).
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Stockholm file not found: {filepath}")

    if BIO_AVAILABLE and max_records is None:
        try:
            return _parse_with_biopython(filepath)
        except (ValueError, AttributeError, TypeError):
            pass

    return _parse_manual(filepath, max_records=max_records)


def _parse_with_biopython(filepath: str) -> list[dict]:
    records = []
    for alignment in Align.parse(filepath, "stockholm"):
        ann = alignment.annotations
        sequences = []
        for seq in alignment.sequences:
            m = SEQUENCE_ID_RE.match(seq.id)
            start = int(m.group("start")) if m else None
            end = int(m.group("end")) if m else None
            sequences.append({
                "id": seq.id,
                "accession": seq.annotations.get("accession", ""),
                "start": start,
                "end": end,
                "species": seq.id.split("/")[0] if "/" in seq.id else seq.id,
            })
        records.append({
            "accession": ann.get("accession", ""),
            "identifier": ann.get("identifier", ""),
            "description": ann.get("definition", ""),
            "type": ann.get("type", ""),
            "clan": ann.get("clan", ""),
            "seq_count": len(sequences),
            "sequences": sequences,
        })
    return records


def _parse_manual(
    filepath: str,
    max_records: Optional[int] = None,
) -> list[dict]:
    records = []
    current = None

    with _open_file(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#=GF "):
                tag = _parse_gf_tag(line)
                value = _parse_gf_value(line)
                if tag == "ID":
                    if current is not None:
                        records.append(current)
                        if max_records is not None and len(records) >= max_records:
                            return records
                    current = _empty_record(value)
                elif current is not None:
                    _set_record_field(current, tag, value)
            elif line.startswith("#=GS "):
                _parse_gs_line(current, line)
            elif line == "//":
                if current is not None:
                    records.append(current)
                    current = None
                    if max_records is not None and len(records) >= max_records:
                        return records

    if current is not None:
        records.append(current)

    return records


def _parse_gf_tag(line: str) -> str:
    return line[5:7].strip()


def _parse_gf_value(line: str) -> str:
    return line[7:].strip()


def _empty_record(identifier: str) -> dict:
    return {
        "accession": "",
        "identifier": identifier,
        "description": "",
        "type": "",
        "clan": "",
        "length": None,
        "seq_count": 0,
        "sequences": [],
    }


def _set_record_field(rec: dict, tag: str, value: str) -> None:
    if tag == "AC":
        rec["accession"] = value
    elif tag == "DE":
        rec["description"] = value
    elif tag == "TP":
        rec["type"] = value
    elif tag == "CL":
        rec["clan"] = value
    elif tag == "ML":
        try:
            rec["length"] = int(value.split(";")[0].strip())
        except (ValueError, IndexError):
            pass


def _parse_gs_line(rec: Optional[dict], line: str) -> None:
    if rec is None:
        return
    parts = line[5:].strip().split(None, 1)
    if len(parts) < 2:
        return
    seq_id = parts[0]
    gs_tag = parts[1][:2].strip()
    gs_value = parts[1][2:].strip()

    m = SEQUENCE_ID_RE.match(seq_id)
    start = int(m.group("start")) if m else None
    end = int(m.group("end")) if m else None

    seq_entry = {
        "id": seq_id,
        "accession": "",
        "start": start,
        "end": end,
        "species": seq_id.split("/")[0] if "/" in seq_id else seq_id,
    }

    if gs_tag == "AC":
        seq_entry["accession"] = gs_value
        rec["sequences"].append(seq_entry)
        rec["seq_count"] = len(rec["sequences"])


def _open_file(filepath: str):
    if filepath.endswith(".gz"):
        return gzip.open(filepath, "rt", encoding="utf-8")
    return open(filepath, "r", encoding="utf-8")


def extract_domain_architectures(
    records: list[dict],
    min_length: int = 2,
    max_length: int = 15,
) -> list[list[str]]:
    """Extract domain architectures from parsed Stockholm records.

    Groups sequences by protein accession across all family records,
    builds ordered (by genomic position) domain architectures, and
    applies length and overlap filters.

    Args:
        records: Parsed Stockholm records from :func:`parse_stockholm`.
        min_length: Minimum number of domains in an architecture (default 2).
        max_length: Maximum number of domains in an architecture (default 15).

    Returns:
        list[list[str]]: Each element is a list of Pfam accession strings
        representing a protein's domain architecture.
    """
    protein_domains: dict[str, list[tuple[str, Optional[int], Optional[int]]]] = {}

    for rec in records:
        fam_acc = rec.get("accession", "")
        if not fam_acc:
            continue
        for seq in rec.get("sequences", []):
            prot_id = seq.get("accession") or seq.get("id", "")
            if not prot_id:
                continue
            protein_domains.setdefault(prot_id, []).append((
                fam_acc,
                seq.get("start"),
                seq.get("end"),
            ))

    architectures = []
    for domains in protein_domains.values():
        valid = [(acc, s, e) for acc, s, e in domains if s is not None and e is not None]
        if len(valid) < 2:
            continue
        valid.sort(key=lambda x: x[1])

        for i in range(1, len(valid)):
            if valid[i][1] < valid[i-1][2]:
                break
        else:
            arch = [acc for acc, _, _ in valid]
            if min_length <= len(arch) <= max_length:
                architectures.append(arch)

    return architectures


def build_domain_vocab(
    architectures: list[list[str]],
    clan_map_path: Optional[str] = None,
) -> tuple[dict[str, int], dict[int, str], dict[str, str]]:
    """Build vocabulary mappings for domain architectures.

    Args:
        architectures: Domain architecture sequences.
        clan_map_path: Path to ``Pfam-A.clans.tsv`` for building clan-level mapping.

    Returns:
        token2id: Token to integer ID mapping (special tokens 0-4 reserved).
        id2token: Integer ID to token mapping.
        clan_map: Pfam accession to clan ID mapping.
    """
    all_domains = set()
    for arch in architectures:
        all_domains.update(arch)

    token2id = dict(SPECIAL_TOKENS)
    next_id = len(SPECIAL_TOKENS)
    for domain in sorted(all_domains):
        token2id[domain] = next_id
        next_id += 1

    id2token = {v: k for k, v in token2id.items()}

    clan_map = {}
    if clan_map_path and os.path.isfile(clan_map_path):
        with open(clan_map_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("\t")
                if len(parts) >= 2:
                    clan_map[parts[0]] = parts[1]

    return token2id, id2token, clan_map


class PfamDataset(Dataset):
    """PyTorch Dataset for Pfam domain architecture language modelling.

    Each architecture is converted to ``(src, tgt)`` pairs where the
    model learns to predict the next domain given previous domains
    (causal language modelling).

    Args:
        architectures: Domain architecture sequences.
        vocab: Token-to-ID vocabulary mapping.
        max_len: Maximum sequence length for padding/truncation (default 20).
    """

    def __init__(
        self,
        architectures: list[list[str]],
        vocab: dict[str, int],
        max_len: int = 20,
    ):
        self.architectures = architectures
        self.vocab = vocab
        self.max_len = max_len
        self.pad_idx = vocab["<PAD>"]
        self.sos_idx = vocab["<SOS>"]
        self.eos_idx = vocab["<EOS>"]
        self.unk_idx = vocab["<UNK>"]

        self._tokenized: list[tuple[list[int], list[int]]] = []
        for arch in architectures:
            tokens = [self.vocab.get(d, self.unk_idx) for d in arch]
            src = tokens[:-1]
            tgt = [self.sos_idx] + tokens + [self.eos_idx]
            self._tokenized.append((src, tgt))

    def __len__(self) -> int:
        """Return the number of architectures in the dataset."""
        return len(self._tokenized)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        """Return a padded ``(src, tgt)`` pair for the architecture at ``idx``.

        Args:
            idx: Index into the dataset.

        Returns:
            (src_tensor, tgt_tensor) each of shape ``(max_len,)`` with dtype ``torch.long``.
        """
        src, tgt = self._tokenized[idx]
        pad = self.pad_idx

        src = (src + [pad] * self.max_len)[: self.max_len]
        tgt = (tgt + [pad] * self.max_len)[: self.max_len]

        return (
            torch.tensor(src, dtype=torch.long),
            torch.tensor(tgt, dtype=torch.long),
        )


def download_pfam(
    output_dir: str,
    pfam_version: str = "38.2",
    files: Optional[list[str]] = None,
) -> None:
    """Idempotent download of Pfam data files.

    Skips files whose SHA256 matches the existing local copy.

    Args:
        output_dir: Directory to save files (a ``raw/`` subdirectory is created).
        pfam_version: Pfam version string (default ``"38.2"``).
        files: List of filenames to download. Defaults to essential files.
    """
    raw_dir = os.path.join(output_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)

    if files is None:
        files = [
            "Pfam-A.hmm.gz",
            "Pfam-A.seed.gz",
            "Pfam-A.hmm.dat.gz",
            "Pfam-A.clans.tsv.gz",
            "Pfam.version.gz",
        ]

    for fname in files:
        dest = os.path.join(raw_dir, fname)

        local_hash = _compute_sha256(dest) if os.path.isfile(dest) else None
        if local_hash is not None:
            print(f"  {fname}: already exists (SHA256: {local_hash[:16]}...), skipping")
            continue

        url = f"{PFAM_FTP_BASE}/current_release/{fname}"
        _download_with_retry(url, dest, desc=fname)
        new_hash = _compute_sha256(dest)
        print(f"  {fname}: downloaded (SHA256: {new_hash[:16]}...)")


def _compute_sha256(filepath: str) -> Optional[str]:
    try:
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except (IOError, OSError):
        return None


def _download_with_retry(
    url: str,
    dest: str,
    desc: str = "",
    retries: int = 3,
) -> None:
    """Download a file with retry logic and progress bar."""
    import urllib.error
    import urllib.request

    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url) as response:
                total = int(response.headers.get("Content-Length", 0))
                with tqdm(
                    total=total, unit="B", unit_scale=True, desc=desc, leave=False,
                ) as pbar:
                    with open(dest + ".tmp", "wb") as f:
                        while True:
                            chunk = response.read(65536)
                            if not chunk:
                                break
                            f.write(chunk)
                            pbar.update(len(chunk))
            os.replace(dest + ".tmp", dest)
            return
        except (urllib.error.URLError, OSError) as e:
            if attempt < retries - 1:
                time.sleep(2**attempt)
            else:
                raise RuntimeError(
                    f"Failed to download {url} after {retries} attempts: {e}"
                )


def get_domain_metadata(
    hmm_dat_path: str,
    clans_tsv_path: str,
) -> pd.DataFrame:
    """Build a DataFrame of Pfam domain metadata.

    Args:
        hmm_dat_path: Path to ``Pfam-A.hmm.dat`` (or ``.gz``).
        clans_tsv_path: Path to ``Pfam-A.clans.tsv`` (or ``.gz``).

    Returns:
        pd.DataFrame: Columns: ``pfam_accession``, ``clan``, ``family_name``,
        ``family_type``, ``description``, ``length``.
    """
    records = parse_stockholm(hmm_dat_path)

    rows = []
    for rec in records:
        rows.append({
            "pfam_accession": rec.get("accession", ""),
            "family_name": rec.get("identifier", ""),
            "family_type": rec.get("type", ""),
            "description": rec.get("description", ""),
            "clan": rec.get("clan", ""),
            "length": rec.get("length"),
        })

    df = pd.DataFrame(rows)

    if os.path.isfile(clans_tsv_path):
        clan_rows = []
        with _open_file(clans_tsv_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("\t")
                if len(parts) >= 5:
                    clan_rows.append({
                        "base_accession": parts[0],
                        "clan_from_tsv": parts[1],
                        "clan_label": parts[2],
                        "family_label": parts[3],
                        "clan_description": parts[4],
                    })
        if clan_rows:
            clan_df = pd.DataFrame(clan_rows)
            # Strip version suffix from hmm.dat accessions for matching
            # (clans.tsv has no version suffix; hmm.dat has e.g. PF00001.1)
            df["base_accession"] = df["pfam_accession"].str.replace(
                r"\.\d+$", "", regex=True
            )
            df = df.merge(clan_df, on="base_accession", how="left")
            df["clan"] = df["clan_from_tsv"].fillna(df["clan"])
            df.drop(columns=["clan_from_tsv", "base_accession"], inplace=True)

    return df


# ── HMMER Bit Score Computation ──────────────────────────────


def _find_hmm(accession: str, hmm_path: str) -> "pyhmmer.plan7.HMM":
    """Find and return an HMM by accession from a flat HMM file."""
    if not PYHMMER_AVAILABLE:
        raise ImportError("pyhmmer is required for HMMER bit score computation")
    acc_stripped = accession.split(".")[0] if "." in accession else accession
    with HMMFile(hmm_path) as f:
        for hmm in f:
            hmm_acc = hmm.accession.split(".")[0] if "." in hmm.accession else hmm.accession
            if hmm_acc == acc_stripped:
                return hmm
    raise ValueError(f"HMM accession {accession!r} not found in {hmm_path}")


def compute_domain_similarity(
    accession_a: str,
    accession_b: str,
    *,
    hmm_path: str = "data/pfam/raw/Pfam-A.hmm",
    seed: int = 42,
) -> float:
    """Compute normalized HMMER bit score similarity between two Pfam families.

    Emits a deterministic random sequence from each HMM (via ``emit_sequence``),
    scores both directions with ``hmmscan``, and symmetrizes.
    Normalizes by the geometric mean of self-scores so that 1.0 = identical.

    Args:
        accession_a: Pfam accession (e.g. ``PF00001.1``).
        accession_b: Pfam accession (e.g. ``PF00002.1``).
        hmm_path: Path to the Pfam-A HMM file.
        seed: Random seed for reproducible sequence emission.

    Returns:
        float: Similarity in [0, 1]. 1.0 if same accession; 0.0 if no cross-score
        was reported (very dissimilar families).
    """
    if accession_a == accession_b:
        return 1.0

    hmm_a = _find_hmm(accession_a, hmm_path)
    hmm_b = _find_hmm(accession_b, hmm_path)

    rng = Randomness(seed)
    seq_a = hmm_a.emit_sequence(rng)
    seq_b = hmm_b.emit_sequence(rng)
    seq_a.name = hmm_a.accession.encode() if isinstance(hmm_a.accession, str) else hmm_a.accession
    seq_b.name = hmm_b.accession.encode() if isinstance(hmm_b.accession, str) else hmm_b.accession

    def _score(query, target_hmms):
        for top_hits in hmmscan([query], target_hmms):
            return {hit.accession: hit.score for hit in top_hits}
        return {}

    scores_ab = _score(seq_a, [hmm_a, hmm_b])
    scores_ba = _score(seq_b, [hmm_a, hmm_b])

    a_to_b = scores_ab.get(hmm_b.accession, 0.0)
    b_to_a = scores_ba.get(hmm_a.accession, 0.0)

    a_to_a = scores_ab.get(hmm_a.accession, 1.0) or 1.0
    b_to_b = scores_ba.get(hmm_b.accession, 1.0) or 1.0

    cross = (a_to_b + b_to_a) / 2.0
    denom = (a_to_a * b_to_b) ** 0.5
    if denom <= 0:
        return 0.0
    return max(0.0, min(1.0, cross / denom))


def precompute_similarity_matrix(
    accessions: list[str],
    hmm_path: str = "data/pfam/raw/Pfam-A.hmm",
    output_path: str = "data/pfam/processed/similarity_matrix.npy",
    *,
    force: bool = False,
    e_value: float = 1000.0,
    cpus: int = 0,
    seed: int = 42,
) -> np.ndarray:
    """Precompute the N×N pairwise domain similarity matrix.

    Presses the HMM database (if not already pressed), loads all HMMs into
    memory, and for each family emits a deterministic sequence and scans it
    against the full database. Results are cached as a ``.npy`` file.

    Args:
        accessions: List of Pfam accessions in the desired row/column order.
        hmm_path: Path to the Pfam-A HMM file.
        output_path: Where to save the N×N float32 matrix (``.npy`` format).
        force: If False (default), skip computation if ``output_path`` exists.
        e_value: E-value threshold for ``hmmscan`` (default 1000.0 — very permissive).
        cpus: Number of CPU cores for ``hmmscan`` parallelism (0 = all available).
        seed: Seed for HMMER emitted-sequence RNG (default 42). Each family uses
            ``seed * n + i + 1`` for unique but reproducible per-family seeds.

    Returns:
        np.ndarray: N×N symmetric matrix with values in [0, 1], diagonal = 1.0.
    """

    if not PYHMMER_AVAILABLE:
        raise ImportError("pyhmmer is required for similarity matrix computation")

    if not force and os.path.isfile(output_path):
        print(f"Loading cached similarity matrix from {output_path}")
        return np.load(output_path)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Press HMM database if needed
    pressed = hmm_path + ".h3m"
    if not os.path.isfile(pressed):
        print("Pressing HMM database ...")
        hmmpress(hmm_path)

    # Load all HMMs into memory
    print(f"Loading {len(accessions)} HMMs into memory ...")
    hmm_dict: dict[str, "pyhmmer.plan7.HMM"] = {}
    with HMMFile(hmm_path) as f:
        for hmm in f:
            acc = hmm.accession.split(".")[0] if "." in hmm.accession else hmm.accession
            if acc in {a.split(".")[0] for a in accessions}:
                hmm_dict[acc] = hmm
                if len(hmm_dict) == len(accessions):
                    break

    missing = [a for a in accessions if a.split(".")[0] not in hmm_dict]
    if missing:
        raise ValueError(f"{len(missing)} accessions not found in HMM file: {missing[:5]}...")

    n = len(accessions)
    matrix = np.zeros((n, n), dtype=np.float32)
    acc_to_idx = {a.split(".")[0]: j for j, a in enumerate(accessions)}

    all_hmm_list = list(hmm_dict.values())

    for i, acc in enumerate(accessions):
        acc_stripped = acc.split(".")[0]
        hmm = hmm_dict[acc_stripped]

        rng = Randomness(seed * n + i + 1)
        seq = hmm.emit_sequence(rng)
        seq.name = acc.encode() if isinstance(acc, str) else acc

        row = np.zeros(n, dtype=np.float32)
        for top_hits in hmmscan([seq], all_hmm_list, cpus=cpus, E=e_value):
            for hit in top_hits:
                hit_acc = hit.accession.split(".")[0] if "." in hit.accession else hit.accession
                j = acc_to_idx.get(hit_acc)
                if j is not None:
                    row[j] = hit.score
            break

        self_score = row[i] if row[i] > 0 else 1.0
        if self_score > 0:
            row = row / self_score
        matrix[i] = np.clip(row, 0.0, 1.0)

        if (i + 1) % 100 == 0:
            print(f"  Processed {i + 1}/{n} families")

    np.fill_diagonal(matrix, 1.0)

    print(f"Saving similarity matrix to {output_path}")
    np.save(output_path, matrix)

    return matrix


# ── Fold Compatibility ───────────────────────────────────────


@functools.lru_cache(maxsize=1)
def _load_clans(clans_tsv_path: str) -> dict[str, str]:
    """Load Pfam accession → clan mapping from a clans TSV file.

    Cached after first call to avoid repeated parsing.
    """
    clan_map: dict[str, str] = {}
    with _open_file(clans_tsv_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                clan_map[parts[0]] = parts[1]
    return clan_map


def compute_fold_compatibility(
    accession_a: str,
    accession_b: str,
    *,
    clans_tsv_path: str = "data/pfam/raw/Pfam-A.clans.tsv",
) -> float:
    """Compute fold compatibility between two Pfam families.

    Uses clan membership as the primary signal:
    - **Same clan**: 0.9 (high compatibility — evolutionary related)
    - **Different clan**: 0.1 (low compatibility)

    A PDB interaction tier (medium = 0.6 for different-clan pairs with
    known structural interaction) is reserved for future use when iPfam
    or 3did data becomes available.

    Args:
        accession_a: Pfam accession (e.g. ``PF00001.1``).
        accession_b: Pfam accession (e.g. ``PF00002.1``).
        clans_tsv_path: Path to ``Pfam-A.clans.tsv``.

    Returns:
        float: Compatibility score in {0.1, 0.9}.
    """
    if accession_a == accession_b:
        return 0.9

    clan_map = _load_clans(clans_tsv_path)

    def _base(acc: str) -> str:
        return acc.split(".")[0] if "." in acc else acc

    clan_a = clan_map.get(_base(accession_a))
    clan_b = clan_map.get(_base(accession_b))

    if clan_a and clan_b and clan_a == clan_b:
        return 0.9
    return 0.1
