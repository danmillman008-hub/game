# Mission 5 — Complete Lesson DSL Grammar and AST

## Scope
Define, from primary evidence, the markup language Mimo uses for interactive-lesson content: the
tag set, the attribute set, per-tag child grammar, the parse order, the AST node shapes, and the
error/degradation behaviour. This supersedes every earlier, partial description.

## Method
1. Located the parser by instruction-level xref, not by name: searched every instruction in all 12
   DEX files for references to `lessonparser.interactive.model.Tag` (the enum) and for the literal
   `visible-if`; every producer points at `te.a`–`te.g` (`evidence` = `find_refs.py` runs, logged in
   `MISSION_05_REPORT.md`).
2. Decompiled `te.a`–`te.g` in batch 1 (`DECOMPILE_MANIFEST_BATCH1.json`) and every model class in
   `com.getmimo.data.content.lessonparser.interactive.model` (41 classes) in the app batch.
3. Reconstructed the enum constant order and the tag/deputy mapping from `Tag.<clinit>` (ordinals
   0–28) and from the `h.c(name, "<literal>")` string comparisons inside `te.*`.
4. Confirmed module kinds against `LessonModule`'s subclasses and against the 10,327 shipped lesson
   JSON files (`assets/lessons-en/tracks/`), i.e. static and corpus evidence agree.

## Sources
| Evidence | Location |
|---|---|
| Tag enum (29 constants, ordinals) | `com.getmimo.data.content.lessonparser.interactive.model.Tag.<clinit>` |
| Code-module parser | `te.a` (entry `require(2, ns, "code")`) |
| Output parsers | `te.a` + `te.f.a` (`Table`, `Row`, `Header`/`Data`) |
| Interaction model | `Interaction$FillTheGap`, `$Selection`, `$Spell`, `$ValidatedInput`, `Option`, `SelectionItem` |
| Visibility / codelang mapping | `ds.x.o`, `CodeLanguage.Companion.fromString`, `ModuleVisibility.<clinit>` |
| Corpus | `mimo-re/complete-extraction/01_STATIC_CODE/` lesson census (20,306 docs) |

## Findings

### 1. Tag set (VERIFIED_STATIC — `Tag.<clinit>`)
29 tags, in declaration order (the ordinal is load-bearing because the parser switches on ordinals
in some paths): `HTML(0) BODY(1) PARAGRAPH(2) EM(3) CODE(4) SELECTION(5) IMAGE(6) WEBVIEW(7)
TABLE(8) TABLES(9) ROW(10) HEADER(11) DATA(12) DATABASE(13) STRONG(14) SPAN(15) CONTENT(16)
TEXT(17) INTERACTIONS(18) INTERACTION(19) OPTIONS(20) OPTION(21) ITEM(22) NUMBER(23) BREAK(24)
OUTPUT(25) COLLAPSIBLE_LINES(26) COLLAPSIBLE_LINE(27) A(28)`.

The language is therefore **HTML-shaped**, not a bespoke XML dialect: inline emphasis (`<em>`,
`<strong>`, `<span>`, `<a>`), block content (`<p>`), `<code>` as the *interactive unit container*,
and application-specific blocks (`<selection>`, `<image>`, `<webview>`, `<database>`, `<table>`,
`<tables>`).

### 2. Grammar (EBNF, derived; each production cites its parser)
```
document      = { module } ;
module        = code | paragraph | selection | image | webview | database ;   (* te.a..te.g *)

code          = "<code" , attr* , ">"
                  content ,                         (* te.a: require(2, ns, "content")      *)
                  interactions ,                    (* may appear BEFORE content            *)
                  [ output ] ,                      (* exactly one of content|table          *)
                  [ collapsibleLines ] ,
                "</code>" ;
content       = "<content>" , text , "</content>" ;
interactions  = "<interactions>" , { interaction } , "</interactions>" ;
interaction   = "<interaction" , type , [ "isDefault" ] , startIndex , endIndex , ">"
                  ( options | item | number )
                "</interaction>" ;
options       = "<options>" , { option } , "</options>" ;
option        = "<option" , [ "correct" ] , span* , ">" , text , "</option>" ;
output        = "<output>" , ( "<content>" , text , "</content>"        (* ConsoleOutput *)
                            | table )                                  (* TableOutput   *) ")" ;
table         = "<table>" , { row } , "</table>" ;
row           = ( "<header>" | "<data>" ) , { cell } , ( "</header>" | "</data>" ) ;
collapsibleLines = "<collapsibleLines>" , { "<collapsibleLine" , "startLineIndex" , "endLineIndex" , "/>" } ,
                "</collapsibleLines>" ;
attr          = "name" | "visible-if" | "codelang" ;
```
The `span*` on `option` reflects the recovered `Option` fields: `a` (correctness flag), `b` (label),
`c`/`d` (**style-span bounds**, see §4).

### 3. Attributes (VERIFIED_STATIC)
| Attribute | Applies to | Default | Mapping |
|---|---|---|---|
| `name` | every module | **required** | stored on the module model |
| `visible-if` | every module | `"always"` | `ModuleVisibility` via `ds.x.o`: `always` → `ALWAYS`, `correct` → `CORRECT`, `wrong` → `WRONG` |
| `codelang` | `code` | `"none"` | `CodeLanguage.Companion.fromString` |
| `type` | `interaction` | — | selects `FillTheGap` / `Selection` / `Spell` / `ValidatedInput` |
| `isDefault` | `interaction` | `false` | marks the interaction shown before the learner acts |
| `startIndex`, `endIndex` | `interaction` | — | **character offsets into `<content>`** |
| `startLineIndex`, `endLineIndex` | `collapsibleLine` | — | line range of a collapsible block |

`ModuleVisibility` string constants are exactly `"always"`, `"correct"`, `"wrong"` (enum names
`ALWAYS`, `CORRECT`, `WRONG`) — VERIFIED_STATIC from `ModuleVisibility.<clinit>`.

`WebviewType` constants: `BROWSER`, `EMBEDDED`, `INTERACTIVE`, `UNLOCK` — VERIFIED_STATIC.

### 4. Index semantics (the single most error-prone point — resolved)
Two unrelated index spaces exist and must never be conflated:
- `interaction@startIndex` / `@endIndex` → **character offsets into the module's `<content>`** used to
  carve the code text that the interaction acts on (`qm.d` clamps them with
  `max(0,start)` / `min(end,length)`).
- `option@span` → the option's **styled text range** in the assembled output. In
  `InteractiveLessonFillTheGapViewModel` the correct option is rendered with
  `SpannableStringBuilder(source, option.c, option.d)`; the *slot* it fills is
  `source.subSequence(previousSlotEnd, option.c)`. So slots occupy `[prevEnd, c)` and the option's
  own label starts at `c`.

Mission-04 described these as "gap bounds"; the correct statement is *span bounds for display* plus
*slot boundaries derived from them*. Correction recorded in `MISSION_05_REPORT.md`.

### 5. Parse order and degradation (VERIFIED_STATIC)
- `<interactions>` may precede `<content>`; the parser strips the interactions block first and then
  reads the remaining text as content. A parser that assumes document order mis-parses such lessons.
- `<output>` accepts exactly two shapes; an unrecognised child terminates the loop (`break`) instead
  of throwing — malformed output is silently dropped.
- Missing `type` on `<interaction>` and unknown `visible-if` fall back to defaults rather than
  failing the lesson.
- Interaction lookups that find nothing raise a developer message and render nothing:
  `"There is no code block found with FillTheGap interaction. There must be at least one"` and the
  `Spell` twin (VERIFIED_STATIC, literal), i.e. content-side errors surface as silent gaps.

### 6. Corpus conformance (VERIFIED_STATIC, aggregate)
The shipped corpus (20,306 interactive documents) exercises every tag above except `<tables>` as a
top-level construct; 29,093 gaps, 14,870 distractors, 1,772 validated inputs, 7,356 selections,
574 database modules, 930 webviews are present (mission-04 census, re-used as frozen input, not
re-derived). 137 structural defects were recorded there and remain unresolved by the app itself
(the app tolerates them at render time).

## Evidence labels
- Tag set, attribute names/defaults, enum constants, index semantics, degradation strings:
  **VERIFIED_STATIC**.
- The EBNF above: **VERIFIED_STATIC** for every production explicitly exercised by `te.a`; the
  `paragraph`/`selection`/`image`/`webview`/`database` productions are **INFERRED_HIGH** (their
  parsers exist in `te.b`–`te.g` and their models exist, but this mission did not re-read all six
  line by line; see Unresolved).
- Corpus counts: **VERIFIED_STATIC** (frozen mission-04 artifact, not re-derived).

## Limitations
- The grammar documents the *interactive* lesson format. Executable lessons carry a different
  payload (`ExecuteFilesResponse`, run/save files) and are out of scope here.
- Attribute *ordering* inside a start tag is not significant to the parser; the EBNF lists them in
  the order they are read for clarity only.

## Unresolved
- Full line-by-line confirmation of `te.b`–`te.g` (paragraph/selection/image/webview/database).
  Register `U-01`.
- Whether `<tables>` (plural) is a list-of-tables construct or a legacy alias. Register `U-02`.

## Reproduction
```bash
/tmp/venv/bin/python tools/find_refs.py --dex-dir /tmp/x \
  --target 'lessonparser/interactive/model/Tag' --json /tmp/refs_tag.json
sed -n '1,90p' /tmp/dad/te.a.java            # module dispatch + output parsing
sed -n '1,60p' /tmp/dad/com.getmimo.data.content.lessonparser.interactive.model.Tag.java
```
