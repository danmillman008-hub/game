# MISSION 06 — ARCHITECTURE DIAGRAMS (Mermaid)

| File | Subject |
|---|---|
| `01_full_architecture.mmd` | whole client: APK assets → loaders → domain → UI → Room → client-side boundary |
| `02_class_dependency.mmd` | real DI/class dependency edges |
| `03_content_pipeline.mmd` | locale → AssetManager → JSON → XmlPullParser → modules → renderer |
| `04_lesson_execution.mmd` | lesson lifecycle from `LessonBundle` to progress |
| `05_interaction_validation.mmd` | five independent answer validators |
| `06_progression_state_machine.mmd` | Locked / Unlocked / UnlockedButNoKeys / Completed |
| `07_persistence_flow.mmd` | `LessonProgress` → Room `in_queue` → sync gate |
| `08_code_execution.mmd` | `solvedContent` comparison vs remote runner boundary |
| `09_offline_architecture.mmd` | local-capable vs client-side blocked vs server-owned |

Solid edges = `VERIFIED_STATIC` xref/field relation; dashed = `INFERRED` or client-side
boundary. `SERVER CONFIRMED = 0`.
