# Mission 7 — Unresolved DSL Constructs

| # | Construct | Status after Mission 7 | Why |
|---|---|---|---|
| 1 | `NUMBER` tag (ordinal 23) | **CLOSED_STATIC — dead vocabulary** | never accepted by any parser; corpus `<number>` hits are prose in 2 documents |
| 2 | multi-select `selection` | **CLOSED_STATIC — not supported** | no `multiple` attribute in DSL; `multiple` only in prose |
| 3 | `<text type=…>` value vocabulary | PARTIALLY_CLOSED | attribute is heavily used (173,737) but the accepted `type` values are consumed by the model, not validated in the parser |
| 4 | `<webview interaction=…>` values | NOT_RECOVERED | attribute read as a raw string; consumer is UI-side and not traced |
| 5 | `<webview version/style>` semantics | NOT_RECOVERED | passed through to the web layer |
| 6 | escaping / entities inside `<content>` | PARTIALLY_CLOSED | corpus stores escaped HTML (`&lt;`, `&#xA;`) inside `content` attributes; the parser performs no unescaping, so the webview receives the raw string |
| 7 | whitespace normalisation in `<p>` | UNKNOWN | no trim/normalise call recovered in `te.d` |
| 8 | unknown-tag behaviour at the top level | UNKNOWN | `te.c.b` compares known names; the else-branch was not readable |

## Confidence note
Items 1–3 were *closed by corpus evidence*, which is stronger than the earlier code-only inference. Items 4–8
need either the webview UI consumer or a runtime observation.
