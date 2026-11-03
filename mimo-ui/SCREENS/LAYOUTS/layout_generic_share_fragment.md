# پروندهٔ لایه — `res/layout/generic_share_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/generic_share_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/generic_share_fragment.xml`](../../SOURCE/res/layout/generic_share_fragment.xml) |
| SHA-256 دیکد | `af6bbe29f1aaf13eeda2b3470fbe063f5051d721c41cda5f37ee9a3932d6ad1e` |
| ریشه | `merge` |
| تعداد گره | 12 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 26 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_share
      │  ├─ FrameLayout  #@id/layout_shareable_image
      │  └─ include  #@id/layout_placeholder_original
      └─ LinearLayout  #@id/layout_share_options
         ├─ TextView  #@id/tv_share_to
         ├─ LinearLayout
         │  ├─ ImageView  #@id/iv_share_instagram
         │  ├─ ImageView  #@id/iv_share_facebook
         │  └─ ImageView  #@id/iv_share_others
         └─ TextView  #@id/tv_tag
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `0.000000dip` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toBottomOf` | `@id/cv_bottom_sheet_header` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_share` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@drawable/rounded_background_primary` |
| 8 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `0.000000dip` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `0.000000dip` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:translationY` | `16777156.000000dip` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:scaleX` | `0.600000` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:scaleY` | `0.600000` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_xxs` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 15 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 16 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 17 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 18 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintVertical_chainStyle` | `0` |
| 19 | `FrameLayout` | `android:id` | `@id/layout_shareable_image` |
| 20 | `FrameLayout` | `android:background` | `@color/background_primary` |
| 21 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 22 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 23 | `FrameLayout` | `android:layout_marginVertical` | `@dimen/spacing_xxs` |
| 24 | `FrameLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 25 | `FrameLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 26 | `FrameLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 27 | `FrameLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 28 | `include` | `android:id` | `@id/layout_placeholder_original` |
| 29 | `include` | `android:layout_width` | `0.000000dip` |
| 30 | `include` | `android:layout_height` | `0.000000dip` |
| 31 | `include` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 32 | `include` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 33 | `include` | `app:layout_constraintEnd_toEndOf` | `0` |
| 34 | `include` | `app:layout_constraintStart_toStartOf` | `0` |
| 35 | `include` | `app:layout_constraintTop_toTopOf` | `0` |
| 36 | `include` | `layout` | `@layout/leaderboard_result_share_placeholders` |
| 37 | `LinearLayout` | `android:orientation` | `vertical` |
| 38 | `LinearLayout` | `android:id` | `@id/layout_share_options` |
| 39 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 40 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 41 | `LinearLayout` | `android:layout_marginVertical` | `@dimen/spacing_m` |
| 42 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 43 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 44 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 45 | `TextView` | `android:textColor` | `@color/text_weak` |
| 46 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 47 | `TextView` | `android:id` | `@id/tv_share_to` |
| 48 | `TextView` | `android:layout_width` | `wrap_content` |
| 49 | `TextView` | `android:layout_height` | `wrap_content` |
| 50 | `TextView` | `android:text` | `@string/streak_chapter_end_sharing_stories_share_to` |
| 51 | `TextView` | `android:textAllCaps` | `true` |
| 52 | `TextView` | `style` | `@style/TextLabel1` |
| 53 | `LinearLayout` | `android:layout_gravity` | `0x00000011` |
| 54 | `LinearLayout` | `android:orientation` | `horizontal` |
| 55 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 56 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 57 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 58 | `LinearLayout` | `app:layout_constraintBottom_toTopOf` | `@id/tv_repost_story` |
| 59 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 60 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 61 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_share_to` |
| 62 | `ImageView` | `android:id` | `@id/iv_share_instagram` |
| 63 | `ImageView` | `android:background` | `?0x0101045C` |
| 64 | `ImageView` | `android:layout_width` | `wrap_content` |
| 65 | `ImageView` | `android:layout_height` | `wrap_content` |
| 66 | `ImageView` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 67 | `ImageView` | `app:srcCompat` | `@drawable/ic_share_ig_rounded_icon` |
| 68 | `ImageView` | `android:id` | `@id/iv_share_facebook` |
| 69 | `ImageView` | `android:background` | `?0x0101045C` |
| 70 | `ImageView` | `android:layout_width` | `wrap_content` |
| 71 | `ImageView` | `android:layout_height` | `wrap_content` |
| 72 | `ImageView` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 73 | `ImageView` | `app:srcCompat` | `@drawable/ic_share_fb_rounded_icon` |
| 74 | `ImageView` | `android:id` | `@id/iv_share_others` |
| 75 | `ImageView` | `android:background` | `?0x0101045C` |
| 76 | `ImageView` | `android:layout_width` | `wrap_content` |
| 77 | `ImageView` | `android:layout_height` | `wrap_content` |
| 78 | `ImageView` | `android:layout_marginHorizontal` | `@dimen/spacing_xs` |
| 79 | `ImageView` | `app:srcCompat` | `@drawable/ic_share_others_rounded_icon` |
| 80 | `TextView` | `android:textColor` | `@color/text_weak` |
| 81 | `TextView` | `android:id` | `@id/tv_tag` |
| 82 | `TextView` | `android:layout_width` | `wrap_content` |
| 83 | `TextView` | `android:layout_height` | `wrap_content` |
| 84 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 85 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@string/streak_chapter_end_sharing_stories_share_to` | `Share with` / `Teilen mit` (de) / `Compartir con` (es) / `Partager sur` (fr) / `Bagikan dengan` (in) / `Condividi con` (it) / `Udostępnij przez` (pl) / `Compartilhar com` (pt-rBR) / `Поделиться при помощи` (ru) / `Şununla paylaş` (tr) |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_share_facebook
@id/iv_share_instagram
@id/iv_share_others
@id/layout_placeholder_original
@id/layout_share
@id/layout_share_options
@id/layout_shareable_image
@id/tv_share_to
@id/tv_tag
```

## ۵. ارجاع به لایه‌های دیگر

```text
0
0.000000dip
@dimen/spacing_xs
@layout/leaderboard_result_share_placeholders
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.base.GenericShareFragment$setupView$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge>
  <androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintTop_toBottomOf="@id/cv_bottom_sheet_header">
    <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/layout_share" android:background="@drawable/rounded_background_primary" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:translationY="16777156.000000dip" android:scaleX="0.600000" android:scaleY="0.600000" android:paddingHorizontal="@dimen/spacing_xxs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="0">
      <FrameLayout android:id="@id/layout_shareable_image" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent" android:layout_marginVertical="@dimen/spacing_xxs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
      <include android:id="@id/layout_placeholder_original" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_marginTop="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" layout="@layout/leaderboard_result_share_placeholders"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
    <LinearLayout android:orientation="vertical" android:id="@id/layout_share_options" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0">
      <TextView android:textColor="@color/text_weak" android:layout_gravity="0x00000011" android:id="@id/tv_share_to" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/streak_chapter_end_sharing_stories_share_to" android:textAllCaps="true" style="@style/TextLabel1"/>
      <LinearLayout android:layout_gravity="0x00000011" android:orientation="horizontal" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/tv_repost_story" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_share_to">
        <ImageView android:id="@id/iv_share_instagram" android:background="?0x0101045C" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_xs" app:srcCompat="@drawable/ic_share_ig_rounded_icon"/>
        <ImageView android:id="@id/iv_share_facebook" android:background="?0x0101045C" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_xs" app:srcCompat="@drawable/ic_share_fb_rounded_icon"/>
        <ImageView android:id="@id/iv_share_others" android:background="?0x0101045C" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_xs" app:srcCompat="@drawable/ic_share_others_rounded_icon"/>
      </LinearLayout>
      <TextView android:textColor="@color/text_weak" android:id="@id/tv_tag" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" style="@style/TextP2"/>
    </LinearLayout>
  </androidx.constraintlayout.widget.ConstraintLayout>
</merge>
```
