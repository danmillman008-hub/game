# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**Target:** original Mimo Android 9.35 APK, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Branch:** `arena/aebb90b7-game`, baseline `d0714b40`  
**Toolchain:** Androguard 4.1.4 in `/home/user/_work/m06/venv` over all 12 original
`ANALYSIS/_INPUT/classes*.dex`; patched read-only harness `EVIDENCE/M06_DEX_HARNESS.py`.  
`SERVER CONFIRMED = 0`. Backend services, server business logic, server databases and cloud
infrastructure are **not** reconstructed; only client-side boundaries are recorded.

> Every finding is classified `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_BOTH`,
> `INFERRED` or `UNKNOWN`. Evidence fields (APK path, class/method, DEX file + code offset,
> bytecode/Smali, caller/callee, SQL, runtime log, reproduction steps) are given inline or in
> the referenced `EVIDENCE/`, `SCHEMAS/`, `CALL_GRAPHS/`, `METHOD_DOSSIERS/` artefacts.

---

## Layered architecture — VERIFIED_STATIC + INFERRED
`DIAGRAMS/01_full_architecture.mmd`, `02_class_dependency.mmd`.

### 1. Process entry (M01/M02/M04 evidence, VERIFIED_RUNTIME)
`com.getmimo`, `versionName=9.35`, `versionCode=1792759685`, `primaryCpuAbi=arm64-v8a`.
Launcher: `.ui.SplashActivity_default` → `.ui.onboarding.intro.IntroSlidesActivity`
(M04 run `41998643355`).
`Lcom/getmimo/ui/SplashActivity;` (2 inner-class votes) → `Lcom/getmimo/ui/a;`
`SplashViewModel`; `MainActivity` (14 votes) → `Lcom/getmimo/ui/main/d;` `MainViewModel`
(35 votes).

### 2. Content layer (M06, VERIFIED_STATIC)
`Lye/b;` assets loader; `Lye/d;` filesDir loader; `tracks/b; DefaultTrackLoader`;
`tracks/c; DefaultTracksRepository`; `Lte/c;` DSL parser; `Lgm/h;` interaction mapper.
Detailed in `05_CONTENT_PIPELINE.md` and dossiers 11–14.

### 3. Domain / interactors (M06, VERIFIED_STATIC)
`interactors/path/d; GetPathMapState`, `path/c; GetPathMapDialogs`,
`chapter/a; CanOpenChapterWithKeys`, `chapter/b; CreateChapterEndScreens`,
`chapter/c; GetLessonType`, `chapter/d; GetChapterEndSuccessState`,
`chapterend/a; GetChapterEndProgressWithEtaScreenData`, `eta/a; GetTrackEta`,
`practice/c; GetPracticeTrackList`, `lesson/b;`, `lesson/CreateBrowserOutput`,
`streak/b; ObserveUserStreakInfoCache`, `aitutor/a; GetAiTutorFreemiumUsage`,
`publicprofile/a; GetPublicCodePlaygrounds`.
These are plain Kotlin use-case classes with `invoke`/`a(…, Continuation)` suspend methods —
not a separate framework. `INFERRED` from naming and constructor injection shape.

### 4. UI layer (VERIFIED_STATIC)
Mix of **Fragments + Android ViewModel/LiveData** and **Jetpack Compose + Orbit MVI**:
- `base/b; InteractiveLessonBaseFragment` + `base/c; InteractiveLessonBaseViewModel`
  (LiveData `m0`, `kotlinx.coroutines.flow.i`).
- `executable/q; ExecutableLessonViewModel` uses `org.orbitmvi.orbit` container with state
  `Lzl/z;`.
- `ui/path/map/j; PathMapViewModel` (15 votes), `ui/path/map/a; PathMapFragment`.
- `ChapterActivity` (16 votes), `ChapterViewModel` (15), `ChapterFinishedFragment`/`ViewModel`.
- `Ui/lesson/interactive/*` per-interaction fragments + viewmodels.

### 5. Persistence (VERIFIED_STATIC)
Room (269 tables per M05; DAO `Lcg/a;`), `LessonProgressQueue`,
`CompletionRepository`, `data/local/a; DataStoreUserPreferences`, SharedPreferences keys,
in-memory `LiveData`/`StateFlow`, `LessonProgressRepository` unsynced queue.
See `11_LOCAL_PERSISTENCE.md`.

### 6. DI — VERIFIED_STATIC, framework `INFERRED`
ViewModels receive a hand-rolled 13-slot container `Lhm/b;` (`a`..`m` all
`Ljava/lang/Object;`), cast at each use site:
`b.d → LessonProgressRepository`, `b.b → analytics/a`, `b.g → data/local/a`,
`b.h → mf/a filesDir`, `b.i → lesson/sound/a`. Larger constructors (e.g. `q` has 32
parameters) indicate constructor injection assembled by a DI graph (Hilt/Dagger or Koin);
the exact framework is `UNKNOWN` — no annotation processor output was decoded.

### 7. Events / callbacks / workers (VERIFIED_STATIC)
`RunButton$State`, `InteractionKeyboardButtonState`, `Lym/f` interaction events,
`mimo.activity.*` WebView bridge messages, `Lqm/b` text watcher, `LessonProgressQueue`
StateFlow, WorkManager workers (`PostVisitWorker`, `StreakWidgetRefreshWorker`,
`AccountDeleteWork`, `AsyncRequestWorker` for glance). Native callbacks via JNI — see
`14_NATIVE_LIBRARIES_AND_JNI.md`.

### Component responsibility table
| Component | Responsibility | Inputs | Outputs / state changes |
|---|---|---|---|
| `Lye/b` | asset stream lookup by locale | `ContentLocale`, id | `InputStream` |
| `tracks/b` | UTF-8 read + JSON decode | stream | `JsonObject` |
| `Lte/c` | XML DSL → modules | HTML string | `ArrayList<LessonModule>` |
| `Lgm/h` | renderer selection | modules | `LessonInteractionType` |
| `base/c` | lesson session state machine | input events | LiveData, `LessonProgress`, Room |
| `LessonProgressQueue` | answer counting + sync | `LessonProgress` | `AnswersInChapter`, Room rows |
| `GetPathMapState` | unlock/completion state | Track + completions + keys + tier | `Lvn/n` |
| `NetworkUtils` | connectivity gate | `ConnectivityManager` | Boolean |
