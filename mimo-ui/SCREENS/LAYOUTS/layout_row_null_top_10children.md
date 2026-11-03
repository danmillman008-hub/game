# پروندهٔ لایه — `res/layout/row_null_top_10children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/row_null_top_10children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/row_null_top_10children.xml`](../../SOURCE/res/layout/row_null_top_10children.xml) |
| SHA-256 دیکد | `6f7fb47488d84d064856efce59d420a933c48d300aa9efbcda7683c6068ed639` |
| ریشه | `LinearLayout` |
| تعداد گره | 11 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 10 |
| ارجاع به منابع | 11 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   ├─ include
   ├─ include
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
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `style` | `@style/Glance.AppWidget.Row` |
| 5 | `include` | `layout` | `@layout/row_child_null_top_group_0` |
| 6 | `include` | `layout` | `@layout/row_child_null_top_group_1` |
| 7 | `include` | `layout` | `@layout/row_child_null_top_group_2` |
| 8 | `include` | `layout` | `@layout/row_child_null_top_group_3` |
| 9 | `include` | `layout` | `@layout/row_child_null_top_group_4` |
| 10 | `include` | `layout` | `@layout/row_child_null_top_group_5` |
| 11 | `include` | `layout` | `@layout/row_child_null_top_group_6` |
| 12 | `include` | `layout` | `@layout/row_child_null_top_group_7` |
| 13 | `include` | `layout` | `@layout/row_child_null_top_group_8` |
| 14 | `include` | `layout` | `@layout/row_child_null_top_group_9` |

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
@layout/row_child_null_top_group_5
@layout/row_child_null_top_group_6
@layout/row_child_null_top_group_7
@layout/row_child_null_top_group_8
@layout/row_child_null_top_group_9
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
  <include layout="@layout/row_child_null_top_group_5"/>
  <include layout="@layout/row_child_null_top_group_6"/>
  <include layout="@layout/row_child_null_top_group_7"/>
  <include layout="@layout/row_child_null_top_group_8"/>
  <include layout="@layout/row_child_null_top_group_9"/>
</LinearLayout>
```
