# پروندهٔ لایه — `res/layout/glance_text.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_text.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_text.xml`](../../SOURCE/res/layout/glance_text.xml) |
| SHA-256 دیکد | `bcafcffb2c51cd2fd031abbc7a20b9b2261f9eaaf5543b77bbd713915218db58` |
| ریشه | `TextView` |
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
└─ TextView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:layout_width` | `wrap_content` |
| 2 | `TextView` | `android:layout_height` | `wrap_content` |
| 3 | `TextView` | `android:textDirection` | `locale` |
| 4 | `TextView` | `app:glance_isTopLevelLayout` | `true` |
| 5 | `TextView` | `style` | `@style/Glance.AppWidget.Text` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Text` | `[{'attr': 'android:ellipsize', 'attr_id': '0x010100AB', 'value': '3', 'value_type': 'int_dec'}]` |

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
res/layout/glance_deleted_view.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.Text"/>
```
