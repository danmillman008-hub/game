# VERIFICATION — Mimo 9.35 offline-unlock APK

> **Correction:** APK signatures and static branch inspection do not establish installation or offline usability. No login bypass or full offline mode was implemented. See [OFFLINE_AUTH_AUDIT.fa.md](OFFLINE_AUTH_AUDIT.fa.md).

Target: original `Mimo_9.35 (1).apk` reconstructed from the user's three Drive
parts (`Mimo_9.35 (1).z01`, `.z02`, `.zip`), verified:

- APK size `142,353,499` B, SHA-256
  `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
  — identical to `ANALYSIS/MISSION_09/COMPLETE_PROGRESSION_ENGINE_SPEC.md`.
- `AndroidManifest.xml`: `versionName=9.35`, `versionCode=1792759685`,
  `minSdkVersion=28`, `targetSdkVersion=36`.
- 14,398 ZIP entries.

## Checks performed on the patched APK

| Check | Result |
|---|---|
| `apksigtool verify` | `v2 verified`, `v3 verified` |
| `zipfile.testzip()` | `None` (all CRCs valid) |
| ZIP entries | 14,395 (only the 3 old `META-INF` signature files removed) |
| Byte-diff vs original | exactly **1 changed entry**: `classes.dex` |
| `classes.dex` size | 16,237,920 B (unchanged) |
| `classes.dex` differing bytes | 169 (4 code sites + 24 B DEX header sha1/checksum) |
| DEX header | SHA-1 over body matches, Adler-32 checksum matches, magic `dex\n039\0` |
| `androguard` reparse | 12,944 classes / 65,536 methods, class/method table parsed; full verification not performed |
| Patched `keys/a.c()` | `const/4 v0,1` → `Boolean.valueOf(v0)` → `return-object v0` |
| `GetPathMapState` @0x4aa | `goto +23h` (was `if-nez v14,+23h`) |
| `GetPathMapState` @0x51a | `goto +20h` (was `if-nez v14,+20h`) |
| `cc/b.y` @0xcc | `nop ; nop` (was `if-eqz v7,+3h`) |
| STORED entries 4-byte aligned | 301 / 301, `resources.arsc` aligned |
| APK Signing Block | starts at 8-byte aligned offset, magic `APK Sig Block 42` present |
| 4-part split reassembly | `cat` of `.z01 + .z02 + .z03 + .zip` == full ZIP byte-for-byte; `unzip` OK |

The four patch sites were confirmed against the checked-in disassembly:
`0x4aa`, `0x4f0`, `0x51a`, `0x608` branch PCs in
`ANALYSIS/MISSION_06/10_LEARNING_PROGRESSION.md`; `keys/a.c()` @10048692 and
`cc/b.y` @8683988 in `ANALYSIS/MISSION_06/EVIDENCE/DISASM/INDEX.json`.

## What was NOT verified

- **No on-device / emulator run.** No Android runtime, ADB or KVM is available
  in this sandbox. UI behaviour (tapping a locked lesson, 3/3 sections) was
  therefore not observed live; the claim rests on static bytecode semantics,
  the checked-in state-machine evidence, and a verified v2/v3 signature (not an installation test).
- Server-backed features remain `SERVER_DEPENDENT`; `SERVER CONFIRMED = 0`
  (unchanged from the MISSION_09 evidence).
