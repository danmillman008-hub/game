# Mission 7 — Locale Content Differences

## Observable differences
| Aspect | Observation | Evidence |
|---|---|---|
| corpus presence | English ships in the base APK; other locales ship as modules | asset census vs manifest |
| string coverage | UI copy exists for many languages (Turkish, German, Russian, Azerbaijani, Mongolian, Indonesian, Swahili, Latvian, Danish, Dutch…) | ARSC string pool |
| content structure | identical DSL across locales (parsers are locale-blind) | `te.*` |
| answer grading | locale-blind ASCII normaliser | `qm.i` |
| league copy | includes locale-specific grammars with 4 placeholders | string pool samples |

## What cannot be compared
No second APK version is available, so **no version-to-version content diff** is produced. Any claim about
content evolution would be fabrication.
