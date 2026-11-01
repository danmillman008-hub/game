# Phase 12 — Open questions and B-1…B-13 closure

## Part 1 — B-1 … B-13 (raised by Stages 5–6)

| ID | Question (verbatim) | Answer | Evidence | Label | What would close it |
|---|---|---|---|---|---|
| B-1 | exact id→SQL assignment for the remaining 25 generated DAO lambdas | unchanged from Stage 5: ids 18–21 carry the four `lesson_progress` statements; the other 25 belong to the completion DAOs and were **not** separated | `Database_Impl` switch, 29 cases | **BLOCKED** | re-read `cg/a`+`leg/c`+`leg/f` lambdas with the APK present |
| B-2 | is learner state intentionally not partitioned by account? | confirmed structurally: no account column in any of the three tables, none in `Progress` DTO; attribution is server-side via the Bearer token only | Stage 6 schema; Stage 7 auth | CLOSED_STATIC (structure) / PARTIALLY (intent) | product docs |
| B-3 | non-network failure path of the progress POST | now constrained: `fh.a` wraps interceptor-thrown exceptions into `java.io.IOException`; HTTP errors throw `HttpException` (INFERRED_HIGH); the repository has no catch | N-06, `postUnsyncedLessonProgress` body | PARTIALLY_CLOSED | read the coroutine scope/exception handler in `MainViewModel` |
| B-4 | is there any track-level completion predicate? | **no** — server returns per-tutorial `isCompleted` + `completedChapters`; nothing computes a track boolean | Stage 5 §5, catalogue | CLOSED_STATIC (negative) | — |
| B-5 | what consumes the streak sink `gg.e`? | no streak endpoint exists in the 62-row catalogue, and app analytics goes to `track.customer.io`; therefore either a local consumer or an analytics event | catalogue + C4 | PARTIALLY_CLOSED | read `gg.e` channel consumer |
| B-6 | can `ChapterViewModel.clearOnExit` drop unsynced progress? | the DELETE path exists and is reachable from `clearOnExit`; ordering against the flush is unproven | Stage 5 §5 | CLOSED_STATIC (mechanism) / PARTIALLY (reachability) | trace chapter exit vs `storeAndPostAllLessonProgress` |
| B-7 | is the per-tutorial POST loop sequential? | not resolved; bounded by OkHttp's default dispatcher (max 5 requests per host) regardless | `postUnsyncedLessonProgress` body | PARTIALLY_CLOSED | read the loop's dispatcher / `async` usage |
| B-8 | does the server merge session `attempts`? | unanswerable from the client | — | BACKEND_ONLY | server contract |
| B-9 | are the two Room builder booleans destructive-fallback flags? | unchanged — operands outside the readable window | Stage 6 | BLOCKED | control-flow walk of the provider case |
| B-10 | which key does `getLastInteractedTrackId` read? | **resolved**: it is a network call — `GET /v1/tracks/completion/lastInteracted` → `LastInteractedTrackResponse.lastInteractedTrackId`; the preference key `last_interacted_tutorial_id_<trackId>` has **no reader** in the recovered code | catalogue row + `CompletionRepository.c` | CLOSED_STATIC | — |
| B-11 | full `mimo_prefs` / DataStore key set | unchanged — keys are parameters of a generic helper | Stage 6 | BLOCKED | data-flow on the helper |
| B-12 | does `com.getmimo.data.local.a` hold learner data? | no evidence either way; no network arm touches it | Stage 6 | BLOCKED | read the DataStore schema |
| B-13 | any other writer of the completion tables? | no — only `fetchTrackCompletion` inserts | Stage 5 §6 | CLOSED_STATIC (reachable code) | — |

## Part 2 — new questions from Stage 7

| ID | Question | Why it matters | Label |
|---|---|---|---|
| A-01 | which endpoints carry the auth marker annotation? | decides whether 9 or 53 (or another number) of the 62 rows send a token | BLOCKED (no APK) |
| A-02 | does a sign-out path exist and what does it clear? | logout semantics; `ui.authentication.logout.*` unread | PARTIALLY_CLOSED |
| A-03 | what does `eh.a` on the long-timeout client (C3) fetch? | only endpoint with a 120 s read timeout | UNKNOWN |
| A-04 | which execution channel does a given lesson use, REST or socket? | two parallel implementations | UNKNOWN |
| A-05 | kotlinx `Json` strictness (`ignoreUnknownKeys`, `explicitNulls`) | compatibility with server additions | NOT_RECOVERED |
| A-06 | what happens when the server sends `null` for a timestamp? | Room adapter rejects `Instant` null → persistence failure | UNKNOWN |
| A-07 | do `Response<T>` call sites check `isSuccessful`? | two error styles coexist | NOT_RECOVERED |
| A-08 | does closing the SSE connection abort server-side generation? | cost/quota implications | UNKNOWN (server) |
| A-09 | which dev-menu preference key sits at `sk.a.r[2]`? | flips the API host | PARTIALLY_CLOSED |
| A-10 | does any feature build its own client outside DI? | completeness of `01_NETWORK_CLIENT_INVENTORY.md` | UNKNOWN (negative claim) |

## Part 3 — environmental blocker (affects A-01, B-1, B-9, B-11, B-12)

The APK (`sha256 48ce1740…`) and its 12 DEX files are not present in this environment, and the sandbox's host
allow-list (`github.com`, `pypi.org`, `registry.npmjs.org`) excludes every APK mirror. Stage 7 therefore re-derived
everything from committed evidence. **Re-running any DEX-level check requires restoring the APK artifact to the
sandbox; no other step is blocked.**
