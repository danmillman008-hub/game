# پروندهٔ لایه — `res/layout/radio_column_start_null_1children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/radio_column_start_null_1children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/radio_column_start_null_1children.xml`](../../SOURCE/res/layout/radio_column_start_null_1children.xml) |
| SHA-256 دیکد | `6a4cfd4f450ff6b9bb1ab34a9a9a48c753336101565fed6a06ed07d19ca108f1` |
| ریشه | `RadioGroup` |
| تعداد گره | 2 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RadioGroup
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RadioGroup` | `android:orientation` | `vertical` |
| 2 | `RadioGroup` | `android:layout_width` | `wrap_content` |
| 3 | `RadioGroup` | `android:layout_height` | `wrap_content` |
| 4 | `RadioGroup` | `style` | `@style/Glance.AppWidget.Column` |
| 5 | `include` | `layout` | `@layout/column_child_start_null_group_0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Column` | `[]` |

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/column_child_start_null_group_0
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RadioGroup xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Column">
  <include layout="@layout/column_child_start_null_group_0"/>
</RadioGroup>
```
