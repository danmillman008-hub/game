# پروندهٔ لایه — `res/layout/mdtp_date_picker_header_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_date_picker_header_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_date_picker_header_view.xml`](../../SOURCE/res/layout/mdtp_date_picker_header_view.xml) |
| SHA-256 دیکد | `388740a0a8a42b6321d201a0de4287b33821f4faa0bb6cc3e5e851d2db4fb5de` |
| ریشه | `TextView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ TextView  #@id/mdtp_date_picker_header
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:textSize` | `@dimen/mdtp_date_picker_header_text_size` |
| 2 | `TextView` | `android:textColor` | `@color/mdtp_white` |
| 3 | `TextView` | `android:gravity` | `0x00000011` |
| 4 | `TextView` | `android:id` | `@id/mdtp_date_picker_header` |
| 5 | `TextView` | `android:background` | `@color/mdtp_calendar_header` |
| 6 | `TextView` | `android:layout_width` | `match_parent` |
| 7 | `TextView` | `android:layout_height` | `@dimen/mdtp_date_picker_title_height` |
| 8 | `TextView` | `android:includeFontPadding` | `false` |
| 9 | `TextView` | `android:textAllCaps` | `@bool/mdtp_title_all_caps` |
| 10 | `TextView` | `android:importantForAccessibility` | `no` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_calendar_header` | `@color/mdtp_accent_color_dark` |
| `@color/mdtp_white` | `#FFFFFFFF` |
| `@dimen/mdtp_date_picker_header_text_size` | `12.000000dip` / `18.000000dip` (sw600dp) |
| `@dimen/mdtp_date_picker_title_height` | `30.000000dip` / `45.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_date_picker_header
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout-land/mdtp_date_picker_dialog.xml
res/layout-sw600dp-land-v13/mdtp_date_picker_dialog.xml
res/layout-sw600dp-v13/mdtp_date_picker_dialog.xml
res/layout-w270dp-h560dp-v13/mdtp_date_picker_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:textSize="@dimen/mdtp_date_picker_header_text_size" android:textColor="@color/mdtp_white" android:gravity="0x00000011" android:id="@id/mdtp_date_picker_header" android:background="@color/mdtp_calendar_header" android:layout_width="match_parent" android:layout_height="@dimen/mdtp_date_picker_title_height" android:includeFontPadding="false" android:textAllCaps="@bool/mdtp_title_all_caps" android:importantForAccessibility="no"/>
```
