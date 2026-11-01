# Mission 7 — Lesson Renderer Architecture

## Renderer discovery (VERIFIED_STATIC)
| Renderer | Kind | Where |
|---|---|---|
| `InteractiveLessonBaseViewModel` (`base.c`) | state owner | builds code-block list (`ym.j` plain, `ym.n` interactive) |
| 4 fragments | View | `ui.lesson.interactive.{fillthegap,selection,spell,validatedinput}` |
| `SpannableStringBuilder` composition | span renderer | narrow-gap display, `qc.a` segments |
| `qm.h(answer,prefix,suffix)` | validated-input splitter | three-part line |
| `PartiallyEditableEditText` | custom View | editable middle of a rendered line |
| `CodingKeyboardView` | custom View | code entry keyboard |
| `HighlightJsTheme` | highlighter | token colours per theme |
| `WebView` | platform | `<webview>` modules |
| Rive | native runtime | 59 `.riv` assets (mapping unresolved — `79`) |

No `RecyclerView` adapter is recovered for the lesson list; the block list is rendered into the fragment's
layout, so the lesson is a **single scrollable page**, not a paged adapter list (`INFERRED_HIGH`).

## Tag → component pipeline
`AST node` → `state field in base.c` → `fragment` → `TextView/SpannableStringBuilder | PartiallyEditableEditText`
→ event handler in the fragment's `setupViews` lambda → `base.c.Z(verdict)`.
Mapping table: `30_DSL_TO_UI_MAPPING.json`.
