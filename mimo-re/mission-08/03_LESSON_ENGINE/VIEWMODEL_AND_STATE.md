# Phase 3.7 — View-model and state

## 1. Fields of `InteractiveLessonBaseViewModel` (`base.c`)

| Field | Type | Reading |
|---|---|---|
| `D` | `LessonBundle` | the resolved lesson bundle (content + identifiers) |
| `B` | `CodePlaygroundBundle.FromLesson` | playground configuration derived from the lesson |
| `c` | `List` | parsed modules |
| `I` | `Instant` | a timestamp (only `Instant` field in the class) |
| `b` | `b` | injected collaborator |
| `E`, `J`, `K`, `L`, `M` | `Z` (boolean), one boxed `Boolean C` | five toggle flags |
| `F`, `G` | `i` | two sealed state types |
| `H` | `String` | free string (not identified) |

The **five boolean flags plus a boxed Boolean** are the engine's real state surface; the flags are not named in the
dex, so their meaning must come from the methods that write them (`f0(Z,Z)V` writes two at once, 41 insns).

## 2. Methods and their observable effect

| Method | Size | Observable effect (strings) |
|---|---|---|
| `O(LessonContent)` | 616 | largest method in the class — the only one taking parsed content |
| `G(...)` | 283 | `createInteractiveAiTutorInfo` |
| `i0(...)` | 215 | `browserOutputDeferred` |
| `W(qm.f, ...)` | 202 | `validated_input_execution_correct_partial_match`, `user_input` |
| `V(...)` | 162 | `solutionFeedbackCorrect` |
| `d0(...)` | 148 | `solutionFeedbackWrong` |
| `g0()` | 140 | `lesson_interaction_delete`, `lesson_id`, `tutorial_id` |
| `U(...)` | 130 | `lessonSolvedAndProceedToNextLesson` |
| `X(...)` | 130 | `lessonSolvedIncorrectly` |
| `a0()` | 104 | `lesson_reset` |
| `P(...)` | 91 | AI-tutor usage resolution + its error string |
| `f0(Z,Z)` | 41 | writes two flags |
| `e0(LessonProgress)` | 39 | `initialiseViewModel` |

## 3. What the strings prove about state

Three of the strings are **analytics event names** (`solutionFeedbackCorrect`, `solutionFeedbackWrong`,
`lesson_reset`, `lesson_interaction_delete`) and the accompanying literals (`lesson_id`, `tutorial_id`, `user_input`)
are property keys. The engine therefore reports *grading outcomes* as analytics events from inside the view-model —
i.e. feedback emission and telemetry are the same code path, not two paths.

## 4. Ambiguity kept open

`base.c.K` resolves to two different names (`initialiseCodeBlocks`, `storeLessonProgressInMemory`) and `base.c.V` to
three (`lessonSolvedCorrectly`, `onLessonRun`, `onValidatedInputExecuted`). The string evidence favours
`lessonSolvedCorrectly` for `V`, but the mapping is recorded as ambiguous rather than silently preferring one name.
