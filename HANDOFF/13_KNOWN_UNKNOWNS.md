# 13 — Known unknowns, limitations and how to live with them

Nothing here is hidden. If a behaviour is in this file, it is **not** claimed to be recovered, and an
implementation that guesses must record the guess in `mimo/OPEN_QUESTIONS.md`.

## 13.1 The two global limitations

| # | Limitation | Consequence |
|---|---|---|
| `LIM-1` | **Zero runtime verification.** Every statement in this package is `VERIFIED_STATIC` (bytecode + assets read from the APK) unless marked otherwise. The app was never executed: the artifact is ARM-only and the analysis environment is x86, and the APK is no longer present in the environment. | A behaviour proven by reading code can still differ at run time; treat matches as strong, not absolute. |
| `LIM-2` | **Server behaviour is unreachable by definition.** No production access was used (and none will be). | Completion rules, ETA, coins, tutor answers remain `BACKEND_ONLY`; the engine must define its own (`ADD-04`). |

## 13.2 Question closure at a glance

| Status | Count | Meaning |
|---|---|---|
| `CLOSED_STATIC` | 36 | answered from the artifact |
| `PARTIALLY_CLOSED` | 24 | answered in part; the residue is listed below |
| `NOT_RECOVERED` | 11 | the code path exists but its content was not read |
| `BLOCKED_BY_ENVIRONMENT` | 8 | would need split APKs, a runtime, or tooling unavailable here |
| `GENUINELY_UNKNOWN` | 6 | no evidence exists in the artifact |
| `BACKEND_ONLY` | 5 | decided by the server; not observable from the client |
| `OUT_OF_SCOPE` | 1 | excluded by the mission rules |

Total tracked: **91** questions. Machine-readable: `data/questions_closure.json`.

## 13.3 Unresolved items, by status

### GENUINELY_UNKNOWN (6)

| id | Question | What it touches |
|---|---|---|
| `Q-140` | webview module URL allowlist | `—` |
| `Q-39` | REST vs WebSocket selection for code execution | `Stage 7 §5.5` |
| `A1` | Is the literal mimo-auth-production a Firebase tenant id, an emulator project, or a preference key? | `05/evidence/DEX_auth_interceptors_and_repository.json` |
| `A10` | Is f9.j's tag-17 branch part of the app or library code? | `mission-07 Pusher doc` |
| `A-03` | what does eh.a on the long-timeout client fetch? | `01_NETWORK_CLIENT_INVENTORY.md §3` |
| `A-04` | which execution channel (REST vs socket) does a lesson use? | `Stage 7 §5.5` |

### NOT_RECOVERED (11)

| id | Question | What it touches |
|---|---|---|
| `Q-17` | serialised JSON names (@SerialName) for DTOs | `—` |
| `A3` | What does the Runnable scheduled inside ku.a.d do? | `05/01 §L11` |
| `A6` | Does account deletion clear the local Firebase user? | `mission-06/11_AUTH_SUBSCRIPTION_CONFIG` |
| `A8` | Does the WebView bridge expose any other JS interface name besides the proven dispatch method? | `mission-08 Stage 3` |
| `A9` | What are the kind values flowing from the lesson page? | `Stage 3` |
| `A14` | what are the two extra JSON documents in id, it, pl, tr (1,032 vs 1,030)? | `Stage 2 corpus stats` |
| `A19` | recovered name of base.c.O | `Stage 3` |
| `A26` | who produces Output.ConsoleOutput in the interactive branch | `Stage 4/7` |
| `A-05` | kotlinx Json strictness (ignoreUnknownKeys, explicitNulls) | `09_DI_DEPENDENCY_MAP.md` |
| `A-07` | do Response<T> call sites check isSuccessful? | `Stage 7` |
| `A-10` | does any feature build its own HTTP client outside DI? | `01_NETWORK_CLIENT_INVENTORY.md §7` |

### BLOCKED_BY_ENVIRONMENT (8)

| id | Question | What it touches |
|---|---|---|
| `Q-05` | dynamic feature module contents (non-English packs) absent from the APK | `mission-08/02_CONTENT_DELIVERY/DYNAMIC_MODULE_IMPLEMENTATION.md` |
| `Q-40` | WebSocket message schema | `mission-07/09_STREAMING/70` |
| `A7` | Which ri.b-annotated endpoints exist? | `Stage 7 §3` |
| `B-1` | exact id→SQL assignment for the remaining 25 generated DAO lambdas | `Stage 6 §2` |
| `B-9` | are the two Room Builder booleans destructive-fallback flags? | `ROOM_MIGRATION_AND_VERSIONING.md §3` |
| `B-11` | full mimo_prefs / DataStore key set | `Stage 6 §3` |
| `B-12` | does com.getmimo.data.local.a hold learner data? | `Stage 6 §4` |
| `A-01` | which of the 62 endpoints carry the auth-marker annotation? | `04_INTERCEPTORS_AND_HEADERS.md §2` |

### BACKEND_ONLY (5)

| id | Question | What it touches |
|---|---|---|
| `Q-49` | server-side chapter completion recomputation | `Stage 5 §5 / 5C` |
| `Q-50` | ETA formula | `Stage 7 endpoint catalogue` |
| `B-8` | does the server merge session attempts? | `—` |
| `A-06` | server sending null for a timestamp -> Room Instant null | `06_REQUEST_RESPONSE_MODELS.md §4` |
| `A-08` | does closing the SSE connection abort server generation? | `08_SSE_AND_WEBSOCKET.md` |

### PARTIALLY_CLOSED (24)

| id | Question | What it touches |
|---|---|---|
| `Q-115` | feature gating matrix for premium | `mission-07/13_SUBSCRIPTION/91_ENTITLEMENT_AND_PAYWALL_COMPLETE.md` |
| `Q-118` | remote-config flag consumers | `mission-07/10_ANALYTICS_CONFIG/85_FEATURE_FLAG_COMPLETE_CATALOG.json` |
| `Q-134` | consent/opt-out surface | `mission-07/evidence/* consent strings` |
| `Q-30` | unknown-tag behaviour per parser | `Stage 3 parser grammar (U-01)` |
| `Q-34` | which .riv animations bind to which lesson state | `mission-07/12_UI_RESOURCES/79_RIVE_COMPONENT_MAPPING.csv` |
| `Q-57` | keys/hearts consumption path | `Stage 7 catalogue (Lbh/a;)` |
| `Q-89` | Pusher channel usage | `mission-07/09_STREAMING/71` |
| `U-20` | analytics event-name to emitter binding | `mission-07/evidence/EVENTS_WITH_CALLSITES.csv` |
| `A2` | Where is sign-out implemented? | `05_AUTHENTICATION_CLOSURE/04_SESSION_STATE_MACHINE.md` |
| `A12` | does a missing locale fall back to en? | `02_CONTENT_DELIVERY/CONTENT_CACHE_IMPLEMENTATION.md` |
| `A13` | are content stream/parse failures caught, and where? | `Stage 2 report` |
| `A15` | which module owns <output> | `Stage 3 module variants` |
| `A17` | meaning of the five boolean flags in InteractiveLessonBaseViewModel | `Stage 4/5 view-model analysis` |
| `A20` | is hardModeLessonModules parsed from the same document? | `Stage 3` |
| `A22` | meaning of the six jm.o booleans (hint / solution / retry / AI tutor) | `Stage 4 jm.o analysis` |
| `A23` | which types use mm.b.E0 pass-through grading | `Stage 4 six graders` |
| `A24` | duration of the delay before verdict dispatch | `Stage 4` |
| `A27` | which composable consumes browserOutputDeferred | `Stage 4 UI surface` |
| `A28` | what selects MultipleChoice vs SingleChoice | `Stage 4 SIX_MODULE_VARIANTS.json` |
| `B-3` | non-network failure path of the progress POST | `07_ERROR_RETRY_OFFLINE.md §1` |
| `B-5` | what consumes the streak sink gg.e? | `Stage 5 + Stage 7 catalogue` |
| `B-7` | is the per-tutorial POST loop sequential? | `07_ERROR_RETRY_OFFLINE.md §5` |
| `A-02` | does a sign-out path exist, and what does it clear? | `Stage 7 §3` |
| `A-09` | which dev-menu preference key is sk.a.r[2]? | `09_DI_DEPENDENCY_MAP.md §3` |

## 13.4 Which of these actually affect the `mimo/` engine

| Unknown | Affects the engine? | How to proceed |
|---|---|---|
| `A-05` JSON strictness (unknown keys) | **yes** — content loading policy | pick ignore-with-warning, document it (`03` §7) |
| `Q-30` unknown-tag behaviour | **yes** — parser | same policy applies; never crash silently |
| `A12` locale fallback | **yes** — content packs | `ADD-07` requires an explicit chain (`en` last) |
| `A17`/`A22` flag meanings in feedback state | **partially** — which affordances appear | implement the subset you need, list the rest |
| `A23`/`A28` grader selection (MultipleChoice vs SingleChoice) | **partially** — type discrimination | derive the type from the DSL block; record the rule |
| `B-1` 25 DAO lambda ids | **no** — statement texts recovered | schema + statements are enough |
| `B-9` Room builder booleans | **no** | irrelevant offline |
| `A-01` per-endpoint auth annotation | **no** — no network in the engine | only matters if you write a sync adapter |
| `Q-140` WebView allowlist | **only if** you render `<webview>` | sandbox it or render as a link |
| `A-04`/`Q-39` execution channel | **no** — executable lessons are dropped (`D-13`) | do not implement |
| `Q-49`/`Q-50`/`B-8` server completion/ETA/attempt merge | **no** — replaced by `ADD-04` | state the local rule |
| `A14` two extra JSON docs in 4 locales | **no** | unexplained, harmless |
| `A8` extra WebView JS interfaces | **no** | not implemented |

## 13.5 Standing corrections to earlier claims

The mission's correction log (`mission-08/99_FINAL_CLOSURE/` register `C-01…C-24`) records every claim that was walked
back, with old and new evidence. The four most relevant to this package:

| id | Correction |
|---|---|
| `C-16` | persisted learner key is `(lessonId, tutorialId)`, not the five-part identifier |
| `C-21` | "offline" must be qualified: content and lesson work are offline; progression is not |
| `C-22` | learner statistics are not persisted; a successful upload deletes the rows |
| `C-24` | the 9-unauthenticated-endpoint claim is `INFERRED_HIGH`, not verified per row |

## 13.6 What "closed with declared limitations" means here

The project is terminal in that state. It will stay that way unless the missing **artifacts** appear: the split APK
bundles (for `Q-05`, `B-1`, `B-9`, `B-11`, `B-12`, `A-01`), an ARM device/emulator (for every runtime question), or
legitimate server documentation (for every `BACKEND_ONLY` item). Absent those, a further investigation would restate
this list, not shorten it.

