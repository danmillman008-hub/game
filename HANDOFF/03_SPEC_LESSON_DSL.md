# 03 — SPEC: lesson DSL and renderer contract (normative)

Sources: `data/dsl_grammar.ebnf` (recovered EBNF), `data/dsl_ast_schema.json`, `data/dsl_tags.json`,
`mimo-re/complete-extraction/05_LESSON_DSL/`. Grammar derived from **20,306 documents / 1,034,686 tag occurrences**;
the parser enum has **29 constants**, the corpus exercises **27 tags**. `VERIFIED_STATIC`.

## 1. Document shell

```ebnf
document      = "<!DOCTYPE html" , ">" , "<html>" , body , "</html>" ;
body          = "<body>" , { block } , "</body>" ;
```

`<head>`/`<style>` appear in **2 documents only** — treat as optional.

## 2. Block inventory (with corpus frequency)

| Tag | Count | Role |
|---|---|---|
| `<p>` | 87,598 | paragraph; supports `visible-if` |
| `<code>` | 189,956 | code block: `version="2"`, `codelang`, `name`, `<content>` with syntax-token spans, optional `<interactions>` |
| `<selection>` | 14,712 | multiple/single choice: `iscode`, `multiple`, `<item value correct>` |
| `<webview>` | 934 | embedded HTML: `version`, `style="embedded"`, `interaction="feedback\|unlock"`, `content` |
| `<database>` | 1,148 | SQL sandbox: `bootstrapScript`, `<tables><table name><header><row><data>>`, optional `<output>` |
| `<table>`/`<tables>`/`<row>`/`<header>`/`<data>` | 2,574 / 1,146 / 10,440 / 3,168 / 10,474 | table rendering |
| `<output>` | 11,568 | program/stdout area |
| `<interactions>` / `<interaction>` / `<options>` / `<option>` | 23,458 / 21,686 / 19,914 / 58,833 | gap + validated-input definitions |
| `<text>` | 369,107 | syntax-token span inside `<content>` (`class="string\|keyword\|…"`, or `type="break"`) |
| `<strong>`, `<em>`, `<br>`, `<img>`, `<a>` | 2,566 / 874 / 218 / 143 / 4 | inline formatting, line break, image, link |

## 3. Interaction grammar (the part that matters for grading)

```ebnf
interactions  = "<interactions>" , { interaction } , "</interactions>" ;
interaction   = gap_interaction | validated_interaction ;

gap_interaction       = "<interaction type=\"fillTheGap\" [isDefault=\"true\"]>"
                          "<options>" , { correct_range | distractor } , "</options>"
                        "</interaction>" ;
correct_range         = "<option startIndex=N endIndex=M/>" ;
distractor            = "<option correct=\"false\">" , content , "</option>" ;

validated_interaction = "<interaction type=\"validatedInput\" [isDefault=\"true\"] startIndex=N endIndex=M/>" ;
```

* `startIndex`/`endIndex` are offsets **into the code content** — the answer string is the code substring in that range.
* `isDefault="true"` marks the interaction offered first.

## 4. Rendering contract (what a renderer must produce)

1. **Blocks** map to visual blocks in document order; `visible-if` gates a block on the current verdict
   (`always` default, `wrong`, `correct`).
2. **`<code>`** renders a syntax-highlighted block; `<content>` tokens carry `class` → highlight spans;
   `type="break"` emits a line break; the interaction range is highlighted as the answer slot.
3. **`<selection>`** renders items as tappable rows; `multiple="multiple"` allows several; `iscode="true"` renders items
   as code.
4. **`<database>`** renders a table view; `bootstrapScript` seeds it; `<output>` shows the query result.
5. **`<webview>`** embeds third-party HTML (an iframe-like host). Mimo's URL allowlist was never recovered (`Q-140`).
6. Inline tags are allowed anywhere inside rich text.

## 5. AST

`data/dsl_ast_schema.json` defines the node shape (`Document → Block[]`, `Block.kind`, `Block.attrs`, `Block.children`,
`Token.kind/value`). Use it verbatim so content from Mimo and content from your own authoring tool share one AST.

## 6. Extension points (explicitly **new**, not Mimo)

The grammar file marks four blocks as *NEW* for the target product: `<math>`, `<diagram>`, `<grammar>`, `<audio>`.
Implementing them is optional; if you do, they must not break §3 or the acceptance vectors.

## 7. Unknown-tag policy

Mimo's behaviour on unknown tags is only partly recovered (`Q-30`). Choose one of: ignore-with-warning (recommended),
fail-fast, or render-as-text — and record the choice in `mimo/OPEN_QUESTIONS.md` as `DECIDED_IN_MIMO_BUILD`.
