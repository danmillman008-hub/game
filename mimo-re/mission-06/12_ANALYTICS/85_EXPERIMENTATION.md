# Mission 6 — Experimentation

## Scope
A/B testing / feature-flag experimentation visible to the client.

## Findings (VERIFIED_STATIC)
1. Firebase Remote Config has only **3 defaults** (Phase 11.77) — a very small switch surface, consistent
   with flags rather than a full experiment matrix.
2. No experiment-assignment class, variant enum or exposure-tracking call was recovered.
3. Because flags are read by key and the keys' consumers were not traced (`Q-118`), **client-side
   experimentation cannot be ruled out**; server-side experimentation is invisible to the client by design
   (RULE 4).

## Evidence labels
Point 1–2 **VERIFIED_STATIC** (as negative evidence); conclusion **UNKNOWN**.

## Open questions
`Q-118`, `Q-135`.
