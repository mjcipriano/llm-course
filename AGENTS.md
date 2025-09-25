# AGENT PLAYBOOK

## Audience & Voice
- The course is for advanced kids (roughly ages 11–15) who are curious and motivated.
- Assume they are smart and ready to stretch—never talk down, use a respectful, enthusiastic tone.
- Introduce new technical vocabulary explicitly, pairing it with plain-language explanations and quick reminders of prior knowledge.
- Favor concrete examples, metaphors, and short practice prompts so learners can connect concepts to what they already know.

## Lesson & Notebook Structure
- Each notebook should open with a **Lesson Overview** section that states the learning goals and a short roadmap.
- Organize content in small loops: concept explanation → worked example → learner challenge or reflection.
- Keep related Markdown and code cells grouped; avoid mixing multiple unrelated ideas in one long cell.
- Use headings (`#`, `##`, `###`) consistently so navigation panes in Jupyter make sense.
- When adding TODOs or fill-in prompts, use bold text and a short instruction paragraph rather than inline ellipses.

## Notebook Code Style
- Write executable Python 3.11 code cells—do **not** wrap code in Markdown fences inside code cells.
- Prefer clear variable names and inline comments that explain *why* a step exists, not just what it does.
- Show minimal but meaningful printouts; long outputs should be summarized or truncated.
- Keep imports at the top of the first relevant code cell in each section; avoid repeated imports unless required for clarity.
- When demonstrating error handling, run the code that produces the error, then follow with the corrected version.

## Dependency Management
- Manage Python dependencies with `uv`. To add packages, run `uv add <package>` (or `!uv add ...` inside a notebook shell cell).
- Do **not** use `uv pip install` or `pip install`; stick with `uv add`/`uv remove` so `pyproject.toml` stays authoritative.

## Writing & Editing Guidance for Agents
- Favor incremental edits that preserve existing narrative momentum—avoid wholesale rewrites unless requested.
- Double-check that code cells execute in order without hidden state; restart-and-run should work.
- Include brief definitions for new jargon at first introduction, and cross-link to earlier lessons when helpful.
- Proofread Markdown for typos, consistent punctuation, and accessible formatting (lists, tables, callouts when appropriate).
- 