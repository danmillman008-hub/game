# پروندهٔ لایه — `res/layout/certificate_download_dialog_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/certificate_download_dialog_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/certificate_download_dialog_fragment.xml`](../../SOURCE/res/layout/certificate_download_dialog_fragment.xml) |
| SHA-256 دیکد | `55ae512d811e6ec52675a1b89df995c0ffd8571b4d9b7e1a168a5c6c4b845782` |
| ریشه | `FrameLayout` |
| تعداد گره | 10 |
| تعداد شناسه | 8 |
| تگ‌های استفاده‌شده | 9 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 33 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/layout_base_modal
   └─ androidx.cardview.widget.CardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rive_congrats_animation
         ├─ ImageButton  #@id/iv_modal_close
         ├─ TextView  #@id/tv_base_modal_title
         ├─ TextView  #@id/tv_base_modal_description
         ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_certificate_download_dialog_name
         │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_certificate_download_dialog_name
         └─ androidx.compose.ui.platform.ComposeView  #@id/btn_primary_action
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `FrameLayout` | `android:id` | `@id/layout_base_modal` |
| 3 | `FrameLayout` | `android:background` | `@color/transparent` |
| 4 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 5 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 6 | `androidx.cardview.widget.CardView` | `android:layout_gravity` | `0x00000011` |
| 7 | `androidx.cardview.widget.CardView` | `android:focusable` | `true` |
| 8 | `androidx.cardview.widget.CardView` | `android:clickable` | `true` |
| 9 | `androidx.cardview.widget.CardView` | `android:layout_width` | `@dimen/modal_default_width` |
| 10 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 11 | `androidx.cardview.widget.CardView` | `android:paddingStart` | `@dimen/modal_default_padding_horizontal` |
| 12 | `androidx.cardview.widget.CardView` | `android:paddingEnd` | `@dimen/modal_default_padding_horizontal` |
| 13 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/background_secondary` |
| 14 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/modal_corner_radius` |
| 15 | `androidx.cardview.widget.CardView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 16 | `androidx.cardview.widget.CardView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 17 | `androidx.cardview.widget.CardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 18 | `androidx.cardview.widget.CardView` | `app:layout_constraintTop_toTopOf` | `0` |
| 19 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 20 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 21 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `24.000000dip` |
| 22 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/rive_congrats_animation` |
| 23 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `wrap_content` |
| 24 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `120.000000dip` |
| 25 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginTop` | `40.000000dip` |
| 26 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 27 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 28 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 29 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintStart_toStartOf` | `0` |
| 30 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintTop_toTopOf` | `0` |
| 31 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveAutoPlay` | `true` |
| 32 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveLoop` | `1` |
| 33 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveResource` | `@raw/celebrating` |
| 34 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveStateMachine` | `default` |
| 35 | `ImageButton` | `android:id` | `@id/iv_modal_close` |
| 36 | `ImageButton` | `android:background` | `?attr/selectableItemBackground` |
| 37 | `ImageButton` | `android:padding` | `@dimen/modal_default_close_button_padding` |
| 38 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 39 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 40 | `ImageButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 41 | `ImageButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 42 | `ImageButton` | `app:srcCompat` | `@drawable/ic_close` |
| 43 | `ImageButton` | `app:tint` | `@color/icon_weak` |
| 44 | `TextView` | `android:textColor` | `@color/text_primary` |
| 45 | `TextView` | `android:gravity` | `0x00000011` |
| 46 | `TextView` | `android:id` | `@id/tv_base_modal_title` |
| 47 | `TextView` | `android:layout_width` | `wrap_content` |
| 48 | `TextView` | `android:layout_height` | `wrap_content` |
| 49 | `TextView` | `android:layout_marginTop` | `@dimen/modal_default_image_margin_bottom` |
| 50 | `TextView` | `android:text` | `@string/certificates_finished_track_dialog_title` |
| 51 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 52 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 53 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 54 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 55 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/rive_congrats_animation` |
| 56 | `TextView` | `style` | `@style/TextH2` |
| 57 | `TextView` | `android:textAppearance` | `@style/TextP2` |
| 58 | `TextView` | `android:textColor` | `@color/text_weak` |
| 59 | `TextView` | `android:gravity` | `0x00000011` |
| 60 | `TextView` | `android:id` | `@id/tv_base_modal_description` |
| 61 | `TextView` | `android:layout_width` | `0.000000dip` |
| 62 | `TextView` | `android:layout_height` | `wrap_content` |
| 63 | `TextView` | `android:layout_marginTop` | `@dimen/modal_default_title_margin_bottom` |
| 64 | `TextView` | `android:text` | `@string/certificates_finished_track_dialog_text` |
| 65 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_l` |
| 66 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_l` |
| 67 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/til_certificate_download_dialog_name` |
| 68 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 69 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 70 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_base_modal_title` |
| 71 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_certificate_download_dialog_name` |
| 72 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 73 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 74 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 75 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 76 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 77 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 78 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 79 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_base_modal_description` |
| 80 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintWidth_max` | `360.000000dip` |
| 81 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 82 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_certificate_download_dialog_name` |
| 83 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 84 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 85 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/certificates_finished_track_dialog_hint` |
| 86 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000021` |
| 87 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x00000006` |
| 88 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 89 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_primary_action` |
| 90 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 91 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 92 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/modal_default_description_margin_bottom` |
| 93 | `androidx.compose.ui.platform.ComposeView` | `android:minWidth` | `@dimen/modal_upgrade_continue_button_width` |
| 94 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 95 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 96 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 97 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 98 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/til_certificate_download_dialog_name` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@color/transparent` | `#00000000` |
| `@dimen/modal_corner_radius` | `12.000000dip` |
| `@dimen/modal_default_close_button_padding` | `12.000000dip` |
| `@dimen/modal_default_description_margin_bottom` | `24.000000dip` |
| `@dimen/modal_default_image_margin_bottom` | `16.000000dip` / `20.000000dip` (sw600dp) |
| `@dimen/modal_default_padding_horizontal` | `24.000000dip` |
| `@dimen/modal_default_title_margin_bottom` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@dimen/modal_default_width` | `296.000000dip` / `360.000000dip` (sw600dp) |
| `@dimen/modal_upgrade_continue_button_width` | `200.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@string/certificates_finished_track_dialog_hint` | `Your Name` / `Dein Name` (de) / `Tu Nombre` (es) / `Ton nom` (fr) / `Namamu` (in) / `Il tuo nome` (it) / `Twoje imię` (pl) / `Seu nome` (pt-rBR) / `Твоё имя` (ru) / `Adın` (tr) |
| `@string/certificates_finished_track_dialog_text` | `Enter the name you would like displayed on your certificate` / `Gib den Namen ein, der auf deinem Zertifikat angezeigt werden soll` (de) / `Introduce el nombre que quieres que aparezca en tu certificado` (es) / `Entre le nom que tu souhaites voir apparaître sur ton certificat` (fr) / `Masukkan nama yang mau ditampilkan di sertifikatmu` (in) / `Inserisci il nome che vuoi far comparire sul certificato` (it) / `Wpisz imię i nazwisko, które mają widnieć na certyfikacie` (pl) / `Digite o nome que você gostaria que fosse exibido em seu certificado` (pt-rBR) / `Введи имя, которое ты хочешь отобразить на сертификате` (ru) / `Sertifikanda görünmesini istediğin adı gir` (tr) |
| `@string/certificates_finished_track_dialog_title` | `Enter your name` / `Gib deinen Namen ein` (de) / `Introduce tu nombre` (es) / `Entre ton nom` (fr) / `Masukkan namamu` (in) / `Inserisci il tuo nome` (it) / `Wpisz swoje imię` (pl) / `Digite seu nome` (pt-rBR) / `Введи имя` (ru) / `Adını gir` (tr) |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_primary_action
@id/et_certificate_download_dialog_name
@id/iv_modal_close
@id/layout_base_modal
@id/rive_congrats_animation
@id/til_certificate_download_dialog_name
@id/tv_base_modal_description
@id/tv_base_modal_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.certificates.CertificateActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_gravity="0x00000011" android:id="@id/layout_base_modal" android:background="@color/transparent" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <androidx.cardview.widget.CardView android:layout_gravity="0x00000011" android:focusable="true" android:clickable="true" android:layout_width="@dimen/modal_default_width" android:layout_height="wrap_content" android:paddingStart="@dimen/modal_default_padding_horizontal" android:paddingEnd="@dimen/modal_default_padding_horizontal" app:cardBackgroundColor="@color/background_secondary" app:cardCornerRadius="@dimen/modal_corner_radius" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="24.000000dip">
      <app.rive.runtime.kotlin.RiveAnimationView android:id="@id/rive_congrats_animation" android:layout_width="wrap_content" android:layout_height="120.000000dip" android:layout_marginTop="40.000000dip" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:riveAutoPlay="true" app:riveLoop="1" app:riveResource="@raw/celebrating" app:riveStateMachine="default"/>
      <ImageButton android:id="@id/iv_modal_close" android:background="?attr/selectableItemBackground" android:padding="@dimen/modal_default_close_button_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_close" app:tint="@color/icon_weak"/>
      <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_base_modal_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/modal_default_image_margin_bottom" android:text="@string/certificates_finished_track_dialog_title" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/rive_congrats_animation" style="@style/TextH2"/>
      <TextView android:textAppearance="@style/TextP2" android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_base_modal_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/modal_default_title_margin_bottom" android:text="@string/certificates_finished_track_dialog_text" android:layout_marginStart="@dimen/spacing_l" android:layout_marginEnd="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/til_certificate_download_dialog_name" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_base_modal_title"/>
      <com.google.android.material.textfield.TextInputLayout android:id="@id/til_certificate_download_dialog_name" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_base_modal_description" app:layout_constraintWidth_max="360.000000dip" style="@style/MaterialEditTextLayout">
        <com.google.android.material.textfield.TextInputEditText android:id="@id/et_certificate_download_dialog_name" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/certificates_finished_track_dialog_hint" android:inputType="0x00000021" android:imeOptions="0x00000006" style="@style/MaterialEditText"/>
      </com.google.android.material.textfield.TextInputLayout>
      <androidx.compose.ui.platform.ComposeView android:id="@id/btn_primary_action" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/modal_default_description_margin_bottom" android:minWidth="@dimen/modal_upgrade_continue_button_width" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/til_certificate_download_dialog_name"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </androidx.cardview.widget.CardView>
</FrameLayout>
```
