# Mission 6 — Interaction Taxonomy

## Scope
Every interaction kind the lesson engine can grade, with the discriminator that the client uses.

## Method
Enumeration of `qm.d` branches (the verdict visitor), the four `ui.lesson.interactive.*` packages, the
`Interaction` model classes and the `<interaction type>` attribute vocabulary.

## Sources
`qm.d`, `qm.e/f/g`, `com.getmimo.ui.lesson.interactive.{fillthegap,selection,spell,validatedinput}.*`,
`evidence/PARSER_GRAMMAR.json`.

## Findings
| Kind | VM package | Input channel | Verdict source | Notes |
|---|---|---|---|---|
| `FILL_THE_GAP` | `fillthegap` | tap on option chips | option `correct` flag | options carry styled spans (`c`,`d`) |
| `SELECTION` | `selection` | tap on `<item>` elements | item `correct` flag, `iscode` styling | module-level, not inside code |
| `SPELL` | `spell` | tap letters to spell the token | option `correct` | same verdict path as fill-the-gap |
| `VALIDATED_INPUT` | `validatedinput` | free text | expected string = `content[startIndex,endIndex]` | **only** kind with the 300 ms delay |

Module kinds (not interactions): `PARAGRAPH`, `CODE`, `SELECTION`, `IMAGE`, `WEBVIEW`, `DATABASE`.

## Findings — what does *not* exist
No drag-and-drop, ordering, matching-pairs, multi-select, audio or free-code interaction class was found
in the recovered UI packages. `EXECUTABLE_FILES` lessons are a separate content type (Phase 3.23), not an
interaction.

## Evidence labels
Four kinds and their verdict sources: **VERIFIED_STATIC**. Completeness of the list ("nothing else
exists"): **INFERRED_HIGH** — based on four UI packages, one verdict visitor and no other `qm.d` branches.

## Open questions
`Q-42` whether `SELECTION` can be multi-answer (`item`×n with several `correct`); `Q-43` spell alphabet
source (content vs locale).

## Reproduction
`ls /tmp/dad | grep 'ui.lesson.interactive' | sed 's/\..*//' | sort -u`
