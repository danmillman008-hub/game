# پروندهٔ لایه — `res/layout/saved_code_item_public.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/saved_code_item_public.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/saved_code_item_public.xml`](../../SOURCE/res/layout/saved_code_item_public.xml) |
| SHA-256 دیکد | `8959766c6f9d74fd15b9933fc44fa76213216240e6b71db876ceaa066575faf9` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 5 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ LinearLayout  #@id/container_public_saved_code_item_lang_icons
      ├─ TextView  #@id/tv_public_saved_code_item_title
      └─ TextView  #@id/tv_public_saved_code_item_url
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 2 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.cardview.widget.CardView` | `android:layout_marginBottom` | `@dimen/spacing_s` |
| 4 | `androidx.cardview.widget.CardView` | `android:foreground` | `?attr/selectableItemBackground` |
| 5 | `androidx.cardview.widget.CardView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 6 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 7 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 8 | `androidx.cardview.widget.CardView` | `app:cardElevation` | `2.000000dip` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 11 | `LinearLayout` | `android:orientation` | `horizontal` |
| 12 | `LinearLayout` | `android:id` | `@id/container_public_saved_code_item_lang_icons` |
| 13 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 14 | `LinearLayout` | `android:layout_height` | `24.000000dip` |
| 15 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 16 | `LinearLayout` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 17 | `LinearLayout` | `android:layout_marginEnd` | `@dimen/spacing_xs` |
| 18 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `LinearLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 21 | `TextView` | `android:textColor` | `@color/text_primary` |
| 22 | `TextView` | `android:id` | `@id/tv_public_saved_code_item_title` |
| 23 | `TextView` | `android:layout_width` | `0.000000dip` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 26 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 27 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 28 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 29 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/container_public_saved_code_item_lang_icons` |
| 30 | `TextView` | `style` | `@style/TextTitle1` |
| 31 | `TextView` | `android:textColor` | `@color/text_weak` |
| 32 | `TextView` | `android:id` | `@id/tv_public_saved_code_item_url` |
| 33 | `TextView` | `android:layout_width` | `0.000000dip` |
| 34 | `TextView` | `android:layout_height` | `wrap_content` |
| 35 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 36 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_s` |
| 37 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 38 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 39 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 40 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 41 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_public_saved_code_item_title` |
| 42 | `TextView` | `style` | `@style/TextP3` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/card_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/container_public_saved_code_item_lang_icons
@id/tv_public_saved_code_item_title
@id/tv_public_saved_code_item_url
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
<androidx.cardview.widget.CardView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_s" android:foreground="?attr/selectableItemBackground" android:layout_marginHorizontal="@dimen/spacing_m" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large" app:cardElevation="2.000000dip">
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
    <LinearLayout android:orientation="horizontal" android:id="@id/container_public_saved_code_item_lang_icons" android:layout_width="0.000000dip" android:layout_height="24.000000dip" android:layout_marginTop="@dimen/spacing_s" android:layout_marginStart="@dimen/spacing_s" android:layout_marginEnd="@dimen/spacing_xs" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_public_saved_code_item_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginHorizontal="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/container_public_saved_code_item_lang_icons" style="@style/TextTitle1"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_public_saved_code_item_url" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginBottom="@dimen/spacing_s" android:layout_marginHorizontal="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_public_saved_code_item_title" style="@style/TextP3"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.cardview.widget.CardView>
```
