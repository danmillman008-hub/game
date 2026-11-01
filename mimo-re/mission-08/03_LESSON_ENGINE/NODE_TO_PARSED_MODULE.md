# Phase 3.4 — Element → module mapping

| Document element | Module variant | Evidence |
|---|---|---|
| `<code codelang name version visible-if>` | `LessonModule.Code` | `te.a` names `code`, `codelang`, `name`, `content`; `Code` holds `CodeLanguage` and an `Output` |
| `<p>` + inline `<strong>/<em>/<br>/<span>` | `LessonModule.Paragraph` | `te.d` names only these tags; `Paragraph` holds an `ArrayList` (spans) |
| `<selection iscode>` with `<item correct>` | `LessonModule.Selection` | `te.e` names `selection`, `item`, `correct`, `iscode`; `Selection` holds only an `ArrayList` |
| `<img src>` | `LessonModule.Image` | `te.c` names `img`, `src`; `Image` holds a `String` |
| `<table name>` with `<row>/<header>/<data>` | `LessonModule.Database` | `te.f` names `table`, `row`, `header`, `data`; `Database` holds an `ArrayList` of tables |
| `<database><tables>…` | `LessonModule.Database` | `te.b` names `database`, `tables` |
| `<webview version style unlock embedded>` | `LessonModule.Webview` | `te.g` names exactly these attributes; `Webview` holds `WebviewType` |
| malformed markup | `xml_parse_error_module` | literal in `te.c` |

## Visibility

Five of six variants carry `ModuleVisibility` (all except `Selection`). Combined with the `visible-if` attribute
(`always`, `none`) this is the mechanism that hides a module — a paragraph is not removed from the model, it is
marked. Consequence for grading: a hidden module still exists in the list, so indices cannot be used as stable answer
identifiers.

## Unknown

Which variant the `<output>` element belongs to is not proven: `Output` is a declared type used by `Code`, and
`output` also appears 3,943 times as a tag. Recorded as question **A15**.
