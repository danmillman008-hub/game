# Phase 3.2 — Parser specification (seven parsers)

| Parser | Tags it names | Attributes it names | Emits | Confidence |
|---|---|---|---|---|
| `te.a` | `code`, `content`, `interactions` | `version`, `codelang`, `name`, `visible-if`, `always`, `none` | `LessonModule.Code` | HIGH |
| `te.b` | `database`, `tables`, `table` | `visible-if` | `LessonModule.Database` | MEDIUM |
| `te.c` | `p`, `img`, `code`, `selection` | `src`, `visible-if` | dispatcher + `Image`; owns `xml_parse_error_module` | HIGH |
| `te.d` | `p`, `span`, `strong`, `br` | `visible-if` | `Paragraph` inline spans | HIGH |
| `te.e` | `selection`, `item` | `iscode`, `correct` | `Selection` | HIGH |
| `te.f` | `table`, `row`, `header`, `content`, `data` | `name` | table structure inside `Database` | MEDIUM |
| `te.g` | `webview`, `interaction` | `version`, `style`, `unlock`, `embedded`, `visible-if` | `Webview` | HIGH |

## Dispatch model

`te.c` is the only parser that mentions three different element families (`p`, `img/code`, `selection`) *and* the
parse-error module, which identifies it as the **root/dispatching parser**: it walks the document and delegates a
sub-tree to one of the other six. This matches its role as the `te.c` instance injected into `DefaultTrackLoader`.

## Ownership rule

Each parser's string pool is a closed vocabulary: no parser names a tag outside its own family. That is why the
mapping above is evidence-based rather than name-based — `te.e` *cannot* be the code parser, because it never
mentions `code`.

## What is not claimed

* method-level control flow inside any parser (no parser body was read line by line in this phase);
* the exact element→variant decision for `table` vs `database`;
* how `visible-if` is evaluated at render time (Phase 11, UI).
