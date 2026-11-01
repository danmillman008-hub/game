# Phase 3 — Unresolved items (carried forward, with the exact blocker)

| # | Item | Blocker | Next phase |
|---|---|---|---|
| A15 | which module owns `<output>` | variant field names obfuscated; `Output` type shared with `Code` | 4/11 |
| A16 | chapter auto-completion on last lesson | needs `U`/`V` bodies read line by line | 5 |
| A17 | meaning of the five boolean flags in the base view-model | need `O` (616 insns) and `f0` read instruction by instruction | 3-continuation |
| A18 | `base.c.K` identity (`initialiseCodeBlocks` vs `storeLessonProgressInMemory`) | two method families resolve to one dex method | 3-continuation |
| A19 | `base.c.O` recovered name (largest method, takes `LessonContent`) | no lambda family maps to it | 3-continuation |
| A20 | whether `hardModeLessonModules` is parsed from the same document or built | parser string pools show one grammar only | 5 |

## Why these were not forced

Each requires reading a specific method body at instruction level (200–616 instructions) and reconciling it with
lambda families. Guessing from names is exactly what the mission forbids, so they are recorded as open.
