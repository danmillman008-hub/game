# Phase 12.1 — How a question is allowed to change status

## 1. The eight statuses

| Status | Means | Requires |
|---|---|---|
| `CLOSED_STATIC` | the mechanism is reconstructed from code, with an evidence artefact and a reproduction command | instructions or source lines + artefact file |
| `PARTIALLY_CLOSED` | part of the question is answered, and the unanswered remainder is named | same, plus an explicit residual statement |
| `BACKEND_ONLY` | the answer cannot exist in the client; the server decides | evidence that the client only sends/receives |
| `NOT_RECOVERED` | the code is present but was not recovered (renamed/merged/absent) | a statement of *why* it is not recovered |
| `GENUINELY_UNKNOWN` | neither the code nor the backend can be inspected here | identification of what would settle it |
| `BLOCKED_BY_ENVIRONMENT` | answerable in principle, blocked by the sandbox (no runtime, no second decompiler) | the exact missing capability |
| `SUPERSEDED` | the question was premised on something false and no longer applies | the refuting evidence |
| `OUT_OF_SCOPE` | excluded by the mission's own rules (provenance, repackaging, credentials) | the rule that excludes it |

Vocabulary is enforced by `tools/build_closure_records.py`; an illegal value aborts the build.

## 2. Transition rules

A transition record is accepted only when it has **all** of:

1. `previous_status` — and it must equal the canonical register's current value (no silent overwrite),
2. `new_status` — one of the eight,
3. `evidence` — a list of mission-relative paths, every one of which must exist,
4. `reproduction` — a runnable command, not a description,
5. `rationale` — one paragraph that a critic could argue against,
6. optional `residual` — what remains unanswered *after* the transition.

The builder refuses the whole file if any record fails any check. Records are additive: the previous status is
never deleted, so the history of a question is a chain, not a value.

## 3. Why so few transitions so far

Only **Q-121** has moved. That is deliberate: Phases 3, 4, 6–11 (which would close the remaining questions) are
not started, and a status change without evidence is exactly the failure mode this mission exists to prevent.
`07_COVERAGE_OF_CLOSURE.md` states which questions have been *re-examined* (even when unchanged) and which have
not been looked at yet.

## 4. Relation to the Mission-7 register

Mission-7's closure register remains the historical record (`mission-07/18_CLOSURE/116_…csv`, unmodified).
Mission-8's `02_QUESTION_REGISTER.json` is the current state: 39 rows, one status each, plus the transition
records. Where the two disagree, this file wins **for the current state** and Mission-7 wins **for the history**.
