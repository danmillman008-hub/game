# پروندهٔ لایه — `res/layout/sign_up_set_email_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/sign_up_set_email_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/sign_up_set_email_fragment.xml`](../../SOURCE/res/layout/sign_up_set_email_fragment.xml) |
| SHA-256 دیکد | `b2692db8ad800a66a513afeb1899015f81bca138ba217a966e722e618cd4cb6c` |
| ریشه | `ScrollView` |
| تعداد گره | 7 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 6 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ScrollView
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ include  #@id/sign_up_set_email_toolbar
      ├─ TextView  #@id/tv_signup_email
      ├─ com.google.android.material.textfield.TextInputLayout
      │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_signup_email
      └─ androidx.compose.ui.platform.ComposeView  #@id/btn_signup_set_email_continue
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ScrollView` | `android:background` | `@color/background_primary` |
| 2 | `ScrollView` | `android:layout_width` | `match_parent` |
| 3 | `ScrollView` | `android:layout_height` | `match_parent` |
| 4 | `ScrollView` | `android:fillViewport` | `true` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 7 | `include` | `android:id` | `@id/sign_up_set_email_toolbar` |
| 8 | `include` | `android:layout_width` | `match_parent` |
| 9 | `include` | `android:layout_height` | `wrap_content` |
| 10 | `include` | `android:layout_marginLeft` | `@dimen/authentication_email_top_bar_margin_horizontal` |
| 11 | `include` | `android:layout_marginTop` | `@dimen/authentication_email_top_bar_margin_top` |
| 12 | `include` | `android:layout_marginRight` | `@dimen/authentication_email_top_bar_margin_horizontal` |
| 13 | `include` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `include` | `layout` | `@layout/authentication_toolbar` |
| 15 | `TextView` | `android:id` | `@id/tv_signup_email` |
| 16 | `TextView` | `android:layout_width` | `wrap_content` |
| 17 | `TextView` | `android:layout_height` | `wrap_content` |
| 18 | `TextView` | `android:text` | `@string/enter_email` |
| 19 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 20 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/sign_up_set_email_toolbar` |
| 21 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/sign_up_set_email_toolbar` |
| 22 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/sign_up_set_email_toolbar` |
| 23 | `TextView` | `app:layout_constraintVertical_bias` | `0.200000` |
| 24 | `TextView` | `style` | `@style/TextViewSignupLoginHeader` |
| 25 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `0.000000dip` |
| 26 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 27 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 28 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 29 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constrainedWidth` | `true` |
| 30 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 31 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 32 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_signup_email` |
| 33 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintWidth_max` | `360.000000dip` |
| 34 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 35 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_signup_email` |
| 36 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 37 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 38 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/enter_email_hint` |
| 39 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 40 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000021` |
| 41 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x00000006` |
| 42 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_signup_set_email_continue` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `android:layout_margin` | `@dimen/spacing_m` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `360.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@dimen/authentication_email_top_bar_margin_horizontal` | `0.000000dip` / `24.000000dip` (sw720dp) |
| `@dimen/authentication_email_top_bar_margin_top` | `0.000000dip` / `24.000000dip` (sw720dp) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@string/enter_email` | `What's your email address` / `Was ist deine E-Mail-Adresse?` (de) / `¿Cuál es tu email?` (es) / `Quelle est ton adresse e-mail?` (fr) / `Apa alamat emailmu` (in) / `Qual è la tua email?` (it) / `Jaki jest twój adres e-mail?` (pl) / `Qual é o seu e-mail?` (pt-rBR) / `Твой email адрес` (ru) / `E-posta adresin nedir?` (tr) |
| `@string/enter_email_hint` | `Email address` / `E-Mail-Adresse` (de) / `Dirección de Email` (es) / `Adresse E-mail` (fr) / `Alamat email` (in) / `Indirizzo email` (it) / `Adres e-mail` (pl) / `Endereço de e-mail` (pt-rBR) / `Email адрес` (ru) / `E-posta adresi` (tr) |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextViewSignupLoginHeader` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/btn_signup_set_email_continue
@id/et_signup_email
@id/sign_up_set_email_toolbar
@id/tv_signup_email
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
com.getmimo.ui.authentication.SignUpSetEmailFragment$onViewCreated$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent" android:fillViewport="true">
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
    <include android:id="@id/sign_up_set_email_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/authentication_email_top_bar_margin_horizontal" android:layout_marginTop="@dimen/authentication_email_top_bar_margin_top" android:layout_marginRight="@dimen/authentication_email_top_bar_margin_horizontal" app:layout_constraintTop_toTopOf="0" layout="@layout/authentication_toolbar"/>
    <TextView android:id="@id/tv_signup_email" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/enter_email" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="@id/sign_up_set_email_toolbar" app:layout_constraintStart_toStartOf="@id/sign_up_set_email_toolbar" app:layout_constraintTop_toBottomOf="@id/sign_up_set_email_toolbar" app:layout_constraintVertical_bias="0.200000" style="@style/TextViewSignupLoginHeader"/>
    <com.google.android.material.textfield.TextInputLayout android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_signup_email" app:layout_constraintWidth_max="360.000000dip" style="@style/MaterialEditTextLayout">
      <com.google.android.material.textfield.TextInputEditText android:id="@id/et_signup_email" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/enter_email_hint" android:ems="10" android:inputType="0x00000021" android:imeOptions="0x00000006" style="@style/MaterialEditText"/>
    </com.google.android.material.textfield.TextInputLayout>
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_signup_set_email_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_margin="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="360.000000dip"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</ScrollView>
```
