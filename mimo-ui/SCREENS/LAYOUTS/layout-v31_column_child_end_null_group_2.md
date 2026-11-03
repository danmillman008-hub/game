# پروندهٔ لایه — `res/layout-v31/column_child_end_null_group_2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v31/column_child_end_null_group_2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v31/column_child_end_null_group_2.xml`](../../SOURCE/res/layout-v31/column_child_end_null_group_2.xml) |
| SHA-256 دیکد | `7f7b53a24371a2d6c468ed7c2bccca4dfb177e10ffaf5fecd638be1e27648aaf` |
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
   ├─ ViewStub  #@id/childStub2_wrap_wrap
   └─ ViewStub  #@id/childStub2_wrap_expand
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ViewStub` | `android:layout_gravity` | `0x00800005` |
| 2 | `ViewStub` | `android:id` | `@id/childStub2_wrap_wrap` |
| 3 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 4 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 5 | `ViewStub` | `android:layout_gravity` | `0x00800005` |
| 6 | `ViewStub` | `android:id` | `@id/childStub2_wrap_expand` |
| 7 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 8 | `ViewStub` | `android:layout_height` | `0.000000dip` |
| 9 | `ViewStub` | `android:layout_weight` | `1.000000` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/childStub2_wrap_expand
@id/childStub2_wrap_wrap
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
0x00800005
1.000000
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/column_end_null_10children.xml
res/layout/column_end_null_3children.xml
res/layout/column_end_null_4children.xml
res/layout/column_end_null_5children.xml
res/layout/column_end_null_6children.xml
res/layout/column_end_null_7children.xml
res/layout/column_end_null_8children.xml
res/layout/column_end_null_9children.xml
res/layout/radio_column_end_null_10children.xml
res/layout/radio_column_end_null_3children.xml
res/layout/radio_column_end_null_4children.xml
res/layout/radio_column_end_null_5children.xml
res/layout/radio_column_end_null_6children.xml
res/layout/radio_column_end_null_7children.xml
res/layout/radio_column_end_null_8children.xml
res/layout/radio_column_end_null_9children.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800005" android:id="@id/childStub2_wrap_wrap" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800005" android:id="@id/childStub2_wrap_expand" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_weight="1.000000"/>
</merge>
```
