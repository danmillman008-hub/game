# Mission 6 — Architecture Overview

## Scope
The architectural pattern **actually** present, with evidence: dependency direction, state ownership,
threading boundaries and the mechanisms that connect subsystems.

## Method
DI factory analysis; interceptor and repository reads; view-model inheritance; package census; call-site
reads recorded in `evidence/` and in the per-domain documents of this mission.

## Sources
`evidence/DI_GRAPH.json`, `01_APK_AND_ARCHITECTURE/07_DEPENDENCY_GRAPH.json`,
`01_APK_AND_ARCHITECTURE/08_CALL_GRAPH.json`, plus the domain documents referenced below.

## Findings
1. **Pattern: single-activity Compose UI + Hilt DI + repository/data-source layering, with a sealed
   state-machine core for lessons.** The evidence is structural, not nominal:
   - one `MainActivity` carrying all deep links, with features delivered as Compose destinations and
     Fragments for onboarding/lesson flows;
   - a 127-case generated component factory (`ae.m`) whose only job is constructing singletons —
     i.e. constructor injection throughout, no service locator;
   - repositories (`LessonProgressRepository`, `AiTutorRepository`, `RemoteLivePreviewRepository`)
     owning their data sources, with Retrofit interfaces injected rather than built.
2. **State ownership**: lesson state is owned by view models, but the *generic* lesson state machine is
   a single base class (`com.getmimo.ui.lesson.interactive.base.c`) with four per-type subclasses
   (fill-the-gap, selection, spell, validated input). Progress state is owned by
   `LessonProgressRepository` + `LessonProgressQueue` (in-memory queue over Room).
3. **Threading**: coroutines (`d70.b` = `Continuation`) are the universal async boundary; the database
   and network layers are suspend-based. Streaming paths use two non-coroutine transports: SSE
   (`okhttp3.sse`) for the AI tutor and a raw `WebSocketListener` (`pg.a`) for code execution.
4. **Event mechanisms**: no global event bus was found in the traced paths. Cross-cutting updates travel
   as `Flow`s (e.g. connectivity monitor `com.getmimo.network.b`, content streams) or as one-shot
   `LiveData`-style events from the lesson VM (`h` = solved event).
5. **Error propagation**: the offline guard throws a typed `NoConnectionException` inside the OkHttp
   chain, so "offline" is an exception at the call site rather than a null/empty result. Progress
   writes are never lost on failure — they stay queued (`in_queue = 1`).
6. **Obfuscation vs architecture**: package names are preserved for `com.getmimo.*`, which makes the
   *product* architecture readable; but the parser, verdict types, DAOs, annotations, interceptors and
   the DI monolith live in obfuscated packages. A reconstruction that only reads `com.getmimo` will
   systematically miss the engine (this was missions 1–4's failure mode).
7. **The artifact is modified** (see baseline I-1/I-2): the Application superclass comes from
   `bin.ghost.yrf`, so the *top* of the component graph is not Mimo's code.

## Evidence labels
Points 1–6: **VERIFIED_STATIC** individually (each cites a read artifact); the *pattern label* is
**INFERRED** (a name for the observed structure, not a claim from the code).

## Limitations
No Compose navigation inspection beyond the single `nav_onboarding_graph.xml`; no DI *scope* analysis
(singleton vs activity-retained) beyond the component holder; runtime object lifetimes unknown.

## Open questions
`Q-11` DI scoping and lazy vs eager component creation; `Q-12` where `MainActivity` hosts Compose vs
Fragment destinations; `Q-13` whether any module is dynamically loaded.

## Reproduction
See `07_DEPENDENCY_GRAPH.json` and `08_CALL_GRAPH.json`; both are small, readable JSON files that name
their evidence per edge.
