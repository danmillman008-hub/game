# پروندهٔ لایه — `res/layout/subscription_podium_button.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/subscription_podium_button.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/subscription_podium_button.xml`](../../SOURCE/res/layout/subscription_podium_button.xml) |
| SHA-256 دیکد | `704e44705cc324c4e308c2e04b625c21ae4a78c5acd12b12d3b02175326f765f` |
| ریشه | `merge` |
| تعداد گره | 14 |
| تعداد شناسه | 12 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 32 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ TextView  #@id/tv_in_app_button_free_trial
   └─ com.google.android.material.card.MaterialCardView  #@id/cv_in_app_button
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_in_app_button_podium_big_title
         ├─ View  #@id/view_iap_separator_1
         ├─ TextView  #@id/tv_iap_button_podium_big_save_percent
         ├─ LinearLayout  #@id/layout_iap_podium_big_countdown
         │  ├─ TextView  #@id/tv_iap_countdown_promotion_percentage
         │  └─ TextView  #@id/tv_iap_countdown_timer
         ├─ TextView  #@id/tv_in_app_button_podium_big_price
         ├─ TextView  #@id/tv_in_app_button_podium_big_period
         ├─ View  #@id/view_iap_separator_2
         └─ TextView  #@id/tv_in_app_button_podium_billing
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:textColor` | `@color/primary_on_primary` |
| 2 | `TextView` | `android:gravity` | `0x00000011` |
| 3 | `TextView` | `android:id` | `@id/tv_in_app_button_free_trial` |
| 4 | `TextView` | `android:visibility` | `gone` |
| 5 | `TextView` | `android:layout_width` | `match_parent` |
| 6 | `TextView` | `android:layout_height` | `wrap_content` |
| 7 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxs` |
| 8 | `TextView` | `android:textAllCaps` | `true` |
| 9 | `TextView` | `android:paddingVertical` | `@dimen/spacing_xs` |
| 10 | `TextView` | `style` | `@style/TextLabel3` |
| 11 | `com.google.android.material.card.MaterialCardView` | `android:id` | `@id/cv_in_app_button` |
| 12 | `com.google.android.material.card.MaterialCardView` | `android:focusable` | `true` |
| 13 | `com.google.android.material.card.MaterialCardView` | `android:clickable` | `true` |
| 14 | `com.google.android.material.card.MaterialCardView` | `android:layout_width` | `match_parent` |
| 15 | `com.google.android.material.card.MaterialCardView` | `android:layout_height` | `wrap_content` |
| 16 | `com.google.android.material.card.MaterialCardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 17 | `com.google.android.material.card.MaterialCardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 18 | `com.google.android.material.card.MaterialCardView` | `app:cardUseCompatPadding` | `true` |
| 19 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 20 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 21 | `TextView` | `android:textColor` | `@color/text_primary` |
| 22 | `TextView` | `android:gravity` | `0x00000011` |
| 23 | `TextView` | `android:id` | `@id/tv_in_app_button_podium_big_title` |
| 24 | `TextView` | `android:layout_width` | `match_parent` |
| 25 | `TextView` | `android:layout_height` | `wrap_content` |
| 26 | `TextView` | `android:textAllCaps` | `true` |
| 27 | `TextView` | `android:paddingVertical` | `@dimen/spacing_s` |
| 28 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 29 | `TextView` | `style` | `@style/TextLabel1` |
| 30 | `View` | `android:id` | `@id/view_iap_separator_1` |
| 31 | `View` | `android:background` | `@color/line_secondary` |
| 32 | `View` | `android:layout_width` | `match_parent` |
| 33 | `View` | `android:layout_height` | `1.000000dip` |
| 34 | `View` | `app:layout_constraintTop_toBottomOf` | `@id/tv_in_app_button_podium_big_title` |
| 35 | `TextView` | `android:id` | `@id/tv_iap_button_podium_big_save_percent` |
| 36 | `TextView` | `android:background` | `@drawable/in_app_button_background_save_percent` |
| 37 | `TextView` | `android:visibility` | `gone` |
| 38 | `TextView` | `android:layout_width` | `wrap_content` |
| 39 | `TextView` | `android:layout_height` | `wrap_content` |
| 40 | `TextView` | `android:textAllCaps` | `true` |
| 41 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/view_iap_separator_1` |
| 42 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/view_iap_separator_1` |
| 43 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/view_iap_separator_1` |
| 44 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/view_iap_separator_1` |
| 45 | `TextView` | `style` | `@style/TextInAppPurchaseSales` |
| 46 | `LinearLayout` | `android:orientation` | `horizontal` |
| 47 | `LinearLayout` | `android:id` | `@id/layout_iap_podium_big_countdown` |
| 48 | `LinearLayout` | `android:visibility` | `gone` |
| 49 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 50 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 51 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `@id/view_iap_separator_1` |
| 52 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `@id/view_iap_separator_1` |
| 53 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `@id/view_iap_separator_1` |
| 54 | `LinearLayout` | `app:layout_constraintTop_toTopOf` | `@id/view_iap_separator_1` |
| 55 | `TextView` | `android:id` | `@id/tv_iap_countdown_promotion_percentage` |
| 56 | `TextView` | `android:background` | `@drawable/in_app_button_background_countdown_left` |
| 57 | `TextView` | `android:layout_width` | `wrap_content` |
| 58 | `TextView` | `android:layout_height` | `wrap_content` |
| 59 | `TextView` | `style` | `@style/TextInAppPurchaseSales` |
| 60 | `TextView` | `android:id` | `@id/tv_iap_countdown_timer` |
| 61 | `TextView` | `android:background` | `@drawable/in_app_button_background_countdown_right` |
| 62 | `TextView` | `android:layout_width` | `@dimen/in_app_purchase_countdown_width` |
| 63 | `TextView` | `android:layout_height` | `wrap_content` |
| 64 | `TextView` | `style` | `@style/TextInAppPurchaseSales` |
| 65 | `TextView` | `android:textColor` | `@color/text_primary` |
| 66 | `TextView` | `android:gravity` | `0x00000011` |
| 67 | `TextView` | `android:id` | `@id/tv_in_app_button_podium_big_price` |
| 68 | `TextView` | `android:layout_width` | `match_parent` |
| 69 | `TextView` | `android:layout_height` | `wrap_content` |
| 70 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 71 | `TextView` | `android:lines` | `1` |
| 72 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/view_iap_separator_1` |
| 73 | `TextView` | `style` | `@style/TextH1` |
| 74 | `TextView` | `android:textColor` | `@color/text_weak` |
| 75 | `TextView` | `android:gravity` | `0x00000011` |
| 76 | `TextView` | `android:id` | `@id/tv_in_app_button_podium_big_period` |
| 77 | `TextView` | `android:paddingBottom` | `@dimen/spacing_s` |
| 78 | `TextView` | `android:layout_width` | `match_parent` |
| 79 | `TextView` | `android:layout_height` | `wrap_content` |
| 80 | `TextView` | `android:layout_marginTop` | `2.000000dip` |
| 81 | `TextView` | `android:lines` | `1` |
| 82 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_in_app_button_podium_big_price` |
| 83 | `TextView` | `style` | `@style/TextP2` |
| 84 | `View` | `android:id` | `@id/view_iap_separator_2` |
| 85 | `View` | `android:background` | `@color/line_secondary` |
| 86 | `View` | `android:layout_width` | `match_parent` |
| 87 | `View` | `android:layout_height` | `1.000000dip` |
| 88 | `View` | `app:layout_constraintTop_toBottomOf` | `@id/tv_in_app_button_podium_big_period` |
| 89 | `TextView` | `android:textColor` | `@color/text_weak` |
| 90 | `TextView` | `android:gravity` | `0x00000011` |
| 91 | `TextView` | `android:id` | `@id/tv_in_app_button_podium_billing` |
| 92 | `TextView` | `android:paddingBottom` | `@dimen/spacing_m` |
| 93 | `TextView` | `android:layout_width` | `match_parent` |
| 94 | `TextView` | `android:layout_height` | `wrap_content` |
| 95 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 96 | `TextView` | `android:lines` | `1` |
| 97 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/view_iap_separator_2` |
| 98 | `TextView` | `style` | `@style/TextP4` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/card_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/line_secondary` | `#FFE4E6F1` / `#FF4A4D85` (night) |
| `@color/primary_on_primary` | `#FFFFFFFF` |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@dimen/in_app_purchase_countdown_width` | `75.000000dip` / `100.000000dip` (sw600dp) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextInAppPurchaseSales` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_reversed', 'value_type': 'reference'}, {'attr': 'android:paddingTop', 'attr_id': '0x010100D7', 'value': '2.000000dip', 'value_type': 'dimension'}, {'attr': 'android:paddingBottom', 'attr_id': '0x010100D9', 'value': '2.000000dip', 'value_type': 'dimension'}, {'attr': 'android:lines', 'attr_id': '0x01010154', 'value': '1', 'value_type': 'int_dec'}, {'attr': 'android:paddingStart', 'attr_id': '0x010103B3', 'value': '8.000000dip', 'value_type': 'dimension'}, {'attr': 'android:paddingEnd', 'attr_id': '0x010103B4', 'value': '8.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/cv_in_app_button
@id/layout_iap_podium_big_countdown
@id/tv_iap_button_podium_big_save_percent
@id/tv_iap_countdown_promotion_percentage
@id/tv_iap_countdown_timer
@id/tv_in_app_button_free_trial
@id/tv_in_app_button_podium_big_period
@id/tv_in_app_button_podium_big_price
@id/tv_in_app_button_podium_big_title
@id/tv_in_app_button_podium_billing
@id/view_iap_separator_1
@id/view_iap_separator_2
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
<merge xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android">
  <TextView android:textColor="@color/primary_on_primary" android:gravity="0x00000011" android:id="@id/tv_in_app_button_free_trial" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxs" android:textAllCaps="true" android:paddingVertical="@dimen/spacing_xs" style="@style/TextLabel3"/>
  <com.google.android.material.card.MaterialCardView android:id="@id/cv_in_app_button" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large" app:cardUseCompatPadding="true">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
      <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_in_app_button_podium_big_title" android:layout_width="match_parent" android:layout_height="wrap_content" android:textAllCaps="true" android:paddingVertical="@dimen/spacing_s" app:layout_constraintTop_toTopOf="0" style="@style/TextLabel1"/>
      <View android:id="@id/view_iap_separator_1" android:background="@color/line_secondary" android:layout_width="match_parent" android:layout_height="1.000000dip" app:layout_constraintTop_toBottomOf="@id/tv_in_app_button_podium_big_title"/>
      <TextView android:id="@id/tv_iap_button_podium_big_save_percent" android:background="@drawable/in_app_button_background_save_percent" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textAllCaps="true" app:layout_constraintBottom_toBottomOf="@id/view_iap_separator_1" app:layout_constraintEnd_toEndOf="@id/view_iap_separator_1" app:layout_constraintStart_toStartOf="@id/view_iap_separator_1" app:layout_constraintTop_toTopOf="@id/view_iap_separator_1" style="@style/TextInAppPurchaseSales"/>
      <LinearLayout android:orientation="horizontal" android:id="@id/layout_iap_podium_big_countdown" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="@id/view_iap_separator_1" app:layout_constraintEnd_toEndOf="@id/view_iap_separator_1" app:layout_constraintStart_toStartOf="@id/view_iap_separator_1" app:layout_constraintTop_toTopOf="@id/view_iap_separator_1">
        <TextView android:id="@id/tv_iap_countdown_promotion_percentage" android:background="@drawable/in_app_button_background_countdown_left" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/TextInAppPurchaseSales"/>
        <TextView android:id="@id/tv_iap_countdown_timer" android:background="@drawable/in_app_button_background_countdown_right" android:layout_width="@dimen/in_app_purchase_countdown_width" android:layout_height="wrap_content" style="@style/TextInAppPurchaseSales"/>
      </LinearLayout>
      <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_in_app_button_podium_big_price" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:lines="1" app:layout_constraintTop_toBottomOf="@id/view_iap_separator_1" style="@style/TextH1"/>
      <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_in_app_button_podium_big_period" android:paddingBottom="@dimen/spacing_s" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="2.000000dip" android:lines="1" app:layout_constraintTop_toBottomOf="@id/tv_in_app_button_podium_big_price" style="@style/TextP2"/>
      <View android:id="@id/view_iap_separator_2" android:background="@color/line_secondary" android:layout_width="match_parent" android:layout_height="1.000000dip" app:layout_constraintTop_toBottomOf="@id/tv_in_app_button_podium_big_period"/>
      <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_in_app_button_podium_billing" android:paddingBottom="@dimen/spacing_m" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:lines="1" app:layout_constraintTop_toBottomOf="@id/view_iap_separator_2" style="@style/TextP4"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </com.google.android.material.card.MaterialCardView>
</merge>
```
