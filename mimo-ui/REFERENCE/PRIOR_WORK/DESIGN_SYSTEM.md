# ۰۳د — سیستم طراحی (توکن‌های اندازه‌گیری‌شده + نگاشت به صفحه)

پایه: `../evidence/design-tokens.json` (۲۳۴ رنگ برنامه، ۳۰۰ دایمن برنامه، ۵۹ جفت روشن/تیره).
همهٔ مقادیر hex/عدد **VERIFIED_STATIC**؛ نگاشت «روشن/شب» **INFERRED** (بر پایهٔ اختلاف روشنایی).

## ۱. رنگ — خانواده‌های معنایی و نمونه‌ها

| خانواده | نمونهٔ مقادیر | کاربرد (از نام) |
|---|---|---|
| سطح | `background_primary #F6F7FB`, `background_secondary #FFFFFF`, `card_enabled #FFFFFF`, `card_pressed #F6F7FB`, `card_disabled #E4E6F1` | بوم، کارت، حالت‌ها |
| شب | `background_primary #252746`, `card_enabled #3F4273`, `background_reversed #333661` | تم تاریک |
| اکشن اصلی | `button_primary #7E4BDE`, `_highlight #6E3EC8`, `_disabled #337E4BDE`, `_text #FFFFFF` | دکمهٔ اصلی |
| متن | `text_primary #252746`, `code_primary #252746` | متن (نه سیاه مطلق) |
| معنایی | `error_default #F05A6E`, `accent_success #66BC5A` / `#A4E59B` (شب) | خطا/موفقیت |
| کد | `code_background #FFFFFF`, `code_background_dark #2F314F`, `code_highlight #EDEEF6`, `code_blue #226EC9`, `code_green #337A29`, `code_purple #6E3EC8`, `code_coral #CF4053`, `code_pink #BB6E8D`, `code_yellow #B88E02`, `code_brown #844A30` | ۹ رنگ نحو + پس‌زمینهٔ ادیتور |
| کیبورد | `codingkeyboard_background #F6F7FB` | کیبورد کد |
| تب ادیتور | `codeeditor_tab_color` | تب فایل |

**قاعدهٔ مهم:** متن و بوم هم‌خانواده‌اند (`#252746` روی `#F6F7FB`)، و ادیتور namespace مستقل
دارد. برای محصول فارسی، یک namespace تازه برای «فرمول/شکل» لازم است.

## ۲. تایپوگرافی و فاصله

| دسته | مقادیر | نمونهٔ کاربرد |
|---|---|---|
| متن | ۱۲، ۱۴، ۱۵، ۱۶، ۱۸، ۲۰، ۲۱، ۲۴، ۳۰، ۳۲، ۴۲ sp | ۱۵sp = ادیتور کد (`code_editor_text_size`)، ۴۲sp = شمارندهٔ XP |
| فاصله | ۴، ۸، ۱۲، ۱۶، ۲۰، ۲۴، ۳۲، ۴۰، ۴۸، ۵۶، ۶۰، ۶۴ dp | ریتم ۸/۱۲/۱۶ + ۲۴ برای بخش‌ها |
| مقیاس expandable | `spacing_xxs/xs/s/m/l/xl/xxl` = ۶/۱۲/۱۶/۲۴/۳۶/۴۸/۶۰ dp | مقیاس رسمی |
| شعاع | ۴، ۶، ۸، ۱۲، ۱۶، ۲۰، ۳۶ dp | ۱۲ رایج‌ترین؛ ۶ برای بلوک کد (`lesson_codeblock_corner_radius 6dip`) |
| عرض محتوا | `content_max_width 608dp`, `bottom_sheet_content_max_width 496dp` | تبلت/دسکتاپ |
| چیدمان | `modal_default_width 360dp`, `lesson_progressbar_height 8dp`, `coding_keyboard_height 64dp`, `streak_calendar_height 324dp` | — |

## ۳. نگاشت توکن → صفحه (بر پایهٔ پیشوند نام دایمن)

| پیشوند/خانواده | صفحهٔ هدف | نمونه |
|---|---|---|
| `lesson_*`, `code_*`, `executable_*` | بازیکن درس و ادیتور | `lesson_description_margin_top 30dip`, `executable_lesson_view_*` |
| `codingkeyboard_*`, `codeeditor_*` | کیبورد/تب کد | `coding_keyboard_height 64dp` |
| `streak_*`, `daily_goal_*` | زنجیره و هدف روزانه | `streak_calendar_day_size 44dp` |
| `leaderboard_*`, `iap_podium_*` | لیگ/لیدربورد | `leaderboard_league_header_height 144dp` |
| `onboarding_*` | ۱۲ گام آنبوردینگ | `onboarding_container_margin_bottom 56dip` |
| `modal_*`, `flashbar_*` | مودال/پیام شناور | `modal_default_description_max_height 300dip` |
| `authentication_*` | ورود | `authentication_email_top_bar_margin_top 24dip` |

> نگاشت از **نام توکن** استخراج شده (VERIFIED_STATIC برای وجود توکن، INFERRED برای تخصیص صفحه).

## ۴. حرکت و صدا

| مورد | شاهد | یادداشت |
|---|---|---|
| انیمیشن Rive | ۵۹ فایل `.riv`، `chapter_end_animation_width 200dp` | جشن پایان فصل/چالش |
| پالس دکمهٔ AI | `AiTutorButton$...$pulseDiameterAnimation`, `pulseOpacityAnimation` | Compose |
| آرک زنجیره | `ArcProgressView` | Canvas سفارشی |
| گذارها | ۷۲ `anim` + ۴۷ `animator` + ۲۴ `interpolator` | Sheet/Dialog/Placeholder |

## ۵. دسترس‌پذیری و RTL

* ۱۱۶ locale اعلام‌شده؛ فقط ۱۰ بستهٔ محتوایی ⇒ زبان بدون بسته، دورهٔ انگلیسی نشان می‌دهد.
* توصیف‌های TalkBack برای Sheet/Loader وجود دارد (`bottomsheet_*_content_description`, `m3_loading_indicator_content_description`) — VERIFIED_STATIC.
* برای فارسی: چیدمان ۸۰۹ layout باید RTL شود، ولی **کروم درس (ادیتور/کیبورد/کنسول) نباید RTL شود**؛
  این تفکیک در Mimo وجود ندارد و کار جدید است.
* اعداد فارسی/عربی و نیم‌فاصله: هیچ توکن یا رشته‌ای در بسته برای آن نیست ⇒ کار جدید.
