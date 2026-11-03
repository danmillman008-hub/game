# Mission 7 — Design System (complete — **Q-102 closed**)

## Method (the fix)
Mission 6 failed because androguard's ARSC API returns raw bytes for this table. Mission 7 wrote
`tools/parse_arsc.py`: a direct parser of `ResTable_*` chunks (string pools, packages, type specs, **sparse and
offset16 type chunks**). Result: **1198 colour keys and 1401 dimension keys with values**.

## Token inventory (VERIFIED_STATIC, sample)
### Colours
| token | value | config |
|---|---|---|
| `$avd_hide_password__0` | `res/color/abc_background_cache_hint_selector_material_dark.xml` | default |
| `$avd_hide_password__1` | `res/color/abc_background_cache_hint_selector_material_light.xml` | default |
| `$avd_hide_password__2` | `res/color-v23/abc_btn_colored_borderless_text_material.xml` | default |
| `$avd_show_password__0` | `res/color-v23/abc_btn_colored_text_material.xml` | default |
| `$avd_show_password__1` | `res/color-v23/abc_color_highlight_material.xml` | default |
| `$avd_show_password__2` | `#ff000000` | default |
| `$glance_switch_thumb_off_to_on__0` | `#ffffffff` | default |
| `$glance_switch_thumb_on_to_off__0` | `res/color/abc_hint_foreground_material_dark.xml` | default |
| `$ic_ai_tutor_intro__0` | `res/color/abc_hint_foreground_material_light.xml` | default |
| `$ic_ai_tutor_intro__1` | `res/color/abc_primary_text_disable_only_material_dark.xml` | default |
| `$ic_ai_tutor_intro__10` | `res/color/abc_primary_text_disable_only_material_light.xml` | default |
| `$ic_ai_tutor_intro__11` | `res/color/abc_primary_text_material_dark.xml` | default |
| `$ic_ai_tutor_intro__12` | `res/color/abc_primary_text_material_light.xml` | default |
| `$ic_ai_tutor_intro__13` | `res/color/abc_search_url_text.xml` | default |
| `$ic_ai_tutor_intro__2` | `#ff7fa87f` | default |
| `$ic_ai_tutor_intro__3` | `17170444` | default |
| `$ic_ai_tutor_intro__4` | `17170444` | default |
| `$ic_ai_tutor_intro__5` | `res/color/abc_secondary_text_material_dark.xml` | default |

### Dimensions
| token | value | config |
|---|---|---|
| `$avd_hide_password__0` | `0.4097dp` | default |
| `$avd_hide_password__1` | `1.8433dp` | default |
| `$avd_hide_password__2` | `1.4337dp` | default |
| `$avd_show_password__0` | `0.0001dp` | default |
| `$avd_show_password__1` | `0.0001dp` | default |
| `$avd_show_password__2` | `0.1025dp` | default |
| `$glance_switch_thumb_off_to_on__0` | `0.4097dp` | default |
| `$glance_switch_thumb_on_to_off__0` | `0.2561dp` | default |
| `$ic_ai_tutor_intro__0` | `0.1537dp` | default |
| `$ic_ai_tutor_intro__1` | `1.2289dp` | default |
| `$ic_ai_tutor_intro__10` | `4.6081dp` | default |
| `$ic_ai_tutor_intro__11` | `0.1281dp` | default |
| `$ic_ai_tutor_intro__12` | `429496.6529dp` | default |
| `$ic_ai_tutor_intro__13` | `1.2289dp` | default |
| `$ic_ai_tutor_intro__2` | `1.2289dp` | default |
| `$ic_ai_tutor_intro__3` | `0.9217dp` | default |
| `$ic_ai_tutor_intro__4` | `1.2289dp` | default |
| `$ic_ai_tutor_intro__5` | `1.2289dp` | default |

## Typography
Aeonik Pro (regular/medium/bold, italic variants + `font-family` XML), Aeonik Mono (code), Aeonik Fono (display),
plus `optimistic_vf.ttf` and `robotomedium.ttf`.

## Structure
Tokens are named resources (semantic + palette layers coexist); both type tables carry multiple configuration
variants (locale/night/dpi/version), which is exactly why a single-value read was misleading in Mission 6.

## What remains open
Which token each screen uses (a layout→token map would need 1,531 layouts decoded — see `81_ACCESSIBILITY_IMPLEMENTATION.md`).
