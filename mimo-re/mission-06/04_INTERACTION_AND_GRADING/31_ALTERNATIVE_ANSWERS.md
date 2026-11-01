# Mission 6 — Alternative Answers

## Scope
Whether an interaction can accept more than one correct answer, and how the corpus expresses that.

## Method
Model inspection (`Option`, `Interaction`), grammar inspection (`<options>/<option>`), grader inspection.

## Sources
`evidence/PARSER_GRAMMAR.json`, `qm.i`, `Enter`/`Option` models.

## Findings (VERIFIED_STATIC)
1. There is **one** expected string per interaction: it is the code substring between `startIndex` and
   `endIndex`. The model carries no answer list.
2. `<options>` may contain several `<option>`s with `correct="true"`, but for graded interactions only
   one option is the intended answer — multiple `correct` flags would make several chips "right" and the
   grader compares by option identity, so each correct chip yields CORRECT (`Q-42`).
3. No `alternatives`, `alsoAccept`, or `regex` attribute exists anywhere in the 29-tag vocabulary.
4. Normalisation (30) is the *only* tolerance mechanism.

## Interpretation
Any requirement for genuinely alternative answers ("print" or "console.log") can only be met by
authoring extra modules or by normalisation collisions. This is a **structural limitation** of the DSL,
not a bug.

## Evidence labels
**VERIFIED_STATIC**; point 2's UX consequence is **INFERRED**.

## Open questions
`Q-42`, `Q-51` whether the corpus contains multi-correct interactions (would need a corpus scan; the
mission-04 census counted 7,356 selections but not their `correct` cardinality).

## Reproduction
`grep -c 'correct' evidence/PARSER_GRAMMAR.json`
