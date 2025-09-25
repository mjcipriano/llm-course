"""Utilities for Lesson 2 (Embeddings & Similarity)."""
from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Dict, Iterable, List, Sequence, Tuple

import numpy as np


@dataclass
class Vocabulary:
    words: Sequence[str]
    word_to_index: Dict[str, int]
    index_to_word: Dict[int, str]


def prepare_tokens(text: str) -> List[str]:
    """Lower-case ``text`` and return alphanumeric tokens."""
    return re.findall(r"[a-zA-Z']+", text.lower())


def build_vocabulary(tokens: Iterable[str]) -> Vocabulary:
    words = sorted(set(tokens))
    word_to_index = {w: i for i, w in enumerate(words)}
    index_to_word = {i: w for w, i in word_to_index.items()}
    return Vocabulary(words, word_to_index, index_to_word)


def build_cooccurrence(tokens: Sequence[str], vocab: Vocabulary, window: int = 2) -> np.ndarray:
    """Build a symmetric co-occurrence matrix."""
    V = len(vocab.words)
    matrix = np.zeros((V, V), dtype=np.float32)
    for i, token in enumerate(tokens):
        wi = vocab.word_to_index[token]
        left = max(0, i - window)
        right = min(len(tokens), i + window + 1)
        for j in range(left, right):
            if j == i:
                continue
            wj = vocab.word_to_index[tokens[j]]
            matrix[wi, wj] += 1.0
    return matrix


def compute_embeddings(cooccurrence: np.ndarray, dims: int = 16) -> np.ndarray:
    """Return truncated SVD embeddings just like in the notebook."""
    U, S, _ = np.linalg.svd(cooccurrence + 1e-6, full_matrices=False)
    dims = min(dims, U.shape[1])
    return U[:, :dims] * S[:dims]


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    """Return cosine similarity between two vectors."""
    denom = float(np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / (denom + 1e-9))


def neighbors(
    query: str,
    embeddings: np.ndarray,
    vocab: Vocabulary,
    k: int = 8,
) -> List[Tuple[float, str]]:
    """Return the ``k`` nearest neighbours of ``query`` using cosine similarity."""
    if query not in vocab.word_to_index:
        return []
    qi = vocab.word_to_index[query]
    sims: List[Tuple[float, str]] = []
    for i in range(len(vocab.words)):
        if i == qi:
            continue
        sims.append((cosine(embeddings[qi], embeddings[i]), vocab.index_to_word[i]))
    sims.sort(key=lambda item: item[0], reverse=True)
    return sims[:k]


__all__ = [
    "Vocabulary",
    "prepare_tokens",
    "build_vocabulary",
    "build_cooccurrence",
    "compute_embeddings",
    "cosine",
    "neighbors",
]
