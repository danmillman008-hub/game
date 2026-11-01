# 14 — Traceability: every claim → data → evidence

Purpose: an auditor (human or agent) can walk from any sentence in this package to the file that proves it, and from
there to the original mission artifact.

## 14.1 The chain

```text
APK (sha256 48ce1740…f0f7c7a)
  → decompiled bytecode + extracted assets
    → mission-04/05/06/07/08 analysis artifacts (unchanged, frozen)
      → HANDOFF/data/*.json / *.ebnf / *.csv      (hash-pinned copies, see data/MANIFEST.json)
        → HANDOFF/0X_*.md                          (normative specs, cite the data file)
          → mimo/                                  (the build, cites the delta ids)
```

Each `HANDOFF/data/MANIFEST.json` entry carries `sha256`, `bytes` and `source_path`, so a copy can be re-derived and
compared. `tools/verify_handoff.py` re-checks all of it.

## 14.2 Spec document → data → mission evidence

| Doc | Primary data | Mission evidence |
|---|---|---|
| `01_WHAT_MIMO_IS.md` | all | `mission-08/16_FINAL_AUDIT/03_MISSION08_METRICS.json` |
| `02_SPEC_CONTENT_MODEL.md` | `content_schema.json` | `mission-06/evidence/CONTENT_MODEL_FIELDS.json`, `mission-08/02_CONTENT_DELIVERY/` |
| `03_SPEC_LESSON_DSL.md` | `dsl_grammar.ebnf`, `dsl_ast_schema.json`, `dsl_tags.json` | `complete-extraction/05_LESSON_DSL/`, `mission-07/04_DSL_PARSER_RENDERER/` |
| `04_SPEC_INTERACTION_AND_GRADING.md` | `grading_vectors.json`, `interaction_variants.json` | `mission-08/04_INTERACTION_ENGINE/`, `mission-05/evidence/TAG_ENUM.json` |
| `05_SPEC_LEARNER_MODEL.md` | `learner_model.json`, `progress_vectors.json` | `mission-08/05_LEARNER_MODEL/{LESSON_PROGRESS_FIELD_MAP,PROGRESS_TEST_VECTORS}.json`, `PROGRESSION_IMPLEMENTATION.md` |
| `06_SPEC_STORAGE.md` | `room_schema.json` | `mission-08/06_PERSISTENCE/{ROOM_SCHEMA,STORAGE_KEYS_SCHEMA}.json`, `ROOM_MIGRATION_AND_VERSIONING.md` |
| `07_SPEC_API_AND_AUTH.md` | `endpoint_catalog.json`, `client_inventory.json` | `mission-07/{04_DSL_PARSER_RENDERER,09_STREAMING}`, `mission-08/07_NETWORKING/`, `mission-05/evidence/API_CATALOG_V2.csv` |
| `08_SPEC_STREAMING_AND_TUTOR.md` | — (partial) | `mission-07/09_STREAMING/{69,70,71}`, `mission-08/07_NETWORKING/` |
| `09_SPEC_ANALYTICS_CONFIG_ENTITLEMENTS.md` | — | `mission-07/{10_ANALYTICS_CONFIG,12_UI_RESOURCES,13_SUBSCRIPTION}`, `mission-07/evidence/{ANALYTICS_DISPATCH.json,EVENTS_WITH_CALLSITES.csv}` |
| `12_DELTA_REGISTER.md` | `spec_deltas.json` | `mission-08/00_BASELINE/CANONICAL_DOMAIN_REGISTER.json` |
| `13_KNOWN_UNKNOWNS.md` | `questions_closure.json` | `mission-08/00_BASELINE/CANONICAL_OPEN_QUESTION_REGISTER.json`, `99_FINAL_CLOSURE/` |

## 14.3 Confidence vocabulary (use it in `mimo/` too)

| Label | Means |
|---|---|
| `VERIFIED_STATIC` | read from bytecode/assets; the only kind of "verified" in this project |
| `VERIFIED_RUNTIME` | observed while running — **count: 0**, never claimed |
| `INFERRED` | conclusion from structure, not read directly |
| `INFERRED_HIGH` | strong structural inference (e.g. inherited auth annotation) |
| `GENUINELY_UNKNOWN` | no evidence in the artifact |
| `BACKEND_ONLY` | decided outside the client |
| `BLOCKED_BY_ENVIRONMENT` | needs artifacts/tooling no longer available |

## 14.4 What a `mimo/` builder must cite

For every non-obvious behaviour in your build, cite one of:

1. a delta id from `12` (`D-xx` / `ADD-xx`),
2. a vector id from `data/grading_vectors.json` / `data/progress_vectors.json`,
3. an acceptance id from `11`.

If a behaviour has none of these, it is a decision → put it in `mimo/OPEN_QUESTIONS.md` with today's date.

## 14.5 Auditing this package in five minutes

```bash
python3 HANDOFF/tools/verify_handoff.py        # expected: 10/10 checks passed
python3 -m pytest -q HANDOFF/tests             # expected: 54 passed
grep -rn "VERIFIED_RUNTIME" HANDOFF/*.md       # expected: the definition row in 14 + this audit block, nothing else
grep -rn "TBD\|TODO\|FIXME" HANDOFF/*.md       # expected: this audit block only
```

(The grep lines match themselves and the vocabulary definitions by design — what matters is that no *claim* carries
the `VERIFIED_RUNTIME` label. The status enum in `data/questions_closure.json` also lists the word; that is a
vocabulary, not a claim.)

## 14.6 Immutability note

`mission-04` … `mission-07` and `complete-extraction/` are frozen. Everything new lives in `mission-08/` and
`HANDOFF/`. Corrections follow the mission rule: original record kept, a new record added, old and new evidence cited,
technical reason stated (`C-01…C-24` are the precedent).
