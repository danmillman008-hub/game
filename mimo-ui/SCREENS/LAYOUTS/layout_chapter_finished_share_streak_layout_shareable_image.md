# پروندهٔ لایه — `res/layout/chapter_finished_share_streak_layout_shareable_image.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_finished_share_streak_layout_shareable_image.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_finished_share_streak_layout_shareable_image.xml`](../../SOURCE/res/layout/chapter_finished_share_streak_layout_shareable_image.xml) |
| SHA-256 دیکد | `1289b70070584f47db27aa83bbcc4db7523a5818554e5210039b23b37651fb3f` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 11 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 35 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_shareable_image
   ├─ ImageView
   ├─ ImageView  #@id/iv_mimo_logo
   ├─ TextView  #@id/tv_100days_of_code
   ├─ TextView  #@id/tv_nb_days_of_code
   ├─ TextView  #@id/tv_days_of_code
   ├─ com.google.android.material.progressindicator.CircularProgressIndicator  #@id/cpi_day_of_code
   ├─ TextView  #@id/tv_description
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_profile
   │  ├─ com.google.android.material.imageview.ShapeableImageView  #@id/iv_user_picture
   │  └─ TextView  #@id/tv_get_to_one_hundred
   └─ TextView  #@id/tv_mimo_app_link
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_shareable_image` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingTop` | `@dimen/spacing_xl` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `ImageView` | `android:layout_width` | `0.000000dip` |
| 7 | `ImageView` | `android:layout_height` | `0.000000dip` |
| 8 | `ImageView` | `android:src` | `@drawable/streak_share_background` |
| 9 | `ImageView` | `android:scaleType` | `fitEnd` |
| 10 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 11 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_description` |
| 14 | `ImageView` | `android:id` | `@id/iv_mimo_logo` |
| 15 | `ImageView` | `android:layout_width` | `60.000000dip` |
| 16 | `ImageView` | `android:layout_height` | `wrap_content` |
| 17 | `ImageView` | `android:src` | `@drawable/mimo_logo_white` |
| 18 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_100days_of_code` |
| 19 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 20 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 21 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 22 | `ImageView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 23 | `ImageView` | `app:tint` | `@color/background_reversed` |
| 24 | `TextView` | `android:textColor` | `@color/primary_default` |
| 25 | `TextView` | `android:id` | `@id/tv_100days_of_code` |
| 26 | `TextView` | `android:layout_width` | `wrap_content` |
| 27 | `TextView` | `android:layout_height` | `wrap_content` |
| 28 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxs` |
| 29 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 30 | `TextView` | `android:text` | `@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_hashtag` |
| 31 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/cpi_day_of_code` |
| 32 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 33 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 34 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_mimo_logo` |
| 35 | `TextView` | `style` | `@style/TextH4` |
| 36 | `TextView` | `android:textColor` | `@color/text_primary` |
| 37 | `TextView` | `android:id` | `@id/tv_nb_days_of_code` |
| 38 | `TextView` | `android:layout_width` | `wrap_content` |
| 39 | `TextView` | `android:layout_height` | `wrap_content` |
| 40 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_days_of_code` |
| 41 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/cpi_day_of_code` |
| 42 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/cpi_day_of_code` |
| 43 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/cpi_day_of_code` |
| 44 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 45 | `TextView` | `style` | `@style/TextDaysOfCodeShareToStories` |
| 46 | `TextView` | `android:textColor` | `@color/text_primary` |
| 47 | `TextView` | `android:id` | `@id/tv_days_of_code` |
| 48 | `TextView` | `android:layout_width` | `wrap_content` |
| 49 | `TextView` | `android:layout_height` | `wrap_content` |
| 50 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/cpi_day_of_code` |
| 51 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/cpi_day_of_code` |
| 52 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/cpi_day_of_code` |
| 53 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_nb_days_of_code` |
| 54 | `TextView` | `style` | `@style/TextH3` |
| 55 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:id` | `@id/cpi_day_of_code` |
| 56 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_width` | `wrap_content` |
| 57 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_height` | `wrap_content` |
| 58 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:progress` | `50` |
| 59 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorColor` | `@color/progress_primary` |
| 60 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorSize` | `234.000000dip` |
| 61 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintBottom_toTopOf` | `@id/tv_description` |
| 62 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintEnd_toEndOf` | `0` |
| 63 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintStart_toStartOf` | `0` |
| 64 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintTop_toBottomOf` | `@id/tv_100days_of_code` |
| 65 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:trackColor` | `@color/progress_empty` |
| 66 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:trackCornerRadius` | `24.000000dip` |
| 67 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:trackThickness` | `12.000000dip` |
| 68 | `TextView` | `android:textAppearance` | `@style/TextH2` |
| 69 | `TextView` | `android:textColor` | `@color/text_primary` |
| 70 | `TextView` | `android:gravity` | `0x00000011` |
| 71 | `TextView` | `android:id` | `@id/tv_description` |
| 72 | `TextView` | `android:layout_width` | `0.000000dip` |
| 73 | `TextView` | `android:layout_height` | `wrap_content` |
| 74 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 75 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 76 | `TextView` | `app:layout_constrainedWidth` | `true` |
| 77 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 78 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 79 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/cpi_day_of_code` |
| 80 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 81 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 82 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_profile` |
| 83 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@drawable/rounded_background_reversed_infinite` |
| 84 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `wrap_content` |
| 85 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 86 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 87 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintBottom_toTopOf` | `@id/layout_profile` |
| 88 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 89 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 90 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_description` |
| 91 | `com.google.android.material.imageview.ShapeableImageView` | `android:id` | `@id/iv_user_picture` |
| 92 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_width` | `32.000000dip` |
| 93 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_height` | `32.000000dip` |
| 94 | `com.google.android.material.imageview.ShapeableImageView` | `android:scaleType` | `centerCrop` |
| 95 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_marginStart` | `@dimen/spacing_xxs` |
| 96 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_marginVertical` | `@dimen/spacing_xxs` |
| 97 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 98 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_get_to_one_hundred` |
| 99 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 100 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 101 | `com.google.android.material.imageview.ShapeableImageView` | `app:shapeAppearanceOverlay` | `@style/CircularImageView` |
| 102 | `com.google.android.material.imageview.ShapeableImageView` | `app:srcCompat` | `@drawable/avatar_placeholder` |
| 103 | `TextView` | `android:textColor` | `@color/text_reversed` |
| 104 | `TextView` | `android:id` | `@id/tv_get_to_one_hundred` |
| 105 | `TextView` | `android:layout_width` | `wrap_content` |
| 106 | `TextView` | `android:layout_height` | `wrap_content` |
| 107 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 108 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 109 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 110 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 111 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_user_picture` |
| 112 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 113 | `TextView` | `style` | `@style/TextH4` |
| 114 | `TextView` | `android:textColor` | `@color/primary_default` |
| 115 | `TextView` | `android:id` | `@id/tv_mimo_app_link` |
| 116 | `TextView` | `android:layout_width` | `wrap_content` |
| 117 | `TextView` | `android:layout_height` | `wrap_content` |
| 118 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 119 | `TextView` | `android:layout_marginBottom` | `40.000000dip` |
| 120 | `TextView` | `android:text` | `@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_mimo_app_link` |
| 121 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 122 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 123 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 124 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/layout_profile` |
| 125 | `TextView` | `app:layout_constraintVertical_bias` | `0.200000` |
| 126 | `TextView` | `style` | `@style/TextH3` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/background_reversed` | `#FF333661` / `#FFFFFFFF` (night) |
| `@color/primary_default` | `#FF7E4BDE` / `#FF885BDE` (night) |
| `@color/progress_empty` | `#FFE4E6F1` / `#FF4A4D85` (night) |
| `@color/progress_primary` | `#FF7E4BDE` / `#FFA175EA` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_reversed` | `#FFFFFFFF` / `#FF252746` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_hashtag` | `#100DaysOfCode` / `#100DaysOfCode` (de) / `#100DaysOfCode` (es) / `#100DaysOfCode` (fr) / `#100DaysOfCode` (in) / `#100DaysOfCode` (it) / `#100DaysOfCode` (pl) / `#100DiasProgramando` (pt-rBR) / `#100DaysOfCode` (ru) / `#100DaysOfCode` (tr) |
| `@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_mimo_app_link` | `mimo.app` / `mimo.app` (de) / `mimo.app` (es) / `mimo.app` (fr) / `mimo.app` (in) / `mimo.app` (it) / `mimo.app` (pl) / `mimo.app` (pt-rBR) / `mimo.app` (ru) / `mimo.app` (tr) |
| `@style/CircularImageView` | `[{'attr': 'attr.cornerFamily', 'attr_id': '0x7F0401A1', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'attr.cornerSize', 'attr_id': '0x7F0401A8', 'value': '50.000001%', 'value_type': 'fraction'}]` |
| `@style/TextDaysOfCodeShareToStories` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '80.000000sp', 'value_type': 'dimension'}]` |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/cpi_day_of_code
@id/iv_mimo_logo
@id/iv_user_picture
@id/layout_profile
@id/layout_shareable_image
@id/tv_100days_of_code
@id/tv_days_of_code
@id/tv_description
@id/tv_get_to_one_hundred
@id/tv_mimo_app_link
@id/tv_nb_days_of_code
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
com.getmimo.ui.chapter.chapterendview.streak.ChapterFinishedShareStreakFragment$Companion$ChapterFinishedShareData
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/layout_shareable_image" android:background="@color/background_primary" android:paddingTop="@dimen/spacing_xl" android:layout_width="match_parent" android:layout_height="match_parent">
  <ImageView android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:src="@drawable/streak_share_background" android:scaleType="fitEnd" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/tv_description"/>
  <ImageView android:id="@id/iv_mimo_logo" android:layout_width="60.000000dip" android:layout_height="wrap_content" android:src="@drawable/mimo_logo_white" app:layout_constraintBottom_toTopOf="@id/tv_100days_of_code" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2" app:tint="@color/background_reversed"/>
  <TextView android:textColor="@color/primary_default" android:id="@id/tv_100days_of_code" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxs" android:layout_marginBottom="@dimen/spacing_m" android:text="@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_hashtag" app:layout_constraintBottom_toTopOf="@id/cpi_day_of_code" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_mimo_logo" style="@style/TextH4"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_nb_days_of_code" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toTopOf="@id/tv_days_of_code" app:layout_constraintEnd_toEndOf="@id/cpi_day_of_code" app:layout_constraintStart_toStartOf="@id/cpi_day_of_code" app:layout_constraintTop_toTopOf="@id/cpi_day_of_code" app:layout_constraintVertical_chainStyle="2" style="@style/TextDaysOfCodeShareToStories"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_days_of_code" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="@id/cpi_day_of_code" app:layout_constraintEnd_toEndOf="@id/cpi_day_of_code" app:layout_constraintStart_toStartOf="@id/cpi_day_of_code" app:layout_constraintTop_toBottomOf="@id/tv_nb_days_of_code" style="@style/TextH3"/>
  <com.google.android.material.progressindicator.CircularProgressIndicator android:id="@id/cpi_day_of_code" android:layout_width="wrap_content" android:layout_height="wrap_content" android:progress="50" app:indicatorColor="@color/progress_primary" app:indicatorSize="234.000000dip" app:layout_constraintBottom_toTopOf="@id/tv_description" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_100days_of_code" app:trackColor="@color/progress_empty" app:trackCornerRadius="24.000000dip" app:trackThickness="12.000000dip"/>
  <TextView android:textAppearance="@style/TextH2" android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cpi_day_of_code" app:layout_constraintVertical_chainStyle="2" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/layout_profile" android:background="@drawable/rounded_background_reversed_infinite" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" app:layout_constraintBottom_toTopOf="@id/layout_profile" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_description">
    <com.google.android.material.imageview.ShapeableImageView android:id="@id/iv_user_picture" android:layout_width="32.000000dip" android:layout_height="32.000000dip" android:scaleType="centerCrop" android:layout_marginStart="@dimen/spacing_xxs" android:layout_marginVertical="@dimen/spacing_xxs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/tv_get_to_one_hundred" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:shapeAppearanceOverlay="@style/CircularImageView" app:srcCompat="@drawable/avatar_placeholder"/>
    <TextView android:textColor="@color/text_reversed" android:id="@id/tv_get_to_one_hundred" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginStart="@dimen/spacing_s" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_user_picture" app:layout_constraintTop_toTopOf="0" style="@style/TextH4"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
  <TextView android:textColor="@color/primary_default" android:id="@id/tv_mimo_app_link" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginBottom="40.000000dip" android:text="@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_mimo_app_link" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_profile" app:layout_constraintVertical_bias="0.200000" style="@style/TextH3"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
