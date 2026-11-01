# Phase 2.1 — Content entry points

Every claim below names the recovered original class (from Stage 1 lambda evidence) and the concrete
`class_def` that implements it.

## 1. The content subsystem's four roles

| Role | Original class | Renamed `class_def` | Evidence |
|---|---|---|---|
| asset/live-preview provider | — | `ye.b` (AssetManager), `ye.d` (developer live preview) | interfaces `ye.f`; strings `lessons-`, `/tracks`, `/tutorial-`, `.json`, `/tracks.json`, `file:///android_asset/lessons-common/icons`, `/live_preview` |
| track loader / JSON reader | `DefaultTrackLoader` | `com.getmimo.data.content.tracks.b` | lambdas `…tracks.DefaultTrackLoader$getTutorial$2`; ctor `(am.l, te.c, np.d, hb0.b)` |
| track repository | `DefaultTracksRepository` | `com.getmimo.data.content.tracks.c` | 7-lambda family, share 0.875; fields `TracksJson`, `HashMap` |
| favourites repository | `DefaultFavoriteTracksRepository` | `com.getmimo.data.content.tracks.a` | 6-lambda family, share 1.0; DataStore keys |

## 2. Entry points (recovered methods)

| Recovered name | Class.method | Descriptor | Size | Notes |
|---|---|---|---|---|
| `getTracksJson` | `tracks.c.h` | `(Continuation)Object` | 86 insns | reads/caches the whole `tracks.json` |
| `getPublishSetVersion` | `tracks.c.h` *or* `tracks.c.c` | `(Continuation)Object` / `()J` | 86 / 18 | two families map to `h`; the `()J` accessor `c()` reads the cached `TracksJson` — the ambiguity is recorded, not resolved by preference |
| `getTracks` | `tracks.c.g` | `(Continuation)Object` | 69 | MEDIUM confidence (single lambda) |
| `getTrackById` | `tracks.c.d` | `(J, Continuation)Object` | 226 | strings `"Track with id … not found. Original track id: …"`, `"Web Development track with id 50 not found"` |
| `getTrackWithChapters` | `tracks.c.e` | `(J, Continuation)Object` | 86 | |
| `loadTrackWithChapters` | `tracks.c.i` | `(J, Continuation)Object` | 409 | largest method in the repository |
| `getTutorial` | `tracks.b.b` *and* `tracks.b.c` | `(J, Continuation)` / `(Continuation)` | 19 / 29+ | `b.b` collects `np.b.c` flow; `b.c` is deserialisation |
| `getInteractiveLesson` / `getExecutableLesson` | `tracks.b.a` | `(J, I, I)JsonObject` | 78 | one method serves both names — they are *selection* paths over the same JSON |
| `addTrackToFavorites` … `syncFavoriteTracksToRemove` | `tracks.a.a` … `tracks.a.f` | suspend | 70–143 | DataStore-backed |

## 3. Caller side (what is proven so far)

The typed call graph (Stage C) contains the repository's *callees*, but the UI callers are reached through
interfaces, so the caller edge is not a direct invoke. What is proven at this checkpoint:

* `tracks.b` (loader) is constructed with `te.c` — the DSL parser dispatcher — so **the loader is where parsed
  lesson content enters the app**.
* `tracks.c` (repository) holds the deserialised `TracksJson` and a `HashMap` cache, so it is the single source of
  track objects for the UI.
* The `Flow.collect` sites owned by `ui.path.map.j` (`PathMapViewModel`, 25 lambdas) and `ui.main.d` (`MainViewModel`,
  39 lambdas) are the largest consumers of track state in the graph.

Not yet proven: which exact ViewModel method triggers `getTracks` first after startup. That belongs to Phase 3.

## 4. What is *not* an entry point (measured negatives)

| Candidate | Why rejected |
|---|---|
| a network API for tracks | no app class builds a tracks request; `tracks.*` never references a Retrofit interface in its own body; content arrives through `ye.f` streams |
| Play Feature Delivery of lesson content | the 8 locale *code* modules are stubs (`BuildConfig`+`R` only), yet the locale **assets** (`lessons-<locale>/tracks/*.json`) are present in the base APK |
| a database table for tracks | `TracksJson` is an in-memory model; no DAO touches it |
