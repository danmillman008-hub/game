# پروندهٔ لایه — `res/layout/mtrl_picker_header_title_text.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_header_title_text.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_header_title_text.xml`](../../SOURCE/res/layout/mtrl_picker_header_title_text.xml) |
| SHA-256 دیکد | `ccc8c93b28a1d3025d7c441e8fc8eeac3b231a6104e368a84bee9e5a9cbb42cf` |
| ریشه | `TextView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ TextView  #@id/mtrl_picker_title_text
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:gravity` | `0x00800033` |
| 2 | `TextView` | `android:layout_gravity` | `0x00800033` |
| 3 | `TextView` | `android:id` | `@id/mtrl_picker_title_text` |
| 4 | `TextView` | `android:layout_width` | `match_parent` |
| 5 | `TextView` | `android:layout_height` | `wrap_content` |
| 6 | `TextView` | `app:firstBaselineToTopHeight` | `@dimen/mtrl_calendar_title_baseline_to_top` |
| 7 | `TextView` | `style` | `?attr/materialCalendarHeaderTitle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_title_baseline_to_top` | `28.000000dip` / `24.000000dip` (land) |

## ۴. شناسه‌های `@id`

```text
@id/mtrl_picker_title_text
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
<TextView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00800033" android:layout_gravity="0x00800033" android:id="@id/mtrl_picker_title_text" android:layout_width="match_parent" android:layout_height="wrap_content" app:firstBaselineToTopHeight="@dimen/mtrl_calendar_title_baseline_to_top" style="?attr/materialCalendarHeaderTitle"/>
```
