# Mission 6 — Feedback Engine

## Scope
How the app tells a learner they are right or wrong, and what it shows afterwards.

## Method
Read of VM feedback fields and the paragraph-visibility selection at lesson init.

## Sources
`base.c` init path; `LessonModule$Paragraph` visibility handling; mission-05 `06_ASSESSMENT_AND_EVALUATION/`.

## Findings (VERIFIED_STATIC)
1. Feedback text is **authored content**, not generated: at lesson init the VM scans the module list and
   stores the paragraph with `visible-if="correct"` and the one with `visible-if="wrong"`.
2. Visibility is evaluated per module: `visible-if="always"` renders always; `correct`/`wrong` render
   only in the corresponding verdict state of *that* exercise.
3. Colour is **state-driven at the span level only** for options (correct option spans are styled), not
   for paragraphs; the recovered code applies no explicit correct/incorrect theme colour to text
   (`Q-46`).
4. Wrong answers do not reveal the solution: the expected text is used to *replace* the input only in
   the normalised-match case (phase 2), never on failure. So a learner who is wrong never sees the
   answer pre-filled (`Q-47` for hint-driven reveal).
5. After proceeding, no feedback is retained; the next lesson starts clean.
6. Analytics: each verdict emits one event with `interactionType` and `solved` (Phase 8).

## Evidence labels
**VERIFIED_STATIC**. Absence of a colour/theme table: **VERIFIED_STATIC** for the lesson VM code,
**UNKNOWN** for the theme (ARSC colour retrieval failed — see Phase 9).

## Open questions
`Q-46` colour tokens; `Q-47` reveal-on-hint; `Q-48` localisation of feedback (content-provided).

## Reproduction
`grep -n 'CORRECT\|WRONG\|ALWAYS' /tmp/dad/com.getmimo.ui.lesson.interactive.base.c.java | head -20`
