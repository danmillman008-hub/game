# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · **branch** `arena/aebb90b7-game` · `SERVER CONFIRMED = 0`  
Evidence: `EVIDENCE/DISASM/*.smali.txt`, `SCHEMAS/METHOD_CATALOG_MIMO.json`,
`CALL_GRAPHS/*.json`, `METHOD_DOSSIERS/*.md`. Classification on every finding.

---

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
