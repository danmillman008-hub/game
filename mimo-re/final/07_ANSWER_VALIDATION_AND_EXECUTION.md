# 07 — Answer validation and code execution

Mimo grades with **two independent engines** and one shared contract: the client decides
nothing about correctness in the executable path, and everything in the interactive path.

---

# Part A — Interactive lessons (client-authoritative)

## A1. Model
Each assessed block carries its own answer model inside the markup (§06). There is no separate
answer key file, no separate answer network call, and no obfuscated answer database: the
answers *are* the code. Consequently the client can grade offline, instantly, and without
leaking anything beyond what the lesson already shows.

## A2. Grading algorithm (V offsets, V grammar)

```pseudo
checkFillTheGap(block, placed):
    correct = true
    for i, gap in block.gaps:                  # gaps ordered by startIndex
        want = block.flat[gap.start : gap.end]
        got  = placed[i]                       # text the learner put there
        correct &= (normalise(got) == normalise(want))
    return correct

checkValidatedInput(block, typed):
    return normalise(typed) == normalise(block.flat[block.input.start : block.input.end])

checkSelection(block, tapped):
    return set(tapped) == {item.value for item in block.items if item.correct}
```
Evidence that this is the real rule (not a guess):
* every one of the 17,526 authored ranges is in bounds of `flatten(content)` under the
  break→`\n` rule and **no** other candidate rule reproduces that in-bounds property;
* the authoring model has no place to put the expected text except those ranges: `<option>`
  with a range has **no content and no value** attribute (17,526 occurrences, zero exceptions);
* decoy chips are the only options with text, and they are **all** `correct="false"`
  (4,939/4,939) — i.e. the author writes distractors only.

## A3. Attempt and feedback semantics
| Signal | Evidence |
|---|---|
| Per-attempt counter persisted | `lessonProgress.attempts`, `tries` columns (Room schema) |
| Binary pass, no partial credit at lesson level | `hasPassed` boolean in progress rows; no score column |
| Remedial content on failure | `visible-if="wrong"` 13,043 modules |
| Escalation content on success | `visible-if="correct"` 143 modules |
| Hint before giving up | `interaction_hint_ftg/multiple_choice/single_choice/validated_input` |
| "See solution" | `see_solution`, `see_solution_confirm_dialog_*`, `see_solution_was_used` key |
| Solution use is tracked and *counts against* the learner | `seeSolutionWasUsed` literal + `solvedContent` keys (V) |
| Partial-match feedback exists | `validated_input_partial_match_feedback_text_the_correct_answer_is` ⇒ the checker can report "close, the correct answer is …" (I: which tolerance triggers it) |

## A4. Why this design is transferable
Offset-based grading needs no sandbox, no server round trip, no per-answer storage and no
fuzzy matcher. For Konkur, the same mechanism grades: fill-in-the-formula, choose-the-unit
("<text>" gaps in a Persian sentence), match-the-definition, and multi-select concept checks.
The only thing that must be added is a **normalisation policy** (§C3).

---

# Part B — Executable (code) lessons (server-authoritative)

## B1. Transport contracts (V)

| Endpoint | Request | Response |
|---|---|---|
| `POST /v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | files `[{name, content}]` (+ lesson identity in path) | `ExecuteFilesResponse(hasPassed, hostedProjectUrl, consoleOutput, error, tests[])` |
| `POST /v1/preview/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | same | same — **unpublished content path**, used by the Developer Menu live-preview flow |
| `POST /v1/code/runfiles` | free project files | `CodePlaygroundExecutionResponse(hostedFilesUrl, consoleOutput, consoleOutputIsError)` |
| `POST /v1/code/{savedCodeId}/runfiles` | run a saved project by id | same |

`ExecuteFilesResponse.tests[]` elements are `ExecuteLessonTestCase(hasPassed, description, error)`.
An older generation still ships: `ExecuteLessonResponse(hasPassed, output, error, tests[])` with
`ExecuteLessonTestCase(hasPassed, description)` — evidence of an API migration kept for cached
or legacy lesson payloads (I).

## B2. UI projection of the result (V)
```
run → ExecutableLessonRunResult =
        TestsPassed   (analytics: "tests_passed")
      | TestsFailed   (analytics: "tests_failed")
      | CompilerError (analytics: "compiler_error")
      | ConnectivityError (analytics: "connectivity_error")
```
Rendered as `%d/%d checks passed`, one row per test with its `description`, and failing tests
labelled `Condition %d`. Feedback copy rotates over
`executable_lesson_feedback_success_0..5` ("That's right!", "Spot on!", …),
`…_almost_there`, `…_somethings_off`, then offers `…_get_help` / `…_ask_ai_tutor`.

Playground has its own sealed result:
`CodePlaygroundRunResult = Browser(hostedFilesUrl, output) | HasOutput(Console(consoleOutput) | CompileError(error))`,
plus `RunCodeEvent` with a `timeout` constant (V) — the client has a run timeout and the server
can return a hosted preview instead of stdout (web lessons).

## B3. What the server does (I, strongly bounded)
* It compiles/executes the submitted files and evaluates a **test suite generated from the
  lesson's own `solvedContent`** — the only per-lesson truth the client ships. The internal
  name appears in an error literal: `Error when executing the MFEL. Error message: `
  ⇒ an internal service ("Mimo File Execution Layer") owns execution.
* It returns human-readable `description` per test, so the *server* authors the test prose;
  the client never contains the expected values of the checks.
* It hosts the built artefact (`hostedProjectUrl` for lessons, `hostedFilesUrl` for
  playground) — for HTML/CSS/JS lessons the "result" is a URL opened in a WebView, not stdout.
* It is the only path that can grade non-web languages (python/node/sql/swift): the client
  contains no interpreter for them.

## B4. Client-side state machine (V literals + class names)
```
editing --run--> running --(tests_passed)--> passed --> storeProgress --> next module
                        --(tests_failed)--> failed --> show tests --> edit again
                        --(compiler_error)--> error --> show error toast/dialog
                        --(connectivity_error)--> offline warning --> keep local code
passed/failed --> see_solution? --> CodeSwitch(Solved|User) diff --> confirm dialog
                                    --> replaces editor content --> marks seeSolutionWasUsed
```
Autosave is continuous (`AutoSaveCodeService`, `savedFiles`), so a lost run never loses code.
Progress is written by `executeLessonAndStoreProgress` — **only on a passing run** (V method
name) — which is why the whole offline story for executable lessons is "you cannot progress
offline", whereas interactive lessons do progress offline (see §16).

## B5. Security consequences (verified public facts only)
* The submission endpoint accepts **arbitrary user code** and executes it server-side. Any
  implementation of this pattern is a remote-code-execution surface by construction; it must
  be sandboxed, CPU/memory/time limited, network-egress blocked, and rate limited per account.
  Mimo's client-side timeout (`RunCodeEvent.timeout`) shows the client expects long runs.
* The **preview** variant executes *unpublished* content: it is an authoring tool reachable
  from the app. If it were reachable outside the dev flow it would expose pre-release course
  material. No exported component leads to the Developer Menu (V), so the exposure is limited
  to builds where the menu is unlocked by a flag/gesture (U which).
* The client never holds expected outputs ⇒ a local attacker cannot mine answers from the APK
  for executable lessons, but *can* for interactive lessons (answers are the code itself).
  That asymmetry is inherent, not a bug.

---

# Part C — Unified grading contract (the part to port)

## C1. One interface, two implementations
```
Grader.check(lessonId, submission, context) -> Verdict {
    passed: bool,
    perItem: [{id, passed, message?}],
    evidence: {attempt, elapsed, endedAt, offline},
    authority: "local" | "server"
}
```
Mimo ships exactly this split informally; writing it as one interface is the main
engineering simplification for Konkur.

## C2. Attempt accounting
`tries` (per lesson, monotonic) and `attempts` (per session/queue entry) both exist in
`lesson_progress`, plus `completedAt`/`startedAt`, and `in_queue` for unsynced rows. Grading
must therefore never be *stateless* even when it is local.

## C3. Normalisation policy (must be decided, Mimo's is unknown)
For Persian Konkur content the checker needs an explicit, testable policy:
`trim`, collapse internal whitespace, Arabic/Persian character folding (ي→ی, ك→ک), Persian
and Arabic-Indic digit folding (۰-۹ / ٠-٩ → 0-9), ZWNJ handling (نیم‌فاصله), optional
diacritic stripping, and number-format tolerance (٫ decimal separator vs `.`).
None of this can be copied from Mimo (its corpus is ASCII identifiers), so it is new work —
and it is the single highest-risk item in an offset-based grading port.
