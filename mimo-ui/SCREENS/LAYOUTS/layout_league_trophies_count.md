# پروندهٔ لایه — `res/layout/league_trophies_count.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/league_trophies_count.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/league_trophies_count.xml`](../../SOURCE/res/layout/league_trophies_count.xml) |
| SHA-256 دیکد | `3d6f4687fd6757abff444abc56aea5b05a7ec0c1bac8622789300f1f543b9ad5` |
| ریشه | `LinearLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 11 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 17 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ ImageView  #@id/iv_league
   ├─ Space  #@id/v_league_spacing
   ├─ LinearLayout  #@id/layout_first_place
   │  ├─ ImageView  #@id/iv_first_place
   │  └─ TextView  #@id/tv_first_place
   ├─ LinearLayout  #@id/layout_second_place
   │  ├─ ImageView  #@id/iv_second_place
   │  └─ TextView  #@id/tv_second_place
   └─ LinearLayout  #@id/layout_third_place
      ├─ ImageView  #@id/iv_third_place
      └─ TextView  #@id/tv_third_place
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:paddingTop` | `@dimen/spacing_l` |
| 3 | `LinearLayout` | `android:paddingBottom` | `@dimen/spacing_l` |
| 4 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 5 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 6 | `LinearLayout` | `android:paddingStart` | `@dimen/spacing_m` |
| 7 | `LinearLayout` | `android:paddingEnd` | `@dimen/spacing_m` |
| 8 | `ImageView` | `android:id` | `@id/iv_league` |
| 9 | `ImageView` | `android:layout_width` | `@dimen/trophies_icon_size` |
| 10 | `ImageView` | `android:layout_height` | `@dimen/trophies_icon_size` |
| 11 | `Space` | `android:id` | `@id/v_league_spacing` |
| 12 | `Space` | `android:layout_width` | `@dimen/spacing_l` |
| 13 | `Space` | `android:layout_height` | `wrap_content` |
| 14 | `LinearLayout` | `android:orientation` | `horizontal` |
| 15 | `LinearLayout` | `android:id` | `@id/layout_first_place` |
| 16 | `LinearLayout` | `android:visibility` | `gone` |
| 17 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 18 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 19 | `LinearLayout` | `android:paddingEnd` | `@dimen/spacing_l` |
| 20 | `ImageView` | `android:id` | `@id/iv_first_place` |
| 21 | `ImageView` | `android:layout_width` | `@dimen/trophies_icon_size` |
| 22 | `ImageView` | `android:layout_height` | `@dimen/trophies_icon_size` |
| 23 | `TextView` | `android:textColor` | `@color/text_primary` |
| 24 | `TextView` | `android:gravity` | `0x00000011` |
| 25 | `TextView` | `android:id` | `@id/tv_first_place` |
| 26 | `TextView` | `android:layout_width` | `wrap_content` |
| 27 | `TextView` | `android:layout_height` | `match_parent` |
| 28 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xs` |
| 29 | `TextView` | `style` | `@style/TextH4` |
| 30 | `LinearLayout` | `android:orientation` | `horizontal` |
| 31 | `LinearLayout` | `android:id` | `@id/layout_second_place` |
| 32 | `LinearLayout` | `android:visibility` | `gone` |
| 33 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 34 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 35 | `LinearLayout` | `android:paddingEnd` | `@dimen/spacing_l` |
| 36 | `ImageView` | `android:id` | `@id/iv_second_place` |
| 37 | `ImageView` | `android:layout_width` | `@dimen/trophies_icon_size` |
| 38 | `ImageView` | `android:layout_height` | `@dimen/trophies_icon_size` |
| 39 | `TextView` | `android:textColor` | `@color/text_primary` |
| 40 | `TextView` | `android:gravity` | `0x00000011` |
| 41 | `TextView` | `android:id` | `@id/tv_second_place` |
| 42 | `TextView` | `android:layout_width` | `wrap_content` |
| 43 | `TextView` | `android:layout_height` | `match_parent` |
| 44 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xs` |
| 45 | `TextView` | `style` | `@style/TextH4` |
| 46 | `LinearLayout` | `android:id` | `@id/layout_third_place` |
| 47 | `LinearLayout` | `android:visibility` | `gone` |
| 48 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 49 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 50 | `ImageView` | `android:id` | `@id/iv_third_place` |
| 51 | `ImageView` | `android:layout_width` | `@dimen/trophies_icon_size` |
| 52 | `ImageView` | `android:layout_height` | `@dimen/trophies_icon_size` |
| 53 | `TextView` | `android:textColor` | `@color/text_primary` |
| 54 | `TextView` | `android:gravity` | `0x00000011` |
| 55 | `TextView` | `android:id` | `@id/tv_third_place` |
| 56 | `TextView` | `android:layout_width` | `wrap_content` |
| 57 | `TextView` | `android:layout_height` | `match_parent` |
| 58 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xs` |
| 59 | `TextView` | `style` | `@style/TextH4` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/trophies_icon_size` | `40.000000dip` |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_first_place
@id/iv_league
@id/iv_second_place
@id/iv_third_place
@id/layout_first_place
@id/layout_second_place
@id/layout_third_place
@id/tv_first_place
@id/tv_second_place
@id/tv_third_place
@id/v_league_spacing
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:paddingTop="@dimen/spacing_l" android:paddingBottom="@dimen/spacing_l" android:layout_width="match_parent" android:layout_height="wrap_content" android:paddingStart="@dimen/spacing_m" android:paddingEnd="@dimen/spacing_m">
  <ImageView android:id="@id/iv_league" android:layout_width="@dimen/trophies_icon_size" android:layout_height="@dimen/trophies_icon_size"/>
  <Space android:id="@id/v_league_spacing" android:layout_width="@dimen/spacing_l" android:layout_height="wrap_content"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/layout_first_place" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:paddingEnd="@dimen/spacing_l">
    <ImageView android:id="@id/iv_first_place" android:layout_width="@dimen/trophies_icon_size" android:layout_height="@dimen/trophies_icon_size"/>
    <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_first_place" android:layout_width="wrap_content" android:layout_height="match_parent" android:layout_marginStart="@dimen/spacing_xs" style="@style/TextH4"/>
  </LinearLayout>
  <LinearLayout android:orientation="horizontal" android:id="@id/layout_second_place" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:paddingEnd="@dimen/spacing_l">
    <ImageView android:id="@id/iv_second_place" android:layout_width="@dimen/trophies_icon_size" android:layout_height="@dimen/trophies_icon_size"/>
    <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_second_place" android:layout_width="wrap_content" android:layout_height="match_parent" android:layout_marginStart="@dimen/spacing_xs" style="@style/TextH4"/>
  </LinearLayout>
  <LinearLayout android:id="@id/layout_third_place" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content">
    <ImageView android:id="@id/iv_third_place" android:layout_width="@dimen/trophies_icon_size" android:layout_height="@dimen/trophies_icon_size"/>
    <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_third_place" android:layout_width="wrap_content" android:layout_height="match_parent" android:layout_marginStart="@dimen/spacing_xs" style="@style/TextH4"/>
  </LinearLayout>
</LinearLayout>
```
