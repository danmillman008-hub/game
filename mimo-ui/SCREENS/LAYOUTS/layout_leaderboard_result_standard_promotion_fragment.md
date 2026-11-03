# پروندهٔ لایه — `res/layout/leaderboard_result_standard_promotion_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_result_standard_promotion_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_result_standard_promotion_fragment.xml`](../../SOURCE/res/layout/leaderboard_result_standard_promotion_fragment.xml) |
| SHA-256 دیکد | `7d82b3b27b9ac83d31d859bc4aee9ca79251de4f4d131b1c1e24f14a8b5d3f54` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 9 |
| تعداد شناسه | 8 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 20 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/constraintLayout
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_promotion_league
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_promotion_indicator
   │  ├─ TextView  #@id/tv_leaderboard_result_header
   │  └─ TextView  #@id/tv_leaderboard_result_message
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_share
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_leaderboard_result_continue
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:focusable` | `true` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:clickable` | `true` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `TextView` | `android:textColor` | `@color/text_weak` |
| 7 | `TextView` | `android:id` | `@id/tv_leaderboard_result_time` |
| 8 | `TextView` | `android:layout_width` | `wrap_content` |
| 9 | `TextView` | `android:layout_height` | `wrap_content` |
| 10 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 11 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 15 | `TextView` | `style` | `@style/TextLabel1` |
| 16 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/constraintLayout` |
| 17 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `0.000000dip` |
| 18 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 19 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_xl` |
| 20 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintBottom_toTopOf` | `@id/btn_leaderboard_result_continue` |
| 21 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 22 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 23 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_result_time` |
| 24 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 25 | `ImageView` | `android:id` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 26 | `ImageView` | `android:layout_width` | `155.000000dip` |
| 27 | `ImageView` | `android:layout_height` | `150.000000dip` |
| 28 | `ImageView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 29 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_leaderboard_result_header` |
| 30 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 31 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 32 | `ImageView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 33 | `ImageView` | `android:id` | `@id/iv_leaderboard_result_illustration_promotion_indicator` |
| 34 | `ImageView` | `android:layout_width` | `72.000000dip` |
| 35 | `ImageView` | `android:layout_height` | `72.000000dip` |
| 36 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 37 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 38 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/iv_leaderboard_result_illustration_promotion_league` |
| 39 | `ImageView` | `app:srcCompat` | `@drawable/ic_leaderboard_promotion_indicator` |
| 40 | `TextView` | `android:textColor` | `@color/text_primary` |
| 41 | `TextView` | `android:id` | `@id/tv_leaderboard_result_header` |
| 42 | `TextView` | `android:layout_width` | `wrap_content` |
| 43 | `TextView` | `android:layout_height` | `wrap_content` |
| 44 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 45 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 46 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_leaderboard_result_illustration_promotion_indicator` |
| 47 | `TextView` | `style` | `@style/TextH1` |
| 48 | `TextView` | `android:textColor` | `@color/text_weak` |
| 49 | `TextView` | `android:gravity` | `0x00000011` |
| 50 | `TextView` | `android:id` | `@id/tv_leaderboard_result_message` |
| 51 | `TextView` | `android:layout_width` | `0.000000dip` |
| 52 | `TextView` | `android:layout_height` | `wrap_content` |
| 53 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 54 | `TextView` | `android:text` | `@string/leaderboard_result_message_promotion` |
| 55 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 56 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 57 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 58 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_result_header` |
| 59 | `TextView` | `style` | `@style/TextP1` |
| 60 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_share` |
| 61 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 62 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 63 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 64 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 65 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_leaderboard_result_continue` |
| 66 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 67 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 68 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/constraintLayout` |
| 69 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintVertical_bias` | `0.000000` |
| 70 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_leaderboard_result_continue` |
| 71 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 72 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 73 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 74 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 75 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constrainedWidth` | `true` |
| 76 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 77 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 78 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 79 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `400.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@string/leaderboard_result_message_promotion` | `You finished #%1d of %2d in the %3s and advanced to the %4s.` / `Du hast #%1d von %2d in der %3s fertiggestellt und bist aufgestiegen in die %4s.` (de) / `Has acabado #%1d de %2d en %3s y avanzas a la %4s.` (es) / `Tu as terminé #%1d de %2d dans les %3s et es passé·e dans la %4s.` (fr) / `Kamu finis #%1d dari %2d di %3s dan naik ke %4s.` (in) / `Hai chiuso #%1d su %2d nella %3s e ora sali nella %4s.` (it) / `Kończysz na miejscu #%1d z %2d (%3s) i awansujesz. Czeka na ciebie %4s.` (pl) / `Você terminou #%1d de %2d no %3s e avançou para %4s.` (pt-rBR) / `Ты закончил(а) #%1d из %2d в %3s и переходишь в %4s.` (ru) / `#%1d olarak, %2d kişilik %3s sıralamasını tamamladın ve %4s seviyesine yükseldin.` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_leaderboard_result_continue
@id/btn_share
@id/constraintLayout
@id/iv_leaderboard_result_illustration_promotion_indicator
@id/iv_leaderboard_result_illustration_promotion_league
@id/tv_leaderboard_result_header
@id/tv_leaderboard_result_message
@id/tv_leaderboard_result_time
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/background_primary" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_leaderboard_result_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2" style="@style/TextLabel1"/>
  <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/constraintLayout" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_xl" app:layout_constraintBottom_toTopOf="@id/btn_leaderboard_result_continue" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_result_time" app:layout_constraintWidth_max="@dimen/general_max_width">
    <ImageView android:id="@id/iv_leaderboard_result_illustration_promotion_league" android:layout_width="155.000000dip" android:layout_height="150.000000dip" android:layout_marginBottom="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/tv_leaderboard_result_header" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintVertical_chainStyle="2"/>
    <ImageView android:id="@id/iv_leaderboard_result_illustration_promotion_indicator" android:layout_width="72.000000dip" android:layout_height="72.000000dip" app:layout_constraintBottom_toBottomOf="@id/iv_leaderboard_result_illustration_promotion_league" app:layout_constraintEnd_toStartOf="@id/iv_leaderboard_result_illustration_promotion_league" app:layout_constraintStart_toStartOf="@id/iv_leaderboard_result_illustration_promotion_league" app:srcCompat="@drawable/ic_leaderboard_promotion_indicator"/>
    <TextView android:textColor="@color/text_primary" android:id="@id/tv_leaderboard_result_header" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_leaderboard_result_illustration_promotion_indicator" style="@style/TextH1"/>
    <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_leaderboard_result_message" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:text="@string/leaderboard_result_message_promotion" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_result_header" style="@style/TextP1"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_share" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/btn_leaderboard_result_continue" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/constraintLayout" app:layout_constraintVertical_bias="0.000000"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_leaderboard_result_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constrainedWidth="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="400.000000dip"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
