# AGENTS.md

## Code style (strict)

- Keep code minimal and easy to grasp: if a handful of lines will do, write a handful of lines.
- No abstractions, helper functions, or error handling unless actually needed.
- No speculative features. Solve the task at hand, nothing more.
- A reader should understand the whole file in under a minute.

## Tooling preference

- Shell first. Reach for Python only when shell is insufficient or too complicated.

## Layout

- One folder per tool/topic, holding all its scripts and configs (e.g. `pi/`, `tmux/`).
- Top level is for repo-wide files only.
- Adding a tool = adding a folder. Never create type-based folders (scripts/, configs/).
