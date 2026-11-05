# MISSION 05 — Execution Plan (concise)

**Branch verified:** `arena/aebb90b7-game` @ `b8b8870a`, clean tree.
**Original APK re-verified read-only:** `/home/user/_work/apk/Mimo_9.35 (1).apk`,
142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`.

## What M01–M04 already established (reused, not redone)

| Area | Already available | Source |
|---|---|---|
| APK/DEX inventory, 12 DEX, 29,454 classes, 122,546 decoded methods | VERIFIED_STATIC | `APK_COMPLETE_INVENTORY.json`, `DEX_BYTECODE_EVIDENCE.json` |
| Content hierarchy + shipped dataset v753 (19 tracks / 144 sections / 1,029 tutorial files / 1,947 chapters / 18,272 lessons) | VERIFIED_STATIC (counts only) | `MIMO_CONTENT_SCHEMA.json`, `00_MIMO_DEEP_ANALYSIS.fa.md` §4 |
| Lesson DSL tag frequency, `LessonProgress` create signature, progress queue, Room SQL strings | VERIFIED_STATIC | `LESSON_AND_SCORING_ENGINE.fa.md`, `MIMO_COMPLETION_ENGINE.json`, `DATA_AND_API_MAP.fa.md` |
| `isSolvedCorrectly = intField >= 1` chain | VERIFIED_STATIC | `LESSON_SCORING_VERIFICATION.fa.md` |
| 53 Retrofit endpoints, 83 endpoint-like strings, currencies/streak/daily goal field names | VERIFIED_STATIC | `MIMO_RETROFIT_ENDPOINTS.json`, `MIMO_SCORING_MODEL.json` |
| Ghidra control flow, 146 geometry constants, Kotlin metadata | VERIFIED_STATIC | `GHIDRA/*`, `PATH_GEOMETRY_CONSTANTS.json` |
| Android 16 emulator boot + real Mimo 9.35 install/launch + onboarding PNG/XML/logcat | VERIFIED_RUNTIME | `ANALYSIS/RUNTIME/MISSION_04/`, run `41998643355` |
| 2,211 JADX-decompiled Java sources | VERIFIED_STATIC | `ANALYSIS/DECOMPILED/getmimo_sources.tar.gz` |

Explicitly **not** redone: DEX re-decoding, Ghidra re-analysis, static APK inventory,
M03 environment proof, M04 transfer/install/launch verification.

## Highest-value remaining unknowns (ordered)

1. **The shipped content itself.** Existing work counted files/keys but did not
   reconstruct the *actual* lesson/exercise/answer JSON from the real shipped
   `assets/lessons-en/tracks/*.json` (57 MB, 1,030 files) nor the answer-validation
   contract. This is the single biggest offline-reconstruction lever:
   the content is **inside the APK**, so no server is needed for it.
2. **Persistence / Room schema.** Only SQL string fragments were collected; no
   entity/DAO/database class inventory, no SharedPreferences/DataStore inventory.
3. **Application state machine / navigation.** 9 deep links + ~300 route strings
   exist but NavHost, back stack and onboarding→path→lesson transitions are UNKNOWN.
4. **Runtime interaction.** M04 stopped at onboarding slide 3. No button was ever
   tapped; no learning path, lesson, answer, or completion screen was ever observed.
5. **Learning-engine formulas.** `rewardMultiplier`, XP, streak, daily goal, chapter
   completion thresholds remain field names only.
6. **Native library call sites.** Only 4 `.so` load lines observed; responsibilities
   are still assigned by filename guess, not call sites.
7. **Offline dependency classification.** No feature-by-feature matrix exists.

## Execution steps (short, concrete)

| # | Step | Method / output |
|---|---|---|
| 1 | **STARTED NOW** — extract (read-only) shipped `assets/lessons-en/tracks/*` + `assets/lesson-webview.js`, `assets/mock/tracks.json`, `assets/testdata/*` into scratch; reconstruct real content model from actual JSON | `CONTENT_MODEL.md`, `SCHEMAS/*`, `SAMPLES/*`, `EVIDENCE/*` |
| 2 | Inventory JADX sources for loaders, Room entities/DAOs, prefs, navigation, ViewModels, interactors; link to DEX offsets where available | `LOCAL_STORAGE_MODEL.md`, `APPLICATION_STATE_MACHINE.md`, `LEARNING_ENGINE.md` |
| 3 | Build `EVIDENCE_DATABASE.json` + append-only `mission_05_append` to `ANALYSIS/EVIDENCE_INDEX.json`; classify every finding | `EVIDENCE_DATABASE.json`, `EVIDENCE_INDEX.json` |
| 4 | Re-stage transfer chunks, extend (not replace) `runtime_smoke.sh` with an isolated M05 interaction branch; capture onboarding→path→lesson states with PNG + XML + logcat | `RUNTIME/` outputs, screenshots/XML in `ANALYSIS/RUNTIME/MISSION_05/` |
| 5 | Offline dependency matrix + native library call-site evidence | `OFFLINE_DEPENDENCY_MATRIX.md`, `NATIVE_LIBRARIES.md` |
| 6 | Architecture, diagrams (Mermaid), open questions, final cross-check | `OFFLINE_ARCHITECTURE.md`, `DIAGRAMS/*`, `OPEN_QUESTIONS.md`, `MISSION_05_REVIEW.md` |

## Evidence vocabulary (mandatory, per finding)

`VERIFIED_STATIC` (APK/DEX/JADX/Ghidra/asset byte-level) ·
`VERIFIED_RUNTIME` (emulator screenshot/XML/logcat/process) ·
`VERIFIED_BOTH` · `INFERRED` (explicitly argued, never promoted) · `UNKNOWN`.

`SERVER CONFIRMED` stays 0. No backend reconstruction, no auth bypass, no fabricated
server responses, no modification of the original APK, no destructive edits to M01–M04.
New work lives under `ANALYSIS/MISSION_05/` and `ANALYSIS/RUNTIME/MISSION_05/`.

**Status:** step 1 in progress.
