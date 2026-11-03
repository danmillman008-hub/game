# پروندهٔ لایه — `res/layout/mtrl_picker_header_selection_text.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_header_selection_text.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_header_selection_text.xml`](../../SOURCE/res/layout/mtrl_picker_header_selection_text.xml) |
| SHA-256 دیکد | `ca4a37b05a2c2b04336c6fa4eef8082ec3c3e26ca200edf7851950f60ce628da` |
| ریشه | `TextView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ TextView  #@id/mtrl_picker_header_selection_text
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:gravity` | `0x00800053` |
| 2 | `TextView` | `android:id` | `@id/mtrl_picker_header_selection_text` |
| 3 | `TextView` | `android:layout_width` | `match_parent` |
| 4 | `TextView` | `android:layout_height` | `wrap_content` |
| 5 | `TextView` | `app:autoSizeTextType` | `1` |
| 6 | `TextView` | `app:firstBaselineToTopHeight` | `@dimen/mtrl_calendar_selection_text_baseline_to_top` |
| 7 | `TextView` | `app:lineHeight` | `@dimen/mtrl_calendar_header_selection_line_height` |
| 8 | `TextView` | `style` | `?attr/materialCalendarHeaderSelection` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_header_selection_line_height` | `32.000000dip` |
| `@dimen/mtrl_calendar_selection_text_baseline_to_top` | `100.000000dip` / `64.000000dip` (land) |

## ۴. شناسه‌های `@id`

```text
@id/mtrl_picker_header_selection_text
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/mtrl_picker_header_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00800053" android:id="@id/mtrl_picker_header_selection_text" android:layout_width="match_parent" android:layout_height="wrap_content" app:autoSizeTextType="1" app:firstBaselineToTopHeight="@dimen/mtrl_calendar_selection_text_baseline_to_top" app:lineHeight="@dimen/mtrl_calendar_header_selection_line_height" style="?attr/materialCalendarHeaderSelection"/>
```
