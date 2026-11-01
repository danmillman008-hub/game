# Mission 5 — Decompilation Coverage

## Scope
What was decompiled, by which engine, with which selection rule — and what that selection rule cost.

## Method
Five batch runs of `tools/decompile_apk.py`; each emits a class inventory and a manifest containing the
SHA-256 of every input dex, the toolchain versions, per-phase timings and peak RSS.

## Sources
`evidence/CLASS_INVENTORY_*.csv`, `evidence/DECOMPILE_MANIFEST_*.json`.

## Findings
| Batch | Selection | Classes | Methods | Bytes |
|---|---|---|---|---|
| app | `--filter 'Lcom/getmimo'` | 3,133 | 12,851 | 8,121,129 |
| obfuscated 1 | explicit prefixes `Lte/ Lku/ Ldh/ Lhg/ Lie0/` | 42 | 88 | 78,401 |
| obfuscated 2 | `Lqm/ Lgm/ Lim/ Lnm/ Lpm/ Lcg/ Lth/ Lie0/ Lka0/ Ljm/ Lze/ Lv80/ Ldh/ Lhg/` | 129 | 444 | 253,574 |
| analytics | `Lcom/getmimo/analytics/Analytics*` | 13 | 55 | 36,102 |
| ghost | `Lbin/ghost/{YRF,yrf,cup,gho,dw,cp}` | 6 | 51 | 15,223 |
| **total** | | **3,323** | **13,489** | **8,504,429** |

**The selection rule is the finding.** A package filter is a *hypothesis about where code lives*; four
missions assumed the lesson parser lived under `com.getmimo` and were wrong. Any future pass must
enumerate packages first (`DEX.get_classes()` by top-level package) and never filter by prefix unless a
xref already proved the location.

## Evidence labels
Counts, timings, hashes: **VERIFIED_STATIC**. "Some classes were not emitted and are therefore
invisible" (e.g. `AiTutorRepository`, the analytics assembler): **INFERRED_HIGH** from absence plus
call sites that reference them.

## Limitations
DAD swallows per-method failures, so a class with source may still have unrendered methods. No smali
cross-check is possible without a JDK.

## Unresolved
`U-04` smali-level confirmation.

## Reproduction
Re-run any batch with the same `--classes-file`; compare `classes_decompiled` against the table above.
