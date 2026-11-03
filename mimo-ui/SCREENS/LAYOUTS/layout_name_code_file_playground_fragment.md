# پروندهٔ لایه — `res/layout/name_code_file_playground_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/name_code_file_playground_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/name_code_file_playground_fragment.xml`](../../SOURCE/res/layout/name_code_file_playground_fragment.xml) |
| SHA-256 دیکد | `6890d0bce68fbe1a48f5bce0961b2b41e36f0af20b866926520669a63b6c4cf6` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 30 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_name_code_file_playground
   └─ androidx.cardview.widget.CardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_name_code_file_header
         ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_name_code_file
         │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_name_code_file
         │     └─ requestFocus
         ├─ TextView  #@id/tv_save_code_name
         ├─ TextView  #@id/tv_name_code_file_chars
         ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_name_code_file_enter
         ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_name_code_cancel
         └─ TextView  #@id/tv_name_code_file_extension
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/root_name_code_file_playground` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/generic_backdrop_color` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:focusable` | `true` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:clickable` | `true` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 7 | `androidx.cardview.widget.CardView` | `android:focusable` | `true` |
| 8 | `androidx.cardview.widget.CardView` | `android:clickable` | `true` |
| 9 | `androidx.cardview.widget.CardView` | `android:layout_width` | `0.000000dip` |
| 10 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 11 | `androidx.cardview.widget.CardView` | `android:layout_marginTop` | `64.000000dip` |
| 12 | `androidx.cardview.widget.CardView` | `android:layout_marginHorizontal` | `@dimen/spacing_xxl` |
| 13 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/background_secondary` |
| 14 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/modal_corner_radius` |
| 15 | `androidx.cardview.widget.CardView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 16 | `androidx.cardview.widget.CardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 17 | `androidx.cardview.widget.CardView` | `app:layout_constraintTop_toTopOf` | `0` |
| 18 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 19 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 20 | `TextView` | `android:textColor` | `@color/text_primary` |
| 21 | `TextView` | `android:id` | `@id/tv_name_code_file_header` |
| 22 | `TextView` | `android:layout_width` | `wrap_content` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 25 | `TextView` | `android:text` | `@string/name_code_file_playground_header` |
| 26 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 29 | `TextView` | `style` | `@style/TextH2` |
| 30 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_name_code_file` |
| 31 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 32 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 33 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 34 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginStart` | `@dimen/spacing_l` |
| 35 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 36 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toStartOf` | `@id/tv_name_code_file_extension` |
| 37 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 38 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_save_code_name` |
| 39 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 40 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_name_code_file` |
| 41 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 42 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 43 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/name_code_playground_hint` |
| 44 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 45 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000061` |
| 46 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x00000006` |
| 47 | `com.google.android.material.textfield.TextInputEditText` | `android:autofillHints` | `@null` |
| 48 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 49 | `TextView` | `android:textColor` | `@color/text_weak` |
| 50 | `TextView` | `android:id` | `@id/tv_save_code_name` |
| 51 | `TextView` | `android:layout_width` | `wrap_content` |
| 52 | `TextView` | `android:layout_height` | `wrap_content` |
| 53 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 54 | `TextView` | `android:text` | `@string/name` |
| 55 | `TextView` | `android:textAllCaps` | `true` |
| 56 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/til_name_code_file` |
| 57 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_name_code_file_header` |
| 58 | `TextView` | `style` | `@style/TextP3` |
| 59 | `TextView` | `android:textColor` | `@color/text_weak` |
| 60 | `TextView` | `android:id` | `@id/tv_name_code_file_chars` |
| 61 | `TextView` | `android:layout_width` | `wrap_content` |
| 62 | `TextView` | `android:layout_height` | `wrap_content` |
| 63 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_xs` |
| 64 | `TextView` | `android:text` | `@string/name_code_playground_characters` |
| 65 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/til_name_code_file` |
| 66 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/til_name_code_file` |
| 67 | `TextView` | `style` | `@style/TextP3` |
| 68 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_name_code_file_enter` |
| 69 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 70 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 71 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 72 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 73 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 74 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/til_name_code_file` |
| 75 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `200.000000dip` |
| 76 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_name_code_cancel` |
| 77 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 78 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 79 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 80 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 81 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 82 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 83 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 84 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/btn_name_code_file_enter` |
| 85 | `TextView` | `android:textColor` | `@color/text_primary` |
| 86 | `TextView` | `android:id` | `@id/tv_name_code_file_extension` |
| 87 | `TextView` | `android:layout_width` | `wrap_content` |
| 88 | `TextView` | `android:layout_height` | `wrap_content` |
| 89 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 90 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/til_name_code_file` |
| 91 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 92 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/til_name_code_file` |
| 93 | `TextView` | `style` | `@style/TextTitle2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/generic_backdrop_color` | `#88000000` |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/modal_corner_radius` | `12.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/name` | `Name` / `Name` (de) / `Nombre` (es) / `Nom` (fr) / `Nama` (in) / `Nome` (it) / `Nazwa` (pl) / `Nome` (pt-rBR) / `Имя` (ru) / `Ad` (tr) |
| `@string/name_code_file_playground_header` | `Name the %s file` / `Gib der %s-Datei einen Namen` (de) / `Nombra el archivo %s` (es) / `Nomme le fichier %s` (fr) / `Beri nama file %s` (in) / `Dai un nome al file %s` (it) / `Nazwij plik %s` (pl) / `Nomeie o arquivo %s` (pt-rBR) / `Назови %s файл` (ru) / `%s dosyasına ad ver` (tr) |
| `@string/name_code_playground_characters` | `0/40 characters` / `0/40 Zeichen` (de) / `0/40 caracteres` (es) / `0/40 caractères` (fr) / `0/40 karakter` (in) / `0/40 caratteri` (it) / `0/40 znaków` (pl) / `0/40 caracteres` (pt-rBR) / `0/40 символов` (ru) / `0/40 karakter` (tr) |
| `@string/name_code_playground_hint` | `My Awesome Demo` / `Meine fantastische Demo` (de) / `Mi fantástica Demo` (es) / `Mon Incroyable Démo` (fr) / `Demo Kerenku` (in) / `La mia demo fantastica` (it) / `Moje super demo` (pl) / `Minha incrível demonstração` (pt-rBR) / `Мое потрясающее демо` (ru) / `Harika Demom` (tr) |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_name_code_cancel
@id/btn_name_code_file_enter
@id/et_name_code_file
@id/root_name_code_file_playground
@id/til_name_code_file
@id/tv_name_code_file_chars
@id/tv_name_code_file_extension
@id/tv_name_code_file_header
@id/tv_save_code_name
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/root_name_code_file_playground" android:background="@color/generic_backdrop_color" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.cardview.widget.CardView android:focusable="true" android:clickable="true" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="64.000000dip" android:layout_marginHorizontal="@dimen/spacing_xxl" app:cardBackgroundColor="@color/background_secondary" app:cardCornerRadius="@dimen/modal_corner_radius" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="match_parent">
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_name_code_file_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/name_code_file_playground_header" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH2"/>
      <com.google.android.material.textfield.TextInputLayout android:id="@id/til_name_code_file" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginStart="@dimen/spacing_l" app:layout_constrainedWidth="true" app:layout_constraintEnd_toStartOf="@id/tv_name_code_file_extension" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_save_code_name" style="@style/MaterialEditTextLayout">
        <com.google.android.material.textfield.TextInputEditText android:id="@id/et_name_code_file" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/name_code_playground_hint" android:ems="10" android:inputType="0x00000061" android:imeOptions="0x00000006" android:autofillHints="@null" style="@style/MaterialEditText">
          <requestFocus/>
        </com.google.android.material.textfield.TextInputEditText>
      </com.google.android.material.textfield.TextInputLayout>
      <TextView android:textColor="@color/text_weak" android:id="@id/tv_save_code_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:text="@string/name" android:textAllCaps="true" app:layout_constraintStart_toStartOf="@id/til_name_code_file" app:layout_constraintTop_toBottomOf="@id/tv_name_code_file_header" style="@style/TextP3"/>
      <TextView android:textColor="@color/text_weak" android:id="@id/tv_name_code_file_chars" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xs" android:text="@string/name_code_playground_characters" app:layout_constraintBottom_toTopOf="@id/til_name_code_file" app:layout_constraintEnd_toEndOf="@id/til_name_code_file" style="@style/TextP3"/>
      <androidx.compose.ui.platform.ComposeView android:id="@id/btn_name_code_file_enter" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/til_name_code_file" app:layout_constraintWidth_max="200.000000dip"/>
      <androidx.compose.ui.platform.ComposeView android:id="@id/btn_name_code_cancel" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginBottom="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/btn_name_code_file_enter"/>
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_name_code_file_extension" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="@id/til_name_code_file" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="@id/til_name_code_file" style="@style/TextTitle2"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </androidx.cardview.widget.CardView>
</androidx.constraintlayout.widget.ConstraintLayout>
```
