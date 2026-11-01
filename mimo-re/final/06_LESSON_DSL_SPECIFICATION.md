# 06 — Lesson DSL specification (formal)

The interactive lesson format is an XML dialect embedded as a **JSON string field**
(`interactiveContent`) inside tutorial files. It is closed: across 18,272 lessons and
235,973 `<text>` nodes there are **0 unknown tags and 0 unknown attributes** relative to the
grammar below, and **0 XML parse errors** (`tools/content_deep.py` → `dsl.unknownTags = {}`).
Element/attribute frequencies below are measured, not illustrative.

## 1. Document envelope (V)

```
<!DOCTYPE html ><html><body> …modules… </body></html>
```
14,249 `<html>` occurrences for 14,248 interactive lessons ⇒ exactly one lesson embeds a nested
document (the single `<head><style>` in the corpus). Whitespace after `</html>` is common.

## 2. Grammar (EBNF; `<x>` = element, `{ }` = 0..n, `[ ]` = optional)

```
document      = "<!DOCTYPE html >", "<html>", "<body>", { module }, "</body>", "</html>" ;
module        = paragraph | code_block | webview | database_block | selection_block | inline ;
paragraph     = "<p>", [ visible_if ], { inline | code_inline }, "</p>" ;        (* 29,193 *)
code_block    = "<code>", version, codelang, name, [ visible_if ], block_version,
                "<content>", { text_run }, "</content>",
                [ interactions ], [ output_block ], "</code>" ;                   (* 58,806 *)
text_run      = "<text value='…'/>" | "<text type='break'/>" ;                    (* 235,973 *)
interactions  = "<interactions>", { interaction | option_set }, "</interactions>" ;(* 8,276 *)
interaction   = "<interaction type='fillTheGap|validatedInput' isDefault='true|false'>"
                     [ start_index, end_index ],
                     [ "<options>", { gap_option | decoy_option }, "</options>" ],
                "/>" | "</interaction>" ;
gap_option    = "<option startIndex='n' endIndex='n'/>" ;                          (* 17,526 *)
decoy_option  = "<option correct='false'>", "<content>", { text_run }, "</content>", "</option>" ; (* 4,939 *)
output_block  = "<output>", "<content>", { text_run }, "</content>", "</output>" ; (* 3,943 *)
webview       = "<webview>", version, content_url, [ visible_if ], [ style ], [ interaction_ref ], "/>" ; (* 841 *)
database_block= "<database>", visible_if, bootstrap_script, "<tables>",
                   { "<table name='…'>", { "<row>", cell, { cell }, "</row>" }, "</table>" }, "</tables>",
                "</database>" ;                                                    (* 574 *)
cell          = "<header content='…'/>" | "<data content='…'/>" ;                  (* 3,168 / 10,474 *)
selection_block = "<selection>", multiple, is_code, { "<item value='…' correct='true|false'/>" }, "</selection>" ; (* 4,751 *)
inline        = "<strong>" | "</strong>" | "<em>" | "<br/>" | [ "<img src='…' visible_if/>" ] | [ "<a href='…'>" ] ;
visible_if    = "visible-if='always|wrong|correct'" ;
```
Attributes actually present per element (V, exhaustive):

| Element | Attributes | Counts |
|---|---|---|
| `<code>` | `version`, `codelang`, `name`, `visible-if` | 14,469 / 14,469 / 14,469 / 10,837 |
| `<text>` | `value` (129,389), `type` (106,584 — only `break`) | 235,973 elements |
| `<interaction>` | `type` (8,276: `fillTheGap` 6,504, `validatedInput` 1,772), `isDefault` (8,276, always `"true"`), `startIndex`/`endIndex` (1,772 — only on `validatedInput`) | — |
| `<option>` | `startIndex`/`endIndex` (17,526 each), `correct` (4,939, **always `"false"`**) | — |
| `<p>` | `visible-if` (13,128 of 29,193) | — |
| `<selection>` | `multiple` (4,751, always `"multiple"`), `iscode` (4,190) | — |
| `<item>` | `value`, `correct` (11,889 each) | — |
| `<webview>` | `version`, `content`, `visible-if` (679), `style` (286), `interaction` (101) | 841 |
| `<database>` | `visible-if`, `bootstrapScript` | 574 |
| `<table>` | `name` | 1,287 |
| `<output>` | — | 3,943 |
| `<img>` | `src`, `visible-if` | 139 |

## 3. Semantics

### 3.1 Flattening (the core operation)
The editor renders a **flattened code string**:
`flat = concat(value of each <text> in document order, mapping <text type="break"/> → "\n")`,
with XML entities decoded (`&lt;` → `<`, etc.). Offsets index into `flat`, 0-based,
`[startIndex, endIndex)` half-open. Cross-check: **17,526 / 17,526 gap options are in bounds**
under exactly this rule, and no alternative rule (ignoring breaks, 1-based, per-line) is
consistent with all of them.

### 3.2 Answer model
| Interaction | Where the correct answer lives | Evidence |
|---|---|---|
| `fillTheGap` | The **code slice** at each `gap_option` range, i.e. `flat[start:end]`. Decoy chips carry `correct="false"`; no `correct="true"` exists anywhere in the corpus ⇒ correct chips are **derived from the code**, decoys are authored. | V counts + I derivation |
| `validatedInput` | The slice at `flat[start:end]` (e.g. an identifier or literal the learner must type). `startIndex/endIndex` sit on the `<interaction>` itself. | V |
| `selection` | `<item correct="true">` — exactly one per block (0 blocks with none, 0 with two) | V |
| `output` | Expected console text for the code block, shown as expected output, not compared to an interaction | V (presence) / I (use) |

The derived-answer rule is the elegant part of the design: the author never types the answer
twice. Writing the correct code *is* authoring the answer; only distractors are extra work.
This is why the corpus can afford 13k assessed blocks with 1,649/1,535/1,669 blocks of 1/2/3
gaps respectively (distribution 1→1,649, 2→1,535, 3→1,669, 4→930, 5→419, 6→203, 7→56, 8→28,
9→7, 10→3, 11→2, 12→3).

### 3.3 Visibility state machine
`visible-if` ∈ {`always`, `wrong`, `correct`} — 12,171 / 13,043 / 143 occurrences.
Per assessed module: `unanswered → checked(wrong|correct)`. Modules with `visible-if="wrong"`
are **remedial feedback** (13,043 of them, 91.5% of interactive lessons have at least one);
`visible-if="correct"` is rare (143) and used for escalation ("you got it — here's the deeper
explanation"). Recovery: the learner can re-check, and after repeated failure the app offers
`see_solution` / hints (`interaction_hint_*`, V strings).

### 3.4 Multi-block lessons
A lesson is a document, not a single exercise: 58,806 `<code>` blocks over 14,248 lessons
(≈4.1 per lesson), each with its own `name` (filename) and `codelang` (11 languages), and each
independently assessed or purely demonstrative. Ordering is document order; there is no
explicit sequencing attribute.

### 3.5 Non-code modules
* `<webview content="…">` (841): renders an HTML/CSS preview or an embedded file; `style`
  selects presentation, `interaction` links it to an interaction for "tap on the element"
  exercises (I).
* `<database bootstrapScript="…">` (574 in 269 SQL lessons…): declarative table + row content
  seeded by a bootstrap SQL script, rendered as a result grid with `<header>`/`<data>` cells.
* `<output>` (3,943): expected program output (e.g. `6`), used both as explanation and as the
  comparison target when the lesson is "predict the output" (I).

## 4. Conformance results (measured over the whole corpus)

| Check | Result |
|---|---|
| Unknown tags / attributes | 0 / 0 |
| Out-of-bounds offsets | 0 of 17,526 |
| Overlapping gap ranges within a block | 0 |
| `selection` with < 2 items | 0 |
| `selection` with ≠ 1 correct item | 0 |
| Blocks with > 12 gaps | 0 |
| `isDefault` values other than `"true"` | 0 |
| `option correct` values other than `"false"` | 0 |
| Lessons whose `interactiveContent` is empty but type is interactive | 0 |

## 5. Reference implementation sketch (language-agnostic, ready to port)

```pseudo
parse(xml) -> Module[]
  # one pass, no DOM required; regex/tokeniser is sufficient because the grammar is flat
  for each top-level element in <body>:
     p        -> Paragraph(visible_if, inlines[])
     code     -> CodeBlock(version, codelang, name, visible_if,
                           flat=flatten(content), gaps=[(s,e)], decoys=[text],
                           input=(s,e)?, expectedOutput=flatten(output)?)
     selection-> Selection(multiple, iscode, items=[(value, correct)])
     webview  -> Webview(version, content, style, interaction?)
     database -> Database(bootstrap, tables=[(name, rows[cell])])
     img      -> Image(src, visible_if)

flatten(content) = join(text.value for text runs, mapping break -> "\n")

check(block, userInput):
   fillTheGap   -> for each gap i: userInput[i] == block.flat[gap[i].s : gap[i].e]
   validatedInput -> normalise(userInput) == normalise(block.flat[s:e])      # see §07.3
   selection    -> set(chosen) == set(items where correct)
```

## 6. Limits of this specification

* Whether `fillTheGap` accepts a *typed* answer in place of a chip tap (partial match) is
  **UNKNOWN**; the string `validated_input_partial_match_feedback_text_the_correct_answer_is`
  proves partial matching exists, but which interaction type uses it is not provable statically.
* Unicode/normalisation rules for `validatedInput` (trim, case, trailing punctuation) are
  **UNKNOWN**; the corpus answers are ASCII identifiers, so the rule is untested by the data.
* `webview`'s `interaction` attribute semantics (element-target matching) rest on one attribute
  name and 101 occurrences; no schema proves it.

## 7. Transfer assessment

The DSL needs four changes for Konkur and nothing else:
1. Add a `subject`/`topic`/`year-weight` attribute set at chapter level (exam blueprint).
2. Add `<equation>` and `<figure>` modules; Persian exam content is formula- and
   diagram-heavy, and Mimo's `<img>`/`<webview>` are not enough (the 139 `<img>` in the whole
   corpus is the proof: this DSL was never designed for figures).
3. Add an RTL-safe `<text dir="ltr">` marker for formulas and code inside Persian prose.
4. Add a **negative-marking** field to `selection` — Konkur's three-option-with-penalty
   format cannot be expressed today (Mimo's `multiple` selection has no scoring policy).
