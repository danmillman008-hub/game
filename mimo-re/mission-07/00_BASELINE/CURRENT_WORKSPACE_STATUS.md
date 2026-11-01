# Mission 7 — Current Workspace Status (verified)

| Item | Value |
|---|---|
| Repository | `/home/user/game` (branch `arena/ecb8af07-game`) |
| Starting commit | `3db0902528945c64a107ca7663d459b541d632b3` (Mission 6) |
| Working tree before Mission 7 | clean |
| Target artifact | `/tmp/apk/Mimo_9.35 (1).apk` — 142,353,499 B, sha256 `48ce1740…`, md5 `f9cef2d8…` |
| DEX extracted | `/tmp/x` — 12 files |
| Decompiled tree | `/tmp/dad` — 3,284 `.java` files (Mission 5/6 batches + Mission 7 additions) |
| Resources | `/tmp/res` — 3,177 `res/*` + `AndroidManifest.xml` + `resources.arsc` |
| Toolchain | python 3.11.2 + androguard 4.1.4 + pytest 9.2.0 (`/tmp/venv`); **no java/jadx/apktool/aapt2/adb/emulator** |
| Mission-06 suites | 21 passed (mission-6), 23 (mission-4), 44 (mission-5) |

## Verified claims in the brief vs. workspace
| Brief claim | Verified | Note |
|---|---|---|
| 3,323 classes decompiled | **no, 3,284 .java files** | file count includes inner classes; the decompiled *class* count in Mission 6 was 3,323 |
| 29,454 classes in inventory | yes | `mission-06/01_APK_AND_ARCHITECTURE/06_CLASS_METHOD_INVENTORY.csv` (29,455 rows incl. header) |
| 62 endpoints / 50 DTOs / 29 tags | yes | mission-05 evidence |
| 59 Rive animations | yes | `find /tmp/x -name '*.riv' \| wc -l` |
| 15 runtime tests planned, blocked | yes | `mission-06/15_RUNTIME/96_TEST_TO_SOURCE_MATRIX.csv` |

## Reconciliation note
Mission 6's "3,323 decompiled" and the file count here are both true: 3,323 classes were decompiled across
batches, producing 3,284 files (nested classes collapse, synthetic `$1` types are dropped). Mission 7 adds 7
classes (`ri.a`, `ri.c`, `ge.j`, plus FCM/Pusher batch) — see `01_CLASS_UNIVERSE/01_CLASS_UNIVERSE.md`.
