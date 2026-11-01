# MISSION 6 — Complete Mimo Reverse Engineering
### Full-system architecture and behavioural reconstruction of the analysed Mimo 9.35 artifact

**Artifact**: `Mimo_9.35 (1).apk`, 142,353,499 B, sha256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`,
md5 `f9cef2d8029e59da3668ec1c18e21566`, 14,398 zip entries, 12 dex.
**Integrity**: third-party re-signed (`META-INF/YOUAREFINISHED.RSA`), mod watermark in 11,543 strings, injected
`com.getmimo.App extends bin.ghost.yrf` + `libyrf.so` → see `00_BASELINE/INTEGRITY_CAVEAT.md`.
**Branch** `arena/ecb8af07-game` · **start** `10a96004` · all work under `mimo-re/mission-06/`.

---

## Verdict in one paragraph
The client is a **content-driven lesson player** whose intelligence lives in two places: a tiny XML DSL with
seven parsers, and a five-state-per-exercise runtime that writes a local outbox. Grading is two-phase string
comparison with an aggressive character filter; the solution ships inside the lesson (`File.solvedContent`),
so interactive correctness is client-side while code tasks are server-executed. Content is bundled in English
and delivered as Play dynamic modules for other locales; the network layer is a single OkHttp client against
`https://api.mimo.org/v1`, bearer-authenticated, with an SSE channel for the AI tutor and a WebSocket for code
runs. Gamification (coins, keys, streaks, leagues, sparks) is **server-authoritative and display-only** — the
client never computes an economy value. Everything below is `VERIFIED_STATIC` unless marked otherwise; **no
claim in this mission is runtime-verified** (`15_RUNTIME/97_RUNTIME_RESULTS.md`).

---

## §25 — the review questions, answered

**Q1 · What is the real application architecture?**
Single-Activity-entry (12 deep-link filters on `MainActivity`) + 61 activities + 19 services, MVVM with
coroutines, Compose for newer surfaces and Fragments/Views for the lesson flow. DI is a hand-rolled
**127-case `when` switch** in `ae.m`, not Dagger/Hilt. Details: `01_APK_AND_ARCHITECTURE/04`.

**Q2 · How does the app start up?**
`bin.ghost.yrf` (foreign) → `com.getmimo.App` → DI graph → Firebase/analytics init → onboarding gate (17-fragment
graph) → main. Mimo-specific initialisation order and the splash aliases are documented in
`01_APK_AND_ARCHITECTURE/03`; the injected base Application is excluded from the picture.

**Q3 · What is the content hierarchy?**
Track → Section → Tutorial (ids/ranges) → Chapter → Lesson → LessonContent (`INTERACTIVE` |
`EXECUTABLE_FILES`). Only four levels are real classes; tutorials exist as `tutorialIds` ranges. `02_CONTENT_SYSTEM/09`.

**Q4 · How is content delivered and cached?**
English corpus bundled (10,327 documents); other locales via Play dynamic modules (`content_<locale>`); previews
as zips (`GET /v1/package/preview`); **no content table in Room** — the database is an outbox, not a cache.
`02_CONTENT_SYSTEM/11`.

**Q5 · How is content versioned?**
`TracksJson.publishSetVersion` + per-lesson `trackVersion`; progress stores both versions but keys on
`(lesson_id, tutorial_id)`, so progress is version-agnostic while addressing is version-aware. Update-detection
policy is **UNKNOWN**. `02_CONTENT_SYSTEM/12`.

**Q6 · What exactly is the lesson DSL?**
XML with **29 tags**, HTML-shaped (`p`, `code`, `selection`, `img`, `webview`, `database`, plus inlines).
Grammar, semantics and corrections to mission-05's grammar: `03_DSL_AND_RUNTIME/16`, `17`, `24`.

**Q7 · How does the parser work?**
Pull-parser recursion with one class per module kind and a string-comparison dispatcher (`te.c.b`); no registry,
no schema validation; structural errors are hard, semantic gaps are soft. `03_DSL_AND_RUNTIME/18`.

**Q8 · What does the AST look like?**
Normalised JSON Schema in `03_DSL_AND_RUNTIME/19_AST_SCHEMA.json` (six module kinds, interactions, output,
tables, inlines).

**Q9 · How does rendering work?**
ViewModel→state→View with span composition (`SpannableStringBuilder`, `qc.a`, `qm.h`), one custom
`PartiallyEditableEditText`, and a separate highlighting palette for code. `03_DSL_AND_RUNTIME/20`.

**Q10 · What happens at runtime when a learner answers?**
Submit → (300 ms delay only for free text) → two-phase compare → verdict → progress write → feedback paragraph →
analytics → proceed marks solved. `03_DSL_AND_RUNTIME/21`.

**Q11 · What is the formal exercise state machine?**
`IDLE, AWAITING, CORRECT, PARTIAL, INCORRECT, SOLVED, RESET` with 10 transitions and three invariants
(`attempts` always increments; `solved` = correct|partial; no pass threshold). `22`, `05_LEARNER_MODEL/38`.

**Q12 · Which interaction kinds exist?**
Exactly four: `FILL_THE_GAP`, `SELECTION`, `SPELL`, `VALIDATED_INPUT`. No drag-and-drop, ordering or multi-select.
`04_INTERACTION_AND_GRADING/25`.

**Q13 · How is grading implemented?**
Exact match → CORRECT; normalised match → CORRECT with input overwritten to the canonical text; else INCORRECT.
Expected text is a **substring of the code module**, so there is no answer list. `04/26`.

**Q14 · What is the normalisation rule?**
`lower()`, then keep only `[a-z0-9<.]`. Consequences include `my_var == myvar` and `a+b == ab` (false
positives), and non-Latin answers collapsing to `""`. `04/30`.

**Q15 · Are alternative answers possible?**
No. One expected string, no regex/alternatives; only normalisation provides tolerance. `04/31`.

**Q16 · How is feedback delivered?**
Authored paragraphs with `visible-if` = `correct`/`wrong`; wrong answers never reveal the solution; no hint
system exists. `04/27`, `04/28`.

**Q17 · What does the learner model contain?**
Server-authoritative identity/premium/coins/keys/streaks; local only progress rows. `05_LEARNER_MODEL/32`.

**Q18 · How is progress aggregated?**
lesson → chapter flag → tutorial completion → track completion/ETA; first-try is **derived**
(`solved && attempts==1`), never stored. `05/33`, `04/29`.

**Q19 · Is there mastery or spaced repetition?**
No. No interval/ease fields, no review queue, no mastery score; "personalisation" is authored difficulty
(chapter type), hard mode, and server pacing. `05/34`.

**Q20 · What gamification exists?**
Coins, keys, daily goal (+coin reward), streaks, leagues (with freeze), leaderboards (friends/latest), sparks as
league score. **No XP model exists.** `05/35`, `05/36`, `05/37`.

**Q21 · How is local persistence structured?**
Three Room tables (`lesson_progress` with 11 columns, `chapter_completions`, `tutorial_completions`); no
migrations → destructive strategy inferred; insert-not-update semantics. `06_PERSISTENCE_AND_SYNC/40`, `41`.

**Q22 · How does sync work?**
`in_queue` dirty flag → batch `POST /v1/tutorials/{tutorialId}/progress {progressList}` → delete on 2xx. No
merge engine, no watermark, no retry/backoff, no dead-letter. `06/43`, `06/44`, `06/45`.

**Q23 · What works offline?**
Bundled lessons and local grading; progress queues; everything else throws `NoConnectionException` before
dialling; executable lessons fail. `06/46`.

**Q24 · What is the network contract?**
`https://api.mimo.org` (+ `api-testing.mimo.org`), `/v1/` paths, OkHttp 20 s/30 s, interceptors
connectivity→UA→Bearer, `Mimo/9.35 Android/<release>` UA, 62 endpoints (28 GET/24 POST/4 PATCH/4 DELETE/2 PUT).
`07_NETWORK/47`–`55`.

**Q25 · How does the AI tutor work?**
POST start/continue with `{systemMessage, userMessage}`, `Accept: text/event-stream`, SSE append, terminate on
`finishReason ∈ {Length, Stop}`, quota by `userMessageCount`, **no local transcript**. `08_AI_TUTOR/56`–`62`.

**Q26 · How does navigation work?**
One entry activity, deep links for `getmimo.com` + `mimo://`, onboarding graph then content; AI tutor reached
from lesson context. Path grammar **NOT_RECOVERED**. `09_NAVIGATION_AND_UI/63`–`69`.

**Q27 · What is the design system?**
Aeonik Pro/Mono/Fono (15 font assets, family descriptors), two colour systems (UI + editor), Rive animation;
token **values** are BLOCKED by tooling. `10_DESIGN_SYSTEM/70`–`74`.

**Q28 · How do auth and subscriptions work?**
Bearer token on authenticated calls (53/62 endpoints); login exchange **NOT_RECOVERED**; RevenueCat for
purchases, single `isPremium` entitlement, coin-priced consumables, remote discount themes; 3 remote-config
flags. `11/75`–`81`.

**Q29 · What analytics exist?**
First-party facade + Firebase/Adjust/Sentry; 252 event-name candidates (INFERRED), only `lesson_reset`
verified at a call site; emitter binding is `U-20`, still open. `12/82`–`85`.

**Q30 · What native and third-party code ships?**
`librive-android.so` (Rive), `libsigner.so` (Adjust), `libc++_shared.so`, `libyrf.so` (foreign); ARM only.
10 SDK groups mapped. `13/86`–`89`.

**Q31 · What is the security posture?**
Code-readability obfuscation only, no string encryption, no pinning found, Play Integrity not found, client
progress is an unsigned assertion, content packs unverified — and the analysed APK itself is re-signed.
`14/90`–`93`.

**Q32 · Can any of this be runtime-verified here?**
No. 15 tests planned with source-derived expectations; all `BLOCKED` (no device, no account, no network, no
stock APK, no instrumentation). `15/94`–`97`.

**Q33 · What is the cross-domain picture?**
Content (bundled AST) → parser → lesson VM → verdict → outbox → tutor/analytics/gamification surfaces, all
mediated by one authenticated OkHttp client and one Room outbox; 20 sequence diagrams in
`107_SYSTEM_SEQUENCE_DIAGRAMS/`. Server-side behaviour is deliberately **not** asserted (RULE 3).

---

## New discoveries (this mission)
1. `LessonIdentifier` is a **5-part key including `trackVersion`**, while progress keys on 2 parts.
2. `File.solvedContent` — the solution ships with executable lessons; grading is server-side.
3. The DSL's "module" tags are HTML tags (`p`, `img`, `br`), correcting mission-05's `<paragraph>`/`<image>`.
4. `ContentLocale` has only 5 constants while UI strings cover ~12+ languages and content modules cover more.
5. `TrackEtaResponse.currentPaceMinutesPerDay` — the only predictive field in the contract.
6. `LeaderboardUserResult` carries both `league` and `newLeague` plus `usedLeagueFreeze` — promotion is reported,
   not requested.
7. Normalisation drops `_`, `+`, quotes and brackets → documented false-positive class.
8. `hg.e` throws before the socket, so offline behaviour is deterministic in code, not in the UI.
9. Error-branch analysis shows `require()` = hard failure vs soft semantic gaps — a two-tier robustness model.
10. The base URL is produced by a 127-case DI switch (why grep failed for two missions).

## Corrections to earlier missions (recorded, not retro-edited)
| Mission-05 statement | Corrected here | Evidence |
|---|---|---|
| DSL modules `<paragraph>`, `<image>` | `<p>`, `<img>` | `te.d.a`, `te.c.a` |
| `<selection>` nested inside code | top-level module | `te.c.b` dispatch |
| U-01 unresolved | closed: full grammar of 7 parsers | `evidence/PARSER_GRAMMAR.json` |
| U-22 unresolved | closed: prod/dev hosts + WSS | `evidence/DI_GRAPH.json` case 22, `pg.a` |
| U-15 partial | closed: SSE, start/continue, quota DTO | `08_AI_TUTOR/*` |
| U-23 PATCH vs PUT ambiguous | both exist (4/2) | `07_NETWORK/52` |
| "progress has 11 columns" | confirmed and extended: no first-try column | `06/40` |

## Where to start reading
`00_BASELINE/INTEGRITY_CAVEAT.md` → `01_APK_AND_ARCHITECTURE/04_ARCHITECTURE_OVERVIEW.md` →
`03_DSL_AND_RUNTIME/16` → `04_INTERACTION_AND_GRADING/26` → `06_PERSISTENCE_AND_SYNC/44` →
`16_INDEX_AND_EVIDENCE/101_COVERAGE_MATRIX.md` → `20_FINAL_AUDIT/118_UNRESOLVED_CLAIMS.md`.
