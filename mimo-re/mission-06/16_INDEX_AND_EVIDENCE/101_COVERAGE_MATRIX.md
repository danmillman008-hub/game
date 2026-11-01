# Mission 6 - Coverage Matrix (two dimensions, no averaged percentage)

## Dimension 1 - domain coverage (38 domains)
| # | Domain | Reconstruction state | Evidence |
|---|---|---|---|
| 1 | APK and packaging | VERIFIED_STATIC | `01` |
| 2 | Application startup | VERIFIED_STATIC | `01_APK_AND_ARCHITECTURE/03` |
| 3 | Architecture and DI | VERIFIED_STATIC | `01_APK_AND_ARCHITECTURE/04` |
| 4 | Content system | VERIFIED_STATIC | `02` |
| 5 | DSL and parser | VERIFIED_STATIC | `03` |
| 6 | Lesson runtime | VERIFIED_STATIC | `03` |
| 7 | Interactions | VERIFIED_STATIC | `04` |
| 8 | Grading | VERIFIED_STATIC | `04` |
| 9 | Feedback | VERIFIED_STATIC | `04` |
| 10 | Learner model | VERIFIED_STATIC | `05` |
| 11 | Progress | VERIFIED_STATIC | `05` |
| 12 | Gamification | VERIFIED_STATIC (display) | `05` |
| 13 | Persistence | VERIFIED_STATIC | `06` |
| 14 | Sync | VERIFIED_STATIC (payload) | `06` |
| 15 | Offline | VERIFIED_STATIC | `06` |
| 16 | Networking | VERIFIED_STATIC | `07` |
| 17 | DTOs | VERIFIED_STATIC (39/50) | `evidence/DTO_FIELDS.json` |
| 18 | Realtime | PARTIAL | `07_NETWORK/54` |
| 19 | AI tutor | VERIFIED_STATIC | `08` |
| 20 | Navigation | PARTIAL | `09` |
| 21 | Screens | PARTIAL | `09` |
| 22 | Design system | PARTIAL (tokens BLOCKED) | `10` |
| 23 | Auth | PARTIAL (exchange NOT_RECOVERED) | `11` |
| 24 | Subscription | VERIFIED_STATIC (client surface) | `11` |
| 25 | Remote config | PARTIAL | `11` |
| 26 | Analytics | INFERRED only | `12` |
| 27 | Native libs | INVENTORY ONLY | `13` |
| 28 | SDKs | VERIFIED_STATIC (presence) | `13` |
| 29 | Security posture | PARTIAL | `14` |
| 30 | Integrity | VERIFIED_STATIC (of this artifact) | `14` |
| 31 | Executable lessons | VERIFIED_STATIC payload; socket schema NOT_RECOVERED | `03_DSL_AND_RUNTIME/23` |
| 32 | Deep links | PARTIAL | `09_NAVIGATION_AND_UI/65` |
| 33 | Localisation | PARTIAL | `09_NAVIGATION_AND_UI/67` |
| 34 | Accessibility | NOT INVESTIGATED | `09_NAVIGATION_AND_UI/67` |
| 35 | Business logic | VERIFIED_STATIC (surface) | `11` |
| 36 | Runtime behaviour | BLOCKED | `15` |
| 37 | Performance | NOT INVESTIGATED | `-` |
| 38 | Backend behaviour | OUT OF SCOPE (RULE 3) | `-` |

## Dimension 2 - evidence-label distribution
| Label | Meaning | Dominant domains |
|---|---|---|
| `VERIFIED_STATIC` | readable in code/data, reproducible | content, DSL, grading, progress, network, AI, gamification |
| `VERIFIED_RUNTIME` | **0 claims** - no execution possible | - |
| `VERIFIED_EXPERIMENTAL` | **0 claims** | - |
| `INFERRED` | code-derived consequence, not observed | analytics names, trust consequences, some ordering |
| `UNKNOWN` | searched, not determined | push triggers, reset semantics, keys, socket schema |
| `NOT_RECOVERED` | absent from recovered material | login exchange, prompt text, token storage |
| `BLOCKED` | obtainable in principle, impossible here | runtime suite, token values, native disassembly |

## Reconstruction classes
- **Fully reconstructed**: DSL/parser, grading+normalisation, lesson state machine, progress outbox, content
  hierarchy, network stack, AI tutor transport, gamification contract.
- **Substantially reconstructed**: sync, localisation, subscription surface, design-system structure.
- **Partially reconstructed**: navigation, screens, auth, remote config, analytics, security.
- **Identified-not-understood**: analytics emitter binding (`U-20`), keys consumption (`Q-57`), Pusher role.
- **Not investigated**: accessibility, performance.
- **Requires runtime**: all 15 rows of `15_RUNTIME/96_TEST_TO_SOURCE_MATRIX.csv`.
- **Requires backend**: completion aggregation, ETA, quota thresholds, league promotion, discount eligibility.
