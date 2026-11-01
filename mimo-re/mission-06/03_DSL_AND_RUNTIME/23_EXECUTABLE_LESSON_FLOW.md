# Mission 6 — Executable Lesson Flow

## Scope
The second lesson engine: code tasks. Payload, transports, verdict source, and the two execution
channels found.

## Method
Field extraction over the executable payload classes; API catalogue review; read of the WebSocket
listener `pg.a`; search of the DEX string pool for socket/route literals.

## Sources
`evidence/CONTENT_MODEL_FIELDS.json`, `evidence/DTO_FIELDS.json`, `pg.a.java`, `evidence/API_CATALOG_V2.csv`.

## Findings — payload (VERIFIED_STATIC)
`LessonContentType = {INTERACTIVE, EXECUTABLE_FILES}`.

```
LessonContent$Executable { instructions: String, preselectedFileIndex: int, files: [File] }
File { name: String, content: String, solvedContent: String, codeLanguage: CodeLanguage }
```
`solvedContent` means the **solution ships with the lesson**; the verdict nevertheless comes from the
server, because the client has no interpreter (no libpython/node/quickjs was found).

## Findings — two execution channels (VERIFIED_STATIC)
| Channel | Evidence | Shape |
|---|---|---|
| REST | `POST /v1/code/runfiles` → `ExecuteFilesResponse{consoleOutput, error, hasPassed, hostedProjectUrl, tests[]}` | request `ExecuteFilesBody{files[]}` |
| WebSocket | `pg.a` connects `wss://api.mimo.org/v1/run/socket` with header `Sec-WebSocket-Protocol: authorization.bearer.<token>` | `okhttp3.WebSocketListener`, `onMessage` streaming |

`hostedProjectUrl` + `Error` + `Tests[]` show that some tasks are *hosted projects* and that grading can
be test-based (`tests`) rather than output-based. `ReportLessonBody{interactionType, reportOption,
reportText, tutorialVersion}` exists for content/problem reporting.

## Findings — flow
```
open executable lesson → render files + instructions (preselectedFileIndex)
edit → run → (REST runfiles | WSS run socket) → streamed console output
verdict → ExecuteFilesResponse.hasPassed / tests → same progress write path as interactive lessons
save    → /v1/code/{savedCodeId} (PATCH), /v1/code (POST), /v1/code/{savedCodeId}/runfiles, remixes
```

## Evidence labels
Payload, both channels, verdict source: **VERIFIED_STATIC**. Which channel is used *when* is
**UNDEFINED** by the recovered code paths (`Q-39`).

## Limitations
No websocket message schema was recovered (`Q-40`); the socket listener's message bodies are parsed
elsewhere (not recovered).

## Open questions
`Q-39` channel selection; `Q-40` socket message schema; `Q-41` whether `tests[]` is shown to learners.

## Reproduction
```bash
grep -n 'wss://' /tmp/dad/pg.a.java
grep -n 'code/runfiles' mimo-re/mission-05/evidence/API_CATALOG_V2.csv
```
