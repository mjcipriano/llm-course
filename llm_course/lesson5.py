"""Utilities for Lesson 5 (Fine-tuning with Hugging Face)."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Protocol


@dataclass
class CorpusConfig:
    data_dir: Path
    corpus_files: Iterable[str]


def aggregate_texts(config: CorpusConfig, encoding: str = "utf-8") -> str:
    """Concatenate multiple corpus files just like in the notebook."""
    texts: List[str] = []
    for name in config.corpus_files:
        path = config.data_dir / name
        texts.append(path.read_text(encoding=encoding))
    return "\n".join(texts)


class SupportsTokenize(Protocol):
    def __call__(self, text: str, *, truncation: bool, max_length: int) -> dict:
        ...


def tokenize_texts(
    tokenizer: SupportsTokenize,
    texts: Iterable[str],
    *,
    truncation: bool = True,
    max_length: int = 512,
) -> List[dict]:
    """Tokenise ``texts`` with a ``tokenizer`` that mimics the notebook behaviour."""
    batches = []
    for text in texts:
        batches.append(tokenizer(text, truncation=truncation, max_length=max_length))
    return batches


__all__ = ["CorpusConfig", "aggregate_texts", "tokenize_texts", "SupportsTokenize"]
