# ۰۸ — بومیسازی، RTL و دسترسپذیری

## ۱. زبانها (فهرست کامل ۱۱۶ زبان + پیشفرض)

`SOURCE/values/` شامل ۱۶۱ پیکربندی و ۲۹۴ فایل مقادیر است. زبانها:

`af, am, ar, as, az, be, bg, bn, bn-rBD, bs, ca, cs, da, de, el, en-rAU, en-rCA,
en-rGB, en-rIN, en-rXC, es, es-r419, es-rES, es-rGT, es-rUS, et, et-rEE, eu, eu-rES,
fa, fi, fr, fr-rCA, gl, gl-rES, gu, he, hi, hr, hu, hy, hy-rAM, id, in, is, is-rIS, it,
iw, ja, ka, ka-rGE, kk, kk-rKZ, km, km-rKH, kn, kn-rIN, ko, ky, ky-rKG, lo, lo-rLA, lt,
lv, mk, mk-rMK, ml, ml-rIN, mn, mn-rMN, mr, mr-rIN, ms, ms-rMY, my, my-rMM, nb, ne,
ne-rNP, nl, no, or, pa, pl, pt, pt-rBR, pt-rPT, ro, ru, ru-rRU, si, si-rLK, sk, sl, sq,
sr, sv, sw, ta, ta-rIN, te, te-rIN, th, tl, tr, uk, ur, ur-rPK, uz, uz-rUZ, vi, zh,
zh-rCN, zh-rHK, zh-rTW, zu`

- **۱٬۷۲۱ نام رشته / ۳۷٬۹۶۹ مقدار**؛ `SOURCE/values/values-fa/string.xml` ترجمهٔ فارسی است.
- **۱۰ بستهٔ محتوای درس**: `lessons-de/en/es/fr/id/it/pl/pt/ru/tr` = ۱۰٬۳۰۸ فایل JSON.
  یعنی ۱۱۶ زبان اعلان شده ولی فقط ۱۰ بستهٔ محتوا وجود دارد ⇒ بقیه دورهٔ انگلیسی میگیرند.
- ۱۵ نام `plurals` / ۲۲۱ ردیف (شامل `chapter_end_streak_multiple_title`).

## ۲. RTL

- پیکربندی `ldrtl` در جدول منابع وجود دارد؛ `res/layout-ldrtl-v17/` و
  `res/drawable-ldrtl-xhdpi-v17/` / `drawable-ldrtl-xxxhdpi-v17/` shipped شدهاند.
- ۸۰۹ لایهٔ پایه برای فارسی/عربی باید آینهدار شوند (start/end به جای left/right).
- **استثنای مهم:** کروم درس (ادیتور کد، کیبورد کد، کنسول، بلوک کد) نباید RTL شود،
  چون کد چپبهراست. این تفکیک در خود اپ دیده نشد و برای محصول فارسی کار جدید است.
- اعداد فارسی/عربی و نیمفاصله: هیچ توکن یا رشتهای در بسته برایشان وجود ندارد ⇒ `UNKNOWN`.

## ۳. دسترسپذیری (شواهد مستقیم رشتهها)

- `abc_action_bar_home_description = "Navigate home"`، `abc_action_bar_up_description`.
- `bottomsheet_*_content_description`, `m3_loading_indicator_content_description`.
- `contentDescription` در لایهها به صورت `@string/...`، و `importantForAccessibility`
  در جدول ویژگیها قابل جستجوست (`CATALOGS/LAYOUT_INDEX.json`).
- `android:hint`, `android:labelFor`, `android:minHeight=48dp` در ویجتهای استاندارد Material.
- فونت `font-display: swap` و `color-scheme: light dark` در WebView (سازگاری با تم سیستم).

## ۴. تم تاریک

۳۷۱ ردیف منبع در پیکربندی `night`، ۴۳۹ ردیف در `v31`،
`res/drawable-night-v8/` (۱۶۵ فایل)، `res/color-night-v8/` (۴ فایل)،
`res/raw-night-v8/` (۱۵ انیمیشن Rive) و دو CSS جداگانه برای ادیتور.
