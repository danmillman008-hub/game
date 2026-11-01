# 15 — Glossary

Identifiers are the **recovered obfuscated names**; they are kept so claims can be re-checked. They are meaningless to
read and that is the point.

## Domain terms

| Term | Meaning |
|---|---|
| **track** | top-level course grouping (e.g. "Python"); has `version` |
| **section** | ordered group of tutorials inside a track; carries `index` but rendering follows array order |
| **tutorial** | one content file (`tutorial-<id>.json`); has `version` |
| **chapter** | ordered group of lessons inside a tutorial |
| **lesson** | leaf unit; body is an HTML-like document in the DSL |
| **lesson document** | the lesson's body, written in the `<p>/<code>/<selection>` DSL |
| **interaction** | the part of a lesson the learner answers |
| **verdict** | `CORRECT` / `PARTIAL` / `INCORRECT` |
| **feedback state** | which blocks render after a verdict (`always` / `correct` / `wrong`) |
| **tries** | 0/1 solved flag, **not** a counter |
| **attempts** | submissions in the current session; not restored |
| **outbox / in_queue** | local flag marking a progress row awaiting upload |
| **publishSetVersion** | content baseline integer (753 shipped) |
| **locale pack** | `lessons-<locale>/` asset directory |
| **completion** | whether a chapter/tutorial is finished — in Mimo, **server-answered** |
| **delta** | a documented decision to keep/change/add/drop a recovered behaviour |

## Recovered identifiers

| Identifier | What it is |
|---|---|
| `te.a` … `te.g` | the seven lesson parsers |
| `te.c` | the dispatcher that chooses a parser |
| `qm.i.a` | the answer normaliser |
| `qm.f` | the ValidatedInput grader (only producer of PARTIAL) |
| `jm.m` / `jm.n` / `jm.o` | feedback states for CORRECT / PARTIAL / INCORRECT |
| `pm.b.E0` / `km.c.E0` | grader guards for MultipleChoice / SingleChoice |
| `cg/a` | lesson-progress DAO (4 statements) |
| `leg/e` | Room open-helper delegate (also hosts a WorkManager DB) |
| `hg.e` → `fh.b` → `fh.a` | interceptor chain (auth → logging → headers) |
| `ku.a.d` | scheduled runnable in the auth layer (not recovered) |
| `Lhg/b;` | an example Retrofit interface holding a network endpoint |
| `eh.a` | call on the long-timeout client (not recovered) |
| `gg.e` | streak sink (consumer not recovered) |
| `sk.a.r[2]` | dev-menu preference key (identity not recovered) |
| `ri.b` | annotation class whose endpoint set is not enumerable |
| `leg/e` DB version 24 | the *WorkManager* database, unrelated to `mimo.db` v2 |

## Numbers to trust

| Number | Value |
|---|---|
| lessons | 18,272 |
| tutorials / chapters / tracks | 1,029 / 1,947 / 19 |
| content documents | 10,317 JSON + 20,306 lesson documents |
| tag occurrences | 1,034,686 over 20,306 documents |
| endpoints / interfaces / clients / hosts | 62 / 29 / 6 / 5 |
| DB tables / migrations | 3 / 0 |
| Grading vectors | see `data/grading_vectors.json` |
| Questions tracked | 91 |
| Tests in the mission | 170 passed / 0 failed |
| Runtime-verified claims | **0** |

## Statuses in `13`

`CLOSED_STATIC`, `PARTIALLY_CLOSED`, `NOT_RECOVERED`, `BLOCKED_BY_ENVIRONMENT`, `GENUINELY_UNKNOWN`, `BACKEND_ONLY`,
`OUT_OF_SCOPE` — see `13` §13.2 for the count and meaning of each.
