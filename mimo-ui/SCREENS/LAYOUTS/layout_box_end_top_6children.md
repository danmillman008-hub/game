# پروندهٔ لایه — `res/layout/box_end_top_6children.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/box_end_top_6children.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/box_end_top_6children.xml`](../../SOURCE/res/layout/box_end_top_6children.xml) |
| SHA-256 دیکد | `38c0c0f134c972a8b2e4a55a9dc8a9442ba4d6a224c1933b5a7b31475ea90570` |
| ریشه | `FrameLayout` |
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
└─ FrameLayout
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
| 4 | `include` | `layout` | `@layout/box_child_end_top_group_0` |
| 5 | `include` | `layout` | `@layout/box_child_end_top_group_1` |
| 6 | `include` | `layout` | `@layout/box_child_end_top_group_2` |
| 7 | `include` | `layout` | `@layout/box_child_end_top_group_3` |
| 8 | `include` | `layout` | `@layout/box_child_end_top_group_4` |
| 9 | `include` | `layout` | `@layout/box_child_end_top_group_5` |

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
@layout/box_child_end_top_group_0
@layout/box_child_end_top_group_1
@layout/box_child_end_top_group_2
@layout/box_child_end_top_group_3
@layout/box_child_end_top_group_4
@layout/box_child_end_top_group_5
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.Box">
  <include layout="@layout/box_child_end_top_group_0"/>
  <include layout="@layout/box_child_end_top_group_1"/>
  <include layout="@layout/box_child_end_top_group_2"/>
  <include layout="@layout/box_child_end_top_group_3"/>
  <include layout="@layout/box_child_end_top_group_4"/>
  <include layout="@layout/box_child_end_top_group_5"/>
</FrameLayout>
```
