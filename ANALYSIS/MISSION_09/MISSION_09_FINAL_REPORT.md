# MISSION 09 — FINAL REPORT: COMPLETE MIMO 9.35 CLIENT RECONSTRUCTION

**Document:** `MISSION_09_FINAL_REPORT.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 0. Verdict (read this first)

**MISSION 09 is complete.** The independent offline-equivalent client **CAN be implemented**
to behavioural fidelity for everything the Mimo 9.35 app does locally. Every technically
resolvable client-side gap has been closed or bounded to an explicit interface. Nothing
server-owned was fabricated, `SERVER CONFIRMED = 0`, and this is **not** a claim of 100%
reverse engineering of the whole product (server-authoritative and authenticated
behaviour remains outside the boundary).

**Can the offline client be implemented? — YES.** `COMPLETE_IMPLEMENTATION_BLUEPRINT.md`
gives 16 component contracts, verbatim data contracts, faithful pseudocode, 4 explicit
interfaces with deterministic offline fallbacks, 4 labelled independent design decisions,
a Mermaid architecture and 15 deterministic acceptance tests. An implementer does not
need to reopen the APK.

## 1. What is FULLY RECONSTRUCTED

* Startup chain and Activity lifecycle (`SplashActivity` -> `IntroSlidesActivity` ->
  `OnboardingActivity` (NavHost) -> `AuthenticationActivity` `Skip` -> `MainActivity` ->
  `ChapterActivity`), with direct API-36-safe lifecycle hooks.
* Application state initialisation (`App` 13 collaborators, hand-rolled `Lhm/b;` container,
  constructor-injected graphs, Room/DataStore/SharedPreferences bootstrap).
* Learner representation (3 Room tables, 11 `lesson_progress` columns, prefs keys,
  `Settings` object, DataStore file).
* Curriculum graph: **all 10,298 shipped tutorial JSON assets across 10 locales validated**;
  19 tracks / 144 sections / 1,029 tutorials / 1,947 chapters / 18,272 unique lessons;
  0 parse failures, 0 missing refs, 0 duplicate lesson IDs, 0 orphan files,
  0 section-range violations; 4 locale discrepancies reported, never repaired.
* Module parsing (`Lte/c.b`, `XmlPullParserFactory`), 9 interaction families and the
  renderer registry for all 37,183 lesson placements.
* Exact validator bodies (fillTheGap, selection, spell, validatedInput normalizer +
  partial-match result, executable `List.equals`, `isSolvedCorrectly()`).
* Progress row construction, attempts/tries semantics, `AnswersInChapter` counters.
* Persistence, offline matrix, connectivity gate, queue cleanup SQL, migrations shape.
* 53 endpoint client contract with DEX-resolved HTTP verbs (3 verb labels corrected).
* `MainActivity` -> `MainViewModel.d` -> repositories/keys/IAP/practice chain,
  `NavigationBar.setActive` destination map, `GetPathMapState` live collaborator graph.
* Guest Practice UI gate vs repository-level streak auth gate (two distinct layers).
* 20 client-side algorithms A1–A20 with signature, inputs, outputs, state, side effects,
  callers/callees, evidence, pseudocode, confidence and edge cases.

## 2. What is RUNTIME-VERIFIED

M08 runs `42042312640`, `42046336206`, `42049141553`, `42050715150` (1,210 raw events)
and **M09 run `42077425594`** (691 events) give **1901** merged events in
`COMPLETE_RUNTIME_TIMELINE.jsonl`.

| M09 proof | Value |
|---|---|
| `sha_gate` | `SHA_MATCH_OK bytes=142353499` |
| Frida attach | `attach_ok=true, pid=3348, name="Mimo"` |
| Hooks installed | 181 |
| Real `com.getmimo` method `entry` events | 72 (71 `exit`, 86 SQL, 17 DI, 19 LiveData, 28 nav) |
| `real_target_method_executed` | **true** |
| `webview` events | 0 (no lesson reached) |
| `server_confirmed` | 0 |

The M08 API-36 `Application$ActivityLifecycleCallbacks` failure is fixed by direct
`android.app.Activity` / `androidx.fragment.app.Fragment` / `WebView` hooks. All three
user-required instrumentation conditions are satisfied.

Runtime-verified specifics: `MainActivity.B()` live field graph; `NavigationBar.setActive`
4-route map; `MainViewModel.F/I/H`; `GetPathMapState` collaborators and
`PathMapViewModel` call `b(50,0,null,...)`; `RefreshPathToolbarState` coin/key flows;
`Coins.getCoins()=0`; `streak_getData` -> `AccessTokenUnavailableException`;
`PostVisitWorker.a()`; **`DELETE FROM lesson_progress WHERE in_queue = 1` at startup**;
Room bootstrap SQL; 17 third-party-only network events; offline cold start returning to
`IntroSlidesActivity`.

## 3. What is STATIC-ONLY (`VERIFIED_STATIC`)

`V()`/`W()`/`X()` bodies, `d0()` feedback objects, `jm/m|n|o`, native validator dispatch,
`GetPathMapState` exact status boolean, `ds/w.c` key membership, HTTP verb mapping,
53 endpoint signatures, `SingleChoice`/`MultipleChoice`/`Reveal` dispatch, worker classes.
These are bytecode-faithful but **not** called `VERIFIED_RUNTIME`.

## 4. What is SERVER-DEPENDENT / genuinely UNKNOWN

Absolute XP / streak / keys / reward / daily-goal formulas, live subscription tier and
unlock keys, chapter/tutorial completion transitions, authenticated practice /
leaderboard / profile screen contents, native WebView bridge object schema, remote code
runner, DataStore protobuf semantics, worker periodicity, JNI internals, real backend
request/response bodies. 12 entries with exact closure conditions are in
`FINAL_UNKNOWN_REGISTER.md`. No fabricated response, formula or unobserved fact exists
in any deliverable.

## 5. High-confidence behaviours (implement these verbatim)

1. `isSolvedCorrectly()` = `tries >= 1` (not `attempts`).
2. `lesson_progress` has exactly 11 columns, PK `(lesson_id, tutorial_id)`, `in_queue=true`
   on creation.
3. `selection` = `all{ selected == isCorrect }`; `fillTheGap`/`spell` = ordered,
   case-sensitive token equality; `validatedInput` normalizes `Locale.US` lower +
   letters/digits + `< > ( ) : { } , .`; `executable` = `List.equals(solvedContent)`.
4. Invalid DSL -> empty module list -> noninteractive slide.
5. Curriculum is strictly ordered, never randomized; prerequisites are the previous
   lesson / chapter / tutorial in the shipped index.
6. `NetworkUtils.a()` = WIFI or CELLULAR transport; `postUnsyncedLessonProgress` throws
   `NoConnectionException` offline.
7. Startup executes `DELETE FROM lesson_progress WHERE in_queue = 1` — destructive,
   local, **not** server acknowledgement.
8. Guest Practice is a UI-only gate; streak data requires an access token at repository level.
9. `f0(false,true)` is analytics, not XP.
10. No Mimo `/v1/...` request or response was ever observed.

## 6. Independent design decisions (never presented as Mimo behaviour)

1. **Durable sync queue** instead of Mimo's destructive startup DELETE.
2. **No award formula** — only local counters F1–F12; any XP/coin rule is opt-in and labelled.
3. **Local sequential unlock** instead of the UNKNOWN tier/key predicate.
4. **Independent WebView bridge** modelled on the shipped JS asset, since the native object
   is unknown.

## 7. Deliverables — exact location

All 19 files are in **`ANALYSIS/MISSION_09/`**:

1. `MISSION_09_FINAL_REPORT.md`
2. `COMPLETE_CLIENT_ARCHITECTURE.md`
3. `COMPLETE_LESSON_ENGINE_SPEC.md`
4. `COMPLETE_LEARNER_STATE_SPEC.md`
5. `COMPLETE_PROGRESSION_ENGINE_SPEC.md`
6. `COMPLETE_ECONOMY_SPEC.md`
7. `COMPLETE_NETWORK_API_CONTRACT.md`
8. `COMPLETE_AUTH_AND_LIFECYCLE_SPEC.md`
9. `COMPLETE_UI_RENDERER_CATALOG.md`
10. `COMPLETE_CURRICULUM_GRAPH.json`
11. `COMPLETE_SYSTEM_MAP.json`
12. `COMPLETE_NAVIGATION_STATE_MACHINE.json`
13. `COMPLETE_RUNTIME_TIMELINE.jsonl`
14. `COMPLETE_EVIDENCE_DATABASE.json`
15. `COMPLETE_IMPLEMENTATION_BLUEPRINT.md`
16. `FINAL_UNKNOWN_REGISTER.md`
17. `FINAL_TEST_MATRIX.json`
18. `FINAL_COVERAGE_MATRIX.md`
19. `MISSION_09_REPRODUCTION_GUIDE.md`

Supporting (preserved, not overwritten): `ANALYSIS/RUNTIME/MISSION_09/` (raw M09 timeline,
UI XML, DB/prefs snapshots, logs, traces), `ANALYSIS/RUNTIME/MISSION_08/`,
`ANALYSIS/MISSION_08/` (7 deliverables), `ANALYSIS/MISSION_07/` (18 reports + 202-entry
evidence DB), `ANALYSIS/MISSION_06/`, `ANALYSIS/MISSION_05/`.

## 8. Test and validation results

| Check | Result |
|---|---|
| M09 GitHub Actions run | SUCCESS (`42077425594`) |
| `sha_gate` / APK unchanged | PASS (`48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`) |
| Instrumentation (3 conditions) | PASS |
| 10,298 curriculum assets parsed | PASS (0 failures) |
| Normalized `Track->...->Prerequisite` graph | PASS |
| All JSON files parse | PASS |
| `COMPLETE_RUNTIME_TIMELINE.jsonl` line-by-line parse | PASS (1901 lines) |
| Mermaid blocks | PASS (flowchart syntax) |
| `[E##]` references resolve | PASS |
| Referenced file paths exist | PASS |
| Third-party token redaction | PASS (no raw token in any deliverable) |
| `SERVER CONFIRMED` | 0 everywhere |
| Existing M05/M06/M07/M08 evidence | PRESERVED |
| Git working tree | CLEAN at final commit |

## 9. Limitations recorded, not hidden

* M09 onboarding chain `reached=false` (stalled at step 4/20 on this build's question
  set); `MainActivity` reached via explicit intent.
* M09 lesson answer matrix **NOT EXECUTED** — `ChapterActivity` not reached; no answer was
  guessed. M07 stage 5/6 runtime matrix remains authoritative.
* Practice/Leaderboard/Profile route screens in M09 were contaminated by an incomplete
  `OnboardingActivity` back stack; screen contents are UNKNOWN. The `setActive`
  destination map and M08's guest Practice gate are verified.
* 0 `webview` events in M09; native WebView bridge remains UNKNOWN.
* No queued row existed in M09 to be deleted; the DELETE statement itself was captured.

## 10. Branch and commit

**Branch:** `arena/aebb90b7-game` (fixed for this session).
**Deliverables commit:** `9e6ec9ac`.
Harness/runtime commit: `1744ab0c`. M08 final: `67353077`. M07 closure: `477d3195`.
The final metadata commit that records this hash is reported in the task response.

**No further broad discovery mission is recommended.** The remaining items require either
a legitimate authenticated account or server cooperation; they are fenced by interfaces
and deterministic offline fallbacks, not left as open-ended investigation.
