# پروندهٔ لایه — `res/layout/material_timepicker_textinput_display.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_timepicker_textinput_display.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_timepicker_textinput_display.xml`](../../SOURCE/res/layout/material_timepicker_textinput_display.xml) |
| SHA-256 دیکد | `3674c863a05dc26f270bc469ca443a28a39fb09092952cd098825ec486f6336f` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include  #@id/material_hour_text_input
   ├─ include
   └─ include  #@id/material_minute_text_input
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:paddingTop` | `8.000000dip` |
| 2 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `android:layoutDirection` | `ltr` |
| 5 | `include` | `android:id` | `@id/material_hour_text_input` |
| 6 | `include` | `layout` | `@layout/material_chip_input_combo` |
| 7 | `include` | `layout` | `@layout/material_clock_display_divider` |
| 8 | `include` | `android:id` | `@id/material_minute_text_input` |
| 9 | `include` | `layout` | `@layout/material_chip_input_combo` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/material_hour_text_input
@id/material_minute_text_input
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/material_chip_input_combo
@layout/material_clock_display_divider
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/material_textinput_timepicker.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:paddingTop="8.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layoutDirection="ltr">
  <include android:id="@id/material_hour_text_input" layout="@layout/material_chip_input_combo"/>
  <include layout="@layout/material_clock_display_divider"/>
  <include android:id="@id/material_minute_text_input" layout="@layout/material_chip_input_combo"/>
</LinearLayout>
```
