# Mission 6 — Request DTO Catalogue

## Scope
Every request body/parameter shape used by the client.

## Method
Mission-05 catalogue (`API_CATALOG_V2.csv`) joined with field extraction over the DTO classes
(`evidence/DTO_FIELDS.json`).

## Findings (VERIFIED_STATIC)
- 62 endpoints; body binding 20, path 45, query 17, header 3 (endpoints can have several bindings).
- 50 distinct DTO types recovered; 39 of 50 have extractable field lists (`DTO_FIELDS.json`).
- Representative bodies:

| Body | Fields |
|---|---|
| `ExecuteFilesBody` | `files: List` |
| `ReportLessonBody` | `interactionType`, `reportOption`, `reportText`, `tutorialVersion` |
| `PostProgressRequestBody` | `progressList: List` |
| `StartConversation` (AI tutor) | `systemMessage`, `userMessage` |

- Verbs: GET 28 · POST 24 · PATCH 4 · DELETE 4 · PUT 2. The PATCH/PUT split matters for updates
  (mission-05 U-23, resolved per-endpoint in 52).
- Every path carries an `HttpMethod` annotation; the obfuscated verb wrappers are `ie0/f, o, n, b, p`
  (`f`=GET-like, etc.) — mapping verified per annotation, not per name.

## Evidence labels
Counts and fields **VERIFIED_STATIC**. 11 DTOs without fields are `NOT_RECOVERED` (obfuscated or
inherited).

## Open questions
`Q-83` the 11 missing DTO field sets; `Q-84` optional/required semantics per field.

## Reproduction
`python3 -c "import json;d=json.load(open('evidence/DTO_FIELDS.json'));print(sum(1 for v in d.values() if v['fields']),'/',len(d))"`
