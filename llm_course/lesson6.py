"""Utilities for Lesson 6 (Evaluation, Prompting, Safety)."""
from __future__ import annotations

import collections
import math
import re
from typing import Iterable, List, Sequence, Tuple

Token = str
BigramProb = Tuple[str, str]
FORBIDDEN = [
    r"how to make a bomb",
    r"credit card number",
    r"social security number",
]


def ngrams(tokens: Sequence[Token], n: int) -> Iterable[Tuple[Token, ...]]:
    for i in range(len(tokens) - n + 1):
        yield tuple(tokens[i : i + n])


def train_bigram(tokens: Sequence[Token], k: float = 0.5):
    counts = collections.Counter(ngrams(tokens, 2))
    ctx_counts = collections.Counter(ngrams(tokens, 1))
    vocab = sorted(set(tokens))
    V = len(vocab)

    def prob(prev: Token, nxt: Token) -> float:
        return (counts[(prev, nxt)] + k) / (ctx_counts[(prev,)] + k * V)

    return prob, vocab


def cross_entropy(prob, tokens: Sequence[Token]) -> Tuple[float, float]:
    split = int(0.8 * len(tokens))
    test = tokens[split:]
    H = 0.0
    count = 0
    for i in range(1, len(test)):
        p = max(prob(test[i - 1], test[i]), 1e-12)
        H += -math.log2(p)
        count += 1
    H = H / max(count, 1)
    return H, 2 ** H


def safe_input(user_text: str) -> Tuple[bool, str]:
    t = user_text.lower()
    for pattern in FORBIDDEN:
        if re.search(pattern, t):
            return False, f"Blocked by rule: {pattern}"
    return True, "ok"


__all__ = ["FORBIDDEN", "ngrams", "train_bigram", "cross_entropy", "safe_input"]
