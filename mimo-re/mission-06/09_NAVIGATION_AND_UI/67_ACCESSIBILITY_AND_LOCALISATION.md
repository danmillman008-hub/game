# Mission 6 — Accessibility and Localisation

## Scope
What the app does for a11y and how UI language is resolved.

## Method
Resource census (33,341 strings, many languages), `values-*` presence, content-description usage in
decompiled UI classes, locale handling in code.

## Findings (VERIFIED_STATIC)
1. **Localisation is broad for UI**: the global string pool contains the same copy in many languages
   (Turkish, German, Russian, Azerbaijani, Mongolian, Indonesian, Swahili, Latvian, Danish, Dutch, …).
   UI locale is therefore richer than `ContentLocale` (5 values, Phase 2.13).
2. **Content locale and UI locale are separate axes**; no code was found that forces them equal.
3. **Accessibility**: `contentDescription` usage appears in Compose/View code, but no systematic
   a11y configuration (talkback labels inventory, minimum touch targets) was recoverable from binary
   resources; `Q-111`.
4. Lesson-specific a11y risk: gap/selection interactions are text-span based; the interaction is not an
   input field except for validated input (which uses `PartiallyEditableEditText`). Screen-reader behaviour
   of span-based gaps is **UNKNOWN** and untested (`R-A11Y-01` in Phase 15).

## Evidence labels
1–2 **VERIFIED_STATIC**; 3–4 **NOT_RECOVERED / UNKNOWN**.

## Open questions
`Q-111` a11y config; `Q-112` RTL handling of gap spans.

## Reproduction
`python3 -c "import json;print(len(json.load(open('/tmp/arsc_strings.json'))))"`
