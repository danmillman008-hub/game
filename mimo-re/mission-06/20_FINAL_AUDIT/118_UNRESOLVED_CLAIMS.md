# Mission 6 — Unresolved Claims

Every claim that could **not** be closed, with the reason and what would close it. Nothing here is
silently dropped; nothing here is asserted elsewhere in the mission.

| # | Claim / question | Status | Why it stays open | What would close it |
|---|---|---|---|---|
| 1 | Analytics event-name ↔ emitter binding (`U-20`) | NOT_RECOVERED | 252 literals extracted, wrapper methods (`np.h`, `be.d`, `oy.t`) not resolvable in DAD output | javap/JADX-grade decompile of the wrapper classes |
| 2 | `bin.ghost`/`libyrf.so` triggers (`U-18`) | BLOCKED (and out of Mimo scope) | injected by repack tool; only in this re-signed artifact | stock APK + native disassembly |
| 3 | Lesson reset effect on progress rows (`Q-08`) | UNKNOWN | reset path arguments unreadable in pseudo-Java | fragment-level trace or runtime |
| 4 | Keys/hearts consumption (`Q-57`) | UNKNOWN | no decrement in lesson code; may be server-side | runtime with server or server contract |
| 5 | Login/credential exchange (`Q-80`) | NOT_RECOVERED | auth repository not in decompiled batch | decompile auth packages |
| 6 | Token storage mechanism (`Q-121`) | NOT_RECOVERED | `ri.b` internals not recovered | decompile token holder |
| 7 | Design token values (`Q-102`) | BLOCKED | 3 ARSC API paths failed; no aapt2 | `aapt2 dump resources` |
| 8 | Dark theme (`Q-103`) | NOT_RECOVERED | resource config enumeration impossible | same as 7 |
| 9 | WebSocket message schema (`Q-40`) | NOT_RECOVERED | listener message parsing elsewhere | decompile socket message classes |
| 10 | REST vs WSS selection for code execution (`Q-39`) | UNKNOWN | both paths exist, selection logic unknown | read VM branch |
| 11 | Progress push trigger points (`Q-70`) | UNKNOWN | no WorkManager worker found | lifecycle trace |
| 12 | 4xx handling on push (`Q-69`) | UNKNOWN | no dead-letter path recovered | runtime |
| 13 | Completion aggregation / ETA formula (`Q-49`, `Q-50`) | UNKNOWN (server) | client sends rows only | backend access (out of scope, RULE 3) |
| 14 | Pusher channel usage (`Q-89`) | UNKNOWN | instantiation found, channels not | decompile channel classes |
| 15 | AI tutor prompt text & lesson context (`Q-92`, `Q-95`) | NOT_RECOVERED | string composition not readable | better decompiler |
| 16 | Quota threshold values (`Q-98`) | UNKNOWN (server) | payload carries count only | server contract |
| 17 | Accessibility configuration (`Q-111`) | NOT_RECOVERED | binary resources | aapt2 + runtime |
| 18 | `NUMBER` tag purpose (`Q-31`) | UNKNOWN | declared, unused by all 7 parsers | corpus scan for `<number` |
| 19 | Multi-correct selection behaviour (`Q-42`) | UNKNOWN | needs corpus statistics on `correct` cardinality | corpus scan |
| 20 | Full locale inventory (`Q-14`) | UNKNOWN | enum partial, modules truncated | Play module listing |
| 21 | Track/Tutorial field sets (`Q-15`) | NOT_RECOVERED | classes not recovered as source | targeted decompile by class name |
| 22 | All runtime behaviour (15 tests) | BLOCKED | no device/account/network/stock APK | see `15_RUNTIME/94` |

## Counts
- Open items in register: **37** (`16_INDEX_AND_EVIDENCE/100_OPEN_QUESTIONS.md`)
- Closed by this mission: **4** (`U-01`, `U-15`, `U-22`, `U-23`)
- BLOCKED (environment): **6** (rows 2, 7, 8, 17, 22, and native disassembly `Q-139`)
- Server-side by nature: **4** (rows 13, 16, plus completion recomputation and league promotion)
