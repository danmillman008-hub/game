# 04 — Design system (measured)

Source: `evidence/design-tokens.json` (produced by `tools/design_tokens.py` from the resource
table), `res/font/*`, and the shipped dimens used by lesson chrome. Everything numeric below
is **VERIFIED STATIC**; the light/night attribution is **INFERRED** (see §4).

## 1. Colour tokens — 234 app-owned colour resources

1,198 colour resources ship in total; 234 are app-owned (the rest are library defaults:
`abc_*`, `m3_*`, `mtrl_*`, `revenuecatui_*`, …). 59 tokens have two values whose relative
luminance differs by more than 0.25 — i.e. a **light/night pair**.

Semantic families (names are the contract; hexes are examples of each family's light value):

| Family | Tokens | Example values |
|---|---|---|
| Surfaces | `background_primary`, `background_secondary`, `background_reversed`, `background_reversed_alpha_20`, `background_reversed_80p`, `card_enabled`, `card_disabled`, `card_pressed`, `card_outline` | `#F6F7FB` (app canvas), `#FFFFFF` (card), night `#252746` / `#3F4273` |
| Brand / primary action | `button_primary`, `button_primary_disabled`, `button_primary_highlight`, `button_primary_text` | `#7E4BDE` light, `#885BDE` night |
| Secondary action | `button_secondary`, `button_secondary_disabled`, `button_secondary_*` | tonal fills |
| Text | `text_primary`, `text_weak`, `text_disabled`, `text_on_primary` | `#252746` (a very dark indigo, not black) |
| Iconography | `icon_primary`, `icon_weak`, `icon_disabled` | — |
| Lines | `line_primary`, `line_weak` | — |
| Semantic | `error_default`, `error_on_error`, `error_state_1`, `error_state_2`, `accent_error`, `accent_success`, `background_info`, `background_info_emphasis`, `flashbar_info_inverse_*` | `#F05A6E` error, `#66BC5A` success, `#A4E59B` success (night) |
| Code | `code_background`, `code_background_dark`, `code_primary`, `code_weak`, `code_on_dark`, `code_highlight`, `code_highlight_2`, `code_blue`, `code_green`, `code_pink`, `code_purple`, `code_coral`, `code_brown`, `code_yellow`, `codeeditor_tab_color` | white / `#1D1F32` editor, 9 syntax hues |
| Keyboard | `codingkeyboard_background` | — |

Two design decisions worth copying:

1. **Text is indigo-black (`#252746`), never `#000`** — the whole surface set
   (`#F6F7FB`) and text share the same hue family, which is why the app reads "soft" rather
   than "high contrast". A Konkur app targeting long study sessions should adopt this.
2. **The code editor has its own token namespace** (`code_*`) with *nine* syntax hues plus a
   highlight pair, independent of the UI palette. Syntax colour is not derived from the theme.

## 2. Typography

Fonts shipped (`res/font/`, V):
`aeonik_pro_regular|medium|bold` (+ italics, + `<family>` XML wrappers),
`aeonik_fono_regular|medium|bold` (monospace-ish companion), `aeonik_mono.otf`,
`optimistic_vf.ttf` (variable, used for streak/celebration numerals), `robotomedium.ttf`
(fallback for WebView/emoji).

Observed text sizes (from app-owned dimens, V): **12, 14, 15, 16, 18, 20, 21, 24, 30, 32, 42 sp**.
The 42 sp entry is not body text — it is `daily_goal_progress_view_current_sparks_text_size_42sp`
(the big XP counter), with `32 sp` variants for its smaller breakpoints. Code editor text is
**15 sp** (`code_editor_text_size`), deliberately 1 sp above the 14 sp UI body so that code is
optically equal to prose.

Practical scale for reuse: caption 12, body 14, body-emphasis 16, title 20–24, display 32,
celebration 42.

## 3. Spacing and shape

Spacing values in use (V, counts): 16 (30 uses), 24 (26), 8 (24), 12 (22), 20 (12), 32 (10),
48 (10), 64 (9), 4 (9), 56 (6), 40 (6), 60 (4), 52 (4), 0 (9).
⇒ a **4 dp base grid** with 8/12/16 as the dominant rhythm and 24 for section separation.

Corner radii (V): 4, 8, 12, 16, 20, 36 dp, with **12 dp** the most frequent
(`bottom_sheet_corner_radius 12dp`). 36 dp appears on pill-shaped streak/goal elements.

Layout constants (V): `content_max_width 608dp` (tablet/desktop content column),
`bottom_sheet_content_max_width 496dp`, `coding_keyboard_height 64dp`,
`chapter_end_animation_width 200dp`.

## 4. Light/night theme and how confident we can be

The resource table stores one entry per configuration; the XML view used here lists them in
arsc order without config labels. The values themselves are exact. Pairing was inferred by
comparing relative luminance: e.g. `background_primary` = `#F6F7FB` then `#252746`, and
`card_enabled` = `#FFFFFF` then `#3F4273`. Both are consistent with a **light canvas / dark
navy night canvas** pair, and the app has an in-app appearance switch
(`settings_appearance_dark` / `settings_appearance_light`, V).

## 5. Motion

* `Rive` runtime (983 classes) drives streak/chapter-end animation;
  `chapter_end_animation_width 200dp` sizes it (V).
* Compose animations for the AI-tutor button pulse
  (`AiTutorButton$…$pulseDiameterAnimation`, `pulseOpacityAnimation`, V).
* `ArcProgressView` is a custom view drawing the streak arc (V class name + dimen family).

## 6. Iconography and illustration

`store_info_app_icons_*` (V) shows that app-icon variants are *sold* and shipped as separate
launcher aliases (`ChangeAppIconActivity`, `settings_app_icon_locked`). Illustration is
Rive-based for celebrations and static drawables otherwise; 809 layouts include the onboarding
illustration frames.

## 7. Accessibility and localisation constraints

* 116 locales declared, 1,721 app strings (V); 10 of those locales also have **content packs**
  (V). Any language needs both or the course stays English — a trap for a Persian build.
* Every state string is named with a `state_*` / `*_description` convention
  (`state_empty`, `activity_offline_description`) — good for RTL since descriptions are
  separate resource entries, not concatenated sentences.
* `m3_loading_indicator_content_description`, `bottomsheet_*_content_description` exist (V),
  so TalkBack handling is deliberate for sheets and loaders. For an RTL Persian product the
  layout mirroring burden is real: 809 XML layouts, of which the lesson chrome
  (editor + keyboard + console) must *not* mirror.

## 8. What a Konkur design system should take

1. The **hue-consistent neutral ramp** (indigo-black text on cool light canvas).
2. The **four-value spacing rhythm** (8/12/16/24) and **12 dp** card/sheet radius.
3. The **separate code/answer token namespace** — in Konkur: a namespace for
   formula/chemical/physics rendering (equations, units, RTL-mixed numerals).
4. The **state-string convention** (`state_*`, `*_offline_*`, `*_empty_*`) — it is what makes
   the 16-state-per-screen discipline in §2 possible.
5. **Do not** copy the celebration-heavy motion layer: for exam prep, the reward moment should
   be a progress delta, not a 200 dp animation; the 42 sp XP counter is the maximum visual
   weight worth keeping.
