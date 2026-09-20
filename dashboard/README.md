# Dashboard

A tiny localhost dashboard. No dependencies beyond Python's standard library.

    python3 dashboard/server.py          # http://127.0.0.1:8787
    python3 dashboard/server.py -p 9000  # other port

Open the page: every widget runs once on load. Click `↻` on a card, or
`Refresh all` (or press `r`), to fetch fresh values.

## Adding a widget

Append an entry to `widgets.json` — no code changes needed:

    {
      "name": "unique-id",
      "title": "Card title",
      "command": "some-cli --flag",
      "timeout": 30,
      "cwd": "/optional/working/dir"
    }

`timeout` and `cwd` are optional. The command runs through the shell; stdout
and stderr are shown together. A non-zero exit turns the card red.

## Renderers

By default a widget's output is shown as plain text. Add `"render": "<name>"`
to draw it differently. Built-in renderers:

- `text` (default) — the raw output in a `<pre>`.
- `credits` — expects JSON like `{credits, used, remaining, today}`, shown as
  a progress bar. Used by OpenRouter; see `../openrouter/openrouter --json`.
- `bars` — expects `{plan, windows:[{label, used_percent, resets_in}]}` and draws
  one progress bar per window. Used by Codex; see `../codex/codex-usage --json`.

The server binds `127.0.0.1` only, but it runs commands you put in the config,
so don't expose the port.