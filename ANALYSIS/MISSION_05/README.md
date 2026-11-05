# MISSION 05 — OFFLINE ARCHITECTURE RECONSTRUCTION

Faithful reconstruction of the **Mimo 9.35 Android client** (not the backend).
Start with `MISSION_05_REVIEW.md`, then `OFFLINE_ARCHITECTURE.md`.

## Deliverables
| File | Purpose |
|---|---|
| `00_EXECUTION_PLAN.md` | short concrete execution plan |
| `OFFLINE_ARCHITECTURE.md` | reconstructed architecture and offline boundary |
| `CONTENT_MODEL.md` | shipped curriculum, DSL, answer keys, static↔runtime matches |
| `APPLICATION_STATE_MACHINE.md` | screens, transitions, onboarding/lesson lifecycle |
| `LEARNING_ENGINE.md` | evaluation, scoring, progression, rewards |
| `OFFLINE_DEPENDENCY_MATRIX.md` | 32-feature offline feasibility matrix |
| `LOCAL_STORAGE_MODEL.md` | exact Room SQL / DataStore / outbox |
| `NATIVE_LIBRARIES.md` | six `.so` purposes with JNI evidence |
| `EVIDENCE_DATABASE.json` | 112 classified findings |
| `DIAGRAMS/` | 4 Mermaid diagrams |
| `OPEN_QUESTIONS.md` | 17 unknowns with next experiments |
| `MISSION_05_REVIEW.md` | final review |
| `SCHEMAS/` | machine-readable content + JADX schemas |
| `SAMPLES/` | verbatim shipped assets |
| `EVIDENCE/` | asset manifest, DEX offsets, Room SQL, runtime↔static proof |
| `RUNTIME/` | per-run runtime findings |

Companion runtime evidence: `ANALYSIS/RUNTIME/MISSION_05/` (with verbatim
archives `RUN_42002808217/`, `RUN_42003884423/`, `RUN_42005358012/` and the
final run `42006697783` in place).

## Rules honoured
- Every finding classified: `VERIFIED_STATIC`, `VERIFIED_RUNTIME`,
  `VERIFIED_BOTH`, `INFERRED`, `UNKNOWN`.
- `SERVER CONFIRMED = 0`; no backend reconstruction or fabricated responses.
- Original APK SHA-256 `48ce1740…7c7a` unchanged; no APK/DEX/resource edits.
- M01–M04 deliverables and `mimo-ui/UPGRADE` untouched; no premature
  implementation, no redesign.
