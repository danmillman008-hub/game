# Mission 5 — Analytics Registry (revalidated)

## Scope
What the app can emit, through which SDKs, and — crucially — what the evidence *does not* support.
This document exists largely to correct inflated historical claims.

## Method
Read the analytics facade `com.getmimo.analytics.a` (fields + constructor), enumerated the
`com.getmimo.analytics.*` type tree, and scanned all 3,323 decompiled classes for snake_case string
literals (event/property candidates). Counted **classes**, not events, and kept the two apart.

## Sources
| Evidence | Symbol |
|---|---|
| Facade | `com.getmimo.analytics.a` (7 injected SDK handles) |
| Property types | `com.getmimo.analytics.properties.*` (305 classes) |
| Enum-ish event enums | `com.getmimo.analytics.Analytics$<Event>$<Property>` nested types |
| Literal census | `/tmp/snake.json` produced during this session (449 unique literals) |

## Findings — the fan-out (VERIFIED_STATIC)
`com.getmimo.analytics.a` holds, and fans every event out to:
| Field | Declared type | Identity |
|---|---|---|
| `g` | `com.google.firebase.analytics.FirebaseAnalytics` | **Firebase** — named explicitly |
| — | `com.adjust.sdk.Adjust` (`getAdid`, `getAttribution`) | **Adjust** — named explicitly |
| `b` | `np.h` | obfuscated handle — vendor **NOT established** |
| `c` | `be.d` | obfuscated handle — vendor **NOT established** |
| `e` | `be.y3` | obfuscated handle — vendor **NOT established** |
| `f` | `oy.t` | obfuscated handle — vendor **NOT established** |
| `d` | `com.getmimo.analytics.b` | in-app helper (remote-config wrapper) |

The constructor also registers an Adjust callback (`Adjust.getAdid(...)`) and an attribution listener.

## Findings — correcting the record
| Earlier claim | Status now | Evidence |
|---|---|---|
| "305 analytics events" | **wrong** — 305 is the number of classes in `com.getmimo.analytics.properties` (one class per event *shape*, not per event) | `ls /tmp/dad | grep -c 'analytics.properties'` |
| "Segment 137 events / Mixpanel 62 / Adjust 315 / Customer.io 351 / Facebook 117" | these are **class counts per vendor package**, not event counts; and vendor identity for the four obfuscated handles is unproven | same package census |
| "Firebase 5,718 classes" | that is the size of the bundled Firebase package, not analytics surface | package census |

## Findings — event-name candidates (INFERRED_MEDIUM)
Scanning all decompiled classes for lowercase snake_case literals yields **449 unique candidates**
across 342 classes; restricting to analytics/lesson/data packages leaves **232**. They mix
*event names*, *property keys* and *analytic constant names*; the code does not distinguish them
structurally (both are passed as `String`). Examples of unambiguous event literals read at call
sites this mission: `lesson_reset`, `lesson_interaction_delete`, `ask_ai_tutor`,
`paywall_plans`, `streak_repair_modal`, `track_overview`, `chapter_end`, `lesson_screen`.
Property keys read directly: `lesson_id, track_id, tutorial_id, lesson_type, tutorial_type,
attempts, duration, attempt`.

**No authoritative event list can be produced from static analysis alone**, because the event name is
a runtime `String` argument and the class that assembles the final `track(...)` call
(`Lcom/getmimo/analytics/Analytics;`) is **absent from the DEX under that name** — it is either
name-shrunk or inlined. Register `U-20`.

## Evidence labels
- Facade structure, Firebase/Adjust identity, package counts, literal census: **VERIFIED_STATIC**.
- Event semantics for the literals quoted at call sites: **VERIFIED_STATIC** (call-site context read).
- Any "registry of N events": **NOT_ESTABLISHED** → deliberately not published as a number.

## Limitations
Without the `Analytics` assembler class, the mapping literal → SDK call is incomplete. Runtime capture
(debug build with a proxy) would resolve it and is **BLOCKED** here.

## Unresolved
`U-20` authoritative event list; `U-21` identity of `np.h`, `be.d`, `be.y3`, `oy.t`.

## Reproduction
```bash
sed -n '1,45p' /tmp/dad/com.getmimo.analytics.a.java          # seven SDK handles + Adjust registration
ls /tmp/dad | grep -c 'analytics.properties'                   # 305 property classes
python3 - <<'P'                                                # 449 snake_case literal candidates
import glob,re,collections
pat=re.compile(r'"([a-z][a-z0-9]*(?:_[a-z0-9]+){1,5})"'); s=set()
for p in glob.glob('/tmp/dad/**/*.java',recursive=True):
    s|={m.group(1) for m in pat.finditer(open(p,errors='replace').read()) if 6<=len(m.group(1))<=48}
print(len(s))
P
```
