# 12 — Delta register: recovered Mimo  →  `mimo/` engine

Machine-readable source: `data/spec_deltas.json` (this table is generated from it). Every row is a decision
about one of the 45 audited domains; every addition is a rule that does **not** exist in Mimo and must be
labelled as new in `mimo/DELTAS.md`.

**Counts:** KEEP 10 · KEEP_WITH_CHANGES 13 · ADD_RULE 1 · DROP 21 (total 45) — plus 8 additions.

## 12.1 Vocabulary

| Decision | Meaning for the engine |
|---|---|
| `KEEP` | reproduce the recovered behaviour as-is |
| `KEEP_WITH_CHANGES` | reproduce the shape, change the listed aspect; record it |
| `ADD_RULE` | Mimo delegates this to the server; the engine must define it locally |
| `DROP` | out of scope for the offline engine; do not reimplement |

## 12.2 Domain decisions

| Domain | Decision | Why | Source completeness | Evidence |
|---|---|---|---|---|
| `D-01` APK/packaging | **DROP** | packaging is Mimo-specific (13 dex, split modules) | COMPLETE | `mission-06/01_APK_AND_ARCHITECTURE` |
| `D-02` startup/DI | **KEEP_WITH_CHANGES** | single DI component is worth keeping; replace Hilt with plain construction for a small engine | COMPLETE | `mission-06/evidence/DI_GRAPH.json` |
| `D-03` content hierarchy | **KEEP** | content hierarchy (track/section/tutorial/chapter/lesson) is the engine's backbone | COMPLETE | `02_CONTENT_DELIVERY/CONTENT_MODEL_COMPLETE.json` |
| `D-04` dynamic modules | **DROP** | dynamic feature modules are stubs; deliver locales as directories | PARTIALLY_COMPLETE | `02_CONTENT_DELIVERY/DYNAMIC_MODULE_IMPLEMENTATION.md` |
| `D-05` DSL grammar | **KEEP** | DSL grammar is the content contract | COMPLETE | `mission-07/04_DSL_PARSER_RENDERER` |
| `D-06` parser | **KEEP** | keep the grammar; one generic parser suffices instead of seven | COMPLETE | `mission-07/04_DSL_PARSER_RENDERER` |
| `D-07` AST | **KEEP** | AST shape is reusable | COMPLETE | `mission-07/04_DSL_PARSER_RENDERER` |
| `D-08` rendering | **KEEP_WITH_CHANGES** | renderer contract reusable; replace the WebView plumbing with an embedded HTML host | SUBSTANTIALLY_COMPLETE | `mission-07/12_UI_RESOURCES/75` |
| `D-09` lesson runtime | **KEEP** | lesson lifecycle K/e0/U/V/W/X maps to open/store/next | COMPLETE | `03_LESSON_ENGINE` |
| `D-10` interactions | **KEEP** | nine interaction types | COMPLETE | `04_INTERACTION_ENGINE/SIX_MODULE_VARIANTS.json` |
| `D-11` grading | **KEEP** | grading predicates incl. the three-way verdict | COMPLETE | `04_INTERACTION_ENGINE/GRADING_IMPLEMENTATION.md` |
| `D-12` feedback/retry | **KEEP** | three feedback states plus visibility gating | COMPLETE | `04_INTERACTION_ENGINE/FEEDBACK_ENGINE_COMPLETE.md` |
| `D-13` executable lessons | **DROP** | executable lessons need a backend sandbox | SUBSTANTIALLY_COMPLETE | `mission-06/03_DSL_AND_RUNTIME/23` |
| `D-14` learner model | **KEEP_WITH_CHANGES** | keep entity shape; add user key, lifetime attempts and monotonic history | COMPLETE | `05_LEARNER_MODEL` |
| `D-15` progression | **ADD_RULE** | completion must become a local rule; Mimo delegates it to the server | COMPLETE | `05_LEARNER_MODEL/PROGRESSION_IMPLEMENTATION.md` |
| `D-16` gamification | **DROP** | coins/streaks are a server economy | COMPLETE | `mission-07/09_PROGRESS_GAMIFICATION` |
| `D-17` room/persistence | **KEEP_WITH_CHANGES** | Room design reusable; add a migration path | COMPLETE | `06_PERSISTENCE/ROOM_SCHEMA.json` |
| `D-18` sync/outbox | **KEEP_WITH_CHANGES** | outbox lifecycle reusable; add idempotency key and retry policy | COMPLETE | `05_LEARNER_MODEL/INQUEUE_IMPLEMENTATION.md` |
| `D-19` network stack | **DROP** | no network client is needed for the offline engine | COMPLETE | `07_NETWORKING/01_NETWORK_CLIENT_INVENTORY.md` |
| `D-20` endpoints | **DROP** | keep the catalogue only for optional sync | COMPLETE | `07_NETWORKING/02_ENDPOINT_CATALOG.json` |
| `D-21` AI tutor | **DROP** | AI tutor belongs to the tutor engine | SUBSTANTIALLY_COMPLETE | `mission-07/09_STREAMING/66` |
| `D-22` SSE | **DROP** | SSE belongs to the tutor engine | COMPLETE | `07_NETWORKING/08_SSE_AND_WEBSOCKET.md` |
| `D-23` execution socket | **DROP** | execution socket out of scope | PARTIALLY_COMPLETE | `07_NETWORKING/08_SSE_AND_WEBSOCKET.md` |
| `D-24` Pusher | **DROP** | Pusher out of scope | PARTIALLY_COMPLETE | `mission-07/09_STREAMING/71` |
| `D-25` push notifications | **DROP** | push notifications out of scope | PARTIALLY_COMPLETE | `mission-07/09_STREAMING/72` |
| `D-26` navigation | **KEEP_WITH_CHANGES** | navigation model reusable; routes rebuilt for new content | SUBSTANTIALLY_COMPLETE | `mission-07/12_UI_RESOURCES/73` |
| `D-27` screens | **KEEP_WITH_CHANGES** | screen catalogue informs the new UI surface | SUBSTANTIALLY_COMPLETE | `mission-07/12_UI_RESOURCES/74` |
| `D-28` resources | **DROP** | Mimo resources are content assets | COMPLETE | `mission-07/12_UI_RESOURCES/76` |
| `D-29` design system | **KEEP_WITH_CHANGES** | reuse token structure, not Mimo branding | COMPLETE | `mission-07/12_UI_RESOURCES/77` |
| `D-30` Rive | **DROP** | Rive animations are Mimo branding | SUBSTANTIALLY_COMPLETE | `mission-07/12_UI_RESOURCES/80` |
| `D-31` localization | **KEEP_WITH_CHANGES** | locale-pack pattern reusable; add explicit fallback | SUBSTANTIALLY_COMPLETE | `02_CONTENT_DELIVERY + mission-07/14` |
| `D-32` accessibility | **KEEP** | accessibility practices reusable | SUBSTANTIALLY_COMPLETE | `mission-07/12_UI_RESOURCES/81` |
| `D-33` analytics | **KEEP_WITH_CHANGES** | event taxonomy reusable; no Mimo sink | SUBSTANTIALLY_COMPLETE | `mission-07/10_ANALYTICS_CONFIG/82` |
| `D-34` remote config | **DROP** | Remote Config is Mimo infrastructure | SUBSTANTIALLY_COMPLETE | `mission-07/10_ANALYTICS_CONFIG/84` |
| `D-35` background jobs | **DROP** | WorkManager jobs are Mimo-specific | COMPLETE | `mission-07/10_ANALYTICS_CONFIG/86` |
| `D-36` subscriptions | **DROP** | subscriptions belong to the product shell | SUBSTANTIALLY_COMPLETE | `mission-07/13_SUBSCRIPTION/90-91` |
| `D-37` native | **DROP** | native libs are Mimo/SDK artefacts | SUBSTANTIALLY_COMPLETE | `mission-06/13_NATIVE_AND_SDKS` |
| `D-38` SDKs | **DROP** | third-party SDKs out of scope | COMPLETE | `mission-06/13_NATIVE_AND_SDKS/87` |
| `D-39` security posture | **KEEP_WITH_CHANGES** | informs but does not constrain the offline engine | COMPLETE | `mission-07/08_NETWORK + mission-06/14_SECURITY` |
| `D-40` offline/failure | **KEEP** | the offline boundary definition is essential | COMPLETE | `08_OFFLINE_CAPABILITY_MATRIX.csv` |
| `D-41` deep-links/URI-routing | **DROP** | deep links are product features | SUBSTANTIALLY_COMPLETE | `mission-06/09_NAVIGATION_AND_UI/63` |
| `D-42` Compose UI layer | **KEEP_WITH_CHANGES** | Compose patterns reusable | SUBSTANTIALLY_COMPLETE | `mission-07/12_UI_RESOURCES/75` |
| `D-43` auth token lifecycle | **DROP** | auth belongs to the app shell | COMPLETE | `05_AUTHENTICATION_CLOSURE + 07_NETWORKING/03` |
| `D-44` privacy/consent & tracking SDKs | **DROP** | consent is SDK-driven | PARTIALLY_COMPLETE | `mission-07/11_SDK_NATIVE + Q-134` |
| `D-45` crash/observability | **KEEP_WITH_CHANGES** | crash/observability useful, different sink | SUBSTANTIALLY_COMPLETE | `mission-07/10_ANALYTICS_CONFIG/87` |

## 12.3 Additions (new rules, absent in Mimo)

| id | Rule | Why it is needed | Origin |
|---|---|---|---|
| `ADD-01` | lesson/question binding | Mimo binds a question to a lesson position; the exam engine needs a question bank independent of lessons | `mimo-re/complete-extraction/17_BUILD_READY_SPEC/DATA_MODEL_TARGET.md` |
| `ADD-02` | concept graph + prerequisites | not present in Mimo | `same` |
| `ADD-03` | error taxonomy per option | distractor-level diagnosis; Mimo grades only correctness | `same` |
| `ADD-04` | local completion rule | Mimo completion is server-side (D-15) | `mimo-re/mission-08/05_LEARNER_MODEL/PROGRESSION_IMPLEMENTATION.md` |
| `ADD-05` | idempotent sync key | Mimo has no idempotency key | `mimo-re/mission-08/07_NETWORKING/07_ERROR_RETRY_OFFLINE.md` |
| `ADD-06` | schema migration policy | Mimo has zero migrations and an inferred destructive fallback | `mimo-re/mission-08/06_PERSISTENCE/ROOM_MIGRATION_AND_VERSIONING.md` |
| `ADD-07` | explicit locale fallback chain | Mimo fallback never observed (A12) | `mimo-re/mission-08/02_CONTENT_DELIVERY/CONTENT_CACHE_IMPLEMENTATION.md` |
| `ADD-08` | per-user data partitioning | Mimo tables have no account column (B-2) | `mimo-re/mission-08/06_PERSISTENCE/STORAGE_KEYS_SCHEMA.json` |

## 12.4 Reading the register

* Rows marked `PARTIALLY_COMPLETE` in the source column mean the *original behaviour* is only partly known — they are
  exactly the domains where an implementation choice is unavoidable. Cross-check `13_KNOWN_UNKNOWNS.md`.
* `DROP` does not mean "unknown"; it means "deliberately excluded". Do not spend time on it.
* The three rows that shape the engine most: `D-11` (grading, KEEP), `D-15`/`ADD-04` (completion, ADD_RULE),
  `D-14`/`ADD-08` (learner model per-user, KEEP_WITH_CHANGES).
* If your build changes any decision, add a row here **and** a matching entry in `mimo/DELTAS.md`; never silently
  diverge.

