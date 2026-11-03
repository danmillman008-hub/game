# پروندهٔ لایه — `res/layout/daily_sparks_goal_progress_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/daily_sparks_goal_progress_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/daily_sparks_goal_progress_view.xml`](../../SOURCE/res/layout/daily_sparks_goal_progress_view.xml) |
| SHA-256 دیکد | `de1ade3a9825ff9e13503c2cdcb546b8fd36309928fbca22641194c45333b87a` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 17 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.getmimo.ui.streaks.ArcProgressView  #@id/pb_daily_goal_progress_view
   ├─ ImageView  #@id/iv_daily_goal_progress_view_streak
   ├─ TextView  #@id/tv_daily_goal_progress_view_current_sparks
   ├─ TextView  #@id/tv_daily_goal_progress_view_daily_sparks
   └─ TextView  #@id/tv_daily_goal_progress_view_today
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 3 | `com.getmimo.ui.streaks.ArcProgressView` | `android:id` | `@id/pb_daily_goal_progress_view` |
| 4 | `com.getmimo.ui.streaks.ArcProgressView` | `android:background` | `@drawable/streak_progress_bar_background` |
| 5 | `com.getmimo.ui.streaks.ArcProgressView` | `android:layout_width` | `match_parent` |
| 6 | `com.getmimo.ui.streaks.ArcProgressView` | `android:layout_height` | `match_parent` |
| 7 | `com.getmimo.ui.streaks.ArcProgressView` | `app:arc_finished_color` | `@color/progress_secondary` |
| 8 | `com.getmimo.ui.streaks.ArcProgressView` | `app:arc_padding` | `12.000000dip` |
| 9 | `com.getmimo.ui.streaks.ArcProgressView` | `app:arc_stroke_width` | `6.000000dip` |
| 10 | `com.getmimo.ui.streaks.ArcProgressView` | `app:arc_unfinished_color` | `@color/progress_empty` |
| 11 | `ImageView` | `android:id` | `@id/iv_daily_goal_progress_view_streak` |
| 12 | `ImageView` | `android:layout_width` | `@dimen/daily_goal_progress_view_sparks_image_size_small` |
| 13 | `ImageView` | `android:layout_height` | `@dimen/daily_goal_progress_view_sparks_image_size_small` |
| 14 | `ImageView` | `android:layout_marginTop` | `36.000000dip` |
| 15 | `ImageView` | `android:src` | `@drawable/ic_bolt_charged` |
| 16 | `ImageView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 17 | `ImageView` | `app:layout_constraintRight_toRightOf` | `0` |
| 18 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/pb_daily_goal_progress_view` |
| 19 | `TextView` | `android:textSize` | `32.000000sp` |
| 20 | `TextView` | `android:textColor` | `@color/text_primary` |
| 21 | `TextView` | `android:id` | `@id/tv_daily_goal_progress_view_current_sparks` |
| 22 | `TextView` | `android:layout_width` | `wrap_content` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:layout_marginTop` | `0.000000dip` |
| 25 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `@id/pb_daily_goal_progress_view` |
| 26 | `TextView` | `app:layout_constraintRight_toRightOf` | `@id/pb_daily_goal_progress_view` |
| 27 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_daily_goal_progress_view_streak` |
| 28 | `TextView` | `style` | `@style/TextH1` |
| 29 | `TextView` | `android:textColor` | `@color/text_weak` |
| 30 | `TextView` | `android:id` | `@id/tv_daily_goal_progress_view_daily_sparks` |
| 31 | `TextView` | `android:layout_width` | `wrap_content` |
| 32 | `TextView` | `android:layout_height` | `wrap_content` |
| 33 | `TextView` | `android:layout_marginTop` | `4.000000dip` |
| 34 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `@id/pb_daily_goal_progress_view` |
| 35 | `TextView` | `app:layout_constraintRight_toRightOf` | `@id/pb_daily_goal_progress_view` |
| 36 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_daily_goal_progress_view_current_sparks` |
| 37 | `TextView` | `style` | `@style/TextSelection1` |
| 38 | `TextView` | `android:textColor` | `@color/support_yellow` |
| 39 | `TextView` | `android:id` | `@id/tv_daily_goal_progress_view_today` |
| 40 | `TextView` | `android:layout_width` | `wrap_content` |
| 41 | `TextView` | `android:layout_height` | `wrap_content` |
| 42 | `TextView` | `android:layout_marginBottom` | `20.000000dip` |
| 43 | `TextView` | `android:text` | `@string/today` |
| 44 | `TextView` | `android:textAllCaps` | `true` |
| 45 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/pb_daily_goal_progress_view` |
| 46 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `@id/pb_daily_goal_progress_view` |
| 47 | `TextView` | `app:layout_constraintRight_toRightOf` | `@id/pb_daily_goal_progress_view` |
| 48 | `TextView` | `style` | `@style/TextTitle1` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/progress_empty` | `#FFE4E6F1` / `#FF4A4D85` (night) |
| `@color/progress_secondary` | `#FFF4D055` / `#FFFBDF83` (night) |
| `@color/support_yellow` | `#FFF4D055` / `#FFFBDF83` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/daily_goal_progress_view_sparks_image_size_small` | `24.000000dip` |
| `@string/today` | `Today` / `Heute` (de) / `Hoy` (es) / `Aujourd'hui` (fr) / `Hari ini` (in) / `Oggi` (it) / `Dziś` (pl) / `Hoje` (pt-rBR) / `Сегодня` (ru) / `Bugün` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextSelection1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_daily_goal_progress_view_streak
@id/pb_daily_goal_progress_view
@id/tv_daily_goal_progress_view_current_sparks
@id/tv_daily_goal_progress_view_daily_sparks
@id/tv_daily_goal_progress_view_today
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.getmimo.ui.streaks.ArcProgressView android:id="@id/pb_daily_goal_progress_view" android:background="@drawable/streak_progress_bar_background" android:layout_width="match_parent" android:layout_height="match_parent" app:arc_finished_color="@color/progress_secondary" app:arc_padding="12.000000dip" app:arc_stroke_width="6.000000dip" app:arc_unfinished_color="@color/progress_empty"/>
  <ImageView android:id="@id/iv_daily_goal_progress_view_streak" android:layout_width="@dimen/daily_goal_progress_view_sparks_image_size_small" android:layout_height="@dimen/daily_goal_progress_view_sparks_image_size_small" android:layout_marginTop="36.000000dip" android:src="@drawable/ic_bolt_charged" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="@id/pb_daily_goal_progress_view"/>
  <TextView android:textSize="32.000000sp" android:textColor="@color/text_primary" android:id="@id/tv_daily_goal_progress_view_current_sparks" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="0.000000dip" app:layout_constraintLeft_toLeftOf="@id/pb_daily_goal_progress_view" app:layout_constraintRight_toRightOf="@id/pb_daily_goal_progress_view" app:layout_constraintTop_toBottomOf="@id/iv_daily_goal_progress_view_streak" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_daily_goal_progress_view_daily_sparks" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="4.000000dip" app:layout_constraintLeft_toLeftOf="@id/pb_daily_goal_progress_view" app:layout_constraintRight_toRightOf="@id/pb_daily_goal_progress_view" app:layout_constraintTop_toBottomOf="@id/tv_daily_goal_progress_view_current_sparks" style="@style/TextSelection1"/>
  <TextView android:textColor="@color/support_yellow" android:id="@id/tv_daily_goal_progress_view_today" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="20.000000dip" android:text="@string/today" android:textAllCaps="true" app:layout_constraintBottom_toBottomOf="@id/pb_daily_goal_progress_view" app:layout_constraintLeft_toLeftOf="@id/pb_daily_goal_progress_view" app:layout_constraintRight_toRightOf="@id/pb_daily_goal_progress_view" style="@style/TextTitle1"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
