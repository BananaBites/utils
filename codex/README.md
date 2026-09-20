# codex-usage

Shows Codex (ChatGPT plan) rate-limit usage — the same numbers as `/status` in
the Codex TUI. Works without the `codex` binary installed.

    ./codex-usage          # human-readable bars
    ./codex-usage --json   # normalized JSON (used by the dashboard)

Credentials are read from whichever login exists:

- pi: `~/.pi/agent/auth.json` → `"openai-codex"` (OAuth), or
- Codex CLI: `~/.codex/auth.json` → `tokens.access_token`.

For pi credentials the account id is read from the access-token JWT claim
(`https://api.openai.com/auth` → `chatgpt_account_id`), exactly like pi does.

Overrides: `PI_AUTH`, `CODEX_AUTH` (paths) and `CODEX_BASE_URL` (default
`https://chatgpt.com/backend-api`).

How it works: `GET {base}/wham/usage` with `Authorization: Bearer <access>`,
`ChatGPT-Account-ID: <account>` and `originator: pi` (or `codex_cli_rs`). The
response has a primary and secondary rate-limit window (`used_percent`,
`limit_window_seconds`, `reset_after_seconds`) plus optional credits.

The script does not refresh tokens (refresh-token rotation could break your
stored login). If you get HTTP 401, the access token has expired — open pi or
Codex once so it refreshes.