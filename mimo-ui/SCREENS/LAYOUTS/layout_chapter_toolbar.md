# پروندهٔ لایه — `res/layout/chapter_toolbar.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_toolbar.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_toolbar.xml`](../../SOURCE/res/layout/chapter_toolbar.xml) |
| SHA-256 دیکد | `76ff965e4787b4841a962c84c403022914643f74e60b79f1caf6113b6eb8cc82` |
| ریشه | `merge` |
| تعداد گره | 7 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ ImageView  #@id/btn_lesson_close
   ├─ TextView  #@id/tv_lesson_streak_chapter_toolbar
   ├─ TextView  #@id/tv_chapter_toolbar_label
   ├─ com.getmimo.ui.common.SpringAnimatingProgressBar  #@id/pb_chapter
   ├─ ImageView  #@id/btn_lesson_report
   └─ View  #@id/v_line
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ImageView` | `android:id` | `@id/btn_lesson_close` |
| 2 | `ImageView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 3 | `ImageView` | `android:clipChildren` | `false` |
| 4 | `ImageView` | `android:clipToPadding` | `false` |
| 5 | `ImageView` | `android:layout_width` | `wrap_content` |
| 6 | `ImageView` | `android:layout_height` | `match_parent` |
| 7 | `ImageView` | `android:paddingStart` | `@dimen/lesson_progress_marginstart` |
| 8 | `ImageView` | `android:paddingEnd` | `@dimen/general_margin_end` |
| 9 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `ImageView` | `app:srcCompat` | `@drawable/ic_close` |
| 12 | `ImageView` | `app:tint` | `@color/navbar_icon` |
| 13 | `TextView` | `android:gravity` | `0x00000011` |
| 14 | `TextView` | `android:id` | `@id/tv_lesson_streak_chapter_toolbar` |
| 15 | `TextView` | `android:layout_width` | `0.000000dip` |
| 16 | `TextView` | `android:layout_height` | `match_parent` |
| 17 | `TextView` | `android:textAllCaps` | `true` |
| 18 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `TextView` | `style` | `@style/TextLabel1` |
| 21 | `TextView` | `android:textColor` | `@color/text_weak` |
| 22 | `TextView` | `android:gravity` | `0x00000011` |
| 23 | `TextView` | `android:id` | `@id/tv_chapter_toolbar_label` |
| 24 | `TextView` | `android:layout_width` | `0.000000dip` |
| 25 | `TextView` | `android:layout_height` | `match_parent` |
| 26 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `TextView` | `style` | `@style/TextButton2` |
| 29 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `android:id` | `@id/pb_chapter` |
| 30 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `android:layout_width` | `0.000000dip` |
| 31 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `android:layout_height` | `@dimen/lesson_progressbar_height` |
| 32 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 33 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `app:layout_constraintEnd_toStartOf` | `@id/btn_lesson_report` |
| 34 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `app:layout_constraintStart_toEndOf` | `@id/btn_lesson_close` |
| 35 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `app:layout_constraintTop_toTopOf` | `0` |
| 36 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `app:layout_goneMarginEnd` | `@dimen/general_margin_end` |
| 37 | `com.getmimo.ui.common.SpringAnimatingProgressBar` | `style` | `@style/ProgressBarChapter` |
| 38 | `ImageView` | `android:id` | `@id/btn_lesson_report` |
| 39 | `ImageView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 40 | `ImageView` | `android:layout_width` | `wrap_content` |
| 41 | `ImageView` | `android:layout_height` | `match_parent` |
| 42 | `ImageView` | `android:contentDescription` | `@string/report` |
| 43 | `ImageView` | `android:paddingStart` | `@dimen/general_margin_end` |
| 44 | `ImageView` | `android:paddingEnd` | `@dimen/lesson_progress_marginstart` |
| 45 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 46 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 47 | `ImageView` | `app:srcCompat` | `@drawable/ic_flag` |
| 48 | `ImageView` | `app:tint` | `@color/navbar_icon` |
| 49 | `View` | `android:id` | `@id/v_line` |
| 50 | `View` | `android:background` | `@color/line_primary` |
| 51 | `View` | `android:layout_width` | `0.000000dip` |
| 52 | `View` | `android:layout_height` | `1.000000dip` |
| 53 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 54 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 55 | `View` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@color/navbar_icon` | `#FF626596` / `#FFB9BBD2` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/general_margin_end` | `16.000000dip` / `30.000000dip` (sw600dp) |
| `@dimen/lesson_progress_marginstart` | `@dimen/spacing_m` / `34.000000dip` (sw600dp) |
| `@dimen/lesson_progressbar_height` | `6.000000dip` / `8.000000dip` (sw600dp) |
| `@string/report` | `Report` / `Melden` (de) / `Reportar` (es) / `Signaler` (fr) / `Laporkan` (in) / `Segnala` (it) / `Zgłoś` (pl) / `Reportar` (pt-rBR) / `Пожаловаться` (ru) / `Bildir` (tr) |
| `@style/ProgressBarChapter` | `[{'attr': 'android:indeterminateDrawable', 'attr_id': '0x0101013B', 'value': '@drawable/progress_bar_chapter', 'value_type': 'reference'}, {'attr': 'android:progressDrawable', 'attr_id': '0x0101013C', 'value': '@drawable/progress_bar_chapter', 'value_type': 'reference'}]` / `[]` (sw600dp) |
| `@style/TextButton2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_lesson_close
@id/btn_lesson_report
@id/pb_chapter
@id/tv_chapter_toolbar_label
@id/tv_lesson_streak_chapter_toolbar
@id/v_line
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">
  <ImageView android:id="@id/btn_lesson_close" android:background="?attr/selectableItemBackgroundBorderless" android:clipChildren="false" android:clipToPadding="false" android:layout_width="wrap_content" android:layout_height="match_parent" android:paddingStart="@dimen/lesson_progress_marginstart" android:paddingEnd="@dimen/general_margin_end" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_close" app:tint="@color/navbar_icon"/>
  <TextView android:gravity="0x00000011" android:id="@id/tv_lesson_streak_chapter_toolbar" android:layout_width="0.000000dip" android:layout_height="match_parent" android:textAllCaps="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" style="@style/TextLabel1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_chapter_toolbar_label" android:layout_width="0.000000dip" android:layout_height="match_parent" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" style="@style/TextButton2"/>
  <com.getmimo.ui.common.SpringAnimatingProgressBar android:id="@id/pb_chapter" android:layout_width="0.000000dip" android:layout_height="@dimen/lesson_progressbar_height" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/btn_lesson_report" app:layout_constraintStart_toEndOf="@id/btn_lesson_close" app:layout_constraintTop_toTopOf="0" app:layout_goneMarginEnd="@dimen/general_margin_end" style="@style/ProgressBarChapter"/>
  <ImageView android:id="@id/btn_lesson_report" android:background="?attr/selectableItemBackgroundBorderless" android:layout_width="wrap_content" android:layout_height="match_parent" android:contentDescription="@string/report" android:paddingStart="@dimen/general_margin_end" android:paddingEnd="@dimen/lesson_progress_marginstart" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_flag" app:tint="@color/navbar_icon"/>
  <View android:id="@id/v_line" android:background="@color/line_primary" android:layout_width="0.000000dip" android:layout_height="1.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</merge>
```
