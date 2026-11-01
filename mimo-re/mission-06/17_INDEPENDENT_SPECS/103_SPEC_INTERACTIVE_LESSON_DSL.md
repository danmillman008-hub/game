# Spec 103 — Interactive Lesson DSL

## MUST
1. Parse XML with the tag vocabulary of `03_DSL_AND_RUNTIME/17_TAG_SEMANTICS.md`, dispatching on tag name.
2. Accept `<html>`/`<body>` wrappers; modules: `p`, `code`, `selection`, `img`, `webview`, `database`.
3. Read `visible-if` on every module, defaulting to `always`; enum `{ALWAYS, CORRECT, WRONG}`.
4. Interaction offsets (`startIndex`, `endIndex`) are character offsets into `<content>`.
5. `<interaction type>` with `isDefault`; children `options/option` (attr `correct`) or `item`
   (attrs `iscode`, `correct`).
6. `<output>` holds either `<content>` or one `<table>`; `<tables>` holds many.
7. `<collapsibleLines><collapseAt startLineIndex endLineIndex/></collapsibleLines>`.
8. `codelang` default `none`; paragraph inlines: `a href`, `br`, `span`, `em`, `strong`, `code`.
9. Malformed nesting is a hard error; semantically empty module is soft (renders nothing).

## MUST NOT
- Use `<paragraph>`/`<image>` (they do not exist; the tags are `p`/`img`).
- Assume schema/DTD validation (there is none).
- Treat `NUMBER` as used (no parser accepts it).

## GIVEN EVIDENCE
`03_DSL_AND_RUNTIME/16..19`, `evidence/PARSER_GRAMMAR.json`, `19_AST_SCHEMA.json`.
