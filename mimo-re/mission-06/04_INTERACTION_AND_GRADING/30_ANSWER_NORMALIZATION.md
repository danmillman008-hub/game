# Mission 6 — Answer Normalisation

## Scope
The exact character filter used in phase 2, and the consequences of its design.

## Method
Instruction-level read of `qm.i`; reconstruction of the filter as a whitelist.

## Sources
`qm.i` (decompiled), Phase 4.26.

## Findings (VERIFIED_STATIC)
Normalisation = `String.toLowerCase()` then keep a character iff it is
`a–z`, `0–9`, `<`, or `.`; all other characters are removed.

```
normalise("Print('Hello, World!')")  -> "printhelloworld"
normalise("print(hello world)")      -> "printhelloworld"     → treated as CORRECT
normalise("a < b")                   -> "a<b"
normalise("1.5")                     -> "1.5"
```

## Consequences
1. Quotes, brackets, commas, spaces, underscores and hyphens are **not** significant; a learner may use
   `"` or `'`, or omit spaces, and still be correct.
2. `_` is dropped, so `my_var` and `myvar` compare equal — a false-positive source for identifiers.
3. Diacritics and non-Latin scripts are dropped entirely (they are not `a–z`), which collapses distinct
   answers to the empty string (`Q-44`).
4. `=` and `+`, `-`, `*`, `/` are dropped — operator-only differences are *not* forgiven between
   digits, but `a+b` vs `ab` do compare equal (another false-positive source).

## Evidence labels
**VERIFIED_STATIC** for the filter; points 2–4 are **INFERRED_HIGH** from applying the filter.

## Reproduction
```python
import re
def normalise(s): return re.sub(r"[^a-z0-9<.]", "", s.lower())
print(normalise("Print('Hello, World!')"))
```
