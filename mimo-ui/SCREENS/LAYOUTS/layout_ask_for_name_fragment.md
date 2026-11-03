# پروندهٔ لایه — `res/layout/ask_for_name_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/ask_for_name_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/ask_for_name_fragment.xml`](../../SOURCE/res/layout/ask_for_name_fragment.xml) |
| SHA-256 دیکد | `06cdecb43e96ae768d5118c070c91b3b9b4720022debabfb2789eaf558d48044` |
| ریشه | `FrameLayout` |
| تعداد گره | 9 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/root_name_code_playground
   └─ androidx.cardview.widget.CardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_ask_for_name_title
         ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_ask_for_name
         │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_ask_for_name
         │     └─ requestFocus
         ├─ TextView  #@id/tv_name_code_chars
         └─ androidx.compose.ui.platform.ComposeView  #@id/btn_ask_for_name_enter
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/root_name_code_playground` |
| 2 | `FrameLayout` | `android:focusable` | `true` |
| 3 | `FrameLayout` | `android:clickable` | `true` |
| 4 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 5 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 6 | `androidx.cardview.widget.CardView` | `android:focusable` | `true` |
| 7 | `androidx.cardview.widget.CardView` | `android:clickable` | `true` |
| 8 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 9 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 10 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/background_secondary` |
| 11 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 14 | `TextView` | `android:textColor` | `@color/text_primary` |
| 15 | `TextView` | `android:id` | `@id/tv_ask_for_name_title` |
| 16 | `TextView` | `android:layout_width` | `wrap_content` |
| 17 | `TextView` | `android:layout_height` | `wrap_content` |
| 18 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 19 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 20 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 21 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 22 | `TextView` | `style` | `@style/TextLabel1` |
| 23 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_ask_for_name` |
| 24 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 25 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 26 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 27 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 28 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 29 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 30 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 31 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_ask_for_name_title` |
| 32 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 33 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_ask_for_name` |
| 34 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 35 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 36 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 37 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000061` |
| 38 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x00000006` |
| 39 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 40 | `TextView` | `android:textColor` | `@color/text_weak` |
| 41 | `TextView` | `android:id` | `@id/tv_name_code_chars` |
| 42 | `TextView` | `android:layout_width` | `wrap_content` |
| 43 | `TextView` | `android:layout_height` | `wrap_content` |
| 44 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 45 | `TextView` | `android:text` | `@string/name_code_playground_characters` |
| 46 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 47 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 48 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/til_ask_for_name` |
| 49 | `TextView` | `style` | `@style/TextP3` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_ask_for_name_enter` |
| 51 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 52 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 53 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 54 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 55 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 56 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 57 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 58 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 59 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_name_code_chars` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@string/name_code_playground_characters` | `0/40 characters` / `0/40 Zeichen` (de) / `0/40 caracteres` (es) / `0/40 caractères` (fr) / `0/40 karakter` (in) / `0/40 caratteri` (it) / `0/40 znaków` (pl) / `0/40 caracteres` (pt-rBR) / `0/40 символов` (ru) / `0/40 karakter` (tr) |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_ask_for_name_enter
@id/et_ask_for_name
@id/root_name_code_playground
@id/til_ask_for_name
@id/tv_ask_for_name_title
@id/tv_name_code_chars
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.common.AskForNameFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/root_name_code_playground" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="wrap_content">
  <androidx.cardview.widget.CardView android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:cardBackgroundColor="@color/background_secondary" app:cardCornerRadius="@dimen/cardview_corner_radius_large">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="match_parent">
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_ask_for_name_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextLabel1"/>
      <com.google.android.material.textfield.TextInputLayout android:id="@id/til_ask_for_name" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_ask_for_name_title" style="@style/MaterialEditTextLayout">
        <com.google.android.material.textfield.TextInputEditText android:id="@id/et_ask_for_name" android:layout_width="match_parent" android:layout_height="wrap_content" android:ems="10" android:inputType="0x00000061" android:imeOptions="0x00000006" style="@style/MaterialEditText">
          <requestFocus/>
        </com.google.android.material.textfield.TextInputEditText>
      </com.google.android.material.textfield.TextInputLayout>
      <TextView android:textColor="@color/text_weak" android:id="@id/tv_name_code_chars" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/name_code_playground_characters" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/til_ask_for_name" style="@style/TextP3"/>
      <androidx.compose.ui.platform.ComposeView android:id="@id/btn_ask_for_name_enter" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:layout_marginBottom="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_name_code_chars"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </androidx.cardview.widget.CardView>
</FrameLayout>
```
