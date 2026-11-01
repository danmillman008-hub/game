# 11 — Acceptance tests (what proves your build is Mimo-faithful)

Two layers: **(A) handoff integrity** — the package itself is consistent; **(B) engine conformance** — your `mimo/`
reproduces the recovered behaviour. Layer A ships here; layer B you implement against the vectors.

## A. Handoff integrity (`HANDOFF/tools/verify_handoff.py`, ships green)

| id | Assertion |
|---|---|
| `A-01` | every entry in `data/MANIFEST.json` exists and its sha256 matches the file |
| `A-02` | every `source_path` in the manifest resolves inside the repo |
| `A-03` | all JSON in `data/` parses; all `.ebnf`/`.csv` are non-empty |
| `A-04` | `spec_deltas.json`: 45 domain decisions, ids D-01…D-45, decision ∈ vocabulary, counts match `counts` |
| `A-05` | `spec_deltas.json`: 8 additions ADD-01…ADD-08 |
| `A-06` | `grading_vectors.json` / `progress_vectors.json` are internally consistent (every vector has input+expected) |
| `A-07` | every delta's `evidence_anchor` resolves to a real path in the repo |
| `A-08` | docs 00–15 referenced from `START_HERE.md` all exist |
| `A-09` | no file in `HANDOFF/` contains a secret-shaped string (token/key buckets) |
| `A-10` | tag counts in `dsl_tags.json` sum to the documented occurrence total |

## B. Engine conformance (you implement; vectors provided)

### B1 — parsing
| id | Input | Expected |
|---|---|---|
| `B1-01` | `<p>Hello</p>` | 1 `paragraph` block, text `Hello` |
| `B1-02` | `<selection><item value="1" correct="true">a</item>…` | selection with 1 correct item |
| `B1-03` | `<interaction type="fillTheGap"><options><option startIndex="0" endIndex="3"/>…` | gap with range (0,3) |
| `B1-04` | unknown `<video>` | policy outcome (ignore+warning / error) — deterministic and documented |
| `B1-05` | malformed unclosed `<p>` | typed `ParseError`, no crash |

### B2 — normalisation (exact)
| id | Input | Expected |
|---|---|---|
| `B2-01` | `"Hello, World!"` | `"hello,world"` |
| `B2-02` | `"a b\tc"` | `"abc"` |
| `B2-03` | `"f(x) {return 1;}"` | `"f(x){return1}"` |
| `B2-04` | `"print('x')"` | `"print(x)"` (quote dropped, parens kept) |
| `B2-05` | `"I"` under a Turkish default locale | must still lowercase to `i` (`Locale.US`) |

### B3 — verdicts
| id | Case | Expected |
|---|---|---|
| `B3-01` | ValidatedInput `"x = 1"` vs `"x = 1"` | CORRECT |
| `B3-02` | ValidatedInput `"x=1"` vs `"x = 1"` | PARTIAL |
| `B3-03` | ValidatedInput `"y=1"` vs `"x = 1"` | INCORRECT |
| `B3-04` | selection single, correct item chosen | CORRECT |
| `B3-05` | multi-select, 2 of 3 correct chosen | INCORRECT (all-or-nothing) |
| `B3-06` | fillTheGap, all gaps right | CORRECT |
| `B3-07` | spell, normalised-equal but raw-different | CORRECT (two-way, no PARTIAL) |

### B4 — feedback
| id | Verdict | Rendered `visible-if` sets |
|---|---|---|
| `B4-01` | CORRECT | `always` + `correct` |
| `B4-02` | PARTIAL | `always` only |
| `B4-03` | INCORRECT | `always` + `wrong` |

### B5 — progress
All vectors in `data/progress_vectors.json`: identity (2), creation (1), ordering guard (1), counter update (6),
completion flag (3), queue (4), retrieval (1), chapter answers (1), first try (1), version change (1), wire mapping (9
fields).

### B6 — persistence
| id | Assertion |
|---|---|
| `B6-01` | `lesson_progress` has exactly the 11 columns of `06` §2, in any order, with PK `(lesson_id, tutorial_id)` |
| `B6-02` | `tutorial_completions` / `chapter_completions` match `06` §2 |
| `B6-03` | pending query returns only `in_queue = 1` |
| `B6-04` | delete-posted-then-query leaves no posted rows |
| `B6-05` | migration from your v1 to v2 preserves rows (`ADD-06`) |

### B7 — completion (local rule, `ADD-04`)
| id | State | Expected |
|---|---|---|
| `B7-01` | 0 of 3 lessons solved | chapter incomplete |
| `B7-02` | 2 of 3 solved | incomplete |
| `B7-03` | 3 of 3 solved | complete |
| `B7-04` | all chapters complete | tutorial complete |
| `B7-05` | completed, then a migration/restart | still complete (persistence, not recompute-from-network) |

## How to run

```bash
python3 HANDOFF/tools/verify_handoff.py        # layer A
python3 -m pytest HANDOFF/tests -q             # vector reproduction reference
# inside your own project:
<your test runner> -k "B1 or B2 or B3 or B4 or B5 or B6 or B7"
```

Report **actual** counts. A skipped test is not a passing test; an existence-only test is not a test.
