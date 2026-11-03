# پروندهٔ لایه — `res/layout/mdtp_time_title_view_v2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_time_title_view_v2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_time_title_view_v2.xml`](../../SOURCE/res/layout/mdtp_time_title_view_v2.xml) |
| SHA-256 دیکد | `c63680f8ee90cb1104e933f9f91ae897d38d8e90f1de9c9ddd1975062ac9fb9d` |
| ریشه | `TextView` |
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
└─ TextView  #@id/mdtp_time_picker_header
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:textSize` | `@dimen/mdtp_time_picker_header_text_size` |
| 2 | `TextView` | `android:textColor` | `@color/mdtp_white` |
| 3 | `TextView` | `android:gravity` | `0x00000011` |
| 4 | `TextView` | `android:id` | `@id/mdtp_time_picker_header` |
| 5 | `TextView` | `android:background` | `@color/mdtp_accent_color_dark` |
| 6 | `TextView` | `android:padding` | `8.000000dip` |
| 7 | `TextView` | `android:visibility` | `gone` |
| 8 | `TextView` | `android:layout_width` | `match_parent` |
| 9 | `TextView` | `android:layout_height` | `wrap_content` |
| 10 | `TextView` | `android:maxLines` | `1` |
| 11 | `TextView` | `android:includeFontPadding` | `false` |
| 12 | `TextView` | `android:textAllCaps` | `@bool/mdtp_title_all_caps` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_accent_color_dark` | `#FF00796B` |
| `@color/mdtp_white` | `#FFFFFFFF` |
| `@dimen/mdtp_time_picker_header_text_size` | `12.000000dip` / `18.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_time_picker_header
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout-land/mdtp_time_picker_dialog_v2.xml
res/layout/mdtp_time_picker_dialog_v2.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:textSize="@dimen/mdtp_time_picker_header_text_size" android:textColor="@color/mdtp_white" android:gravity="0x00000011" android:id="@id/mdtp_time_picker_header" android:background="@color/mdtp_accent_color_dark" android:padding="8.000000dip" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" android:maxLines="1" android:includeFontPadding="false" android:textAllCaps="@bool/mdtp_title_all_caps"/>
```
