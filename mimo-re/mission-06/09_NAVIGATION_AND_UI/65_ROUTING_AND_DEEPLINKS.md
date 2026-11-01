# Mission 6 — Routing and Deep Links

## Scope
URL scheme → in-app destination mapping.

## Method
Manifest `intent-filter`s (12 × `https://getmimo.com/*` on `MainActivity`), `mimo://` scheme, argument
extraction in the activity.

## Findings (VERIFIED_STATIC)
- One host (`getmimo.com`) + one custom scheme (`mimo://`), both routed through `MainActivity`.
- Because all 12 filters target the same activity, path routing is **data-driven**: the activity reads the
  URI (path/host fragments) and dispatches. The exact path grammar was not recovered (`Q-109`).
- Notification payloads use the same entry point (FCM receiver → activity intent) (`INFERRED`).
- Pusher/WebSocket do **not** deep-link: they update state, not navigation (Phase 7.54).

## Evidence labels
Hosts, scheme, single entry activity: **VERIFIED_STATIC**. Path grammar: **NOT_RECOVERED**.

## Open questions
`Q-109` path grammar; `Q-90` notification → route mapping.

## Reproduction
`grep -A3 'getmimo.com' /tmp/manifest.xml | head -20`
