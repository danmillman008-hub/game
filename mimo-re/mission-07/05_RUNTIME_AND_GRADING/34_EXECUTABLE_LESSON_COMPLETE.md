# Mission 7 — Executable Lessons (complete)

## Payload (VERIFIED_STATIC)
```
LessonContent$Executable { instructions, preselectedFileIndex, files[] }
File { name, content, solvedContent, codeLanguage }
```
`solvedContent` ships with the lesson but is **not** used for local grading (no interpreter in the APK).

## Execution channels
| Channel | Evidence | Request | Response |
|---|---|---|---|
| REST | `POST /v1/code/runfiles` | `ExecuteFilesBody{files[]}` | `ExecuteFilesResponse{consoleOutput,error,hasPassed,hostedProjectUrl,tests[]}` |
| WebSocket | `pg.a` → `wss://api.mimo.org/v1/run/socket`, header `Sec-WebSocket-Protocol: authorization.bearer.<token>` | message schema NOT_RECOVERED | streamed frames |

## Field → consumer trace
| Field | Consumer | Label |
|---|---|---|
| `consoleOutput` | console panel of the executable lesson fragment | INFERRED_HIGH (fragment reads response; exact binding not decompiled) |
| `error` | error state / console | INFERRED_HIGH |
| `hasPassed` | verdict → same progress write path as interactive | VERIFIED_STATIC for the shape; mapping to `tries` INFERRED |
| `hostedProjectUrl` | open-in-browser affordance | INFERRED |
| `tests[]` | not rendered in recovered UI code | UNKNOWN (Q-41) |

## Saved code
`POST /v1/code`, `PATCH /v1/code/{id}`, `/v1/code/{id}/runfiles`, remix endpoints — the editor is a first-class
CRUD surface, not just a run button.

## Unresolved
Channel selection logic (`Q-39`), socket message schema (`Q-40`), test-result rendering (`Q-41`).
