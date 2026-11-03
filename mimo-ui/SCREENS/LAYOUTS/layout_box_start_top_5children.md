# پروندهٔ لایه — `res/layout/box_start_top_5children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/box_start_top_5children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/box_start_top_5children.xml`](../../SOURCE/res/layout/box_start_top_5children.xml) |
| SHA-256 دیکد | `4d7e9d7134e9f7e4261235130b5ec60523820f621ff982a6da6f2f1d06bb0773` |
| ریشه | `FrameLayout` |
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
└─ FrameLayout
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
| 4 | `include` | `layout` | `@layout/box_child_start_top_group_0` |
| 5 | `include` | `layout` | `@layout/box_child_start_top_group_1` |
| 6 | `include` | `layout` | `@layout/box_child_start_top_group_2` |
| 7 | `include` | `layout` | `@layout/box_child_start_top_group_3` |
| 8 | `include` | `layout` | `@layout/box_child_start_top_group_4` |

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
@layout/box_child_start_top_group_0
@layout/box_child_start_top_group_1
@layout/box_child_start_top_group_2
@layout/box_child_start_top_group_3
@layout/box_child_start_top_group_4
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Box">
  <include layout="@layout/box_child_start_top_group_0"/>
  <include layout="@layout/box_child_start_top_group_1"/>
  <include layout="@layout/box_child_start_top_group_2"/>
  <include layout="@layout/box_child_start_top_group_3"/>
  <include layout="@layout/box_child_start_top_group_4"/>
</FrameLayout>
```
