# پروندهٔ لایه — `res/layout/calendar_grid_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/calendar_grid_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/calendar_grid_item.xml`](../../SOURCE/res/layout/calendar_grid_item.xml) |
| SHA-256 دیکد | `246e8521ec43791d56558954a8ad4aa3043797a7e96112ac92abc18a8179e295` |
| ریشه | `FrameLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   ├─ TextView  #@id/tv_day
   ├─ ImageView  #@id/iv_day
   └─ ImageView  #@id/iv_current_day
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 2 | `FrameLayout` | `android:layout_height` | `@dimen/streak_calendar_day_item_height` |
| 3 | `TextView` | `android:textColor` | `@color/streak_on_primary` |
| 4 | `TextView` | `android:gravity` | `0x00000011` |
| 5 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 6 | `TextView` | `android:id` | `@id/tv_day` |
| 7 | `TextView` | `android:layout_width` | `@dimen/streak_calendar_day_size` |
| 8 | `TextView` | `android:layout_height` | `@dimen/streak_calendar_day_size` |
| 9 | `TextView` | `style` | `@style/TextTitle2` |
| 10 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 11 | `ImageView` | `android:id` | `@id/iv_day` |
| 12 | `ImageView` | `android:padding` | `@dimen/spacing_xs` |
| 13 | `ImageView` | `android:layout_width` | `@dimen/streak_calendar_current_day_size` |
| 14 | `ImageView` | `android:layout_height` | `@dimen/streak_calendar_current_day_size` |
| 15 | `ImageView` | `app:tint` | `@color/streak_on_primary` |
| 16 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 17 | `ImageView` | `android:id` | `@id/iv_current_day` |
| 18 | `ImageView` | `android:layout_width` | `@dimen/streak_calendar_current_day_size` |
| 19 | `ImageView` | `android:layout_height` | `@dimen/streak_calendar_current_day_size` |
| 20 | `ImageView` | `app:srcCompat` | `@drawable/streak_day_current_background` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/streak_on_primary` | `#FFFFFFFF` / `#FF252746` (night) |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/streak_calendar_current_day_size` | `40.000000dip` / `50.000000dip` (sw600dp) |
| `@dimen/streak_calendar_day_item_height` | `44.000000dip` / `54.000000dip` (sw600dp) |
| `@dimen/streak_calendar_day_size` | `36.000000dip` / `44.000000dip` (sw600dp) |
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_current_day
@id/iv_day
@id/tv_day
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="@dimen/streak_calendar_day_item_height">
  <TextView android:textColor="@color/streak_on_primary" android:gravity="0x00000011" android:layout_gravity="0x00000011" android:id="@id/tv_day" android:layout_width="@dimen/streak_calendar_day_size" android:layout_height="@dimen/streak_calendar_day_size" style="@style/TextTitle2"/>
  <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_day" android:padding="@dimen/spacing_xs" android:layout_width="@dimen/streak_calendar_current_day_size" android:layout_height="@dimen/streak_calendar_current_day_size" app:tint="@color/streak_on_primary"/>
  <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_current_day" android:layout_width="@dimen/streak_calendar_current_day_size" android:layout_height="@dimen/streak_calendar_current_day_size" app:srcCompat="@drawable/streak_day_current_background"/>
</FrameLayout>
```
