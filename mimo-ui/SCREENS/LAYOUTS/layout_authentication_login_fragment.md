# پروندهٔ لایه — `res/layout/authentication_login_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/authentication_login_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/authentication_login_fragment.xml`](../../SOURCE/res/layout/authentication_login_fragment.xml) |
| SHA-256 دیکد | `ec5adfcb3f9efd80b5fb79f54fdab755293476e20fe4ab6ece50913c95e9ca75` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 11 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 35 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/btn_back
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rive_login
   ├─ TextView  #@id/tv_headline_authentication
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_login_with_email
   ├─ TextView  #@id/tv_continue_with
   ├─ com.getmimo.ui.authentication.ButtonSocialLogin  #@id/btn_continue_google
   ├─ com.getmimo.ui.authentication.ButtonSocialLogin  #@id/btn_continue_facebook
   │  └─ com.facebook.login.widget.LoginButton  #@id/btn_facebook_login
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_last_used_auth_method
   ├─ include  #@id/layout_terms_conditions
   └─ TextView  #@id/tv_delete_account
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `ImageView` | `android:id` | `@id/btn_back` |
| 5 | `ImageView` | `android:padding` | `@dimen/spacing_m_expandable` |
| 6 | `ImageView` | `android:layout_width` | `wrap_content` |
| 7 | `ImageView` | `android:layout_height` | `wrap_content` |
| 8 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 9 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 10 | `ImageView` | `app:srcCompat` | `@drawable/ic_arrow_left` |
| 11 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 12 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_gravity` | `0x00000011` |
| 13 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/rive_login` |
| 14 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `wrap_content` |
| 15 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `0.000000dip` |
| 16 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:adjustViewBounds` | `true` |
| 17 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginHorizontal` | `@dimen/spacing_xxl` |
| 18 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_headline_authentication` |
| 19 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 20 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintStart_toStartOf` | `0` |
| 21 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintTop_toBottomOf` | `@id/btn_back` |
| 22 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintVertical_bias` | `0.050000` |
| 23 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintVertical_weight` | `2.000000` |
| 24 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveAutoPlay` | `true` |
| 25 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveResource` | `@raw/log_in` |
| 26 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveStateMachine` | `default` |
| 27 | `TextView` | `android:gravity` | `0x00000011` |
| 28 | `TextView` | `android:id` | `@id/tv_headline_authentication` |
| 29 | `TextView` | `android:layout_width` | `0.000000dip` |
| 30 | `TextView` | `android:layout_height` | `0.000000dip` |
| 31 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 32 | `TextView` | `android:text` | `@string/login_welcome_message` |
| 33 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_xl_expandable` |
| 34 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_login_with_email` |
| 35 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 36 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 37 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/rive_login` |
| 38 | `TextView` | `app:layout_constraintVertical_weight` | `1.000000` |
| 39 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/content_max_width` |
| 40 | `TextView` | `style` | `@style/TextViewOnBoardingPageTitle` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_login_with_email` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_continue_with` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/content_max_width` |
| 50 | `TextView` | `android:textColor` | `@color/text_weak` |
| 51 | `TextView` | `android:gravity` | `0x00000011` |
| 52 | `TextView` | `android:id` | `@id/tv_continue_with` |
| 53 | `TextView` | `android:layout_width` | `0.000000dip` |
| 54 | `TextView` | `android:layout_height` | `wrap_content` |
| 55 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 56 | `TextView` | `android:text` | `@string/login_or_continue_with` |
| 57 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_xl_expandable` |
| 58 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_continue_google` |
| 59 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 60 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 61 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 62 | `TextView` | `style` | `@style/TextSubtitle` |
| 63 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:id` | `@id/btn_continue_google` |
| 64 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:layout_width` | `56.000000dip` |
| 65 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:layout_height` | `56.000000dip` |
| 66 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:layout_marginBottom` | `@dimen/spacing_xl` |
| 67 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:button_logo` | `@drawable/google_logo` |
| 68 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:button_style` | `1` |
| 69 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintBottom_toTopOf` | `@id/layout_terms_conditions` |
| 70 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintEnd_toStartOf` | `@id/btn_continue_facebook` |
| 71 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintHorizontal_chainStyle` | `2` |
| 72 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintStart_toStartOf` | `@id/tv_continue_with` |
| 73 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintWidth_max` | `@dimen/content_max_width` |
| 74 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `style` | `@style/GoogleLogin` |
| 75 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:id` | `@id/btn_continue_facebook` |
| 76 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:layout_width` | `56.000000dip` |
| 77 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:layout_height` | `56.000000dip` |
| 78 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:layout_marginBottom` | `@dimen/spacing_xs_expandable` |
| 79 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `android:layout_marginStart` | `@dimen/spacing_xl` |
| 80 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:button_logo` | `@drawable/facebook_logo` |
| 81 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:button_style` | `1` |
| 82 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintEnd_toEndOf` | `@id/tv_continue_with` |
| 83 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintStart_toEndOf` | `@id/btn_continue_google` |
| 84 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintTop_toTopOf` | `@id/btn_continue_google` |
| 85 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `app:layout_constraintWidth_max` | `@dimen/content_max_width` |
| 86 | `com.getmimo.ui.authentication.ButtonSocialLogin` | `style` | `@style/FacebookLogin` |
| 87 | `com.facebook.login.widget.LoginButton` | `android:id` | `@id/btn_facebook_login` |
| 88 | `com.facebook.login.widget.LoginButton` | `android:layout_width` | `0.000000dip` |
| 89 | `com.facebook.login.widget.LoginButton` | `android:layout_height` | `0.000000dip` |
| 90 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_last_used_auth_method` |
| 91 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 92 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 93 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 94 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `16777208.000000dip` |
| 95 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_login_with_email` |
| 96 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `@id/btn_login_with_email` |
| 97 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `@id/btn_login_with_email` |
| 98 | `include` | `android:gravity` | `0x00000011` |
| 99 | `include` | `android:id` | `@id/layout_terms_conditions` |
| 100 | `include` | `android:layout_width` | `wrap_content` |
| 101 | `include` | `android:layout_height` | `wrap_content` |
| 102 | `include` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 103 | `include` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 104 | `include` | `app:layout_constraintBottom_toTopOf` | `@id/tv_delete_account` |
| 105 | `include` | `app:layout_constraintEnd_toEndOf` | `0` |
| 106 | `include` | `app:layout_constraintStart_toStartOf` | `0` |
| 107 | `include` | `layout` | `@layout/authentication_terms_and_conditions` |
| 108 | `TextView` | `android:textColor` | `@color/text_weak` |
| 109 | `TextView` | `android:gravity` | `0x00000011` |
| 110 | `TextView` | `android:id` | `@id/tv_delete_account` |
| 111 | `TextView` | `android:paddingTop` | `2.000000dip` |
| 112 | `TextView` | `android:layout_width` | `0.000000dip` |
| 113 | `TextView` | `android:layout_height` | `wrap_content` |
| 114 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 115 | `TextView` | `android:text` | `@string/login_delete_account` |
| 116 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 117 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 118 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 119 | `TextView` | `style` | `@style/TextP3` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/content_max_width` | `608.000000dip` |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xl_expandable` | `32.000000dip` / `48.000000dip` (sw600dp) |
| `@dimen/spacing_xs_expandable` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/login_delete_account` | `You can delete your account in your settings` / `Deinen Account kannst du in den Einstellungen löschen` (de) / `Puedes eliminar tu cuenta en Ajustes` (es) / `Tu peux supprimer ton compte dans les paramètres` (fr) / `Kamu bisa menghapus akunmu di pengaturan` (in) / `Puoi eliminare il tuo account dalle impostazioni` (it) / `Konto możesz usunąć w ustawieniach` (pl) / `Você pode excluir sua conta em suas configurações` (pt-rBR) / `Ты можешь удалить свой аккаунт в настройках` (ru) / `Hesabını ayarlardan silebilirsin` (tr) |
| `@string/login_or_continue_with` | `Or continue with:` / `Oder weiter mit:` (de) / `O continúa con:` (es) / `Ou continuer avec:` (fr) / `Atau lanjutkan dengan:` (in) / `Oppure continua con:` (it) / `Lub kontynuuj przez:` (pl) / `Ou continue com:` (pt-rBR) / `Или продолжить с` (ru) / `Ya da şununla devam et:` (tr) |
| `@string/login_welcome_message` | `Welcome back!
You’ve been missed.` / `Willkommen zurück!
Wir haben dich vermisst.` (de) / `¡Bienvenido/a de nuevo!
Te echamos de menos.` (es) / `Bienvenue à nouveau.
Tu nous as manqué.` (fr) / `Selamat datang kembali!
Kami merindukanmu.` (in) / `Che bello rivederti!
Sentivamo la tua mancanza.` (it) / `Witaj ponownie!
Tęskniliśmy.` (pl) / `Bem-vindo de volta!
Sentimos sua falta.` (pt-rBR) / `Добро пожаловать назад!
Мы скучали.` (ru) / `Tekrar hoş geldin!
Seni özledik.` (tr) |
| `@style/FacebookLogin` | `[{'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/button_background_facebook', 'value_type': 'reference'}, {'attr': 'android:foreground', 'attr_id': '0x01010109', 'value': '@drawable/button_background_round_12dp_ripple', 'value_type': 'reference'}]` |
| `@style/GoogleLogin` | `[{'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/button_background_google', 'value_type': 'reference'}, {'attr': 'android:foreground', 'attr_id': '0x01010109', 'value': '@drawable/button_background_round_12dp_ripple', 'value_type': 'reference'}]` |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextSubtitle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextViewOnBoardingPageTitle` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/btn_back
@id/btn_continue_facebook
@id/btn_continue_google
@id/btn_facebook_login
@id/btn_login_with_email
@id/cv_last_used_auth_method
@id/layout_terms_conditions
@id/rive_login
@id/tv_continue_with
@id/tv_delete_account
@id/tv_headline_authentication
```

## ۵. ارجاع به لایه‌های دیگر

```text
0
@dimen/spacing_l
@id/tv_delete_account
@layout/authentication_terms_and_conditions
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.authentication.AuthenticationActivity
com.getmimo.ui.authentication.AuthenticationFragment$configureButtons$2
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <ImageView android:id="@id/btn_back" android:padding="@dimen/spacing_m_expandable" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_arrow_left" app:tint="@color/icon_weak"/>
  <app.rive.runtime.kotlin.RiveAnimationView android:layout_gravity="0x00000011" android:id="@id/rive_login" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:adjustViewBounds="true" android:layout_marginHorizontal="@dimen/spacing_xxl" app:layout_constraintBottom_toTopOf="@id/tv_headline_authentication" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/btn_back" app:layout_constraintVertical_bias="0.050000" app:layout_constraintVertical_weight="2.000000" app:riveAutoPlay="true" app:riveResource="@raw/log_in" app:riveStateMachine="default"/>
  <TextView android:gravity="0x00000011" android:id="@id/tv_headline_authentication" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_marginTop="@dimen/spacing_l" android:text="@string/login_welcome_message" android:layout_marginHorizontal="@dimen/spacing_xl_expandable" app:layout_constraintBottom_toTopOf="@id/btn_login_with_email" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/rive_login" app:layout_constraintVertical_weight="1.000000" app:layout_constraintWidth_max="@dimen/content_max_width" style="@style/TextViewOnBoardingPageTitle"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_login_with_email" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m_expandable" app:layout_constraintBottom_toTopOf="@id/tv_continue_with" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/content_max_width"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_continue_with" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l" android:text="@string/login_or_continue_with" android:layout_marginHorizontal="@dimen/spacing_xl_expandable" app:layout_constraintBottom_toTopOf="@id/btn_continue_google" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width" style="@style/TextSubtitle"/>
  <com.getmimo.ui.authentication.ButtonSocialLogin android:id="@id/btn_continue_google" android:layout_width="56.000000dip" android:layout_height="56.000000dip" android:layout_marginBottom="@dimen/spacing_xl" app:button_logo="@drawable/google_logo" app:button_style="1" app:layout_constraintBottom_toTopOf="@id/layout_terms_conditions" app:layout_constraintEnd_toStartOf="@id/btn_continue_facebook" app:layout_constraintHorizontal_chainStyle="2" app:layout_constraintStart_toStartOf="@id/tv_continue_with" app:layout_constraintWidth_max="@dimen/content_max_width" style="@style/GoogleLogin"/>
  <com.getmimo.ui.authentication.ButtonSocialLogin android:id="@id/btn_continue_facebook" android:layout_width="56.000000dip" android:layout_height="56.000000dip" android:layout_marginBottom="@dimen/spacing_xs_expandable" android:layout_marginStart="@dimen/spacing_xl" app:button_logo="@drawable/facebook_logo" app:button_style="1" app:layout_constraintEnd_toEndOf="@id/tv_continue_with" app:layout_constraintStart_toEndOf="@id/btn_continue_google" app:layout_constraintTop_toTopOf="@id/btn_continue_google" app:layout_constraintWidth_max="@dimen/content_max_width" style="@style/FacebookLogin">
    <com.facebook.login.widget.LoginButton android:id="@id/btn_facebook_login" android:layout_width="0.000000dip" android:layout_height="0.000000dip"/>
  </com.getmimo.ui.authentication.ButtonSocialLogin>
  <androidx.compose.ui.platform.ComposeView android:id="@id/cv_last_used_auth_method" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="16777208.000000dip" app:layout_constraintBottom_toTopOf="@id/btn_login_with_email" app:layout_constraintEnd_toEndOf="@id/btn_login_with_email" app:layout_constraintStart_toStartOf="@id/btn_login_with_email"/>
  <include android:gravity="0x00000011" android:id="@id/layout_terms_conditions" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintBottom_toTopOf="@id/tv_delete_account" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" layout="@layout/authentication_terms_and_conditions"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_delete_account" android:paddingTop="2.000000dip" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:text="@string/login_delete_account" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" style="@style/TextP3"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
