# Mission 6 — Typography

## Scope
Font families, weights and their use sites.

## Findings (VERIFIED_STATIC)
| Family | Assets | Use |
|---|---|---|
| Aeonik Pro | `regular`, `medium`, `bold` (each `*_normal` + `*_italic`), plus XML family descriptors | UI text |
| Aeonik Mono | `aeonik_mono.otf` | code blocks, editor |
| Aeonik Fono | `regular`, `medium`, `bold` | display headings |
| third-party | `optimistic_vf.ttf` (variable), `robotomedium.ttf` | system fallback/legacy |

- The XML files (`aeonik_pro_bold.xml` …) are `font-family` resources: weight/style → file mapping is
  declared, so the app requests a family + weight, not a file.
- No `textAppearance`/type-scale table was recoverable (binary styles; `dimen`/`style` entries are in the
  ARSC but the API path that would dump them failed — see 71 Method).

## Open questions
`Q-127` type scale; `Q-128` line-height tokens.

## Reproduction
`ls /tmp/res/res/font`
