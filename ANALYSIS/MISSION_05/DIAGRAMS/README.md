# DIAGRAMS — MISSION 05

Four Mermaid diagrams, each annotated with the M05 evidence vocabulary. They
visualise **verified components** and **explicitly inferred edges**; they are not
new architecture proposals.

| File | Content |
|---|---|
| `architecture.mmd` | client layer map: APK assets → loader → UI → Room/DataStore → Retrofit endpoints |
| `content_data_flow.mmd` | shipped curriculum → DSL parser → evaluation → local progress → sync outbox |
| `application_state_machine.mmd` | launch → onboarding → path → chapter → lesson → chapter-end, with `VERIFIED_RUNTIME` vs `INFERRED` labels |
| `lesson_flow.mmd` | single-lesson lifecycle: correct / wrong / partial / retry / completion |

Render with any Mermaid viewer. Solid edges = local; dashed = network
(`SERVER CONFIRMED = 0`).
