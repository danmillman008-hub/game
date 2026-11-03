# پروندهٔ لایه — `res/layout/certificate_upgrade_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/certificate_upgrade_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/certificate_upgrade_activity.xml`](../../SOURCE/res/layout/certificate_upgrade_activity.xml) |
| SHA-256 دیکد | `3da9d205173a6570a259e1a3c88a67df5e75d25b779a82ab8b38348d2bb68333` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 13 |
| تعداد شناسه | 8 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 28 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ LinearLayout  #@id/ll_certificate_upgrade
   │  ├─ ImageView  #@id/iv_badge
   │  ├─ TextView
   │  └─ TextView  #@id/tv_user_name
   ├─ TextView  #@id/tv_title
   ├─ LinearLayout  #@id/ll_advantages_upgrade
   │  ├─ TextView
   │  ├─ TextView
   │  └─ TextView
   ├─ TextView  #@id/tv_secured_by
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_upgrade
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_no_thanks
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 3 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 4 | `LinearLayout` | `android:orientation` | `vertical` |
| 5 | `LinearLayout` | `android:id` | `@id/ll_certificate_upgrade` |
| 6 | `LinearLayout` | `android:background` | `@drawable/certificate_upgrade_background` |
| 7 | `LinearLayout` | `android:padding` | `@dimen/spacing_l` |
| 8 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 9 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 10 | `LinearLayout` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 11 | `LinearLayout` | `app:layout_constraintBottom_toTopOf` | `@id/tv_title` |
| 12 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `LinearLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `LinearLayout` | `app:layout_constraintVertical_chainStyle` | `2` |
| 16 | `ImageView` | `android:id` | `@id/iv_badge` |
| 17 | `ImageView` | `android:layout_width` | `44.000000dip` |
| 18 | `ImageView` | `android:layout_height` | `60.000000dip` |
| 19 | `ImageView` | `android:src` | `@drawable/ic_badge_fullstack` |
| 20 | `TextView` | `android:textColor` | `@color/support_purple` |
| 21 | `TextView` | `android:gravity` | `0x00000011` |
| 22 | `TextView` | `android:layout_width` | `wrap_content` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 25 | `TextView` | `android:text` | `CERTIFICATE OF COMPLETION` |
| 26 | `TextView` | `style` | `@style/TextTitle1` |
| 27 | `TextView` | `android:textColor` | `#FF2C2E4A` |
| 28 | `TextView` | `android:id` | `@id/tv_user_name` |
| 29 | `TextView` | `android:layout_width` | `wrap_content` |
| 30 | `TextView` | `android:layout_height` | `wrap_content` |
| 31 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 32 | `TextView` | `style` | `@style/TextH4` |
| 33 | `TextView` | `android:textColor` | `@color/text_primary` |
| 34 | `TextView` | `android:gravity` | `0x00000011` |
| 35 | `TextView` | `android:id` | `@id/tv_title` |
| 36 | `TextView` | `android:layout_width` | `0.000000dip` |
| 37 | `TextView` | `android:layout_height` | `wrap_content` |
| 38 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_xl` |
| 39 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 40 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/ll_advantages_upgrade` |
| 41 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 42 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 43 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/ll_certificate_upgrade` |
| 44 | `TextView` | `style` | `@style/TextH1` |
| 45 | `LinearLayout` | `android:orientation` | `vertical` |
| 46 | `LinearLayout` | `android:id` | `@id/ll_advantages_upgrade` |
| 47 | `LinearLayout` | `android:background` | `@drawable/rounded_background_secondary` |
| 48 | `LinearLayout` | `android:padding` | `@dimen/spacing_m` |
| 49 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 50 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 51 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 52 | `LinearLayout` | `app:layout_constraintBottom_toTopOf` | `@id/tv_secured_by` |
| 53 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 54 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 55 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_title` |
| 56 | `TextView` | `android:textColor` | `@color/text_primary` |
| 57 | `TextView` | `android:gravity` | `0x00000011` |
| 58 | `TextView` | `android:layout_width` | `wrap_content` |
| 59 | `TextView` | `android:layout_height` | `wrap_content` |
| 60 | `TextView` | `android:text` | `@string/certificate_upselling_boost_your_learning` |
| 61 | `TextView` | `android:drawablePadding` | `@dimen/spacing_m` |
| 62 | `TextView` | `app:drawableStartCompat` | `@drawable/ic_check` |
| 63 | `TextView` | `style` | `@style/TextP2` |
| 64 | `TextView` | `android:textColor` | `@color/text_primary` |
| 65 | `TextView` | `android:layout_width` | `wrap_content` |
| 66 | `TextView` | `android:layout_height` | `wrap_content` |
| 67 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 68 | `TextView` | `android:text` | `@string/certificate_upselling_likely_to_finish` |
| 69 | `TextView` | `android:drawablePadding` | `@dimen/spacing_m` |
| 70 | `TextView` | `app:drawableStartCompat` | `@drawable/ic_check` |
| 71 | `TextView` | `style` | `@style/TextP2` |
| 72 | `TextView` | `android:textColor` | `@color/text_primary` |
| 73 | `TextView` | `android:layout_width` | `wrap_content` |
| 74 | `TextView` | `android:layout_height` | `wrap_content` |
| 75 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 76 | `TextView` | `android:text` | `@string/certificate_upselling_download_all` |
| 77 | `TextView` | `android:drawablePadding` | `@dimen/spacing_m` |
| 78 | `TextView` | `app:drawableStartCompat` | `@drawable/ic_check` |
| 79 | `TextView` | `style` | `@style/TextP2` |
| 80 | `TextView` | `android:gravity` | `0x00000011` |
| 81 | `TextView` | `android:id` | `@id/tv_secured_by` |
| 82 | `TextView` | `android:layout_width` | `wrap_content` |
| 83 | `TextView` | `android:layout_height` | `wrap_content` |
| 84 | `TextView` | `android:text` | `@string/upgrade_modal_cancel_anytime` |
| 85 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 86 | `TextView` | `android:layout_marginVertical` | `@dimen/spacing_m` |
| 87 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_upgrade` |
| 88 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 89 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 90 | `TextView` | `style` | `@style/TextP2` |
| 91 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_upgrade` |
| 92 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 93 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 94 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 95 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 96 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_no_thanks` |
| 97 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 98 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 99 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_no_thanks` |
| 100 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 101 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 102 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_xxl` |
| 103 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 104 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 105 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/support_purple` | `#FF7E4BDE` / `#FFB99AF4` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/certificate_upselling_boost_your_learning` | `Boost your learning with Pro` / `Fördere dein Lernen mit Pro` (de) / `Potencia tu aprendizaje con Pro` (es) / `Booste ton apprentissage avec Pro` (fr) / `Tingkatkan belajarmu dengan Pro` (in) / `Accelera il tuo apprendimento con Pro` (it) / `Przyspiesz naukę z Pro` (pl) / `Acelere seu aprendizado com Pro` (pt-rBR) / `Улучши свое обучение с Pro` (ru) / `Öğrenmeni Pro ile hızlandır` (tr) |
| `@string/certificate_upselling_download_all` | `Download all earned certificates` / `Lade all deine verdienten Zertifikate herunter` (de) / `Descarga todos los certificados obtenidos` (es) / `Télécharge tous les certificats obtenus` (fr) / `Unduh semua sertifikat yang diraih` (in) / `Scarica tutti i certificati ottenuti` (it) / `Pobierz wszystkie zdobyte certyfikaty` (pl) / `Baixe todos os certificados conquistados` (pt-rBR) / `Скачать все заработанные сертификаты` (ru) / `Kazandığın tüm sertifikaları indir` (tr) |
| `@string/certificate_upselling_likely_to_finish` | `Pro-users are 4x likely to finish` / `Pro-Nutzende schließen 4x wahrscheinlicher ab` (de) / `Las personas que usan Pro tienen un 4x más de probabilidad de terminar` (es) / `Les utilisateurs professionnels sont 4x fois plus susceptibles de terminer` (fr) / `Pelajar Pro 4x lebih mungkin selesai` (in) / `Con Pro le probabilità di finire sono 4 volte più alte` (it) / `Osoby z Pro kończą 4x częściej` (pl) / `Usuários Pro tem 4x mais chances de concluir o curso` (pt-rBR) / `Про-пользователи имеют в 4x раза больше шансов закончить` (ru) / `Pro kullanıcılarının bitirme olasılığı 4 kat fazla` (tr) |
| `@string/upgrade_modal_cancel_anytime` | `Secured by Google Play. Cancel anytime.` / `Gesichert durch Google Play. Jederzeit kündigen.` (de) / `Validado por Google Play. Cancela en cualquier momento.` (es) / `Sécurisé par Google Play. Annule à tout moment.` (fr) / `Diamankan oleh Google Play. Batalkan kapan saja.` (in) / `Pagamento sicuro con Google Play. Disdici quando vuoi.` (it) / `Zabezpieczone przez Google Play. Anuluj w każdej chwili.` (pl) / `Protegido pelo Google Play. Cancele a qualquer momento.` (pt-rBR) / `Защищено Google Play. Отмени в любое время.` (ru) / `Google Play güvencesiyle. İstediğin zaman iptal et.` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_no_thanks
@id/btn_upgrade
@id/iv_badge
@id/ll_advantages_upgrade
@id/ll_certificate_upgrade
@id/tv_secured_by
@id/tv_title
@id/tv_user_name
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.certificates.CertificateActivity
com.getmimo.ui.certificateupgrade.CertificateUpgradeActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <LinearLayout android:gravity="0x00000011" android:orientation="vertical" android:id="@id/ll_certificate_upgrade" android:background="@drawable/certificate_upgrade_background" android:padding="@dimen/spacing_l" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/tv_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2">
    <ImageView android:id="@id/iv_badge" android:layout_width="44.000000dip" android:layout_height="60.000000dip" android:src="@drawable/ic_badge_fullstack"/>
    <TextView android:textColor="@color/support_purple" android:gravity="0x00000011" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="CERTIFICATE OF COMPLETION" style="@style/TextTitle1"/>
    <TextView android:textColor="#FF2C2E4A" android:id="@id/tv_user_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" style="@style/TextH4"/>
  </LinearLayout>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xl" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/ll_advantages_upgrade" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/ll_certificate_upgrade" style="@style/TextH1"/>
  <LinearLayout android:orientation="vertical" android:id="@id/ll_advantages_upgrade" android:background="@drawable/rounded_background_secondary" android:padding="@dimen/spacing_m" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/tv_secured_by" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_title">
    <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/certificate_upselling_boost_your_learning" android:drawablePadding="@dimen/spacing_m" app:drawableStartCompat="@drawable/ic_check" style="@style/TextP2"/>
    <TextView android:textColor="@color/text_primary" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/certificate_upselling_likely_to_finish" android:drawablePadding="@dimen/spacing_m" app:drawableStartCompat="@drawable/ic_check" style="@style/TextP2"/>
    <TextView android:textColor="@color/text_primary" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/certificate_upselling_download_all" android:drawablePadding="@dimen/spacing_m" app:drawableStartCompat="@drawable/ic_check" style="@style/TextP2"/>
  </LinearLayout>
  <TextView android:gravity="0x00000011" android:id="@id/tv_secured_by" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/upgrade_modal_cancel_anytime" android:layout_marginHorizontal="@dimen/spacing_m" android:layout_marginVertical="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/btn_upgrade" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" style="@style/TextP2"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_upgrade" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/btn_no_thanks" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_no_thanks" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xxl" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
