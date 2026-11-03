# پروندهٔ لایه — `res/layout/column_child_start_null_group_2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/column_child_start_null_group_2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/column_child_start_null_group_2.xml`](../../SOURCE/res/layout/column_child_start_null_group_2.xml) |
| SHA-256 دیکد | `322c3b36599d4b5e17f2ca2d1be790583083c539450f554edc672244526be11a` |
| ریشه | `merge` |
| تعداد گره | 7 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ ViewStub  #@id/childStub2_wrap_wrap
   ├─ ViewStub  #@id/childStub2_wrap_match
   ├─ ViewStub  #@id/childStub2_wrap_expand
   ├─ ViewStub  #@id/childStub2_match_wrap
   ├─ ViewStub  #@id/childStub2_match_match
   └─ ViewStub  #@id/childStub2_match_expand
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ViewStub` | `android:layout_gravity` | `0x00800003` |
| 2 | `ViewStub` | `android:id` | `@id/childStub2_wrap_wrap` |
| 3 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 4 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 5 | `ViewStub` | `android:layout_gravity` | `0x00800003` |
| 6 | `ViewStub` | `android:id` | `@id/childStub2_wrap_match` |
| 7 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 8 | `ViewStub` | `android:layout_height` | `match_parent` |
| 9 | `ViewStub` | `android:layout_gravity` | `0x00800003` |
| 10 | `ViewStub` | `android:id` | `@id/childStub2_wrap_expand` |
| 11 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 12 | `ViewStub` | `android:layout_height` | `0.000000dip` |
| 13 | `ViewStub` | `android:layout_weight` | `1.000000` |
| 14 | `ViewStub` | `android:layout_gravity` | `0x00800003` |
| 15 | `ViewStub` | `android:id` | `@id/childStub2_match_wrap` |
| 16 | `ViewStub` | `android:layout_width` | `match_parent` |
| 17 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 18 | `ViewStub` | `android:layout_gravity` | `0x00800003` |
| 19 | `ViewStub` | `android:id` | `@id/childStub2_match_match` |
| 20 | `ViewStub` | `android:layout_width` | `match_parent` |
| 21 | `ViewStub` | `android:layout_height` | `match_parent` |
| 22 | `ViewStub` | `android:layout_gravity` | `0x00800003` |
| 23 | `ViewStub` | `android:id` | `@id/childStub2_match_expand` |
| 24 | `ViewStub` | `android:layout_width` | `match_parent` |
| 25 | `ViewStub` | `android:layout_height` | `0.000000dip` |
| 26 | `ViewStub` | `android:layout_weight` | `1.000000` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/childStub2_match_expand
@id/childStub2_match_match
@id/childStub2_match_wrap
@id/childStub2_wrap_expand
@id/childStub2_wrap_match
@id/childStub2_wrap_wrap
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
0x00800003
1.000000
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/column_start_null_10children.xml
res/layout/column_start_null_3children.xml
res/layout/column_start_null_4children.xml
res/layout/column_start_null_5children.xml
res/layout/column_start_null_6children.xml
res/layout/column_start_null_7children.xml
res/layout/column_start_null_8children.xml
res/layout/column_start_null_9children.xml
res/layout/radio_column_start_null_10children.xml
res/layout/radio_column_start_null_3children.xml
res/layout/radio_column_start_null_4children.xml
res/layout/radio_column_start_null_5children.xml
res/layout/radio_column_start_null_6children.xml
res/layout/radio_column_start_null_7children.xml
res/layout/radio_column_start_null_8children.xml
res/layout/radio_column_start_null_9children.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800003" android:id="@id/childStub2_wrap_wrap" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800003" android:id="@id/childStub2_wrap_match" android:layout_width="wrap_content" android:layout_height="match_parent"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800003" android:id="@id/childStub2_wrap_expand" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_weight="1.000000"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800003" android:id="@id/childStub2_match_wrap" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800003" android:id="@id/childStub2_match_match" android:layout_width="match_parent" android:layout_height="match_parent"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800003" android:id="@id/childStub2_match_expand" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_weight="1.000000"/>
</merge>
```
