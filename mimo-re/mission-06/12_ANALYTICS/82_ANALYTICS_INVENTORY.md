# Mission 6 — Analytics Inventory

## Scope
Which analytics providers are embedded and what the client can emit — refining mission-05 U-20.

## Method
SDK class presence, `com.getmimo.analytics.*` package, `tools/extract_event_candidates.py` (459 unique
snake_case literals, 252 with analytics context), property classes.

## Findings (VERIFIED_STATIC)
1. **`com.getmimo.analytics`** is a first-party facade over a provider SDK; property classes such as
   `analytics.properties.AiTutorInteractionSource` are typed enums passed as event properties.
2. Provider SDKs present in the DEX: Firebase Analytics (bundled with Firebase), Adjust (`libsigner.so` is
   the Adjust signer), Sentry (crash/error). Attribution therefore spans **Adjust** (install/campaign) and
   Firebase (product events).
3. 252 analytics-context event-name candidates were extracted; they are **INFERRED** identifiers because
   DAD renders constant names, and a literal may be an event name, a property key or a screen name
   (`83_EVENT_TAXONOMY.md`).
4. Named emitters recovered but not resolved: `np.h`, `be.d`, `oy.t` — the wrapper methods remain
   `NOT_RECOVERED` (mission-05 U-20 status unchanged in substance).

## Evidence labels
Provider presence **VERIFIED_STATIC**; event names **INFERRED**; wrappers **NOT_RECOVERED**.

## Open questions
`U-20` (carried) — event-name → emitter binding; `Q-131` whether events are dual-sent to Adjust.

## Reproduction
`/tmp/venv/bin/python tools/extract_event_candidates.py --out evidence/EVENT_CANDIDATES.csv`
