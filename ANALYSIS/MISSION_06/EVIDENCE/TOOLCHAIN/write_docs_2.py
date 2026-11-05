import pathlib
D=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06')
APK='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
PRE=f'''# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `{APK}` (unchanged) · **branch** `arena/aebb90b7-game` · `SERVER CONFIRMED = 0`  
Evidence: `EVIDENCE/DISASM/*.smali.txt`, `SCHEMAS/METHOD_CATALOG_MIMO.json`,
`CALL_GRAPHS/*.json`, `METHOD_DOSSIERS/*.md`. Classification on every finding.

---

'''
docs={}
docs['08_INTERACTION_VALIDATION.md']=r'''
## Scope
`USER INPUT → EVENT HANDLER → INTERACTION VIEWMODEL → ANSWER VALIDATION → RESULT STATE →
FEEDBACK RENDERING → PROGRESS UPDATE → LOCAL PERSISTENCE`, reconstructed independently for
each interaction from real implementation (not lesson-JSON metadata).
Diagram `DIAGRAMS/05_interaction_validation.mmd`; call graphs `CALL_GRAPHS/02..05*.json`.

## Shared run dispatcher — VERIFIED_STATIC
`base/c.Y(Z)V` @10954996:
```
if (f.value == Boolean.TRUE) return        // prevents double submission
f.value = TRUE
viewModelScope.launch { onLessonRun$1(isCorrect) }
```
`InteractiveLessonBaseViewModel$onLessonRun$1.invokeSuspend` @10938584 (85 insns):
```
if (isCorrect) V() else X()
e.value = lessonBundle.b                  // chapter index → next page
f.value = FALSE
```
`onValidatedInputExecuted$1` @10939224 is a **separate** dispatcher with `delay(300)` and
three branches.

## 1. fillTheGap — VERIFIED_STATIC
`Lim/d.E0()` @12834200, 200 insns. Inputs/state:
`Lim/a{a:List<cn/d> allTokens, b:ArrayList<cn/d> correctTokens,
c:ArrayList<cn/d> placedTokens, d:List renderItems}`.
`cn/d{a:String text, b:Z, c:Z isCorrect, id:int}` created with id `120`.
Algorithm (see `METHOD_DOSSIERS/05_FillTheGap.md` and `EVIDENCE/VALIDATION_RAW_DISASM.txt`):
```
selected = placedTokens.filter { it.b }
ok = selected.size == correctTokens.size &&
     selected.indices.all { i -> selected[i].a == correctTokens[i].a }
answer = selected.filter{ it.a.isNotBlank() }.joinToString(" ") { it.a }
b0(answer); Y(ok)
```
Conditions: exact, ordered, case-sensitive `String.equals`; no partial credit; `correct=true`
options from `Option.a` are the answer key. Output: `Y(boolean)` → `V`/`X`.
State changes: `H` answer text, `C` wrong latch, `d` attempts, Room `lesson_progress`.

## 2. selection / single / multiple choice — VERIFIED_STATIC
`Lkm/f.b(List<sm/a>):Boolean` @13243392:
`selection.all { it.b == it.c }` where `b=selected`, `c=isCorrect`.
Empty list returns `true` (RunButton state prevents empty submission — `INFERRED`).
`Lkm/f.d(List)` @13243720 rebuilds `sm/a` display state for wrong-answer highlighting.
Four fragment run handlers (`Lnm/b`, `Lkm/c`, `Lom/d`, `Lmm/b`) join selected labels with
`", "` → `b0(text)` → `Y(result)`; `Lmm/b` additionally uses a count-based variant.
Exact SingleChoice/MultipleChoice dispatch inside `Lgm/h.a` = `UNKNOWN`.

## 3. spell — VERIFIED_STATIC
`Lpm/b.E0()` — same shape as fillTheGap with separator `""`:
`typed` vs `expected` (`Lpm/f.b/c`), sizes equal and every `cn/d.a` string equal → `Y(true)`.

## 4. validatedInput — VERIFIED_STATIC (M05 gap closed)
Expected answer: `code.subSequence(max(0,startIndex), min(endIndex,len)).toString()`
from `Lqm/d.E()`; typed text stored in `Lqm/d.S` by `Lqm/b` text-watcher.
Normalizer `Lqm/i.a(String)` @14172860:
```
lower = s.toLowerCase(Locale.US)
keep only Character.isLetterOrDigit(c) || c in ['<','>','(',')',':','{','}',',','.']
```
`InteractiveLessonValidatedInputFragment$setupViews$2.invokeSuspend` @10985684:
```
if (normalize(user) != normalize(expected))  result = Lqm/g (INCORRECT)
else if (user == expected)                   result = Lqm/e (CORRECT)
else                                         result = Lqm/f(user, expected) PARTIAL
b0(user); Z(result)
```
`onValidatedInputExecuted$1`: `delay(300)` then
`Lqm/e → V()`, `Lqm/f → b0(f.h) + W(f)`, `Lqm/g → X()`.
This is the only interaction with **tolerant matching**: case and most punctuation are
ignored; a normalised-only match is still accepted but takes the partial-match path.

## 5. WebView / activity lessons — VERIFIED_STATIC
`mimo.activity.correct|wrong|completed` are WebView→native bridge messages
(`lesson-webview.js`); `WebViewActivityResult` enum holds the three constants.
`webview/c.j0(cont)` and `InteractiveWebViewLessonFragment$goToNextPage$1` call
`base/c.U()` (auto-advance + progress). Exact payload→`Y(bool)` mapping = `INFERRED`.

## 6. executableFiles — VERIFIED_STATIC
`q.I()` @10912932 compares `userFileContents` (ArrayList<String>) with shipped
`solvedContent` (ArrayList<String>) via `List.equals`; equal → correct, else
`Ldm/h` error state + `IncorrectSolutionException`. Full dossier 10.

## 7. no-interaction / Reveal — VERIFIED_STATIC
`NonInteractiveLessonFragment$goToNextPage$1` → `U()`; `tries = NOT(C==TRUE)` so a
lesson with no wrong answers records `tries=1`.

## Result state → feedback — VERIFIED_STATIC
| Result | Method | Feedback | Sound | Progress |
|---|---|---|---|---|
| Correct | `V()` | `solutionFeedbackCorrect`, `jm/m.b(...,true,...)` | `sound.a(true)` | `H(1,d)` |
| Correct (partial) | `W(f)` | partial-match feedback | (not decoded) | `H(...)` |
| Incorrect | `X()` | `d0()` `solutionFeedbackWrong`, `jm/o` copy | — | `H(0,d)` |
| Auto-advance | `U()` | `e=chapterIndex` | — | `H(NOT(C==TRUE),d)` |
| Retry | `a0()` | `lesson_reset` analytics, `jm/q(list,false)` | — | no new row |

M05 run-004 `VERIFIED_RUNTIME`: wrong answer → red "Try again", Q disabled/grey,
`Continue` → code-editor lesson. Consistent with `X()`/`d0()`.

## Local persistence — VERIFIED_STATIC
`H(tries,attempts)` → `LessonProgressRepository.createLessonProgress` →
`e0()` → `LessonProgressQueue.storeLessonProgress` → Room `lesson_progress` `in_queue=1`.
Full chain in `CALL_GRAPHS/07_progress_persistence.json`.

## Remaining uncertainty (precise)
- `W()` full body (202 insns) and its difference from `V()` = `UNKNOWN`.
- `d0()` exact hard-mode/AI-Tutor/attempt boolean combination = `UNKNOWN`.
- `Lsm/a.b/.c`, `cn/d.b` semantic names = `INFERRED`.
- `SingleChoice`/`MultipleChoice` dispatch = `UNKNOWN`.
- Offline **correct** answer state was never observed at runtime (M05); the static
  reconstruction is `VERIFIED_STATIC`, not `VERIFIED_BOTH`.
'''
docs['09_LESSON_STATE_MACHINE.md']=r'''
## Verified states and transitions
Diagram `DIAGRAMS/04_lesson_execution.mmd` and `06_progression_state_machine.mmd`.

### Session lifecycle (`VERIFIED_STATIC`)
```
ChapterActivity
 → InteractiveLessonFragment (LessonBundle Parcelable)
 → InteractiveLessonViewModel.E(content,bundle)
 → Lgm/h.a(modules) : LessonInteractionType
 → base/c.O(content,bundle)  initialiseViewModel
 → N() reset RunButton + keyboard states
 → per-interaction ViewModel.E(content)  configure interaction state
 → user input (EditText / token taps / option taps / code editor)
 → Fragment.E0()  run handler
 → base/c.Y(isCorrect)
 → onLessonRun$1 → V() | X()
 → H(tries,attempts) → e0() → Room
 → e LiveData = lessonBundle.b → next lesson / chapter end
```

### Guard states (`VERIFIED_STATIC` field evidence)
| Field | Type | Meaning |
|---|---|---|
| `f` | `LiveData<Boolean>` | run-in-progress; `Y()` returns early if TRUE |
| `C` | `Boolean?` | wrong-answer latch; FALSE on correct, TRUE on incorrect |
| `d` | `int` | attempt counter (incremented in `V`, `X`, `U`) |
| `M` | `boolean` | `e0()` guard preventing duplicate progress writes |
| `E` | `boolean` | hard-mode / analytics flag |
| `I` | `Instant` | `startedAt` |
| `H` | `String` | last submitted answer text |
| `s`,`t` | `jm/m`,`jm/o` | correct / wrong feedback state |
| `n` | `LiveData<jm/q>` | module list + visibility flag |
| `e` | `LiveData<Integer>` | chapter/next-page index |
| `h` | `MutableSharedFlow<Long>` | emits `lessonId` on solve |

### Retry / reset — VERIFIED_STATIC
`a0()` emits `lesson_reset` analytics with
`lesson_id, tutorial_id, tutorial_version, track_id, attempts, duration`;
reposts `jm/q(list,false)`; calls `M()` and `Q()`; clears code-playground bundle `A`.
`g0()` emits `lesson_interaction_delete`.
`base/c.N()` resets `j`/`k` keyboard LiveData to `InteractionKeyboardButtonState.b`.

### Feedback state machine — VERIFIED_STATIC + VERIFIED_RUNTIME
`V()` → `i0()` browser output → `C=FALSE` → `d++` → `c0()` →
`solutionFeedbackCorrect` + success sound → `f0(isSolvedCorrectly, …)` → emit lessonId →
`I()` file cleanup.
`X()` → `d++` → `C=TRUE` → `H(0,d)` → `e0()` → `d0()` wrong feedback block.
`d0()` consults `S()`, DataStore `a.f()`/`a.p()`, `P()` (AI Tutor unlimited) and stores a
`jm/o` copy. M05 run-004 UI: red "Try again", Q disabled.

### Completion / advancement — VERIFIED_STATIC
`U()` and `onLessonRun$1` post `e = lessonBundle.b`;
`ChapterViewModel` drives chapter-end; `ChapterFinishedViewModel` branches online/offline;
`NonInteractiveLessonFragment` and WebView lessons use `U()` directly.

### Still `UNKNOWN`
- Correct-answer **runtime** screen (M05 never produced one); `UNKNOWN VERIFIED_RUNTIME`.
- `W()` partial-match feedback branch details.
- Full `d0()` boolean combination.
- How a wrong answer followed by a correct one affects `C` at the moment of the final
  submission (static `V()` sets `C=FALSE`; interaction = `INFERRED`).
'''
docs['10_LEARNING_PROGRESSION.md']=r'''
## VERIFIED_STATIC — content hierarchy (M05 reused)
19 tracks → 144 sections → 1,029 tutorials → 1,947 chapters → 18,272 lessons (English v753).
Tutorial types: `Learn, MobileProject, Challenge, Quiz, GuidedProject,
GuidedProjectOptional, RecreateProject, PracticeRequired, PracticeOptional`
(enum `<clinit>` verified). M05 counts: course 507, guidedProjectOptional 117,
guidedProject 74, challenges 40, practiceRequired 157, practiceOptional 134.
Chapter types: `NONE, PRACTICE_LEVEL_1..3, QUIZ, CHALLENGE_DIFFICULTY_0..4`.
All 144 sections satisfy `endIndex-startIndex+1 == len(tutorialIds)` (M05).

## VERIFIED_STATIC — path-map state machine
`GetPathMapState$invoke$3.invokeSuspend` @10129608, 659 insns
(`EVIDENCE/PATH_STATE_DISASM.txt`, dossier 15):
- states `Lvn/d0 Completed`, `Lvn/e0 Locked`, `Lvn/g0 Unlocked`,
  `Lvn/h0 UnlockedButNoKeys`, `Lvn/d chapter item`,
  `Lvn/y Locked(index)` / `Lvn/a0 Unlocked(index)` section states,
  `Lvn/a Locked(trackId)` / `Lvn/b Unlocked(trackId)` track states.
- `Challenge` tutorials are excluded from path items.
- Sequential prerequisite: a reverse `listIterator` over already-built items checks
  `TutorialType.isRequired()` and `Lvn/i0.d()`; the next item unlocks after the previous
  **required** predecessor is completed.
- `Tutorial.isCompleted()` → `Completed`; chapter items carry `isCompleted` and
  `isCompletedInHardMode` (from `Lds/w.c(Set, trackId, tutorialId, chapterId)`).
- `Tutorial.getHasProgress()`, `TutorialType.PracticeOptional`, Pro subscription tier
  (`Lyg/c.c`), `CanOpenChapterWithKeys`, keys count and dev-menu overrides
  (`Lsk/a.d()/e()`) choose `Locked` / `UnlockedButNoKeys` / `Unlocked`.
- Section states from `Lcc/b.y(List, Z, Integer?, Z, Z)`.
- Final `Lvn/n(track, sectionStates, selectedSectionIndex, dialogs, nextSectionState, …)`.

## VERIFIED_STATIC — completion records
`LessonProgressQueue.updateCorrectAnswersCount`:
`AnswersInChapter(correct = queued.count{isSolvedCorrectly()}, total = queued.size)`.
`getCorrectLessonProgressCount` = same correct count.
`getCorrectLessonsFirstTryCount` = `queued.count{isSolvedCorrectly() && attempts == 1}`.
`CompletionRepository.b(Track, cont)` attaches `TutorialCompletion.isCompleted` and
`completedChapters` from Room. `ChapterFinishedViewModel.R` =
`handleChapterAlreadyCompletedState` is the offline fallback.

## Economy / rewards — client-side boundary only
`VERIFIED_STATIC` strings and classes: `MainViewModel$fetchKeys$1`, `fetchRewards$1`,
`confirmRewardAndLookForNewRewards`, `daily_goal`, `streak_challenge_7d`,
`ChapterFinishedSuccessType{DAILY_GOAL_NOT_REACHED, DAILY_GOAL_REACHED,
DAILY_GOAL_ALREADY_REACHED_EARLIER_TODAY}`, `streakChallengeCoinPrice`, `userCoins`,
`local_coins`, `DefaultKeysRepository`, `DefaultStreakRepository`, `DefaultRewardRepository`,
`OnboardingSetDailyGoalViewModel`, `SetDailyGoalViewModel`, `GetUserStreakMonth`,
`ObserveUserStreakInfoCache`, `GetTrackEta`, `QueuePathOverviewEtaIfNeeded`.
**No XP/keys/coins/streak award formulas or thresholds were recovered** — they depend on
`Progress`/`PostProgressResponse`/`TrackEtaResponse` server bodies that M06 deliberately did
not reconstruct. `SERVER CONFIRMED = 0`.

## Unlock rule — EXPLICIT UNKNOWN
The exact boolean combination selecting `Locked` vs `UnlockedButNoKeys` vs `Unlocked` in
`GetPathMapState$invoke$3` is `UNKNOWN`: 659 instructions, 3 suspension labels, junk
`const/4` decoys. Precise pointer:
`Lcom/getmimo/interactors/path/GetPathMapState$invoke$3;->invokeSuspend`,
`classes.dex` @10129608, branches at PC `0x04aa`, `0x4f0`, `0x51a`, `0x608`.
`CanOpenChapterWithKeys$invoke$1` @10104004 second branch also `UNKNOWN`.

## Resume / restoration — `UNKNOWN`
M05 showed offline cold start rendering the same first three screens byte-for-byte and
offline AI/ChatGPT track content (`VERIFIED_RUNTIME`), but no persisted-progress-after-answer
or resume-after-force-stop evidence exists. `LessonBundle` and DataStore
`path_overview`/`first_run` keys indicate local state, but the exact restore algorithm is
`UNKNOWN`.
'''
docs['11_LOCAL_PERSISTENCE.md']=r'''
## VERIFIED_STATIC — Room schema (M05 SQL reused, M06 verified callers)
`ANALYSIS/MISSION_05/EVIDENCE/ROOM_SQL.txt`:
- `lesson_progress` 11 columns, PK(`lesson_id`,`tutorial_id`) @`classes.dex 2183344`.
- `chapter_completions` PK(`chapter_id`,`track_id`) @2183130.
- `tutorial_completions` PK(`tutorial_id`,`track_id`) @2183790.
- DAO strings: `SELECT * FROM lesson_progress WHERE in_queue = 1`,
  `UPDATE lesson_progress SET in_queue = 0 WHERE in_queue = 1`,
  `DELETE FROM lesson_progress WHERE in_queue = 1`,
  `SELECT COUNT(DISTINCT chapter_id) FROM chapter_completions`.
- Identity hashes `08b926448d86528e697981ddd30459f7`,
  `2b8ab6d303d9a501bd8c8fb78d8352fc`.
- 269 database tables in the APK (M05).

M06 verified the exact `LessonProgress` field order from
`LessonProgressRepository.createLessonProgress` @10063916 and the entity constructor
`(J Instant Instant I J I J J I Z Z)V`:
`lessonId, completedAt, startedAt, tries, tutorialId, tutorialVersion, trackId,
publishSetVersion, attempts, isPracticeProgress, inQueue`.

## VERIFIED_STATIC — write path
```
V()/X()/U()/W()
 → base/c.H(tries,attempts)
 → LessonProgressRepository.createLessonProgress(bundle, startedAt, tries, attempts)
 → base/c.e0()  (guard field M)
 → LessonProgressQueue.storeLessonProgress(progress, bool, bool, cont)
     ├─ if devMenuStorage.e() → return (dev override)
     ├─ LessonProgressRepository.addOrUpdateLessonProgressInQueue(listOf(progress), …)
     │    → Room lesson_progress (in_queue = 1)
     ├─ updateCorrectAnswersCount() → _answersInChapter StateFlow
     └─ if attempts == 1 → updateLessonStreakDetector
```
Diagram `DIAGRAMS/07_persistence_flow.mmd`; call graph `CALL_GRAPHS/07_progress_persistence.json`.

## VERIFIED_STATIC — queue drain / sync boundary
`LessonProgressQueue.storeAndPostAllLessonProgress` →
`LessonProgressRepository.moveLessonProgressFromQueue()` (clears `in_queue`) →
`postUnsyncedLessonProgress()`:
```
if (!networkUtils.a()) {
    log("No internet connection, not posting unsynced lesson progress")
    throw NoConnectionException
}
launch { POST via LessonProgressApi }
```
`SERVER CONFIRMED = 0`: no response bodies or server logic reconstructed.

## VERIFIED_STATIC — other stores
- `data/local/a; DataStoreUserPreferences`: `completed_hard_mode_chapters`,
  `KEY_HARD_MODE_COMPLETED_LESSON_IDS`, onboarding/first-run/path-overview flags,
  `dailyGoal`; `f(cont):Boolean`, `p()` reset used by `base/c.d0()`.
- SharedPreferences strings: `onboarding_user_daily_goal`, `networkUtils`,
  `KEY_HARD_MODE_COMPLETED_LESSON_IDS` (M05 `STORAGE_AND_ONBOARDING_STRINGS.txt`).
- In-memory: `m0` LiveData (`e,f,i,j,k,m,n,q,w,A,R`), `kotlinx.coroutines.flow.i`
  shared flow (`h`), `_answersInChapter` StateFlow, `LessonProgressQueue` unsynced rows.
- `Lye/d` reads/writes under `Context.getFilesDir()` (updated content);
  `base/c.D()` deletes `File(filesDir, lessonId.toString())` after a solve.
- `libdatastore_shared_counter.so` native counter (M04/M05) = `INFERRED` DataStore
  multi-process support.

## Lifecycle / force-stop — `UNKNOWN`
Room rows with `in_queue=1` survive process death by design of SQLite, but M06 has **no
runtime test** of force-stop → relaunch → queue restoration. No root/private DB extraction
was performed (forbidden). This is an explicit `UNKNOWN` with pointer
`LessonProgressRepository.getAllLessonProgressInQueue` / `LessonProgressDao` (`Lcg/a;`).

## Migrations — `UNKNOWN`
Room identity hashes are known; the full migration class list and SQL was not decoded in M06.
'''
docs['12_CODE_EDITOR_AND_EXECUTABLE_LESSONS.md']=r'''
## VERIFIED_STATIC — editor architecture
`Lcom/getmimo/ui/codeeditor/view/b;` = `CodeEditViewModel` (7 votes),
`Lam/o;` = `CodeDiffViewModel`, `Lep/t0;` emits `Lep/b0` events (`Lep/v` code pair,
`Lep/y` highlight list), `Lcom/getmimo/ui/codeeditor/highlight/a;` syntax highlighter,
`Lcom/getmimo/ui/inputconsole/a;` input console,
`Lcom/getmimo/ui/codeplayground/CodePlaygroundActivity;`,
`CodePlaygroundBundle$FromLesson` (referenced by `base/c.Q()`),
`Ldg/a;<clinit>` shipped HTML template:
```
<!doctype html>\n<html>\n<head>\n  <title></title>\n
  <link rel="stylesheet" href="style.css">\n</head>\n<body>\n
  <script src="script.js"></script>\n</body>
```
`assets/lesson-webview.js` / `lesson-webview-fonts.js` injected into `EmbeddedLessonWebView`.
`CodeLanguage` enum covers `BASH, CPP, CSHARP, CSS, CSV, …` with default file names
(`program.cpp`, `program.cs`, `style.css`, `data.csv`, `script.js`, `script.py`).

## VERIFIED_STATIC — file model & selection
`LessonContent$Executable{instructions, preselectedFileIndex, files,
getHasBrowserOutput(), getHasInputConsole()}`;
`File{name, codeLanguage, content, solvedContent}`; runtime `CodeFile{name, content}`.
`preselectedFileIndex` chooses the initially open tab; `q.G/H` handle tab selection.
M05: all 4,024 `executableContent` objects have
`instructions, preselectedFileIndex, hasVisualOutput, files, hints`.

## VERIFIED_STATIC — offline correctness decision
`ExecutableLessonViewModel.I()` @10912932 compares
`codeFiles.map{getContent()}` with `executable.files.map{getSolvedContent()}` using
`ArrayList.equals`. Equal → correct; otherwise `Ldm/h` error state and
`IncorrectSolutionException`. `E()` @10913380 then calls
`createLessonProgress(bundle, startedAt, tries, attempts)`.
⇒ **Shipped `solvedContent` is sufficient for the offline correctness check.**
`VERIFIED_STATIC`, resolving M05's open question.

## VERIFIED_STATIC — hints & browser preview
`q.F(Lym/h, Lzl/z)` (248 insns) handles guided-project hints: for file names
`style.css`, `index.html`, `script.py`, `script.js` it looks up static maps `Lcm/b.a..d`
keyed by lessonId, extracts identifiers, emits `Lep/v` and `Lep/y`.
`q.J(...)` builds `Lbe/n0` analytics with `ExecutableLessonRunResult`, duration from
`Seconds.secondsBetween(startedAt, now)`, attempts and either a dump of all files or
`"Lesson passed"`.
`q.K(...)` = `updateCodeExecutionState` (Orbit MVI intent).
`CreateBrowserOutput$invoke$2` logs `"Can't create WebView output"`.

## Client-side boundary (NOT reconstructed)
Retrofit endpoints `POST /v1/code/runfiles`, `POST /v1/tutorials/{id}/runFiles` exist in
M02 `HTTP_VERBS_RESOLVED.json` (53 endpoints). M06 records only the boundary:
no request/response bodies, no server execution engine, no server-side test harness.
`SERVER CONFIRMED = 0`.

## SQL / HTML / CSS / JS exercises
`LessonModule$Database` + `DatabaseView` render SQL exercises;
`WebviewType` + embedded WebView render HTML/CSS/JS; `hasVisualOutput` controls browser
preview. Which languages go through a local WebView vs a remote runner is `INFERRED` from
`hasVisualOutput`/`getHasBrowserOutput()`; exact routing = `UNKNOWN`.

## Remaining uncertainty
- Whether `q.I()` applies to every executable lesson or only guided-project variants
  (`callers=1`, reducer not fully decoded) = `UNKNOWN`.
- Result/test feedback from any remote runner = `UNKNOWN` (server-owned).
- `Interaction$ValidatedInput.e/f` and hint-test semantics = `UNKNOWN`.
'''
docs['13_UI_NAVIGATION_AND_RUNTIME.md']=r'''
## VERIFIED_STATIC — component names recovered
`SCHEMAS/OBFUSCATION_MAP.json` (173 entries). Key UI components:
| Semantic | Obfuscated | Votes |
|---|---|---|
| `MainActivity` | `ui/main/d;` | 35 (ViewModel) / `MainActivity` |
| `SplashViewModel` | `ui/a;` | 1 |
| `ChapterActivity` | `ui/chapter/ChapterActivity;` | 16 |
| `ChapterViewModel` | `ui/chapter/ChapterViewModel;` | 15 |
| `PathMapViewModel` | `ui/path/map/j;` | 15 |
| `PathMapFragment` | `ui/path/map/a;` | 1 |
| `ChapterFinishedViewModel` | `chapterendview/main/f;` | 13 |
| `ChapterFinishedFragment` | `chapterendview/main/e;` | 7 |
| `InteractiveLessonFragment` | `ui/lesson/interactive/c;` | 2 |
| `InteractiveLessonViewModel` | `ui/lesson/interactive/d;` | 4 |
| `InteractiveLessonBaseViewModel/Fragment` | `base/c;` / `base/b;` | 14 / 11 |
| `NonInteractiveLessonFragment` | `nointeraction/a;` | 1 |
| `InteractiveWebViewLessonFragment/ViewModel` | `webview/b;` / `webview/c;` | 1 / 1 |
| `ExecutableLessonViewModel` | `executable/q;` | 46 |
| `CodeEditViewModel` | `codeeditor/view/b;` | 7 |
| `SettingsFragment/ViewModel`, `ProfileFragment/ViewModel`, `PracticeTabFragment/ViewModel`, `SearchTrackFragment/ViewModel`, `StoreViewModel`, `AiTutorViewModel`, `LeaderboardFragment`, `HonestFreeTrialFragment/ViewModel`, `Paywall` screens | see map | |

## VERIFIED_RUNTIME (M04/M05, reused)
Launch `.ui.SplashActivity_default` → `.ui.onboarding.intro.IntroSlidesActivity`;
`com.getmimo`, `9.35`, `versionCode 1792759685`, `arm64-v8a`.
M05 run `42002808217`: first three offline UI hierarchies byte-identical to online.
`42003884423`: 24 taps to "Guess the letter" Q/R/D lesson.
`42005358012`: wrong answer → red "Try again", Q disabled/grey, `Continue` → code editor.
`42006697783`: offline track 274 "Automating Tasks with AI" lessons rendered.
`VERIFIED_BOTH` asset↔runtime matches MATCH-1..5 in M05
`EVIDENCE/RUNTIME_STATIC_MATCH.json`.

## VERIFIED_STATIC — navigation events
`base/c.e : LiveData<Integer>` = chapter/next-page index (`lessonBundle.b`);
`base/c.A : m0` posts `CodePlaygroundBundle` (`Ljm/h`) when `Q()` is true;
`ChapterActivity.G(ChapterBundle,Z)` / `J(cont)` use `key_skip_unlock_animation`;
`ChapterViewModel$StartupStage` enum = `CheckingUnlock`, `Unlocking`, …;
`PathMapViewModel.L refreshPathMapState`, `M init`, `N shouldStartChapterInHardMode`;
`Lxn/n0 ScrollToSection(sectionIndex=…)` Compose event.

## VERIFIED_STATIC — runtime behaviours
`base/c.Y()` prevents double-run with `f==TRUE`;
`a0()` lesson reset; `g0()` interaction delete;
`c0()`/`d0()` feedback visibility; `N()` keyboard state reset;
`D()` deletes per-lesson temp dir; `I()` cleanup after solve.
`RunButton$State.a/b` and `InteractionKeyboardButtonState.a/b/c` gate input.

## Android framework interactions — VERIFIED_STATIC
`androidx.lifecycle.m0/i0` LiveData `setValue`/`postValue` (`l`,`k`,`d`);
`kotlinx.coroutines` `ra0/z`, `Lkotlinx/coroutines/a.delay(300)`, Orbit MVI
`Lorg/orbitmvi/orbit/a.d`; `android.os.Handler(Looper.getMainLooper()).postDelayed`;
`AssetManager.open`; `ConnectivityManager`; `XmlPullParserFactory`; Jetpack Compose and
WorkManager.

## Remaining uncertainty
- Exact navigation graph (NavHost routes / fragment transactions) = `UNKNOWN`; only
  component names and LiveData events were decoded.
- Full layout XML / Compose hierarchy = `UNKNOWN` (M05 UI hierarchies cover observed screens).
- Process-recreation restoration = `UNKNOWN`.
'''
for n,c in docs.items():
    (D/n).write_text(PRE+c.strip()+'\n',encoding='utf-8')
    print('wrote',n,len(PRE+c))
