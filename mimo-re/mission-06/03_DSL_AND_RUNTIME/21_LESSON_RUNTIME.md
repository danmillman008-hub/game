# Mission 6 — Lesson Runtime

## Scope
What executes when a learner opens and works through an interactive lesson, in order, with the exact
state transitions and side effects.

## Method
Re-read of `com.getmimo.ui.lesson.interactive.base.c` plus the four subclasses and the two verdict
lambdas; cross-checked against progress writes and analytics emissions.

## Sources
Phase 4 documents, mission-05 `05_LESSON_RUNTIME/RUNTIME_SPEC.md`, `06_ASSESSMENT_AND_EVALUATION/ASSESSMENT_SPEC.md`.

## Findings — execution sequence (VERIFIED_STATIC)
```
1 open lesson        VM constructed from LessonBundle; content already parsed (Phase 3)
2 initialise         first-visit flag → write progress row H(0,0); pick feedback paragraphs
                     (CORRECT / WRONG visibility) into s/t; select the `isDefault` interaction
3 render             per-type VM builds code blocks + slots (Phase 3.20)
4 user acts          tap option / type text / select items
5 submit             typed event → Z(verdict):
                       validated input: delay(300ms) then compare
                       option types:    immediate
6 verdict            V() correct | W(partial: overwrite input, count as solved) | X(incorrect)
7 record             H(tries,attempts) → LessonProgressRepository.createLessonProgress(...)
                     progress row upserted with in_queue=1
8 feedback           correct/wrong paragraph text; attempt counter pushed to tracking state
9 analytics          f0(interactionType, solved) per submission; lesson_reset / interaction_delete
10 proceed           U(): tries = (lastVerdictCorrect ? 1 : 0); d++; H(tries,d); mark lesson solved;
                     emit "solved" event → navigation to next lesson
11 sync              queue batch → POST /v1/tutorials/{tutorialId}/progress → delete local rows
```

## Findings — invariants
- `attempts` (`d`) increments on **every** submission, including correct; `tries` is written 0/1.
- A lesson that is opened and abandoned is still recorded (`tries=0, attempts=0`).
- The verdict set is closed: a fourth outcome cannot exist (`NoWhenBranchMatchedException` otherwise).
- Feedback is *content-driven*: no `visible-if="wrong"` paragraph ⇒ no targeted wrong-answer text.
- The 300 ms delay applies **only** to validated input.

## Evidence labels
All of the above: **VERIFIED_STATIC**. Nothing here is runtime-verified (`R-*` items in Phase 15).

## Limitations
Interstitials, animations between lessons, sound/haptics and the exact navigation call after the
`solved` event were not traced (`Q-36`).

## Open questions
`Q-36` post-lesson navigation; `Q-08`/`Q-37` hint and retry UI ownership; `Q-38` whether a wrong answer
replays the same interaction instance.

## Reproduction
`sed -n '520,860p' /tmp/dad/com.getmimo.ui.lesson.interactive.base.c.java`
