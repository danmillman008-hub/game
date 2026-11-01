# Mission 7 — Normalisation Specification

## Definition (VERIFIED_STATIC, `qm.i`)
```
normalise(s):
    s = s.lower()
    keep c  iff  'a' <= c <= 'z'  OR '0' <= c <= '9'  OR c == '<'  OR c == '.'
```
Everything else is deleted: spaces, tabs, quotes (`"` `'`), brackets, `_`, `+`, `-`, `*`, `/`, `=`, `:`, `;`,
commas, backticks, `!`, `?`, and **all non-ASCII characters** (accented letters, Cyrillic, CJK, emoji).

## Consequences (verified against candidate vectors)
| Input pair | Normalised | Equal? | Consequence |
|---|---|---|---|
| `Print("hi")` / `print('hi')` | `printhi` / `printhi` | yes | quote + case tolerant |
| `my_var` / `myvar` | `myvar` | yes | **identifier false positive** |
| `a + b` / `ab` | `ab` | yes | **operator false positive** |
| `Café` / `Cafe` | `caf` / `cafe` | no | accent deletion breaks a legitimate match |
| `Ça marche` / `ça marche` | `amarche` / `amarche` | yes | symmetric deletion still matches |
| `АБВ` / `abc` | `` / `abc` | no | non-Latin answers can never match |

## Locale dependency
The filter is **not** locale-aware: it is ASCII-only, so any lesson whose expected answer contains non-ASCII
characters cannot be answered via the normalised path (only exact match works). No per-locale variant of
`qm.i` was found — the same grader serves all content locales (`Q-44` now closed as a code fact).
