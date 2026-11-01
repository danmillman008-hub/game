# Mission 7 — Complete Application Architecture

## Five layers, as built
1. **Presentation** — Fragment/View lesson surface (4 interaction fragments + base VM), Compose for newer
   screens, one deep-link entry activity.
2. **Interaction/domain** — `interactors.*`, `qm.*` assessment, `te.*` parsing. Thin, no use-case framework.
3. **Data** — per-feature repositories, remote sources (Retrofit), local sources (Room), typed DTOs.
4. **Infrastructure** — 127-arm DI switch, OkHttp with three interceptors, analytics singleton, SDK wrappers.
5. **Content** — bundled English assets + Play dynamic locale modules, interpreted by the bespoke DSL engine.

## Architectural signatures (all evidence-backed)
- **Hand-wired DI** with eager field ordering — no Dagger/Hilt/annotations.
- **Two lesson engines** — interactive (client-graded) vs executable (server-graded via REST/WSS).
- **Server-authoritative economy** — coins/keys/streaks/leagues are display-only client-side.
- **Typed analytics** — event objects `ge.j(name,index)` + typed properties; Firebase + Adjust dual dispatch.
- **Content is data, not code** — no content table, no content code, no plugin system: 7 parsers + fixed modules.
- **AB-test group flags** are the feature-flag mechanism, not a general Remote Config matrix (3 defaults).

## Where to go next
`105_COMPLETE_MIMO_ARCHITECTURE.md`, `106_MASTER_COMPONENT_GRAPH.json`, `113_END_TO_END_BEHAVIORAL_RECONSTRUCTION.md`.
