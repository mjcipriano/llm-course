import sys
from pathlib import Path
from typing import Iterable

import nbformat
import pytest
from nbconvert import HTMLExporter
from html import unescape

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS_DIR = ROOT / "notebooks"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _discover_lesson_notebooks() -> list[Path]:
    notebooks = sorted(NOTEBOOKS_DIR.glob("L*_*.ipynb"))
    if not notebooks:
        raise RuntimeError("No lesson notebooks found under the notebooks directory.")
    return notebooks


LESSON_NOTEBOOKS = _discover_lesson_notebooks()


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """Parameterize tests that accept a lesson_notebook_path argument."""

    if "lesson_notebook_path" in metafunc.fixturenames:
        metafunc.parametrize(
            "lesson_notebook_path",
            LESSON_NOTEBOOKS,
            ids=[path.stem for path in LESSON_NOTEBOOKS],
        )


@pytest.fixture(scope="session")
def html_exporter() -> HTMLExporter:
    """Shared HTML exporter used to render notebooks inside tests."""

    exporter = HTMLExporter()
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    return exporter


@pytest.fixture(scope="session")
def lesson_notebook_headings() -> dict[Path, str]:
    """Cache the primary Markdown heading for each lesson notebook."""

    headings: dict[Path, str] = {}
    for path in LESSON_NOTEBOOKS:
        notebook = nbformat.read(path, as_version=4)
        heading = _find_primary_heading(notebook.cells)
        headings[path] = heading
    return headings


def _find_primary_heading(cells: Iterable[nbformat.NotebookNode]) -> str:
    for cell in cells:
        if cell.get("cell_type") != "markdown":
            continue
        for line in cell.get("source", "").splitlines():
            if line.startswith("# "):
                return line.lstrip("# ").strip()
    raise AssertionError("Expected a level-1 Markdown heading in the lesson notebook.")


@pytest.fixture
def rendered_notebook_html(
    lesson_notebook_path: Path,
    html_exporter: HTMLExporter,
) -> tuple[str, str]:
    """Render the requested notebook path into HTML for downstream assertions."""

    notebook = nbformat.read(lesson_notebook_path, as_version=4)
    html, _ = html_exporter.from_notebook_node(notebook)
    return html, unescape(html)
