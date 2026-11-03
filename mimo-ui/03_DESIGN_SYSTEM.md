# ۰۳ — سیستم طراحی (همهٔ توکنها، بدون نمونه)

منبع: `resources.arsc` → `CATALOGS/RESOURCE_INDEX.csv` (۵۰٬۴۷۷ ردیف)،
`CATALOGS/DESIGN_TOKENS.json`، `SOURCE/values/values*/*.xml` (۲۹۴ فایل)،
`ATLAS/tokens.css` (همهٔ متغیرهای CSS)، `ATLAS/index.html` (نمایش رنگها).

## ۱. شمارش کامل

| نوع منبع | نام یکتا | مقدار/ردیف |
|---|---|---|
| color | ۱٬۱۹۸ | ۱٬۴۵۵ |
| dimen | ۱٬۴۰۱ | ۱٬۶۳۱ |
| string | ۱٬۷۲۱ | ۳۷٬۹۶۹ |
| style | ۱٬۷۲۸ | ۱٬۸۷۵ |
| attr | ۱٬۷۰۷ | — |
| id | ۲٬۲۳۳ | — |
| drawable | ۱٬۲۵۳ | — |
| layout | ۱٬۶۹۹ | — |
| plurals | ۱۵ نام | ۲۲۱ ردیف |
| array | ۸ | — |
| bool / integer | ۱۵ / ۷۸ | — |
| menu / navigation | ۵ / ۱ | — |
| پیکربندی / زبان | ۱۶۱ / ۱۱۶ | ۵۰٬۴۷۷ ردیف |

> تفاوت با گزارش دور قبل: عدد ۲۳۴ رنگ / ۳۰۰ دایمن «توکنهای اپ» بود؛اینجا  ۱٬۱۹۸ / ۱٬۴۰۱
> **همهٔ نامها** شامل کتابخانههای AndroidX/Material است. هر دو درستاند، دامنه فرق میکند.
> `14_CROSS_CHECK_PRIOR_WORK.md` این را موشکافی کرده.

## ۲. پالت اصلی (مقادیر واقعی، روشن / شب)

| توکن | روشن (default) | شب (night) |
|---|---|---|
| background_primary | #FFF6F7FB | #FF252746 |
| background_secondary | #FFFFFFFF | #FF333661 |
| background_reversed | #FF333661 | #FFFFFFFF |
| card_enabled | #FFFFFFFF | #FF3F4273 |
| card_pressed | #FFF6F7FB | #FF333661 |
| card_disabled | #FFE4E6F1 | #FF1D1F32 |
| text_primary | #FF252746 | #FFFFFFFF |
| button_primary | #FF7E4BDE | #FF885BDE |
| button_primary_highlight | #FF6E3EC8 | #FF7E4BDE |
| button_primary_disabled | #337E4BDE | #4D885BDE |
| accent_success | #FF66BC5A | #FFA4E59B |
| error_default | #FFF05A6E | #FFF97F8D |
| code_background | #FFFFFFFF | #FF1D1F32 |
| code_background_dark | #FF2F314F | #FFF5F9FE |
| code_blue | #FF226EC9 | #FF86BDFE |
| code_green | #FF337A29 | #FF97E58D |
| code_purple | #FF6E3EC8 | #FFB99AF4 |
| code_coral | #FFCF4053 | #FFF97F8D |
| code_background_dark | #FF2F314F | #FFF5F9FE |

خانوادههای معنایی (همه در `DESIGN_TOKENS.json`): `background_*`، `card_*`، `button_*`،
`text_*`، `accent_*`، `code_*` (۹ رنگ نحو)، `codingkeyboard_*`، `codeeditor_*`،
`leaderboard_*`، `iap_*`، `streak_*`، `flashbar_*`، `modal_*`، `onboarding_*`، `widget_*`.
قاعدهٔ مهم: متن و بوم همخانوادهاند (`#252746` روی `#F6F7FB`) و ادیتور namespace مستقل دارد.

## ۳. مقیاس فاصلهگذاری (کشف کامل، شامل نسخهٔ تبلت)

| توکن | گوشی (default) | تبلت (sw600dp) |
|---|---|---|
| spacing_xxs | 4.000000dip | — |
| spacing_xs | 8.000000dip | — |
| spacing_s | 12.000000dip | — |
| spacing_m | 16.000000dip | — |
| spacing_l | 24.000000dip | — |
| spacing_xl | 32.000000dip | — |
| spacing_xxl | 40.000000dip | — |
| spacing_xxs_expandable | 4.000000dip | 6.000000dip |
| spacing_xs_expandable | 8.000000dip | 12.000000dip |
| spacing_s_expandable | 12.000000dip | 16.000000dip |
| spacing_m_expandable | 16.000000dip | 24.000000dip |
| spacing_l_expandable | 24.000000dip | 36.000000dip |
| spacing_xl_expandable | 32.000000dip | 48.000000dip |
| spacing_xxl_expandable | 40.000000dip | 60.000000dip |

پیشتر فقط ردیف `sw600dp` به عنوان «مقیاس رسمی» گزارش شده بود (۶/۱۲/۱۶/۲۴/۳۶/۴۸/۶۰)؛
در واقع **دو مقیاس** وجود دارد: مقیاس پایه برای گوشی و `*_expandable` برای `sw600dp`.
هر دو به طور کامل در جدول بالا/فایل JSON هستند.

## ۴. ابعاد کلیدی (همهٔ مقادیر، نه چندتا)

| توکن | default | sw600dp / سایر |
|---|---|---|
| content_max_width | 608.000000dip | — |
| bottom_sheet_content_max_width | 496.000000dip | — |
| modal_default_width | 296.000000dip | sw600dp:360.000000dip |
| lesson_progressbar_height | 6.000000dip | sw600dp:8.000000dip |
| coding_keyboard_height | 64.000000dip | — |
| streak_calendar_height | 264.000000dip | sw600dp:324.000000dip |
| chapter_end_animation_width | 200.000000dip | sw600dp:260.000000dip |
| leaderboard_league_header_height | 100.000000dip | sw600dp:144.000000dip |
| streak_calendar_day_size | 36.000000dip | sw600dp:44.000000dip |
| bottom_sheet_corner_radius | 12.000000dip | — |
| lesson_codeblock_corner_radius | 4.000000dip | sw600dp:6.000000dip |
| code_editor_text_size | 15.000000sp | sw600dp:18.000000sp |

شعاعها: ۴، ۶، ۸، ۱۲، ۱۶، ۲۰، ۳۶ dp (`bottom_sheet_corner_radius = 12dp`،
`lesson_codeblock_corner_radius = 6dp`). اندازههای متن: ۱۲، ۱۴، ۱۵، ۱۶، ۱۸، ۲۰، ۲۱،
۲۴، ۳۰، ۳۲، ۴۲ sp. عرض محتوا: `content_max_width = 608dp`،
`bottom_sheet_content_max_width = 496dp`.

## ۵. تم، استایل و حالتها

- ۱٬۷۲۸ نام استایل، ۱٬۷۰۷ ویژگی (`attr`)، ۲٬۲۳۳ شناسه (`id`)، ۸ آرایه، ۱۵ bool، ۸۴ integer.
- تم پایه `@style/MaterialDarkModeTheme`؛ ۳۷۱ ردیف منبع در پیکربندی `night`،
  ۴۳۹ ردیف در `v31`، و ۱۶۱ پیکربندی کلی (شامل `ldrtl`, `land`, `sw600dp`, `h720dp`, `xhdpi`…).
- ۳۰۴ فایل `res/color*/` سلکتور حالت (enabled/pressed/disabled/checked) هستند؛
  نمونهٔ واقعی `button_primary_disabled = #337E4BDE` (همان رنگ با آلفای ۲۰٪).

## ۶. تایپ و فونت

فونتهای shipped: Aeonik Pro / Fono / Mono، `optimistic_vf`، Roboto، و `Aeonik Mono`
در باندل ادیتور. `@font-face` دقیقاً در `lesson-webview-fonts.js` با وزنهای ۴۰۰/۵۰۰/۷۰۰ و
normal/italic ساخته میشود (`font-display: swap`).

## ۷. حرکت

۷۲ `anim` + ۴۷ `animator` + ۲۴ `interpolator` + 59 انیمیشن Rive.
شاهد Compose: پالس قطر/شفافیت دکمهٔ مربی هوشمند، `ArcProgressView` (کمان زنجیره)،
`DailySparksGoalProgressView` (متن ۴۲sp). جزئیات در `09_STATE_AND_MOTION.md`.
