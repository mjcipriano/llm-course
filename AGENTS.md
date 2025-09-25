# Repository Guidelines

- **Always run the full test suite (`uv run pytest`) before completing any task.** If your changes require new tests, add or update them so they cover the new behavior.
- **Use the `uv` tool for Python package management and commands.** Prefer `uv pip install` and `uv run <command>` instead of calling `pip` or Python directly.
- **Notebook formatting matters.** When editing notebooks in `notebooks/`, keep code cells stored as JSON arrays of strings (one line per element, ending with `\n`) consistent with the other lessons.
- Keep the project documentation and dependencies in sync with your changes.
- Follow standard Python formatting and linting expectations used throughout the repository.
