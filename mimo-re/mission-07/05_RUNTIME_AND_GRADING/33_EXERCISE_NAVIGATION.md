# Mission 7 — Exercise Navigation

## What is recovered (VERIFIED_STATIC)
| Action | Implementation | Effect |
|---|---|---|
| submit | `Z(verdict)` | verdict state, no navigation |
| proceed / next | `U()` | marks solved, writes progress, moves to the next lesson (navigation call outside the VM) |
| retry | re-submit | `attempts++` |
| restart lesson | `a0()` | clears exercise state, emits `lesson_reset` |
| back / exit | Android back | no VM hook recovered |

## Not recovered
Skip, previous-exercise, cross-section navigation, resume-at-position and completion screens have **no**
recovered implementation: the VM has no such methods, and no navigation controller call was traced from the
lesson flow. The only resume signal in the contract is `LastInteractedTrackResponse` / `TrackCompletionResponse.
lastInteractedTutorialId` (**server-provided**), which can position the learner at a *tutorial*, not an exercise.

## Consequence
"Exercise navigation" in this build is: forward on success, retry on failure, restart on demand. Multi-exercise
lessons are a sequence rendered in one page (Phase 5.29), so there is no per-exercise navigation surface.
