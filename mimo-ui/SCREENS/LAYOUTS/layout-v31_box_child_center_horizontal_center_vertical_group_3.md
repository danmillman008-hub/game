# پروندهٔ لایه — `res/layout-v31/box_child_center_horizontal_center_vertical_group_3.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v31/box_child_center_horizontal_center_vertical_group_3.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v31/box_child_center_horizontal_center_vertical_group_3.xml`](../../SOURCE/res/layout-v31/box_child_center_horizontal_center_vertical_group_3.xml) |
| SHA-256 دیکد | `88eb68e1680151ef96e4e0ae80221cf2a9a9a4a036ab8a11d0c2107bcda7fc13` |
| ریشه | `merge` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   └─ ViewStub  #@id/childStub3_wrap_wrap
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ViewStub` | `android:layout_gravity` | `0x00000011` |
| 2 | `ViewStub` | `android:id` | `@id/childStub3_wrap_wrap` |
| 3 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 4 | `ViewStub` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/childStub3_wrap_wrap
```

## ۵. ارجاع به لایه‌های دیگر

```text
0x00000011
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/box_center_horizontal_center_vertical_10children.xml
res/layout/box_center_horizontal_center_vertical_4children.xml
res/layout/box_center_horizontal_center_vertical_5children.xml
res/layout/box_center_horizontal_center_vertical_6children.xml
res/layout/box_center_horizontal_center_vertical_7children.xml
res/layout/box_center_horizontal_center_vertical_8children.xml
res/layout/box_center_horizontal_center_vertical_9children.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:id="@id/childStub3_wrap_wrap" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</merge>
```
