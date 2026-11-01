# START HERE — everything an agent needs to rebuild Mimo's offline learning engine

You are holding a repository that contains a complete static reverse-engineering of the **Mimo 9.35** Android app
(`com.getmimo`, APK `sha256 48ce1740…`) plus this handoff package. **You do not need any chat history, any prior
conversation, or any external document.** Everything is here, and everything is traceable.

## Read in this order (≈ 45 minutes total; 10-minute path: `AGENT_BRIEF` → `01` → `04` → `10`)

| # | File | Why |
|---|---|---|
| 1 | `AGENT_BRIEF.md` | what you must build, what you must not invent, definition of done |
| 2 | `01_WHAT_MIMO_IS.md` | the app in one page: layers, data, flows, what is server-side |
| 3 | `02_SPEC_CONTENT_MODEL.md` | normative content shapes (track → tutorial → chapter → lesson) |
| 4 | `03_SPEC_LESSON_DSL.md` | normative lesson grammar (27 tags) + AST + renderer contract |
| 5 | `04_SPEC_INTERACTION_AND_GRADING.md` | the exact grading algorithm (copy it literally) |
| 6 | `05_SPEC_LEARNER_MODEL.md` | progress entity, counters, outbox, completion boundary |
| 7 | `06_SPEC_STORAGE.md` | database schema, DAOs, statements |
| 8 | `07_SPEC_API_AND_AUTH.md` | 62 endpoints, 6 clients, auth lifecycle (for the optional sync layer) |
| 9 | `08_SPEC_STREAMING_AND_TUTOR.md` | SSE + WebSocket (third engine, informational) |
| 10 | `09_SPEC_ANALYTICS_CONFIG_ENTITLEMENTS.md` | events, flags, entitlements (mostly not needed) |
| 11 | `10_BUILD_THE_MIMO_PROJECT.md` | **the build plan**: repo layout, modules, milestones M0–M6 |
| 12 | `11_ACCEPTANCE_TESTS.md` | executable acceptance criteria you must satisfy |
| 13 | `12_DELTA_REGISTER.md` | what to keep / change / add / drop, with IDs |
| 14 | `13_KNOWN_UNKNOWNS.md` | the honest inventory: 91 questions, 54 not fully closed, 2 global limitations |
| 15 | `14_TRACEABILITY.md` | every spec clause → the evidence artifact behind it |
| 16 | `15_GLOSSARY.md` | obfuscated identifiers (`hg.e`, `fh.a`, `te.c`, `qm.i`, …) decoded |

## Machine-readable data (`data/`)

| File | Contents |
|---|---|
| `content_schema.json` | JSON-Schema of the content model (packs, tracks, tutorials, versions) |
| `dsl_grammar.ebnf` | recovered EBNF grammar of the lesson DSL |
| `dsl_ast_schema.json` | AST node schema |
| `dsl_tags.json` | 29 enum tags + corpus frequencies over 20,306 documents / 1,034,686 tag occurrences |
| `grading_vectors.json` | source-derived grading vectors (must pass in your implementation) |
| `progress_vectors.json` | learner-model vectors (counters, queue, first-try) |
| `learner_model.json` | entity fields, keys, rules |
| `room_schema.json` | tables, columns, primary keys, DB version, identity hash |
| `endpoint_catalog.json` | 62 endpoints with client attribution, provenance, request/response types |
| `client_inventory.json` | 6 HTTP clients + interceptor chain + timeouts |
| `interaction_variants.json` | the six module variants and their grading guards |
| `questions_closure.json` | 91 questions with terminal statuses and evidence |
| `coverage_matrix.csv` | 45 domains with terminal status |
| `spec_deltas.json` | keep/change/add/drop per domain + 8 additions |
| `MANIFEST.json` | sha256 of every data file plus its source path |

## Executable material

| Path | What it is |
|---|---|
| `tools/verify_handoff.py` | **layer A** integrity gate: manifest hashes, resolvable evidence anchors, JSON validity, delta/question/tag counts, doc presence, secret scan. Stdlib only. |
| `tools/reference_engine.py` | clean-room reference implementation of the recovered rules (normaliser, verdicts, visibility, counters, outbox, `ADD-04`). Read it before you write your own. |
| `tests/test_grading_vectors.py`, `tests/test_progress_vectors.py` | **layer B** reference suite: 54 tests that reproduce `data/grading_vectors.json` and `data/progress_vectors.json` exactly |

## Verify the package before trusting it

```bash
cd <repo-root>
python3 HANDOFF/tools/verify_handoff.py            # 10/10 checks, stdlib only
python3 -m pytest -q HANDOFF/tests                 # 54 passed (needs pytest)
#   no pytest available?  python3 -m venv /tmp/venv && /tmp/venv/bin/pip -q install pytest
```

`verify_handoff.py` fails loudly if any data file drifts from its recorded sha256, if any traceability reference does not
resolve, if any count disagrees with the mission registers, or if a secret-shaped string appears. If you edit a data
file on purpose, re-pin it with `python3 HANDOFF/tools/verify_handoff.py --update-manifest` and say why in your commit.

## The one-paragraph version of Mimo, if you read nothing else

Mimo is a **content-in-the-APK** learning app: 19 tracks / 1,029 tutorials / 1,947 chapters / 18,272 lessons ship as JSON
and HTML-like documents inside `assets/lessons-<locale>` (10 locales, 10,317 documents, `publishSetVersion 753`). Lessons
are a custom HTML DSL (27 tags) parsed by seven parsers, rendered as custom elements, and graded **on the device**. The
device keeps three Room tables (`lesson_progress` as an upload outbox, plus two completion cache tables filled from the
server). Progression, completion, coins and streaks are **server-decided**; the client posts solved lessons to
`POST /v1/tutorials/{tutorialId}/progress` and then asks `GET /v1/tracks/{trackId}/completion` what is complete. Identity
is Firebase; the token is fetched per request and injected only into annotated Retrofit methods. The AI tutor is SSE and
code execution is a WebSocket, both authenticated differently from REST.

**What you are rebuilding is the offline learning engine** (content → parse → render → interact → grade → feedback →
local progress), with one deliberate change: completion must become a local rule, because Mimo's was the server's.
