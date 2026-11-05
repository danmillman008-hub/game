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

## E2 — `km.f.b(List)` selection validator — `VERIFIED_BOTH`
Static M06: returns `true` when the selected/correct flags of every `sm.a`
item agree. Stage 3's seven constructed cases failed with a Frida
argument-coercion error (`sm.a.<init>(CharSequence,Z,Z,Z)`); passing an
explicit `java.lang.String` fixed it and stage 4 measured all 8 cases:

| case | items (selected/correct) | `km.f.b` |
|---|---|---|
| `empty` | `[]` | `true` (vacuous) |
| `one_match_true_true` | `(true,true)` | `true` |
| `one_mismatch_true_false` | `(true,false)` | `false` |
| `one_mismatch_false_true` | `(false,true)` | `false` |
| `one_false_false` | `(false,false)` | `true` |
| `three_all_match` | `(T,T),(F,F),(T,T)` | `true` |
| `three_one_wrong` | `(T,T),(T,F),(T,T)` | `false` |
| `three_one_missing` | `(T,T),(F,T),(T,T)` | `false` |

Exact runtime predicate: **`∀ item: item.selected == item.correct`** (an all-
match/XNOR fold), independent of item text. Reproduced identically online and
offline (8 cases each).

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

## E5 — `te.c.b(String)` XML/DSL parser — `VERIFIED_BOTH`
`te.c.<init>(te.d,te.a,te.e,te.g,te.b,pe.a)` cannot be constructed with null
dependencies (NPE). At initial online attach no `te.c` instance existed in the
heap (`experiment_error`), but after app restart the offline session found a
live DI-created parser with `Java.choose('te.c')` and returned real module lists
for 5 controlled XML strings. Full table in
`10_CODE_EDITOR_AND_WEBVIEW_BOUNDARY.md`. `VERIFIED_RUNTIME`:
`Paragraph`, `Code(language,name,content,interactions,output,visibilty,collapsibleLines)`,
`Selection`/`SelectionItem`, `Image`; unknown tags dropped; malformed XML →
empty list.

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

**Stage 5 `VERIFIED_RUNTIME`:** a real wrong `Q` then correct `D` in shipped
lesson 151403 produced `Try again` → `Correct!` / `D O G` → next lesson and a
**new `lesson_progress` row for lesson 151403** (`tries=1, attempts=1,
in_queue=1`). See `05_ANSWER_STATE_TRANSITIONS.md` and
`06_DATABASE_BEFORE_AFTER.md`. The native `V()/W()/X()` dispatch for
*validatedInput/selection/fillTheGap* exercises remains `UNKNOWN`: stage 6
measured the fill-the-gap module and `RUN_DISABLED` state but did not submit a
native exercise answer.

## Stage 6 additions (`VERIFIED_RUNTIME`, run `42033599909`)
* `gm.h.a(nonEmptyList)` on a real shipped module list returned
  **`FillTheGap(interactionTypeName=fill_the_gap)`** — the non-empty mapping is
  now verified for this case (`interactionSelector#24` exit).
* `te.c.b()` on **real shipped lesson HTML** returned, verbatim:
  `[Paragraph(texts=[Let's do this step by step. To create a button, first we
  need an opening , <button>,  tag.], visibilty=ALWAYS), Code(content=<button>,
  interactions=[FillTheGap(isDefault=true, options=[Option(correct=true, text=,
  startIndex=0, endIndex=8)])], output=null, visibilty=ALWAYS, language=HTML,
  name=index.html, collapsibleLines=[]), Paragraph(texts=[Make sure to pick ,
  <button>, .], visibilty=WRONG)]`. A second shipped lesson added
  `Option(correct=false, text=</button>, startIndex=0, endIndex=0)` and
  `Option(correct=false, text=button, startIndex=0, endIndex=0)`. This confirms
  the `interaction type="fillTheGap"`, `option correct=` and
  `visible-if="wrong"` DSL semantics at runtime.
* `LessonProgressRepository.createLessonProgress` returned the real 11-field
  `LessonProgress` for lesson 151403 (see `03`/`06`).
* `isSolvedCorrectly()` returned `true` for the real rows 151410 and 151403,
  both with `tries=1`.
* `c.U()` returned `COROUTINE_SUSPENDED` on the first suspension and
  `kotlin.Unit` on completion — confirming it is a suspend function.
