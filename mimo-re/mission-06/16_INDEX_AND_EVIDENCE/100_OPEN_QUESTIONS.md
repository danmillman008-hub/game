# Mission 6 - Open Questions Register

`U-*` ids are inherited from mission-05 (not retro-edited there); `Q-*` are new in mission 6.

| ID | Question | Domain | Status |
|---|---|---|---|
| Q-05 | dynamic feature module contents (non-English packs) absent from the APK | content | NOT_RECOVERED |
| Q-08 | lesson reset effect on the persisted progress row | progress | UNKNOWN |
| Q-14 | complete content-locale inventory (enum has 5, modules imply more) | content | UNKNOWN |
| Q-15 | Track/Tutorial field sets | content | NOT_RECOVERED |
| Q-17 | serialised JSON names (@SerialName) for DTOs | network | NOT_RECOVERED |
| Q-19 | OkHttp disk cache presence | content | UNKNOWN |
| Q-27 | chapter ordering (index vs server order) | content | UNKNOWN |
| Q-30 | unknown-tag behaviour per parser | dsl | UNKNOWN |
| Q-31 | NUMBER tag purpose (declared, no parser accepts it) | dsl | UNKNOWN |
| Q-34 | which .riv animations bind to which lesson state | ui | NOT_RECOVERED |
| Q-39 | REST vs WebSocket selection for code execution | executable | UNKNOWN |
| Q-40 | WebSocket message schema | executable | NOT_RECOVERED |
| Q-42 | whether a SELECTION can have several correct items | grading | UNKNOWN |
| Q-44 | non-ASCII answer handling (filter drops non-[a-z0-9<.]) | grading | INFERRED |
| Q-49 | server-side chapter completion recomputation | progress | UNKNOWN |
| Q-50 | ETA formula | progress | UNKNOWN |
| Q-54 | per-row vs per-batch delete after push | sync | INFERRED |
| Q-57 | keys/hearts consumption path | gamification | UNKNOWN |
| Q-69 | 4xx handling for progress push (no dead-letter found) | sync | UNKNOWN |
| Q-70 | push trigger points | sync | UNKNOWN |
| Q-80 | login/credential exchange payload | auth | NOT_RECOVERED |
| Q-81 | token refresh/expiry handling | auth | NOT_RECOVERED |
| Q-88 | pagination shape (none seen) | network | UNKNOWN |
| Q-89 | Pusher channel usage | realtime | UNKNOWN |
| Q-92 | whether lesson/code context is inlined into tutor messages | ai | UNKNOWN |
| Q-102 | design token values (colours/dimens) - toolchain BLOCKED | design | BLOCKED |
| Q-103 | dark theme existence | design | NOT_RECOVERED |
| Q-115 | feature gating matrix for premium | business | INFERRED |
| Q-118 | remote-config flag consumers | config | UNKNOWN |
| Q-120 | certificate pinning / cleartext policy details | security | NOT_RECOVERED |
| Q-121 | token storage mechanism | security | NOT_RECOVERED |
| Q-134 | consent/opt-out surface | privacy | NOT_RECOVERED |
| Q-140 | webview module URL allowlist | security | UNKNOWN |
| Q-141 | Play Integrity presence | security | NOT_RECOVERED |
| U-18 | bin.ghost/libyrf.so triggers - repack-related, not Mimo behaviour | integrity | BLOCKED |
| U-20 | analytics event-name to emitter binding | analytics | NOT_RECOVERED |
| U-23 | PATCH vs PUT - resolved: both genuinely exist (4 PATCH, 2 PUT) | network | VERIFIED_STATIC |

Total: **37** items. Closed in mission 6: `U-22` (base URL), `U-01` (DSL grammar), `U-15` (AI tutor
transport/quota/persistence), `U-23` (verb split). Load-bearing and still open: `U-20`, `U-18`, `Q-08`,
`Q-57`, `Q-80`, `Q-102`.
