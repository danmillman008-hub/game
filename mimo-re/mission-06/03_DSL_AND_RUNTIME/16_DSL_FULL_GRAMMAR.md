# Mission 6 — Full DSL Grammar (corrected, evidence-complete)

## Scope
The complete document grammar of an interactive lesson, verified against all seven parser classes —
closing mission-05's open item U-01.

## Method
`tools/extract_parser_grammar.py` mechanically extracted, per parser method, every
`require(depth, ns, "tag")`, every `getName()==` comparison, every `getAttributeValue(ns, …)` and every
`new <Model>(...)`. The grammar below is a direct rendering of that table
(`evidence/PARSER_GRAMMAR.json`) plus the 29-constant `Tag` enum.

## Sources
`evidence/PARSER_GRAMMAR.json`, `evidence/TAG_ENUM.json` (mission-05), the seven `te/*` classes.

## Findings — document grammar (VERIFIED_STATIC)
```
document      := ( html | body )? module+          ; te.c.b dispatches on the tag name
module        := p | code | selection | img | webview | database
               ; NOTE: the tags are HTML-shaped (p, img, br, a, span), not <paragraph>/<image>

p             := "<p" [ visible-if ] ">" inline* "</p>"                 ; te.d.a  -> LessonModule$Paragraph
inline        := "<a" href ">" text "</a>" | "<br/>" | "<span>" inline* "</span>" | "<code>" text "</code>"
                 ; te.d.a handles <a href>; te.d.b <br>; te.d.e <span>; te.d.c inline <code>

code          := "<code" [ name ] [ visible-if ] [ codelang ] ">"
                   content interactions* [ output ] [ collapsibleLines ]
                 "</code>"                                              ; te.a.a -> LessonModule$Code
content       := "<content>" ( text | "<text" [ type ] [ value ] "/>" )* "</content>"   ; te.a.b
interactions  := "<interactions>" interaction+ "</interactions>"
interaction   := "<interaction" type [ isDefault ] startIndex endIndex ">"
                   ( options | item ) "</interaction>"                  ; te.a.a
options       := "<options>" option+ "</options>"
option        := "<option" [ correct ] ">" text "</option>"
output        := "<output>" ( "<content>"…"</content>" | table ) "</output>"
collapsible   := "<collapsibleLines>" "<collapseAt" startLineIndex endLineIndex "/>"* "</collapsibleLines>"

selection     := "<selection" visible-if ">" "<item"…">"* "</selection>"   ; te.e.a -> LessonModule$Selection
                 ; item carries attrs `iscode` and `correct`
img           := "<img" src visible-if "/>"                                ; te.c.a -> LessonModule$Image
webview       := "<webview" visible-if version style interaction content ">"
                 "</webview>"                                             ; te.g.a -> LessonModule$Webview
database      := "<database" visible-if ">" tables "</database>"           ; te.b.a -> LessonModule$Database
tables        := "<tables>" table+ "</tables>"
table         := "<table" [ name ] [ content ] ">" row+ "</table>"         ; te.f.a -> Table
row           := ( "<header>" | "<data>" ) cell+ ( "</header>" | "</data>" )
```

## Findings — corrections to the mission-05 grammar
| Mission-05 statement | Corrected | Evidence |
|---|---|---|
| module tags `<paragraph>`, `<image>` | they are `<p>` and `<img>` | `te.d.a` requires `p`; `te.c.a` requires `img` |
| `<content>` holds raw text only | may contain `<text type= value=>` children | `te.a.b` requires `content`/`text` |
| output table is `<table>` under `<output>` | true, **and** `<tables>` exists as a container under `<database>` | `te.b.a` requires `tables` |
| `collapsibleLine` | the tag is `<collapseAt startLineIndex endLineIndex/>` | `te.a.a` |
| interaction `type` values unknown | child elements decide the parser branch (`options` vs `item`) | `te.a.a` requires `options`/`option`; `te.e.a` requires `item` |
| `<selection>` is a code-module interaction container | `<selection>` is a **top-level module** with `<item>` children | `te.c.b` dispatch + `te.e.a` |

## Evidence labels
The whole grammar: **VERIFIED_STATIC** (extracted mechanically, not inferred from corpus statistics).
Attribute *optionality* is **INFERRED** from the presence/absence of a null-check before each read.

## Limitations
`require()` gives expected events but not loop structure; where a tag was accepted in a loop this is
shown as `+`. Text/whitespace handling and escaping rules are only partly recoverable (see 17).

## Open questions
`Q-28` escaping/CDATA handling; `Q-29` whether `<html>/<body>` wrappers are optional in packaged
content; `Q-30` unknown-tag behaviour (skip vs abort) for each parser.

## Reproduction
`/tmp/venv/bin/python tools/extract_parser_grammar.py --json evidence/PARSER_GRAMMAR.json`
