# 16 — Consolidated evidence register

23 records, machine-readable in `16_CONSOLIDATED_EVIDENCE_REGISTER.json`. Schema (16 fields):
`evidence_id, domain, apk_sha256, original_class, recovered_class, method, dex_location, decompiled_source,
call_chain, claim, evidence_type, confidence, related_open_question, related_correction, verification_status,
artifact_ref`.

Every `artifact_ref` resolves to a file that exists in this repository (validated by
`tests/test_final_closure.py::test_evidence_refs_resolve`).

## Records

| ID | Domain | Claim | Status | Ref |
|---|---|---|---|---|
| E-C01 | content | `tracks.json` carries `publishSetVersion` + track list; 753 shipped | VERIFIED_STATIC | `mission-06/evidence/CONTENT_MODEL_FIELDS.json` |
| E-C02 | content | content is read from APK assets across 10 locale packs | VERIFIED_STATIC | `02_CONTENT_DELIVERY/CONTENT_SOURCE_MATRIX.csv` |
| E-C03 | content | seven parsers share one tag grammar; `NUMBER` unparsed | VERIFIED_STATIC | `mission-07/04_DSL_PARSER_RENDERER` |
| E-L01 | lesson | `e0` stores progress; `U` emits next lesson | VERIFIED_STATIC | `03_LESSON_ENGINE` |
| E-L02 | grading | normaliser keeps `< > ( ) : { } , .` and drops the rest | VERIFIED_STATIC | `04_INTERACTION_ENGINE/PROPERTY_NAME_RECOVERY.md` |
| E-L03 | grading | six `E0` guards; only validated input has partial | VERIFIED_STATIC | `04_INTERACTION_ENGINE/GRADING_IMPLEMENTATION.md` |
| E-L04 | feedback | three feedback states; WRONG only observes `jm.o` | VERIFIED_STATIC | `04_INTERACTION_ENGINE/FEEDBACK_ENGINE_COMPLETE.md` |
| E-P01 | learner | 11-field row; `tries` flag, `attempts` session | VERIFIED_STATIC | `05_LEARNER_MODEL/LESSON_PROGRESS_FIELD_MAP.json` |
| E-P02 | learner | store = upsert + counters + streak sink | VERIFIED_STATIC | `05_LEARNER_MODEL/PROGRESS_REPOSITORY_IMPLEMENTATION.md` |
| E-P03 | sync | outbox flush: select-all → group → POST → delete-by-ids | VERIFIED_STATIC | same |
| E-P04 | completion | completion rows come from the server response | VERIFIED_STATIC | `05_LEARNER_MODEL/COMPLETION_REPOSITORY_IMPLEMENTATION.md` |
| E-D01 | persistence | three tables, three DAOs, empty auto-migration set | VERIFIED_STATIC | `06_PERSISTENCE/ROOM_SCHEMA.json` |
| E-D02 | persistence | schema v2 + identity hash | VERIFIED_STATIC | `06_PERSISTENCE/ROOM_MIGRATION_AND_VERSIONING.md` |
| E-A01 | auth | token provider lifecycle (`exp` + one refresh) | VERIFIED_STATIC | `evidence/DEX_ku.a_access_token_provider.json` |
| E-A02 | auth | annotation-conditional Bearer; never forces | VERIFIED_STATIC | `05_AUTHENTICATION_CLOSURE/evidence/…` |
| E-A03 | auth | offline gate throws `java.io.IOException` | VERIFIED_STATIC | same |
| E-N01 | network | interceptor order + timeouts + retry flag | VERIFIED_STATIC | `mission-06/evidence/DI_GRAPH.json` |
| E-N02 | network | host switch by dev-menu preference | VERIFIED_STATIC | same |
| E-N03 | network | 62 endpoints / 29 interfaces | VERIFIED_STATIC | `mission-05/evidence/API_CATALOG_V2.csv` |
| E-N04 | network | dedicated clients + tutor repo + socket wrapper | VERIFIED_STATIC | `mission-06/evidence/DI_GRAPH.json` |
| E-X01 | AI | SSE frames + manual Bearer | VERIFIED_STATIC | `mission-07/09_STREAMING/69` |
| E-X02 | execution | socket handshake proven, frame schema not | **BLOCKED** | `mission-07/09_STREAMING/70` |
| E-G01 | analytics | 14 events bound to emitters | VERIFIED_STATIC | `mission-07/evidence/ANALYTICS_DISPATCH.json` |

## Claim-to-evidence rule

Every material statement in documents `02`–`12` maps to at least one of these records or to a named artifact inside
the referenced mission directory. Statements that cannot be mapped are not present in those documents; where a topic is
unmapped, it appears in `14` as an open question instead.
