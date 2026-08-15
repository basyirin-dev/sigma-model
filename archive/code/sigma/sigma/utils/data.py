import torch
from torch.utils.data import Dataset


class SCANDataset(Dataset):
    def __init__(self, pairs: list[tuple[str, str]], vocab: dict[str, int], max_len: int = 50):
        self.pairs = pairs
        self.vocab = vocab
        self.max_len = max_len
        self.pad_idx = vocab["<PAD>"]
        self.sos_idx = vocab["<SOS>"]
        self.eos_idx = vocab["<EOS>"]

    def __len__(self) -> int:
        return len(self.pairs)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        cmd, action = self.pairs[idx]
        cmd_tok = [self.vocab.get(t, 3) for t in cmd.split()]
        act_tok = (
            [self.sos_idx]
            + [self.vocab.get(t, 3) for t in action.split()]
            + [self.eos_idx]
        )
        pad = self.pad_idx
        cmd_tok = (cmd_tok + [pad] * self.max_len)[: self.max_len]
        act_tok = (act_tok + [pad] * self.max_len)[: self.max_len]
        return (
            torch.tensor(cmd_tok, dtype=torch.long),
            torch.tensor(act_tok, dtype=torch.long),
        )
