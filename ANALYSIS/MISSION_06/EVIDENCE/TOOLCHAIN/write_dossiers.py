import pathlib,json
D=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/METHOD_DOSSIERS');D.mkdir(parents=True,exist_ok=True)
HEADER='''# {title}

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/{smali}`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

'''
DOSSIERS=[
dict(file='01_InteractiveLessonBaseViewModel.md',title='InteractiveLessonBaseViewModel (`Lcom/getmimo/ui/lesson/interactive/base/c;`)',smali='InteractiveLessonBaseViewModel.smali.txt',body=r'''
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
'''),
dict(file='02_LessonProgressRepository.md',title='LessonProgressRepository & createLessonProgress',smali='LessonProgressRepository.smali.txt',body=r'''
## VERIFIED_STATIC — exact record construction
`Lcom/getmimo/data/source/remote/progress/LessonProgressRepository;->createLessonProgress(
 Lcom/getmimo/ui/lesson/interactive/LessonBundle; Lorg/joda/time/Instant; I I)
 Lcom/getmimo/data/model/room/LessonProgress;`  
`classes.dex` code_offset `10063916`, 44 instructions.

Pseudocode recovered from the `invoke-direct/range` register map:
```
fun createLessonProgress(bundle, startedAt, tries, attempts): LessonProgress {
    val completedAt = Instant()                       // now
    if (Instant().isBefore(startedAt))                // guard, logged, not thrown
        logError("CreateLessonProgress: completedAt date (" + now +
                 ") is before startedAt date (" + startedAt + ")")
    return LessonProgress(
        lessonId          = bundle.a,                 // long
        completedAt       = completedAt,
        startedAt         = startedAt,
        tries             = tries,                    // 3rd arg
        tutorialId        = bundle.e,                 // long
        tutorialVersion   = bundle.v,                 // int
        trackId           = bundle.f,                 // long
        publishSetVersion = tracksRepository.c(),     // current shipped publish set
        attempts          = attempts,                 // 4th arg
        isPracticeProgress= bundle.B,                 // boolean
        inQueue           = true                      // const/4 v15,1
    )
}
```
`LessonProgress` constructor signature `(J Instant Instant I J I J J I Z Z)V` and 11 getters
are in `EVIDENCE/DISASM/LessonProgress.smali.txt`. Room SQL (M05 `EVIDENCE/ROOM_SQL.txt`)
confirms columns and composite PK `(lesson_id, tutorial_id)`.

## Callers — VERIFIED_STATIC
`base/c;->H(I I)` @10948948 passes `(tries, attempts)`; `ExecutableLessonViewModel.E()`
@10913380 also calls it with `state.zl/z` fields.

## Other methods (verified)
`addOrUpdateLessonProgressInQueue(List, Z, cont)` (62 insns) — Room upsert;
`clearLessonProgressQueue` (36), `getAllLessonProgressInQueue` (22),
`moveLessonProgressFromQueue` (26) — clears `in_queue`;
`postUnsyncedLessonProgress` (44) — **offline gate**, see dossier `18_NetworkUtils.md`;
`toProgressList` (76), `toLessonProgressSyncResult` (14), `fetchTrackCompletionForFavoriteTracks` (239).

## Client-side boundary
`LessonProgressApi` Retrofit interface is only referenced; no response bodies, no server logic
were reconstructed. `SERVER CONFIRMED = 0`.

## Remaining uncertainty
- Argument names `tries`/`attempts` are `INFERRED` from constructor order and getter names;
  DEX has no parameter names for these two ints.
- `isBefore` vs `isAfter` of joda `Lld0/c;->h` = `INFERRED` (guard message names the condition).
'''),
dict(file='03_LessonProgressQueue.md',title='LessonProgressQueue — local answer counting',smali='LessonProgressQueue.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;`, `classes.dex`.
Fields: `devMenuStorage Lze/a;`, `lessonProgressRepository`, `_answersInChapter Lua0/o;`
(MutableStateFlow), `answersInChapter` Flow.

### `storeLessonProgress(LessonProgress, Z, Z, cont)` @10058920, 136 insns
```
if (devMenuStorage.e()) return                  // dev-menu "disable progress" override
lessonProgressRepository.addOrUpdateLessonProgressInQueue(listOf(progress), bool, cont)
updateCorrectAnswersCount(cont)
if (progress.attempts != 1) ... else updateLessonStreakDetector(progress, bool)
```
### `updateCorrectAnswersCount(cont)` @10056956, 123 insns
```
val queued = repo.getAllLessonProgressInQueue()
val correct = queued.count { it.isSolvedCorrectly() }
_answersInChapter.emit(AnswersInChapter(correct, queued.size))
```
### `getCorrectLessonProgressCount` @10057692 = `queued.count{isSolvedCorrectly()}`
### `getCorrectLessonsFirstTryCount` @10058148 = `queued.count{isSolvedCorrectly() && attempts == 1}`
### `storeAndPostAllLessonProgress` @10058624
`repo.moveLessonProgressFromQueue()` → `repo.postUnsyncedLessonProgress()`.

These are the **only** chapter-end scoring formulas recovered from real bytecode; M05 left
scoring/thresholds `UNKNOWN`. `isSolvedCorrectly()` is `tries >= 1` (see dossier 04), not
`attempts >= 1`.

## Remaining uncertainty
- How `AnswersInChapter(correct,total)` is converted into XP / keys / coins / chapter-end
  success type is **not** in this class → `UNKNOWN`, likely server-owned
  (`GetChapterEndSuccessState`, `ChapterFinishedSuccessType`).
- `updateLessonStreakDetector` body (10 insns) delegates to another class; exact streak algorithm
  `UNKNOWN`.
'''),
dict(file='04_LessonProgress_isSolvedCorrectly.md',title='LessonProgress.isSolvedCorrectly() — M05 correction',smali='LessonProgress.smali.txt',body=r'''
## VERIFIED_STATIC — exact bytecode
`Lcom/getmimo/data/model/room/LessonProgress;->isSolvedCorrectly()Z`  
`classes.dex` code_offset `9913532`, 13 instructions:
```
000000  move-object v1, v5
000002  iget v1, v1, LessonProgress->tries I
000006  const/4 v3, 2          <- Smob junk
000008  const/4 v3, 1          <- real 1
00000a  move v0, v3
00000c  if-lt v1, v0, +004h
000010  const/4 v4, 1
000012  return v0              <- v0 == 1 (true)
000014  const/4 v3, 2
000016  const/4 v3, 0
000018  move v1, v3
00001a  return v1              <- false
```
**`return tries >= 1`.** The field is `tries`, not `attempts`.

## CORRECTION to M05
M05 (`CONTENT_MODEL.md` / `LEARNING_ENGINE.md`) recorded `isSolvedCorrectly()` as
`attempts >= 1`. M02 had only `intField >= 1`. The DEX bytecode proves the read is
`iget … ->tries I`. Reason for the earlier error: the JADX archive is incomplete and the
Room entity's two integer getters were conflated. Documented in
`17_CORRECTIONS_AND_LIMITATIONS.md`. Classification of correction: `VERIFIED_STATIC`.

## How `tries` is produced — VERIFIED_STATIC
- `base/c;->V()` (lessonSolvedCorrectly): `v2 = (C == TRUE) XOR 1` → `H(v2, d)`;
  with `C = FALSE`, `tries = 1`.
- `base/c;->X()` (lessonSolvedIncorrectly): `H(0, d)` → `tries = 0`.
- `base/c;->U()` (proceed to next): `tries = NOT(C == TRUE)`.
Thus `tries` is effectively the "solved correctly" flag (0/1) while `attempts` (`d`) counts
submissions. `LessonProgressQueue.getCorrectLessonsFirstTryCount` uses
`isSolvedCorrectly() && attempts == 1`.

## Remaining uncertainty
- Whether a wrong answer followed by a correct one in the same lesson leaves `C` FALSE
  (so `tries=1`) is `INFERRED` from `V()` overwriting `C`; not runtime-verified.
'''),
dict(file='05_FillTheGap.md',title='fillTheGap ViewModel + Fragment run handler',smali='FillTheGapViewModel.smali.txt',body=r'''
## VERIFIED_STATIC
- `Lcom/getmimo/ui/lesson/interactive/fillthegap/a;` = `InteractiveLessonFillTheGapViewModel`
  (inner class `…$configureInteraction$1`, `…$createCursorBlinkEvents$3`). 4 methods.
- `Lim/d;` = its Fragment (has `T(View,Bundle)`, `M0()` returning the VM, `E0()` run handler).

### `a;->E(LessonContent$Interactive)V` @10964388, 210 insns
Finds first `jm/e` whose `b` is `Interaction$FillTheGap`; reads
`Interaction$FillTheGap.c : List<Option>`. Each `Option` has fields
`a:Z (isCorrect)`, `b:CharSequence (text)`, `c:I (startIndex)`, `d:I (endIndex)`.
Builds:
```
allTokens      = options.map { cn/d(120, it.b.toString(), it.a) }
correctTokens  = allTokens.filter { it.c }            // expected answer in content order
renderItems    = prose spans jm/y + gaps jm/x (from Option.c/d char offsets)
state          = Lim/a(allTokens, correctTokens, shuffledTokens?, renderItems)
Q = state; j0(state);   // posts to LiveData R
// finally: flow of cursor-blink events → configureInteraction$1/$2, launched in viewModelScope
```
Error string: `"There is no code block found with FillTheGap interaction. There must be at least one"`.

### `Lim/d;->E0()V` @12834200, 200 insns — THE ANSWER VALIDATOR
```
val st = vm.Q ?: return
val expected = st.b                       // correctTokens, ordered
val selected = st.c.filter { it.b }       // tokens the learner placed, ordered
var ok = false
if (selected.size == expected.size) {
    ok = true
    for ((i,t) in selected.withIndex())
        if (t.a != expected[i].a) { ok = false; break }
}
val answerText = selected.filter { it.a.isNotBlank() }
                         .joinToString(separator = " ") { it.a }
vm.b0(answerText)                         // stores answer for analytics
vm.Y(ok)                                  // onLessonRun(ok)
```
Comparison is **exact String equality** on `cn/d.a` (token text), in order, against the
`correct=true` options. There is no server call and no fuzzy matching on this path.

### `a;->j0(Lim/a;)V` @10965552, 137 insns
Recomputes RunButton state (`RunButton$State.a` enabled / `.b` disabled) from whether the
number of placed tokens equals the number of gaps, and posts `Lym/f` via `base/c.h0()`.

## Remaining uncertainty
- Meaning of `cn/d.b` (used by the filter) is `INFERRED` as "placed/filled"; DEX has no field names.
- `Lud/a.C(allTokens)` (third state list) is probably a shuffled keyboard pool = `INFERRED`.
'''),
dict(file='06_Selection.md',title='selection / single / multiple choice validation',smali='SelectionViewModel.smali.txt',body=r'''
## VERIFIED_STATIC
- `Lcom/getmimo/ui/lesson/interactive/selection/a;` = `InteractiveLessonSelectionViewModel`
  (6 methods; `L()` returns `LessonType$Selection`).
- `Lnm/b;`, `Lkm/c;`, `Lom/d;`, `Lmm/b;` are four Fragment run handlers that all call
  `Lkm/f;->b(List)Z` and then `base/c.Y(boolean)`.
- `Lkm/f;` = shared selector validator (4 methods).

### `Lkm/f;->b(Ljava/util/List;)Z` @13243392, 46 insns
```
fun isValid(selection: List<sm/a>): Boolean =
    selection.all { it.b == it.c }
```
where `Lsm/a` fields: `b:Z` (selected by learner), `c:Z` (isCorrect from content).
Bytecode: `iget-boolean v1, c; iget-boolean v0, b;` → continue loop only when both equal;
any mismatch returns `false`; an empty list falls through to `true` (the Fragment's RunButton
state prevents submitting an empty selection — `INFERRED`).
`Lkm/f;->d(List)` @13243720 maps each `sm/a` through `sm/a.a(...)` to produce the post-run
display state (wrong answers highlighted), then `Fragment.E0()` reposts it to LiveData.

### `Lnm/b;->E0()V` (selection fragment)
Calls `km/f.b(currentList)` → joins selected labels with `", "` → `base/c.b0(text)` →
`base/c.Y(result)`. Also handles a count-based variant (lines 0x0a8–0x136 of
`EVIDENCE/DISASM/SelectionFragmentRunHandler.smali.txt`) that compares the number of
correctly-chosen items to an expected count.

### `Lgm/h;->a(List)` maps `LessonModule$Selection` to
`LessonInteractionType$Selection`, `$SingleChoice` (`"selection"`) or
`$MultipleChoice` (`"multiple_choice"`) — three distinct renderer branches not previously
identified in M05.

## Remaining uncertainty
- `Lsm/a.b`/`.c` semantic names = `INFERRED` from usage.
- Exact SingleChoice vs MultipleChoice dispatch condition inside `Lgm/h.a` = `UNKNOWN`
  (437-instruction method, only partially decoded).
'''),
dict(file='07_Spell.md',title='spell interaction validation',smali='SpellViewModel.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/ui/lesson/interactive/spell/a;` = `InteractiveLessonSpellViewModel`
(7 methods; `E()` 249 insns, `j0(Lcn/d;)`, `k0(Lpm/f;)`).
`Lpm/b;` = its Fragment (`E0()` @1283xxxx).

### `Lpm/b;->E0()V` — THE ANSWER VALIDATOR
```
val st = vm.Q ?: return           // Lpm/f
val expected = st.b               // ArrayList<cn/d> expected letters, ordered
val typed    = st.c               // ArrayList<cn/d> user letters, ordered
var ok = false
if (typed.size == expected.size) {
    ok = true
    for ((i,t) in typed.withIndex())
        if (t.a != expected[i].a) { ok = false; break }
}
val answerText = typed.filter{ it.a.isNotBlank() }.joinToString(separator = "") { it.a }
vm.b0(answerText)
vm.Y(ok)
```
Exact byte-for-byte same algorithm shape as fillTheGap but with separator `""` (letters
concatenated) instead of `" "`. Error/keyword string `"spell"`.

### Interaction model
`Interaction$Spell` fields `b:Z (isDefault)`, `c:I (startIndex)`, `d:I (endIndex)`;
the expected letter sequence comes from the code-block substring between those indices.

## Remaining uncertainty
- Whether case is normalised before this comparison = `UNKNOWN`; the bytecode shows only
  `String.equals` via `kotlin/jvm/internal/h.c`, i.e. case-sensitive.
'''),
dict(file='08_ValidatedInput.md',title='validatedInput ViewModel, normalizer and result types',smali='ValidatedInputViewModel.smali.txt',body=r'''
## VERIFIED_STATIC — M05 gap closed
`Lqm/d;` = `InteractiveLessonValidatedInputViewModel` (extends `base/c`),
`Lcom/getmimo/ui/lesson/interactive/validatedinput/b;` = its Fragment,
`Lqm/b;` = `EditText` text-watcher lambda (writes `Lqm/d;->S : String`).

### `Lqm/d;->E(LessonContent$Interactive)V` — expected-answer extraction
Finds the `jm/e` code block with `Interaction$ValidatedInput` (`c:I startIndex`,
`d:I endIndex`, `e:String`, `f:String[]`). From the code `CharSequence a`:
```
prefix  = a.subSequence(0, coerce(startIndex,0,len))
answer  = a.subSequence(max(0,startIndex), min(endIndex,len)).toString()   // EXPECTED
suffix  = a.subSequence(coerce(endIndex,0,len), len)
state.R = Lqm/h(answer, prefix, suffix)
```
So **the expected answer is shipped inside the lesson's own code block**, delimited by
`startIndex`/`endIndex` — not fetched from a server and not a separate JSON key.
`E()` also builds `Lym/n`/`Lym/j` render tabs with `Lym/m` prefix/suffix, calls `h0(...)`
and resets `S` to `""` via `j0("")`.

### `Lqm/i;->a(String)String` @14172860, 50 insns — NORMALIZER
```
fun normalize(s: String): String {
    val lower = s.toLowerCase(Locale.US)
    val out = StringBuilder()
    for (i in 0 until lower.length) {
        val c = lower[i]
        if (Character.isLetterOrDigit(c) || KEEP.contains(c)) out.append(c)
    }
    return out.toString()
}
```
`KEEP` from `<clinit>` = `['<', '>', '(', ')', ':', '{', '}', ',', '.']`
(`const/16 60,62,40,41,58,123,125,44,46`). Whitespace, quotes, `=`, `;`, `+`, `-`,
`/` etc. are discarded. The class also contains the Smob marker string.

### `InteractiveLessonValidatedInputFragment$setupViews$2->invokeSuspend` @10985684, 75 insns
```
vm.l <- Lum/a.a                        // validating state
val user = vm.S
val expected = vm.R?.a ?: throw ...
val normalizedEqual = normalize(user).equals(normalize(expected))
val exactEqual      = user.equals(expected)
val result = when {
    !normalizedEqual -> Lqm/g;        // INCORRECT (singleton)
    exactEqual       -> Lqm/e;        // CORRECT (singleton)
    else             -> Lqm/f(user, expected)   // CORRECT WITH PARTIAL MATCH
}
vm.b0(user)
vm.Z(result)
```
`Lqm/f` has two String fields `h` (user) and `i` (expected).

### `base/c$onValidatedInputExecuted$1->invokeSuspend` @10939224, 144 insns
`delay(300)` then `when(result)`:
- `Lqm/e` → `V()` (lessonSolvedCorrectly)
- `Lqm/f` → `b0(f.h)` + `W(f)` (lessonSolvedCorrectlyWithPartialMatch)
- `Lqm/g` → `X()` (lessonSolvedIncorrectly)
then posts `e = lessonBundle.b` and clears `f=FALSE`.

## Why this matters for offline reconstruction
Case-insensitive, punctuation-insensitive matching is a **client-side** algorithm, fully
reproducible from shipped content. M05 listed `validatedInput` expected-answer matching as
`UNKNOWN`; it is now `VERIFIED_STATIC`.

## Remaining uncertainty
- `Interaction$ValidatedInput.e : String` and `f : String[]` purpose = `UNKNOWN`
  (likely keyboard / allowed-answer hints; not decoded).
- Why the partial-match branch exists (analytics tolerance vs feedback) = `INFERRED`.
'''),
dict(file='09_WebViewLesson.md',title='Interactive WebView lesson & activity-result messages',smali='WebViewLessonViewModel.smali.txt',body=r'''
## VERIFIED_STATIC
- `Lcom/getmimo/ui/lesson/interactive/webview/c;` = `InteractiveWebViewLessonViewModel`
  (9 methods: `E()` 57 insns, `Q/S/T()` booleans, `a0()`, `j0(cont)` 75 insns).
- `Lcom/getmimo/ui/lesson/interactive/webview/b;` = `InteractiveWebViewLessonFragment`.
- `WebViewActivityResult` enum constants (from `<clinit>`): `mimo.activity.correct`,
  `mimo.activity.wrong`, `mimo.activity.completed` (M05 counted 217/217/90).
- `assets/lesson-webview.js` + `lesson-webview-fonts.js` are injected into
  `Lcom/getmimo/ui/lesson/interactive/webview/a;` and `EmbeddedLessonWebView`.
- `WebViewType` enum has an `UNLOCK` constant; `Lte/g;->a(XmlPullParser)` maps the
  `<webview ...>` tag attributes `visible-if`, `version`, `style`, `interaction`, `content`.
  It resolves `unlock` / `embedded` / other to `WebviewType.e/d/c/b` and HTML-escapes `#`→`%23`.

### Client-side completion path — VERIFIED_STATIC
`base/c;->U()` (lessonSolvedAndProceedToNextLesson) is called from
`webview/c;->j0(cont)` and
`InteractiveWebViewLessonFragment$goToNextPage$1` (error string
`"Error storing unlock activity lesson progress"`).
`webview/c;->j0` also calls `Lgm/h` interaction-type logic.

## Boundary
`mimo.activity.*` messages are WebView→native events (`lesson-webview.js` `postMessage`
JSON `{documentID, ...}`), **not** server responses. M05 already established the JS only
relays gesture/activity/focus/height/ready. No answer evaluation is performed in JS.

## Remaining uncertainty
- Exact mapping from `mimo.activity.correct|wrong|completed` payload to `Y(true/false)`/`U()`
  = `INFERRED` (call sites exist, full argument decoding incomplete).
- `WebviewType` version/style semantics = `UNKNOWN`.
'''),
dict(file='10_ExecutableLessonViewModel.md',title='ExecutableLessonViewModel (Orbit MVI) — offline solution check',smali='ExecutableLessonViewModel.smali.txt',body=r'''
## VERIFIED_STATIC — M05 code-execution boundary resolved
`Lcom/getmimo/ui/lesson/executable/q;` = `ExecutableLessonViewModel` (46 inner-class votes).
Constructor takes 32 injected dependencies; state class `Lzl/z;`; MVI container
`Lorg/orbitmvi/orbit/…`. 9 methods.

### `q;->I(Ldm/i; LessonBundle; ArrayList; LessonContent$Executable; Z)Ldm/i` @10912932, 114 insns
**This is the answer validator for `executableFiles` lessons.**
```
val userContents    = codeFiles.map { it.getContent() }          // ArrayList<String>
val solvedContents  = executable.files.map { it.getSolvedContent() }  // shipped
if (userContents == solvedContents) return currentState          // CORRECT
else {
    // Ldm/g(emptyList) + Ldm/h(...) error state
    log(IncorrectSolutionException())
    return Ldm/h(...)                                            // INCORRECT
}
```
The comparison is `ArrayList.equals()` on **exact strings**, in file order. Therefore the
shipped `solvedContent` field alone is sufficient to decide correctness offline; no remote
code execution is required for that decision. M05 asked whether `solvedContent` suffices —
answer: **yes for the correctness check** (`VERIFIED_STATIC`).

### `q;->E(container)LlessonProgress` @10913380, 57 insns
`createLessonProgress(bundle, state.h(startedAt), tries, state.e(attempts))`, where
`tries` uses `if (state.f) 1 else min(...)` — exact condition `INFERRED`.

### `q;->F(Lym/h; Lzl/z;)V` @~10913600, 248 insns — local hints
For `TutorialType.GuidedProject`, maps the selected file name
`style.css / index.html / script.py / script.js` to static maps `Lcm/b.a..d` keyed by
lessonId, extracts identifiers and emits `Lep/v`, `Lep/y` hint/highlight events.

### `q;->J(...)` (118 insns) builds `Lbe/n0` analytics with
`ExecutableLessonRunResult`, `lessonId`, `tutorialId`, `tutorialVersion`, `trackId`,
`duration` (`Seconds.secondsBetween(startedAt, now)`), `attempts`, file dump or
`"Lesson passed"`.
### `q;->K(x10/b, cont)` = `updateCodeExecutionState` (Orbit intent).
### `q;->H(Lo70/m;)` returns a coroutine Job; `q;->G()` 12 insns.

## Boundary — NOT reconstructed
`POST /v1/code/runfiles` and `/v1/tutorials/{id}/runFiles` are Retrofit endpoints referenced
by the client; **no server response bodies, no server business logic** were reconstructed.
Browser preview is local: `Ldg/a;<clinit>` contains a shipped HTML template with
`<link rel="stylesheet" href="style.css">` and `<script src="script.js">`.

## Remaining uncertainty
- Whether `q->I` is used for *all* executable lessons or only for guided-project variants
  = `UNKNOWN` (callers: 1, from an MVI reducer not fully decoded).
- SQL / HTML / CSS / JS exercise execution via an external runner remains a client-side
  boundary = `UNKNOWN` on the server side.
'''),
dict(file='11_DSL_LessonParser.md',title='XML DSL parser (`Lte/c` and module parsers)',smali='DSL_LessonParser.smali.txt',body=r'''
## VERIFIED_STATIC — technology recovered
The lesson DSL is **XML-like text parsed with `org.xmlpull.v1.XmlPullParser`**, not a regex
and not a JSON sub-schema. `Lte/c;->b(String) : ArrayList<LessonModule>` @14378108,
400 instructions:

```
val factory = XmlPullParserFactory.newInstance()
factory.setNamespaceAware(true)
val p = factory.newPullParser()
p.setInput(StringReader(html))
val modules = ArrayList<LessonModule>()
while (p.next() !in (END_DOCUMENT, ...)) {
    when (p.name) {
      "p"        -> modules += Lte/d.a(p)      // LessonModule$Paragraph
      "code"     -> modules += Lte/a.a(p)      // LessonModule$Code
      "selection"-> modules += Lte/e.a(p)      // LessonModule$Selection
      "img"      -> modules += Lte/c.a(p)      // LessonModule$Image
      "webview"  -> modules += Lte/g.a(p)      // LessonModule$Webview
      "database" -> modules += Lte/b.a(p)      // LessonModule$Database
      "html","body" -> skip
      else       -> log("skipping <tag>") + skip
    }
}
```
Per-module `try/catch` logs `"could not parse <x> module for lesson <id>"` and emits
analytics `xml_parse_error_module` / `xml_parse_error_skipped` via `Lpe/a.b`.

### Module parsers (verified signatures)
| Class | Method | Output | insns |
|---|---|---|---|
| `Lte/a;` | `a(XmlPullParser)` | `LessonModule$Code` | 490 |
| `Lte/a;` | `b(XmlPullParser)` | `SpannableStringBuilder` (inline `<text value=... type=.../>`) | 97 |
| `Lte/d;` | `a(XmlPullParser)` | `LessonModule$Paragraph` | 291 |
| `Lte/d;` | `c/d/e(XmlPullParser)` | attribute/visibility extraction | 105/43/65 |
| `Lte/e;` | `a(XmlPullParser)` | `LessonModule$Selection` | 288 |
| `Lte/b;` | `a(XmlPullParser)` | `LessonModule$Database` | 92 |
| `Lte/f;` | `a(XmlPullParser)` | `Table` | 176 |
| `Lte/g;` | `a(XmlPullParser)` | `LessonModule$Webview` | 228 |

### Verified tag/attribute vocabulary (DEX string constants)
`p`, `code`, `content`, `text`, `value`, `type`, `option`, `interaction`, `selection`,
`output`, `webview`, `visible-if`, `correct`, `always`, `wrong`, `strong`, `br`, `src`,
`startIndex`, `endIndex`, `version`, `style`, `codelang`, `name`.
`ModuleVisibility` enum: `ALWAYS("always")`, `CORRECT("correct")`, `WRONG("wrong")`
(`<clinit>` @`EVIDENCE/DISASM/ModuleVisibility.smali.txt`).
`ParserModule` enum: `CODE`, `PARAGRAPH`, `SELECTION`.
`Interaction` subclasses: `FillTheGap{c:List<Option>}`, `Selection{c,d,e}`,
`Spell{c,d}`, `ValidatedInput{c,d,e,f}`.
`LessonModule` subclasses: `Code`, `Paragraph`, `Image`, `Webview`, `Selection`, `Database`.

## Original shipped samples
`SAMPLES/ORIGINAL_*.json` are byte-exact APK members (`MANIFEST.json` has SHA-256).
`ORIGINAL_testdata_127-0-1.html` contains a `spell` interaction (v753 English curriculum
contains no `spell` tag in the sampled set).

## Remaining uncertainty
- Full 490-instruction `Lte/a.a` (option/offset/interaction construction) is only
  partially decoded = `UNKNOWN` in detail; its inputs/outputs are verified.
- `Tag` and `Attribute` enum ordinal→string tables are not completely enumerated = `INFERRED`.
'''),
dict(file='12_LessonInteractionTypeSelector.md',title='Lgm/h — interaction/renderer selection',smali='LessonInteractionTypeMapper.smali.txt',body=r'''
## VERIFIED_STATIC
`Lgm/h;-><clinit>` creates `Regex("<\\s*body[^>]*>(.*?)<\\s*/\\s*body>")` (extracts the
HTML body before the XmlPullParser stage). `Lgm/h;->a(List) : LessonInteractionType`
@12460480, 437 instructions, dispatches on `LessonModule` instance types.

### Nine renderer types (all recovered; M05 knew only 6)
`LessonInteractionType` subclasses, each carrying `a:String interactionTypeName`:
| Type | Marker string | Trigger |
|---|---|---|
| `InteractiveWebView` | `interactive_webview` | `LessonModule$Webview` |
| `FillTheGap` | `fill_the_gap` | `Interaction$FillTheGap` |
| `Spell` | `spell` | `Interaction$Spell` |
| `Selection` | `selection` | `Interaction$Selection` |
| `ValidatedInput` | `validated_input` | `Interaction$ValidatedInput` |
| `SingleChoice` | (selection variant) | `LessonModule$Selection` |
| `MultipleChoice` | `multiple_choice` | `LessonModule$Selection` |
| `Reveal` | — | `LessonModule$Code` present |
| `None` | — | no code / no interaction |

Also reads `Interaction.a:Z (isDefault)` and checks `LessonModule$Paragraph` instances to
choose `slide` vs other layouts.

## Callers — VERIFIED_STATIC
`Lcom/getmimo/ui/lesson/interactive/d;->E(LessonContent$Interactive, LessonBundle)V`
(InteractiveLessonViewModel) and
`Lcom/getmimo/interactors/chapter/c;->a(LessonBundle, cont)V` (GetLessonContentType).
`d->E` also handles `hardModeLessonModules` / `getHasDifferentHardModeContent()` /
`hardModeModulesOrDefault()` and posts `Lgm/g` (type + content + bundle + index) to LiveData.

## Remaining uncertainty
- Exact `SingleChoice` vs `MultipleChoice` predicate = `UNKNOWN`.
- `Reveal` vs `None` full condition chain = `UNKNOWN` (437-insn method).
'''),
dict(file='13_AssetLoaders.md',title='Asset loaders + locale selection + DefaultTrackLoader',smali='AssetTracksLoader.smali.txt',body=r'''
## VERIFIED_STATIC — exact asset paths
`Lye/b;` fields: `a:Landroid/content/res/AssetManager;`, `b:Lke/a;` (locale provider),
`c:Ljava/util/LinkedHashMap;` (static).

`<clinit>` (97 insns):
```
ContentLocale.values().associate { it -> "lessons-" + it.getLanguageString() }
  → then { locale -> "lessons-<lang>/tracks" }
```
`ContentLocale` enum (`<clinit>` @9681384, 141 insns) = `RU(ru), EN(en), ES(es), PT(pt),
DE(de), FR(fr), IT(it), ID(id), TR(tr), PL(pl)` — 10 locales, matching M05's 10,298 files.

| Method | Path built | Action |
|---|---|---|
| `b(J)` | `"lessons-<lang>/tracks/tutorial-<id>.json"` | `AssetManager.open(path)` |
| `d()` | `"lessons-<lang>/tracks/tracks.json"` | `AssetManager.open(path)` |
| `c()` | `"file:///android_asset/lessons-common/icons"` | image base URL |
| `a(Tutorial)` | — | filters GuidedProject chapters/lessons by `CodeLanguage` and `LessonContentType.EXECUTABLE_FILES` |

`Lye/d;` is a second loader reading from `context.getFilesDir().getAbsolutePath()` (downloaded
/ updated content variant); its `b(J)`/`d()` use the same `tutorial-<id>.json` / `tracks.json`
names.

`Lcom/getmimo/data/content/tracks/b;` = `DefaultTrackLoader` (4 inner-class votes):
- `a(J,I,I) : kotlinx.serialization.json.JsonObject` — reads a stream, `Json.decodeFromString`,
  applies version/offset selectors;
- `b(J,cont)` launches `DefaultTrackLoader$getTutorial$2`;
- `c(InputStream) : String` — `InputStreamReader(UTF-8)` → `BufferedReader` → `readText()`;
- `d(String) : String` — rewrites image references (`"/"` substitution via `Ls7/a.n`).
Inner class `DefaultTrackLoader$getExecutableLesson$2` contains the string
`"executableContent"`.

## Remaining uncertainty
- Which loader (`Lye/b` assets vs `Lye/d` filesDir) wins at runtime, and the update/download
  trigger = `UNKNOWN`; selection is a DI binding not decoded here.
- `Lye/b.a(Tutorial)` full filter predicate = `INFERRED`.
'''),
dict(file='14_DefaultTracksRepository.md',title='DefaultTracksRepository — track/tutorial/chapter loading',smali='DefaultTracksRepository.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/data/content/tracks/c;` = `DefaultTracksRepository` (7 votes).
Constructor `(Lye/e; Lfe/a;)V`. Methods:
`a(J,I,I,cont)` 25, `b(J,I,I,cont)` 25, `c()J` 18 (current `publishSetVersion`),
`d(J,cont)` 226 (load single `TrackJson`), `e(J,cont)` 86,
`f(List,cont)` 102, `g(cont)` 69 (5 callers), `h(cont)` 86 (3 callers),
`i(J,cont)` 409 (`loadTrackWithChapters$1`).

`i(J)` reads `TrackJson` via `d(J)`, then maps:
```
Track(id, version, title, descriptionContent, isNew, isHidden, iconBanner, sections)
```
For each `SectionJson` it reads `getName()`, `getDescription()`, `getTutorialIds()`,
resolves each tutorial id through the loader, and builds `Chapter` / `Tutorial` models
with `isCompleted` flags from `CompletionRepository`. It excludes a set of `TutorialType`s
(`GuidedProject`, `MobileProject`, `Quiz`, `RecreateProject`, `GuidedProjectOptional`)
from the chapter-loading path — `INFERRED` exact reason.
`c()` is called by `LessonProgressRepository.createLessonProgress` to stamp
`publishSetVersion`.

## Callers — VERIFIED_STATIC
`PathMapViewModel`, `GetPathMapState`, `ChapterViewModel`, `LessonProgressRepository`,
`GetPracticeTrackList`.

## Remaining uncertainty
- Complete 409-instruction `i()` state machine not decoded line-by-line = `UNKNOWN` in detail.
- Caching/invalidation policy between asset JSON and Room completion state = `UNKNOWN`.
'''),
dict(file='15_GetPathMapState.md',title='GetPathMapState — unlock state machine',smali='GetPathMapState.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/interactors/path/d;` = `GetPathMapState`; its `invoke$3.invokeSuspend`
@10129608, 659 instructions constructs the whole path-map state `Lvn/n`.

### Verified state classes (constructed only here)
| Class | Meaning (from `toString()` strings) |
|---|---|
| `Lvn/d0` | `Completed(id=…, isProLocked=…)` — built when `Tutorial.isCompleted()` |
| `Lvn/e0` | `Locked(id=…, isProLocked=…)` |
| `Lvn/g0` | `Unlocked(id=…, isProLocked=…)` |
| `Lvn/h0` | `UnlockedButNoKeys(id=…)` |
| `Lvn/d` | chapter item `(id,title,isCompleted,isCompletedInHardMode)` |
| `Lvn/y` / `Lvn/a0` | `Locked(index=…)` / `Unlocked(index=…)` section states |
| `Lvn/a` / `Lvn/b` | track-level `Locked(trackId…)` / `Unlocked(trackId…)` |

### Verified rules
- Tutorials of type `Challenge` are excluded from the path item list
  (`Set.of(TutorialType.Challenge).contains(t.type)`).
- A `lastOrNull()` over already-built items is used together with
  `TutorialType.isRequired()` and `Lvn/i0.d()` to decide whether the next required
  predecessor is completed → sequential unlock.
- `Tutorial.isCompleted()` → `Lvn/d0`; chapter items get `isCompleted` and a hard-mode
  flag from `Lds/w.c(Set, trackId, tutorialId, chapterId)`.
- `Tutorial.getHasProgress()`, `TutorialType.PracticeOptional`, a Pro subscription tier
  (`Lyg/c.c`), dev-menu overrides (`Lsk/a.d()/e()`), and an integer keys count decide
  `Locked` / `UnlockedButNoKeys` / `Unlocked`.
- Section states are built by `Lcc/b;->y(List, Z, Integer?, Z, Z) : ArrayList`
  (verified constructor callers `Lvn/y`, `Lvn/a0`, `Lvn/v`, `Lvn/w`).
- Final state `Lvn/n(track, sectionStates, selectedSectionIndex, dialogs, nextSectionState, …)`.

## Remaining uncertainty — explicit
The **exact boolean combination** selecting `Locked` vs `UnlockedButNoKeys` vs `Unlocked`
is `UNKNOWN` (registers `v14`, `v24`, `v31`, `v43`, `v46` are junk-obfuscated and the
659-instruction coroutine has 3 suspension labels). This is the precise unresolved
component for the unlock rule. `CanOpenChapterWithKeys` (dossier 19) is the other half.
'''),
dict(file='16_CompletionRepository.md',title='CompletionRepository — local completion attachment',smali='CompletionRepository.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/data/source/local/completion/a;` = `CompletionRepository` (7 votes),
8 methods, constructor uses `Leg/f;` (Room database wrapper).

`b(Track, cont)` = `CompletionRepository$attachTutorialCompletionToTrack$1` @9981172,
178 instructions:
```
val rows = Room.query("SELECT ... tutorial completions WHERE trackId=?", ...)  // via Leg/a
val byTutorialId = rows.associateBy { it.getTutorialId() }
return track.copy(sections = sections.map { it.copy(tutorials = tutorials.map { t ->
    t.copy(isCompleted = byTutorialId[t.id]?.isCompleted ?: false,
           completedChapters = ..., hardMode = ...) }) })
```
Verified entities: `Lcom/getmimo/data/model/room/TutorialCompletion;` with getters
`getTutorialId()`, `isCompleted()`, `completedChapters`; Room SQL for
`chapter_completions` (PK `chapter_id,track_id`) and `tutorial_completions`
(PK `tutorial_id,track_id`) is in M05 `EVIDENCE/ROOM_SQL.txt`.

## Remaining uncertainty
- Exact Room query strings behind `Leg/a` are 269-table SQL strings catalogued by M05 but
  not re-decoded here = `INFERRED` for this specific DAO method.
- How server sync merges completions into these tables = `UNKNOWN` / server-owned boundary.
'''),
dict(file='17_ChapterFinishedViewModel.md',title='ChapterFinishedViewModel — online/offline chapter end',smali='ChapterFinishedViewModel.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/ui/chapter/chapterendview/main/f;` = `ChapterFinishedViewModel` (13 votes).
Inner classes `ChapterFinishedViewModel$handleOfflineState$1` and
`$handleOnlineState$1` (+ `$1$1`, `$1$2`) exist — M05 already noted them.

`handleOfflineState$1.invokeSuspend` (48 insns):
```
val vm = this.b
vm.R(cont)      // f->R = handleChapterAlreadyCompletedState
catch (t) { log(t) }
```
i.e. **offline chapter end falls back to the already-completed local state**, with no server
call. `f->G` = `handleOnlineState`, `f->F` =
`getChapterEndSuccessStateWithRetry`, `f->E` = `consumeKeyIfNeeded`,
`f->R` = `handleChapterAlreadyCompletedState`, `f->O` = `onContinue`,
`f->I`/`S` = `onChapterFinishedScreenShown`, `f->M` = `shouldShowRatingBottomSheet`,
`f->N` = `shouldShowStreakChallengeScreen`, `f->H` = refresh after streak-goal purchase.

Strings in the class: `streakChallengeCoinPrice`, `userCoins`,
`DAILY_GOAL_NOT_REACHED|REACHED|ALREADY_REACHED_EARLIER_TODAY`
(`ChapterFinishedSuccessType`), `chapterFinishedStreakChallengeFragment`, etc.

## Offline significance
This is the precise client-side method behind M05 run-002/003's
"Connect to the internet to progress further" while local content remained visible: the
chapter-end screen branches offline to local completion state instead of fetching
server-owned rewards. `VERIFIED_STATIC` for the branch; `VERIFIED_RUNTIME` for the screen
text comes from M05 run evidence.

## Remaining uncertainty
- Success-type thresholds (daily goal, streak, XP) = `UNKNOWN`, require server response bodies
  which M06 deliberately did not reconstruct.
'''),
dict(file='18_NetworkUtils.md',title='NetworkUtils — exact offline gate',smali='NetworkUtils.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/network/a;` = `AndroidNetworkUtils`; `Lcom/getmimo/network/b;` =
`ConnectivityManagerNetworkMonitor`.

`a()Z` @10174360, 38 instructions:
```
val cm: ConnectivityManager
val net = cm.getActiveNetwork()          ?: return false
val caps = cm.getNetworkCapabilities(net) ?: return false
if (caps.hasTransport(TRANSPORT_WIFI))     return true
if (caps.hasTransport(TRANSPORT_CELLULAR)) return true
return false
```
`b()Z` @10174512 = `!a()` (isOffline). `a()` has 14 callers, `b()` 13 callers across
`LessonProgressRepository`, `ChapterViewModel`, `GetPathMapState`, AiTutor, practice tabs,
IAP, notifications.

### Verified client-side blocking method
`LessonProgressRepository.postUnsyncedLessonProgress(cont)` @`EVIDENCE/DISASM/LessonProgressRepository.smali.txt`:
```
if (!networkUtils.a()) {
    log("No internet connection, not posting unsynced lesson progress")
    throw NoConnectionException(...)
}
launch { /* POST unsynced rows */ }
```
Verb exact log string from DEX. `storeAndPostAllLessonProgress` calls
`moveLessonProgressFromQueue()` **before** this gate.

## Runtime correlation (M05, no new M06 run)
M05 `42002808217` cold start with `Active default network: none` showed
`NetworkUnknown` / `UnknownHostException` for analytics `cdp.customer.io`, no FATAL/ANR,
and the first three offline UI hierarchies were byte-identical to online. This is consistent
with the `hasTransport` gate above. `VERIFIED_BOTH`.

## Remaining uncertainty
- Whether `NetworkUtils` also checks `NET_CAPABILITY_VALIDATED` = `UNKNOWN` (only two
  `hasTransport` calls were recovered; no capability check visible).
'''),
dict(file='19_CanOpenChapterWithKeys.md',title='CanOpenChapterWithKeys — keys gate',smali='CanOpenChapterWithKeys.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/interactors/chapter/a;` = `CanOpenChapterWithKeys` (constructor injects
`Lcom/getmimo/data/source/remote/keys/a;` = `DefaultKeysRepository`).

`CanOpenChapterWithKeys$invoke$1.invokeSuspend` @10104004, 102 insns:
```
val keysRepo = this.a.a
val flag = keysRepo.c() : Boolean?          // feature/config flag
if (flag == false) {
    val count = keysRepo.f.first() : Int    // StateFlow<Int> key balance
    return count > 0
}
return <other branch>                      // not fully decoded
```
`Lvn/h0` (`UnlockedButNoKeys`) is the UI state for `count == 0`. `Lsk/a` dev-menu can override.

## Remaining uncertainty
- The `flag == true` branch and the exact `Boolean` return = `UNKNOWN`.
- Key consumption (`ChapterFinishedViewModel.E consumeKeyIfNeeded`) and any server-side
  balance update = `UNKNOWN` / server-owned boundary.
'''),
dict(file='20_DataStoreUserPreferences.md',title='DataStore / SharedPreferences local state',smali='DataStoreUserPreferences.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/data/local/a;` = `DataStoreUserPreferences` (26 methods). Verified string
constants from DEX / M05 `EVIDENCE/STORAGE_AND_ONBOARDING_STRINGS.txt`:
`completed_hard_mode_chapters`, `KEY_HARD_MODE_COMPLETED_LESSON_IDS`,
`onboarding_user_daily_goal`, `dailyGoal`, `first_run`, `path_overview`, hard-mode flags.
`base/c;->d0()` calls `a.f(cont)` returning a Boolean and `a.p()` (clear/reset), i.e. the
wrong-feedback block reads a locally stored preference before deciding whether to show
extra feedback.

`ChapterViewModel` stores `KEY_HARD_MODE_COMPLETED_LESSON_IDS`;
`MainActivity.onCreate` reads `onboarding_user_daily_goal` / `dailyGoal`.

## Persistence architecture (VERIFIED_STATIC from M05 + M06)
Room database with 269 tables (M05), identity hashes
`08b926448d86528e697981ddd30459f7` and `2b8ab6d303d9a501bd8c8fb78d8352fc`;
`lesson_progress` 11 columns with `in_queue`; `chapter_completions`,
`tutorial_completions`; DataStore preferences; in-memory `LiveData`/`StateFlow`;
`LessonProgressQueue` unsynced rows survive process death by virtue of Room.

## Remaining uncertainty
- Exact DataStore filename, migrations and every preference key = `UNKNOWN` in detail.
- Force-stop / process-recreation restoration was not runtime-tested in M06 = `UNKNOWN`.
'''),
dict(file='21_LessonBundle_and_LessonContent.md',title='LessonBundle / LessonContent data models',smali='LessonBundle.smali.txt',body=r'''
## VERIFIED_STATIC field tables
`Lcom/getmimo/ui/lesson/interactive/LessonBundle;` (Parcelable):
`a:J lessonId`, `b:I chapterIndex`, `c:I sectionIndex`, `d:J`, `e:J tutorialId`,
`f:J trackId`, `g:J`, `v:I tutorialVersion`, `w:I`, `x:TutorialType`, `y:ChapterType`,
`z:Z`, `A:Z`, `B:Z isPracticeProgress`, `C:Z`, `D:Integer?`, `E:String?`,
`F:LessonIdentifier`, `G:Z`, `H:I`, plus `CREATOR`, `I` (empty instance).

`LessonContent$Interactive`: `lessonModules:List`, `hardModeLessonModules:List`;
`getHasDifferentHardModeContent()`, `hardModeModulesOrDefault()`.

`LessonContent$Executable`: `instructions:String`, `preselectedFileIndex:int`, `files:List`,
`getHasBrowserOutput()`, `getHasInputConsole()`.
`LessonContent$Executable$File`: `name`, `codeLanguage`, `content`, `solvedContent`.

`Lesson`: `id:J`, `title:String`, `images:List`, `contentType:LessonContentType`,
`hardModeSelected:boolean`.
`LessonContentType` enum: `INTERACTIVE`, `EXECUTABLE_FILES`.
`TutorialType`: `Learn, MobileProject, Challenge, Quiz, GuidedProject,
GuidedProjectOptional, RecreateProject, PracticeRequired, PracticeOptional`.
`ChapterType`: `NONE, PRACTICE_LEVEL_1..3, QUIZ, CHALLENGE_DIFFICULTY_0..4`.
`CodeLanguage`: `NONE, BASH(.bash), CPP(.cpp), CSHARP(.cs), CSS(style.css),
CSV(data.csv), …` (full enum not enumerated here).

## Remaining uncertainty
- Field names for `LessonBundle` are `INFERRED` from usage in `createLessonProgress`,
  `f0`, `U()` and `toString()` strings; DEX stores only letters `a..H`.
'''),
dict(file='22_BaseFragment_and_NonInteractive.md',title='InteractiveLessonBaseFragment / NonInteractive / no-interaction path',smali='InteractiveLessonBaseFragment.smali.txt',body=r'''
## VERIFIED_STATIC
`Lcom/getmimo/ui/lesson/interactive/base/b;` = `InteractiveLessonBaseFragment` (11 votes,
29 methods). `T(View,Bundle)` wires `RunButton`, `InteractionKeyboardContainerView`,
`CodeBodyView`, `CodeHeaderView`, `DatabaseView`, `EmbeddedLessonWebView` and registers
`onLessonWebViewError(ConsoleMessage,String)` callbacks. `onViewCreated$3` emits
analytics properties `webview_type`, `webview_provider`, `webview_version`.

`Lcom/getmimo/ui/lesson/interactive/nointeraction/a;` = `NonInteractiveLessonFragment`
(20 methods). `goToNextPage$1.invokeSuspend` calls `base/c.U()` — the no-interaction
completion path (`lessonSolvedAndProceedToNextLesson`), which records `tries=1` if no
wrong answer was latched.

`Lcom/getmimo/ui/lesson/interactive/c;` = `InteractiveLessonFragment` (2 votes),
`d;` = `InteractiveLessonViewModel` (4 votes, 5 methods incl. `F`, `G`, `H` coroutines).

## Verified UI-state types
`RunButton$State` (`a` enabled / `b` disabled), `InteractionKeyboardButtonState`
(`a`, `b`, `c`), `jm/q(List,boolean)`, `jm/m`/`jm/o` solution feedback,
`jm/j` paragraph, `jm/i` image, `jm/k` webview render items, `Lym/f` interaction event.

## Remaining uncertainty
- Full Compose/XML layout hierarchy and view-binding details = `UNKNOWN` (not needed for
  behavioural reconstruction; M05 already captured runtime UI hierarchies).
'''),
]
for d in DOSSIERS:
    txt=HEADER.format(title=d['title'],smali=d['smali'])+d['body'].strip()+'\n'
    (D/d['file']).write_text(txt,encoding='utf-8')
    print('wrote',d['file'],len(txt))
