# پروندهٔ لایه — `res/layout/glance_linear_progress_indicator.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_linear_progress_indicator.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_linear_progress_indicator.xml`](../../SOURCE/res/layout/glance_linear_progress_indicator.xml) |
| SHA-256 دیکد | `34bf49962f42c10ad27be5c484b264e27e960b3188c71ad5e689473f134a2535` |
| ریشه | `ProgressBar` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ProgressBar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 2 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 3 | `ProgressBar` | `app:glance_isTopLevelLayout` | `true` |
| 4 | `ProgressBar` | `style` | `@style/Glance.AppWidget.LinearProgressIndicator` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.LinearProgressIndicator` | `[{'attr': 'android:progressDrawable', 'attr_id': '0x0101013C', 'value': '@drawable/glance_progress_horizontal', 'value_type': 'reference'}]` |

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

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ProgressBar xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.LinearProgressIndicator"/>
```
