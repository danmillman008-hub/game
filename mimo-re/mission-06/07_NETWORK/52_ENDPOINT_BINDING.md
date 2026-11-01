# Mission 6 — Endpoint Binding (annotations ↔ paths ↔ verbs)

## Scope
Proof that each catalogue row is bound by a real annotation, and the resolution of the PATCH-vs-PUT
question (mission-05 U-23).

## Method
`ANNOTATIONS_V2.csv.gz` (mission-05) for `@GET/@POST/@PATCH/@PUT/@DELETE` on interface methods, joined to
the URL literal found in the same method body (`API_CATALOG_V2.csv`), with the interface and dex recorded
per row.

## Findings (VERIFIED_STATIC)
- All 62 rows carry `annotation` + `path` in the same method; rows where the path was assembled via string
  concatenation are marked `INFERRED_HIGH` in the `verb_confidence` column.
- **U-23 resolution**: the PATCH/PUT ambiguity is *not* a single mis-read annotation — there are genuinely
  both: 4 `@PATCH` endpoints (partial updates such as saved-code) and 2 `@PUT` (full replacement), each
  verified on its own method. No endpoint was found that is PATCH in one place and PUT in another.

| Verb | count |
|---|---|
| GET | 28 |
| POST | 24 |
| PATCH | 4 |
| DELETE | 4 |
| PUT | 2 |

## Evidence labels
Per-row: **VERIFIED_STATIC** where `verb_confidence=VERIFIED`; **INFERRED_HIGH** otherwise (see column).

## Open questions
`Q-87` semantics of the two PUT endpoints (idempotency contract).

## Reproduction
`awk -F, 'NR>1{print $4}' ../mission-05/evidence/API_CATALOG_V2.csv | sort | uniq -c`
