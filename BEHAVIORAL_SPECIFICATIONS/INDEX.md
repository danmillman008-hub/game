# Behavioural Specifications — Index

| Spec | Subject | Component | Validation |
|---|---|---|---|
| `WS-01_KINEMATICS.md` | gravity variants, terminal clamp, air control, integration + freeze | `sor_engine/kinematics.py` | D1–D4, D9 |
| `WS-02_BODY_BOX_COLLISION.md` | two body boxes, table arithmetic, AABB predicate | `sor_engine/boxes.py` | D5, D6 |
| `WS-03_PROJECTION_CULLING.md` | world→screen, camera exception, cull window | `sor_engine/projection.py` | D7 |
| `WS-04_FRAME_COMPOSITION.md` | per-frame ordering that binds the three together | `reconstruction/slice_runner.py` | D8 |

Each specification follows the same 13-part structure: purpose, inputs, state,
formats, algorithm, edge cases, outputs, dependencies, timing, revision differences,
evidence, confidence, tests.

**Conventions.** Addresses are ROM file offsets in `REV 00` (`dd44f120…`). "Confirmed"
means read from the binary *and* reproduced by executing it. Fields are written
`+$XX` relative to the actor record base. All numbers are exact integers.
