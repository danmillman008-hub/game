# پروندهٔ لایه — `res/layout/row_null_top_5children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/row_null_top_5children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/row_null_top_5children.xml`](../../SOURCE/res/layout/row_null_top_5children.xml) |
| SHA-256 دیکد | `1d2c578fabe6547566a4ac7c5c4289c01b359248e1114a1c3e53422556a05d80` |
| ریشه | `LinearLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   ├─ include
   ├─ include
   ├─ include
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `style` | `@style/Glance.AppWidget.Row` |
| 5 | `include` | `layout` | `@layout/row_child_null_top_group_0` |
| 6 | `include` | `layout` | `@layout/row_child_null_top_group_1` |
| 7 | `include` | `layout` | `@layout/row_child_null_top_group_2` |
| 8 | `include` | `layout` | `@layout/row_child_null_top_group_3` |
| 9 | `include` | `layout` | `@layout/row_child_null_top_group_4` |

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
@layout/row_child_null_top_group_0
@layout/row_child_null_top_group_1
@layout/row_child_null_top_group_2
@layout/row_child_null_top_group_3
@layout/row_child_null_top_group_4
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Row">
  <include layout="@layout/row_child_null_top_group_0"/>
  <include layout="@layout/row_child_null_top_group_1"/>
  <include layout="@layout/row_child_null_top_group_2"/>
  <include layout="@layout/row_child_null_top_group_3"/>
  <include layout="@layout/row_child_null_top_group_4"/>
</LinearLayout>
```
