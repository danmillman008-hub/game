# Mission 7 — Closed Findings

## Distribution (37 inherited items)
| Status | Count |
|---|---|
| `BACKEND_ONLY` | 2 |
| `BLOCKED_BY_ENVIRONMENT` | 2 |
| `CLOSED_STATIC` | 12 |
| `GENUINELY_UNKNOWN` | 3 |
| `NOT_RECOVERED` | 7 |
| `PARTIALLY_CLOSED` | 11 |

## Closed outright in Mission 7 (with answer)
| ID | Answer | Evidence |
|---|---|---|
| `U-01` | grammar of all 7 parsers incl. attributes and nesting, corpus-verified | 04/21 |
| `U-15` | typed SystemMessage/UserMessage context, SSE transport, quota DTO, no local store | 09/66 |
| `U-22` | base URL from DI case 22; prod/test hosts; consumers | 02/09 |
| `U-23` | PATCH×4 and PUT×2 both real | 08/59 |
| `Q-19` | no OkHttp disk cache | 08/58 |
| `Q-31` | `NUMBER` is dead vocabulary | 04/28 |
| `Q-42` | selections are single-answer (no `multiple` attribute) | 04/28 |
| `Q-44` | normaliser is ASCII-only, locale-blind | 06/39 |
| `Q-81` | no refresh/Authenticator/401 branch | 08/62 |
| `Q-88` | no pagination in any response DTO | 08/59 |
| `Q-92` | tutor context is typed messages, no lesson ids in DTO | 09/67 |
| `Q-102` | design token values recovered (1,198 colours, 1,401 dimens) | 12/77 |
| `Q-103` | theme variants exist at resource level; no runtime switch | 12/78 |
| `Q-120` | no certificate pinning | 08/58 |
| `Q-141` | no Play Integrity | 11/96 |

## Notable partial closures (real progress, honest limits)
| ID | What was established | What remains |
|---|---|---|
| `U-20` | dispatcher `com.getmimo.analytics.a.e(String,Map)`; 14 events with call sites; typed properties | names/emitters inside the 89% undecompiled classes |
| `Q-57` | `DefaultKeysRepository.consumeUserKey` exists | which UI action calls it |
| `Q-08` | `a0()` body: clears state + emits `lesson_reset` (7 properties) | effect on the persisted row |
| `Q-70` | no WorkManager worker ⇒ foreground-only push | exact trigger |
| `Q-89` | Pusher client and auth path | channels/events |
| `Q-118` | AB-test groups fetched at analytics init | consumers |
