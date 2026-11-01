# E1 — Content Format Specification (independent)

## Scope
A normative description of the lesson document format: document structure, tags, attributes, parse
order, index spaces and validation rules. Implementable without Mimo source.

## Method
Normalised from the verified grammar (`04_CONTENT_AND_DSL/DSL_GRAMMAR.md`) into requirements with
identifiers (`E1-R-n`), each traceable to a finding.

## Sources
`04_CONTENT_AND_DSL/DSL_GRAMMAR.md`, `04_CONTENT_AND_DSL/AST_AND_MODELS.md`, `evidence/TAG_ENUM.json`.

## Findings (normative requirements)
- **E1-R-1** A document is a sequence of *modules*. Each module is one of: `code`, `paragraph`,
  `selection`, `image`, `webview`, `database`.
- **E1-R-2** Every module carries `name` (required) and `visible-if` ∈ {`always`, `correct`, `wrong`}
  (default `always`). `visible-if` controls conditional display in lesson feedback, not parsing.
- **E1-R-3** A `code` module contains: `content` (source text), an `interactions` block, an optional
  `output`, and optional `collapsibleLines`.
- **E1-R-4** Parse order is *not* document order: the `interactions` block must be located and removed
  before the remaining inner text is taken as `content`. Implementations that assume order will
  mis-parse any document where `interactions` precedes `content`.
- **E1-R-5** An `interaction` has `type` ∈ {fill-the-gap, selection, spell, validated-input},
  `isDefault` (default false), `startIndex`, `endIndex`.
- **E1-R-6** `startIndex`/`endIndex` are **character offsets into `content`** and must be clamped to
  `[0, len(content)]` before use. Out-of-range values must not throw.
- **E1-R-7** Option-bearing interactions contain options; each option has a correctness flag, a label,
  and an optional styled span `[spanStart, spanEnd)`. The option's span is a *display* range; the input
  slot it fills is `[previousSlotEnd, spanStart)`.
- **E1-R-8** `output` has exactly two forms: a console form (free text) and a table form (rows typed as
  header or data). Unrecognised children of `output` must be skipped, not treated as an error.
- **E1-R-9** `collapsibleLines` declares line ranges (`startLineIndex`, `endLineIndex`) that the editor
  may fold. Ranges are line-based, not character-based, and must not be confused with E1-R-6.
- **E1-R-10** Unknown `visible-if` and missing `type` must degrade to defaults; a lesson must never be
  rejected for them.
- **E1-R-11** A missing interaction for a code block is a **content defect**, surfaced to the developer
  and rendered as an empty block to the learner. Validators should reject such documents at authoring
  time; the runtime deliberately does not.

## Evidence labels
E1-R-1…R-11: **VERIFIED_STATIC** (parser + models). The *validator* recommendation in E1-R-11 is
**INFERRED_HIGH** (a design recommendation, not observed behaviour).

## Limitations
Only the interactive-lesson format is specified; executable lessons (run/save files) use a different
payload and are out of scope.

## Unresolved
Payload fields of the five non-code modules are under-specified (`U-01`); the `<tables>` plural tag's
role is unresolved (`U-02`).

## Reproduction
Parse the shipped corpus with any implementation of E1-R-3…R-8 and compare module counts against the
census in `mimo-re/complete-extraction/01_STATIC_CODE/` (20,306 documents, 29,093 gaps).
