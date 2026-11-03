# پروندهٔ لایه — `res/layout/mtrl_picker_header_toggle.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_header_toggle.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_header_toggle.xml`](../../SOURCE/res/layout/mtrl_picker_header_toggle.xml) |
| SHA-256 دیکد | `65a6a0fec1dd998eca3ebc5852a37f13c50c0de1da60c9bcdc0e71b18ccfe21c` |
| ریشه | `com.google.android.material.internal.CheckableImageButton` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.google.android.material.internal.CheckableImageButton  #@id/mtrl_picker_header_toggle
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.google.android.material.internal.CheckableImageButton` | `android:id` | `@id/mtrl_picker_header_toggle` |
| 2 | `com.google.android.material.internal.CheckableImageButton` | `android:layout_width` | `@dimen/mtrl_min_touch_target_size` |
| 3 | `com.google.android.material.internal.CheckableImageButton` | `android:layout_height` | `@dimen/mtrl_min_touch_target_size` |
| 4 | `com.google.android.material.internal.CheckableImageButton` | `android:layout_marginTop` | `@dimen/mtrl_calendar_header_toggle_margin_top` |
| 5 | `com.google.android.material.internal.CheckableImageButton` | `android:layout_marginBottom` | `@dimen/mtrl_calendar_header_toggle_margin_bottom` |
| 6 | `com.google.android.material.internal.CheckableImageButton` | `style` | `?attr/materialCalendarHeaderToggleButton` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_header_toggle_margin_bottom` | `8.000000dip` / `0.000000dip` (land) |
| `@dimen/mtrl_calendar_header_toggle_margin_top` | `24.000000dip` / `0.000000dip` (land) |
| `@dimen/mtrl_min_touch_target_size` | `48.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/mtrl_picker_header_toggle
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout-land/mtrl_picker_header_dialog.xml
res/layout/mtrl_picker_header_dialog.xml
res/layout/mtrl_picker_header_fullscreen.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<com.google.android.material.internal.CheckableImageButton xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/mtrl_picker_header_toggle" android:layout_width="@dimen/mtrl_min_touch_target_size" android:layout_height="@dimen/mtrl_min_touch_target_size" android:layout_marginTop="@dimen/mtrl_calendar_header_toggle_margin_top" android:layout_marginBottom="@dimen/mtrl_calendar_header_toggle_margin_bottom" style="?attr/materialCalendarHeaderToggleButton"/>
```
