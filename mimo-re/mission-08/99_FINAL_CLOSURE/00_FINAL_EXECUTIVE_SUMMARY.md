# 00 — Final executive summary

**Target:** Mimo for Android 9.35 · `sha256 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
**Branch:** `arena/ecb8af07-game` · **Inputs:** missions 04–08 (Stages A–E, 1–7)
**Terminal status of this mission: `CLOSED_WITH_DECLARED_LIMITATIONS`.**

This is the terminal dossier. It is not a progress report and there is no successor stage.

## What was achieved

| Area | Result |
|---|---|
| Application architecture | one Hilt/Dagger component (127 provider cases), Activity → Compose UI → ViewModel → use case → repository → Room / network |
| Content system | **19 tracks, 1,029 tutorials, 1,947 chapters, 18,272 lessons**, 10 locale packs, 10,317 JSON documents, `publishSetVersion 753`, delivered **from APK assets** |
| Lesson engine | HTML custom elements (not Markdown), **7 parsers** (`te.a`–`te.g`), **6 module variants**, dispatcher `te.c` |
| Interaction/grading | **9 UI interaction types**, client-side grading, normaliser `qm.i.a`, three-way verdict for validated input, 3 feedback states, `ModuleVisibility {ALWAYS, CORRECT, WRONG}` |
| Learner model | `tries` is a 0/1 flag, `attempts` is session-local, key `(lesson_id, tutorial_id)`, outbox via `in_queue` |
| Persistence | one database `mimo.db` (schema **v2**, identity hash `2b8ab6d3…`), 3 tables, 3 DAOs, **0 migrations**, no encryption |
| Networking | **6 client objects**, proven interceptor chain `hg.e → fh.b → fh.a`, **62 endpoints / 29 interfaces / 5 hosts** |
| Authentication | FirebaseAuth identity, `ku.a.d(boolean)` token provider with `exp` check + one forced refresh, annotation-conditional Bearer |
| AI tutor / execution | SSE with `finishReason {Stop, Length}`, one WebSocket with bearer **subprotocol**, Pusher via SDK |
| Analytics | 14 verified events, dispatcher `analytics.a` → Firebase/Adjust/Customer.io |
| Class coverage | 29,454 class definitions inventoried; 3,133 app-named; 1,148 renamed app classes; 637 methods with status records; 85,724 typed call edges over 138,025 call sites |
| Questions | **91 closed** (canonical 39 + mission-8 A 28 + Stage-7 A 10 + B 13 + Q-76) with terminal statuses |
| Semantic tests | **170 passed, 0 failed** (missions 5–7 + Stages 4–7 + this package) |
| Runtime | **0 runtime claims** — no device/emulator; every claim is static or explicitly labelled |

## What is *not* claimed

`VERIFIED_RUNTIME` count is **zero**. The APK and the 12 DEX files are absent from this environment and cannot be
re-acquired (only `github.com`, `api.github.com`, `pypi.org`, `registry.npmjs.org` are reachable; `apkpure`, `ghproxy`
and even `raw.githubusercontent.com` return 000). Everything here is re-derived from committed evidence produced while
the artifact was present, and the claims that would need a fresh read are marked `BLOCKED_BY_ENVIRONMENT` (8 questions).

## The five findings that matter most

1. **Content is local, progression is not.** Lessons, chapters and tutorials come from `assets/lessons-<locale>`; only
   completion, ETA, coins, keys, rewards, leaderboards, tutor and execution need the network.
2. **The client never computes completion.** It posts progress, then asks the server what is complete. Any rebuild of
   the engine must own that rule itself.
3. **`tries`/`attempts` are not a history.** `tries` is a solved flag; `attempts` resets with the view-model. Lifetime
   statistics do not exist locally.
4. **One outbox, two triggers, batch acknowledgement.** `in_queue` marks pending rows; chapter end and app start flush
   them; a 2xx deletes the posted ids. There is no retry policy, no backoff and no idempotency key.
5. **Auth is annotation-driven and triple-channelled.** REST uses the interceptor, SSE a manual header, the socket a
   subprotocol — one token provider (`ku.a`) behind all three.

## Where each claim lives (evidence anchors)

| Area | Document | Machine-readable |
|---|---|---|
| baseline and artifact identity | `01_TARGET_AND_REPOSITORY_BASELINE.md` | `00_BASELINE_FACTS.json` |
| architecture, DI | `02_COMPLETE_APPLICATION_ARCHITECTURE.md` | `mission-06/evidence/DI_GRAPH.json` |
| coverage / class dispositions | `03_CLASS_AND_METHOD_COVERAGE.md` | `03_CLASS_DISPOSITION.csv` |
| content | `04_CONTENT_AND_TRACK_DELIVERY.md` | `mission-08/02_CONTENT_DELIVERY/CONTENT_MODEL_COMPLETE.json` |
| lesson engine, grading | `05`, `06` | `mission-08/04_INTERACTION_ENGINE/SIX_MODULE_VARIANTS.json` |
| learner model, completion | `07` | `mission-08/05_LEARNER_MODEL/LESSON_PROGRESS_FIELD_MAP.json` |
| persistence, offline | `08` | `08_OFFLINE_CAPABILITY_MATRIX.csv`, `06_PERSISTENCE/ROOM_SCHEMA.json` |
| auth | `09` | `mission-08/05_AUTHENTICATION_CLOSURE/evidence/DEX_ku.a_access_token_provider.json` |
| network | `10` | `mission-08/07_NETWORKING/02_ENDPOINT_CATALOG.json` |
| tutor / execution | `11` | `mission-07/09_STREAMING/69`, `70` |
| analytics, entitlements | `12` | `mission-07/evidence/ANALYTICS_DISPATCH.json` |
| questions | `14` | `14_ALL_OPEN_QUESTIONS_CLOSURE.json` |
| coverage matrix | `15` | `15_FINAL_COVERAGE_MATRIX.csv` |
| evidence | `16` | `16_CONSOLIDATED_EVIDENCE_REGISTER.json` |

## Reusability for an independent offline engine (informational only, no redesign)

Reusable behaviour: DSL grammar + parsers, module dispatch, normaliser and grading predicates, feedback state machine,
lesson navigation, content schema and version fields. **Not** reusable as-is: completion/progression (server-owned),
token plumbing, tutor and execution channels, analytics. Original content and assets are separable from all engine
behaviour described here.
