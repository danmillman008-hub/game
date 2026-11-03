# پروندهٔ لایه — `res/layout/onboarding_step_3_set_experience_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_step_3_set_experience_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_step_3_set_experience_fragment.xml`](../../SOURCE/res/layout/onboarding_step_3_set_experience_fragment.xml) |
| SHA-256 دیکد | `ee80ad578de64f58370ec0cf1c49e5a5ac4343125a0fd71f4cdc079a7c801aff` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_experience_slider_title
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_set_experience_animation
   ├─ LinearLayout  #@id/layout_set_experience_slider_and_text
   │  ├─ com.getmimo.ui.common.SeekBarWithIntervals  #@id/seekbar_set_experience
   │  └─ TextView  #@id/tv_set_experience_slider_description
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000031` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 7 | `TextView` | `android:textColor` | `@color/text_primary` |
| 8 | `TextView` | `android:gravity` | `0x00000011` |
| 9 | `TextView` | `android:id` | `@id/tv_set_experience_slider_title` |
| 10 | `TextView` | `android:layout_width` | `0.000000dip` |
| 11 | `TextView` | `android:layout_height` | `wrap_content` |
| 12 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 13 | `TextView` | `android:text` | `@string/onboarding_set_experience_title` |
| 14 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 15 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 16 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 17 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 18 | `TextView` | `style` | `@style/TextH1` |
| 19 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/iv_set_experience_animation` |
| 20 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `0.000000dip` |
| 21 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `0.000000dip` |
| 22 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 23 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constrainedHeight` | `true` |
| 24 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintBottom_toTopOf` | `@id/layout_set_experience_slider_and_text` |
| 25 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 26 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintHeight_max` | `200.000000dip` |
| 27 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_experience_slider_title` |
| 29 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 30 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveAutoPlay` | `true` |
| 31 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveLoop` | `0` |
| 32 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveResource` | `@raw/experience` |
| 33 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 34 | `LinearLayout` | `android:orientation` | `vertical` |
| 35 | `LinearLayout` | `android:id` | `@id/layout_set_experience_slider_and_text` |
| 36 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 37 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 38 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 39 | `LinearLayout` | `android:layout_marginVertical` | `@dimen/spacing_s` |
| 40 | `LinearLayout` | `app:layout_constraintBottom_toTopOf` | `@id/compose_content` |
| 41 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 42 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 43 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/iv_set_experience_animation` |
| 44 | `com.getmimo.ui.common.SeekBarWithIntervals` | `android:id` | `@id/seekbar_set_experience` |
| 45 | `com.getmimo.ui.common.SeekBarWithIntervals` | `android:layout_width` | `match_parent` |
| 46 | `com.getmimo.ui.common.SeekBarWithIntervals` | `android:layout_height` | `wrap_content` |
| 47 | `com.getmimo.ui.common.SeekBarWithIntervals` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 48 | `TextView` | `android:gravity` | `0x00000031` |
| 49 | `TextView` | `android:id` | `@id/tv_set_experience_slider_description` |
| 50 | `TextView` | `android:layout_width` | `match_parent` |
| 51 | `TextView` | `android:layout_height` | `wrap_content` |
| 52 | `TextView` | `android:layout_marginBottom` | `@dimen/onboarding_container_slider_description_margin_bottom` |
| 53 | `TextView` | `android:text` | `@string/onboarding_set_experience_none_description` |
| 54 | `TextView` | `android:maxLines` | `2` |
| 55 | `TextView` | `android:lines` | `2` |
| 56 | `TextView` | `android:minLines` | `2` |
| 57 | `TextView` | `style` | `@style/TextViewOnBoardingPageDescription` |
| 58 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_content` |
| 59 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 60 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 61 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 62 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 63 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/onboarding_container_slider_description_margin_bottom` | `8.000000dip` / `8.000000dip` (sw320dp-xhdpi) / `26.000000dip` (sw320dp-xxhdpi) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/onboarding_set_experience_none_description` | `You're about to write your first line of code` / `Du bist dabei, deine erste Zeile Code zu schreiben` (de) / `Estás a punto de escribir tu primera línea de código` (es) / `Tu es sur le point d'écrire ta première ligne de code` (fr) / `Kamu akan menulis baris kode pertamamu` (in) / `Stai per scrivere la tua prima riga di codice` (it) / `Zaraz napiszesz swoją pierwszą linijkę kodu` (pl) / `Você está prestes a escrever sua primeira linha de código` (pt-rBR) / `Ты собираешься написать свою первую строку кода` (ru) / `İlk kod satırını yazmak üzeresin` (tr) |
| `@string/onboarding_set_experience_title` | `How much coding experience do you have?` / `Wieviel Programmiererfahrung hast du?` (de) / `¿Cuánta experiencia tienes en programación?` (es) / `Quelle est ton expérience en matière de codage?` (fr) / `Seberapa banyak pengalaman kodingmu?` (in) / `Quanta esperienza hai con il coding?` (it) / `Ile masz doświadczenia w kodowaniu?` (pl) / `Qual seu nível de experiência com programação?` (pt-rBR) / `У тебя есть опыт в программировании?` (ru) / `Ne kadar kodlama deneyimin var?` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextViewOnBoardingPageDescription` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/compose_content
@id/iv_set_experience_animation
@id/layout_set_experience_slider_and_text
@id/seekbar_set_experience
@id/tv_set_experience_slider_description
@id/tv_set_experience_slider_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.OnboardingActivity
com.getmimo.ui.onboarding.step2.SetExperienceFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000031" android:layout_width="match_parent" android:layout_height="match_parent" android:layout_marginBottom="@dimen/spacing_m" android:maxWidth="@dimen/general_max_width" android:layout_marginHorizontal="@dimen/spacing_l">
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_set_experience_slider_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/onboarding_set_experience_title" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
  <app.rive.runtime.kotlin.RiveAnimationView android:id="@id/iv_set_experience_animation" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_marginTop="@dimen/spacing_m" app:layout_constrainedHeight="true" app:layout_constraintBottom_toTopOf="@id/layout_set_experience_slider_and_text" app:layout_constraintEnd_toEndOf="0" app:layout_constraintHeight_max="200.000000dip" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_set_experience_slider_title" app:layout_constraintVertical_chainStyle="2" app:riveAutoPlay="true" app:riveLoop="0" app:riveResource="@raw/experience"/>
  <LinearLayout android:gravity="0x00000011" android:orientation="vertical" android:id="@id/layout_set_experience_slider_and_text" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_xs" android:layout_marginVertical="@dimen/spacing_s" app:layout_constraintBottom_toTopOf="@id/compose_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_set_experience_animation">
    <com.getmimo.ui.common.SeekBarWithIntervals android:id="@id/seekbar_set_experience" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l"/>
    <TextView android:gravity="0x00000031" android:id="@id/tv_set_experience_slider_description" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/onboarding_container_slider_description_margin_bottom" android:text="@string/onboarding_set_experience_none_description" android:maxLines="2" android:lines="2" android:minLines="2" style="@style/TextViewOnBoardingPageDescription"/>
  </LinearLayout>
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_content" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
