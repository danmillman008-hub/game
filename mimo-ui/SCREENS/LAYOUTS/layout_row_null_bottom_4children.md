# پروندهٔ لایه — `res/layout/row_null_bottom_4children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/row_null_bottom_4children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/row_null_bottom_4children.xml`](../../SOURCE/res/layout/row_null_bottom_4children.xml) |
| SHA-256 دیکد | `4e5383fa22e2c05e1048096400d0d84be4cef305b21b3d9066eb7d3fb01170aa` |
| ریشه | `LinearLayout` |
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
└─ LinearLayout
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
| 5 | `include` | `layout` | `@layout/row_child_null_bottom_group_0` |
| 6 | `include` | `layout` | `@layout/row_child_null_bottom_group_1` |
| 7 | `include` | `layout` | `@layout/row_child_null_bottom_group_2` |
| 8 | `include` | `layout` | `@layout/row_child_null_bottom_group_3` |

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
@layout/row_child_null_bottom_group_0
@layout/row_child_null_bottom_group_1
@layout/row_child_null_bottom_group_2
@layout/row_child_null_bottom_group_3
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Row">
  <include layout="@layout/row_child_null_bottom_group_0"/>
  <include layout="@layout/row_child_null_bottom_group_1"/>
  <include layout="@layout/row_child_null_bottom_group_2"/>
  <include layout="@layout/row_child_null_bottom_group_3"/>
</LinearLayout>
```
