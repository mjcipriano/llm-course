"""Smoke tests that ensure each lesson notebook renders to HTML."""

from __future__ import annotations

from pathlib import Path


def test_lesson_notebook_renders_without_errors(
    lesson_notebook_path: Path,
    rendered_notebook_html: tuple[str, str],
    lesson_notebook_headings: dict[Path, str],
):
    """Each notebook should convert to HTML without crashing."""

    raw_html, normalized_html = rendered_notebook_html

    # Basic sanity checks that the resulting document looks like HTML and
    # contains the main lesson heading after HTML entities are unescaped.
    assert "<html" in raw_html.lower()
    heading = lesson_notebook_headings[lesson_notebook_path]
    assert heading in normalized_html
