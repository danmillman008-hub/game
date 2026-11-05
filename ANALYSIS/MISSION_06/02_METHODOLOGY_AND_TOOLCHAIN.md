# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**Target:** original Mimo Android 9.35 APK, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Branch:** `arena/aebb90b7-game`, baseline `d0714b40`  
**Toolchain:** Androguard 4.1.4 in `/home/user/_work/m06/venv` over all 12 original
`ANALYSIS/_INPUT/classes*.dex`; patched read-only harness `EVIDENCE/M06_DEX_HARNESS.py`.  
`SERVER CONFIRMED = 0`. Backend services, server business logic, server databases and cloud
infrastructure are **not** reconstructed; only client-side boundaries are recorded.

> Every finding is classified `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_BOTH`,
> `INFERRED` or `UNKNOWN`. Evidence fields (APK path, class/method, DEX file + code offset,
> bytecode/Smali, caller/callee, SQL, runtime log, reproduction steps) are given inline or in
> the referenced `EVIDENCE/`, `SCHEMAS/`, `CALL_GRAPHS/`, `METHOD_DOSSIERS/` artefacts.

---

## Starting state (verified)
`git status --short` clean at `d0714b40` (`MISSION 05 FINAL…`); branch
`arena/aebb90b7-game`. M05 evidence reviewed: 42 deliverables, 112 evidence entries,
`EVIDENCE/ROOM_SQL.txt`, `SCHEMAS/JADX_MODEL_FIELDS.json`, `SCHEMAS/SHIPPED_CONTENT_STATS.json`,
`EVIDENCE/RUNTIME_STATIC_MATCH.json` (MATCH-1..5), five runtime run findings.
Original APK unchanged (142,353,499 B, SHA-256 above).

## Toolchain decisions — VERIFIED_STATIC
| Tool | Status | Decision |
|---|---|---|
| `java`, `jadx`, `jadx-gui`, `apktool`, `baksmali`, `dexdump`, `aapt`, `aapt2`, `radare2`, `ghidra`, `analyzeHeadless` | absent locally | not used |
| system `pip3 install androguard` | **failed** Debian PEP 668 `externally-managed-environment` | not retried |
| `/home/user/_work/m06/venv` + `pip install androguard` | **succeeded**, 4.1.4 | primary disassembler |
| M01 `ANALYSIS/_TOOLCHAIN/dexlib.py`, `dex_bytecode.py` | available | used as independent offset/call-graph cross-check |
| M02 `ANALYSIS/DEX_BYTECODE_EVIDENCE.json` | 6,016 edges / 1,211 exact | reused, not regenerated |
| JADX archive (`ANALYSIS/DECOMPILED/getmimo_sources.tar.gz`, 2,211 `.java`) | incomplete, many `Method not decompiled` | used only for field names; **not** treated as absence of implementation |

### Exact failure/cause records (requirement)
- `pip3 install --quiet --disable-pip-version-check androguard` →
  `error: externally-managed-environment`. Cause: Debian PEP 668. Alternative: venv, succeeded.
- Harness build #1/#2 produced `xrefs=0`. Cause: `DEX.get_methods()` returns
  `MethodIdItem` (no instructions); must iterate `d.get_classes()` → `c.get_methods()`.
- Build #3 `AttributeError: 'MethodIdItem' object has no attribute 'get_instructions'`.
- Build #4 `AttributeError: 'Instruction12x' object has no attribute 'get_offset'`;
  Androguard instructions expose `get_length()`, `get_name()`, `get_operands()`, `str(i)`.
  Fix: PC accumulator + regex over `str(i)`.
- **M06 xref bug found and fixed**: the original regex
  `(L[…]+;->[^\s,]+)` truncated descriptors containing spaces, e.g.
  `h0(Ljava/util/List; Z)V`, silently dropping call edges. Fixed to
  `(L[…]+;->.*)$` capturing to end-of-line; cache rebuilt from scratch
  (corrected cache: 78,560 xref targets). All call graphs in this mission use the corrected cache.
- Operand tuple repr is unsuitable for method refs; `str(i)` contains the full
  `Lclass;->method(...)`.

## Anti-decompilation — VERIFIED_STATIC + INFERRED
DEX contains exactly one `"Smob - Mod obfuscation tool v4.6 by Kirlif'"` string in
`classes.dex` (also emitted in `<clinit>` of `Lqm/i`, `Lte/a`, `Lye/b`, `ParserModule`,
`ModuleVisibility`, `Lgm/h` and several constructors). Bytecode streams contain injected
`const/4 vN, <small int>` no-ops that clobber registers not subsequently read, plus trailing
`fill-array-data-payload` objects inside the linear instruction stream. Example
`LessonProgress.isSolvedCorrectly()` has `const/4 v3, 2` immediately overwritten by
`const/4 v3, 1`. Causal link to M05's `JADX ERROR: NullPointerException in pass: ClassModifier`
is `INFERRED`, not proven. M06 filtered/annotated these decoys when reading branches.

## Deobfuscation technique — VERIFIED_STATIC
R8 renamed most classes to single letters but Kotlin synthetic inner-class names preserve
the original outer name. For each `X$foo$N`, parse `X` and read the first `<init>` argument
(the outer instance); the modal `X` is the original class name.
- 173 class mappings in `SCHEMAS/OBFUSCATION_MAP.json` (e.g. `base/c` →
  `InteractiveLessonBaseViewModel` 14 votes, `executable/q` → `ExecutableLessonViewModel`
  46 votes, `tracks/b` → `DefaultTrackLoader`, `network/a` → `AndroidNetworkUtils`).
- 596 method mappings in `SCHEMAS/METHOD_NAME_MAP.json` from coroutine inner-class
  `invokeSuspend` bodies. **Low-vote entries are heuristic**; only manually verified
  mappings (`V`, `X`, `W`, `U`, `Y`, `H`, `h0`, `d0`, `b0`, `e0`, `f0`, …) are used as
  facts in the call graphs and dossiers.

## Evidence pipeline
`dex → class/method index → disassembly → invoke xrefs → strings → fields → state
changes → pseudocode → dossier → diagram → evidence DB entry`.
`SCHEMAS/METHOD_CATALOG_MIMO.json` (6.8 MB) and `CLASS_CATALOG_MIMO.json` (1.6 MB) hold
per-method DEX file, code offset, instruction count, access, caller/callee counts and strings.

## What was NOT done
No backend reconstruction, no fabricated server responses, no account/login/purchase/
credential work, no auth bypass, no root/private DB extraction, no TLS/pinning bypass,
no APK modification, no replacement-app implementation, no repeated UI screenshot
collection, no new workflow dispatch.
