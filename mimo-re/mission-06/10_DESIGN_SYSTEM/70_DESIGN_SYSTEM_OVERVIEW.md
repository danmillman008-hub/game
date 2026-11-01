# Mission 6 — Design System Overview

## Scope
The structural design system: what exists, what is shared, what could not be recovered.

## Findings (VERIFIED_STATIC)
- **One typeface family in three cuts** (Aeonik Pro / Mono / Fono, 15 font assets incl. `font-family`
  XML descriptors) — see 72.
- **Two colour systems**: UI palette (resources, values BLOCKED) and editor/highlighting theme (code) —
  see 71.
- **Component layer**: Compose components under `ui.compose.components.*` (incl. internal `SpanCopier`) plus
  View-based fragments for the lesson flow — see 73.
- **Motion**: Rive (59 `.riv`) — see 68.
- **Iconography**: vector drawables in `res/drawable*` (63 dirs/files at the top level) — content not
  recovered as vectors.

## Evidence labels
Structure **VERIFIED_STATIC**; token values **BLOCKED** (71).

## Open questions
`Q-102`, `Q-104`, `Q-126` component inventory completeness.
