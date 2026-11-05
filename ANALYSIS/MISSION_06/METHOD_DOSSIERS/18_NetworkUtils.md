# NetworkUtils — exact offline gate

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/NetworkUtils.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/network/a;` = `AndroidNetworkUtils`; `Lcom/getmimo/network/b;` =
`ConnectivityManagerNetworkMonitor`.

`a()Z` @10174360, 38 instructions:
```
val cm: ConnectivityManager
val net = cm.getActiveNetwork()          ?: return false
val caps = cm.getNetworkCapabilities(net) ?: return false
if (caps.hasTransport(TRANSPORT_WIFI))     return true
if (caps.hasTransport(TRANSPORT_CELLULAR)) return true
return false
```
`b()Z` @10174512 = `!a()` (isOffline). `a()` has 14 callers, `b()` 13 callers across
`LessonProgressRepository`, `ChapterViewModel`, `GetPathMapState`, AiTutor, practice tabs,
IAP, notifications.

### Verified client-side blocking method
`LessonProgressRepository.postUnsyncedLessonProgress(cont)` @`EVIDENCE/DISASM/LessonProgressRepository.smali.txt`:
```
if (!networkUtils.a()) {
    log("No internet connection, not posting unsynced lesson progress")
    throw NoConnectionException(...)
}
launch { /* POST unsynced rows */ }
```
Verb exact log string from DEX. `storeAndPostAllLessonProgress` calls
`moveLessonProgressFromQueue()` **before** this gate.

## Runtime correlation (M05, no new M06 run)
M05 `42002808217` cold start with `Active default network: none` showed
`NetworkUnknown` / `UnknownHostException` for analytics `cdp.customer.io`, no FATAL/ANR,
and the first three offline UI hierarchies were byte-identical to online. This is consistent
with the `hasTransport` gate above. `VERIFIED_BOTH`.

## Remaining uncertainty
- Whether `NetworkUtils` also checks `NET_CAPABILITY_VALIDATED` = `UNKNOWN` (only two
  `hasTransport` calls were recovered; no capability check visible).
