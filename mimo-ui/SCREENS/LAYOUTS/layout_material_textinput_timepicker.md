# پروندهٔ لایه — `res/layout/material_textinput_timepicker.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_textinput_timepicker.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_textinput_timepicker.xml`](../../SOURCE/res/layout/material_textinput_timepicker.xml) |
| SHA-256 دیکد | `c11e88deba4358382d1f412626fcf3a415c4a7a7598dabf4f9442ea2dc50f34a` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   └─ include  #@id/material_clock_period_toggle
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `android:baselineAligned` | `false` |
| 5 | `include` | `layout` | `@layout/material_timepicker_textinput_display` |
| 6 | `include` | `android:id` | `@id/material_clock_period_toggle` |
| 7 | `include` | `android:layout_width` | `@dimen/material_clock_period_toggle_width` |
| 8 | `include` | `android:layout_height` | `@dimen/material_clock_period_toggle_height` |
| 9 | `include` | `android:layout_marginStart` | `@dimen/material_clock_period_toggle_horizontal_gap` |
| 10 | `include` | `layout` | `@layout/material_clock_period_toggle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/material_clock_period_toggle_height` | `98.000000dip` |
| `@dimen/material_clock_period_toggle_horizontal_gap` | `12.000000dip` |
| `@dimen/material_clock_period_toggle_width` | `52.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/material_clock_period_toggle
```

## ۵. ارجاع به لایه‌های دیگر

```text
@dimen/material_clock_period_toggle_height
@dimen/material_clock_period_toggle_horizontal_gap
@dimen/material_clock_period_toggle_width
@layout/material_clock_period_toggle
@layout/material_timepicker_textinput_display
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/material_timepicker_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:layout_width="wrap_content" android:layout_height="wrap_content" android:baselineAligned="false">
  <include layout="@layout/material_timepicker_textinput_display"/>
  <include android:id="@id/material_clock_period_toggle" android:layout_width="@dimen/material_clock_period_toggle_width" android:layout_height="@dimen/material_clock_period_toggle_height" android:layout_marginStart="@dimen/material_clock_period_toggle_horizontal_gap" layout="@layout/material_clock_period_toggle"/>
</LinearLayout>
```
