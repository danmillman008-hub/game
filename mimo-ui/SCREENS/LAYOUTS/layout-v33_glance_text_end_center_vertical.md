# پروندهٔ لایه — `res/layout-v33/glance_text_end_center_vertical.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_text_end_center_vertical.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_text_end_center_vertical.xml`](../../SOURCE/res/layout-v33/glance_text_end_center_vertical.xml) |
| SHA-256 دیکد | `0c160df3648338423d2695b2bb6dc51491ac231cdaac23614ac8c4d706858d80` |
| ریشه | `TextView` |
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
└─ TextView  #@id/glanceView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:layout_gravity` | `0x00800015` |
| 2 | `TextView` | `android:id` | `@id/glanceView` |
| 3 | `TextView` | `android:layout_width` | `wrap_content` |
| 4 | `TextView` | `android:layout_height` | `wrap_content` |
| 5 | `TextView` | `android:textDirection` | `locale` |
| 6 | `TextView` | `android:layoutDirection` | `locale` |
| 7 | `TextView` | `app:glance_isTopLevelLayout` | `true` |
| 8 | `TextView` | `style` | `@style/Glance.AppWidget.Text` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Text` | `[{'attr': 'android:ellipsize', 'attr_id': '0x010100AB', 'value': '3', 'value_type': 'int_dec'}]` |

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
<TextView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800015" android:id="@id/glanceView" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textDirection="locale" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.Text"/>
```
