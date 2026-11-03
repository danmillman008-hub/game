# پروندهٔ لایه — `res/layout/material_clock_display_divider.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_clock_display_divider.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_clock_display_divider.xml`](../../SOURCE/res/layout/material_clock_display_divider.xml) |
| SHA-256 دیکد | `7769adeb9f2b0b69e8b75cc0b72eb9703b34c79d7f839e9d283f0ceb485fa297` |
| ریشه | `TextView` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ TextView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:gravity` | `0x00000011` |
| 2 | `TextView` | `android:layout_width` | `@dimen/material_clock_display_padding` |
| 3 | `TextView` | `android:layout_height` | `@dimen/material_clock_display_height` |
| 4 | `TextView` | `android:importantForAccessibility` | `no` |
| 5 | `TextView` | `style` | `?attr/materialDisplayDividerStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/material_clock_display_height` | `80.000000dip` |
| `@dimen/material_clock_display_padding` | `24.000000dip` |

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/material_clock_display.xml
res/layout/material_timepicker_textinput_display.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:layout_width="@dimen/material_clock_display_padding" android:layout_height="@dimen/material_clock_display_height" android:importantForAccessibility="no" style="?attr/materialDisplayDividerStyle"/>
```
