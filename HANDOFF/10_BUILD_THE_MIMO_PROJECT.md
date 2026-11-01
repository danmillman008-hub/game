# 10 — BUILD GUIDE: the `mimo/` offline learning engine

This is the instruction set for building the **second** project. It is independent of the recovered app: no Android, no
server, no Mimo branding, no Mimo assets. It reproduces Mimo's *learning behaviour* — content model, DSL, interactions,
grading, feedback, progress — with server-derived completion replaced by a local rule.

## 0. Definition of the deliverable

```text
mimo/
├── README.md                  what this is, how to run, what it diverges from
├── DELTAS.md                  every deliberate difference, with a delta id (from HANDOFF/12)
├── OPEN_QUESTIONS.md          every DECIDED_IN_MIMO_BUILD choice, dated
├── content/                   YOUR OWN synthetic/practice content (never Mimo content)
│   └── lessons-en/tracks/{tracks.json,tutorial-<id>.json}
├── src/
│   ├── model/                 Track, Section, Tutorial, Chapter, Lesson, ids
│   ├── dsl/                   tokenizer, parser, AST, validator
│   ├── interact/              interaction types, answer capture
│   ├── grade/                 normaliser, verdicts, feedback states
│   ├── learn/                 learner model, progress store, completion rule
│   ├── persist/               SQLite schema + DAOs + migrations
│   └── ui/                    your renderer/adapter of choice
└── tests/                     must reproduce HANDOFF/data/{grading,progress}_vectors.json
```

## 1. Non-negotiable engineering rules

1. **Copy behaviour, not code or content.** No decompiled source, no Mimo assets, no Mimo lesson text. Synthetic
   fixtures only (Rule 6).
2. **Every delta is labelled.** Behaviour that differs from `HANDOFF/data/spec_deltas.json` must appear in
   `mimo/DELTAS.md` with the delta id (`D-xx`, `ADD-xx`) and a one-line reason.
3. **Vectors are law.** If your code and `grading_vectors.json` disagree, the code is wrong.
4. **No silent completeness.** Anything unimplemented stays in `OPEN_QUESTIONS.md`.
5. **No auth/entitlement emulation.** Out of scope by design (`09`).

## 2. Milestones

### M0 — skeleton and content loading (half a day)
* project scaffold; `content/lessons-en/tracks/tracks.json` with 1 track / 1 section / 1 tutorial / 1 chapter / 3 lessons;
* model classes exactly as `02` §4; `LessonIdentifier` 5-long struct for navigation only;
* loader reads the pack, exposes `Track → Section → Tutorial → Chapter → Lesson`.
* **Gate:** a test prints the tree of the synthetic pack and asserts counts; no parsing of lesson bodies yet.

### M1 — DSL parser (1–2 days)
* tokenizer + parser for the block inventory in `03` §2 and the interaction grammar in `03` §3;
* AST validated against `data/dsl_ast_schema.json`;
* unknown-tag policy implemented and documented (recommended: ignore + warning list).
* **Gate:** every document in `content/` parses; the 29-tag enum table matches `data/dsl_tags.json` for the tags you
  support; malformed input produces typed errors, never exceptions escaping the parser.

### M2 — rendering adapter (1–2 days)
* map AST → your UI blocks; implement `visible-if` gating against a supplied verdict;
* implement the answer-slot highlight for interaction ranges (`startIndex`/`endIndex`);
* inline formatting, code tokens with `class`, tables, `<output>`.
* **Gate:** a golden-render test per block kind (text snapshot), and a gating test showing `always|correct|wrong`.

### M3 — interaction + grading (1–2 days) — the heart
* implement the nine types (`04` §1), the normaliser byte-for-byte (`04` §2), the verdicts (`04` §3–4), the feedback
  states (`04` §5);
* implement the counters (`04` §6) exactly, including "`tries` is a flag".
* **Gate:** keep the `tries >= 1` semantics and note the divergence.
* **Gate:** 100% of `grading_vectors.json` pass, including the PARTIAL-vs-CORRECT raw-equality trap.

### M4 — learner model + persistence (1–2 days)
* schema from `06` §2 verbatim (same columns, same composite PKs), plus your `ADD-06` migration table and `ADD-08`
  user column;
* outbox lifecycle (`store/move/post/clear`) with `ADD-05` idempotency key for the optional sync adapter;
* **local completion rule** (`ADD-04`): chapter complete ⟺ all lessons have `tries >= 1`; tutorial likewise.
* **Gate:** all of `progress_vectors.json` passes; schema test compares `PRAGMA table_info` against `06` §2.

### M5 — lesson runtime / session loop (1 day)
* open → submit → verdict → feedback → next; `attempts` increments per submission and is **not** reloaded from disk
  unless you deliberately change it (then log the change);
* duration from `completed_at − started_at`; ordering guard logs, never blocks.
* **Gate:** end-to-end scripted session over the synthetic pack producing the expected completion states.

### M6 — audit, docs, honesty pass (half a day)
* `DELTAS.md` enumerates D-01…D-45 and ADD-01…ADD-08 with keep/change/drop status;
* `OPEN_QUESTIONS.md` lists every choice you made where Mimo's behaviour was unknown (`13`);
* run `python3 HANDOFF/tools/verify_handoff.py` — it must stay green after your changes;
* smoke: fresh checkout → load content → play one lesson → see progress persisted.

## 3. What to copy (and what not to)

| Copy | Do not copy |
|---|---|
| the 11-field progress entity and its PK | the seven-parser architecture — one generic parser is enough |
| the normaliser + three-way verdict | `tries` as a boolean + `attempts` as session-only, **unless** you keep it deliberately |
| feedback states and `visible-if` gating | the outbox's delete-after-upload (loses history) |
| the three-table shape | Mimo's Android/Room/Firebase/Retrofit stack |
| the DSL block inventory | Mimo's assets, lesson text, images, branding |
| the interaction grammar | server-driven completion, coins, certificates, tutor, code execution |

## 4. Recommended conventions

* **Types:** `long` ids, `Instant` timestamps (UTC), `enum Verdict { CORRECT, PARTIAL, INCORRECT }`.
* **Errors:** typed results (`ParseError`, `GradeError`, `StoreError`) — no stringly-typed failures.
* **Tests:** one test file per milestone gate; fixtures in `tests/fixtures/`.
* **Determinism:** inject a clock (`Clock` interface) so `startedAt/completedAt` are testable.

## 5. Time budget

Roughly 6–10 focused days for one engineer, M3 being the risky part. If you must cut, cut M5's niceties and M6's UI —
never M3 or M4.

## 6. Traps that cost real time

1. PARTIAL only exists for `validatedInput`; everything else is binary.
2. Multi-select is all-or-nothing.
3. `tries` is not a counter (repeated submission does not monotonically increase it in Mimo; it settles at 1).
4. Normalisation keeps only `< > ( ) : { } , .` as punctuation — dropping or adding one changes results.
5. `Locale.US` lowercasing, not the device default.
6. `in_queue = 0` after `move` means a naive retry query misses rows — decide the retry story explicitly.
7. A local completion rule is a **new** rule; state it in `DELTAS.md` or you have invented undocumented behaviour.
