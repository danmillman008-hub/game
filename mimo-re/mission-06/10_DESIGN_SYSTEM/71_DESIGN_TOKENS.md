# Mission 6 — Design Tokens

## Scope
Colour, typography, editor theme and the exact limit of what is recoverable from binary resources with
the available toolchain.

## Method — four paths, three failed
1. `ARSCParser.get_color_resources()` — raises `TypeError` in androguard 4.1.4 (requires `package_name`).
2. `get_color_resources("com.getmimo")` — returns **raw bytes** (90,679 B type-chunk dump), not a mapping.
3. `ARSCParser.resource_configs` — exposes **1** entry; the id→config index is not built for this table.
4. ARSC **global string pool** (33,341 entries) — contains string *values* only (all UI translations);
   resource **names** live in the key pool, which androguard does not expose here.

Result: colour names and values, dimensions, radii and spacing are **NOT_RECOVERED / BLOCKED** at
toolchain level (`Q-102`). Nothing is guessed.

## Findings — typography (VERIFIED_STATIC)
15 font assets in `res/font`:

| family | files |
|---|---|
| Aeonik Pro | `aeonik_pro_regular{,_normal}.otf`, `aeonik_pro_medium{,_normal}.otf`, `aeonik_pro_bold{,_normal}.otf`, `*_italic.otf`, + 3 `font-family` XML descriptors |
| Aeonik Mono | `aeonik_mono.otf` (code editor / code blocks) |
| Aeonik Fono | `aeonik_fono_{regular,medium,bold}.otf` (display cut) |
| third-party | `optimistic_vf.ttf`, `robotomedium.ttf` |

The `.xml` entries are `font-family` descriptors, i.e. the app resolves families (weight/style mapping)
rather than referencing single files — typography is a small, well-structured scale with **three** cuts and
weight variants of one typeface.

## Findings — syntax highlighting is a separate colour system (VERIFIED_STATIC)
`ui.codeeditor.utils.HighlightJsTheme` + `ui.compose.components.internal.SpanCopier$FOREGROUND_COLOR`
show highlighting colours are declared per editor theme, not derived from UI colour resources. A
reconstruction must therefore keep two palettes.

## Findings — UI string localisation is broad (VERIFIED_STATIC)
The string pool holds UI text in many languages (Turkish, German, Russian, Azerbaijani, Mongolian,
Indonesian, Swahili, Latvian, Danish, Dutch, …) including league copy
("#%1d olarak, %2d kişilik %3s sıralamasını tamamladın ve %4s seviyesine yükseldin" = "you finished #x of y
in league z and moved up to w"). So **UI locale breadth ≫ `ContentLocale` enum breadth** (Phase 2.13).

## Evidence labels
Fonts, editor-theme separation, locale breadth: **VERIFIED_STATIC**. Colour/dimension values: **BLOCKED**.

## Open questions
`Q-102` token values (needs `aapt2 dump resources`); `Q-103` dark theme; `Q-104` spacing scale.

## Reproduction
```bash
python3 -c "import json;print(json.load(open('evidence/DESIGN_TOKENS_NAMES.json'))['fonts'])"
ls /tmp/res/res/font
```
