# Phase 6 — open questions

| ID | Question | Evidence | Blocker |
|---|---|---|---|
| B-9 | are the two `Builder` booleans (`n`, `o`) `requireMigration=false` + `allowDestructiveMigrationOnDowngrade=true` (i.e. destructive fallback)? | the field pair matches `fallbackToDestructiveMigration()`; operands unreadable in the provider block | register values set before the linear window; needs a control-flow walk of a 1,643-instruction provider |
| B-10 | what key does `t.M / getLastInteractedTrackId` read? | the recovered writer key is per-track (`…_<trackId>`), the reader is a track id lookup | key is passed through the generic preference helper |
| B-11 | full key set of `mimo_prefs` / DataStore | generic helper takes key names as parameters | static enumeration requires data-flow on every call site |
| B-12 | does `com.getmimo.data.local.a` store anything learner-related? | built beside the DB, Preferences protobuf classes present | key set not enumerated |
| B-13 | is there any writer of `tutorial_completions` besides `fetchTrackCompletion`? | only one insert site found | negative claim limited to reachable code in this build |

## Non-claims

* No claim that the database is encrypted: no SQLCipher class, no `SupportOpenHelperFactory` argument in the builder
  block (the only keystore string `android-keystore://firebear_main_key_id_for_storage_crypto.` belongs to a
  third-party SDK).
* No claim about `clearAllTables` being reachable from the UI (it is a library API; no app caller found).
