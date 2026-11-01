# 04 — SPEC: interactions and grading (normative, copy literally)

Sources: `mimo-re/mission-08/04_INTERACTION_ENGINE/` (16 files), `data/grading_vectors.json`,
`data/interaction_variants.json`. Algorithm recovered from bytecode; `VERIFIED_STATIC`. Never executed.

## 1. The nine interaction types

| # | Type | Content form | Answer model |
|---|---|---|---|
| 1 | Selection (single) | `<selection>` + `<item correct>` | chosen item index |
| 2 | Selection (multiple) | `<selection multiple="multiple">` | chosen set |
| 3 | FillTheGap | `<interaction type="fillTheGap">` | text typed into the gap range |
| 4 | ValidatedInput | `<interaction type="validatedInput">` | text typed into the code range |
| 5 | Spell | code block + text answer | text |
| 6 | MultipleChoice | `<selection>` variant with criteria | chosen set + criteria |
| 7 | SingleChoice | `<selection>` variant | single choice |
| 8 | Reveal | informational block | none |
| 9 | Table / WebView / Database | structural blocks | none (informational) |

## 2. Normaliser — the exact algorithm

```text
normalise(s):
    t = s.toLowerCase(Locale.US)
    out = ""
    for ch in t:
        if ch.isLetterOrDigit(): out += ch
        elif ch in "<>():{},." : out += ch      # the only punctuation kept
        # everything else (space, tab, newline, " ' ; = [ ] _ - / \ | ! ? + * & % $ # @ ~ ^ `) is dropped
    return out
```

Two traps that break naive implementations:

* `Locale.US` matters — Turkish `I` would otherwise lowercase to `ı`;
* `isLetterOrDigit` keeps **Unicode letters**, so a non-Latin answer normalises to non-empty text in your engine but was
  effectively unusable in Mimo (`Q-44`). Decide explicitly and document.

## 3. Verdicts — the three-way rule (ValidatedInput)

```text
verdict(input, expected):
    if normalise(input) != normalise(expected):  return INCORRECT
    if input == expected:                        return CORRECT
    return PARTIAL
```

Note the second test is **raw** equality, not normalised: the answer is CORRECT only when the user's text matches the
expected text byte-for-byte; a normalised match with different whitespace/punctuation is PARTIAL. This is the single
most mis-implemented rule in Mimo and it is pinned by `data/grading_vectors.json`.

## 4. Verdicts — every other type

| Type | Rule |
|---|---|
| Selection (single) | correct iff the chosen item has `correct="true"` |
| Selection (multiple) | correct iff chosen set == set of correct items (all-or-nothing; no partial) |
| FillTheGap | correct iff every gap's text equals its expected range text (all-or-nothing) |
| Spell | correct iff `normalise(input) == normalise(expected)` (two-way, no partial) |
| MultipleChoice | predicate over the chosen set (`pm.b.E0` guard) |
| SingleChoice | single-item predicate (`km.c.E0` guard) |
| Reveal / structural | no verdict |

Only **ValidatedInput** structurally produces PARTIAL (`qm.f` has exactly one construction site).

## 5. Feedback states

| Verdict | Feedback state | Which `visible-if` blocks render |
|---|---|---|
| CORRECT | `jm.m` | `always`, `correct` |
| PARTIAL | `jm.n` | `always` (**not** `wrong`, not `correct`) |
| INCORRECT | `jm.o` | `always`, `wrong` |

`jm.o` takes six boolean flags (hint / solution / retry / tutor candidates); their order is not recoverable (`A22`).
Implement whatever subset you support and record it.

## 6. Counters (as Mimo does it)

```text
on submit (any path): attempts += 1
CORRECT:  tries = (lastVerdictWasWrong ? 1 : 0)      # i.e. !(C == TRUE)
INCORRECT/PARTIAL: tries = 0 for INCORRECT; tries = !(C==TRUE) for PARTIAL
```

Practical reading: `tries` ends up 1 whenever the lesson has been solved in this session, and `isSolvedCorrectly()` is
`tries >= 1`. Never treat `tries` as a count.

## 7. Acceptance

`data/grading_vectors.json` contains the source-derived cases. Your engine must reproduce them exactly; the reference
implementation in `HANDOFF/tools/verify_handoff.py` demonstrates the expected outputs.
