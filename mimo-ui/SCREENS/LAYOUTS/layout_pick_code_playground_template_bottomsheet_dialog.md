# پروندهٔ لایه — `res/layout/pick_code_playground_template_bottomsheet_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/pick_code_playground_template_bottomsheet_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/pick_code_playground_template_bottomsheet_dialog.xml`](../../SOURCE/res/layout/pick_code_playground_template_bottomsheet_dialog.xml) |
| SHA-256 دیکد | `0c600d62968fb3a6e6f6f20aa8355edd8087c2ff3f2a3a804d5123448494c09d` |
| ریشه | `merge` |
| تعداد گره | 4 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ TextView  #@id/tv_pick_playground_template
      └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_pick_playground_template
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toBottomOf` | `@id/cv_bottom_sheet_header` |
| 5 | `TextView` | `android:textColor` | `@color/text_weak` |
| 6 | `TextView` | `android:id` | `@id/tv_pick_playground_template` |
| 7 | `TextView` | `android:layout_width` | `match_parent` |
| 8 | `TextView` | `android:layout_height` | `wrap_content` |
| 9 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 10 | `TextView` | `android:text` | `@string/codeplayground_template_label` |
| 11 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 12 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `TextView` | `style` | `@style/TextSubtitle` |
| 14 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_pick_playground_template` |
| 15 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `match_parent` |
| 16 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `wrap_content` |
| 17 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 18 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 19 | `androidx.recyclerview.widget.RecyclerView` | `android:nestedScrollingEnabled` | `false` |
| 20 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |
| 21 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 22 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_pick_playground_template` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@string/codeplayground_template_label` | `Select a Template` / `Wähle eine Vorlage` (de) / `Selecciona una plantilla` (es) / `Sélectionne un modèle` (fr) / `Pilih template` (in) / `Scegli un modello` (it) / `Wybierz szablon` (pl) / `Escolha um Modelo` (pt-rBR) / `Выбери шаблон` (ru) / `Bir Şablon Seç` (tr) |
| `@style/TextSubtitle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/rv_pick_playground_template
@id/tv_pick_playground_template
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.codeplayground.CodePlaygroundActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">
  <androidx.constraintlayout.widget.ConstraintLayout android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintTop_toBottomOf="@id/cv_bottom_sheet_header">
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_pick_playground_template" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:text="@string/codeplayground_template_label" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintTop_toTopOf="0" style="@style/TextSubtitle"/>
    <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_pick_playground_template" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginBottom="@dimen/spacing_l" android:nestedScrollingEnabled="false" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintTop_toBottomOf="@id/tv_pick_playground_template"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</merge>
```
