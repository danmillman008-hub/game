# Mission 6 — Native Libraries

## Scope
Every `.so` in the APK, by ABI, with role.

## Method
`assets/`+`meta/lib/{arm64-v8a,armeabi-v7a}` listing, size/name analysis, class references.

## Findings (VERIFIED_STATIC)
| Library | Size | Role | Evidence |
|---|---|---|---|
| `librive-android.so` | 5.7 MB | Rive animation runtime | 59 `.riv` assets + Rive classes |
| `libsigner.so` | — | Adjust SDK signer (attribution) | Adjust classes present |
| `libc++_shared.so` | — | C++ runtime for the above | dependency |
| `libyrf.so` | — | **foreign** — injected by the repack/protection tool; pairs with `bin.ghost` base Application | not referenced by Mimo code; see `00_BASELINE/INTEGRITY_CAVEAT.md` |

Two ABIs: `arm64-v8a`, `armeabi-v7a`. **No x86/x86_64** → the app does not ship an emulator-compatible
native set, which constrains any future runtime verification (`95_RUNTIME_PREREQUISITES.md`).

Native analysis depth: **library inventory only**. No disassembly was attempted (no `objdump`/`radare2`
in the environment); sizes and symbol-free inference only (`Q-136`).

## Evidence labels
Inventory **VERIFIED_STATIC**; roles **VERIFIED_STATIC** (via API class evidence) except `libyrf.so`
(**INFERRED_HIGH** as foreign).
