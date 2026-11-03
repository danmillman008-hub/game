# پروندهٔ لایه — `res/layout/lesson_interaction_selection_item_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/lesson_interaction_selection_item_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/lesson_interaction_selection_item_layout.xml`](../../SOURCE/res/layout/lesson_interaction_selection_item_layout.xml) |
| SHA-256 دیکد | `30277b5d02c9475869903157f18f5948e173f7d60a2287ff159c299d18b1d2ca` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView
   └─ TextView  #@id/item_name
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 2 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.cardview.widget.CardView` | `android:foreground` | `?attr/selectableItemBackground` |
| 4 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius` |
| 5 | `androidx.cardview.widget.CardView` | `app:elevation` | `@dimen/cardview_elevation` |
| 6 | `TextView` | `android:gravity` | `0x00000011` |
| 7 | `TextView` | `android:id` | `@id/item_name` |
| 8 | `TextView` | `android:paddingTop` | `14.000000dip` |
| 9 | `TextView` | `android:paddingBottom` | `14.000000dip` |
| 10 | `TextView` | `android:layout_width` | `wrap_content` |
| 11 | `TextView` | `android:layout_height` | `wrap_content` |
| 12 | `TextView` | `android:singleLine` | `false` |
| 13 | `TextView` | `android:paddingStart` | `18.000000dip` |
| 14 | `TextView` | `android:paddingEnd` | `18.000000dip` |
| 15 | `TextView` | `style` | `@style/TextSelectionViewItem` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/cardview_corner_radius` | `6.000000dip` |
| `@dimen/cardview_elevation` | `1.500000dip` |
| `@style/TextSelectionViewItem` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:typeface', 'attr_id': '0x01010096', 'value': '3', 'value_type': 'int_dec'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': '@font/aeonik_mono', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': '@font/aeonik_mono', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/item_name
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
<androidx.cardview.widget.CardView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackground" app:cardCornerRadius="@dimen/cardview_corner_radius" app:elevation="@dimen/cardview_elevation">
  <TextView android:gravity="0x00000011" android:id="@id/item_name" android:paddingTop="14.000000dip" android:paddingBottom="14.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="false" android:paddingStart="18.000000dip" android:paddingEnd="18.000000dip" style="@style/TextSelectionViewItem"/>
</androidx.cardview.widget.CardView>
```
