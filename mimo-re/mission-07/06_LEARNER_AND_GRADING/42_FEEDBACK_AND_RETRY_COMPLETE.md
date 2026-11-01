# Mission 7 — Feedback and Retry (complete)

## Feedback sources (VERIFIED_STATIC)
| Type | Source | Trigger |
|---|---|---|
| correct text | paragraph module with `visible-if="correct"` | verdict CORRECT/PARTIAL |
| wrong text | paragraph module with `visible-if="wrong"` | verdict INCORRECT |
| always text | `visible-if="always"` / default | always |
| canonical answer | input overwrite with `expected` | normalised match only |
| console output | `<output>` module (console or table) | lesson render |
| server feedback | executable `consoleOutput` / `error` | after run |

## Animations
`.riv` assets exist (59) and `ui.sonar.*` (59 classes) is a UI-effect package, but **no code path binding a
specific animation to a verdict was recovered** — the animation layer is outside the decompiled subset.

## Retry
Unlimited. No cost, no lockout, no decreasing feedback. `attempts` records the count but nothing consumes it.

## Reveal
Wrong answers never reveal the solution; the expected string is only shown when the learner's answer was
already equivalent (normalisation path). No hint system exists (`CLOSED_STATIC`).
