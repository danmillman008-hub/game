# پروندهٔ لایه — `res/layout/column_end_null_2children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/column_end_null_2children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/column_end_null_2children.xml`](../../SOURCE/res/layout/column_end_null_2children.xml) |
| SHA-256 دیکد | `7551031904943e6937d7a35a04bfe1e6f4d5b357bec4473c55905ee4da1f99c0` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `style` | `@style/Glance.AppWidget.Column` |
| 5 | `include` | `layout` | `@layout/column_child_end_null_group_0` |
| 6 | `include` | `layout` | `@layout/column_child_end_null_group_1` |

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
@layout/column_child_end_null_group_0
@layout/column_child_end_null_group_1
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Column">
  <include layout="@layout/column_child_end_null_group_0"/>
  <include layout="@layout/column_child_end_null_group_1"/>
</LinearLayout>
```
