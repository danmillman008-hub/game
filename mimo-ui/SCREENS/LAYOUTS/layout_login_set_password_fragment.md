# پروندهٔ لایه — `res/layout/login_set_password_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/login_set_password_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/login_set_password_fragment.xml`](../../SOURCE/res/layout/login_set_password_fragment.xml) |
| SHA-256 دیکد | `def29ef78b008b5100106465f8363e534d32626618b40e17f3c3a3588b8a5e62` |
| ریشه | `ScrollView` |
| تعداد گره | 8 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 6 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ScrollView
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ include  #@id/login_set_password_toolbar
      ├─ TextView  #@id/tv_login_password
      ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_password
      │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_login_password
      ├─ androidx.compose.ui.platform.ComposeView  #@id/button_forgot_password
      └─ androidx.compose.ui.platform.ComposeView  #@id/btn_login_set_password_continue
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ScrollView` | `android:layout_width` | `match_parent` |
| 2 | `ScrollView` | `android:layout_height` | `match_parent` |
| 3 | `ScrollView` | `android:fillViewport` | `true` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 6 | `include` | `android:id` | `@id/login_set_password_toolbar` |
| 7 | `include` | `android:layout_width` | `match_parent` |
| 8 | `include` | `android:layout_height` | `wrap_content` |
| 9 | `include` | `android:layout_marginLeft` | `@dimen/authentication_email_top_bar_margin_horizontal` |
| 10 | `include` | `android:layout_marginTop` | `@dimen/authentication_email_top_bar_margin_top` |
| 11 | `include` | `android:layout_marginRight` | `@dimen/authentication_email_top_bar_margin_horizontal` |
| 12 | `include` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `include` | `layout` | `@layout/authentication_toolbar` |
| 14 | `TextView` | `android:id` | `@id/tv_login_password` |
| 15 | `TextView` | `android:layout_width` | `wrap_content` |
| 16 | `TextView` | `android:layout_height` | `wrap_content` |
| 17 | `TextView` | `android:layout_marginTop` | `@dimen/authentication_email_headline_margin_top` |
| 18 | `TextView` | `android:text` | `@string/enter_password` |
| 19 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 20 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/login_set_password_toolbar` |
| 21 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/login_set_password_toolbar` |
| 22 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/login_set_password_toolbar` |
| 23 | `TextView` | `app:layout_constraintVertical_bias` | `0.200000` |
| 24 | `TextView` | `style` | `@style/TextViewSignupLoginHeader` |
| 25 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_password` |
| 26 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 27 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 28 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 29 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 30 | `com.google.android.material.textfield.TextInputLayout` | `app:endIconDrawable` | `@drawable/ic_eye_off` |
| 31 | `com.google.android.material.textfield.TextInputLayout` | `app:endIconMode` | `1` |
| 32 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 33 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 34 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 35 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_login_password` |
| 36 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintWidth_max` | `360.000000dip` |
| 37 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 38 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_login_password` |
| 39 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 40 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 41 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/enter_password_hint` |
| 42 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 43 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000081` |
| 44 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x00000006` |
| 45 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/button_forgot_password` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `@id/til_password` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `@id/til_password` |
| 51 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/til_password` |
| 52 | `androidx.compose.ui.platform.ComposeView` | `style` | `@style/MaterialButton.TextButton.Weak` |
| 53 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_login_set_password_continue` |
| 54 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 55 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 56 | `androidx.compose.ui.platform.ComposeView` | `android:layout_margin` | `@dimen/spacing_m` |
| 57 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 58 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 59 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 60 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `360.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/authentication_email_headline_margin_top` | `12.000000dip` |
| `@dimen/authentication_email_top_bar_margin_horizontal` | `0.000000dip` / `24.000000dip` (sw720dp) |
| `@dimen/authentication_email_top_bar_margin_top` | `0.000000dip` / `24.000000dip` (sw720dp) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@string/enter_password` | `Enter your password` / `Gib dein Passwort ein` (de) / `Introduce tu contraseña` (es) / `Entre ton mot de passe` (fr) / `Masukkan kata sandimu` (in) / `Inserisci la tua password` (it) / `Wpisz hasło` (pl) / `Insira sua senha` (pt-rBR) / `Введи пароль` (ru) / `Şifreni gir` (tr) |
| `@string/enter_password_hint` | `Password (+6 characters)` / `Passwort (+6 Zeichen)` (de) / `Contraseña (+6 caracteres)` (es) / `Mot de passe (+6 caractères)` (fr) / `Kata sandi (+6 karakter)` (in) / `Password (+6 caratteri)` (it) / `Hasło (min. 6 znaków)` (pl) / `Senha (+6 caracteres)` (pt-rBR) / `Пароль (более 6 символов)` (ru) / `Şifre (+6 karakter)` (tr) |
| `@style/MaterialButton.TextButton.Weak` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}]` |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextViewSignupLoginHeader` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/btn_login_set_password_continue
@id/button_forgot_password
@id/et_login_password
@id/login_set_password_toolbar
@id/til_password
@id/tv_login_password
```

## ۵. ارجاع به لایه‌های دیگر

```text
0
@dimen/authentication_email_top_bar_margin_horizontal
@dimen/authentication_email_top_bar_margin_top
@layout/authentication_toolbar
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.authentication.LoginSetPasswordFragment$onViewCreated$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="match_parent" android:fillViewport="true">
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
    <include android:id="@id/login_set_password_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/authentication_email_top_bar_margin_horizontal" android:layout_marginTop="@dimen/authentication_email_top_bar_margin_top" android:layout_marginRight="@dimen/authentication_email_top_bar_margin_horizontal" app:layout_constraintTop_toTopOf="0" layout="@layout/authentication_toolbar"/>
    <TextView android:id="@id/tv_login_password" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/authentication_email_headline_margin_top" android:text="@string/enter_password" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="@id/login_set_password_toolbar" app:layout_constraintStart_toStartOf="@id/login_set_password_toolbar" app:layout_constraintTop_toBottomOf="@id/login_set_password_toolbar" app:layout_constraintVertical_bias="0.200000" style="@style/TextViewSignupLoginHeader"/>
    <com.google.android.material.textfield.TextInputLayout android:id="@id/til_password" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m" app:endIconDrawable="@drawable/ic_eye_off" app:endIconMode="1" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_login_password" app:layout_constraintWidth_max="360.000000dip" style="@style/MaterialEditTextLayout">
      <com.google.android.material.textfield.TextInputEditText android:id="@id/et_login_password" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/enter_password_hint" android:ems="10" android:inputType="0x00000081" android:imeOptions="0x00000006" style="@style/MaterialEditText"/>
    </com.google.android.material.textfield.TextInputLayout>
    <androidx.compose.ui.platform.ComposeView android:id="@id/button_forgot_password" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/til_password" app:layout_constraintStart_toStartOf="@id/til_password" app:layout_constraintTop_toBottomOf="@id/til_password" style="@style/MaterialButton.TextButton.Weak"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_login_set_password_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_margin="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="360.000000dip"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</ScrollView>
```
