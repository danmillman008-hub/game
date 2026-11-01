# Mission 7 — Parser Internal Architecture

## Objects and control flow (VERIFIED_STATIC)
`XmlPullParser` (Android platform) is the tokenizer. Each class is a **cursor-consuming recursive-descent
parser** with no intermediate token list and no shared state:

| Class | Responsibility | Calls |
|---|---|---|
| `te.c` | module dispatcher (`getName()` string compare) + `<img>` parser | delegate to `te.a/b/d/e/f/g`, `te.b.a` calls `te.f.a` |
| `te.a` | `<code>` incl. `<content>`, `<interactions>`, `<output>`, `<collapsibleLines>` | `te.a.b` for content, `te.f.a` for output tables |
| `te.b` | `<database>` + `<tables>` | `te.f.a` per table |
| `te.d` | `<p>` + inline HTML (`a`,`br`,`span`,`em`,`strong`,`code`) | itself |
| `te.e` | `<selection>` + `<item>` | — |
| `te.f` | `<table>`, `<row>`, `<header>`, `<data>` | — |
| `te.g` | `<webview>` | — |

## Error model (VERIFIED_STATIC)
- Structural violations → `require(event, ns, tag)` throws (`XmlPullParserException` at call site).
- Semantic gaps → soft: unknown `<output>` child ends the loop and yields a module without output; a missing
  interaction yields an empty render.
- No schema/DTD validation; no recovery mode; the cursor is never rewound.

## State
No instance fields: all results are returned as built model objects (`LessonModule$*`, `Table`, `Option`), which
are `Parcelable`. Parsing is therefore pure w.r.t. the parser and stateful only w.r.t. the cursor.

## Offsets
Interaction boundaries (`startIndex`, `endIndex`) are **character offsets into the `<content>` text of the same
`<code>` module** (30,867 occurrences each). Option span bounds (`Option.c`, `Option.d`) are separate **style
spans inside the option label**, never gap bounds. See `24_AST_COMPLETE_SCHEMA.json` for the typed model.
