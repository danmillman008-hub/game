# پروندهٔ لایه — `res/layout/material_time_input.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_time_input.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_time_input.xml`](../../SOURCE/res/layout/material_time_input.xml) |
| SHA-256 دیکد | `a6aac5eb1ede1c64f6bc55d9b5fe0b81fe38659203be4f5988d4bfd48bb2d608` |
| ریشه | `com.google.android.material.textfield.TextInputLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.google.android.material.textfield.TextInputLayout
   ├─ com.google.android.material.textfield.TextInputEditText
   └─ TextView  #@id/material_label
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `wrap_content` |
| 2 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 3 | `com.google.android.material.textfield.TextInputLayout` | `app:errorIconDrawable` | `@null` |
| 4 | `com.google.android.material.textfield.TextInputLayout` | `app:hintEnabled` | `false` |
| 5 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `@dimen/material_clock_display_width` |
| 6 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `@dimen/material_clock_display_height` |
| 7 | `com.google.android.material.textfield.TextInputEditText` | `android:textCursorDrawable` | `@drawable/material_cursor_drawable` |
| 8 | `TextView` | `android:id` | `@id/material_label` |
| 9 | `TextView` | `android:focusable` | `false` |
| 10 | `TextView` | `android:layout_width` | `@dimen/material_clock_display_width` |
| 11 | `TextView` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/material_clock_display_height` | `80.000000dip` |
| `@dimen/material_clock_display_width` | `96.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/material_label
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<com.google.android.material.textfield.TextInputLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="wrap_content" android:layout_height="wrap_content" app:errorIconDrawable="@null" app:hintEnabled="false">
  <com.google.android.material.textfield.TextInputEditText android:layout_width="@dimen/material_clock_display_width" android:layout_height="@dimen/material_clock_display_height" android:textCursorDrawable="@drawable/material_cursor_drawable"/>
  <TextView android:id="@id/material_label" android:focusable="false" android:layout_width="@dimen/material_clock_display_width" android:layout_height="wrap_content"/>
</com.google.android.material.textfield.TextInputLayout>
```
