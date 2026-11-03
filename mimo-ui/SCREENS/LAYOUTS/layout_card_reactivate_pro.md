# پروندهٔ لایه — `res/layout/card_reactivate_pro.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/card_reactivate_pro.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/card_reactivate_pro.xml`](../../SOURCE/res/layout/card_reactivate_pro.xml) |
| SHA-256 دیکد | `1a821721d87cbf336e5e398a9f81963277fa059abfe8b1bd79d9235f494aad76` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 20 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView  #@id/cv_partnership_card_strive
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_reactivate_pro
      ├─ TextView  #@id/tv_reactivate_pro_title
      ├─ TextView  #@id/tv_reactivate_pro_description
      └─ TextView  #@id/btn_claim
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:id` | `@id/cv_partnership_card_strive` |
| 2 | `androidx.cardview.widget.CardView` | `android:clipChildren` | `false` |
| 3 | `androidx.cardview.widget.CardView` | `android:clipToPadding` | `false` |
| 4 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 5 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 6 | `androidx.cardview.widget.CardView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 7 | `androidx.cardview.widget.CardView` | `android:layout_marginVertical` | `@dimen/spacing_m` |
| 8 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 9 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 10 | `androidx.cardview.widget.CardView` | `app:cardElevation` | `2.000000dip` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:padding` | `@dimen/spacing_m` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 14 | `ImageView` | `android:id` | `@id/iv_reactivate_pro` |
| 15 | `ImageView` | `android:layout_width` | `wrap_content` |
| 16 | `ImageView` | `android:layout_height` | `105.000000dip` |
| 17 | `ImageView` | `android:src` | `@drawable/reactivate_pro_card` |
| 18 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/btn_claim` |
| 19 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_reactivate_pro_title` |
| 21 | `TextView` | `android:textColor` | `@color/text_primary` |
| 22 | `TextView` | `android:id` | `@id/tv_reactivate_pro_title` |
| 23 | `TextView` | `android:layout_width` | `0.000000dip` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:text` | `@string/reactivate_pro_card_title` |
| 26 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xs` |
| 27 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_reactivate_pro_description` |
| 28 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_reactivate_pro` |
| 29 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 30 | `TextView` | `style` | `@style/TextTitle1` |
| 31 | `TextView` | `android:textColor` | `@color/text_weak` |
| 32 | `TextView` | `android:id` | `@id/tv_reactivate_pro_description` |
| 33 | `TextView` | `android:layout_width` | `0.000000dip` |
| 34 | `TextView` | `android:layout_height` | `wrap_content` |
| 35 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 36 | `TextView` | `android:text` | `@string/reactivate_pro_card_description` |
| 37 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_claim` |
| 38 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 39 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/tv_reactivate_pro_title` |
| 40 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_reactivate_pro_title` |
| 41 | `TextView` | `style` | `@style/TextP2` |
| 42 | `TextView` | `android:textColor` | `@color/primary_default` |
| 43 | `TextView` | `android:id` | `@id/btn_claim` |
| 44 | `TextView` | `android:layout_width` | `0.000000dip` |
| 45 | `TextView` | `android:layout_height` | `wrap_content` |
| 46 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 47 | `TextView` | `android:text` | `@string/reactivate_pro_card_button` |
| 48 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 49 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 50 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/tv_reactivate_pro_title` |
| 51 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_reactivate_pro_description` |
| 52 | `TextView` | `style` | `@style/TextButton2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/card_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/primary_default` | `#FF7E4BDE` / `#FF885BDE` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/reactivate_pro_card_button` | `Claim 50% off` / `Hole dir 50 % Rabatt` (de) / `Pedir 50% de descuento` (es) / `Réclamer 50 % de réduction` (fr) / `Ambil diskon 50%` (in) / `Ottieni il 50% di sconto` (it) / `Odbierz 50% zniżki` (pl) / `Resgatar desconto de 50%` (pt-rBR) / `Получить 50% off` (ru) / `%50 indirimi al` (tr) |
| `@string/reactivate_pro_card_description` | `Enjoy unlimited content and support free education` / `Genieße unbegrenzten Content und unterstütze eine freie Bildung` (de) / `Disfruta de contenido ilimitado y apoyo educativo gratuito` (es) / `Profite de contenus illimités et soutiens l'éducation gratuite` (fr) / `Nikmati konten tanpa batas dan dukung edukasi gratis` (in) / `Goditi contenuti illimitati e sostieni l'istruzione gratuita` (it) / `Korzystaj z nielimitowanych treści i wspieraj darmową edukację` (pl) / `Desfrute de conteúdo ilimitado e apoie educação gratuita` (pt-rBR) / `Наслаждайся неограниченным контентом и поддержи бесплатное образование` (ru) / `Sınırsız içeriğin tadını çıkar ve ücretsiz eğitimi destekle` (tr) |
| `@string/reactivate_pro_card_title` | `Reactivate Pro` / `Pro reaktivieren` (de) / `Reactivar Pro` (es) / `Réactiver le Pro` (fr) / `Aktifkan Pro lagi` (in) / `Riattiva Pro` (it) / `Aktywuj Pro ponownie` (pl) / `Reativar Pro` (pt-rBR) / `Восстановить Pro` (ru) / `Pro'yu yeniden etkinleştir` (tr) |
| `@style/TextButton2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_claim
@id/cv_partnership_card_strive
@id/iv_reactivate_pro
@id/tv_reactivate_pro_description
@id/tv_reactivate_pro_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/cv_partnership_card_strive" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_m" android:layout_marginVertical="@dimen/spacing_m" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large" app:cardElevation="2.000000dip">
  <androidx.constraintlayout.widget.ConstraintLayout android:padding="@dimen/spacing_m" android:layout_width="match_parent" android:layout_height="wrap_content">
    <ImageView android:id="@id/iv_reactivate_pro" android:layout_width="wrap_content" android:layout_height="105.000000dip" android:src="@drawable/reactivate_pro_card" app:layout_constraintBottom_toBottomOf="@id/btn_claim" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/tv_reactivate_pro_title"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_reactivate_pro_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/reactivate_pro_card_title" android:layout_marginStart="@dimen/spacing_xs" app:layout_constraintBottom_toTopOf="@id/tv_reactivate_pro_description" app:layout_constraintStart_toEndOf="@id/iv_reactivate_pro" app:layout_constraintTop_toTopOf="0" style="@style/TextTitle1"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_reactivate_pro_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/reactivate_pro_card_description" app:layout_constraintBottom_toTopOf="@id/btn_claim" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="@id/tv_reactivate_pro_title" app:layout_constraintTop_toBottomOf="@id/tv_reactivate_pro_title" style="@style/TextP2"/>
    <TextView android:textColor="@color/primary_default" android:id="@id/btn_claim" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/reactivate_pro_card_button" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="@id/tv_reactivate_pro_title" app:layout_constraintTop_toBottomOf="@id/tv_reactivate_pro_description" style="@style/TextButton2"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.cardview.widget.CardView>
```
