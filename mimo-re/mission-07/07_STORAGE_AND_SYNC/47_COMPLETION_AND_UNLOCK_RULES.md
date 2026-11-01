# Mission 7 — Completion and Unlock Rules

## Completion (VERIFIED_STATIC)
| Level | Rule | Where |
|---|---|---|
| exercise | verdict CORRECT/PARTIAL (client) | `qm.d/e/f/g` |
| lesson | learner proceeds after any verdict; `tries` records correctness | `base.c.U()` |
| chapter | `Chapter.isCompleted` + `chapter_completions` row | model + Room |
| tutorial | `tutorial_completions` row + progress push | Room + API |
| track | server-computed (`/v1/tracks/{id}/completion`) | server |

## Unlock (VERIFIED_STATIC / INFERRED)
- No locked-lesson check was found in the lesson VM: the VM will render any lesson it is given.
- Whether the *list* UI hides future chapters is not recovered (`INFERRED`: `isCompleted` and `hasProgress`
  exist specifically to drive such a UI).
- No gating by score exists (no score).

## Ambiguity that remains
A learner who answers everything wrong still completes lessons and therefore advances — the only difference is
`tries=0`. This is a deliberate design property (completion ≠ correctness) and is why first-try accuracy must be
derived, never read.
