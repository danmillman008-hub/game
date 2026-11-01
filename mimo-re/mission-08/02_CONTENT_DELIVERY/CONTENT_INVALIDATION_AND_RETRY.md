# Phase 2.9 — Content invalidation and retry

## 1. What exists (proven)

| Mechanism | Evidence | Consequence |
|---|---|---|
| `publishSetVersion` | `TracksJson.publishSetVersion` = 753; carried on `Progress` | a content baseline exists that both the bundle and the stored progress can reference |
| not-found path | `getTrackById` strings: `"Track with id … not found. Original track id: …"`, `"Web Development track with id 50 not found"` | a lookup miss is *reported*, not silently substituted |
| per-locale document counts differ | 1,030 vs 1,032 JSON in `id`, `it`, `pl`, `tr` | locales are not copies of each other; the extra documents are not identified in this phase |
| live-preview provider | `ye.d` reads `/live_preview/tracks/...` | a second source can replace the bundled one at runtime (developer path) |

## 2. What does **not** exist (measured negatives)

* no HTTP request in the content path — there is no remote content refresh to invalidate;
* no `SharedPreferences`/DataStore key holding a *content* version (the only DataStore keys found are favourites and
  user preferences);
* no WorkManager job in the content packages;
* no checksum/hash of content files.

## 3. Consequence — the honest statement

Content invalidation in this build is **shipping-time, not runtime**: content changes only when a new APK (or a new
publish set) is installed. A publish-set bump therefore cannot arrive through the network; it arrives with the app.

Retry semantics are consequently limited to *read/parse* failures, and Phase 2 did not find an exception handler on
the `ye.b.d()` / `ye.b.b(J)` stream path. Whether a parse failure crashes the load or is caught upstream is
**UNKNOWN** and recorded as question **A13**.

## 4. Open questions raised

| ID | Question | Status |
|---|---|---|
| A11 | is `getPublishSetVersion` compared against a stored value anywhere? | open |
| A12 | does a missing locale fall back to `en`? | open |
| A13 | are stream/parse errors caught, and at which layer? | open |
