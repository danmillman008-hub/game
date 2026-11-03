# پروندهٔ لایه — `res/layout/column_end_null_6children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/column_end_null_6children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/column_end_null_6children.xml`](../../SOURCE/res/layout/column_end_null_6children.xml) |
| SHA-256 دیکد | `7131040e4eab134e1b6340c6e280d43a35c272578e431559145187903f5a20c0` |
| ریشه | `LinearLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 6 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   ├─ include
   ├─ include
   ├─ include
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
| 7 | `include` | `layout` | `@layout/column_child_end_null_group_2` |
| 8 | `include` | `layout` | `@layout/column_child_end_null_group_3` |
| 9 | `include` | `layout` | `@layout/column_child_end_null_group_4` |
| 10 | `include` | `layout` | `@layout/column_child_end_null_group_5` |

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
@layout/column_child_end_null_group_4
@layout/column_child_end_null_group_5
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
  <include layout="@layout/column_child_end_null_group_2"/>
  <include layout="@layout/column_child_end_null_group_3"/>
  <include layout="@layout/column_child_end_null_group_4"/>
  <include layout="@layout/column_child_end_null_group_5"/>
</LinearLayout>
```
