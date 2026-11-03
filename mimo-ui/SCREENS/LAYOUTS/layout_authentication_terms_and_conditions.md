# پروندهٔ لایه — `res/layout/authentication_terms_and_conditions.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/authentication_terms_and_conditions.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/authentication_terms_and_conditions.xml`](../../SOURCE/res/layout/authentication_terms_and_conditions.xml) |
| SHA-256 دیکد | `f4532fdcdf320b6348db8b42c696dd54a9d12867d764bfa0d9e1f14e5992d11f` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.constraintlayout.helper.widget.Flow
   ├─ LinearLayout  #@id/ll_terms_conditions_prefix
   │  ├─ TextView  #@id/tv_terms_conditions_prefix
   │  └─ TextView  #@id/tv_sing_in_terms_conditions_prefix
   └─ TextView  #@id/tv_terms
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 3 | `androidx.constraintlayout.helper.widget.Flow` | `android:layout_width` | `0.000000dip` |
| 4 | `androidx.constraintlayout.helper.widget.Flow` | `android:layout_height` | `wrap_content` |
| 5 | `androidx.constraintlayout.helper.widget.Flow` | `app:constraint_referenced_ids` | `ll_terms_conditions_prefix, tv_terms` |
| 6 | `androidx.constraintlayout.helper.widget.Flow` | `app:flow_firstHorizontalStyle` | `2` |
| 7 | `androidx.constraintlayout.helper.widget.Flow` | `app:flow_horizontalAlign` | `2` |
| 8 | `androidx.constraintlayout.helper.widget.Flow` | `app:flow_horizontalGap` | `4.000000dip` |
| 9 | `androidx.constraintlayout.helper.widget.Flow` | `app:flow_horizontalStyle` | `2` |
| 10 | `androidx.constraintlayout.helper.widget.Flow` | `app:flow_wrapMode` | `1` |
| 11 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `LinearLayout` | `android:orientation` | `horizontal` |
| 15 | `LinearLayout` | `android:id` | `@id/ll_terms_conditions_prefix` |
| 16 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 17 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 18 | `LinearLayout` | `app:layout_constraintEnd_toStartOf` | `@id/tv_terms` |
| 19 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `LinearLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 21 | `TextView` | `android:textColor` | `@color/text_weak` |
| 22 | `TextView` | `android:id` | `@id/tv_terms_conditions_prefix` |
| 23 | `TextView` | `android:layout_width` | `wrap_content` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:text` | `@string/sign_up_terms_conditions_prefix` |
| 26 | `TextView` | `style` | `@style/TextP3` |
| 27 | `TextView` | `android:textColor` | `@color/text_weak` |
| 28 | `TextView` | `android:id` | `@id/tv_sing_in_terms_conditions_prefix` |
| 29 | `TextView` | `android:visibility` | `gone` |
| 30 | `TextView` | `android:layout_width` | `wrap_content` |
| 31 | `TextView` | `android:layout_height` | `wrap_content` |
| 32 | `TextView` | `android:text` | `@string/sign_in_terms_conditions_prefix` |
| 33 | `TextView` | `style` | `@style/TextP3` |
| 34 | `TextView` | `android:textColor` | `@color/text_weak` |
| 35 | `TextView` | `android:gravity` | `0x00000011` |
| 36 | `TextView` | `android:id` | `@id/tv_terms` |
| 37 | `TextView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 38 | `TextView` | `android:focusable` | `true` |
| 39 | `TextView` | `android:clickable` | `true` |
| 40 | `TextView` | `android:layout_width` | `wrap_content` |
| 41 | `TextView` | `android:layout_height` | `wrap_content` |
| 42 | `TextView` | `android:text` | `@string/sign_up_terms_conditions_clickable_terms` |
| 43 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/ll_terms_conditions_prefix` |
| 44 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 45 | `TextView` | `style` | `@style/TextP3` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@string/sign_in_terms_conditions_prefix` | `By signing in you agree to our` / `Mit der Anmeldung akzeptierst du unsere` (de) / `Al firmar aceptas nuestros` (es) / `En t'inscrivant, tu acceptes nos` (fr) / `Dengan masuk, kamu menyetujui` (in) / `Accedendo accetti i nostri` (it) / `Logując się, akceptujesz nasz` (pl) / `Ao se inscrever, você concorda com nossos` (pt-rBR) / `Регистрируясь, ты соглашаешься на наши` (ru) / `Giriş yaparak şunları kabul edersin:` (tr) |
| `@string/sign_up_terms_conditions_clickable_terms` | `Terms of service` / `AGB` (de) / `Términos de servicio` (es) / `Conditions d'utilisation` (fr) / `Ketentuan Layanan` (in) / `Termini di servizio` (it) / `Regulamin` (pl) / `Termos de serviço` (pt-rBR) / `Условия использования` (ru) / `Hizmet Şartları` (tr) |
| `@string/sign_up_terms_conditions_prefix` | `By signing up you agree to our` / `Mit der Registrierung akzeptierst du unsere` (de) / `Al registrarte aceptas nuestros` (es) / `En t'inscrivant, tu acceptes nos` (fr) / `Dengan mendaftar, kamu menyetujui` (in) / `Registrandoti accetti i nostri` (it) / `Rejestrując się, akceptujesz nasz` (pl) / `Ao se inscrever, você concorda com nossos` (pt-rBR) / `Регистрируясь, ты соглашаешься на наши` (ru) / `Kaydolarak şunları kabul edersin:` (tr) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/ll_terms_conditions_prefix
@id/tv_sing_in_terms_conditions_prefix
@id/tv_terms
@id/tv_terms_conditions_prefix
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.authentication.AuthenticationActivity
com.getmimo.ui.authentication.AuthenticationFragment$configureButtons$2
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/authentication_fragment.xml
res/layout/authentication_login_fragment.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.constraintlayout.helper.widget.Flow android:layout_width="0.000000dip" android:layout_height="wrap_content" app:constraint_referenced_ids="ll_terms_conditions_prefix, tv_terms" app:flow_firstHorizontalStyle="2" app:flow_horizontalAlign="2" app:flow_horizontalGap="4.000000dip" app:flow_horizontalStyle="2" app:flow_wrapMode="1" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/ll_terms_conditions_prefix" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toStartOf="@id/tv_terms" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_terms_conditions_prefix" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/sign_up_terms_conditions_prefix" style="@style/TextP3"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_sing_in_terms_conditions_prefix" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/sign_in_terms_conditions_prefix" style="@style/TextP3"/>
  </LinearLayout>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_terms" android:background="?attr/selectableItemBackgroundBorderless" android:focusable="true" android:clickable="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/sign_up_terms_conditions_clickable_terms" app:layout_constraintStart_toEndOf="@id/ll_terms_conditions_prefix" app:layout_constraintTop_toTopOf="0" style="@style/TextP3"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
