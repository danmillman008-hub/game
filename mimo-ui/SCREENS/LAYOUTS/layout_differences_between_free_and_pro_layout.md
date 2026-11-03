# پروندهٔ لایه — `res/layout/differences_between_free_and_pro_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/differences_between_free_and_pro_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/differences_between_free_and_pro_layout.xml`](../../SOURCE/res/layout/differences_between_free_and_pro_layout.xml) |
| SHA-256 دیکد | `a7bb01a2c1723b3d8522e024c07662b46330e187244810110f3ec3979ca38f86` |
| ریشه | `LinearLayout` |
| تعداد گره | 16 |
| تعداد شناسه | 7 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 29 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ androidx.constraintlayout.widget.ConstraintLayout
   │  ├─ TextView  #@id/tv_benefits
   │  ├─ TextView  #@id/tv_pro
   │  ├─ TextView  #@id/tv_basic
   │  ├─ TextView  #@id/tv_benefit_1
   │  ├─ ImageView
   │  ├─ ImageView
   │  ├─ TextView  #@id/tv_benefit_3
   │  ├─ ImageView
   │  ├─ TextView  #@id/tv_benefit_4
   │  └─ ImageView
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ TextView  #@id/tv_benefit_6
      ├─ ImageView
      └─ ImageView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@drawable/onboarding_pro_benefits_background_top` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingTop` | `@dimen/spacing_s` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 8 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_m` |
| 9 | `TextView` | `android:textColor` | `@color/text_primary` |
| 10 | `TextView` | `android:id` | `@id/tv_benefits` |
| 11 | `TextView` | `android:layout_width` | `wrap_content` |
| 12 | `TextView` | `android:layout_height` | `wrap_content` |
| 13 | `TextView` | `android:text` | `@string/benefits` |
| 14 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 15 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 16 | `TextView` | `style` | `@style/TextTitle2` |
| 17 | `TextView` | `android:textColor` | `@color/support_purple` |
| 18 | `TextView` | `android:id` | `@id/tv_pro` |
| 19 | `TextView` | `android:layout_width` | `wrap_content` |
| 20 | `TextView` | `android:layout_height` | `wrap_content` |
| 21 | `TextView` | `android:text` | `@string/pro` |
| 22 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 23 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 24 | `TextView` | `style` | `@style/TextTitle2` |
| 25 | `TextView` | `android:textColor` | `@color/text_primary` |
| 26 | `TextView` | `android:id` | `@id/tv_basic` |
| 27 | `TextView` | `android:layout_width` | `wrap_content` |
| 28 | `TextView` | `android:layout_height` | `wrap_content` |
| 29 | `TextView` | `android:text` | `@string/subscription_comparison_basic` |
| 30 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 31 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_pro` |
| 32 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 33 | `TextView` | `style` | `@style/TextTitle2` |
| 34 | `TextView` | `android:textColor` | `@color/text_primary` |
| 35 | `TextView` | `android:id` | `@id/tv_benefit_1` |
| 36 | `TextView` | `android:layout_width` | `0.000000dip` |
| 37 | `TextView` | `android:layout_height` | `wrap_content` |
| 38 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxs` |
| 39 | `TextView` | `android:text` | `@string/learn_on_your_phone` |
| 40 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 41 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_basic` |
| 42 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 43 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_benefits` |
| 44 | `TextView` | `style` | `@style/TextP4` |
| 45 | `ImageView` | `android:layout_width` | `wrap_content` |
| 46 | `ImageView` | `android:layout_height` | `wrap_content` |
| 47 | `ImageView` | `android:src` | `@drawable/ic_check` |
| 48 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/tv_basic` |
| 49 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/tv_basic` |
| 50 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_benefit_1` |
| 51 | `ImageView` | `android:layout_width` | `wrap_content` |
| 52 | `ImageView` | `android:layout_height` | `wrap_content` |
| 53 | `ImageView` | `android:src` | `@drawable/ic_check` |
| 54 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/tv_pro` |
| 55 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/tv_pro` |
| 56 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_benefit_1` |
| 57 | `ImageView` | `app:tint` | `@color/support_purple` |
| 58 | `TextView` | `android:textColor` | `@color/text_primary` |
| 59 | `TextView` | `android:id` | `@id/tv_benefit_3` |
| 60 | `TextView` | `android:layout_width` | `0.000000dip` |
| 61 | `TextView` | `android:layout_height` | `wrap_content` |
| 62 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 63 | `TextView` | `android:text` | `@string/keys_unlimited_keys` |
| 64 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 65 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_basic` |
| 66 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 67 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_benefit_1` |
| 68 | `TextView` | `style` | `@style/TextP4` |
| 69 | `ImageView` | `android:layout_width` | `wrap_content` |
| 70 | `ImageView` | `android:layout_height` | `wrap_content` |
| 71 | `ImageView` | `android:src` | `@drawable/ic_check` |
| 72 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/tv_pro` |
| 73 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/tv_pro` |
| 74 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_benefit_3` |
| 75 | `ImageView` | `app:tint` | `@color/support_purple` |
| 76 | `TextView` | `android:textColor` | `@color/text_primary` |
| 77 | `TextView` | `android:id` | `@id/tv_benefit_4` |
| 78 | `TextView` | `android:layout_width` | `0.000000dip` |
| 79 | `TextView` | `android:layout_height` | `wrap_content` |
| 80 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 81 | `TextView` | `android:text` | `@string/certificates_of_completion` |
| 82 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 83 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_basic` |
| 84 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 85 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_benefit_3` |
| 86 | `TextView` | `style` | `@style/TextP4` |
| 87 | `ImageView` | `android:layout_width` | `wrap_content` |
| 88 | `ImageView` | `android:layout_height` | `wrap_content` |
| 89 | `ImageView` | `android:src` | `@drawable/ic_check` |
| 90 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/tv_pro` |
| 91 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/tv_pro` |
| 92 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_benefit_4` |
| 93 | `ImageView` | `app:tint` | `@color/support_purple` |
| 94 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@drawable/onboarding_pro_benefits_background_bottom` |
| 95 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 96 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 97 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_m` |
| 98 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingVertical` | `@dimen/spacing_xxs` |
| 99 | `TextView` | `android:textColor` | `@color/text_reversed` |
| 100 | `TextView` | `android:id` | `@id/tv_benefit_6` |
| 101 | `TextView` | `android:layout_width` | `wrap_content` |
| 102 | `TextView` | `android:layout_height` | `wrap_content` |
| 103 | `TextView` | `android:text` | `@string/personal_ai_tutor` |
| 104 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 105 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 106 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 107 | `TextView` | `style` | `@style/TextTitle3` |
| 108 | `ImageView` | `android:layout_width` | `16.000000dip` |
| 109 | `ImageView` | `android:layout_height` | `16.000000dip` |
| 110 | `ImageView` | `android:src` | `@drawable/ic_ai_tutor` |
| 111 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_xs` |
| 112 | `ImageView` | `app:layout_constraintStart_toEndOf` | `@id/tv_benefit_6` |
| 113 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_benefit_6` |
| 114 | `ImageView` | `app:tint` | `@color/primary_on_reversed` |
| 115 | `ImageView` | `android:layout_width` | `wrap_content` |
| 116 | `ImageView` | `android:layout_height` | `wrap_content` |
| 117 | `ImageView` | `android:src` | `@drawable/ic_check` |
| 118 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/tv_benefit_6` |
| 119 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 120 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_benefit_6` |
| 121 | `ImageView` | `app:tint` | `@color/support_purple` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/primary_on_reversed` | `#FFB89CED` / `#FF7E4BDE` (night) |
| `@color/support_purple` | `#FF7E4BDE` / `#FFB99AF4` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_reversed` | `#FFFFFFFF` / `#FF252746` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@string/benefits` | `Benefits` / `Vorteile` (de) / `Beneficios` (es) / `Avantages` (fr) / `Manfaat` (in) / `Vantaggi` (it) / `Korzyści` (pl) / `Benefícios` (pt-rBR) / `Преимущества` (ru) / `Avantajlar` (tr) |
| `@string/certificates_of_completion` | `Certificates of completion` / `Abschlusszertifikate` (de) / `Certificados de finalización` (es) / `Certificat d'accomplissement` (fr) / `Sertifikat penyelesaian` (in) / `Certificati di completamento` (it) / `Certyfikaty ukończenia` (pl) / `Certificados de conclusão` (pt-rBR) / `Certificates of completion` (ru) / `Tamamlama sertifikaları` (tr) |
| `@string/keys_unlimited_keys` | `Unlimited keys` / `Unbegrenzte Schlüssel` (de) / `Llaves ilimitadas` (es) / `Clés illimitées` (fr) / `Kunci tanpa batas` (in) / `Chiavi illimitate` (it) / `Nielimitowane klucze` (pl) / `Chaves ilimitadas` (pt-rBR) / `Неограниченные ключи` (ru) / `Sınırsız anahtar` (tr) |
| `@string/learn_on_your_phone` | `Learn on your phone` / `Lerne auf deinem Telefon` (de) / `Aprende en tu móvil` (es) / `Apprends sur ton téléphone` (fr) / `Belajar di ponselmu` (in) / `Impara dal telefono` (it) / `Ucz się na telefonie` (pl) / `Aprenda do seu celular` (pt-rBR) / `Учись на своем телефоне` (ru) / `Telefonundan öğren` (tr) |
| `@string/personal_ai_tutor` | `Personal AI tutor` / `Persönlicher AI-Tutor` (de) / `Tutor AI Personal` (es) / `Tuteur IA personnel` (fr) / `Tutor AI pribadi` (in) / `Tutor AI personale` (it) / `Osobisty tutor AI` (pl) / `Tutor IA pessoal` (pt-rBR) / `Персональный AI помощник` (ru) / `Kişisel yapay zeka öğretmeni` (tr) |
| `@string/pro` | `Pro` / `Pro` (de) / `Pro` (es) / `Pro` (fr) / `Pro` (in) / `Pro` (it) / `Pro` (pl) / `Pro` (pt-rBR) / `Pro` (ru) / `Pro` (tr) |
| `@string/subscription_comparison_basic` | `Basic` / `Basic` (de) / `Basic` (es) / `Basique` (fr) / `Basic` (in) / `Base` (it) / `Podstawowy` (pl) / `Básico` (pt-rBR) / `Basic` (ru) / `Temel` (tr) |
| `@style/TextP4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/tv_basic
@id/tv_benefit_1
@id/tv_benefit_3
@id/tv_benefit_4
@id/tv_benefit_6
@id/tv_benefits
@id/tv_pro
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/free_trial_honest_fragment.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
  <androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" android:background="@drawable/onboarding_pro_benefits_background_top" android:paddingTop="@dimen/spacing_s" android:layout_width="match_parent" android:layout_height="wrap_content" android:paddingHorizontal="@dimen/spacing_m">
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_benefits" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/benefits" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle2"/>
    <TextView android:textColor="@color/support_purple" android:id="@id/tv_pro" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/pro" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle2"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_basic" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/subscription_comparison_basic" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toStartOf="@id/tv_pro" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle2"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_benefit_1" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxs" android:text="@string/learn_on_your_phone" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintEnd_toStartOf="@id/tv_basic" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_benefits" style="@style/TextP4"/>
    <ImageView android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/ic_check" app:layout_constraintEnd_toEndOf="@id/tv_basic" app:layout_constraintStart_toStartOf="@id/tv_basic" app:layout_constraintTop_toTopOf="@id/tv_benefit_1"/>
    <ImageView android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/ic_check" app:layout_constraintEnd_toEndOf="@id/tv_pro" app:layout_constraintStart_toStartOf="@id/tv_pro" app:layout_constraintTop_toTopOf="@id/tv_benefit_1" app:tint="@color/support_purple"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_benefit_3" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:text="@string/keys_unlimited_keys" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintEnd_toStartOf="@id/tv_basic" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_benefit_1" style="@style/TextP4"/>
    <ImageView android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/ic_check" app:layout_constraintEnd_toEndOf="@id/tv_pro" app:layout_constraintStart_toStartOf="@id/tv_pro" app:layout_constraintTop_toTopOf="@id/tv_benefit_3" app:tint="@color/support_purple"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_benefit_4" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:text="@string/certificates_of_completion" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintEnd_toStartOf="@id/tv_basic" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_benefit_3" style="@style/TextP4"/>
    <ImageView android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/ic_check" app:layout_constraintEnd_toEndOf="@id/tv_pro" app:layout_constraintStart_toStartOf="@id/tv_pro" app:layout_constraintTop_toTopOf="@id/tv_benefit_4" app:tint="@color/support_purple"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
  <androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" android:background="@drawable/onboarding_pro_benefits_background_bottom" android:layout_width="match_parent" android:layout_height="wrap_content" android:paddingHorizontal="@dimen/spacing_m" android:paddingVertical="@dimen/spacing_xxs">
    <TextView android:textColor="@color/text_reversed" android:id="@id/tv_benefit_6" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/personal_ai_tutor" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle3"/>
    <ImageView android:layout_width="16.000000dip" android:layout_height="16.000000dip" android:src="@drawable/ic_ai_tutor" android:layout_marginStart="@dimen/spacing_xs" app:layout_constraintStart_toEndOf="@id/tv_benefit_6" app:layout_constraintTop_toTopOf="@id/tv_benefit_6" app:tint="@color/primary_on_reversed"/>
    <ImageView android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/ic_check" app:layout_constraintBottom_toBottomOf="@id/tv_benefit_6" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="@id/tv_benefit_6" app:tint="@color/support_purple"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</LinearLayout>
```
