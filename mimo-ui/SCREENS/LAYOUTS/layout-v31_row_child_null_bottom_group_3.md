# پروندهٔ لایه — `res/layout-v31/row_child_null_bottom_group_3.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v31/row_child_null_bottom_group_3.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v31/row_child_null_bottom_group_3.xml`](../../SOURCE/res/layout-v31/row_child_null_bottom_group_3.xml) |
| SHA-256 دیکد | `d474fb74b6926503baf809c957cf1a847c73bd7d81774edc309f84bbcd0940ef` |
| ریشه | `merge` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ ViewStub  #@id/childStub3_wrap_wrap
   └─ ViewStub  #@id/childStub3_expand_wrap
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ViewStub` | `android:layout_gravity` | `0x00000050` |
| 2 | `ViewStub` | `android:id` | `@id/childStub3_wrap_wrap` |
| 3 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 4 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 5 | `ViewStub` | `android:layout_gravity` | `0x00000050` |
| 6 | `ViewStub` | `android:id` | `@id/childStub3_expand_wrap` |
| 7 | `ViewStub` | `android:layout_width` | `0.000000dip` |
| 8 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 9 | `ViewStub` | `android:layout_weight` | `1.000000` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/childStub3_expand_wrap
@id/childStub3_wrap_wrap
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
0x00000050
1.000000
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/radio_row_null_bottom_10children.xml
res/layout/radio_row_null_bottom_4children.xml
res/layout/radio_row_null_bottom_5children.xml
res/layout/radio_row_null_bottom_6children.xml
res/layout/radio_row_null_bottom_7children.xml
res/layout/radio_row_null_bottom_8children.xml
res/layout/radio_row_null_bottom_9children.xml
res/layout/row_null_bottom_10children.xml
res/layout/row_null_bottom_4children.xml
res/layout/row_null_bottom_5children.xml
res/layout/row_null_bottom_6children.xml
res/layout/row_null_bottom_7children.xml
res/layout/row_null_bottom_8children.xml
res/layout/row_null_bottom_9children.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000050" android:id="@id/childStub3_wrap_wrap" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000050" android:id="@id/childStub3_expand_wrap" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000"/>
</merge>
```
