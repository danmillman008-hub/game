# Mission 7 — Complete DSL Grammar (verified, corrected)

## Method
1. Mechanical extraction over the 7 parser classes (`evidence/PARSER_GRAMMAR.json`, inherited and re-read).
2. **Corpus evidence**: 1,030 lesson documents scanned; DSL tag and attribute frequencies derived
   (`evidence/CORPUS_TAG_STATISTICS.json`). Only names that cannot appear in HTML payload were treated as DSL
   attributes.

## Grammar (VERIFIED_STATIC)
```
document   := (html|body)? module+
module     := p | code | selection | img | webview | database
p          := "<p" [visible-if] ">" inline* "</p>"
inline     := a[href] | br | span inline* | em | strong | code
code       := "<code" [name] [visible-if] [codelang] ">"
                [interactions] content [output] [collapsibleLines] "</code>"
interactions := "<interactions>" interaction+ "</interactions>"
interaction  := "<interaction" type [isDefault] startIndex endIndex ">"
                  (options|item) "</interaction>"
options    := "<options>" option+ "</options>"
option     := "<option" [correct] ">" text "</option>"        ; Option carries span bounds c,d
content    := "<content>" (text | "<text" [type] [value] "/>")* "</content>"
output     := "<output>" (content | table) "</output>"
collapsible:= "<collapsibleLines>" "<collapseAt" startLineIndex endLineIndex "/>"* "</collapsibleLines>"
selection  := "<selection" visible-if ">" "<item" [iscode] [correct] ">"* "</selection>"
img        := "<img" src [visible-if] "/>"
webview    := "<webview" [visible-if] version style interaction content "></webview>"
database   := "<database" [visible-if] ">" "<tables>" table+ "</tables>" "</database>"
table      := "<table" [name] [content] ">" row+ "</table>"
row        := ("<header>"|"<data>") cell+ ("</header>"|"</data>")
```

## Corrections to Mission 6
| Mission 6 | Mission 7 | Evidence |
|---|---|---|
| tag list complete at 29 ordinals | **29 ordinals, but only 25 tags are used by content**; `NUMBER` is dead vocabulary | corpus scan: `<number>` appears only inside prose in 2 documents, never as markup |
| `multiple` may exist on selections | **no `multiple` attribute exists in the DSL**; `multiple` occurs only in prose | corpus scan of 1,030 documents |
| inline set = a, br, span, em, strong, code | confirmed | `te.d` methods |

## Corpus statistics (DSL-relevant, VERIFIED_STATIC)
| Tag | occurrences (1,030 docs) | Attribute | occurrences |
|---|---|---|---|
| text | 369,108 | value | 231,611 |
| code | 189,959 | type | 173,737 |
| p | 92,721 | visible-if | 38,143 |
| content | 82,437 | correct | 35,124 |
| option | 59,357 | startIndex | 30,867 |
| body | 46,336 | endIndex | 30,867 |
| html | 46,319 | name | 23,623 |
| item | 40,497 | version | 22,034 |
| interaction | 21,686 | codelang | 21,108 |
| selection | 14,712 | isDefault | 11,729 |
| output | 11,568 | iscode | 6,486 |
| database/table/row/header/data | 10,440–10,474 | href | 5,919 |

`type` dominates because `<text type=…>` is used for every text run; `value` likewise.

## Not grammar
Tags observed in the corpus that the parsers do **not** accept — `h1…h6`, `div`, `ul/ol/li`, `tr/th/td`,
`input`, `button`, `form`, `figure`, `blockquote`, `script`, `nav` — come from HTML lessons **inside**
`<webview content=…>` payload and from HTML examples **inside** `<code>`/`<content>`. They are data, not DSL
(300 documents contain `<webview>`; 121 contain `<h1>` without a webview element, i.e. inside code/text payload).
