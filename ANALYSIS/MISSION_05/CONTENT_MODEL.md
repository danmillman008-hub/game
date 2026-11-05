# CONTENT_MODEL — Mimo 9.35 shipped learning content, reconstructed from the original APK

**Status legend (mandatory, used on every finding):**
`VERIFIED_STATIC` = read directly out of the original APK / DEX / JADX / asset bytes ·
`VERIFIED_RUNTIME` = observed on the running app (emulator PNG/XML/logcat) ·
`VERIFIED_BOTH` · `INFERRED` = argued from verified facts, never promoted · `UNKNOWN`.

`APK SHA-256 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` ·
`com.getmimo` 9.35 / `1792759685` · branch `arena/aebb90b7-game`.

---

## 1. The single most important fact — `VERIFIED_STATIC`

> **The complete curriculum is packaged inside the APK.** No network request is
> needed to obtain tracks, tutorials, chapters, lessons, exercises, correct answers,
> hints, feedback text, or solved code.

`assets/` holds **10,564** files; **10,298** of them are tutorial JSON files under
`assets/lessons-<locale>/tracks/`, i.e. ~1,030 per locale × 10 locales.
English alone: 1,030 files, 57,274,569 bytes uncompressed (9,781,687 B deflated).
`assets/lessons-en/tracks/tracks.json` is the root index (`publishSetVersion: 753`).
Locales (`ContentLocale` enum, `VERIFIED_STATIC`):
`RU EN ES PT DE FR IT ID TR PL`. Supporting assets shipped:
`lessons-common/icons/` (215), `lesson-webview.js`, `lesson-webview-fonts.js`,
`highlight.min.js`, `beautify/*.js`, `prettier/*.js`, `snippets/*-snippets.json`,
`spieglein/editor.bundle.js` (2,369,375 B) + `spieglein/index.html`,
`styles/mimo_code_style*.css`, `testdata/*` (fixtures).

**New in M05:** M01/M02 counted these files (`MIMO_CONTENT_SCHEMA.json`) but did not
open the lesson payloads. This document reconstructs the *actual* object graph and
the answer-validation contract from the shipped bytes.

**Evidence:** `SCHEMAS/SHIPPED_CONTENT_STATS.json`, `SAMPLES/`, `EVIDENCE/ASSET_MANIFEST.txt`,
`ANALYSIS/MIMO_CONTENT_SCHEMA.json` (prior counts), `ANALYSIS/APK_COMPLETE_INVENTORY.json`.

---

## 2. Object graph — `VERIFIED_STATIC` (asset JSON) + `VERIFIED_STATIC` (JADX classes)

```
TracksJson { publishSetVersion: Long, tracks: List<TrackJson> }
  TrackJson { id, version, title, descriptionContent, onboardingCategory,
              isNew, isHidden, iconBanner, sections: List<SectionJson>,
              tutorials: List<{id,version,type,title}> }
    SectionJson { name, description, startIndex, endIndex, tutorialIds: List<Long> }
    TutorialJson (one file per id) { tutorial: {...} }
      Tutorial { id, version, type, isNew, codeLanguage, title,
                 descriptionContent, shortDescriptionContent, showInTrack,
                 iconBanner, chapters: List<Chapter> }
        Chapter { id, title, type, lessons: List<Lesson> }
          Lesson { id, title, contentType, images,
                   interactiveContent | executableContent,
                   hardModeSelected?, hardModeContent? }
```

Measured on English v753 (`VERIFIED_STATIC`, full recompute in
`SCHEMAS/SHIPPED_CONTENT_STATS.json`):

| Level | Count | Notes |
|---|---:|---|
| `TracksJson.publishSetVersion` | `753` | `long` in `TracksJson.java` |
| tracks | **19** | `onboardingCategory`: `build` 3, `none` 16 |
| sections | **144** | all 144 satisfy `endIndex − startIndex + 1 == tutorialIds.size()` |
| `tutorials[]` refs in tracks | **2,002** | refs are `{id,version,type,title}` — the *body* lives in a separate file |
| tutorial JSON files | **1,029** | 1,029 unique ids; 2,002 refs ⇒ tutorials are reused across tracks/sections |
| chapters | **1,947** | |
| lessons | **18,272** | 18,272 unique lesson ids, 0 duplicates |
| `images[]` entries | 135 | most lessons have `images: []` |

**JADX class correspondence** (`VERIFIED_STATIC`,
`ANALYSIS/DECOMPILED/getmimo_sources.tar.gz`, extracted field lists in
`SCHEMAS/JADX_MODEL_FIELDS.json`):

| Java class | Fields (as decompiled) |
|---|---|
| `…data/content/model/track/TracksJson` | `long publishSetVersion; List<TrackJson> tracks` |
| `TrackJson` | `descriptionContent, iconBanner, id, isHidden, isNew, sections, title, version` |
| `SectionJson` | `description, endIndex, name, startIndex, tutorialIds` |
| `Track` (runtime model) | adds `List<Tutorial> tutorials`, `g hasProgress` per `Section` |
| `Section` (runtime model) | `description, hasProgress, index, name, List<Tutorial> tutorials` |
| `TutorialJson` | `Tutorial tutorial` (single-key wrapper — confirmed by reading the files) |
| `Tutorial` | `chapters, codeLanguage, hasProgress, iconBanner, id, isCompleted, showInTrack, title, type, version` |
| `Chapter` | `id, isCompleted, lessons, title, type` |
| `Lesson` | `contentType, hardModeSelected, id, images, title` |
| `LessonContent.Interactive` | `List<LessonModule> lessonModules, hardModeLessonModules` |
| `LessonContent.Executable` | `String instructions; int preselectedFileIndex; List<File> files` |
| `LessonContent.Executable.File` | `CodeLanguage codeLanguage; String content, name, solvedContent` |
| `LessonImage` | `String id` |
| `LessonIdentifier` | `chapterId, lessonId, trackId, trackVersion, tutorialId` |
| `ChapterIdentifier` | `chapterId, trackId, tutorialId` |
| `TrackIdentifier` | `trackId, trackVersion` |
| `TrackEta` | `currentPaceMinutesPerDay, sectionEstimatedCompletionByIndex, trackEstimatedCompletionAt` |

**Key architectural point — `VERIFIED_STATIC`:** the JSON DTOs (`*Json`) are the
*shipped* serialization; the runtime models (`Track`, `Section`, `Tutorial`, `Chapter`)
carry **derived state** (`hasProgress`, `isCompleted`, `index`) merged in by the
loader. This is where local persistence meets the shipped content — see
`LOCAL_STORAGE_MODEL.md`.

---

## 3. Sequencing, prerequisites and node types — `VERIFIED_STATIC` + `INFERRED`

- **Sequencing is positional, `VERIFIED_STATIC`:** `SectionJson.startIndex`/`endIndex`
  index into the track's flat node sequence; `tutorialIds` is an ordered list.
  In all 144 sections the length equals the inclusive index span, so there are no
  holes. Chapter → lesson order is array order in the JSON.
- **Node types — `VERIFIED_STATIC` (`TutorialType` enum values vs shipped counts):**
  `course 507`, `practiceRequired 157`, `practiceOptional 134`,
  `guidedProjectOptional 117`, `guidedProject 74`, `challenges 40`.
  Also declared in the enum but **not present** in v753 English data:
  `mobileProject`, `quiz`, `proficiencyProject`, `recreateProject`.
  `TutorialType` exposes `isRequired`, `isPractice`, `isChallenge`, `trackingField`.
- **Chapter types — `VERIFIED_STATIC`:** `practiceLevel1 810`, `practiceLevel3 522`,
  `challengeLevel2 382`, `practiceLevel2 174`, `challengeLevel0 45`,
  `challengeLevel1 14`. `ChapterType` enum also declares `none`, `quiz`,
  `challengeLevel3`, `challengeLevel4` (absent in v753 data).
  `ChapterType` exposes `level` / `isChallengeLevel`.
- **Locked/unlocked & prerequisite rule — `INFERRED` (deliberately not promoted):**
  shipped JSON has **no** `prerequisiteId`, `locked`, `unlockAfter` or `order`
  field. Unlock state is therefore computed by the client from
  `chapter_completions` / `tutorial_completions` plus `TutorialType.isRequired`,
  `Section.hasProgress`, `Tutorial.isCompleted`, `Chapter.isCompleted`.
  The precise mapping (`GetPathMapState$invoke$3` in M02: `isCompleted`,
  `isRequired`, `getType` → `locked/available/completed`) remains `UNKNOWN`
  and is listed in `OPEN_QUESTIONS.md` (#1).
- **Hard mode — `VERIFIED_STATIC`:** 6,058 lessons carry an alternate
  `hardModeContent` DSL body and 4,054 carry `hardModeSelected: true`.
  `InteractiveLessonBaseViewModel` has `setupHardModeState` and
  `DataStoreUserPreferences` has `setHardModeEnabled`,
  `markChapterCompletedInHardMode`, `observeCompletedHardModeChapters`.
  So a lesson has **two local renderings**; the hard variant is not fetched.

---

## 4. Lesson content representation — `VERIFIED_STATIC`

`contentType` (enum `LessonContentType`, values `interactive` / `executableFiles`):

| contentType | lessons | payload field |
|---|---:|---|
| `interactive` | **14,248** | `interactiveContent`: an HTML-like XML/DSL **string** |
| `executableFiles` | **4,024** | `executableContent`: a JSON **object** |

### 4.1 Interactive DSL

Every `interactiveContent` is a string beginning `<!DOCTYPE html ><html><body>…`.
Tag/attribute frequencies over all 18,272 lessons (`VERIFIED_STATIC`,
`SCHEMAS/SHIPPED_CONTENT_STATS.json`):

| Tag | count | Role (`VERIFIED_STATIC` where literals exist; else `INFERRED`) |
|---:|---:|---|
| `text` | 369,108 | tokenised source-code character runs with `value=`, `class=`, `type="break"` |
| `code` | 94,981 | a code block (`version="2"`, `codelang=`, `name=`, `visible-if=`) |
| `p` | 46,388 | prose paragraph |
| `option` | 44,225 | answer option (`correct=`, or `startIndex/endIndex`) |
| `content` | 41,221 | container of `<text>` tokens / expected `<output>` |
| `interactions` / `interaction` | 11,729 each | exercise definition |
| `data` | 10,474 | tabular data |
| `options` | 9,957 | container for `<option>` |
| `selection` | 7,356 | multiple-choice exercise (`iscode=`, `multiple=`) with `<item correct=…>` |
| `output` | 5,784 | expected console/table output |
| `row`, `table`, `tables`, `database` | 5,232 / 1,301 / 574 / 574 | SQL result rendering |
| `webview` | 930 | embedded HTML (`version="2"`, `visible-if=`, `content=` escaped HTML) |
| `item` | 20,249 | `<selection>` choice and `<data>` row cells |
| `img`, `link`, `script`, `head`, `title`, … | 1,533 / 1,877 / 819 / 1,834 / 645 | standard HTML payload |

Attributes (`VERIFIED_STATIC`): `visible-if` = `always 18,869`, `wrong 19,101`,
`correct 173`; `correct` on `<option>/<item>` = `true 7,356`, `false 27,762`;
`webview version="2"` 926; `code version="2"` 22,034; `isDefault="true"`;
`startIndex`/`endIndex` integer ranges into the `<content>` token stream;
`codelang`, `name` (`index.html 5,154`, `script.js 4,174`, `script.py 3,155`,
`style.css 2,263`, `index.jsx 1,337`, `App.jsx 795`, `script.sql 694`,
`main.swift 643`, `app.js 549`, `script.ts 243`, `script.sh 186`).

**Parser classes — `VERIFIED_STATIC`** (`com.getmimo.data.content.lessonparser.interactive`):
`ParserModule`, `model/LessonModule` (subclasses `Code`, …),
`model/Interaction` (subclasses `FillTheGap`, `Selection`, …),
`model/Option`, `model/SelectionItem`, `model/Output` (`ConsoleOutput`, `TableOutput`),
`model/Table`, `model/ModuleVisibility`, `model/Attribute`, `model/AttributeType`,
`model/Tag`, `model/WebviewType`, `model/CollapsibleLine`,
`textstyle/CustomTypefaceSpan`.
`LessonModule.Code` fields: `CharSequence` text, `List` interactions,
`Output`, `ModuleVisibility`, `CodeLanguage`, `String name`, `List` lines.
`Option` fields: `boolean`, `CharSequence`, `int`, `int` ⇒
`(correct, content, startIndex, endIndex)`.
`SelectionItem`: `(CharSequence, boolean)`.

### 4.2 Exercise types — `VERIFIED_STATIC`

`<interaction type=…>` in shipped v753: **`fillTheGap` 9,957**, **`validatedInput` 1,772**.
Additionally the standalone `<selection>` quiz tag: **7,356** occurrences.
`LessonInteractionType` enum declares `FillTheGap`, `Spell`, `Selection`,
`ValidatedInput`, `InteractiveWebView`, `MultipleChoice`, `SingleChoice`,
`Reveal`, `None`; corresponding UI packages exist for
`fillthegap`, `spell`, `selection`, `validatedinput`, `webview`, `nointeraction`.
The **v52 test fixture** (`assets/testdata/test-tracks.json`, `test-tutorial.json`,
`127-0-1.html`) additionally uses `interaction type="spell"`; v753 English does not.

### 4.3 Answer validation and feedback — `VERIFIED_STATIC` (the decisive finding)

**Correctness is data inside the shipped asset, not a server decision.**

1. **Multiple choice** — `<selection><item value="1" correct="true">…</item>
   <item value="2" correct="false">…</item></selection>`.
   The answer key is the `correct` attribute; 7,356 true / 27,762 false values.
   `SAMPLES/selection_lesson.txt`, `SAMPLES/testdata_127-0-1.html`.
2. **Fill the gap** — `<interaction type="fillTheGap"><options>
   <option startIndex="70" endIndex="78"/> … <option correct="false"><content>
   <text value="&lt;p&gt;"/></content></option></options></interaction>`.
   Correct tokens are `[startIndex,endIndex)` ranges into the lesson's own
   `<content>`; distractors are literal `<option correct="false">`.
   `SAMPLES/fillthegap_lesson.txt`.
3. **Validated input** — `<interaction type="validatedInput" isDefault="true"
   startIndex="108" endIndex="113"/>` with no `correct` attribute and no explicit
   answer string. The `<content>` already contains the full correct code
   (`…<button>Login</button>…`); range `[108,113)` resolves to `Login`
   (`SAMPLES/validatedinput_lesson.txt`, verified locally by reconstructing the
   `<text>` stream). **Classification: `INFERRED` for the general rule** — the
   substring check is confirmed on this example but some ranges do not align with
   a naive `<text>` reconstruction (other `<content>` blocks / token offsets).
   The exact renderer/index semantics remain `UNKNOWN` (`OPEN_QUESTIONS.md` #4).
4. **Feedback** — `visible-if="correct" | "wrong" | "always"` selects which
   `<p>`/`<code>`/`<webview>` modules are shown. A wrong answer reveals a
   shipped remediation paragraph (e.g. `Make sure to type <code>Login</code>.`).
   `InteractiveLessonBaseViewModel` has `showWrongFeedbackBlock$1`,
   `lessonSolvedIncorrectly$1`, `lessonSolvedCorrectly$1`,
   `lessonSolvedCorrectlyWithPartialMatch$1`,
   `lessonSolvedAndProceedToNextLesson$1`.
5. **Embedded interactive webviews** — `assets/lesson-webview.js` (`VERIFIED_STATIC`,
   full copy in `SAMPLES/lesson-webview.js`) installs a JS↔native bridge
   `MimoLesson.postMessage(JSON.stringify({documentID, ...payload}))` and listens for
   `window.postMessage({type: 'mimo.activity.correct' | 'mimo.activity.wrong' |
   'mimo.activity.completed'})`, forwarding them as `{kind:'activity', result}`.
   The DEX string table contains all three literals at offsets
   `0x3459A3` (`mimo.activity.completed` @3,432,650),
   `0x345A63` (`mimo.activity.correct` @3,432,675),
   `0x345A7A` (`mimo.activity.wrong` @3,432,698) in `classes.dex`.
   Shipped content uses them in **217 / 217 / 90** lesson bodies respectively.
   The same bridge also reports `{kind:'gesture'|'focus'|'height'|'ready'}`
   for swipe ownership, input focus and dynamic WebView height.
   ⇒ **Exercise correctness is decided in the WebView JS and reported to the
   native client, entirely on-device.** `VERIFIED_STATIC`.
6. **Executable lessons** — `executableContent` keys (`VERIFIED_STATIC`, 4,024 each):
   `instructions`, `preselectedFileIndex`, `hasVisualOutput`, `files`, `hints`;
   optional `sourceDatabaseTables` (269), `solutionDatabaseTables` (269),
   `httpOptions` (85). `files[]` = `{name, codeLanguage, content, solvedContent}` —
   **`solvedContent` is the expected solved source and is shipped locally**.
   `ExecuteFilesResponse` / `ExecuteLessonResponse` carry `hasPassed`, `tests[]`,
   `consoleOutput`, `error`, `hostedProjectUrl`; Retrofit endpoints
   `POST /v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles`
   and `POST /v1/code/runfiles` exist ⇒ **code execution / automated test
   checking is a server round-trip** for this lesson type, while the exercise
   *content, hints and the reference solution* are local.
   Offline implication: see `OFFLINE_DEPENDENCY_MATRIX.md`.
   `SAMPLES/executable_lesson.json`.

### 4.4 Completion conditions — `VERIFIED_STATIC` (local) / `INFERRED` (aggregation)

- Per-lesson: `LessonProgress.isSolvedCorrectly()` is `attempts >= 1`
  (M02: `intField >= 1`); `tries`, `attempts`, `startedAt`, `completedAt` are
  recorded in Room `lesson_progress` with `in_queue` for later sync.
- Per-chapter: `ChapterCompletion` row `(chapter_id, created_at, track_id,
  tutorial_id)`; SQL `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions`.
- Per-tutorial: `TutorialCompletion` row `(tutorial_id, is_completed, updated_at,
  track_id)`.
- **Exact threshold** that flips a chapter/tutorial to completed is `UNKNOWN`
  (M02 gap #7); the SQL and the entity show only that a chapter-completion row
  is written when a chapter finishes.

---

## 5. Shipped vs dynamically supplied — `VERIFIED_STATIC` (endpoints) / `INFERRED` (ownership)

| Data | Where it lives | Classification |
|---|---|---|
| Tracks / sections / tutorials / chapters / lessons | `assets/lessons-*/tracks/*.json` | `VERIFIED_STATIC` — **fully offline** |
| Exercise answer keys, distractors, hints, feedback, solved code | same assets | `VERIFIED_STATIC` — **fully offline** |
| Icons, fonts, syntax highlighter, code editor bundle, WebView bridge JS | `assets/` | `VERIFIED_STATIC` — **fully offline** |
| `hasProgress`, `isCompleted`, `index` | merged at load time from Room | `VERIFIED_STATIC` (class fields) + `INFERRED` (merge point) |
| `publishSetVersion` | shipped `tracks.json` = 753 | `VERIFIED_STATIC` |
| Track ETA / completion / last-interacted | `GET /v1/tracks/{trackId}/eta`, `/completion`, `/completion/lastInteracted` | `VERIFIED_STATIC` (endpoints) — **server** |
| Favourite tracks | `GET/POST /v1/user/favorites/tracks` + local `FavoriteTracks` | both |
| Saved code / user files for executable lessons | `GET/POST /v1/.../savefiles`, `/savedFiles`, `/v1/code` | **server** |
| Code execution results / tests | `POST /v1/.../runFiles`, `/v1/code/runfiles` | **server** |
| XP, sparks, coins, keys, streak, daily goal, leaderboard, rewards | `/v1/user/*`, `/v1/leaderboards/*`, `/v2/client-config` | **server** |
| Remote config / A-B tests / paywalls | `GET /v2/client-config`, `remote_config.json`, Firebase Remote Config | **server / remote config** |
| Lesson report / drafts rendering | `POST /v1/tutorials/{id}/lessons/{id}/report`, `GET /v1/tutorials/drafts/.../render` | **server** |
| AI tutor | `/v1/aiTutor/...` | **server** |
| Authentication / account / profile / social | `/v1/account/*`, `/v1/users/*`, `/v1/user/*` | **server + auth** |

**External references inside lesson bodies — `VERIFIED_STATIC`:** 4,257
`http(s)://` occurrences across ~60 hosts. Top:
`mimo.app 2,282` (CDN images, e.g. `https://mimo.app/i/dan.png`),
`mimo.org 365`, `www.w3.org 224`, `fonts.googleapis.com 180`,
`pokedex.mimo.dev 132`, `example.com 124`, `cdnjs.cloudflare.com 90`,
`swapi.mimo.dev 90`, `things.mimo.dev 57`, `rickandmortyapi.com 53`,
`unpkg.com 52`, `localhost 49`, `cdn.jsdelivr.net 45`, `fonts.gstatic.com 42`.
These are **displayed demo assets / exercise APIs**, not curriculum metadata;
they are the main offline fidelity gap. Full list in
`SCHEMAS/SHIPPED_CONTENT_STATS.json → external_url_domains`.

---

## 6. Loader path — `VERIFIED_STATIC`

`classes.dex` string literals (offsets from `classes.dex`):

| Offset | Literal |
|---|---|
| `2,130,911` | `/tracks.json` |
| `2,130,925` | `/tutorial-` |
| `2,129,523` | `.json` |
| `3,326,905` | `lessons-` |
| `3,326,883` | `file:///android_asset/lessons-common/icons` |
| `3,432,650 / 3,432,675 / 3,432,698` | `mimo.activity.completed / correct / wrong` |
| `2,183,344` | `CREATE TABLE IF NOT EXISTS \`lesson_progress\`…` |
| `3,550,076` | `user_preferences` |
| `3,432,719` | `mimo.db` |
| `classes2.dex 8,586,633 / 8,586,649` | `%s[0-9]+.json$`, `^(%s\|%s\|%s)[0-9]+.json$` |

Classes: `com.getmimo.data.content.tracks.DefaultTrackLoader`
(`getAllTracks`, `getTutorial`, `getInteractiveLesson`, `getExecutableLesson`),
`DefaultTracksRepository` (`getTracksJson`, `getTrackById`,
`getTrackWithChapters`, `loadTrackWithChapters`, `getPublishSetVersion`),
`ContentLocale.fromLocale/toLocale`, `userContentLocaleProvider`.
⇒ Path construction is `lessons-<locale>/tracks/tracks.json` and
`lessons-<locale>/tracks/tutorial-<id>.json`. `VERIFIED_STATIC`.

All offsets above are byte offsets of the first literal match in the DEX file; full list in `EVIDENCE/DEX_STRING_OFFSETS.txt`.

---

## 7. What is still `UNKNOWN` here

- Exact `validatedInput`/`fillTheGap` index → token-stream algorithm
  (parser bytecode not decompiled; `INFERRED` on one confirmed example).
- Exact chapter/tutorial completion threshold and unlock rule.
- Whether `solvedContent` is used locally for code-diff validation or only for
  display (there is a `ui/lesson/executable/codediff` package — `INFERRED`).
- Behaviour of `spell`/`Reveal`/`MultipleChoice` in shipped v753 (declared in
  enums, absent from English data — may appear in other locales).
- Content-update mechanism: how a newer `publishSetVersion` reaches the client
  (no endpoint named for it in the 53 Retrofit definitions).

---

**Evidence files:** `SCHEMAS/SHIPPED_CONTENT_STATS.json`,
`SCHEMAS/JADX_MODEL_FIELDS.json`, `SAMPLES/*`, `EVIDENCE/*`,
`ANALYSIS/MIMO_CONTENT_SCHEMA.json`, `ANALYSIS/MIMO_COMPLETION_ENGINE.json`,
`ANALYSIS/MIMO_RETROFIT_ENDPOINTS.json`, `ANALYSIS/DECOMPILED/getmimo_sources.tar.gz`.
