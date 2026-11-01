# Mission 6 — Parser Architecture

## Scope
How the seven parser classes share work: dispatcher, per-module parsers, delegation, state and error
behaviour.

## Method
Method-level extraction (`PARSER_GRAMMAR.json`) plus call-graph inspection of `te.c.b` (the dispatcher)
and the shared helpers it calls.

## Sources
`evidence/PARSER_GRAMMAR.json`, `te.a`–`te.g` decompiled sources.

## Findings
1. **Top-level entry is `te.c.b`**, a dispatcher that inspects `XmlPullParser.getName()` and compares it
   against the literals `p`, `code`, `selection`, `img`, `webview`, `database`, plus the wrappers `html`
   and `body`. It is not a tokenizer: the tokenizer is Android's `XmlPullParser` itself.
2. **One class per module kind** (except `te.c`/`te.d`, which each hold two roles):
   `te.a` code (+content), `te.b` database, `te.c` img + dispatch, `te.d` paragraph + inline HTML,
   `te.e` selection, `te.f` table, `te.g` webview.
3. **Delegation is by direct static call**: `te.b.a()` calls `te.f.a()` for each `<table>`;
   `te.c.b()` calls the module parser for the matching tag. There is no registry, no map of tag→parser,
   and no plugin mechanism — the "tag registry" is a chain of string comparisons.
4. **State is the pull-parser cursor only.** No parser instance holds a stack; nesting is handled by
   `require(event, ns, tag)` assertions (event 2 = START_TAG, 3 = END_TAG). This makes the parser
   strictly *recursive-descent over a cursor*, with no intermediate token list.
5. **Attributes are read by name**, never by index: `getAttributeValue(ns, "visible-if")` etc. Missing
   attributes fall back to defaults (`visible-if` → `"always"`, `codelang` → `"none"`,
   `isDefault` → `false`) — visible as null-checks before the mapping call.
6. **Error behaviour**: malformed structure raises through `require(...)` (an `XmlPullParserException`
   at the call site); *semantically* wrong content does **not** throw — e.g. an unrecognised `<output>`
   child breaks the loop and yields a module with no output; a missing interaction produces a
   developer-facing message and an empty render. So parse errors are hard failures, content errors are
   soft.
7. **`isDefault`** on `interaction` marks the interaction that is active before the learner acts; the
   value reaches the VM as a boolean field, not as an enum.

## Findings — what the parser is *not*
No DTD/schema validation, no namespace strictness (all reads pass the parser's own namespace), no
character-offset computation (offsets arrive as attributes), and no AST serialisation (models are
Parcelable, not JSON-serialisable).

## Evidence labels
All seven points: **VERIFIED_STATIC**.

## Limitations
DAD renders `require()` with the *literal* tag, but the loop conditions are reconstructed; a `while` that
accepts any child versus one that filters by name can look similar in pseudo-Java. Where that ambiguity
mattered it is flagged in 16 (the `+` notation).

## Open questions
`Q-30` unknown-tag behaviour per parser; `Q-33` whether a lesson-level "root" parser (`te.c.b`'s caller)
adds extra validation.

## Reproduction
```bash
grep -n 'getName()' /tmp/dad/te.c.java | head -20
python3 -c "import json;d=json.load(open('evidence/PARSER_GRAMMAR.json'));print(d['classes'][2]['methods'][1])"
```
