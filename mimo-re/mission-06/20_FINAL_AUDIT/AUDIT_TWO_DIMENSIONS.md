# Mission 6 — Final Audit (two dimensions, no averaged percentage)

## Dimension 1 — domain coverage
See `16_INDEX_AND_EVIDENCE/101_COVERAGE_MATRIX.md`, 38 domains with per-domain state and evidence link.
Summary of *classes*, not percentages:

| Class | Domains |
|---|---|
| Fully reconstructed | content hierarchy, DSL/parser, grading+normalisation, lesson runtime/state machine, progress outbox, network stack, AI tutor transport, gamification contract (8) |
| Substantially reconstructed | sync, localisation, subscription surface, design-system structure, executable lessons (5) |
| Partially reconstructed | navigation, screens, auth, remote config, analytics, security posture, business surface, deep links, realtime (9) |
| Identified, not understood | analytics emitters, keys consumption, Pusher role, Rive triggers (4) |
| Not investigated | accessibility, performance (2) |
| Blocked | runtime suite, native disassembly, design tokens (3) |
| Requires backend | completion aggregation, ETA, quota thresholds, league promotion, discount eligibility (5) |
| Out of scope | backend behaviour (RULE 3) (1) |

## Dimension 2 — evidence coverage
| Label | Count of substantive claims | Notes |
|---|---|---|
| `VERIFIED_STATIC` | dominant across 60+ documents | each carries a file/method citation and a reproduction command |
| `VERIFIED_RUNTIME` | **0** | no execution possible |
| `VERIFIED_EXPERIMENTAL` | **0** | no experiment ran |
| `INFERRED` | analytics names, trust consequences, some ordering/optionality | never presented as fact |
| `UNKNOWN` | 12 register entries | stated, not filled |
| `NOT_RECOVERED` | 11 register entries | searched and reported absent |
| `BLOCKED` | 6 register entries | environment-limited, with prerequisites listed |

## Discipline checks (enforced by tests)
1. No document asserts runtime verification (`test_no_document_claims_runtime_verification`).
2. Every evidence path cited by a document exists (`test_evidence_files_referenced_by_docs_exist`).
3. Grammar/tag/AST/DTO documents cannot drift from extracted JSON (5 dedicated tests).
4. Grading vectors are computed from the documented filter, so doc↔code disagreement fails the build.
5. Evidence DB labels are restricted to the 7-label set.

## What this audit deliberately does **not** contain
A single "completeness %". Coverage is bimodal (strong on execution paths, thin on visual/native/analytics)
and an average would misrepresent both halves.
