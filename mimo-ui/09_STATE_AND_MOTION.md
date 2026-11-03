# ۰۹ — حالتهای رابط و حرکت

## ۱. حالتها (شواهد = نام رشتهها، `PARTIALLY_VERIFIED`)

از ۱٬۷۲۱ نام رشته، گروههای زیر به طور کامل استخراج شدهاند؛ نمونه نیاوردههایم،
فهرست کامل در `CATALOGS/DESIGN_TOKENS.json` و `SOURCE/values/values/string.xml`:

| خانواده | تعداد نام | نمونهٔ شناسهها |
|---|---|---|
| آفلاین (`offline`) | 14 | `generic_offline_*`, `practice_offline_*` |
| خالی (`empty`) | 10 | `playgrounds_empty_*`, `saved_code_empty_state_*` |
| خطا (`error`) | 71 | `authentication_error_*`, `generic_error_retry` |
| بارگذاری (`loading`) | 7 | `onboarding_curriculum_loading`, `chapter_finished_loading` |
| قفل/غیرفعال (`locked`, `disabled`) | 6 | `anonymous_feature_locked_*` |
| ارتقا (`upgrade`) | 42 | `*_upgrade_*`, `keys_*` |

`CATALOGS/SCREEN_STATE_MATRIX` (دور قبل، `REFERENCE/PRIOR_WORK`) ۲۴ جفت (سطح، حالت) را
با شاهد مستقیم مستند کرده؛ بقیه `NOT_TESTED`اند چون نیازمند اجرا هستند.

## ۲. حرکت اعلانی (۱۴۳ فایل، کامل)

- `res/anim/` ۷۲ فایل: `design_bottom_sheet_slide_in/out`, `fade_in/out`,
  `fragment_fast_out_extra_slow_in`, `abc_*`, `m3_*`, `glance_*`.
- `res/animator/` ۴۷ فایل: انیماتورهای حالت دکمه/چکباکس/رادیو/سوئیچ Material.
- `res/interpolator/` ۲۴ فایل: `decelerate_cubic`, `fast_out_slow_in`, … .
- استایلها اینها را وصل میکنند: `Animation.Design.BottomSheetDialog` →
  `@anim/design_bottom_sheet_slide_in` / `_out`؛
  `Animation.Material3.BottomSheetDialog` → `@anim/m3_bottom_sheet_slide_in/out`؛
  `Animation.Material3.SideSheetDialog` → `m3_side_sheet_enter_from_left/right`.

## ۳. Rive (59 فایل)

`SOURCE/res/raw/*.riv` و `SOURCE/res/raw-night-v8/*.riv` شامل انیمیشنهای جشن پایان فصل،
زنجیره، شخصیتها و `chapter_end_animation_width = 200dp` (تبلت ۲۶۰dp).
کتابخانهٔ بومی `librive-android.so` در `lib/arm64-v8a` و `lib/armeabi-v7a` shipped شده.

## ۴. حرکت در Compose / ویوهای سفارشی

| مورد | شاهد |
|---|---|
| پالس دکمهٔ مربی | `AiTutorButton$…$pulseDiameterAnimation`, `pulseOpacityAnimation` |
| کمان پیشرفت روز | `ArcProgressView` (Canvas سفارشی) |
| حلقهٔ هدف روزانه | `DailySparksGoalProgressView` + متن ۴۲sp |
| دکمهٔ اجرای کد | `com.getmimo.ui.common.runbutton.AnimatedRunButton` |
| صفحهٔ درس | `ViewPager2` + `animateLayoutChanges=false` (سوایپ نیتیو) |
| لیست حالات رنگ | ۳۰۴ فایل `res/color*/` (pressed/disabled/checked) |
