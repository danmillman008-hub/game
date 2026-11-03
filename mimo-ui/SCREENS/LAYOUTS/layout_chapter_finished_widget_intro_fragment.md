# پروندهٔ لایه — `res/layout/chapter_finished_widget_intro_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_finished_widget_intro_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_finished_widget_intro_fragment.xml`](../../SOURCE/res/layout/chapter_finished_widget_intro_fragment.xml) |
| SHA-256 دیکد | `14e2daa152b5192381802240814dc78601dfcb5380ad8d1a3cec13da5e371bd4` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_chapter_finished_widget_intro_fragment
   ├─ ImageView  #@id/img_widget
   ├─ TextView  #@id/widget_intro_header
   └─ androidx.compose.ui.platform.ComposeView  #@id/buttons_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/cl_chapter_finished_widget_intro_fragment` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `ImageView` | `android:id` | `@id/img_widget` |
| 6 | `ImageView` | `android:layout_width` | `wrap_content` |
| 7 | `ImageView` | `android:layout_height` | `wrap_content` |
| 8 | `ImageView` | `android:src` | `@drawable/img_widget_intro` |
| 9 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/widget_intro_header` |
| 10 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `ImageView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 14 | `TextView` | `android:textColor` | `@color/background_reversed` |
| 15 | `TextView` | `android:gravity` | `0x00000011` |
| 16 | `TextView` | `android:id` | `@id/widget_intro_header` |
| 17 | `TextView` | `android:layout_width` | `0.000000dip` |
| 18 | `TextView` | `android:layout_height` | `wrap_content` |
| 19 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 20 | `TextView` | `android:text` | `@string/chapter_end_widget_intro_title` |
| 21 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 22 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/buttons_view` |
| 23 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 24 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/img_widget` |
| 26 | `TextView` | `style` | `@style/TextH1` |
| 27 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/buttons_view` |
| 28 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 29 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 30 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/chapter_end_continue_button_margin_bottom` |
| 31 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 32 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 33 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 34 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 35 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/background_reversed` | `#FF333661` / `#FFFFFFFF` (night) |
| `@dimen/chapter_end_continue_button_margin_bottom` | `16.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@string/chapter_end_widget_intro_title` | `Add the Mimo widget to stay on track easily` / `Füge das Mimo-Widget hinzu, um leicht auf Kurs zu bleiben` (de) / `Agrega el widget de Mimo para mantenerte en camino fácilmente` (es) / `Ajoute le widget Mimo pour garder le cap facilement` (fr) / `Tambahkan widget Mimo agar mudah tetap konsisten` (in) / `Aggiungi il widget Mimo per restare in carreggiata` (it) / `Dodaj widżet Mimo, aby łatwo trzymać się planu` (pl) / `Adicione o widget do Mimo para continuar no caminho certo com facilidade` (pt-rBR) / `Добавь виджет Mimo, чтобы легко оставаться на верном пути` (ru) / `Kolayca yolunda kalmak için Mimo widget'ını ekle` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/buttons_view
@id/cl_chapter_finished_widget_intro_fragment
@id/img_widget
@id/widget_intro_header
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$onChapterFinishedContinue$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$1$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$2
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/cl_chapter_finished_widget_intro_fragment" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <ImageView android:id="@id/img_widget" android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/img_widget_intro" app:layout_constraintBottom_toTopOf="@id/widget_intro_header" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2"/>
  <TextView android:textColor="@color/background_reversed" android:gravity="0x00000011" android:id="@id/widget_intro_header" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:text="@string/chapter_end_widget_intro_title" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/buttons_view" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/img_widget" style="@style/TextH1"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/buttons_view" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/chapter_end_continue_button_margin_bottom" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
