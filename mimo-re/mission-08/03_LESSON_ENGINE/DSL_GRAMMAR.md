# Phase 3.3 — Lesson content grammar (derived from the corpus, not from names)

The lesson text is **not** Markdown and not a custom DSL in the usual sense: it is an **HTML document with
custom elements**, delivered as the `interactiveContent` string of a lesson.

## 1. How this grammar was derived

1. 18,272 lessons were walked in `assets/lessons-en/tracks/*.json` (structure only).
2. Every `<tag` occurrence was counted.
3. The attribute vocabulary was taken from the string pools of the seven parser classes, not guessed.

## 2. Tag census (interactive content, en)

| Tag | Occurrences | Role |
|---|---|---|
| `text` | 235,973 | literal text carrier (`<text value="…">`) |
| `code` | 58,806 | code block |
| `p` | 29,193 | paragraph |
| `content` | 22,810 | code-block content container |
| `option` | 22,465 | selection option |
| `html`, `body` | 14,249 each | document wrapper |
| `item` | 11,889 | selection item |
| `data` | 10,474 | table cell |
| `interactions` / `interaction` | 8,276 each | interactive answer container |
| `options` | 6,504 | option list |
| `row` | 5,220 | table row |
| `selection` | 4,751 | multiple-choice module |
| `output` | 3,943 | expected/rendered output |
| `header` | 3,168 | table header cell |
| `table` | 1,287 | table |
| `strong` | 1,096 | inline emphasis |
| `webview` | 841 | embedded web content |
| `database` / `tables` | 574 each | database module |
| `em` | 362 | inline emphasis |
| `br` | 188 | line break |
| `img` | 139 | image |
| `a` | 2 | link |

## 3. Elements and attributes

```
document   ::= "<!DOCTYPE html >" "<html>" "<body>" block* "</body></html>"
block      ::= paragraph | code | selection | table | database | webview | image
paragraph  ::= "<p>" inline* "</p>"
inline     ::= "<strong>"…"</strong>" | "<em>"…"</em>" | "<br>" | "<span …>"…"</span>" | "<a …>"…"</a>"
code       ::= "<code version=… codelang=… name=… visible-if=…>"
                 "<content>" ( "<text value=…>" | nested )* "</content>"
                 ( "<interactions>" interaction* "</interactions>" )?
               "</code>"
selection  ::= "<selection iscode=…>" "<item correct=…>" inline* "</item>"* "</selection>"
table      ::= "<table name=…>" "<table>" "<row>" ("<header>"|"<data>")* "</row>"* "</table>" "</table>"
database   ::= "<database>" "<tables>" table* "</tables>" "</database>"
webview    ::= "<webview version=… style=… interaction=… unlock=… embedded=…>"
```

### Attribute vocabulary (union of parser string pools)

| Attribute | Values observed / declared | Parser |
|---|---|---|
| `visible-if` | `always`, `none` | te.a, te.b, te.c, te.d, te.g |
| `codelang` | language id (e.g. `html`) | te.a |
| `version` | integer | te.a, te.g |
| `name` | file name (e.g. `index.html`) | te.a, te.f |
| `iscode` | boolean | te.e |
| `correct` | boolean | te.e |
| `src` | asset/URL path | te.c |
| `style`, `unlock`, `embedded`, `interaction` | declared | te.g |

## 4. The parse-error module

`te.c` contains the literal `xml_parse_error_module`. The content pipeline therefore has an explicit
**error module** representation: malformed markup becomes a module of its own rather than an exception. That is the
error path Phase 2 could not find on the stream layer — it lives in the parser, not in the loader.

## 5. Two lesson types, one grammar

`contentType` distribution across 18,272 lessons: **`interactive` 14,248**, **`executableFiles` 4,024**.
Both types carry `interactiveContent`; executable lessons instead expose file contents through
`LessonContent.Executable(files, instructions, preselectedFileIndex)`. The grammar above therefore describes the
*interactive* branch; the executable branch is Phase 10.

## 6. Limits

* Element nesting was inferred from tag co-occurrence and parser strings, **not** from an XSD or a parser body read
  line by line; the `table`/`database` overlap is the weakest part (marked in `PARSED_MODULE_MODEL.json`).
* Attribute value domains are only what appears in the string pools.
* Only the `en` corpus was walked; nine other locales share the same tag set by construction but were not counted.
