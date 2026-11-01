# Mission 7 — Grading Algorithms (complete)

## Validated input — `qm.i` (VERIFIED_STATIC)
```
expected = code.content.substring(interaction.startIndex, interaction.endIndex)
phase 1: input == expected                      -> CORRECT
phase 2: normalise(input) == normalise(expected) -> CORRECT, input := expected
else                                             -> INCORRECT
normalise(s) = remove every char not in [a-z0-9<.] after lowercase
```
Verification of the false-positive class in the corpus-derived vectors:
`my_var`≈`myvar`, `a+b`≈`ab`, `"hi"`≈`'hi'`, `Print(x)`≈`print(x)`.

## Option interactions (VERIFIED_STATIC)
Correctness is decided by **which option was tapped**, using the option's `correct` attribute — not by text
comparison. Therefore two options with identical labels but different `correct` flags are distinguishable, and a
correct option cannot be "typed" by the learner.

## Partial credit — none
`PARTIAL` in the state machine is **not** partial credit: it is the *normalised match* verdict, which yields
success and rewrites the input. There is no numeric score anywhere (`LessonProgress` has no score column).

## Executable lessons
Server decides via `hasPassed`; `tests[]` exists but is not rendered in the recovered UI.
