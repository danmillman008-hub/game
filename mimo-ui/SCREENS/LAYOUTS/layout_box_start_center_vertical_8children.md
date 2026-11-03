# پروندهٔ لایه — `res/layout/box_start_center_vertical_8children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/box_start_center_vertical_8children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/box_start_center_vertical_8children.xml`](../../SOURCE/res/layout/box_start_center_vertical_8children.xml) |
| SHA-256 دیکد | `7f65fc6a3af2a33830cf843dd1dbb5d0c3adbafe8bc43e5399a33a4336da1893` |
| ریشه | `FrameLayout` |
| تعداد گره | 9 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 8 |
| ارجاع به منابع | 9 |

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
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 2 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 3 | `FrameLayout` | `style` | `@style/Glance.AppWidget.Box` |
| 4 | `include` | `layout` | `@layout/box_child_start_center_vertical_group_0` |
| 5 | `include` | `layout` | `@layout/box_child_start_center_vertical_group_1` |
| 6 | `include` | `layout` | `@layout/box_child_start_center_vertical_group_2` |
| 7 | `include` | `layout` | `@layout/box_child_start_center_vertical_group_3` |
| 8 | `include` | `layout` | `@layout/box_child_start_center_vertical_group_4` |
| 9 | `include` | `layout` | `@layout/box_child_start_center_vertical_group_5` |
| 10 | `include` | `layout` | `@layout/box_child_start_center_vertical_group_6` |
| 11 | `include` | `layout` | `@layout/box_child_start_center_vertical_group_7` |

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
@layout/box_child_start_center_vertical_group_0
@layout/box_child_start_center_vertical_group_1
@layout/box_child_start_center_vertical_group_2
@layout/box_child_start_center_vertical_group_3
@layout/box_child_start_center_vertical_group_4
@layout/box_child_start_center_vertical_group_5
@layout/box_child_start_center_vertical_group_6
@layout/box_child_start_center_vertical_group_7
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Box">
  <include layout="@layout/box_child_start_center_vertical_group_0"/>
  <include layout="@layout/box_child_start_center_vertical_group_1"/>
  <include layout="@layout/box_child_start_center_vertical_group_2"/>
  <include layout="@layout/box_child_start_center_vertical_group_3"/>
  <include layout="@layout/box_child_start_center_vertical_group_4"/>
  <include layout="@layout/box_child_start_center_vertical_group_5"/>
  <include layout="@layout/box_child_start_center_vertical_group_6"/>
  <include layout="@layout/box_child_start_center_vertical_group_7"/>
</FrameLayout>
```
