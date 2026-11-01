# Spec 114 — Executable Lessons

## MUST
1. Payload `{instructions, preselectedFileIndex, files[{name, content, solvedContent, codeLanguage}]}`.
2. Run via `POST /v1/code/runfiles` or the run WebSocket; render `consoleOutput`, `error`, and honour
   `hasPassed`; surface `hostedProjectUrl` when present.
3. Treat grading as server-executed (no local interpreter ships).
4. Saved code: create (`POST /v1/code`), update (`PATCH /v1/code/{id}`), run (`…/runfiles`), remix.

## MUST NOT
- Implement local code execution.
- Assume the socket message schema (NOT_RECOVERED).

## GIVEN EVIDENCE
`03_DSL_AND_RUNTIME/23`, `50_REQUEST_RESPONSE_SCHEMAS/ExecuteFiles*.json`.
