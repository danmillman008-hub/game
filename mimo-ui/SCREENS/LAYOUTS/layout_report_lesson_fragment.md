# پروندهٔ لایه — `res/layout/report_lesson_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/report_lesson_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/report_lesson_fragment.xml`](../../SOURCE/res/layout/report_lesson_fragment.xml) |
| SHA-256 دیکد | `0e4e581c311999578b8a252e533ca381a0b2c10265066c178d98edd25451b6b7` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 10 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 28 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ FrameLayout  #@id/report_lesson_header
   │  ├─ TextView  #@id/tv_report_lesson_header
   │  └─ ImageButton  #@id/btn_report_lesson_close
   ├─ androidx.core.widget.NestedScrollView  #@id/nsv_report_content
   │  └─ androidx.constraintlayout.widget.ConstraintLayout
   │     ├─ TextView  #@id/tv_report_lesson_title
   │     └─ ViewFlipper  #@id/vf_report_lesson_view_flipper
   │        ├─ com.getmimo.ui.common.ChoiceCard  #@id/layout_report_lesson_choice_card
   │        └─ com.google.android.material.textfield.TextInputLayout
   │           └─ com.google.android.material.textfield.TextInputEditText  #@id/et_report_lesson_feedback
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_report_lesson_report
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `FrameLayout` | `android:id` | `@id/report_lesson_header` |
| 5 | `FrameLayout` | `android:background` | `@color/background_secondary` |
| 6 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 7 | `FrameLayout` | `android:layout_height` | `@dimen/toolbar_height` |
| 8 | `FrameLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 9 | `TextView` | `android:textColor` | `@color/text_weak` |
| 10 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 11 | `TextView` | `android:id` | `@id/tv_report_lesson_header` |
| 12 | `TextView` | `android:layout_width` | `wrap_content` |
| 13 | `TextView` | `android:layout_height` | `wrap_content` |
| 14 | `TextView` | `android:text` | `@string/report_lesson_header` |
| 15 | `TextView` | `style` | `@style/TextH4` |
| 16 | `ImageButton` | `android:layout_gravity` | `0x00800015` |
| 17 | `ImageButton` | `android:id` | `@id/btn_report_lesson_close` |
| 18 | `ImageButton` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 19 | `ImageButton` | `android:padding` | `@dimen/spacing_xxs` |
| 20 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 21 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 22 | `ImageButton` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 23 | `ImageButton` | `app:srcCompat` | `@drawable/ic_close` |
| 24 | `ImageButton` | `app:tint` | `@color/icon_weak` |
| 25 | `androidx.core.widget.NestedScrollView` | `android:id` | `@id/nsv_report_content` |
| 26 | `androidx.core.widget.NestedScrollView` | `android:layout_width` | `match_parent` |
| 27 | `androidx.core.widget.NestedScrollView` | `android:layout_height` | `0.000000dip` |
| 28 | `androidx.core.widget.NestedScrollView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 29 | `androidx.core.widget.NestedScrollView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_report_lesson_report` |
| 30 | `androidx.core.widget.NestedScrollView` | `app:layout_constraintTop_toBottomOf` | `@id/report_lesson_header` |
| 31 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 32 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 33 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginTop` | `80.000000dip` |
| 34 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 35 | `TextView` | `android:textColor` | `@color/text_primary` |
| 36 | `TextView` | `android:gravity` | `0x00000011` |
| 37 | `TextView` | `android:id` | `@id/tv_report_lesson_title` |
| 38 | `TextView` | `android:layout_width` | `match_parent` |
| 39 | `TextView` | `android:layout_height` | `wrap_content` |
| 40 | `TextView` | `android:text` | `@string/report_lesson_title` |
| 41 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 42 | `TextView` | `style` | `@style/TextH1` |
| 43 | `ViewFlipper` | `android:id` | `@id/vf_report_lesson_view_flipper` |
| 44 | `ViewFlipper` | `android:layout_width` | `0.000000dip` |
| 45 | `ViewFlipper` | `android:layout_height` | `wrap_content` |
| 46 | `ViewFlipper` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 47 | `ViewFlipper` | `app:layout_constraintEnd_toEndOf` | `0` |
| 48 | `ViewFlipper` | `app:layout_constraintStart_toStartOf` | `0` |
| 49 | `ViewFlipper` | `app:layout_constraintTop_toBottomOf` | `@id/tv_report_lesson_title` |
| 50 | `ViewFlipper` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 51 | `com.getmimo.ui.common.ChoiceCard` | `android:id` | `@id/layout_report_lesson_choice_card` |
| 52 | `com.getmimo.ui.common.ChoiceCard` | `android:layout_width` | `match_parent` |
| 53 | `com.getmimo.ui.common.ChoiceCard` | `android:layout_height` | `wrap_content` |
| 54 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `match_parent` |
| 55 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 56 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 57 | `com.google.android.material.textfield.TextInputEditText` | `android:gravity` | `0x00000030` |
| 58 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_report_lesson_feedback` |
| 59 | `com.google.android.material.textfield.TextInputEditText` | `android:padding` | `@dimen/spacing_m` |
| 60 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 61 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 62 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/report_lesson_other_hint` |
| 63 | `com.google.android.material.textfield.TextInputEditText` | `android:minLines` | `5` |
| 64 | `com.google.android.material.textfield.TextInputEditText` | `android:maxLength` | `1000` |
| 65 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 66 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_report_lesson_report` |
| 67 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 68 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 69 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 70 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 71 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 72 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 73 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 74 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@dimen/toolbar_height` | `56.000000dip` |
| `@string/report_lesson_header` | `Lesson report` / `Lektion melden` (de) / `Reporte de lección` (es) / `Signaler l'exercice` (fr) / `Laporan pelajaran` (in) / `Segnalazione lezione` (it) / `Zgłoszenie lekcji` (pl) / `Reportar exercício` (pt-rBR) / `Пожаловаться на задание` (ru) / `Ders geri bildirimi` (tr) |
| `@string/report_lesson_other_hint` | `Please explain your issue in more detail` / `Bitte beschreibe das Problem detaillierter` (de) / `Por favor, explica el problema en más detalle` (es) / `Explique ton problème plus en détail` (fr) / `Jelaskan masalahnya lebih detail` (in) / `Spiega il problema più nel dettaglio` (it) / `Opisz problem dokładniej` (pl) / `Explique seu problema com mais detalhes` (pt-rBR) / `Пожалуйста, расскажи подробнее, в чём проблема` (ru) / `Lütfen sorununu biraz daha ayrıntılı anlat` (tr) |
| `@string/report_lesson_title` | `Report Exercise` / `Übung melden` (de) / `Reportar Ejercicio` (es) / `Rapport sur l'exercice` (fr) / `Laporkan Latihan` (in) / `Segnala esercizio` (it) / `Zgłoś ćwiczenie` (pl) / `Reportar exercício` (pt-rBR) / `Пожаловаться на урок` (ru) / `Alıştırmayı Bildir` (tr) |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_report_lesson_close
@id/btn_report_lesson_report
@id/et_report_lesson_feedback
@id/layout_report_lesson_choice_card
@id/nsv_report_content
@id/report_lesson_header
@id/tv_report_lesson_header
@id/tv_report_lesson_title
@id/vf_report_lesson_view_flipper
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.lesson.report.ReportLessonFragment$onViewCreated$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <FrameLayout android:id="@id/report_lesson_header" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" app:layout_constraintTop_toTopOf="0">
    <TextView android:textColor="@color/text_weak" android:layout_gravity="0x00000011" android:id="@id/tv_report_lesson_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/report_lesson_header" style="@style/TextH4"/>
    <ImageButton android:layout_gravity="0x00800015" android:id="@id/btn_report_lesson_close" android:background="?attr/selectableItemBackgroundBorderless" android:padding="@dimen/spacing_xxs" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_m" app:srcCompat="@drawable/ic_close" app:tint="@color/icon_weak"/>
  </FrameLayout>
  <androidx.core.widget.NestedScrollView android:id="@id/nsv_report_content" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_marginBottom="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/btn_report_lesson_report" app:layout_constraintTop_toBottomOf="@id/report_lesson_header">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="80.000000dip" android:layout_marginHorizontal="@dimen/spacing_m">
      <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_report_lesson_title" android:layout_width="match_parent" android:layout_height="wrap_content" android:text="@string/report_lesson_title" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
      <ViewFlipper android:id="@id/vf_report_lesson_view_flipper" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_report_lesson_title" app:layout_constraintWidth_max="@dimen/general_max_width">
        <com.getmimo.ui.common.ChoiceCard android:id="@id/layout_report_lesson_choice_card" android:layout_width="match_parent" android:layout_height="wrap_content"/>
        <com.google.android.material.textfield.TextInputLayout android:layout_width="match_parent" android:layout_height="wrap_content" style="@style/MaterialEditTextLayout">
          <com.google.android.material.textfield.TextInputEditText android:gravity="0x00000030" android:id="@id/et_report_lesson_feedback" android:padding="@dimen/spacing_m" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/report_lesson_other_hint" android:minLines="5" android:maxLength="1000" style="@style/MaterialEditText"/>
        </com.google.android.material.textfield.TextInputLayout>
      </ViewFlipper>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </androidx.core.widget.NestedScrollView>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_report_lesson_report" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
