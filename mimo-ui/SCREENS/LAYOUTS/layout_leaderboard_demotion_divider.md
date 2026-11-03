# پروندهٔ لایه — `res/layout/leaderboard_demotion_divider.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_demotion_divider.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_demotion_divider.xml`](../../SOURCE/res/layout/leaderboard_demotion_divider.xml) |
| SHA-256 دیکد | `53ed0ff3c38f4ad04e56742c04bf9e935a2328357c01c1a9030d4d54ffa07a81` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_leaderboard_demotion_divider
   ├─ View  #@id/view_leaderboard_demotion_divider_start
   └─ View  #@id/view_leaderboard_demotion_divider_end
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `60.000000dip` |
| 5 | `TextView` | `android:textColor` | `@color/support_coral` |
| 6 | `TextView` | `android:gravity` | `0x00000011` |
| 7 | `TextView` | `android:id` | `@id/tv_leaderboard_demotion_divider` |
| 8 | `TextView` | `android:layout_width` | `wrap_content` |
| 9 | `TextView` | `android:layout_height` | `wrap_content` |
| 10 | `TextView` | `android:text` | `@string/leaderboard_demotion_zone` |
| 11 | `TextView` | `android:textAllCaps` | `true` |
| 12 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 13 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 14 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 15 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 16 | `TextView` | `style` | `@style/TextLabel1` |
| 17 | `View` | `android:id` | `@id/view_leaderboard_demotion_divider_start` |
| 18 | `View` | `android:background` | `@color/support_coral` |
| 19 | `View` | `android:layout_width` | `0.000000dip` |
| 20 | `View` | `android:layout_height` | `2.000000dip` |
| 21 | `View` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 22 | `View` | `android:layout_marginEnd` | `@dimen/spacing_xs` |
| 23 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `View` | `app:layout_constraintEnd_toStartOf` | `@id/tv_leaderboard_demotion_divider` |
| 25 | `View` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 27 | `View` | `android:id` | `@id/view_leaderboard_demotion_divider_end` |
| 28 | `View` | `android:background` | `@color/support_coral` |
| 29 | `View` | `android:layout_width` | `0.000000dip` |
| 30 | `View` | `android:layout_height` | `2.000000dip` |
| 31 | `View` | `android:layout_marginStart` | `@dimen/spacing_xs` |
| 32 | `View` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 33 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 35 | `View` | `app:layout_constraintStart_toEndOf` | `@id/tv_leaderboard_demotion_divider` |
| 36 | `View` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/support_coral` | `#FFF05A6E` / `#FFF97F8D` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/leaderboard_demotion_zone` | `Danger Zone` / `Gefahrenzone` (de) / `Zona de Peligro` (es) / `Zone à risque` (fr) / `Zona Bahaya` (in) / `Zona a rischio` (it) / `Strefa zagrożenia` (pl) / `Zona de Perigo` (pt-rBR) / `Опасная Зона` (ru) / `Tehlike Bölgesi` (tr) |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/tv_leaderboard_demotion_divider
@id/view_leaderboard_demotion_divider_end
@id/view_leaderboard_demotion_divider_start
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="60.000000dip">
  <TextView android:textColor="@color/support_coral" android:gravity="0x00000011" android:id="@id/tv_leaderboard_demotion_divider" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/leaderboard_demotion_zone" android:textAllCaps="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextLabel1"/>
  <View android:id="@id/view_leaderboard_demotion_divider_start" android:background="@color/support_coral" android:layout_width="0.000000dip" android:layout_height="2.000000dip" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/tv_leaderboard_demotion_divider" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <View android:id="@id/view_leaderboard_demotion_divider_end" android:background="@color/support_coral" android:layout_width="0.000000dip" android:layout_height="2.000000dip" android:layout_marginStart="@dimen/spacing_xs" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/tv_leaderboard_demotion_divider" app:layout_constraintTop_toTopOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
