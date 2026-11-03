# پروندهٔ لایه — `res/layout/material_clock_display.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_clock_display.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_clock_display.xml`](../../SOURCE/res/layout/material_clock_display.xml) |
| SHA-256 دیکد | `9f449ade24d1073bed5e018779bfa4b58689b7c06683345dd7f0aba07f24583f` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/material_clock_display
   ├─ include  #@id/material_hour_tv
   ├─ include
   └─ include  #@id/material_minute_tv
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:id` | `@id/material_clock_display` |
| 3 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:baselineAligned` | `false` |
| 6 | `LinearLayout` | `android:layoutDirection` | `ltr` |
| 7 | `include` | `android:id` | `@id/material_hour_tv` |
| 8 | `include` | `layout` | `@layout/material_time_chip` |
| 9 | `include` | `layout` | `@layout/material_clock_display_divider` |
| 10 | `include` | `android:id` | `@id/material_minute_tv` |
| 11 | `include` | `layout` | `@layout/material_time_chip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/material_clock_display
@id/material_hour_tv
@id/material_minute_tv
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/material_clock_display_divider
@layout/material_time_chip
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout-land/material_timepicker.xml
res/layout/material_timepicker.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:id="@id/material_clock_display" android:layout_width="wrap_content" android:layout_height="wrap_content" android:baselineAligned="false" android:layoutDirection="ltr">
  <include android:id="@id/material_hour_tv" layout="@layout/material_time_chip"/>
  <include layout="@layout/material_clock_display_divider"/>
  <include android:id="@id/material_minute_tv" layout="@layout/material_time_chip"/>
</LinearLayout>
```
