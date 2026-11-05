# MISSION 07 — 04 ANSWER VALIDATION AT RUNTIME

**Baseline:** M06 static bytecode + M07 live Frida invocation of the ORIGINAL
app (`com.getmimo`, 9.35). Evidence:
`ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE3_ONLINE.jsonl` (914 events),
`FRIDA/STAGE3_ONLINE_DRIVER.log`, `m07_frida_stage2.js`,
`ANALYSIS/MISSION_06/EVIDENCE/DISASM/`, `ANALYSIS/MISSION_05/EVIDENCE/ROOM_SQL.txt`.
`SERVER CONFIRMED = 0`.

## E1 — `qm.i.a(String)` validatedInput normalizer — `VERIFIED_RUNTIME`
21 controlled inputs, direct invocation on the live app process. Static M06
reading said: lowercase with `Locale.US`, keep letters/digits plus
`< > ( ) : { } , .` (ASCII 60,62,40,41,58,123,125,44,46), discard whitespace
and all other punctuation. Runtime confirms and extends it:

| case | input | returned |
|---|---|---|
| exact / case_upper / case_lower | `D`, `D`, `d` | `d` |
| leading/trailing/both whitespace | `  D`, `D  `, `  D  ` | `d` |
| repeated / internal whitespace | `D   O   G`, `D O G` | `dog` |
| tab+newline | `D\tO\nG` | `dog` |
| allowed punctuation | `<button>Hi:</button>{a,b.c}` | `<button>hi:<button>{a,b.c}` |
| allowed-all | `< > ( ) : { } , .` | `<>():{},.` |
| disallowed-all | `-_=+;!?@#$%^&*` | `` (empty) |
| disallowed mixed | `a+b-c=d;e/f"g'h!i?j@k#l$m%n^o&p*q` | `abcdefghijklmnopq` |
| digits | `A1b2C3` | `a1b2c3` |
| empty / only whitespace | ``, `   ` | `` |
| Unicode | `Café`, `Straße ÄÖÜ ß`, `你好` | `café`, `straßeäöüß`, `你好` |
| Turkish | `İstanbul ı I i` | `istanbulıii` |
| emoji | `D🐶` | `d` |
| empty | `''` | `''` |

New runtime facts beyond M06: the filter is **Unicode-aware** (`Character`-
class letter/digit, not ASCII-only) — `é`, `ß`, `ä`, `ö`, `ü`, CJK and the
dotless `ı` survive; the combining dot of `İ` and the emoji are dropped.
Whitespace includes tabs/newlines. This is the exact normalizer used for the
"normalized-only → partial match" branch, so `D O G`, `dog`, `DOG` and
`  d o g  ` all normalise to `dog`.

## E2 — `km.f.b(List)` selection validator — `PARTIALLY VERIFIED`
Static M06: returns `true` when the selected/correct flags of every `sm.a`
item agree (selection exercise). Runtime: the `empty` list case returned
`true` (vacuous truth). All 7 constructed cases failed with
`Error: a(): argument types do not match any of: .overload('java.lang.CharSequence','boolean','boolean','boolean')`
— a Frida argument-coercion problem with `sm.a.<init>(CharSequence,Z,Z,Z)`,
not an app result. Stage 4 replaces the JS string with an explicit
`java.lang.String`; until it succeeds the non-empty truth table is `UNKNOWN`.
No conclusion is drawn from the failed cases.

## E3 — `LessonProgress.isSolvedCorrectly()` — `VERIFIED_RUNTIME`
20 real `LessonProgress` objects (`lessonId=151403, tutorialId=904,
tutorialVersion=2, trackId=1, publishSetVersion=753, inQueue=true`) with
`tries ∈ {-1,0,1,2,5}` × `attempts ∈ {-1,0,1,3}`:

* `tries = -1` → `false` (all 4 attempts)
* `tries = 0`  → `false` (all 4 attempts)
* `tries = 1, 2, 5` → `true` (all 12 combinations)

Exact predicate: **`tries >= 1`**, independent of `attempts`. This CONFIRMS the
M06 bytecode correction and **corrects M05**, which had inferred
`attempts >= 1`. `toString()` of a constructed row (verbatim):
`LessonProgress(lessonId=151403, completedAt=2026-11-05T12:18:27.559Z, startedAt=2026-11-05T12:18:27.559Z, tries=-1, tutorialId=904, tutorialVersion=2, trackId=1, publishSetVersion=753, attempts=-1, isPracticeProgress=false, inQueue=true)`.

## E4 — `com.getmimo.network.a` offline gate — `VERIFIED_RUNTIME`
With a real `ActivityThread.currentApplication()` context and network ONLINE:
`a()` → `true`, `b()` → `false`. M06 disassembly of `NetworkUtils.a()`
@10174360 used `getActiveNetwork`/`getNetworkCapabilities`/two `hasTransport`
calls; `a()`/`b()` are two distinct checks (naming `INFERRED`). Offline values
are measured in `09_OFFLINE_EXECUTION_RESULTS.md`.

## E5 — `te.c.b(String)` XML/DSL parser — `UNKNOWN` (stage-3 attempt)
`te.c.<init>(te.d,te.a,te.e,te.g,te.b,pe.a)` cannot be constructed with null
dependencies: `java.lang.NullPointerException: … getClass() on a null object
reference`. Stage 4 instead uses `Java.choose('te.c')` to call `b()` on a live
DI-created parser instance. Until that succeeds, the six module parsers remain
`VERIFIED_STATIC` only (M06).

## E6 — `gm.h.a(List)` interaction-type selector — `PARTIALLY VERIFIED`
`emptyList` → `None(interactionTypeName=slide)` (the "slide"/non-interactive
type). M06 disassembly is 437 instructions with 59 callees; mapping of
non-empty `LessonContent$Interactive` lists to `LessonInteractionType` values
is not yet runtime-tabulated → `UNKNOWN`.

## Executable behavioural spec (answer validation, evidence-backed)
```
normalise(s)  = lowercase(s, Locale.US)
                keep Character.isLetterOrDigit(c) OR c in "<>() :{},."
                (set = { '<','>','(',')',':','{','}',',','.' })
                drop everything else (incl. all whitespace)
isSolvedCorrectly(progress) = progress.tries >= 1
```
Feedback branches (M06 `setupViews$2` @10985684, rechecked in
`RUNTIME_TRACE/STATIC_DECODE/00_STATIC_DECODE_M07.md`):
* exact match → `c.V()` → `jm/m` feedback + `solutionFeedbackCorrect`;
* normalised-only match → `c.W()` → `jm/n(userInput, expectedInput, true, E)`
  + analytics `validated_input_execution_correct_partial_match`;
* mismatch → `c.X()`/`c.d0()` → `jm/o` 7-boolean feedback `solutionFeedbackWrong`.

Both `V()` and `W()` execute the same persistence spine:
`i0()` await browser output → `C=FALSE` → `d++` → `c0()` →
`tries = (C==TRUE) ? 0 : 1` → `H(tries,d)` → `e0(progress)` →
`sound.a(true)` → `f0(false, progress.isSolvedCorrectly())` → emit
`Long(lessonBundle.a)` → `I()`.
**M07 correction:** M06 reported `f0(true, isSolvedCorrectly())`; bytecode at
`V @0x180` and `W @0x19e` passes **false** as the first argument.

Shipped lesson content (ORIGINAL APK) gives exact expected answers used by M07
experiments: `assets/lessons-en/tracks/tutorial-904.json` lesson 151403 WebView
`correctLetter='D'`; `tutorial-1103.json` lesson 123420
`<selection multiple="multiple">` correct item `value=1` =
"To store information for later use". A generated index of 2,855 shipped
selection questions with their correct/wrong item texts is at
`ANALYSIS/MISSION_07/RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json`.

**Not yet VERIFIED:** live `onLessonRun$1` dispatch for a real answer, the
`lesson_progress` row written by `e0()`, and the resulting correct/wrong UI.
Those are targeted by the stage-4 controlled experiment; see
`05_ANSWER_STATE_TRANSITIONS.md` and `06_DATABASE_BEFORE_AFTER.md`.
