# Phase 2.8 — Content cache

Three distinct caches exist, at three layers — and none of them is a database.

| Layer | Structure | Owner | Evidence |
|---|---|---|---|
| asset stream cache | `LinkedHashMap` field `c` | `ye.b` | field table + `<clinit>` strings `lessons-`, `/tracks` |
| parsed bundle cache | field `c: TracksJson` + field `d: HashMap` | `DefaultTracksRepository` (`tracks.c`) | field table; `c()J` reads the cached bundle |
| favourite tracks | DataStore preference keys | `DefaultFavoriteTracksRepository` (`tracks.a`) | strings `favorite_tracks`, `favorite_tracks_to_sync`, `favorite_tracks_to_remove` |

## 1. Asset layer (`ye.b`)

* `d()` opens `<base>/tracks.json`, `b(J)` opens `<base>/tutorial-<id>.json`;
* `a(Tutorial)` post-processes a parsed tutorial;
* the `LinkedHashMap` is an in-process memo, so repeated reads of the same tutorial inside one session do not touch
  the asset manager twice — the *key* was not read (Phase 2 records the structure, not the key semantics).

## 2. Bundle layer (`DefaultTracksRepository`)

* one `TracksJson` (the whole `tracks.json`) plus a `HashMap` used for id lookups;
* `getTrackById` (226 insns) contains the not-found strings, i.e. the cache miss path is *within the repository*;
* `loadTrackWithChapters` (409 insns) is the heaviest method and the one that must reconcile chapter/lesson objects
  with the identifier model.

## 3. Favourites

DataStore keys are the only content-adjacent state that is persisted locally, and they are keyed by *track*, not by
lesson. Favourites therefore survive a publish-set bump.

## 4. What is *not* cached

| Thing | Status |
|---|---|
| parsed lesson DSL | not cached by the loader; parsing is per-open (the `te.c` dispatcher is injected into the loader, not into a cache) |
| images/icons | referenced as `file:///android_asset/lessons-common/icons` base URL — no cache layer observed |
| remote content | no remote content path exists in the repository (only favourites sync) |

## 5. Measured negative

No Room entity, DAO or migration is involved in content delivery. Mission-06's three Room tables belong to
progress/learner state (Phase 5/6), not to content.
