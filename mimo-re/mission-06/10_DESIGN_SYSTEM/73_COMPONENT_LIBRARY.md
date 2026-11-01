# Mission 6 — Component Library

## Scope
Shared UI components that a reconstruction would have to reproduce.

## Findings (VERIFIED_STATIC — from class/package names + behaviour)
| Component | Evidence | Notes |
|---|---|---|
| `PartiallyEditableEditText` | class in `ui.lesson.*` | edits only the answer window inside a rendered line; core of validated-input UX |
| span-based gap renderer | `qc.a`, `SpannableStringBuilder` usage | builds split segments for gap/selection |
| `SpanCopier` (+`FOREGROUND_COLOR`) | `ui.compose.components.internal` | copies styled spans into Compose |
| `CodingKeyboardView` | `ui.codeeditor.codingkeyboard` | symbol-heavy keyboard for code entry |
| syntax highlighter | `ui.codeeditor.utils.HighlightJsTheme` | per-theme token colours |
| lesson fragments (4) | `ui.lesson.interactive.*` | one per interaction kind |
| onboarding pager | 17-fragment nav graph | first-run flow |
| paywall/upgrade modals | `ui.iap.modal`, `ui.upgrade` | purchase surface |

## Evidence labels
Presence and role **VERIFIED_STATIC**; visual specification **NOT_RECOVERED**.

## Open questions
`Q-126`, `Q-129` reusable design-system module (no single `designsystem` package was found).
