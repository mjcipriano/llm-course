"""Convenience re-exports for the course notebooks."""
from __future__ import annotations

from importlib import import_module
from types import ModuleType
from typing import Dict, Tuple

_IMPORT_MAP: Dict[str, Tuple[str, str]] = {
    # Lesson 1
    "lesson1_aggregate_corpus": ("llm_course.lesson1", "aggregate_corpus"),
    "lesson1_get_stats": ("llm_course.lesson1", "get_stats"),
    "lesson1_get_vocab": ("llm_course.lesson1", "get_vocab"),
    "lesson1_learn_bpe": ("llm_course.lesson1", "learn_bpe"),
    "lesson1_merge_vocab": ("llm_course.lesson1", "merge_vocab"),
    "lesson1_tokenize": ("llm_course.lesson1", "tokenize"),
    # Lesson 2
    "lesson2_prepare_tokens": ("llm_course.lesson2", "prepare_tokens"),
    "lesson2_build_vocabulary": ("llm_course.lesson2", "build_vocabulary"),
    "lesson2_build_cooccurrence": ("llm_course.lesson2", "build_cooccurrence"),
    "lesson2_compute_embeddings": ("llm_course.lesson2", "compute_embeddings"),
    "lesson2_cosine": ("llm_course.lesson2", "cosine"),
    "lesson2_neighbors": ("llm_course.lesson2", "neighbors"),
    # Lesson 3
    "lesson3_ngrams": ("llm_course.lesson3", "ngrams"),
    "lesson3_train_ngram": ("llm_course.lesson3", "train_ngram"),
    "lesson3_sample": ("llm_course.lesson3", "sample"),
    "lesson3_cross_entropy": ("llm_course.lesson3", "cross_entropy"),
    # Lesson 4
    "SelfAttention": ("llm_course.lesson4", "SelfAttention"),
    "TinyTransformer": ("llm_course.lesson4", "TinyTransformer"),
    "lesson4_encode": ("llm_course.lesson4", "encode"),
    "lesson4_decode": ("llm_course.lesson4", "decode"),
    # Lesson 5
    "lesson5_aggregate_texts": ("llm_course.lesson5", "aggregate_texts"),
    "lesson5_tokenize_texts": ("llm_course.lesson5", "tokenize_texts"),
    # Lesson 6
    "lesson6_FORBIDDEN": ("llm_course.lesson6", "FORBIDDEN"),
    "lesson6_safe_input": ("llm_course.lesson6", "safe_input"),
    "lesson6_train_bigram": ("llm_course.lesson6", "train_bigram"),
    "lesson6_cross_entropy": ("llm_course.lesson6", "cross_entropy"),
}

__all__ = sorted(_IMPORT_MAP)


def _load(name: str):
    module_name, attr = _IMPORT_MAP[name]
    try:
        module: ModuleType = import_module(module_name)
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on optional deps
        if module_name.endswith("lesson4") and exc.name == "torch":
            raise ModuleNotFoundError(
                "PyTorch is required to use Lesson 4 utilities"
            ) from exc
        raise
    value = getattr(module, attr)
    globals()[name] = value
    return value


def __getattr__(name: str):  # pragma: no cover - simple attribute hook
    if name in _IMPORT_MAP:
        return _load(name)
    raise AttributeError(name)


def __dir__():  # pragma: no cover - debugging helper
    return sorted(list(globals()) + list(_IMPORT_MAP))
