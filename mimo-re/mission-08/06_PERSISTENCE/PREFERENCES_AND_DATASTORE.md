# Phase 6C — preferences and DataStore

## 1. App preference files

| File | Evidence | Content (evidenced) |
|---|---|---|
| `mimo_prefs` | `const-string "mimo_prefs"` | app preferences; **contains `last_interacted_tutorial_id_<trackId>`** (`putLong` in `CompletionRepository.fetchTrackCompletion`) |
| `mimo_prefs_global` | `const-string "mimo_prefs_global"` | global/one-shot flags |
| `mimo_dev_prefs` | `const-string "mimo_dev_prefs"` | developer menu state (`DevMenuStorage`, gate `sk/a.e()`) |

## 2. Keys

Only one key is evidenced end-to-end in this phase:

```text
key format : "last_interacted_tutorial_id_" + trackId
writer     : CompletionRepository.fetchTrackCompletion(trackId, trackVersion)
reader     : t.M() -> getLastInteractedTrackId  ("continue where you left off")
value      : long (tutorial id)
```

There is a real asymmetry worth recording: the **writer is per track** (`last_interacted_tutorial_id_<trackId>`) while
the reader `t.M` asks for a single *track* id — the reader therefore cannot be reading this same key for a track id;
it is consistent with a per-track "last tutorial" pointer plus a separate global "last track" value, but the global
key was not recovered (question **B-10**).

## 3. Generic preference helper

Keys inside `mimo_prefs` are read/written through a generic wrapper, so the key name is a *parameter*, not a literal at
the call site. That is why the census yields one evidenced key instead of a list: the remaining names are constructed
or passed in, and a static dump cannot enumerate them without following every argument. Recorded as a coverage limit,
not as absence of keys.

## 4. DataStore

`com.getmimo.data.local.a(Context, np/d)` is constructed in the same DI provider as the database. It is a
Preferences-DataStore-style store (`androidx.datastore.preferences` protobuf classes are present in the APK, plus the
`.preferences_pb` filename suffix and the standard "There are multiple DataStores active for the same file"
corruption message). Its key set was not enumerated in this phase.

## 5. Cross-store consistency

Nothing coordinates the three stores. A completion fetch writes Room rows **and** the preference; if the process dies
between them, Room keeps the completion and the pointer is stale. No transaction, no reconciliation code.
