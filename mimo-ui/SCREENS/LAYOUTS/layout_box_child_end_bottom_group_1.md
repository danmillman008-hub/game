# پروندهٔ لایه — `res/layout/box_child_end_bottom_group_1.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/box_child_end_bottom_group_1.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/box_child_end_bottom_group_1.xml`](../../SOURCE/res/layout/box_child_end_bottom_group_1.xml) |
| SHA-256 دیکد | `3f2893c1e8914f1fa453d96b58081c645e249c6273f076c07d842c097ae52e5c` |
| ریشه | `merge` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ ViewStub  #@id/childStub1_wrap_wrap
   ├─ ViewStub  #@id/childStub1_wrap_match
   ├─ ViewStub  #@id/childStub1_match_wrap
   └─ ViewStub  #@id/childStub1_match_match
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ViewStub` | `android:layout_gravity` | `0x00800055` |
| 2 | `ViewStub` | `android:id` | `@id/childStub1_wrap_wrap` |
| 3 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 4 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 5 | `ViewStub` | `android:layout_gravity` | `0x00800055` |
| 6 | `ViewStub` | `android:id` | `@id/childStub1_wrap_match` |
| 7 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 8 | `ViewStub` | `android:layout_height` | `match_parent` |
| 9 | `ViewStub` | `android:layout_gravity` | `0x00800055` |
| 10 | `ViewStub` | `android:id` | `@id/childStub1_match_wrap` |
| 11 | `ViewStub` | `android:layout_width` | `match_parent` |
| 12 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 13 | `ViewStub` | `android:layout_gravity` | `0x00800055` |
| 14 | `ViewStub` | `android:id` | `@id/childStub1_match_match` |
| 15 | `ViewStub` | `android:layout_width` | `match_parent` |
| 16 | `ViewStub` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/childStub1_match_match
@id/childStub1_match_wrap
@id/childStub1_wrap_match
@id/childStub1_wrap_wrap
```

## ۵. ارجاع به لایه‌های دیگر

```text
0x00800055
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/box_end_bottom_10children.xml
res/layout/box_end_bottom_2children.xml
res/layout/box_end_bottom_3children.xml
res/layout/box_end_bottom_4children.xml
res/layout/box_end_bottom_5children.xml
res/layout/box_end_bottom_6children.xml
res/layout/box_end_bottom_7children.xml
res/layout/box_end_bottom_8children.xml
res/layout/box_end_bottom_9children.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800055" android:id="@id/childStub1_wrap_wrap" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800055" android:id="@id/childStub1_wrap_match" android:layout_width="wrap_content" android:layout_height="match_parent"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800055" android:id="@id/childStub1_match_wrap" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  <ViewStub xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800055" android:id="@id/childStub1_match_match" android:layout_width="match_parent" android:layout_height="match_parent"/>
</merge>
```
