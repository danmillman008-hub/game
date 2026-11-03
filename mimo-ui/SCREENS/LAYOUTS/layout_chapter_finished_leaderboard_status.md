# پروندهٔ لایه — `res/layout/chapter_finished_leaderboard_status.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_finished_leaderboard_status.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_finished_leaderboard_status.xml`](../../SOURCE/res/layout/chapter_finished_leaderboard_status.xml) |
| SHA-256 دیکد | `ae8985f3cbebb3734ce4e2a60ef0f4e2149389924c9474ef582f37330e36a962` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 14 |
| تعداد شناسه | 13 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 24 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ Space  #@id/s_chapter_finished_top_space
   ├─ ImageView  #@id/iv_chapter_finished_leaderboard_status_image
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_status_title
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_status_description
   └─ LinearLayout  #@id/chapter_finished_leaderboard_status_user_container
      ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_1st_place
      │  └─ include  #@id/empty_user_item_1st_place
      ├─ View  #@id/v_chapter_finished_leaderboard_status_1st_place_divider
      ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_2nd_place
      │  └─ include  #@id/current_user_item
      ├─ View  #@id/v_chapter_finished_leaderboard_status_3rd_place_divider
      └─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_3rd_place
         └─ include  #@id/empty_user_item_3rd_place
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:padding` | `12.000000dip` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `Space` | `android:id` | `@id/s_chapter_finished_top_space` |
| 7 | `Space` | `android:layout_width` | `match_parent` |
| 8 | `Space` | `android:layout_height` | `0.000000dip` |
| 9 | `Space` | `app:layout_constraintBottom_toTopOf` | `@id/iv_chapter_finished_leaderboard_status_image` |
| 10 | `Space` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `Space` | `app:layout_constraintVertical_weight` | `1.000000` |
| 12 | `ImageView` | `android:id` | `@id/iv_chapter_finished_leaderboard_status_image` |
| 13 | `ImageView` | `android:layout_width` | `125.000000dip` |
| 14 | `ImageView` | `android:layout_height` | `125.000000dip` |
| 15 | `ImageView` | `android:layout_marginTop` | `8.000000dip` |
| 16 | `ImageView` | `android:layout_marginBottom` | `12.000000dip` |
| 17 | `ImageView` | `android:layout_marginStart` | `24.000000dip` |
| 18 | `ImageView` | `android:layout_marginEnd` | `24.000000dip` |
| 19 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_chapter_finished_leaderboard_status_title` |
| 20 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 21 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 22 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/s_chapter_finished_top_space` |
| 23 | `TextView` | `android:textAppearance` | `@style/TextH1` |
| 24 | `TextView` | `android:textColor` | `@color/text_primary` |
| 25 | `TextView` | `android:gravity` | `0x00000001` |
| 26 | `TextView` | `android:id` | `@id/tv_chapter_finished_leaderboard_status_title` |
| 27 | `TextView` | `android:layout_width` | `match_parent` |
| 28 | `TextView` | `android:layout_height` | `wrap_content` |
| 29 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 30 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 31 | `TextView` | `android:text` | `@string/chapter_end_screen_leaderboard_status_title` |
| 32 | `TextView` | `android:layout_marginStart` | `24.000000dip` |
| 33 | `TextView` | `android:layout_marginEnd` | `24.000000dip` |
| 34 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_chapter_finished_leaderboard_status_description` |
| 35 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_chapter_finished_leaderboard_status_image` |
| 36 | `TextView` | `android:textAppearance` | `@style/TextP1` |
| 37 | `TextView` | `android:textColor` | `@color/text_weak` |
| 38 | `TextView` | `android:gravity` | `0x00000031` |
| 39 | `TextView` | `android:id` | `@id/tv_chapter_finished_leaderboard_status_description` |
| 40 | `TextView` | `android:layout_width` | `match_parent` |
| 41 | `TextView` | `android:layout_height` | `0.000000dip` |
| 42 | `TextView` | `android:layout_marginTop` | `8.000000dip` |
| 43 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 44 | `TextView` | `android:minLines` | `1` |
| 45 | `TextView` | `android:layout_marginStart` | `24.000000dip` |
| 46 | `TextView` | `android:layout_marginEnd` | `24.000000dip` |
| 47 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/chapter_finished_leaderboard_status_user_container` |
| 48 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_chapter_finished_leaderboard_status_title` |
| 49 | `TextView` | `app:layout_constraintVertical_weight` | `1.000000` |
| 50 | `LinearLayout` | `android:orientation` | `vertical` |
| 51 | `LinearLayout` | `android:id` | `@id/chapter_finished_leaderboard_status_user_container` |
| 52 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 53 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 54 | `LinearLayout` | `android:elevation` | `4.000000dip` |
| 55 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 56 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_chapter_finished_leaderboard_status_description` |
| 57 | `FrameLayout` | `android:id` | `@id/fl_chapter_finished_leaderboard_status_1st_place` |
| 58 | `FrameLayout` | `android:background` | `@drawable/rounded_background_top` |
| 59 | `FrameLayout` | `android:paddingTop` | `8.000000dip` |
| 60 | `FrameLayout` | `android:paddingBottom` | `8.000000dip` |
| 61 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 62 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 63 | `include` | `android:id` | `@id/empty_user_item_1st_place` |
| 64 | `include` | `android:layout_width` | `match_parent` |
| 65 | `include` | `android:layout_height` | `wrap_content` |
| 66 | `include` | `layout` | `@layout/friend_empty_item` |
| 67 | `View` | `android:id` | `@id/v_chapter_finished_leaderboard_status_1st_place_divider` |
| 68 | `View` | `android:background` | `@color/line_primary` |
| 69 | `View` | `android:layout_width` | `match_parent` |
| 70 | `View` | `android:layout_height` | `1.000000px` |
| 71 | `FrameLayout` | `android:id` | `@id/fl_chapter_finished_leaderboard_status_2nd_place` |
| 72 | `FrameLayout` | `android:background` | `@color/background_secondary` |
| 73 | `FrameLayout` | `android:paddingTop` | `8.000000dip` |
| 74 | `FrameLayout` | `android:paddingBottom` | `8.000000dip` |
| 75 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 76 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 77 | `include` | `android:id` | `@id/current_user_item` |
| 78 | `include` | `android:layout_width` | `match_parent` |
| 79 | `include` | `android:layout_height` | `wrap_content` |
| 80 | `include` | `layout` | `@layout/leaderboard_item` |
| 81 | `View` | `android:id` | `@id/v_chapter_finished_leaderboard_status_3rd_place_divider` |
| 82 | `View` | `android:background` | `@color/line_primary` |
| 83 | `View` | `android:layout_width` | `match_parent` |
| 84 | `View` | `android:layout_height` | `1.000000px` |
| 85 | `FrameLayout` | `android:id` | `@id/fl_chapter_finished_leaderboard_status_3rd_place` |
| 86 | `FrameLayout` | `android:background` | `@drawable/rounded_background_bottom` |
| 87 | `FrameLayout` | `android:paddingTop` | `8.000000dip` |
| 88 | `FrameLayout` | `android:paddingBottom` | `8.000000dip` |
| 89 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 90 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 91 | `include` | `android:id` | `@id/empty_user_item_3rd_place` |
| 92 | `include` | `android:layout_width` | `match_parent` |
| 93 | `include` | `android:layout_height` | `wrap_content` |
| 94 | `include` | `layout` | `@layout/friend_empty_item` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@string/chapter_end_screen_leaderboard_status_title` | `You are strengthening your position!` / `Du stärkst deine Position!` (de) / `¡Estás fortaleciendo tu posición!` (es) / `Tu renforces ta position !` (fr) / `Kamu memperkuat posisimu!` (in) / `Stai rafforzando la tua posizione!` (it) / `Umacniasz swoją pozycję!` (pl) / `Você está fortalecendo sua posição!` (pt-rBR) / `Ты укрепляешь свою позицию!` (ru) / `Konumunu güçlendiriyorsun!` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/chapter_finished_leaderboard_status_user_container
@id/current_user_item
@id/empty_user_item_1st_place
@id/empty_user_item_3rd_place
@id/fl_chapter_finished_leaderboard_status_1st_place
@id/fl_chapter_finished_leaderboard_status_2nd_place
@id/fl_chapter_finished_leaderboard_status_3rd_place
@id/iv_chapter_finished_leaderboard_status_image
@id/s_chapter_finished_top_space
@id/tv_chapter_finished_leaderboard_status_description
@id/tv_chapter_finished_leaderboard_status_title
@id/v_chapter_finished_leaderboard_status_1st_place_divider
@id/v_chapter_finished_leaderboard_status_3rd_place_divider
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/friend_empty_item
@layout/leaderboard_item
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
com.getmimo.ui.chapter.chapterendview.leaderboard.ChapterFinishedLeaderboardFragment$setupAuthenticationObservers$2
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$onChapterFinishedContinue$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$1$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$2
com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:orientation="vertical" android:padding="12.000000dip" android:layout_width="match_parent" android:layout_height="match_parent">
  <Space android:id="@id/s_chapter_finished_top_space" android:layout_width="match_parent" android:layout_height="0.000000dip" app:layout_constraintBottom_toTopOf="@id/iv_chapter_finished_leaderboard_status_image" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_weight="1.000000"/>
  <ImageView android:id="@id/iv_chapter_finished_leaderboard_status_image" android:layout_width="125.000000dip" android:layout_height="125.000000dip" android:layout_marginTop="8.000000dip" android:layout_marginBottom="12.000000dip" android:layout_marginStart="24.000000dip" android:layout_marginEnd="24.000000dip" app:layout_constraintBottom_toTopOf="@id/tv_chapter_finished_leaderboard_status_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/s_chapter_finished_top_space"/>
  <TextView android:textAppearance="@style/TextH1" android:textColor="@color/text_primary" android:gravity="0x00000001" android:id="@id/tv_chapter_finished_leaderboard_status_title" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:text="@string/chapter_end_screen_leaderboard_status_title" android:layout_marginStart="24.000000dip" android:layout_marginEnd="24.000000dip" app:layout_constraintBottom_toTopOf="@id/tv_chapter_finished_leaderboard_status_description" app:layout_constraintTop_toBottomOf="@id/iv_chapter_finished_leaderboard_status_image"/>
  <TextView android:textAppearance="@style/TextP1" android:textColor="@color/text_weak" android:gravity="0x00000031" android:id="@id/tv_chapter_finished_leaderboard_status_description" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_marginTop="8.000000dip" android:layout_marginBottom="8.000000dip" android:minLines="1" android:layout_marginStart="24.000000dip" android:layout_marginEnd="24.000000dip" app:layout_constraintBottom_toTopOf="@id/chapter_finished_leaderboard_status_user_container" app:layout_constraintTop_toBottomOf="@id/tv_chapter_finished_leaderboard_status_title" app:layout_constraintVertical_weight="1.000000"/>
  <LinearLayout android:orientation="vertical" android:id="@id/chapter_finished_leaderboard_status_user_container" android:layout_width="match_parent" android:layout_height="wrap_content" android:elevation="4.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintTop_toBottomOf="@id/tv_chapter_finished_leaderboard_status_description">
    <FrameLayout android:id="@id/fl_chapter_finished_leaderboard_status_1st_place" android:background="@drawable/rounded_background_top" android:paddingTop="8.000000dip" android:paddingBottom="8.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content">
      <include android:id="@id/empty_user_item_1st_place" android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/friend_empty_item"/>
    </FrameLayout>
    <View android:id="@id/v_chapter_finished_leaderboard_status_1st_place_divider" android:background="@color/line_primary" android:layout_width="match_parent" android:layout_height="1.000000px"/>
    <FrameLayout android:id="@id/fl_chapter_finished_leaderboard_status_2nd_place" android:background="@color/background_secondary" android:paddingTop="8.000000dip" android:paddingBottom="8.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content">
      <include android:id="@id/current_user_item" android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/leaderboard_item"/>
    </FrameLayout>
    <View android:id="@id/v_chapter_finished_leaderboard_status_3rd_place_divider" android:background="@color/line_primary" android:layout_width="match_parent" android:layout_height="1.000000px"/>
    <FrameLayout android:id="@id/fl_chapter_finished_leaderboard_status_3rd_place" android:background="@drawable/rounded_background_bottom" android:paddingTop="8.000000dip" android:paddingBottom="8.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content">
      <include android:id="@id/empty_user_item_3rd_place" android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/friend_empty_item"/>
    </FrameLayout>
  </LinearLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
