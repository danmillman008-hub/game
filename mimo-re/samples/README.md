# samples/

Provenance material kept for reproducibility. **Do not redistribute.**

| File | What it is | Notes |
|---|---|---|
| `tracks.json` | real Mimo `tracks.json` (EN pack, publishSetVersion 753) | proprietary content — analysis provenance only |
| `tutorial-1001.interactive.json` | one real tutorial containing markup lessons | same caveat |
| `executable-lesson.sample.json` | extracted `executableContent` object | same caveat |
| `parser-fixture-45-1-1.html` | golden fixture shipped by Mimo at `assets/testdata/45-1-1.html` | their own parser test vector |

For **structural** samples that can be reused without copying proprietary content, use the
generated templates in `templates/` (placeholder text, real schema) and the formal grammar in
`../schemas/lesson-dsl.ebnf`.
