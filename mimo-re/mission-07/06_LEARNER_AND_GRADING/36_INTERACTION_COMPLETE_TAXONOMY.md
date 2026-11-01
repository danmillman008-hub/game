# Mission 7 — Complete Interaction Taxonomy

| Kind | Input | Where declared | Grader | Client/server |
|---|---|---|---|---|
| `FILL_THE_GAP` | tap option chip | `<interaction type>` inside `<code>` | option identity vs `correct` | **client** |
| `SELECTION` | tap `<item>` | `<selection>` module | item `correct` flag | **client** |
| `SPELL` | tap letters | `<code>` interaction | same verdict path as fill-the-gap | **client** |
| `VALIDATED_INPUT` | free text | `<code>` interaction | expected = `content[startIndex,endIndex]`, exact→normalised | **client** |
| executable run | code submission | `EXECUTABLE_FILES` lesson | server (`hasPassed`/`tests`) | **server** |

## Evidence
- Four UI packages (`fillthegap`, `selection`, `spell`, `validatedinput`) and four `qm.d` branches.
- `Q-42` closed: no `multiple` attribute exists in the DSL or the corpus → selections are single-answer.
- Nothing else exists: no drag/order/match/multi-select/audio interaction class was found.

## Ownership statement
Interactive grading is **entirely client-side**; only executable lessons are server-graded. This is now a
two-value distinction, not a spectrum ("hybrid") — no hybrid interaction was found.
