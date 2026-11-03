# پروندهٔ لایه — `res/layout/name_code_playground_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/name_code_playground_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/name_code_playground_fragment.xml`](../../SOURCE/res/layout/name_code_playground_fragment.xml) |
| SHA-256 دیکد | `5122ebb3e48378c804f6b00962aff6ab5a05f6d20043baa3c44862a87614da50` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 15 |
| تعداد شناسه | 12 |
| تگ‌های استفاده‌شده | 10 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 38 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_name_code_playground
   └─ androidx.cardview.widget.CardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_save_code_header
         ├─ TextView  #@id/tv_save_code_name
         ├─ TextView  #@id/tv_name_code_chars
         ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_name_code
         │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_name_code
         │     └─ requestFocus
         ├─ ImageView  #@id/iv_public_playground
         ├─ TextView  #@id/tv_public_playground
         ├─ androidx.appcompat.widget.SwitchCompat  #@id/sw_public_playground
         ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_name_code_enter
         ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_name_code_cancel
         └─ androidx.constraintlayout.widget.Group  #@id/group_save_code_visibility
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/root_name_code_playground` |
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
| 21 | `TextView` | `android:id` | `@id/tv_save_code_header` |
| 22 | `TextView` | `android:layout_width` | `wrap_content` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 25 | `TextView` | `android:text` | `@string/name_code_playground_header` |
| 26 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 29 | `TextView` | `style` | `@style/TextH2` |
| 30 | `TextView` | `android:textColor` | `@color/text_weak` |
| 31 | `TextView` | `android:id` | `@id/tv_save_code_name` |
| 32 | `TextView` | `android:layout_width` | `wrap_content` |
| 33 | `TextView` | `android:layout_height` | `wrap_content` |
| 34 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 35 | `TextView` | `android:text` | `@string/name` |
| 36 | `TextView` | `android:textAllCaps` | `true` |
| 37 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/til_name_code` |
| 38 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_save_code_header` |
| 39 | `TextView` | `style` | `@style/TextP3` |
| 40 | `TextView` | `android:textColor` | `@color/text_weak` |
| 41 | `TextView` | `android:id` | `@id/tv_name_code_chars` |
| 42 | `TextView` | `android:layout_width` | `wrap_content` |
| 43 | `TextView` | `android:layout_height` | `wrap_content` |
| 44 | `TextView` | `android:text` | `@string/name_code_playground_characters` |
| 45 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/til_name_code` |
| 46 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/tv_save_code_name` |
| 47 | `TextView` | `style` | `@style/TextP3` |
| 48 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_name_code` |
| 49 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 50 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 51 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 52 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 53 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 54 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 55 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 56 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_name_code_chars` |
| 57 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 58 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_name_code` |
| 59 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 60 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 61 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/name_code_playground_hint` |
| 62 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 63 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000061` |
| 64 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x00000006` |
| 65 | `com.google.android.material.textfield.TextInputEditText` | `android:autofillHints` | `@null` |
| 66 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 67 | `ImageView` | `android:id` | `@id/iv_public_playground` |
| 68 | `ImageView` | `android:layout_width` | `wrap_content` |
| 69 | `ImageView` | `android:layout_height` | `wrap_content` |
| 70 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 71 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/til_name_code` |
| 72 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/til_name_code` |
| 73 | `ImageView` | `app:srcCompat` | `@drawable/ic_globe` |
| 74 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 75 | `TextView` | `android:textColor` | `@color/text_primary` |
| 76 | `TextView` | `android:id` | `@id/tv_public_playground` |
| 77 | `TextView` | `android:layout_width` | `wrap_content` |
| 78 | `TextView` | `android:layout_height` | `wrap_content` |
| 79 | `TextView` | `android:text` | `@string/public_playground` |
| 80 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 81 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_public_playground` |
| 82 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_public_playground` |
| 83 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_public_playground` |
| 84 | `TextView` | `style` | `@style/TextP1` |
| 85 | `androidx.appcompat.widget.SwitchCompat` | `android:id` | `@id/sw_public_playground` |
| 86 | `androidx.appcompat.widget.SwitchCompat` | `android:layout_width` | `wrap_content` |
| 87 | `androidx.appcompat.widget.SwitchCompat` | `android:layout_height` | `wrap_content` |
| 88 | `androidx.appcompat.widget.SwitchCompat` | `android:checked` | `false` |
| 89 | `androidx.appcompat.widget.SwitchCompat` | `android:thumb` | `@drawable/component_switch_thumb` |
| 90 | `androidx.appcompat.widget.SwitchCompat` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_public_playground` |
| 91 | `androidx.appcompat.widget.SwitchCompat` | `app:layout_constraintEnd_toEndOf` | `@id/til_name_code` |
| 92 | `androidx.appcompat.widget.SwitchCompat` | `app:layout_constraintTop_toTopOf` | `@id/iv_public_playground` |
| 93 | `androidx.appcompat.widget.SwitchCompat` | `app:track` | `@drawable/component_switch_track` |
| 94 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_name_code_enter` |
| 95 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 96 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 97 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 98 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 99 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 100 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 101 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_public_playground` |
| 102 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `200.000000dip` |
| 103 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_name_code_cancel` |
| 104 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 105 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 106 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 107 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 108 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 109 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 110 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 111 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/btn_name_code_enter` |
| 112 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/group_save_code_visibility` |
| 113 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `wrap_content` |
| 114 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `wrap_content` |
| 115 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `iv_public_playground,tv_public_playground,sw_public_playground` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/generic_backdrop_color` | `#88000000` |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
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
| `@string/name_code_playground_characters` | `0/40 characters` / `0/40 Zeichen` (de) / `0/40 caracteres` (es) / `0/40 caractères` (fr) / `0/40 karakter` (in) / `0/40 caratteri` (it) / `0/40 znaków` (pl) / `0/40 caracteres` (pt-rBR) / `0/40 символов` (ru) / `0/40 karakter` (tr) |
| `@string/name_code_playground_header` | `Save your Code` / `Speichere deinen Code` (de) / `Guarda tu Código` (es) / `Sauvegarde ton code` (fr) / `Simpan kodemu` (in) / `Salva il tuo codice` (it) / `Zapisz swój kod` (pl) / `Salve seu código` (pt-rBR) / `Сохранить Код` (ru) / `Kodunu Kaydet` (tr) |
| `@string/name_code_playground_hint` | `My Awesome Demo` / `Meine fantastische Demo` (de) / `Mi fantástica Demo` (es) / `Mon Incroyable Démo` (fr) / `Demo Kerenku` (in) / `La mia demo fantastica` (it) / `Moje super demo` (pl) / `Minha incrível demonstração` (pt-rBR) / `Мое потрясающее демо` (ru) / `Harika Demom` (tr) |
| `@string/public_playground` | `Public` / `Öffentlich` (de) / `Público` (es) / `Publique` (fr) / `Publik` (in) / `Pubblico` (it) / `Publiczny` (pl) / `Público` (pt-rBR) / `Все` (ru) / `Herkese açık` (tr) |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_name_code_cancel
@id/btn_name_code_enter
@id/et_name_code
@id/group_save_code_visibility
@id/iv_public_playground
@id/root_name_code_playground
@id/sw_public_playground
@id/til_name_code
@id/tv_name_code_chars
@id/tv_public_playground
@id/tv_save_code_header
@id/tv_save_code_name
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.codeplayground.CodePlaygroundActivity
com.getmimo.ui.codeplayground.NameCodePlaygroundFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/root_name_code_playground" android:background="@color/generic_backdrop_color" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.cardview.widget.CardView android:focusable="true" android:clickable="true" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="64.000000dip" android:layout_marginHorizontal="@dimen/spacing_xxl" app:cardBackgroundColor="@color/background_secondary" app:cardCornerRadius="@dimen/modal_corner_radius" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="match_parent">
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_save_code_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/name_code_playground_header" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH2"/>
      <TextView android:textColor="@color/text_weak" android:id="@id/tv_save_code_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:text="@string/name" android:textAllCaps="true" app:layout_constraintStart_toStartOf="@id/til_name_code" app:layout_constraintTop_toBottomOf="@id/tv_save_code_header" style="@style/TextP3"/>
      <TextView android:textColor="@color/text_weak" android:id="@id/tv_name_code_chars" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/name_code_playground_characters" app:layout_constraintEnd_toEndOf="@id/til_name_code" app:layout_constraintTop_toTopOf="@id/tv_save_code_name" style="@style/TextP3"/>
      <com.google.android.material.textfield.TextInputLayout android:id="@id/til_name_code" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_name_code_chars" style="@style/MaterialEditTextLayout">
        <com.google.android.material.textfield.TextInputEditText android:id="@id/et_name_code" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/name_code_playground_hint" android:ems="10" android:inputType="0x00000061" android:imeOptions="0x00000006" android:autofillHints="@null" style="@style/MaterialEditText">
          <requestFocus/>
        </com.google.android.material.textfield.TextInputEditText>
      </com.google.android.material.textfield.TextInputLayout>
      <ImageView android:id="@id/iv_public_playground" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintStart_toStartOf="@id/til_name_code" app:layout_constraintTop_toBottomOf="@id/til_name_code" app:srcCompat="@drawable/ic_globe" app:tint="@color/icon_weak"/>
      <TextView android:textColor="@color/text_primary" android:id="@id/tv_public_playground" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/public_playground" android:layout_marginStart="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="@id/iv_public_playground" app:layout_constraintStart_toEndOf="@id/iv_public_playground" app:layout_constraintTop_toTopOf="@id/iv_public_playground" style="@style/TextP1"/>
      <androidx.appcompat.widget.SwitchCompat android:id="@id/sw_public_playground" android:layout_width="wrap_content" android:layout_height="wrap_content" android:checked="false" android:thumb="@drawable/component_switch_thumb" app:layout_constraintBottom_toBottomOf="@id/iv_public_playground" app:layout_constraintEnd_toEndOf="@id/til_name_code" app:layout_constraintTop_toTopOf="@id/iv_public_playground" app:track="@drawable/component_switch_track"/>
      <androidx.compose.ui.platform.ComposeView android:id="@id/btn_name_code_enter" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_public_playground" app:layout_constraintWidth_max="200.000000dip"/>
      <androidx.compose.ui.platform.ComposeView android:id="@id/btn_name_code_cancel" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginBottom="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/btn_name_code_enter"/>
      <androidx.constraintlayout.widget.Group android:id="@id/group_save_code_visibility" android:layout_width="wrap_content" android:layout_height="wrap_content" app:constraint_referenced_ids="iv_public_playground,tv_public_playground,sw_public_playground"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </androidx.cardview.widget.CardView>
</androidx.constraintlayout.widget.ConstraintLayout>
```
