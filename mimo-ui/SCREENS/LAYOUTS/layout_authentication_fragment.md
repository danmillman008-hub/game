# پروندهٔ لایه — `res/layout/authentication_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/authentication_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/authentication_fragment.xml`](../../SOURCE/res/layout/authentication_fragment.xml) |
| SHA-256 دیکد | `59634651cbf00adeb33738393900e1d333578f27016202ad0ef38ae1c4a76673` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_skip
   ├─ androidx.compose.ui.platform.ComposeView  #@id/benefits_content
   ├─ androidx.constraintlayout.widget.Barrier  #@id/footer_content
   ├─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
   ├─ include  #@id/layout_terms_conditions
   └─ TextView  #@id/tv_delete_account
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_skip` |
| 5 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 6 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 7 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 8 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |
| 9 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/benefits_content` |
| 10 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 11 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 12 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/footer_content` |
| 13 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 14 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 15 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/btn_skip` |
| 16 | `androidx.constraintlayout.widget.Barrier` | `android:id` | `@id/footer_content` |
| 17 | `androidx.constraintlayout.widget.Barrier` | `android:layout_width` | `0.000000dip` |
| 18 | `androidx.constraintlayout.widget.Barrier` | `android:layout_height` | `0.000000dip` |
| 19 | `androidx.constraintlayout.widget.Barrier` | `app:barrierDirection` | `2` |
| 20 | `androidx.constraintlayout.widget.Barrier` | `app:constraint_referenced_ids` | `layout_terms_conditions, compose_content` |
| 21 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_content` |
| 22 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 23 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 24 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 25 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/layout_terms_conditions` |
| 26 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `include` | `android:gravity` | `0x00000011` |
| 29 | `include` | `android:id` | `@id/layout_terms_conditions` |
| 30 | `include` | `android:layout_width` | `wrap_content` |
| 31 | `include` | `android:layout_height` | `wrap_content` |
| 32 | `include` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 33 | `include` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `include` | `app:layout_constraintBottom_toTopOf` | `@id/tv_delete_account` |
| 35 | `include` | `app:layout_constraintEnd_toEndOf` | `0` |
| 36 | `include` | `app:layout_constraintStart_toStartOf` | `0` |
| 37 | `include` | `layout` | `@layout/authentication_terms_and_conditions` |
| 38 | `TextView` | `android:textColor` | `@color/text_weak` |
| 39 | `TextView` | `android:gravity` | `0x00000011` |
| 40 | `TextView` | `android:id` | `@id/tv_delete_account` |
| 41 | `TextView` | `android:paddingTop` | `2.000000dip` |
| 42 | `TextView` | `android:layout_width` | `0.000000dip` |
| 43 | `TextView` | `android:layout_height` | `wrap_content` |
| 44 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 45 | `TextView` | `android:text` | `@string/login_delete_account` |
| 46 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 47 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 48 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 49 | `TextView` | `style` | `@style/TextP3` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@string/login_delete_account` | `You can delete your account in your settings` / `Deinen Account kannst du in den Einstellungen löschen` (de) / `Puedes eliminar tu cuenta en Ajustes` (es) / `Tu peux supprimer ton compte dans les paramètres` (fr) / `Kamu bisa menghapus akunmu di pengaturan` (in) / `Puoi eliminare il tuo account dalle impostazioni` (it) / `Konto możesz usunąć w ustawieniach` (pl) / `Você pode excluir sua conta em suas configurações` (pt-rBR) / `Ты можешь удалить свой аккаунт в настройках` (ru) / `Hesabını ayarlardan silebilirsin` (tr) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/benefits_content
@id/btn_skip
@id/compose_content
@id/footer_content
@id/layout_terms_conditions
@id/tv_delete_account
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
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_skip" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/benefits_content" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toTopOf="@id/footer_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/btn_skip"/>
  <androidx.constraintlayout.widget.Barrier android:id="@id/footer_content" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:barrierDirection="2" app:constraint_referenced_ids="layout_terms_conditions, compose_content"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_content" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toTopOf="@id/layout_terms_conditions" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
  <include android:gravity="0x00000011" android:id="@id/layout_terms_conditions" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintBottom_toTopOf="@id/tv_delete_account" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" layout="@layout/authentication_terms_and_conditions"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_delete_account" android:paddingTop="2.000000dip" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:text="@string/login_delete_account" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" style="@style/TextP3"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
