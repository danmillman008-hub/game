# Phase 12.6 — Evidence requirements per status

| Status | Minimum evidence | Forbidden |
|---|---|---|
| `CLOSED_STATIC` | instruction dump or source lines **and** a mission-relative artefact path **and** a reproduction command | citing a class name alone; citing a mission-7 report as proof |
| `PARTIALLY_CLOSED` | as above, plus an explicit residual sentence | implying the rest is answered |
| `BACKEND_ONLY` | evidence that the client only serialises/deserialises | claiming server behaviour |
| `NOT_RECOVERED` | the reason (renamed / merged / absent / decompiler failure) | "probably" |
| `GENUINELY_UNKNOWN` | what would settle it | speculation in the answer column |
| `BLOCKED_BY_ENVIRONMENT` | the missing capability, named | claiming the answer is impossible in principle |
| `SUPERSEDED` | the artefact that refutes the premise | deleting the old question |
| `OUT_OF_SCOPE` | the rule (provenance, repackaging, credentials) | using it to avoid a hard question |

## Automated enforcement

`tools/build_closure_records.py` verifies:

* the status vocabulary (eight values, case-sensitive),
* `previous_status` equals the canonical register value,
* every evidence path exists on disk relative to `mimo-re/mission-08/`,
* `new_status`, `rationale` and `reproduction` are present.

A failing record aborts the build with a non-zero exit code, so a broken transition cannot be committed silently.
