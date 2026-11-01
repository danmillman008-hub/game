# Mission 8 — Stage B Report (Phase 1: deep class investigation)

**Status:** complete for its defined scope · **Date:** 2026-11-01 · **Base:** Stage A commit `cfdde92`

## Delivered (9 artefacts)

| File | Content |
|---|---|
| `01_DEEP_CLASS_INVESTIGATION/01_PRIORITISATION_METHOD.md` | role-then-domain prioritisation, published rules, P0…P3 counts |
| `01_DEEP_CLASS_INVESTIGATION/02_CLASS_CATEGORISATION.csv` | 2,178 rows: priority, role, domain, source basis, flags, dex |
| `01_DEEP_CLASS_INVESTIGATION/03_PRIORITISED_QUEUE.json` | distributions, rule table, P0 list, DEX-only P0 list |
| `01_DEEP_CLASS_INVESTIGATION/04_DEEP_CLASS_INVESTIGATION.md` | C-01…C-08 records against a 23-point template |
| `01_DEEP_CLASS_INVESTIGATION/05_RENAMED_APP_LOGIC_REGISTER.csv` | 1,148 renamed app classes found by evidence, not by name |
| `01_DEEP_CLASS_INVESTIGATION/06_METHOD_STATUS_REGISTER.csv` | 637 methods, 11-value scale, callers by invoke kind, evidence refs |
| `01_DEEP_CLASS_INVESTIGATION/07_METHOD_BODY_INVESTIGATION.md` | Java vs DEX reading, worked `ku.a.d(Z)` skeleton, merged-class rule |
| `01_DEEP_CLASS_INVESTIGATION/08_COVERAGE_DENOMINATORS.md` | every denominator stated explicitly, with measured fractions |
| `01_DEEP_CLASS_INVESTIGATION/09_MERGED_CLASS_AND_STRUCTURAL_CAVEATS.md` | merged classes, renamed logic, orphan lambdas, decompiler corruption |
| `tools/build_m8_class_investigation.py`, `tools/build_renamed_app_register.py`, `tools/build_method_status_register.py` | deterministic builders |

## Priority distribution (2,178 rows)

`P0 45 · P1 84 · P2 212 · P3 1,837` — sum 2,178. Roles: `logic 378 · value 280 · enum 53 · component 3 · lambda 1,464`.

## Method status distribution (637 methods, 61 classes)

`BEHAVIOUR_RECONSTRUCTED 9 · DEX_INSPECTED 44 · JAVA_INSPECTED 2 · BODY_PRESENT_NOT_READ 561 ·
SIGNATURE_ONLY 21 · RUNTIME_TESTED 0`.

## Structural findings that change every later phase

1. **48.6 % of the queue is DEX-only** and **13.1 % of the decompiled Java is syntactically invalid** — so
   "decompiled" cannot be used as a proxy for "readable".
2. **1,148 app classes live outside the `com.getmimo` namespace** (renamed by the build's obfuscation) and
   **1,379 app-named classes are orphan lambdas** whose owner was renamed away. The Mission-7 queue cannot see
   either group.
3. **47 classes are merged** (tag-byte constructors with switches), so class-level responsibility statements are
   invalid for them; the register records branch-level facts only.
4. **Q-121 is answered** (Firebase ID token, no app token store) and the `ri.*` hypothesis is refuted — details
   and reproduction in `00_BASELINE/HISTORICAL_FINDINGS_RECONCILIATION.md` R-05.
5. `AuthenticationFragment` / `AuthenticationViewModel` / `PusherConnectionManager` are **renamed**, not absent;
   their lambdas survive, so the auth and Pusher UI wiring must be reconstructed from the renamed register.

## Not claimed

No method reached `RUNTIME_TESTED`; no `CALL_GRAPH_TRACED` yet (Phase 2); no class was declared out of scope yet
(Phase 10 owns exclusions).
