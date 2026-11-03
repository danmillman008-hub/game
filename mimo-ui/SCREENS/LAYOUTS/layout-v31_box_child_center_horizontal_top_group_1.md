# پروندهٔ لایه — `res/layout-v31/box_child_center_horizontal_top_group_1.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v31/box_child_center_horizontal_top_group_1.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v31/box_child_center_horizontal_top_group_1.xml`](../../SOURCE/res/layout-v31/box_child_center_horizontal_top_group_1.xml) |
| SHA-256 دیکد | `cb25222ee83770617acde68779075f60bbdf2365104830b07305d8510186526d` |
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
   └─ ViewStub  #@id/childStub1_wrap_wrap
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ViewStub` | `android:layout_gravity` | `0x00000031` |
| 2 | `ViewStub` | `android:id` | `@id/childStub1_wrap_wrap` |
| 3 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 4 | `ViewStub` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/childStub1_wrap_wrap
```

## ۵. ارجاع به لایه‌های دیگر

```text
0x00000031
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/box_center_horizontal_top_10children.xml
res/layout/box_center_horizontal_top_2children.xml
res/layout/box_center_horizontal_top_3children.xml
res/layout/box_center_horizontal_top_4children.xml
res/layout/box_center_horizontal_top_5children.xml
res/layout/box_center_horizontal_top_6children.xml
res/layout/box_center_horizontal_top_7children.xml
res/layout/box_center_horizontal_top_8children.xml
res/layout/box_center_horizontal_top_9children.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000031" android:id="@id/childStub1_wrap_wrap" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</merge>
```
