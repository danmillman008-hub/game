# پروندهٔ لایه — `res/layout/onboarding_step_1_introduction_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_step_1_introduction_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_step_1_introduction_fragment.xml`](../../SOURCE/res/layout/onboarding_step_1_introduction_fragment.xml) |
| SHA-256 دیکد | `f84df60195b9606bc924f722a016e9cdfc4e4a46f2d01b1d78922dbc60e1a3d9` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 16 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_experience_introduction_title
   ├─ TextView  #@id/tv_set_experience_introduction_description
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/lv_set_experience_introduction
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 7 | `TextView` | `android:textColor` | `@color/text_primary` |
| 8 | `TextView` | `android:gravity` | `0x00000001` |
| 9 | `TextView` | `android:id` | `@id/tv_set_experience_introduction_title` |
| 10 | `TextView` | `android:layout_width` | `0.000000dip` |
| 11 | `TextView` | `android:layout_height` | `wrap_content` |
| 12 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 13 | `TextView` | `android:text` | `@string/onboarding_page_5_title` |
| 14 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 15 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 16 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 17 | `TextView` | `style` | `@style/TextH1` |
| 18 | `TextView` | `android:gravity` | `0x00000001` |
| 19 | `TextView` | `android:id` | `@id/tv_set_experience_introduction_description` |
| 20 | `TextView` | `android:layout_width` | `0.000000dip` |
| 21 | `TextView` | `android:layout_height` | `wrap_content` |
| 22 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 23 | `TextView` | `android:text` | `@string/onboarding_page_5_description` |
| 24 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_experience_introduction_title` |
| 27 | `TextView` | `style` | `@style/TextViewOnBoardingPageDescription` |
| 28 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/lv_set_experience_introduction` |
| 29 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `0.000000dip` |
| 30 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `0.000000dip` |
| 31 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 32 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintBottom_toTopOf` | `@id/compose_content` |
| 33 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintDimensionRatio` | `1:1` |
| 34 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 35 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintStart_toStartOf` | `0` |
| 36 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_experience_introduction_description` |
| 37 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintVertical_bias` | `0.500000` |
| 38 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 39 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveAutoPlay` | `true` |
| 40 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveLoop` | `1` |
| 41 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveResource` | `@raw/intro` |
| 42 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveStateMachine` | `default` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_content` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@string/onboarding_page_5_description` | `To build your personal curriculum, we'll ask you a few questions.` / `Um deinen persönlichen Lehrplan zu erstellen, werden wir dir einige Fragen stellen.` (de) / `Para crear tu currículum personal, te haremos unas preguntas.` (es) / `Pour élaborer ton programme personnel, nous te poserons quelques questions.` (fr) / `Untuk menyusun kurikulum pribadimu, kami akan menanyakan beberapa hal.` (in) / `Per creare il tuo programma personale ti faremo qualche domanda.` (it) / `Zadamy ci kilka pytań, aby ułożyć twój plan nauki.` (pl) / `Para criar seu currículo pessoal, faremos algumas perguntas.` (pt-rBR) / `Мы хотим немного узнать о тебе, чтобы создать учебный план, который подходит именно тебе.` (ru) / `Kişisel müfredatını oluşturmak için sana birkaç soru soracağız.` (tr) |
| `@string/onboarding_page_5_title` | `Welcome to Mimo!` / `Willkommen bei Mimo!` (de) / `¡Bienvenido/a a Mimo!` (es) / `Bienvenue à Mimo!` (fr) / `Selamat datang di Mimo!` (in) / `Ti diamo il benvenuto su Mimo!` (it) / `Witaj w Mimo!` (pl) / `Bem-vindo ao Mimo!` (pt-rBR) / `Добро пожаловать в Mimo!` (ru) / `Mimo'ya hoş geldin!` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextViewOnBoardingPageDescription` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/compose_content
@id/lv_set_experience_introduction
@id/tv_set_experience_introduction_description
@id/tv_set_experience_introduction_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.OnboardingActivity
com.getmimo.ui.onboarding.step1.IntroductionFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_gravity="0x00000011" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent" android:maxWidth="@dimen/general_max_width" android:layout_marginHorizontal="@dimen/spacing_l">
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000001" android:id="@id/tv_set_experience_introduction_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/onboarding_page_5_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
  <TextView android:gravity="0x00000001" android:id="@id/tv_set_experience_introduction_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/onboarding_page_5_description" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_set_experience_introduction_title" style="@style/TextViewOnBoardingPageDescription"/>
  <app.rive.runtime.kotlin.RiveAnimationView android:id="@id/lv_set_experience_introduction" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_marginHorizontal="@dimen/spacing_m_expandable" app:layout_constraintBottom_toTopOf="@id/compose_content" app:layout_constraintDimensionRatio="1:1" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_set_experience_introduction_description" app:layout_constraintVertical_bias="0.500000" app:layout_constraintWidth_max="@dimen/general_max_width" app:riveAutoPlay="true" app:riveLoop="1" app:riveResource="@raw/intro" app:riveStateMachine="default"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_content" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
