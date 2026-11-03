# پروندهٔ لایه — `res/layout/radio_column_end_null_4children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/radio_column_end_null_4children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/radio_column_end_null_4children.xml`](../../SOURCE/res/layout/radio_column_end_null_4children.xml) |
| SHA-256 دیکد | `e2aa150e3f7cc7edd110688bd6288c71c183ebd82dea3e8fd567c772e66066f7` |
| ریشه | `RadioGroup` |
| تعداد گره | 5 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RadioGroup
   ├─ include
   ├─ include
   ├─ include
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RadioGroup` | `android:orientation` | `vertical` |
| 2 | `RadioGroup` | `android:layout_width` | `wrap_content` |
| 3 | `RadioGroup` | `android:layout_height` | `wrap_content` |
| 4 | `RadioGroup` | `style` | `@style/Glance.AppWidget.Column` |
| 5 | `include` | `layout` | `@layout/column_child_end_null_group_0` |
| 6 | `include` | `layout` | `@layout/column_child_end_null_group_1` |
| 7 | `include` | `layout` | `@layout/column_child_end_null_group_2` |
| 8 | `include` | `layout` | `@layout/column_child_end_null_group_3` |

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
@layout/column_child_end_null_group_2
@layout/column_child_end_null_group_3
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RadioGroup xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Column">
  <include layout="@layout/column_child_end_null_group_0"/>
  <include layout="@layout/column_child_end_null_group_1"/>
  <include layout="@layout/column_child_end_null_group_2"/>
  <include layout="@layout/column_child_end_null_group_3"/>
</RadioGroup>
```
