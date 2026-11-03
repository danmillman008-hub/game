# پروندهٔ لایه — `res/layout/streak_info_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/streak_info_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/streak_info_layout.xml`](../../SOURCE/res/layout/streak_info_layout.xml) |
| SHA-256 دیکد | `d1c183235ef8cf498a85ff2894b098d8feb4ecb6f6003bd2c7540afe792dd9d1` |
| ریشه | `merge` |
| تعداد گره | 5 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ ImageView  #@id/iv_icon
   └─ LinearLayout
      ├─ TextView  #@id/tv_title
      └─ TextView  #@id/tv_subtitle
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ImageView` | `android:id` | `@id/iv_icon` |
| 2 | `ImageView` | `android:layout_width` | `@dimen/icon_size_large_expandable` |
| 3 | `ImageView` | `android:layout_height` | `@dimen/icon_size_large_expandable` |
| 4 | `ImageView` | `android:layout_marginEnd` | `@dimen/spacing_s_expandable` |
| 5 | `LinearLayout` | `android:orientation` | `vertical` |
| 6 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 7 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 8 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 9 | `TextView` | `android:textColor` | `@color/text_primary` |
| 10 | `TextView` | `android:gravity` | `0x00000010` |
| 11 | `TextView` | `android:id` | `@id/tv_title` |
| 12 | `TextView` | `android:layout_width` | `match_parent` |
| 13 | `TextView` | `android:layout_height` | `wrap_content` |
| 14 | `TextView` | `style` | `@style/TextH4` |
| 15 | `TextView` | `android:textColor` | `@color/text_weak` |
| 16 | `TextView` | `android:id` | `@id/tv_subtitle` |
| 17 | `TextView` | `android:layout_width` | `match_parent` |
| 18 | `TextView` | `android:layout_height` | `wrap_content` |
| 19 | `TextView` | `android:textAllCaps` | `true` |
| 20 | `TextView` | `style` | `@style/TextLabel3` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/icon_size_large_expandable` | `24.000000dip` / `32.000000dip` (sw600dp) |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_icon
@id/tv_subtitle
@id/tv_title
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
<merge xmlns:android="http://schemas.android.com/apk/res/android">
  <ImageView android:id="@id/iv_icon" android:layout_width="@dimen/icon_size_large_expandable" android:layout_height="@dimen/icon_size_large_expandable" android:layout_marginEnd="@dimen/spacing_s_expandable"/>
  <LinearLayout android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_weight="1.000000">
    <TextView android:textColor="@color/text_primary" android:gravity="0x00000010" android:id="@id/tv_title" android:layout_width="match_parent" android:layout_height="wrap_content" style="@style/TextH4"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_subtitle" android:layout_width="match_parent" android:layout_height="wrap_content" android:textAllCaps="true" style="@style/TextLabel3"/>
  </LinearLayout>
</merge>
```
