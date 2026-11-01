# Phase 1.8 — Coverage denominators (explicit, so no percentage can be invented)

Every number below is measured in this mission; the command that produces it is named next to it.
**No percentage in mission-08 may be quoted without the denominator it belongs to.**

## 1. Class denominators

| Denominator | Value | How measured |
|---|---|---|
| `class_def` objects in the 12-dex set | **29,454** | `DEX(...).get_classes()` over `/tmp/x/*.dex` |
| rows in `mission-07/01_CLASS_UNIVERSE/02_COMPLETE_CLASS_INVENTORY.csv` | 29,454 | symmetric difference with the dex set = **0** both ways |
| classes with a `com.getmimo.` name | **3,133** | name prefix |
| … of those, names containing `$` | 2,095 | name contains `$` |
| … of those, **orphan lambdas** (immediate outer class absent from the dex) | **1,379** | outer name lookup in the same set |
| renamed app classes (short name, code references `com/getmimo/` types) | **1,148** | `tools/build_renamed_app_register.py` |
| merged classes (tag-byte constructor + switch) | **47** | `evidence/MERGED_CLASS_REGISTER.json` |
| library/obfuscated remainder | 29,454 − 3,133 − 1,148 = **25,173** | arithmetic, includes 47 merged |

**Ownership cannot be read off names.** The app's logic is split across the `com.getmimo.*` namespace *and*
1,148 short-named classes. A defensible app-logic denominator is therefore a *range*, and mission-08 states it
as one:

* **lower bound** = app-named classes that are not lambdas = 3,133 − 2,095 = **1,038**
* **upper bound** = lower bound + renamed app classes = **2,186**
* (the 1,379 orphan lambdas are glue code belonging to those same classes; they are not counted twice)

## 2. Method denominators

| Denominator | Value | How measured |
|---|---|---|
| methods in `03_METHOD_INVENTORY.csv` | **15,087** | mission-7 inventory (app-relevant index) |
| methods in the 61 classes of the Phase-1 register | **637** | `06_METHOD_STATUS_REGISTER.csv` |
| … `BEHAVIOUR_RECONSTRUCTED` | 9 | register |
| … `DEX_INSPECTED` | 44 | register |
| … `JAVA_INSPECTED` | 2 | register |
| … `BODY_PRESENT_NOT_READ` | 561 | register |
| … `SIGNATURE_ONLY` | 21 | register |
| … `RUNTIME_TESTED` | **0** | nothing executed |
| methods with ≥ 1 static caller inside the dex set | 368 | caller scan |
| methods with **no** static caller | 269 | caller scan (framework entry points necessarily included) |

## 3. Source denominators

| Denominator | Value |
|---|---|
| decompiled `.java` files | 3,284 |
| … containing invalid `= ;` fragments | 431 (13.1 %) |
| queue classes with `.java` | 1,119 / 2,178 (51.4 %) |
| queue classes DEX-only | 1,059 / 2,178 (48.6 %) |
| renamed app classes with `.java` | 36 / 1,148 (3.1 %) |

## 4. Phase-1 conclusion in denominator terms

Phase 1 established behaviour for **9 methods in 6 classes**, out of:
* 637 methods in the inspected set (1.4 %),
* 2,178 queue classes (0.3 %),
* 29,454 `class_def`s (0.02 %).

Those are the honest fractions. Mission-7's "41 open questions, 17 closed" summary, by contrast, had no
denominator at all and was arithmetically wrong (see `00_BASELINE/HISTORICAL_COUNT_AUDIT.md`).

## 5. What will move these numbers

| Future phase | Effect on denominators |
|---|---|
| Phase 2 (relationships) | methods with traced callers move from 368 to a measured value |
| Phase 3 (subsystems) | behaviour statements per subsystem, still against 637/15,087 |
| Phase 10 (complete coverage) | every one of the 29,454 class_defs must end in exactly one bucket: investigated, informed-exclusion, library, or blocked |
| Phase 13 (semantic tests) | `TEST_DERIVED` grows; nothing becomes `RUNTIME_TESTED` |
| Phase 14 (runtime) | reassess availability; if still unavailable, `RUNTIME_TESTED` stays 0 and every affected claim stays `INFERRED`/`VERIFIED_STATIC` |
