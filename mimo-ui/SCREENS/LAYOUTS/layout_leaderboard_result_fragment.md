# پروندهٔ لایه — `res/layout/leaderboard_result_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_result_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_result_fragment.xml`](../../SOURCE/res/layout/leaderboard_result_fragment.xml) |
| SHA-256 دیکد | `4fce0348675e82a00d33342204e9c33c5d9bca8d2fa86c3f3ec57a36acb3fa1d` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 10 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 21 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ FrameLayout  #@id/iv_leaderboard_result_illustration_header
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_neutral
   │  └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container_leaderboard_result_illustration_demotion
   │     ├─ ImageView  #@id/iv_leaderboard_result_illustration_demotion_league
   │     └─ ImageView  #@id/iv_leaderboard_result_illustration_demotion_indicator
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
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
| 6 | `FrameLayout` | `android:id` | `@id/iv_leaderboard_result_illustration_header` |
| 7 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 8 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 9 | `FrameLayout` | `android:layout_marginTop` | `46.000000dip` |
| 10 | `FrameLayout` | `android:minHeight` | `232.000000dip` |
| 11 | `FrameLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `FrameLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `FrameLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_result_time` |
| 14 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 15 | `ImageView` | `android:id` | `@id/iv_leaderboard_result_illustration_neutral` |
| 16 | `ImageView` | `android:visibility` | `invisible` |
| 17 | `ImageView` | `android:layout_width` | `match_parent` |
| 18 | `ImageView` | `android:layout_height` | `150.000000dip` |
| 19 | `ImageView` | `android:adjustViewBounds` | `true` |
| 20 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/container_leaderboard_result_illustration_demotion` |
| 21 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:visibility` | `invisible` |
| 22 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 23 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 24 | `ImageView` | `android:id` | `@id/iv_leaderboard_result_illustration_demotion_league` |
| 25 | `ImageView` | `android:layout_width` | `154.000000dip` |
| 26 | `ImageView` | `android:layout_height` | `150.000000dip` |
| 27 | `ImageView` | `android:layout_marginTop` | `72.000000dip` |
| 28 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 29 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 30 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 31 | `ImageView` | `android:id` | `@id/iv_leaderboard_result_illustration_demotion_indicator` |
| 32 | `ImageView` | `android:layout_width` | `72.000000dip` |
| 33 | `ImageView` | `android:layout_height` | `72.000000dip` |
| 34 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_leaderboard_result_illustration_demotion_league` |
| 35 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/iv_leaderboard_result_illustration_demotion_league` |
| 36 | `ImageView` | `app:layout_constraintStart_toEndOf` | `@id/iv_leaderboard_result_illustration_demotion_league` |
| 37 | `ImageView` | `app:srcCompat` | `@drawable/ic_leaderboard_demotion_indicator` |
| 38 | `TextView` | `android:textColor` | `@color/text_weak` |
| 39 | `TextView` | `android:id` | `@id/tv_leaderboard_result_time` |
| 40 | `TextView` | `android:layout_width` | `wrap_content` |
| 41 | `TextView` | `android:layout_height` | `wrap_content` |
| 42 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 43 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 44 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 45 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 46 | `TextView` | `style` | `@style/TextLabel1` |
| 47 | `TextView` | `android:textColor` | `@color/text_primary` |
| 48 | `TextView` | `android:id` | `@id/tv_leaderboard_result_header` |
| 49 | `TextView` | `android:layout_width` | `wrap_content` |
| 50 | `TextView` | `android:layout_height` | `wrap_content` |
| 51 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 52 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 53 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 54 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_leaderboard_result_illustration_header` |
| 55 | `TextView` | `style` | `@style/TextH1` |
| 56 | `TextView` | `android:textColor` | `@color/text_weak` |
| 57 | `TextView` | `android:gravity` | `0x00000011` |
| 58 | `TextView` | `android:id` | `@id/tv_leaderboard_result_message` |
| 59 | `TextView` | `android:layout_width` | `0.000000dip` |
| 60 | `TextView` | `android:layout_height` | `wrap_content` |
| 61 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 62 | `TextView` | `android:text` | `@string/leaderboard_result_message` |
| 63 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 64 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 65 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 66 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_result_header` |
| 67 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 68 | `TextView` | `style` | `@style/TextP1` |
| 69 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_leaderboard_result_continue` |
| 70 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 71 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 72 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 73 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 74 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constrainedWidth` | `true` |
| 75 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 76 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 77 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 78 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `400.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@string/leaderboard_result_message` | `You finished #%1d of %2d. Can you stay at the top this week?` / `Du hast #%1d von %2d fertiggestellt. Schaffst du es, diese Woche oben zu bleiben?` (de) / `Has acabado #%1d de %2d. ¿Puedes mantenerte arriba esta semana?` (es) / `Tu as terminé #%1d de %2d. Peux-tu rester en tête cette semaine?` (fr) / `Kamu finis #%1d dari %2d. Bisakah kamu bertahan di puncak minggu ini?` (in) / `Hai chiuso #%1d su %2d. Riesci a restare in cima questa settimana?` (it) / `Kończysz na miejscu #%1d z %2d. Utrzymasz się na szczycie w tym tygodniu?` (pl) / `Você terminou #%1d de %2d. Será que você consegue ficar no topo esta semana?` (pt-rBR) / `Ты закончил(а) #%1d из %2d. Сможешь ли ты остаться в топе на этой неделе?` (ru) / `#%1d olarak, %2d kişi arasında bitirdin. Bu hafta zirvede kalabilir misin?` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_leaderboard_result_continue
@id/container_leaderboard_result_illustration_demotion
@id/iv_leaderboard_result_illustration_demotion_indicator
@id/iv_leaderboard_result_illustration_demotion_league
@id/iv_leaderboard_result_illustration_header
@id/iv_leaderboard_result_illustration_neutral
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:background="@color/background_primary" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <FrameLayout android:id="@id/iv_leaderboard_result_illustration_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="46.000000dip" android:minHeight="232.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_result_time">
    <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_leaderboard_result_illustration_neutral" android:visibility="invisible" android:layout_width="match_parent" android:layout_height="150.000000dip" android:adjustViewBounds="true"/>
    <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/container_leaderboard_result_illustration_demotion" android:visibility="invisible" android:layout_width="match_parent" android:layout_height="match_parent">
      <ImageView android:id="@id/iv_leaderboard_result_illustration_demotion_league" android:layout_width="154.000000dip" android:layout_height="150.000000dip" android:layout_marginTop="72.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
      <ImageView android:id="@id/iv_leaderboard_result_illustration_demotion_indicator" android:layout_width="72.000000dip" android:layout_height="72.000000dip" app:layout_constraintBottom_toBottomOf="@id/iv_leaderboard_result_illustration_demotion_league" app:layout_constraintEnd_toEndOf="@id/iv_leaderboard_result_illustration_demotion_league" app:layout_constraintStart_toEndOf="@id/iv_leaderboard_result_illustration_demotion_league" app:srcCompat="@drawable/ic_leaderboard_demotion_indicator"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </FrameLayout>
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_leaderboard_result_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextLabel1"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_leaderboard_result_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_leaderboard_result_illustration_header" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_leaderboard_result_message" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:text="@string/leaderboard_result_message" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_result_header" app:layout_constraintWidth_max="@dimen/general_max_width" style="@style/TextP1"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_leaderboard_result_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constrainedWidth="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="400.000000dip"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
