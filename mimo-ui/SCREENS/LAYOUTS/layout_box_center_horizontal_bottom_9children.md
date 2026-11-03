# پروندهٔ لایه — `res/layout/box_center_horizontal_bottom_9children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/box_center_horizontal_bottom_9children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/box_center_horizontal_bottom_9children.xml`](../../SOURCE/res/layout/box_center_horizontal_bottom_9children.xml) |
| SHA-256 دیکد | `b2fc93b7d31e7ec02b91ed694a6902883b53ec3ce313c460ee5ac315ca282fd9` |
| ریشه | `FrameLayout` |
| تعداد گره | 10 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 9 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
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
| 1 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 2 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 3 | `FrameLayout` | `style` | `@style/Glance.AppWidget.Box` |
| 4 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_0` |
| 5 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_1` |
| 6 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_2` |
| 7 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_3` |
| 8 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_4` |
| 9 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_5` |
| 10 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_6` |
| 11 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_7` |
| 12 | `include` | `layout` | `@layout/box_child_center_horizontal_bottom_group_8` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Box` | `[]` |

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/box_child_center_horizontal_bottom_group_0
@layout/box_child_center_horizontal_bottom_group_1
@layout/box_child_center_horizontal_bottom_group_2
@layout/box_child_center_horizontal_bottom_group_3
@layout/box_child_center_horizontal_bottom_group_4
@layout/box_child_center_horizontal_bottom_group_5
@layout/box_child_center_horizontal_bottom_group_6
@layout/box_child_center_horizontal_bottom_group_7
@layout/box_child_center_horizontal_bottom_group_8
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Box">
  <include layout="@layout/box_child_center_horizontal_bottom_group_0"/>
  <include layout="@layout/box_child_center_horizontal_bottom_group_1"/>
  <include layout="@layout/box_child_center_horizontal_bottom_group_2"/>
  <include layout="@layout/box_child_center_horizontal_bottom_group_3"/>
  <include layout="@layout/box_child_center_horizontal_bottom_group_4"/>
  <include layout="@layout/box_child_center_horizontal_bottom_group_5"/>
  <include layout="@layout/box_child_center_horizontal_bottom_group_6"/>
  <include layout="@layout/box_child_center_horizontal_bottom_group_7"/>
  <include layout="@layout/box_child_center_horizontal_bottom_group_8"/>
</FrameLayout>
```
