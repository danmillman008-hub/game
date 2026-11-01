# Mission 6 — User Properties

## Scope
User-level attributes sent to analytics.

## Findings
1. `PublicUser`-shaped attributes (premium flag, streak length, leaderboard first-place count) are the
   natural candidates, but **no `setUserProperty`/`setUserId` call site was recovered**.
2. Adjust requires an ad-id/attribution identity; `libsigner.so` exists, so attribution identity is
   handled in native code (**VERIFIED_STATIC for the library, NOT_RECOVERED for the fields**).
3. Lesson-level context is passed via typed enums (`AiTutorInteractionSource`), i.e. properties are
   **strongly typed**, not free-form maps — a good structural finding, but the property *names* remain
   unknown.

## Evidence labels
As marked.

## Open questions
`Q-133` user-property names; `Q-134` consent handling (GDPR surface not found).
