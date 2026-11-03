# پروندهٔ لایه — `res/layout/onboarding_step_2a_set_occupation_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_step_2a_set_occupation_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_step_2a_set_occupation_fragment.xml`](../../SOURCE/res/layout/onboarding_step_2a_set_occupation_fragment.xml) |
| SHA-256 دیکد | `4c27247090d68b160172710b98b1e53d5e5fe613c606c45da47cdde7b6642ce4` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 10 |
| تعداد شناسه | 7 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 26 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_set_occupation_title
         └─ LinearLayout  #@id/layout_motive
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_high_school
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_university
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_professional
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_self_employed
            └─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_none
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000031` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `@dimen/onboarding_container_margin_bottom` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 7 | `ScrollView` | `android:layout_width` | `0.000000dip` |
| 8 | `ScrollView` | `android:layout_height` | `0.000000dip` |
| 9 | `ScrollView` | `android:fillViewport` | `true` |
| 10 | `ScrollView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 11 | `ScrollView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `ScrollView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `ScrollView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 15 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 16 | `TextView` | `android:textColor` | `@color/text_primary` |
| 17 | `TextView` | `android:gravity` | `0x00000011` |
| 18 | `TextView` | `android:id` | `@id/tv_set_occupation_title` |
| 19 | `TextView` | `android:layout_width` | `0.000000dip` |
| 20 | `TextView` | `android:layout_height` | `wrap_content` |
| 21 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 22 | `TextView` | `android:text` | `@string/onboarding_set_occupation_title` |
| 23 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 24 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 26 | `TextView` | `style` | `@style/TextH1` |
| 27 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 28 | `LinearLayout` | `android:orientation` | `vertical` |
| 29 | `LinearLayout` | `android:id` | `@id/layout_motive` |
| 30 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 31 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 32 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_xxl` |
| 33 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 35 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 36 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_occupation_title` |
| 37 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_occupation_high_school` |
| 38 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 39 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 40 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 41 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_occupation_high_school` |
| 42 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_occupation_high_school_student` |
| 43 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_occupation_university` |
| 44 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 45 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 46 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 47 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_occupation_university` |
| 48 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_occupation_university_student` |
| 49 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_occupation_professional` |
| 50 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 51 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 52 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 53 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_occupation_employed` |
| 54 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_occupation_professional` |
| 55 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_occupation_self_employed` |
| 56 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 57 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 58 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 59 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_occupation_self_employed` |
| 60 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_occupation_self_employed` |
| 61 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:id` | `@id/btn_occupation_none` |
| 62 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_width` | `match_parent` |
| 63 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_height` | `wrap_content` |
| 64 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 65 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_image` | `@drawable/img_something_else` |
| 66 | `com.getmimo.ui.onboarding.motive.OnboardingMotiveButton` | `app:motive_title` | `@string/onboarding_set_occupation_none` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/onboarding_container_margin_bottom` | `16.000000dip` / `16.000000dip` (sw320dp-xhdpi) / `32.000000dip` (sw320dp-xxhdpi) / `56.000000dip` (sw600dp) / `16.000000dip` (sw600dp-land) / `56.000000dip` (sw720dp) / `16.000000dip` (sw720dp-land) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/onboarding_set_occupation_high_school_student` | `High school student` / `Oberschüler` (de) / `Estudiante de instituto` (es) / `Étudiant de lycée` (fr) / `Pelajar SMA` (in) / `Studio alle superiori` (it) / `Uczeń szkoły średniej` (pl) / `Estudante do ensino médio` (pt-rBR) / `Старшеклассник` (ru) / `Lise öğrencisi` (tr) |
| `@string/onboarding_set_occupation_none` | `Something else` / `Etwas anderes` (de) / `Otra cosa` (es) / `Autre chose` (fr) / `Lainnya` (in) / `Altro` (it) / `Coś innego` (pl) / `Outra coisa` (pt-rBR) / `Другое` (ru) / `Başka bir şey` (tr) |
| `@string/onboarding_set_occupation_professional` | `Employed` / `Angestellt` (de) / `Empleado/a` (es) / `Salarié` (fr) / `Karyawan` (in) / `Lavoro come dipendente` (it) / `Pracownik` (pl) / `Empregado` (pt-rBR) / `Работаю` (ru) / `Çalışan` (tr) |
| `@string/onboarding_set_occupation_self_employed` | `Self-employed` / `Selbstständig` (de) / `Trabajador/a por cuenta propia` (es) / `Travailleur indépendant` (fr) / `Wiraswasta` (in) / `Lavoro in proprio` (it) / `Własna działalność` (pl) / `Autônomo` (pt-rBR) / `Самозанятый` (ru) / `Serbest çalışan` (tr) |
| `@string/onboarding_set_occupation_title` | `Which of these describes you best?` / `Was davon beschreibt dich am besten?` (de) / `¿Cuál de las siguientes te describe mejor?` (es) / `Laquelle de ces propositions te décrit le mieux?` (fr) / `Mana yang paling menggambarkan kamu?` (in) / `Quale di queste ti descrive meglio?` (it) / `Co opisuje cię najlepiej?` (pl) / `Qual destas opções melhor se aplica a você?` (pt-rBR) / `Что из этого списка описывает тебя лучше всего?` (ru) / `Hangisi seni en iyi anlatıyor?` (tr) |
| `@string/onboarding_set_occupation_university_student` | `University student` / `Universitätsstudent` (de) / `Estudiante de universidad` (es) / `Étudiant d'université` (fr) / `Mahasiswa` (in) / `Studio all'università` (it) / `Student` (pl) / `Estudante universitário` (pt-rBR) / `Студент` (ru) / `Üniversite öğrencisi` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_occupation_high_school
@id/btn_occupation_none
@id/btn_occupation_professional
@id/btn_occupation_self_employed
@id/btn_occupation_university
@id/layout_motive
@id/tv_set_occupation_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.OnboardingActivity
com.getmimo.ui.onboarding.occupation.SetOccupationFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000031" android:layout_width="match_parent" android:layout_height="match_parent" android:layout_marginBottom="@dimen/onboarding_container_margin_bottom" android:maxWidth="@dimen/general_max_width" android:layout_marginHorizontal="@dimen/spacing_l">
  <ScrollView android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:fillViewport="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
      <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_set_occupation_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/onboarding_set_occupation_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
      <LinearLayout android:gravity="0x00000011" android:orientation="vertical" android:id="@id/layout_motive" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxl" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_set_occupation_title">
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_occupation_high_school" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_occupation_high_school" app:motive_title="@string/onboarding_set_occupation_high_school_student"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_occupation_university" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_occupation_university" app:motive_title="@string/onboarding_set_occupation_university_student"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_occupation_professional" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_occupation_employed" app:motive_title="@string/onboarding_set_occupation_professional"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_occupation_self_employed" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_occupation_self_employed" app:motive_title="@string/onboarding_set_occupation_self_employed"/>
        <com.getmimo.ui.onboarding.motive.OnboardingMotiveButton android:id="@id/btn_occupation_none" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_xs" app:motive_image="@drawable/img_something_else" app:motive_title="@string/onboarding_set_occupation_none"/>
      </LinearLayout>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </ScrollView>
</androidx.constraintlayout.widget.ConstraintLayout>
```
