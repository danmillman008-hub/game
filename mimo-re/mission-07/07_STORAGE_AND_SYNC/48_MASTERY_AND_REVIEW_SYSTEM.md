# Mission 7 — Mastery and Review

## Result: **no mastery system, no review system** (VERIFIED_STATIC, negative evidence)
Searched for and not found:
- interval / ease / due-date / next-review fields in DTOs, entities, or preferences;
- any table besides the three progress tables;
- any algorithm reading `attempts` history (the grader is stateless; `qm.i` sees one input at a time);
- any endpoint with `review`, `mastery`, `skill` in the catalogue.

## What exists instead
- `attempts`/`tries` per lesson (kept, never aggregated client-side),
- chapter difficulty tiers (authored),
- hard mode (learner-chosen),
- server pace for ETA.

## Why this matters
Any "adaptive review" claim about this app would be a backend-only behaviour at most. The client contributes
nothing to scheduling and stores nothing that could support it locally.
