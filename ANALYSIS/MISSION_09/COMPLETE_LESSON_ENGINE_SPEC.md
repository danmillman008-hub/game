# MIMO 9.35 — COMPLETE LESSON ENGINE SPECIFICATION

**Document:** `COMPLETE_LESSON_ENGINE_SPEC.md` · **Mission:** MISSION 09 (final reconstruction) · **Branch:** `arena/aebb90b7-game`
**Target APK:** `com.getmimo` 9.35, `versionCode=1792759685`, 142,353,499 B, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` — unchanged.
**SERVER CONFIRMED = 0.** Classification vocabulary: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_ASSET`, `VERIFIED_DATABASE`, `VERIFIED_NETWORK_OBSERVATION`, `INFERRED`, `UNKNOWN`, `SERVER_DEPENDENT`.
Evidence codes resolve in `COMPLETE_EVIDENCE_DATABASE.json` / `COMPLETE_SYSTEM_MAP.json -> evidence_index`.

---


## 0. Lifecycle under specification

```
Lesson Selection -> Lesson Loading -> DSL Parsing -> Renderer -> User Interaction
  -> Validation -> Feedback -> Completion -> Persistence -> Next Lesson
```

Each arrow below is resolved to an original class/method, an evidence class and the
behaviour an independent implementation must reproduce. `SERVER CONFIRMED = 0`.

MISSION 09 runtime run `42077425594`: 691 timeline events. Instrumentation proof: `{"seq": 689, "ts_mono_ms": 284854.774, "ts_utc": "2026-11-05T17:52:13.776Z", "experiment_id": "EXP-M09-005", "action_id": "ACT-0031", "source": "orchestrator", "event": "instrumentation_proof", "server_active": true, "attach_ok": true, "hook_installed_events":`. MainActivity reached: `{"seq": 395, "ts_mono_ms": 186334.805, "ts_utc": "2026-11-05T17:50:35.256Z", "experiment_id": "EXP-M09-001", "action_id": "ACT-0021", "source": "orchestrator", "event": "main_activity_reached", "reached": true, "activity`. Lesson matrix executed: `{"seq": 526, "ts_mono_ms": 258667.306, "ts_utc": "2026-11-05T17:51:47.589Z", "experiment_id": "EXP-M09-003", "action_id": "ACT-0031", "source": "orchestrator", "event": "lesson_entry_result", "reached_chapter": false, "r`.

## 1. Asset schema (VERIFIED_ASSET — 10,298 tutorial files validated)

Root of each tutorial asset: `{"tutorial": {...}}` — **not** a bare tutorial object.
`tutorial` fields: `id, version, type, isNew, codeLanguage, title, descriptionContent,
shortDescriptionContent, showInTrack, iconBanner, chapters`.
`chapter`: `id, title, type, lessons`. `lesson`: `title, id, contentType, images,
interactiveContent, hardModeSelected, hardModeContent, executableContent`.

Measured aggregate from the shipped v753 English curriculum [E23, E24]:

| Content shape | Count |
|---|---|
| `interactive` lessons | 14,248 |
| `executableFiles` lessons | 4,024 |
| `hardModeSelected` | 4,054 |
| `hardModeContent` | 6,058 |
| code languages | html 139, css 169, javascript 283, python 195, sql 64, node 47, jsx 46, swift 43, typescript 23, bash 1 |

`interactiveContent` is an HTML/XML-like DSL string, **not** JSON. Example
(tutorial-904, lesson 151410): `<p>Welcome! ...</p><p>Before you realize it ...</p>`
with `visible-if="always"` on `<img>`. `<code version="2" codelang="html" name="index.html">`
wraps `<content><text value="..."/><text type="break"/></content>`.
`<selection iscode="false" multiple="multiple"><item value="1" correct="true">...</item></selection>`,
`<webview version="2" content="...escaped HTML...">`, `<interaction type="fillTheGap">`,
`<interaction type="validatedInput">`, `<database>` and `<output>` appear in the DSL tag census
[E24, `ANALYSIS/MISSION_05/SAMPLES/`].

`LessonContent$Executable` carries `instructions, preselectedFileIndex, files, hints,
hasVisualOutput, sourceDatabaseTables, solutionDatabaseTables, httpOptions`; each `File`
carries `name, codeLanguage, content, solvedContent` [E09, E24].

## 2. Parser (VERIFIED_RUNTIME + VERIFIED_STATIC)

`Lte/c.b(String)` @14378108 [E25 §N]:

```
parser = XmlPullParserFactory.newInstance()
parser.isNamespaceAware = true
parser.setInput(StringReader(html))
for each START_TAG:
    "p"        -> Lte/d.a    (Paragraph)
    "code"     -> Lte/a.a    (Code block)
    "selection"-> Lte/e.a    (Selection + items)
    "img"      -> Lte/c.a    (Image)
    "webview"  -> Lte/g.a    (Embedded WebView)
    "database" -> Lte/b.a    (SQL database fixture)
    "html"/"body"/unknown -> SKIP (unknown tags dropped)
malformed XML -> []  (measured: M07 stage 4, 21 normalizer/parser cases)
```

`gm.h.a(List)` maps the parsed module list to one of nine `LessonInteractionType`s:
`InteractiveWebView, FillTheGap, Spell, Selection, ValidatedInput, SingleChoice,
MultipleChoice, Reveal, None`. `gm.h.a(nonEmpty)` returned `FillTheGap` in M07 stage 4;
`gm.h.a(empty)` returned `None` (slide) [E05, E25 §P].

**Renderer registry (derived from shipped DSL tags, VERIFIED_ASSET):** the
`COMPLETE_CURRICULUM_GRAPH.json` `rendererFamilies` field classifies every one of the
37,183 lesson placements. Distribution: `fillTheGap` 13,496, `MultipleChoice` 9,837,
`executableFiles` 7,859, `validatedInput` 3,847, `InteractiveWebView` 1,442,
`noninteractiveSlide` 1,079 (counts are placements, not unique lessons).

## 3. Renderer / interaction lifecycle per module family

`base/c.O(LessonContent$Interactive, LessonBundle)` maps ALWAYS-visible modules to render
items `jm/j` (Paragraph), `jm/i` (Image), `jm/k` (Webview) and posts them to LiveData `m`;
CORRECT/WRONG modules are revealed by `c0()`/`d0()` after a run [E09].
`RunButton$State`: `RUN_ENABLED, RUN_DISABLED, SUBMIT_ENABLED, SUBMIT_DISABLED, PROCESSING,
CONTINUE_BIG, CONTINUE_DISABLED, NOT_SHOWN`; `InteractionKeyboardButtonState`:
`ENABLED/DISABLED/HIDDEN` [E05, E10].

| Family | Input event | Validation | Correct feedback | Incorrect feedback | Runtime evidence |
|---|---|---|---|---|---|
| noninteractiveSlide | `Continue` / auto-advance swipe | none | `U()` -> `H(1,1)` | n/a | M07 stage6 `NonInteractiveLessonFragment$goToNextPage$1` (VERIFIED_RUNTIME) |
| InteractiveWebView | JS `window.postMessage({type:'mimo.activity.correct|wrong|completed'})` | inside shipped HTML | `Correct!` / `D O G` / `dog_yawn.png` | `Try again` + disable wrong key | M07 stage5 (VERIFIED_RUNTIME) |
| fillTheGap | tap ordered tokens, Run/Submit | `im/d.E0()` ordered equality | `V()` path (static) | `X()` path (static) | VALIDATOR VERIFIED_RUNTIME; dispatch VERIFIED_STATIC |
| validatedInput | typed text, Run | `qm/i.a` normalizer | `qm/e`->`V()`, `qm/f`->`W()` | `qm/g`->`X()` | normalizer VERIFIED_RUNTIME; dispatch VERIFIED_STATIC |
| Selection / SingleChoice / MultipleChoice | tap options | `km/f.b(List)`: `all{selected==isCorrect}` | `V()` | `X()` | validator VERIFIED_RUNTIME |
| Spell | ordered typed tokens | `pm/b.E0()` | `V()` | `X()` | VERIFIED_STATIC |
| Reveal | Continue | none | reveal CORRECT block | n/a | VERIFIED_STATIC |
| executableFiles | Run / submit code | `q.I()`: `userFiles.content == shipped solvedContent` | advance | `IncorrectSolutionException` | VERIFIED_STATIC |

`Y(Z)` double-run guard: `if runInProgress.value == TRUE return; set TRUE; launch {
if(isCorrect) V() else X(); nextPage.value = lessonBundle.chapterIndex; set FALSE }` [E25 §A].

## 4. Exact validators (pseudocode — from DEX, NOT invented)

```text
# A6 fillTheGap  Lim/d.E0()
selected = state.placedTokens.filter{ it.placed }
ok       = selected.size == state.correctTokens.size &&
           selected.indices.all{ selected[it].text == state.correctTokens[it].text }
answer   = selected.filter{ it.text.isNotBlank() }.joinToString(" ")
baseVM.b0(answer); baseVM.Y(ok)

# A7 selection  Lkm/f.b(List)
return list.all { it.selected == it.isCorrect }

# A8 spell  Lpm/b.E0()
ok = typed.size == expected.size && typed.indices.all{ typed[it].text == expected[it].text }
answer = typed.filter{ it.text.isNotBlank() }.joinToString("")

# A9 validatedInput normalizer  Lqm/i.a(String)
KEEP = ['<','>','(',')',':','{','}',',','.']
lower = s.toLowerCase(Locale.US)
out = "" ; for (c in lower) if (c.isLetterOrDigit() || c in KEEP) out += c
return out

# A10 validatedInput result  setupViews$2.invokeSuspend
if (normalize(user) != normalize(expected)) -> qm/g   (wrong)
else if (user == expected)                 -> qm/e   (exact)
else                                       -> qm/f   (partial)
onValidatedInputExecuted$1: delay(300); qm/e -> V(); qm/f -> W(); qm/g -> X()

# A11 executable  Lq.I()
user   = codeFiles.map{ it.content }
answer = executable.files.map{ it.solvedContent }
return if (user == answer) state else errorState + IncorrectSolutionException

# A5 isSolvedCorrectly  LessonProgress
return tries >= 1
```

**Edge cases:** comparison in fillTheGap/spell is case-sensitive and order-sensitive;
the validatedInput normalizer drops whitespace and all punctuation except `KEEP`;
`ArrayList.equals` in `q.I()` is element-wise and order-sensitive; `isSolvedCorrectly()`
uses `tries`, **not** `attempts`; malformed DSL yields an empty module list (slide).

## 5. Correct / incorrect / retry / attempts semantics

`V()` (correct): `awaitBrowserOutput(); wrongLatch=FALSE; attempts++; updateSolutionFeedback();
tries = wrongLatch?0:1; createLessonProgress(tries, attempts); storeInMemory();
showSolutionFeedbackCorrect(); sound.playCorrect(); analytics.track(...); emitLessonId();
cleanupFiles()` [E25 §B].
`X()` (incorrect): `attempts++; wrongLatch=TRUE; createLessonProgress(0, attempts);
storeInMemory(); showWrongFeedbackBlock()` [E25 §C].

**Important:** an incorrect answer DOES create/update a progress row with `tries=0`
(static), while the measured WebView letter exercise used a different path: M07 stage 5
wrong `Q` produced `Try again` with no new row; correct `D` produced `Correct!` and the
row `151403 | 1793883744787 | 1793883713744 | 1 | 904 | 161 | 219 | 753 | 1 | 0 | 1`
[E06, E07]. Do not generalise one module family's behaviour to another.

`createLessonProgress` sets `completedAt=Instant.now()`, logs when
`completedAt < startedAt`, and builds the 11-field row with `inQueue=true`,
`isPracticeProgress=bundle.B`, `publishSetVersion=tracksRepository.currentPublishSetVersion()`
[E25 §D]. M07 stage 6 measured the full chain:
`c.U()` -> `c.H(1,1)` -> `LessonProgressRepository.createLessonProgress(
LessonBundle(lessonId=151403, lessonIndex=1, chapterId=17742, tutorialId=904, trackId=219,
tutorialTitle=Discovering HTML and Tags))` -> `LessonProgress(tries=1, attempts=1,
isPracticeProgress=false, inQueue=true, publishSetVersion=753)` -> `c.e0()` ->
`LessonProgressQueue.storeLessonProgress` -> `isSolvedCorrectly()=true` ->
`c.f0(false,true)` (analytics, **not XP**) -> `c.N()` [E06].

**Negative result preserved:** no `V()/W()/X()`, `d0()`, `onLessonRun$1`,
`jm/m|n|o`, native selection submit or WebView JS-interface event fired in M07 stage 6
or M08/M09; those dispatch paths remain `VERIFIED_STATIC` only [E06, E12, E29].

## 6. WebView / JavaScript-to-native bridge (VERIFIED_ASSET + UNKNOWN boundary)

`assets/lesson-webview.js` (8,189 B, SHA `665ee4cbf...`) is injected into interactive WebView
lessons. It defines `MimoLesson.postMessage(JSON.stringify({documentID, ...payload}))` and
posts exactly five `kind`s [E33]:

| kind | payload | Purpose |
|---|---|---|
| `gesture` | `decision: 'web'|'lesson'|'ready'`, `startedAt` | pointer/touch ownership arbitration between lesson pager and Web content |
| `activity` | `result: 'mimo.activity.correct'|'mimo.activity.wrong'|'mimo.activity.completed'` | relays in-page `window.postMessage` activity results |
| `focus` | `focused: Boolean` | input/textarea/contentEditable focus state |
| `height` | `height: Integer` | body measurement via ResizeObserver / MutationObserver |
| (ready) | `gesture.decision='ready'` sent once at init | signals bridge ready |

Template placeholders: `__MIMO_DOCUMENT_ID__`, `__MIMO_TOUCH_SLOP_CSS_PX__`,
`__MIMO_FONT_SCRIPT__`. In-page activities emit `window.postMessage({type:'mimo.activity.*'})`;
the relay only forwards events whose `event.source === window`. Shipped WebView letter
exercise 151403 uses `correctLetter='D'` and renders `Correct! / D O G / dog_yawn.png`
on D, `Try again` otherwise [E18].

**Native side is UNKNOWN:** `WebView.addJavascriptInterface` was hooked in M07 stage 6 and
produced **zero** events; the JS interface object class, method names, payload schema,
native callbacks, error handling and retry signals were not observed. M09 added
`WebView.loadUrl/loadDataWithBaseURL/evaluateJavascript/postUrl` and
`WebViewClient.shouldOverrideUrlLoading` hooks to capture the bridge in a real lesson;
result is recorded in `COMPLETE_RUNTIME_TIMELINE.jsonl` (`webview` events). No payload is
invented here. Closure condition: `FINAL_UNKNOWN_REGISTER.md -> U-WEB-001`.

## 7. Code editor / executable lessons (VERIFIED_STATIC + UNKNOWN boundary)

`CodeEditViewModel`, `CodeDiffViewModel`, `CodePlaygroundActivity`, syntax highlighter
(`highlight.min.js`, `prettier/standalone.js`, `spieglein/editor.bundle.js`) and an input
console are shipped. Offline validation is `q.I()` comparing user file contents to shipped
`solvedContent`. `POST /v1/code/runfiles` exists in the endpoint list [E04]; whether a given
lesson executes locally, remotely, or in a sandbox, and how console output/errors return,
was **not measured**. M07 stage 3 reached a WebView JavaScript snippet lesson but could not
establish the execution boundary [E10, E26]. Classification:
`VERIFIED_STATIC` (offline comparison, editor assets) + `SERVER_DEPENDENT`/`UNKNOWN`
(remote runner).

## 8. Independent implementation pseudocode

```text
function runLesson(lesson, bundle, store):
    modules = parseDSL(lesson.interactiveContent)      # A15
    family  = selectInteractionType(modules)           # A16
    render(family, modules)
    on Submit(input):
        if runInProgress: return
        runInProgress = true
        ok = validate(family, input, lesson)           # A6..A11 registry
        if ok: showCorrectFeedback() else showWrongFeedback()
        attempts += 1
        tries = ok ? 1 : 0
        progress = createLessonProgress(bundle, tries, attempts, now(), inQueue=true)
        store.upsert(progress)
        updateCorrectAnswersCount()                    # A12: AnswersInChapter
        nextPage = bundle.chapterIndex
        runInProgress = false
    on Continue / autoAdvance:
        # noninteractive slides can complete without an explicit answer
        createLessonProgress(bundle, 1, 1, now(), inQueue=true)
        advanceTo(nextLessonInChapter(bundle))
```


---

## MISSION 09 runtime addendum (`VERIFIED_RUNTIME`, run `42077425594`)

The MISSION 09 controlled run succeeded where M08 failed: the API-36 `Java.registerClass`
lifecycle hook was replaced with **direct** `android.app.Activity` / `Fragment` /
`WebView` hooks, giving `server_active=true`, `attach_ok=true` (pid 3348, process `Mimo`),
**181 hooks installed, 72 real `com.getmimo` method `entry` events**, 71 `exit`,
86 SQL, 17 DI, 19 LiveData and 28 lifecycle `nav` events. `real_target_method_executed=true`.
All three user-required instrumentation conditions are therefore met [E29, E30].

`SERVER CONFIRMED = 0`. Instrumentation success is not a claim that every screen was
reached: the fixed 20-tap onboarding chain stalled at step 4 on this build, so
`MainActivity` was reached with an explicit intent; the lesson answer matrix was
**not executed** (`lesson_matrix_not_executed`, `ChapterActivity` not reached) and the
resulting three route screens resumed an incomplete `OnboardingActivity` back stack.
See `FINAL_UNKNOWN_REGISTER.md` and `FINAL_TEST_MATRIX.json` for the honest limitations.

### M09 runtime outcome for the answer matrix

The M09 lesson-entry experiment recorded `lesson_entry_result.reached_chapter=false` and
`lesson_matrix_not_executed` (`ChapterActivity not reached`), so **no new wrong/correct/
retry/Continue/FTG runtime event was produced in M09** and no answer was guessed. The
authoritative runtime matrix remains M07 stage 5 (wrong `Q` -> `Try again`; correct `D` ->
`Correct!`, `D O G`, `dog_yawn.png`) and stage 6 (`U()->H(1,1)->createLessonProgress->
Queue->f0(false,true)->N()`), which are already `VERIFIED_RUNTIME` [E06, E07].
M09 added 5 WebView hooks but recorded **0 `webview` events** for the same reason;
`U-WEB-001` remains open. Static validator dispatch (`V/W/X`, `jm/m|n|o`, `d0`) remains
`VERIFIED_STATIC` only (`U-LESSON-001`).
