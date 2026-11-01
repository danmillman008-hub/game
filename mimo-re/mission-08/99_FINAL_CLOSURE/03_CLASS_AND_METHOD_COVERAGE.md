# 03 — Class and method coverage (honest denominators)

## 1. Inventory

| Metric | Count | Denomination |
|---|---|---|
| Class definitions | **29,454** | every class in the 13 DEX files |
| App-named classes | 3,133 | package under the app namespace |
| Renamed app classes | 1,148 | app classes relocated to obfuscated names (Stage 1) |
| Orphan lambdas | 1,379 | lambdas without a recoverable owner (265 resolved in Stage 1) |
| Merged classes | 47 | R8 merged unrelated classes into shared shells |
| Decompiled Java files | 3,284 | decompiler output |
| Invalid Java files | 431 | output that does not parse |
| Deep-investigation queue | 2,178 | prioritised classes (P0 45 / P1 84 / P2 212 / P3 1,837) |
| Queued without a body | 1,059 | no recoverable body → `BLOCKED_BY_MISSING_DECOMPILED_BODY` |
| Methods with a status record | 637 | explicit per-method disposition |
| Typed call edges | **85,724** | over 138,025 call sites |
| Runtime-verified classes | **0** | no execution environment |

## 2. Denominators — stated explicitly, because percentages are meaningless without them

* **"Class coverage"** below is always *classes with a recorded disposition ÷ 29,454*, and separately
  *÷ 3,133 app-named*. Third-party SDK classes are counted but never deeply analysed.
* **"Behaviour coverage"** is *domains rated COMPLETE ÷ 45*, not a class ratio.
* A class that appears in the inventory but was never opened counts as `SIGNATURE_ANALYZED`, never as analysed.

## 3. Disposition by kind

| Disposition | Count | Meaning |
|---|---|---|
| DEEP_ANALYZED | 330 (mission-07 deep set) + 180 bodies + Stage 3–7 additions | body read, behaviour reconstructed |
| CALL_CHAIN_ANALYZED | 85,724 edges cover the reachable app graph | edges, not bodies |
| SIGNATURE_ANALYZED | remainder of the 3,133 app-named | name/fields/annotations only |
| GENERATED_CODE | Hilt/Dagger factories, Room `_Impl`, Kotlin synthetics | framework output |
| THIRD_PARTY | remainder of 29,454 | SDK/vendor |
| RESOURCE_OR_ASSET | DEX BuildConfig/R stubs of the 10 locale modules | 1,096 B each |
| DUPLICATE_OR_SYNTHETIC | 1,379 orphan lambdas + 47 merged shells | structural artefacts |
| UNRESOLVED | 1,148 renamed classes not yet mapped | obfuscation residue |
| BLOCKED_BY_MISSING_DECOMPILED_BODY | 1,059 of the queue | no body available |

Machine-readable: `03_CLASS_DISPOSITION.csv`. Method-level register: `mission-08/01_DEEP_CLASS_INVESTIGATION/06_METHOD_STATUS_REGISTER.csv`.

## 4. Critical-path coverage (the only ratio that matters for behaviour)

| Critical path | Classes on it | Deep-analysed |
|---|---|---|
| content load → parse → render | `ye.b`, `te.a`–`te.g`, `te.c`, renderer | yes |
| lesson state → grading → feedback | `base.c` + 6 `E0` graders + `qm.*` + `jm.*` | yes |
| progress → outbox → POST | `LessonProgress*`, `cg.*`, `lal.*` | yes |
| completion → UI flags | `completion.a`, `attach*`, `GetPathMapState` | yes |
| auth → request | `ku.a`, `fh.a`, `hg.e` | yes |
| tutor / execution | `aitutor.a`, `pg.a` | partial (frame schema blocked) |

## 5. Known blind spots

1,059 queued classes have no body; 8 questions are blocked on the artifact; the WebSocket frame schema, the WebView JS
surface, the DAO lambda id table and the Room builder flag values are the concrete holes. They are enumerated in
`14_ALL_OPEN_QUESTIONS_CLOSURE.json`, not hidden.
