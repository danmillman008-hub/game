# Mission 7 — Blocked Investigations

| Investigation | Blocker | Exact prerequisite |
|---|---|---|
| runtime verification (15 planned tests) | no device/emulator/account/network to `api.mimo.org`; ARM-only libs | authorised ARM device + stock build + test account |
| native symbol/disassembly analysis | no `readelf`/`objdump`/`radare2` | any ELF tool; or `pip install pyelftools` + parse |
| locale module contents | modules absent from APK | APK + split APKs / Play delivery capture |
| cross-version behaviour diff | only one APK version | a second version |
| full-tree decompilation (26k classes) | DAD ~40 s/100 classes, 2.6 GB RSS, session time budget | long-running batch job outside this session |
| layout→token mapping | 1,531 layouts need decoding + inflation semantics | aapt2 / layout decoder |
| webview JS bridge semantics | JS assets + bridge class not recovered | decompile bridge + inspect JS bundles |

## Method note
Each blocker names a concrete prerequisite — none is "impossible in principle". Nothing in this list was marked
BLOCKED merely because a preferred tool was missing; alternative paths were tried first (e.g. the ARSC blocker
from Mission 6 was **solved** in Mission 7 by writing a manual parser).
