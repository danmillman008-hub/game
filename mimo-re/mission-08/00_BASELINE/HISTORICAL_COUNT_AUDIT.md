# Mission 8 — Historical Count Audit

**Generated:** 2026-11-01 from the registers themselves, not from the Mission-7 prose.  
**Rule:** every number below is recomputed; nothing is copied out of a Mission-7 report.

## 1. Open questions

| Metric | Mission-7 report claim | Recomputed | Verdict |
|---|---|---|---|
| total closure rows | 41 (`17+12+4+3+3+2`) | **39** | claim wrong: rows were never 41 |
| CLOSED_STATIC | 17 | **14** | mismatch |
| PARTIALLY_CLOSED | 12 | **11** | mismatch |
| BACKEND_ONLY | 4 | **2** | mismatch |
| NOT_RECOVERED | 3 | **7** | mismatch |
| GENUINELY_UNKNOWN | 3 | **3** | matches |
| BLOCKED_BY_ENVIRONMENT | 2 | **2** | matches |

Recomputed distribution (all eight canonical statuses):

| Status | Count |
|---|---|
| CLOSED_STATIC | 14 |
| PARTIALLY_CLOSED | 11 |
| BACKEND_ONLY | 2 |
| NOT_RECOVERED | 7 |
| GENUINELY_UNKNOWN | 3 |
| BLOCKED_BY_ENVIRONMENT | 2 |
| SUPERSEDED | 0 |
| OUT_OF_SCOPE | 0 |

Sum: **39** (claimed 41 → arithmetic in the Mission-7 report does not close).

### Register-upgrade artefact

The Mission-6 master register holds 37 questions; the Mission-7 closure register holds 39. The delta is explained, not lost:
IDs present in closure but absent from the Mission-6 register: `U-01`, `U-22`.
IDs present in the Mission-6 register but missing from closure: `none`.

## 2. Evidence references

Mission-7 stored evidence as extension-less directory stems (`03_CONTENT_AND_MODULES/16`), so a naive `Path.exists()` fails for all 39 rows. Resolved by stem matching here: **39/39 resolved**, 0 unresolved.

## 3. Domains

Mission-7's audit contains **40** domain rows; the Mission-7 summary text said 41.

| Claimed classification (Mission 7) | Rows |
|---|---|
| FULLY RECONSTRUCTED | 24 |
| PARTIALLY RECONSTRUCTED | 7 |
| SUBSTANTIALLY RECONSTRUCTED | 9 |

Mission 8 requires 45 domains: **40 inherited + 5 newly separated** = **45**.

| Mission-8 classification | Domains |
|---|---|
| FULLY RECONSTRUCTED | 24 |
| NOT_INVESTIGATED | 5 |
| PARTIALLY RECONSTRUCTED | 7 |
| SUBSTANTIALLY RECONSTRUCTED | 9 |

## 4. Runtime column defect (correction)

The Mission-7 audit table has a `Runtime` column whose values are `complete`/`substantial`/`partial` for many domains, while every Mission-7 artifact states **0 runtime-verified findings**. Two different meanings were conflated: the column actually records *how much of the runtime logic was reconstructed from static evidence*. Mission 8 keeps them apart in `CANONICAL_DOMAIN_REGISTER.json`:

* `static_claim_m7` — what Mission 7 actually did (kept verbatim, provenance preserved),
* `runtime_executed` — always `NONE` until an authorised execution produces evidence.

No domain in this register claims runtime execution.

## 5. Decompiled-source gap

| Metric | Value |
|---|---|
| deep-investigation queue rows | 2178 |
| rows flagged `decompiled=1` in Mission 7 | 1119 |
| rows whose `.java` is actually present in `/tmp/dad` | 1119 |
| **rows with no decompiled body (DEX-only)** | **1059** |

Mission 7's flag is correct (it counts what the decompiler produced), but the consequence was never stated: **48.6% of the queue is DEX-only**, so any 'deep investigation' of those classes must read Dalvik instructions, not Java. Mission 8 adds `tools/dex_inspect.py` for exactly that.

## 6. Prose defect

The Mission-7 final response listed `Q-27` twice. The CSV contains `Q-27` exactly once, so this is a *reporting* defect, not a register defect; recorded here rather than editing Mission 7.

## 7. What is deliberately not repaired

Mission 7's files stay byte-identical (`WORKSPACE_INTEGRITY.json` pins their hashes). Every correction lives in mission-08 so the historical record remains falsifiable.

