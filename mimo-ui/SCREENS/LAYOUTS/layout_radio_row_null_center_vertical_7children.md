# پروندهٔ لایه — `res/layout/radio_row_null_center_vertical_7children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/radio_row_null_center_vertical_7children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/radio_row_null_center_vertical_7children.xml`](../../SOURCE/res/layout/radio_row_null_center_vertical_7children.xml) |
| SHA-256 دیکد | `70d4bb5f1811d19c932082d08e16ba85d3d5b2dd0da309d2f4c7ced6d53cc951` |
| ریشه | `RadioGroup` |
| تعداد گره | 8 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 7 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RadioGroup
   ├─ include
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
| 1 | `RadioGroup` | `android:orientation` | `horizontal` |
| 2 | `RadioGroup` | `android:layout_width` | `wrap_content` |
| 3 | `RadioGroup` | `android:layout_height` | `wrap_content` |
| 4 | `RadioGroup` | `style` | `@style/Glance.AppWidget.Row` |
| 5 | `include` | `layout` | `@layout/row_child_null_center_vertical_group_0` |
| 6 | `include` | `layout` | `@layout/row_child_null_center_vertical_group_1` |
| 7 | `include` | `layout` | `@layout/row_child_null_center_vertical_group_2` |
| 8 | `include` | `layout` | `@layout/row_child_null_center_vertical_group_3` |
| 9 | `include` | `layout` | `@layout/row_child_null_center_vertical_group_4` |
| 10 | `include` | `layout` | `@layout/row_child_null_center_vertical_group_5` |
| 11 | `include` | `layout` | `@layout/row_child_null_center_vertical_group_6` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Row` | `[]` |

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/row_child_null_center_vertical_group_0
@layout/row_child_null_center_vertical_group_1
@layout/row_child_null_center_vertical_group_2
@layout/row_child_null_center_vertical_group_3
@layout/row_child_null_center_vertical_group_4
@layout/row_child_null_center_vertical_group_5
@layout/row_child_null_center_vertical_group_6
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RadioGroup xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Row">
  <include layout="@layout/row_child_null_center_vertical_group_0"/>
  <include layout="@layout/row_child_null_center_vertical_group_1"/>
  <include layout="@layout/row_child_null_center_vertical_group_2"/>
  <include layout="@layout/row_child_null_center_vertical_group_3"/>
  <include layout="@layout/row_child_null_center_vertical_group_4"/>
  <include layout="@layout/row_child_null_center_vertical_group_5"/>
  <include layout="@layout/row_child_null_center_vertical_group_6"/>
</RadioGroup>
```
