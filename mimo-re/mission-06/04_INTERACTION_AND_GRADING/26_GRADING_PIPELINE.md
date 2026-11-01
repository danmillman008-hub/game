# Mission 6 — Grading Pipeline

## Scope
The exact path from a submitted answer to a verdict, including normalisation and the two-phase compare.

## Method
Line-level read of `qm.i` (grader), the verdict lambdas (`qm.e`, `qm.f`, `qm.g`) and `base.c.Z`.

## Sources
`com.getmimo.assessment.*` (mission-05), `qm.i`, `base.c`.

## Findings — pipeline (VERIFIED_STATIC)
```
submit(input, interaction)
  ├─ normalise(input)  ──┐
  │    lowercase         │
  │    keep [a-z0-9] and the literals '<' '.'   (everything else dropped)
  └──────────────────────┘
  ├─ phase 1  exact string equality (raw input vs expected)      → qm.e  CORRECT
  ├─ phase 2  normalised equality (normalise(input) vs normalise(expected))
  │            → qm.f  CORRECT, and the *input is overwritten* with the expected text
  └─ else                                                         → qm.g  INCORRECT
```
- Phase 2 is deliberately forgiving of case and punctuation — e.g. `Print("Hi")` `==` `print('hi')`
  after normalisation, because quotes/parens/spaces are stripped.
- The overwrite in phase 2 is what makes a "typo-only" answer still display the canonical text.
- `VALIDATED_INPUT` wraps this in `delay(300 ms)`; option kinds call it synchronously.
- Expected text is **not** a stored answer list: it is `content.substring(startIndex, endIndex)` of the
  code module, so the same interaction cannot have two accepted answers in this build.

## Evidence labels
**VERIFIED_STATIC**. Consequences for UX (overwrite) are directly visible in `W()`.

## Limitations
Unicode/diacritic handling is not normalised (the filter drops them, which can make two distinct answers
collapse) — a correctness risk that is *described*, not observed (`Q-44`).

## Open questions
`Q-44` non-ASCII answers; `Q-45` whether trimming happens before phase 1 (`trim()` presence unconfirmed).

## Reproduction
`sed -n '1,120p' /tmp/dad/qm.i.java`
