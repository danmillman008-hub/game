# پروندهٔ لایه — `res/layout-v33/glance_linear_progress_indicator_center_horizontal_center_vertical.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_linear_progress_indicator_center_horizontal_center_vertical.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_linear_progress_indicator_center_horizontal_center_vertical.xml`](../../SOURCE/res/layout-v33/glance_linear_progress_indicator_center_horizontal_center_vertical.xml) |
| SHA-256 دیکد | `ad0ec474ccd5608216789e6b7b740b98f093bd6c53e010d62c7197e7f820df84` |
| ریشه | `ProgressBar` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ProgressBar  #@id/glanceView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 2 | `ProgressBar` | `android:id` | `@id/glanceView` |
| 3 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 4 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 5 | `ProgressBar` | `android:layoutDirection` | `locale` |
| 6 | `ProgressBar` | `app:glance_isTopLevelLayout` | `true` |
| 7 | `ProgressBar` | `style` | `@style/Glance.AppWidget.LinearProgressIndicator` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.LinearProgressIndicator` | `[{'attr': 'android:progressDrawable', 'attr_id': '0x0101013C', 'value': '@drawable/glance_progress_horizontal', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/glanceView
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
<ProgressBar xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_gravity="0x00000011" android:id="@id/glanceView" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.LinearProgressIndicator"/>
```
