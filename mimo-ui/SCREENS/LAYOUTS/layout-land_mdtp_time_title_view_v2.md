# پروندهٔ لایه — `res/layout-land/mdtp_time_title_view_v2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-land/mdtp_time_title_view_v2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-land/mdtp_time_title_view_v2.xml`](../../SOURCE/res/layout-land/mdtp_time_title_view_v2.xml) |
| SHA-256 دیکد | `addd3589fdbe0020a1b0878ce96fb2c829c2e3301b697e35234a42a186e2bd67` |
| ریشه | `com.wdullaer.materialdatetimepicker.VerticalTextView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.wdullaer.materialdatetimepicker.VerticalTextView  #@id/mdtp_time_picker_header
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:textSize` | `@dimen/mdtp_time_picker_header_text_size` |
| 2 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:textColor` | `@color/mdtp_white` |
| 3 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:gravity` | `0x00000051` |
| 4 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:id` | `@id/mdtp_time_picker_header` |
| 5 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:background` | `@color/mdtp_accent_color_dark` |
| 6 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:paddingTop` | `@dimen/mdtp_date_picker_title_padding` |
| 7 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:visibility` | `gone` |
| 8 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:layout_width` | `@dimen/mdtp_date_picker_title_height` |
| 9 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:layout_height` | `match_parent` |
| 10 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:maxLines` | `1` |
| 11 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:includeFontPadding` | `false` |
| 12 | `com.wdullaer.materialdatetimepicker.VerticalTextView` | `android:textAllCaps` | `@bool/mdtp_title_all_caps` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_accent_color_dark` | `#FF00796B` |
| `@color/mdtp_white` | `#FFFFFFFF` |
| `@dimen/mdtp_date_picker_title_height` | `30.000000dip` / `45.000000dip` (sw600dp) |
| `@dimen/mdtp_date_picker_title_padding` | `9.000000dip` / `14.000000dip` (sw600dp-land) |
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
<com.wdullaer.materialdatetimepicker.VerticalTextView xmlns:android="http://schemas.android.com/apk/res/android" android:textSize="@dimen/mdtp_time_picker_header_text_size" android:textColor="@color/mdtp_white" android:gravity="0x00000051" android:id="@id/mdtp_time_picker_header" android:background="@color/mdtp_accent_color_dark" android:paddingTop="@dimen/mdtp_date_picker_title_padding" android:visibility="gone" android:layout_width="@dimen/mdtp_date_picker_title_height" android:layout_height="match_parent" android:maxLines="1" android:includeFontPadding="false" android:textAllCaps="@bool/mdtp_title_all_caps"/>
```
