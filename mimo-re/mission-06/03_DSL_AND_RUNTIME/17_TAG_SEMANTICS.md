# Mission 6 — Tag Semantics (all 29 tags)

## Scope
Every tag constant in the DSL enum: ordinal, grammar role, attributes, runtime meaning and error
behaviour — the table the parser actually implements.

## Method
`Tag.<clinit>` (ordinals 0–28) joined with `evidence/PARSER_GRAMMAR.json` (which parser accepts/produces
each tag) and with the AST model classes.

## Sources
`evidence/TAG_ENUM.json`, `evidence/PARSER_GRAMMAR.json`, `03_DSL_AND_RUNTIME/24_DSL_TAG_MAPPING.csv`.

## Findings
| # | Tag | Role | Produces / consumed by | Notes |
|---|---|---|---|---|
| 0 | `HTML` | document wrapper | `te.c.b` dispatch | optional outer element |
| 1 | `BODY` | document wrapper | `te.c.b` | second accepted wrapper |
| 2 | `PARAGRAPH` | module | `te.d.a` → `LessonModule$Paragraph` | tag literal is `p` |
| 3 | `EM` | inline emphasis | `te.d` inline handling | styling only |
| 4 | `CODE` | module **and** inline | `te.a.a` → `LessonModule$Code`; `te.d.c` inline | same word, two meanings |
| 5 | `SELECTION` | module | `te.e.a` → `LessonModule$Selection` | `<item>` children |
| 6 | `IMAGE` | module | `te.c.a` → `LessonModule$Image` | tag literal is `img`; attr `src` |
| 7 | `WEBVIEW` | module | `te.g.a` → `LessonModule$Webview` | attrs `version/style/interaction/content` |
| 8 | `TABLE` | output/database child | `te.f.a` → `Table` | used in both output and database |
| 9 | `TABLES` | database container | `te.b.a` | plural container (mission-05 U-02) |
| 10 | `ROW` | table child | `te.f.a` | |
| 11 | `HEADER` | row kind | `te.f.a` | |
| 12 | `DATA` | row kind | `te.f.a` | |
| 13 | `DATABASE` | module | `te.b.a` → `LessonModule$Database` | |
| 14 | `STRONG` | inline | `te.d` | styling |
| 15 | `SPAN` | inline | `te.d.e` | |
| 16 | `CONTENT` | code child | `te.a.b` | source text container |
| 17 | `TEXT` | content child | `te.a.b` | carries `type`, `value` |
| 18 | `INTERACTIONS` | code child | `te.a.a` | container, **may precede content** |
| 19 | `INTERACTION` | interaction | `te.a.a` | attrs `type/isDefault/startIndex/endIndex` |
| 20 | `OPTIONS` | interaction child | `te.a.a` | |
| 21 | `OPTION` | option | `te.a.a` → `Option` | attrs `correct` (+ span bounds in model) |
| 22 | `ITEM` | selection child | `te.e.a` | attrs `iscode`, `correct` |
| 23 | `NUMBER` | (declared) | not accepted by any recovered parser | `Q-31` |
| 24 | `BREAK` | inline break | `te.d.b` | tag literal `br` |
| 25 | `OUTPUT` | code child | `te.a.a` → `Output$ConsoleOutput` / `$TableOutput` | exactly one of content/table |
| 26 | `COLLAPSIBLE_LINES` | code child | `te.a.a` | |
| 27 | `COLLAPSIBLE_LINE` | line range | `te.a.a` (`collapseAt`) | `startLineIndex`, `endLineIndex` |
| 28 | `A` | inline link | `te.d.a` | attr `href` |

**Observations that matter for a reconstruction**
- `CODE`, `TABLE` and `SELECTION`/`ITEM` appear in more than one grammatical position; the enum is a
  vocabulary, not a grammar, so an implementation must dispatch on *context*, not tag alone.
- `NUMBER` is declared but unused by the recovered parsers — either dead vocabulary or handled by a
  parser branch not recovered (`Q-31`).
- Attribute sets are small and per-tag: `visible-if` (all modules), `codelang`/`name` (code),
  `src` (img), `version/style/interaction/content` (webview), `type/isDefault/startIndex/endIndex`
  (interaction), `correct` (option/item), `iscode` (item), `href` (a), `startLineIndex/endLineIndex`
  (collapseAt), `name/content` (table).

## Evidence labels
Ordinals and parser acceptance: **VERIFIED_STATIC**. "Same tag in two positions" and "`NUMBER` unused":
**VERIFIED_STATIC** (negative evidence from all seven parsers).

## Limitations
Error/unknown-tag handling per parser was not fully traced (see 18 §error behaviour).

## Open questions
`Q-31` `NUMBER`; `Q-32` whether `EM`/`STRONG` survive into any rendered span (no style-span evidence
found for paragraph text, unlike options).

## Reproduction
`head -c 800 03_DSL_AND_RUNTIME/24_DSL_TAG_MAPPING.csv`
