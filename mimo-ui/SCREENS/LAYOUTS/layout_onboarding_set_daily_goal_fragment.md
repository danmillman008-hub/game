# پروندهٔ لایه — `res/layout/onboarding_set_daily_goal_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_set_daily_goal_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_set_daily_goal_fragment.xml`](../../SOURCE/res/layout/onboarding_set_daily_goal_fragment.xml) |
| SHA-256 دیکد | `c631a92337208cf5992bfa00ff3473f6f4b41e36a41cf4389c3f22e9f58f3cbf` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 16 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_daily_goal_title
   ├─ TextView  #@id/tv_goal_subtitle
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCard  #@id/layout_daily_goal_card
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_l` |
| 6 | `TextView` | `android:textColor` | `@color/text_primary` |
| 7 | `TextView` | `android:gravity` | `0x00000011` |
| 8 | `TextView` | `android:id` | `@id/tv_set_daily_goal_title` |
| 9 | `TextView` | `android:layout_width` | `0.000000dip` |
| 10 | `TextView` | `android:layout_height` | `wrap_content` |
| 11 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 12 | `TextView` | `android:text` | `@string/onboarding_set_daily_goal_title` |
| 13 | `TextView` | `android:minLines` | `2` |
| 14 | `TextView` | `android:paddingHorizontal` | `@dimen/onboarding_set_goal_margin_horizontal` |
| 15 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 16 | `TextView` | `app:layout_constraintRight_toRightOf` | `0` |
| 17 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 18 | `TextView` | `app:layout_constraintWidth_max` | `420.000000dip` |
| 19 | `TextView` | `style` | `@style/TextH1` |
| 20 | `TextView` | `android:textColor` | `@color/text_weak` |
| 21 | `TextView` | `android:gravity` | `0x00000011` |
| 22 | `TextView` | `android:id` | `@id/tv_goal_subtitle` |
| 23 | `TextView` | `android:layout_width` | `match_parent` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:layout_margin` | `@dimen/spacing_s` |
| 26 | `TextView` | `android:text` | `@string/daily_goal_subtitle` |
| 27 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_daily_goal_title` |
| 28 | `TextView` | `style` | `@style/TextP1` |
| 29 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:gravity` | `0x00000010` |
| 30 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:id` | `@id/layout_daily_goal_card` |
| 31 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:background` | `@drawable/rounded_background` |
| 32 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:layout_width` | `0.000000dip` |
| 33 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:layout_height` | `wrap_content` |
| 34 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:elevation` | `1.000000dip` |
| 35 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:layout_marginVertical` | `@dimen/spacing_l` |
| 36 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constrainedWidth` | `true` |
| 37 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintBottom_toTopOf` | `@id/compose_content` |
| 38 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintEnd_toEndOf` | `0` |
| 39 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintStart_toStartOf` | `0` |
| 40 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintTop_toBottomOf` | `@id/tv_goal_subtitle` |
| 41 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_content` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/onboarding_set_goal_margin_horizontal` | `22.000000dip` / `22.000000dip` (sw320dp-xhdpi) / `40.000000dip` (sw600dp) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@string/daily_goal_subtitle` | `You can always change this goal later` / `Du kannst dieses Ziel später jederzeit ändern` (de) / `Siempre puedes cambiar este objetivo después` (es) / `Tu peux toujours changer cet objectif plus tard` (fr) / `Kamu selalu bisa mengubah target ini nanti` (in) / `Puoi cambiare questo obiettivo quando vuoi` (it) / `Ten cel zmienisz w każdej chwili` (pl) / `Você sempre pode alterar essa meta mais tarde` (pt-rBR) / `Ты всегда можешь изменить свою цель позже` (ru) / `Bu hedefi istediğin zaman değiştirebilirsin` (tr) |
| `@string/onboarding_set_daily_goal_title` | `How long do you want to learn each day?` / `Wie lange möchtest du jeden Tag lernen?` (de) / `¿Cuánto tiempo quieres aprender cada día?` (es) / `Combien de temps veux-tu apprendre chaque jour?` (fr) / `Berapa lama kamu mau belajar tiap hari?` (in) / `Quanto tempo vuoi dedicare allo studio ogni giorno?` (it) / `Ile chcesz uczyć się każdego dnia?` (pl) / `Quanto tempo você quer aprender por dia?` (pt-rBR) / `Сколько времени ты хочешь учиться каждый день?` (ru) / `Her gün ne kadar öğrenmek istersin?` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/compose_content
@id/layout_daily_goal_card
@id/tv_goal_subtitle
@id/tv_set_daily_goal_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.OnboardingActivity
com.getmimo.ui.onboarding.dailygoal.OnboardingSetDailyGoalFragment
com.getmimo.ui.profile.SetDailyGoalActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="match_parent" android:maxWidth="@dimen/general_max_width" android:paddingHorizontal="@dimen/spacing_l">
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_set_daily_goal_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/onboarding_set_daily_goal_title" android:minLines="2" android:paddingHorizontal="@dimen/onboarding_set_goal_margin_horizontal" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintWidth_max="420.000000dip" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_goal_subtitle" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_margin="@dimen/spacing_s" android:text="@string/daily_goal_subtitle" app:layout_constraintTop_toBottomOf="@id/tv_set_daily_goal_title" style="@style/TextP1"/>
  <com.getmimo.ui.profile.view.SetDailyGoalCard android:gravity="0x00000010" android:id="@id/layout_daily_goal_card" android:background="@drawable/rounded_background" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:elevation="1.000000dip" android:layout_marginVertical="@dimen/spacing_l" app:layout_constrainedWidth="true" app:layout_constraintBottom_toTopOf="@id/compose_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_goal_subtitle" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_content" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
