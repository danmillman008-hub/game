# Mission 6 — Locale and Publish-Set Analysis

## Scope
Which locales exist, how locale is represented, and how the publish set interacts with locale.

## Method
Enum enumeration (`ContentLocale`), manifest dynamic-module meta-data, asset tree census, resource
`values-*` directory census.

## Sources
`evidence/CONTENT_MODEL_FIELDS.json`, `/tmp/manifest.xml`, `/tmp/res/res/values-*`.

## Findings
1. **`ContentLocale` in the base DEX enumerates 5 locales**: `IT, PL, PT, RU, TR` (each with
   `languageString`). (VERIFIED_STATIC)
2. **Dynamic modules imply more locales**: the fused-module meta-data lists at least
   `content_de, content_es, content_fr, content_id, content_it` — i.e. content packs for German,
   Spanish, French, Indonesian, Italian (+ more, the meta-data value was truncated in the decoded XML).
   (VERIFIED_STATIC for the string; complete list `Q-14`)
3. **Therefore the enum is not a reliable locale inventory.** Two hypotheses remain: (a) the enum holds
   only *fallback*/legacy locales and the rest are module-driven; (b) the repackaged build lost
   constants. This mission does not choose between them.
4. **UI translations** exist as `values-*` resource directories (separate from content locale); a UI
   locale can therefore differ from the content locale.
5. `publishSetVersion` is a **single global number per pack**, not per locale (field exists once in
   `TracksJson`).

## Evidence labels
Point 1, 2, 4, 5: **VERIFIED_STATIC**. Point 3: **UNKNOWN** by design.

## Limitations
No per-locale content census was performed (the non-English packs are not in the APK's base assets).

## Open questions
`Q-14` complete locale set; `Q-24` whether a locale switch refetches progress; `Q-25` fallback order.

## Reproduction
```bash
grep -o 'content_[a-z][a-z]' /tmp/manifest.xml | sort -u
ls -d /tmp/res/res/values-* | sed 's/.*values-//' | sort -u | tr '\n' ' '
```
