# Mission 7 — Complete Class Universe

## Method
`tools/build_m7_inventory.py` reads all 12 DEX files with androguard `DEX.get_classes()` and classifies every
descriptor; decompiled files in `/tmp/dad` are matched by name.

## Result (VERIFIED_STATIC)
| Kind | Classes |
|---|---|
| application-owned (`com.getmimo.*`) | 1,563 |
| application anonymous/inner (`$1`, `$2`, …) | 1,570 |
| obfuscated application candidates (top-level single-letter packages) | 13,113 |
| target-modified base (`bin.ghost.*`) | 19 |
| third-party libraries | 10,351 |
| other/unclassified | 2,838 |
| **total** | **29,454** |

Decompiled to source: **3,284 files** covering **15,087 methods** (`03_METHOD_INVENTORY.csv`).
Deep-investigation queue: **2178** classes, priority-ordered (`04_DEEP_INVESTIGATION_QUEUE.csv`).

## Interpretation
- The 13,113 "obfuscated-app-candidate" classes are Mimo code whose packages were renamed (e.g. `te.a`, `qm.i`,
  `ae.m`). They are *not* a separate library: they call `com.getmimo.*` types and resource ids.
  Distinguishing them from the 2,838 "other" is heuristic (top-level package of 1–3 lowercase letters).
- `bin.ghost.*` (19 classes) is part of the target build; treated as base-Application infrastructure
  (`97_BIN_GHOST_APPLICATION_ARCHITECTURE.md`).
- Inventory coverage is complete; **behavioural** coverage is not — see `08_CLASSES_NOT_YET_UNDERSTOOD.md`.

## Reproduction
```bash
/tmp/venv/bin/python tools/build_m7_inventory.py --dex-dir /tmp/x --src /tmp/dad --out-dir 01_CLASS_UNIVERSE
```
