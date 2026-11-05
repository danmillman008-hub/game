# OFFLINE_ARCHITECTURE — reconstructed client architecture of Mimo 9.35

**Goal:** faithful reconstruction of the *client*, not a redesign and not a
backend reproduction. `SERVER CONFIRMED = 0`.
APK `48ce1740…7c7a` · `com.getmimo` 9.35 / `1792759685` ·
`minSdk 28 / targetSdk 36` · Android 16 emulator, `x86_64` + ARM64 translation.

## 0. Vocabulary

`VERIFIED_STATIC` · `VERIFIED_RUNTIME` · `VERIFIED_BOTH` · `INFERRED` · `UNKNOWN`.
Every section below labels its claims. Mermaid diagrams in `DIAGRAMS/`.

## 1. One-paragraph architecture — `VERIFIED_STATIC` + `INFERRED`

A Kotlin/Java Android app (R8-obfuscated, 12 DEX, 29,454 classes, 122,546
methods) with a **shipped, read-only JSON curriculum** in `assets/`, a
**kotlinx.serialization** DTO layer, an **HTML-like lesson DSL** parsed into
`Parcelable` `LessonModule`/`Interaction` objects, a **Compose + Fragment hybrid
UI** rendering lessons partly in a **WebView** with a JS↔native bridge, a
**Room/SQLite** progress database with an `in_queue` offline outbox, a
**DataStore Preferences** flag store, and a **Retrofit** layer for the account,
economy, sync, code-execution and remote-config services. Six `arm64` native
libraries (Rive animation, Adjust signer, DataStore counter, graphics path,
C++ runtime, and an in-app-integrity helper) load via `libndk_translation.so`
on x86_64. Learning content and answer keys are **local**; economy and
execution services are **remote**.

## 2. Layer map — `VERIFIED_STATIC`

| Layer | Components | Provenance |
|---|---|---|
| **Content (read-only)** | `assets/lessons-<10 locales>/tracks/tracks.json` + `tutorial-<id>.json` (10,298 files), `lessons-common/icons/` (215), `lesson-webview.js`, `highlight.min.js`, `beautify/*`, `prettier/*`, `snippets/*`, `spieglein/editor.bundle.js`, `styles/*.css` | `EVIDENCE/ASSET_MANIFEST.txt` |
| **Serialization / loader** | `TracksJson`/`TrackJson`/`SectionJson`/`TutorialJson` + `*$$serializer`, `DefaultTrackLoader`, `DefaultTracksRepository`, `ContentLocale`, `userContentLocaleProvider` | JADX + DEX literals |
| **Lesson DSL parser** | `data/content/lessonparser/interactive/ParserModule`, `model/{LessonModule,Interaction,Option,SelectionItem,Output,Table,ModuleVisibility,Attribute,Tag,WebviewType}`, `textstyle/CustomTypefaceSpan` | JADX package tree |
| **Runtime content model** | `Track`, `Section` (`hasProgress`, `index`), `Tutorial` (`isCompleted`), `Chapter` (`isCompleted`), `Lesson`, `LessonContent.Interactive/Executable`, `LessonIdentifier` | `SCHEMAS/JADX_MODEL_FIELDS.json` |
| **UI** | `MainActivity`, `OnboardingActivity`, `IntroSlidesActivity`, Compose path map (`PathMapFragment`), `ChapterActivity`, `InteractiveLessonFragment` + 6 interaction-specific ViewModels, executable lesson + `CodeDiffView`, `ChapterFinished*Fragment`s, Rive composables | DEX class names |
| **WebView bridge** | `assets/lesson-webview.js` → `MimoLesson.postMessage` → `mimo.activity.correct/wrong/completed`, `gesture`, `focus`, `height` | `SAMPLES/lesson-webview.js`, DEX offsets |
| **State / domain** | ViewModels + `interactors/{lesson,chapter,chapterend,path,streak,practice,leaderboard,settings,authentication,…}`, `GetPathMapState`, `GetChapterEndSuccessState`, `LoadOnboardingPaths` | JADX package tree |
| **Persistence** | Room `mimo.db` (`lesson_progress`, `chapter_completions`, `tutorial_completions`), DataStore `user_preferences`, legacy SharedPreferences migration, WorkManager | `EVIDENCE/ROOM_SQL.txt` |
| **Network** | Retrofit, 53 endpoints; `LessonProgressApi`, `CompletionApi`, `TrackEtaApi`, `CodePlaygroundExecution…`, `/v2/client-config` | `ANALYSIS/MIMO_RETROFIT_ENDPOINTS.json` |
| **Native** | 6 × `arm64-v8a` + 6 × `armeabi-v7a` `.so` | `NATIVE_LIBRARIES.md` |
| **Third-party** | Firebase (Crashlytics, Remote Config, Analytics), Adjust, RevenueCat, Customer.io, Rive, Joda-Time, kotlinx.serialization, OkHttp/Retrofit, WorkManager | `APK_COMPLETE_INVENTORY.json`, logcat |

## 3. Data flow: a lesson — `VERIFIED_STATIC` for components, `INFERRED` for order

```
APK assets (tracks.json + tutorial-<id>.json)
   │  kotlinx.serialization → *Json DTOs
   ▼
DefaultTracksRepository / DefaultTrackLoader
   │  + Room (chapter_completions, tutorial_completions, lesson_progress)
   ▼
Runtime models (Track/Section/Tutorial/Chapter/Lesson with isCompleted/hasProgress)
   │  Parcelable LessonBundle / LessonContent
   ▼
ChapterActivity → InteractiveLessonFragment (+ per-interaction ViewModel)
   │  ParserModule → LessonModule / Interaction / Option / Output
   ▼
Native Compose views  +  WebView (lesson-webview.js, highlight.js, prettier)
   │  user answers  →  mimo.activity.correct / wrong / completed
   ▼
InteractiveLessonBaseViewModel
   ├─ visible-if feedback (shipped text)
   ├─ storeLessonProgressInMemory → Room lesson_progress (in_queue=1)
   └─ lessonSolvedAndProceedToNextLesson / showWrongFeedbackBlock (retry)
   ▼
ChapterFinishedViewModel → storeAndPostAllLessonProgress
   ├─ handleOnlineState  → POST /v1/tutorials/{id}/progress → in_queue=0
   └─ handleOfflineState → keep queued rows
```

**`VERIFIED_STATIC` break:** the correct/incorrect decision and the feedback
text do not traverse the network. **Only the sync and the economy do.**

## 4. Data flow: application start — `VERIFIED_STATIC` + `VERIFIED_RUNTIME`

```
launcher intent → com.getmimo/.ui.SplashActivity_default        VERIFIED_RUNTIME (41998643355, 42002808217)
  → IntroSlidesActivity (ViewPager, rotating slides)           VERIFIED_RUNTIME (PNG+XML)
  → Get started / I already have an account                     VERIFIED_RUNTIME (XML bounds)
  → OnboardingActivity: Welcome → 12-step questionnaire
      → "Front-End Developer is the best choice for you!"       VERIFIED_RUNTIME (STEP-01..12)
  → dailygoal … PreparingCurriculum … PathMapFragment           INFERRED (declared fragments)

OFFLINE COLD START (42002808217, wifi+data disabled, "Active default network: none"):
  IntroSlidesActivity → Welcome → motive → goal                 VERIFIED_RUNTIME (OFFLINE-00..03)
  UI_HIERARCHY STEP-01/02/03 == OFFLINE-01/02/03 byte-for-byte VERIFIED_RUNTIME (equality proof)
```

Application init order (`App.onCreate`, DI graph, `InitializationProvider`),
NavHost and back stack remain `UNKNOWN` (M02 gap #11/#13).

## 5. Offline boundary — the decisive finding — `VERIFIED_STATIC`

| Concern | Resides on device? | Consequence |
|---|---|---|
| **Curriculum** (19 tracks / 144 sections / 1,029 tutorials / 1,947 chapters / 18,272 lessons, English; ×10 locales) | ✅ **whole** | offline learning content is already available, byte-for-byte |
| **Answer keys** (`correct=`, ranges, `solvedContent`) | ✅ | no server needed to evaluate |
| **Feedback / hints / instructions** | ✅ | no server needed to teach |
| **Renderer assets** (JS/CSS/fonts/icons/editor bundle/bridge) | ✅ mostly | 4,257 external refs need a local mirror |
| **Progress** (per-lesson / chapter / tutorial) | ✅ Room | durable offline; `in_queue` = outbox |
| **UI flags / onboarding stage** | ✅ DataStore | restart/resume locally |
| **Economy / streak / leaderboard / ETA / rewards** | ❌ server | must be replaced by local logic or omitted |
| **Code execution for executable lessons** | ❌ server | must be replaced by a local runner |
| **Auth / profile / social / purchases / AI tutor** | ❌ server + auth | omitted for an offline clone |

⇒ **A faithful offline client is possible without reconstructing any server
business logic.** What is missing is not content but: (a) the exact unlock /
completion thresholds, (b) scoring formulas, (c) the `validatedInput` token
algorithm, (d) a local code runner for 4,024 executable lessons, (e) a mirror
of 4,257 external references, (f) a local substitute for the economy. See
`OPEN_QUESTIONS.md` and `OFFLINE_DEPENDENCY_MATRIX.md`.

## 6. What M05 did **not** do

- No APK/DEX/resource/manifest/signature modification; original APK SHA
  re-verified read-only.
- No DEX re-decoding, no Ghidra re-analysis, no static-inventory rebuild —
  M01/M02 results reused.
- No server reconstruction, no response fabrication, no auth bypass, no test
  account, no purchases, no TLS bypass, no root / private DB extraction.
- No premature implementation: **no new database, no new architecture, no app
  skeleton was built.** Reconstruction only.
- M01–M04 deliverables, `mimo-ui/UPGRADE`, v12.5-fa, ZIP/MANIFEST,
  `verify_upgrade.py` and all previous evidence remain untouched.

## 7. Confidence summary

| Question | Answer | Level |
|---|---|---|
| Is the curriculum inside the APK? | **Yes**, 10,298 JSON files, v753 | `VERIFIED_STATIC` |
| Are answer keys inside the APK? | **Yes**, `correct=`, ranges, `solvedContent` | `VERIFIED_STATIC` |
| Is there a local progress DB? | **Yes**, Room `mimo.db`, 3 tables with exact SQL | `VERIFIED_STATIC` |
| Does the client handle offline? | `handleOfflineState` + `in_queue` exist; **cold start + 3 onboarding steps work with no network** | `VERIFIED_STATIC` (classes) + `VERIFIED_RUNTIME` (42002808217) |
| Does the app run offline end-to-end (lesson → completion)? | **Not observed** | `UNKNOWN` |
| Are scoring formulas known? | **No** | `UNKNOWN` |
| Does the client launch real Mimo? | **Yes** | `VERIFIED_RUNTIME` (M04 `41998643355`, M05 `42001925381`) |
| Any server behaviour confirmed? | **No** | `SERVER CONFIRMED = 0` |

**Cross-references:** `CONTENT_MODEL.md`, `APPLICATION_STATE_MACHINE.md`,
`LEARNING_ENGINE.md`, `OFFLINE_DEPENDENCY_MATRIX.md`, `LOCAL_STORAGE_MODEL.md`,
`NATIVE_LIBRARIES.md`, `DIAGRAMS/`, `EVIDENCE_DATABASE.json`, `OPEN_QUESTIONS.md`.
