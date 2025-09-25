"""Utilities for Lesson 3 (N-gram language models)."""
from __future__ import annotations

import collections
import math
import random
from typing import Callable, Iterable, Iterator, List, Sequence, Tuple

Token = str
NGram = Tuple[Token, ...]
ProbabilityFn = Callable[[NGram, Token], float]


def ngrams(tokens: Sequence[Token], n: int) -> Iterator[NGram]:
    """Yield ``n``-grams from ``tokens``."""
    if n <= 0:
        raise ValueError("n must be positive")
    for i in range(len(tokens) - n + 1):
        yield tuple(tokens[i : i + n])


def train_ngram(tokens: Sequence[Token], n: int = 2, k: float = 1.0) -> Tuple[ProbabilityFn, List[Token]]:
    """Train a Laplace-smoothed ``n``-gram model."""
    if n < 1:
        raise ValueError("n must be >= 1")
    counts = collections.Counter(ngrams(tokens, n))
    ctx_counts = collections.Counter(ngrams(tokens, n - 1)) if n > 1 else None
    vocab = sorted(set(tokens))
    V = len(vocab)

    def prob(context: NGram, word: Token) -> float:
        if n == 1:
            total = len(tokens)
            return (counts[(word,)] + k) / (total + k * V)
        ctx = ctx_counts[context]
        return (counts[context + (word,)] + k) / (ctx + k * V)

    return prob, vocab


def sample(
    prob: ProbabilityFn,
    vocab: Sequence[Token],
    n: int = 2,
    max_len: int = 30,
    temperature: float = 1.0,
    seed: int | None = None,
) -> List[Token]:
    """Sample a sequence from an ``n``-gram model."""
    random.seed(seed)
    if n == 1:
        context: List[Token] = []
    elif n == 2:
        context = [random.choice(vocab)]
    else:
        context = [random.choice(vocab), random.choice(vocab)]

    result: List[Token] = []
    for _ in range(max_len):
        scores = [prob(tuple(context[-(n - 1):]), w) ** (1.0 / temperature) for w in vocab]
        total = sum(scores)
        r = random.random() * total
        cum = 0.0
        chosen = vocab[0]
        for w, score in zip(vocab, scores):
            cum += score
            if cum >= r:
                chosen = w
                break
        result.append(chosen)
        if n == 1:
            context = []
        else:
            context = (context + [chosen])[-(n - 1):]
    return result


def cross_entropy(
    prob: ProbabilityFn,
    tokens: Sequence[Token],
    n: int,
    split: float = 0.8,
) -> float:
    """Return the cross-entropy on the held-out set."""
    if not 0 < split < 1:
        raise ValueError("split must be between 0 and 1")
    pivot = int(len(tokens) * split)
    test = tokens[pivot:]
    if n == 1:
        contexts = [() for _ in test]
    else:
        contexts = [tuple(test[max(0, i - (n - 1)) : i]) for i in range(len(test))]
    H = 0.0
    count = 0
    for ctx, word in zip(contexts, test):
        if len(ctx) != n - 1:
            continue
        p = max(prob(ctx, word), 1e-12)
        H += -math.log2(p)
        count += 1
    return H / max(count, 1)


__all__ = ["ngrams", "train_ngram", "sample", "cross_entropy"]
