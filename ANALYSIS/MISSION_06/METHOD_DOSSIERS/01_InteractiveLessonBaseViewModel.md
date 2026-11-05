# InteractiveLessonBaseViewModel (`Lcom/getmimo/ui/lesson/interactive/base/c;`)

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/InteractiveLessonBaseViewModel.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## Identity — VERIFIED_STATIC
R8 renamed this class to `c`, but 14 Kotlin inner classes retain the original name
(`InteractiveLessonBaseViewModel$lessonSolvedCorrectly$1`, `$onLessonRun$1`, …).
`SCHEMAS/OBFUSCATION_MAP.json` records 14 votes. Constructor `<init>(Lhm/b;)V` takes the
13-slot DI container `Lhm/b;`. `classes.dex`, 33 methods; base class of every interactive
lesson ViewModel used in M06.

## Fields (verified `iget`/`iput` operands)
| Field | Type | Role |
|---|---|---|
| `b` | `Lhm/b;` | DI container: `a`..`m` Object slots (`d`=LessonProgressRepository, `b`=analytics, `g`=DataStore prefs, `h`=filesDir wrapper, `i`=sound) |
| `c` | `List` | parsed code blocks (`jm/e`) carrying `Interaction` objects |
| `d` | `int` | attempt counter, `+1` in `V()`, `X()`, `U()` |
| `e`,`f` | `m0` (LiveData) | `e` = next-page/chapter index event, `f` = "run in progress" Boolean guard |
| `h` | `kotlinx.coroutines.flow.i` | MutableSharedFlow<Long> emitting `lessonId` on solve |
| `i`,`j`,`k`,`m`,`n`,`q`,`w`,`A`,`R` | `m0` | RunButton state, keyboard button state, render items, solution feedback, code-playground bundle |
| `C` | `Boolean?` | wrong-answer latch: `FALSE` in `V()`, `TRUE` in `X()` |
| `E` | `boolean` | analytics/feedback flag |
| `H` | `String` | last submitted answer text (`b0`) |
| `I` | `org.joda.time.Instant` | lesson `startedAt` |
| `M` | `boolean` | guard set by `e0()` before launching `storeLessonProgressInMemory$2` |
| `s`,`t` | `jm/m`,`jm/o` | solution-feedback states (correct / wrong) |
| `u` | `LessonContent$Interactive` | current content |
| `D` | `LessonBundle` | current navigation bundle |
| `v` | `int` | index stored in `Lym/f` interaction event |

## Methods (semantic names recovered from coroutine inner classes)
| Obfuscated | Name | code_offset | insns | What it really does |
|---|---|---|---|---|
| `H(I I)` | createLessonProgress | 10948948 | 17 | `b.d` → `LessonProgressRepository.createLessonProgress(K(), I, arg1, arg2)` |
| `I()` | cleanupLessonFiles | 10949040 | 28 | `new File(filesDir, String.valueOf(lessonId))` → `k70/h.J(File)` (delete recursively) |
| `K()` | getLessonBundle | 10949304 | ~ | returns `D` |
| `L()` | getLessonType | 10949404 | ~ | analytics `LessonType` |
| `Q()Z` | hasCodePlaygroundBundle | 10952588 | ~ | `B != null` |
| `T()Z` | isFeedbackEnabled (field `J`) | 10952812 | 4 | |
| `U(cont)` | lessonSolvedAndProceedToNextLesson | 10952900 | 130 | sets `f=TRUE`, `d++`, `H(tries, d)`, `e0`, `e=chapterIndex`, `f0(false,v4)`, emits lessonId, `f=FALSE` |
| `V(cont)` | lessonSolvedCorrectly | 10953356 | 162 | `i0()` (browser output) → `C=FALSE`, `d++`, `c0()`, `v2 = (C==TRUE) XOR 1` → `H(v2,d)` → `e0` → `solutionFeedbackCorrect` + sound → `isSolvedCorrectly()` → `f0` → emit lessonId → `I()` |
| `W(qm/f,cont)` | lessonSolvedCorrectlyWithPartialMatch | 10953916 | 202 | partial-match branch |
| `X(cont)` | lessonSolvedIncorrectly | 10954596 | 113 | `d++`, `C=TRUE`, `H(0,d)`, `e0`, `d0()` wrong feedback block |
| `Y(Z)` | onLessonRun | 10954996 | 30 | if `f.value == TRUE` return; else set `TRUE`, launch `onLessonRun$1` with the boolean |
| `Z(iq/w)` | emitValidationResult | — | — | coroutine channel used by validatedInput |
| `a0()` | lesson_reset | 10955284 | ~ | analytics `lesson_reset` with `lesson_id,tutorial_id,tutorial_version,track_id,attempts,duration`; posts `jm/q(list,false)` |
| `b0(String)` | onValidatedInputExecuted (answer capture) | 10955764 | 31 | `trim()` then `toString()`; if blank → `"No answer text available"`; stores into `H` |
| `c0()` | updateSolutionFeedback | 10955960 | 31 | if `T()` and `n.value` non-null → post `new jm/q(list,true)` |
| `d0(cont)` | showWrongFeedbackBlock | 10956096 | 148 | `solutionFeedbackWrong`, consults `S()`, DataStore `a.f()`/`a.p()`, `P()` (AI Tutor unlimited) |
| `e0(…)` | storeLessonProgressInMemory | 10956692 | ~ | guard field `M`, launch `storeLessonProgressInMemory$2` on `Lnp/b;->c` dispatcher |
| `f0(Z Z)` | trackLessonResult | 10956848 | 41 | builds `Lth/b.a(...)` analytics event with `d`, `I`, `LessonBundle.c`, `TutorialType.getTrackingField()`, `E` |
| `g0()` | lesson_interaction_delete analytics | 10957044 | ~ | |
| `h0(List,Z)` | configureInteraction | 10957544 | 14 | creates `Lym/f(v, list, boolean)` → posts LiveData `w` |
| `i0(cont)` | updateTabbedCodeViewWithBrowserOutput | — | ~ | suspends until browser output available |
| `O(content,bundle)` | initialiseViewModel | 10949840 | 616 | stores `D`,`u`; filters `LessonModule.a == ModuleVisibility.c(ALWAYS)`; maps `Paragraph→jm/j`, `Image→jm/i`, `Webview→jm/k`; posts render list to `m`; sets code interactions; wires coroutine flows |

## Verified call chain
`RunButton → Fragment.E0() → Y(boolean) → onLessonRun$1.invokeSuspend →
V() | X() → H(tries,attempts) → LessonProgressRepository.createLessonProgress →
e0() → LessonProgressQueue.storeLessonProgress → Room lesson_progress`.
See `CALL_GRAPHS/01_answer_validation_core.json` (36 nodes / 63 real invoke edges).

## Remaining uncertainty
- `W()` (partial match) full body not fully interpreted: exact feedback difference vs `V()` = `UNKNOWN`.
- `d0()` boolean combination (hard mode / AI Tutor / attempts) not completely decoded = `UNKNOWN`.
- `h0()` originally mapped to `configureInteraction` by inner-class heuristic; the exact downstream
  consumer of `Lym/f` is only partially traced = `INFERRED`.
