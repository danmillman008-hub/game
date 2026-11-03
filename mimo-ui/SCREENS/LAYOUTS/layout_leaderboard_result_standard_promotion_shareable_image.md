# پروندهٔ لایه — `res/layout/leaderboard_result_standard_promotion_shareable_image.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_result_standard_promotion_shareable_image.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_result_standard_promotion_shareable_image.xml`](../../SOURCE/res/layout/leaderboard_result_standard_promotion_shareable_image.xml) |
| SHA-256 دیکد | `3c1d7e56f0fb212a29cffd7fb4ec807bf11b0a4d94146687c45596b36f9ea8d5` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 8 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 24 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_shareable_image
   ├─ ImageView  #@id/iv_mimo_logo
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ ImageView  #@id/iv_leaderboard_result_illustration_promotion_league
   ├─ ImageView  #@id/iv_leaderboard_result_illustration_promotion_indicator
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   └─ TextView  #@id/tv_mimo_app_link
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_shareable_image` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingVertical` | `@dimen/spacing_xxl` |
| 6 | `ImageView` | `android:id` | `@id/iv_mimo_logo` |
| 7 | `ImageView` | `android:layout_width` | `60.000000dip` |
| 8 | `ImageView` | `android:layout_height` | `wrap_content` |
| 9 | `ImageView` | `android:src` | `@drawable/mimo_logo_dark` |
| 10 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `TextView` | `android:textColor` | `@color/text_weak` |
| 14 | `TextView` | `android:id` | `@id/tv_leaderboard_result_time` |
| 15 | `TextView` | `android:layout_width` | `wrap_content` |
| 16 | `TextView` | `android:layout_height` | `wrap_content` |
| 17 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 18 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_mimo_logo` |
| 21 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 22 | `TextView` | `style` | `@style/TextLabel1` |
| 23 | `ImageView` | `android:id` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 24 | `ImageView` | `android:layout_width` | `105.000000dip` |
| 25 | `ImageView` | `android:layout_height` | `102.000000dip` |
| 26 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 27 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_leaderboard_result_header` |
| 28 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 29 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 30 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_result_time` |
| 31 | `ImageView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 32 | `ImageView` | `android:id` | `@id/iv_leaderboard_result_illustration_promotion_indicator` |
| 33 | `ImageView` | `android:layout_width` | `48.000000dip` |
| 34 | `ImageView` | `android:layout_height` | `48.000000dip` |
| 35 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 36 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 37 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 38 | `ImageView` | `app:srcCompat` | `@drawable/ic_leaderboard_promotion_indicator` |
| 39 | `TextView` | `android:textAppearance` | `@style/TextH1` |
| 40 | `TextView` | `android:textColor` | `@color/text_primary` |
| 41 | `TextView` | `android:id` | `@id/tv_leaderboard_result_header` |
| 42 | `TextView` | `android:layout_width` | `wrap_content` |
| 43 | `TextView` | `android:layout_height` | `wrap_content` |
| 44 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxl` |
| 45 | `TextView` | `android:text` | `@string/leaderboard_result_title_podium_promotion_share` |
| 46 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_leaderboard_result_message` |
| 47 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 48 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 49 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 50 | `TextView` | `android:textColor` | `@color/text_weak` |
| 51 | `TextView` | `android:gravity` | `0x00000011` |
| 52 | `TextView` | `android:id` | `@id/tv_leaderboard_result_message` |
| 53 | `TextView` | `android:layout_width` | `0.000000dip` |
| 54 | `TextView` | `android:layout_height` | `wrap_content` |
| 55 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 56 | `TextView` | `android:text` | `@string/leaderboard_result_message_promotion_share` |
| 57 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_l` |
| 58 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_l` |
| 59 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_mimo_app_link` |
| 60 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 61 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 62 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_result_header` |
| 63 | `TextView` | `style` | `@style/TextP1` |
| 64 | `TextView` | `android:textColor` | `@color/primary_default` |
| 65 | `TextView` | `android:id` | `@id/tv_mimo_app_link` |
| 66 | `TextView` | `android:layout_width` | `wrap_content` |
| 67 | `TextView` | `android:layout_height` | `wrap_content` |
| 68 | `TextView` | `android:text` | `@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_mimo_app_link` |
| 69 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 70 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 71 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 72 | `TextView` | `style` | `@style/TextH3` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/primary_default` | `#FF7E4BDE` / `#FF885BDE` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/leaderboard_result_message_promotion_share` | `I finished #%1d of %2d in the %3s and advanced to the %4s.` / `Ich habe #%1d von %2d in der %3s fertiggestellt und bin aufgestiegen in die %4s.` (de) / `Terminé #%1d de %2d en %3s y avancé a %4s.` (es) / `J'ai terminé #%1d de %2d dans la %3s et j'ai progressé dans la %4s.` (fr) / `Aku finis #%1d dari %2d di %3s dan naik ke %4s.` (in) / `Ho chiuso #%1d su %2d nella %3s e ora sono nella %4s.` (it) / `Kończę na miejscu #%1d z %2d (%3s) i awansuję. Czeka na mnie %4s.` (pl) / `Terminei #%1d de %2d no %3s e avancei para o %4s.` (pt-rBR) / `Я закончил эту неделю #%1d из %2d в %3s и продвинулся в %4s.` (ru) / `#%1d olarak, %2d kişilik %3s sıralamasını tamamladım ve %4s seviyesine yükseldim.` (tr) |
| `@string/leaderboard_result_title_podium_promotion_share` | `Made it to the top!` / `Du hast es an die Spitze geschafft!` (de) / `¡Conseguiste llegar al top!` (es) / `Tu as atteint le sommet!` (fr) / `Berhasil sampai puncak!` (in) / `In cima alla classifica!` (it) / `Szczyt zdobyty!` (pl) / `Cheguei ao topo!` (pt-rBR) / `Я в топе!` (ru) / `Zirveye çıktım!` (tr) |
| `@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_mimo_app_link` | `mimo.app` / `mimo.app` (de) / `mimo.app` (es) / `mimo.app` (fr) / `mimo.app` (in) / `mimo.app` (it) / `mimo.app` (pl) / `mimo.app` (pt-rBR) / `mimo.app` (ru) / `mimo.app` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_leaderboard_result_illustration_promotion_indicator
@id/iv_leaderboard_result_illustration_promotion_league
@id/iv_mimo_logo
@id/layout_shareable_image
@id/tv_leaderboard_result_header
@id/tv_leaderboard_result_message
@id/tv_leaderboard_result_time
@id/tv_mimo_app_link
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/layout_shareable_image" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent" android:paddingVertical="@dimen/spacing_xxl">
  <ImageView android:id="@id/iv_mimo_logo" android:layout_width="60.000000dip" android:layout_height="wrap_content" android:src="@drawable/mimo_logo_dark" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_leaderboard_result_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_mimo_logo" app:layout_constraintVertical_chainStyle="2" style="@style/TextLabel1"/>
  <ImageView android:id="@id/iv_leaderboard_result_illustration_promotion_league" android:layout_width="105.000000dip" android:layout_height="102.000000dip" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/tv_leaderboard_result_header" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_result_time" app:layout_constraintVertical_chainStyle="2"/>
  <ImageView android:id="@id/iv_leaderboard_result_illustration_promotion_indicator" android:layout_width="48.000000dip" android:layout_height="48.000000dip" app:layout_constraintBottom_toBottomOf="@id/iv_leaderboard_result_illustration_promotion_league" app:layout_constraintEnd_toStartOf="@id/iv_leaderboard_result_illustration_promotion_league" app:layout_constraintStart_toStartOf="@id/iv_leaderboard_result_illustration_promotion_league" app:srcCompat="@drawable/ic_leaderboard_promotion_indicator"/>
  <TextView android:textAppearance="@style/TextH1" android:textColor="@color/text_primary" android:id="@id/tv_leaderboard_result_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxl" android:text="@string/leaderboard_result_title_podium_promotion_share" app:layout_constraintBottom_toTopOf="@id/tv_leaderboard_result_message" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_leaderboard_result_illustration_promotion_league"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_leaderboard_result_message" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:text="@string/leaderboard_result_message_promotion_share" android:layout_marginStart="@dimen/spacing_l" android:layout_marginEnd="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/tv_mimo_app_link" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_result_header" style="@style/TextP1"/>
  <TextView android:textColor="@color/primary_default" android:id="@id/tv_mimo_app_link" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/streak_chapter_end_sharing_stories_share_layout_days_of_code_mimo_app_link" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" style="@style/TextH3"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
