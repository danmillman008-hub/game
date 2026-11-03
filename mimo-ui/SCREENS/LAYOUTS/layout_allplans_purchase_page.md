# پروندهٔ لایه — `res/layout/allplans_purchase_page.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/allplans_purchase_page.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/allplans_purchase_page.xml`](../../SOURCE/res/layout/allplans_purchase_page.xml) |
| SHA-256 دیکد | `eefa76a9717e13d0e9f4a7950ffd2f90bea12b0e8d305e1c201e4ccd0d95c45c` |
| ریشه | `LinearLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ FrameLayout  #@id/image_content
   │  ├─ ImageView  #@id/iv_in_app_page_illustration
   │  └─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rive_in_app_page_animation
   ├─ TextView  #@id/tv_in_app_page_title
   └─ TextView  #@id/tv_in_app_page_description
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `LinearLayout` | `android:layout_marginVertical` | `16.000000dip` |
| 6 | `LinearLayout` | `android:paddingHorizontal` | `@dimen/view_pager_horizontal_padding` |
| 7 | `FrameLayout` | `android:id` | `@id/image_content` |
| 8 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 9 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 10 | `FrameLayout` | `android:layout_marginStart` | `56.000000dip` |
| 11 | `FrameLayout` | `android:layout_marginEnd` | `60.000000dip` |
| 12 | `ImageView` | `android:id` | `@id/iv_in_app_page_illustration` |
| 13 | `ImageView` | `android:layout_width` | `wrap_content` |
| 14 | `ImageView` | `android:layout_height` | `@dimen/allplans_image_height` |
| 15 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_gravity` | `0x00000001` |
| 16 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/rive_in_app_page_animation` |
| 17 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `wrap_content` |
| 18 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `160.000000dip` |
| 19 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveLoop` | `1` |
| 20 | `TextView` | `android:textColor` | `@color/text_primary` |
| 21 | `TextView` | `android:gravity` | `0x00000001` |
| 22 | `TextView` | `android:id` | `@id/tv_in_app_page_title` |
| 23 | `TextView` | `android:layout_width` | `match_parent` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 26 | `TextView` | `style` | `@style/TextH1` |
| 27 | `TextView` | `android:textColor` | `@color/text_weak` |
| 28 | `TextView` | `android:gravity` | `0x00000001` |
| 29 | `TextView` | `android:id` | `@id/tv_in_app_page_description` |
| 30 | `TextView` | `android:layout_width` | `match_parent` |
| 31 | `TextView` | `android:layout_height` | `wrap_content` |
| 32 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 33 | `TextView` | `android:lines` | `3` |
| 34 | `TextView` | `style` | `@style/TextP1` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/allplans_image_height` | `140.000000dip` / `100.000000dip` (sw600dp-land) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/view_pager_horizontal_padding` | `24.000000dip` / `50.000000dip` (w550dp-h650dp) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/image_content
@id/iv_in_app_page_illustration
@id/rive_in_app_page_animation
@id/tv_in_app_page_description
@id/tv_in_app_page_title
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00000011" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent" android:layout_marginVertical="16.000000dip" android:paddingHorizontal="@dimen/view_pager_horizontal_padding">
  <FrameLayout android:id="@id/image_content" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginStart="56.000000dip" android:layout_marginEnd="60.000000dip">
    <ImageView android:id="@id/iv_in_app_page_illustration" android:layout_width="wrap_content" android:layout_height="@dimen/allplans_image_height"/>
    <app.rive.runtime.kotlin.RiveAnimationView android:layout_gravity="0x00000001" android:id="@id/rive_in_app_page_animation" android:layout_width="wrap_content" android:layout_height="160.000000dip" app:riveLoop="1"/>
  </FrameLayout>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000001" android:id="@id/tv_in_app_page_title" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000001" android:id="@id/tv_in_app_page_description" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:lines="3" style="@style/TextP1"/>
</LinearLayout>
```
