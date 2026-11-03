# پروندهٔ لایه — `res/layout/code_playground_template_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/code_playground_template_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/code_playground_template_item.xml`](../../SOURCE/res/layout/code_playground_template_item.xml) |
| SHA-256 دیکد | `88ee8c9d22837888f8858fa6e25bb3c0bc5b6157b0982202a1f95a7d45c6da40` |
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
      ├─ ImageView  #@id/iv_code_playground_template
      ├─ TextView  #@id/tv_code_playground_template_title
      └─ TextView  #@id/tv_code_playground_template_description
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 2 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.cardview.widget.CardView` | `android:foreground` | `?attr/selectableItemBackground` |
| 4 | `androidx.cardview.widget.CardView` | `android:minHeight` | `100.000000dip` |
| 5 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 6 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 7 | `androidx.cardview.widget.CardView` | `app:cardElevation` | `2.000000dip` |
| 8 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 10 | `ImageView` | `android:id` | `@id/iv_code_playground_template` |
| 11 | `ImageView` | `android:layout_width` | `104.000000dip` |
| 12 | `ImageView` | `android:layout_height` | `88.000000dip` |
| 13 | `ImageView` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 14 | `ImageView` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 15 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 16 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 17 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 18 | `TextView` | `android:textColor` | `@color/text_primary` |
| 19 | `TextView` | `android:id` | `@id/tv_code_playground_template_title` |
| 20 | `TextView` | `android:layout_width` | `wrap_content` |
| 21 | `TextView` | `android:layout_height` | `wrap_content` |
| 22 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 23 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 24 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_code_playground_template` |
| 25 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 26 | `TextView` | `style` | `@style/TextTitle2` |
| 27 | `TextView` | `android:textColor` | `@color/text_weak` |
| 28 | `TextView` | `android:id` | `@id/tv_code_playground_template_description` |
| 29 | `TextView` | `android:layout_width` | `0.000000dip` |
| 30 | `TextView` | `android:layout_height` | `wrap_content` |
| 31 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 32 | `TextView` | `android:layout_marginVertical` | `@dimen/spacing_s` |
| 33 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 35 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/tv_code_playground_template_title` |
| 36 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_code_playground_template_title` |
| 37 | `TextView` | `app:layout_constraintVertical_bias` | `0.000000` |
| 38 | `TextView` | `app:layout_constraintWidth_default` | `1` |
| 39 | `TextView` | `style` | `@style/TextP3` |

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
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_code_playground_template
@id/tv_code_playground_template_description
@id/tv_code_playground_template_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.codeplayground.CodePlaygroundActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackground" android:minHeight="100.000000dip" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large" app:cardElevation="2.000000dip">
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
    <ImageView android:id="@id/iv_code_playground_template" android:layout_width="104.000000dip" android:layout_height="88.000000dip" android:layout_marginHorizontal="@dimen/spacing_xs" android:layout_marginVertical="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_code_playground_template_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toEndOf="@id/iv_code_playground_template" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle2"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_code_playground_template_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_m" android:layout_marginVertical="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="@id/tv_code_playground_template_title" app:layout_constraintTop_toBottomOf="@id/tv_code_playground_template_title" app:layout_constraintVertical_bias="0.000000" app:layout_constraintWidth_default="1" style="@style/TextP3"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.cardview.widget.CardView>
```
