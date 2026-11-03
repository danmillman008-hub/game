# پروندهٔ لایه — `res/layout/quiz_introduction_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/quiz_introduction_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/quiz_introduction_fragment.xml`](../../SOURCE/res/layout/quiz_introduction_fragment.xml) |
| SHA-256 دیکد | `1f3cb40eb57e26ea64f954010e351ee737137bef866610c8a9847a9bb166dc38` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 18 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_quiz_introduction
   ├─ TextView  #@id/tv_quiz_introduction_title
   ├─ TextView  #@id/tv_quiz_introduction_description
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_start_quiz
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_not_now
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `ImageView` | `android:id` | `@id/iv_quiz_introduction` |
| 5 | `ImageView` | `android:layout_width` | `180.000000dip` |
| 6 | `ImageView` | `android:layout_height` | `wrap_content` |
| 7 | `ImageView` | `android:layout_marginBottom` | `@dimen/spacing_xl_expandable` |
| 8 | `ImageView` | `android:src` | `@drawable/ic_survey` |
| 9 | `ImageView` | `android:adjustViewBounds` | `true` |
| 10 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_quiz_introduction_title` |
| 11 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `ImageView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 15 | `TextView` | `android:textAppearance` | `@style/TextH1` |
| 16 | `TextView` | `android:textColor` | `@color/text_primary` |
| 17 | `TextView` | `android:gravity` | `0x00000001` |
| 18 | `TextView` | `android:id` | `@id/tv_quiz_introduction_title` |
| 19 | `TextView` | `android:layout_width` | `0.000000dip` |
| 20 | `TextView` | `android:layout_height` | `wrap_content` |
| 21 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs_expandable` |
| 22 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_xs_expandable` |
| 23 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_l_expandable` |
| 24 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_l_expandable` |
| 25 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_quiz_introduction_description` |
| 26 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_quiz_introduction` |
| 29 | `TextView` | `android:textAppearance` | `@style/TextP1` |
| 30 | `TextView` | `android:textColor` | `@color/text_weak` |
| 31 | `TextView` | `android:gravity` | `0x00000001` |
| 32 | `TextView` | `android:id` | `@id/tv_quiz_introduction_description` |
| 33 | `TextView` | `android:layout_width` | `0.000000dip` |
| 34 | `TextView` | `android:layout_height` | `wrap_content` |
| 35 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs_expandable` |
| 36 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_xs_expandable` |
| 37 | `TextView` | `android:text` | `@string/quiz_introduction_description` |
| 38 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_l_expandable` |
| 39 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_l_expandable` |
| 40 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_start_quiz` |
| 41 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 42 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 43 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_quiz_introduction_title` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_start_quiz` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_s_expandable` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_s_expandable` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_not_now` |
| 51 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 52 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 53 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 54 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_not_now` |
| 55 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 56 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 57 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 58 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_s_expandable` |
| 59 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 60 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 61 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 62 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l_expandable` | `24.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@dimen/spacing_xl_expandable` | `32.000000dip` / `48.000000dip` (sw600dp) |
| `@dimen/spacing_xs_expandable` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@string/quiz_introduction_description` | `Test your knowledge on key concepts 
from past sections. Retake the quiz to 
earn a higher score and bonus XP.` / `Teste dein Wissen zu wichtigen Konzepten 
aus vorigen Abschnitten. Mache das Quiz erneut, um 
einen höheren Score und mehr Bonus-XP zu erhalten.` (de) / `Prueba tus conocimientos en conceptos clave 
sobre secciones pasadas. Haz el quiz otra vez para 
puntuar más alto y bonificar tu XP.` (es) / `Teste tes connaissances sur les concepts clés 
des rubriques précédentes. Repasse le quiz pour 
obtenir un meilleur score et des bonus d'XP.` (fr) / `Uji pengetahuanmu tentang konsep penting 
dari bagian sebelumnya. Ulangi kuis untuk 
dapat skor lebih tinggi dan bonus XP.` (in) / `Metti alla prova quello che sai sui concetti chiave 
delle sezioni precedenti. Ripeti il quiz per 
ottenere un punteggio più alto e XP bonus.` (it) / `Sprawdź wiedzę z kluczowych pojęć 
z poprzednich sekcji. Powtórz quiz, aby 
zdobyć lepszy wynik i dodatkowe XP.` (pl) / `Teste seus conhecimentos sobre os principais conceitos das seções anteriores. Refaça o quiz para obter uma pontuação mais alta e o bônus XP.` (pt-rBR) / `Проверь свои знания по ключевым понятиям 
из предыдущих разделов. Пройди проверку ещё раз, чтобы 
заработать больше очков и бонусные XP.` (ru) / `Önceki bölümlerdeki temel konularda 
bilgini sına. Daha yüksek puan ve bonus XP 
kazanmak için testi tekrar çöz.` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_not_now
@id/btn_start_quiz
@id/iv_quiz_introduction
@id/tv_quiz_introduction_description
@id/tv_quiz_introduction_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.step1.IntroductionFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <ImageView android:id="@id/iv_quiz_introduction" android:layout_width="180.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xl_expandable" android:src="@drawable/ic_survey" android:adjustViewBounds="true" app:layout_constraintBottom_toTopOf="@id/tv_quiz_introduction_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2"/>
  <TextView android:textAppearance="@style/TextH1" android:textColor="@color/text_primary" android:gravity="0x00000001" android:id="@id/tv_quiz_introduction_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs_expandable" android:layout_marginBottom="@dimen/spacing_xs_expandable" android:layout_marginStart="@dimen/spacing_l_expandable" android:layout_marginEnd="@dimen/spacing_l_expandable" app:layout_constraintBottom_toTopOf="@id/tv_quiz_introduction_description" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_quiz_introduction"/>
  <TextView android:textAppearance="@style/TextP1" android:textColor="@color/text_weak" android:gravity="0x00000001" android:id="@id/tv_quiz_introduction_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs_expandable" android:layout_marginBottom="@dimen/spacing_xs_expandable" android:text="@string/quiz_introduction_description" android:layout_marginStart="@dimen/spacing_l_expandable" android:layout_marginEnd="@dimen/spacing_l_expandable" app:layout_constraintBottom_toTopOf="@id/btn_start_quiz" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_quiz_introduction_title"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_start_quiz" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s_expandable" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginHorizontal="@dimen/spacing_s_expandable" app:layout_constraintBottom_toTopOf="@id/btn_not_now" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_not_now" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginHorizontal="@dimen/spacing_s_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
