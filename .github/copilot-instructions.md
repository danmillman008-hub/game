# Copilot instructions

Canonical instructions: **[`AGENTS.md`](../AGENTS.md)** — read it before editing.
Entry point: [`README.md`](../README.md). Full handoff: [`docs/00_START_HERE.md`](../docs/00_START_HERE.md)
through `docs/09_COMMIT_LOG.md`. Machine-readable map: [`REPO_INDEX.json`](../REPO_INDEX.json).

Hard rules: work only on `arena/aebb90b7-game`; `SERVER CONFIRMED=0`; no LLM,
network, API key or generated text; `app/content/source/` stays out of Git;
byte-protected approved assets and all historical evidence stay untouched;
`app/dist/` is generated — do not hand-edit. Answer the user in Persian.

Before finishing: `npm test --prefix app`, `npm run verify --prefix app`,
content validator, and `python3 docs/verify_docs.py`.
