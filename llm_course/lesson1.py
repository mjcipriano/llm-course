"""Utilities mirroring Lesson 1 (Tokens & Tokenizers)."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
from typing import Iterable, List, Sequence, Tuple

CorpusFiles = Sequence[str]
Merge = Tuple[str, str]


def aggregate_corpus(
    data_dir: Path | str,
    corpus_files: CorpusFiles,
    encoding: str = "utf-8",
) -> str:
    """Return concatenated text for the requested files.

    Parameters
    ----------
    data_dir:
        Directory that contains the text files.
    corpus_files:
        Iterable of file names to concatenate.
    encoding:
        File encoding used when reading the corpus.
    """
    base = Path(data_dir)
    texts: List[str] = []
    for name in corpus_files:
        path = base / name
        texts.append(path.read_text(encoding=encoding))
    return "\n".join(texts)


def get_vocab(text: str) -> Counter[str]:
    """Return the character-level vocabulary with ``</w>`` markers."""
    words = re.findall(r"\S+", text.lower())
    return Counter(" ".join(list(word)) + " </w>" for word in words)


def get_stats(vocab: Counter[str]) -> Counter[Merge]:
    """Count symbol pair frequencies for the current vocabulary."""
    pairs: Counter[Merge] = Counter()
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs


def merge_vocab(pair: Merge, vocab_in: Counter[str]) -> Counter[str]:
    """Merge the given ``pair`` inside ``vocab_in`` and return an updated copy."""
    merged = Counter()
    bigram = " ".join(pair)
    replacement = "".join(pair)
    for word, freq in vocab_in.items():
        merged[word.replace(bigram, replacement)] += freq
    return merged


def learn_bpe(text: str, num_merges: int) -> List[Merge]:
    """Learn a list of BPE merges for ``text``."""
    vocab = get_vocab(text)
    merges: List[Merge] = []
    for _ in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        merges.append(best)
        vocab = merge_vocab(best, vocab)
    return merges


def tokenize(word: str, merges: Iterable[Merge]) -> List[str]:
    """Tokenise ``word`` according to ``merges`` learned by ``learn_bpe``."""
    symbols: List[str] = list(word.lower()) + ["</w>"]
    for a, b in merges:
        i = 0
        while i < len(symbols) - 1:
            if symbols[i] == a and symbols[i + 1] == b:
                symbols[i : i + 2] = [a + b]
            else:
                i += 1
    if symbols and symbols[-1] == "</w>":
        symbols = symbols[:-1]
    return symbols


__all__ = [
    "aggregate_corpus",
    "get_vocab",
    "get_stats",
    "merge_vocab",
    "learn_bpe",
    "tokenize",
]
