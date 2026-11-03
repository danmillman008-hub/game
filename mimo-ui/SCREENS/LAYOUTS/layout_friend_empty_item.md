# پروندهٔ لایه — `res/layout/friend_empty_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/friend_empty_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/friend_empty_item.xml`](../../SOURCE/res/layout/friend_empty_item.xml) |
| SHA-256 دیکد | `89b222cf2a1f8f3d2aa7c1a7041139f4dd0138b98a219d1516a96c483fc0d1c7` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_friend_item
   ├─ TextView  #@id/tv_rank
   ├─ View  #@id/iv_avatar
   ├─ View  #@id/tv_username_friend_podium_item
   └─ View
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/root_friend_item` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `60.000000dip` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 5 | `TextView` | `android:textColor` | `@color/text_primary` |
| 6 | `TextView` | `android:gravity` | `0x00000011` |
| 7 | `TextView` | `android:id` | `@id/tv_rank` |
| 8 | `TextView` | `android:visibility` | `invisible` |
| 9 | `TextView` | `android:layout_width` | `30.000000dip` |
| 10 | `TextView` | `android:layout_height` | `30.000000dip` |
| 11 | `TextView` | `android:layout_marginStart` | `@dimen/leaderboard_item_ranking_margin_start` |
| 12 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 13 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `TextView` | `style` | `@style/TextSubtitle` |
| 16 | `View` | `android:id` | `@id/iv_avatar` |
| 17 | `View` | `android:background` | `@drawable/background_friends_empty_item_round` |
| 18 | `View` | `android:layout_width` | `40.000000dip` |
| 19 | `View` | `android:layout_height` | `40.000000dip` |
| 20 | `View` | `android:layout_marginStart` | `@dimen/leaderboard_item_icon_margin_start` |
| 21 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 22 | `View` | `app:layout_constraintStart_toEndOf` | `@id/tv_rank` |
| 23 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 24 | `View` | `android:id` | `@id/tv_username_friend_podium_item` |
| 25 | `View` | `android:background` | `@drawable/background_friends_empty_item_rectangle` |
| 26 | `View` | `android:layout_width` | `80.000000dip` |
| 27 | `View` | `android:layout_height` | `12.000000dip` |
| 28 | `View` | `android:layout_marginStart` | `@dimen/leaderboard_item_name_margin_start` |
| 29 | `View` | `android:layout_marginEnd` | `4.000000dip` |
| 30 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 31 | `View` | `app:layout_constraintHorizontal_bias` | `0.000000` |
| 32 | `View` | `app:layout_constraintStart_toEndOf` | `@id/iv_avatar` |
| 33 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 34 | `View` | `android:background` | `@drawable/background_friends_empty_item_rectangle` |
| 35 | `View` | `android:layout_width` | `36.000000dip` |
| 36 | `View` | `android:layout_height` | `12.000000dip` |
| 37 | `View` | `android:layout_marginEnd` | `@dimen/leaderboard_item_sparks_margin_end` |
| 38 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 39 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 40 | `View` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/leaderboard_item_icon_margin_start` | `14.000000dip` / `22.000000dip` (sw600dp) |
| `@dimen/leaderboard_item_name_margin_start` | `20.000000dip` |
| `@dimen/leaderboard_item_ranking_margin_start` | `8.000000dip` / `22.000000dip` (sw600dp) |
| `@dimen/leaderboard_item_sparks_margin_end` | `12.000000dip` / `24.000000dip` (sw600dp) |
| `@style/TextSubtitle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_avatar
@id/root_friend_item
@id/tv_rank
@id/tv_username_friend_podium_item
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/chapter_finished_leaderboard_status.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/root_friend_item" android:layout_width="match_parent" android:layout_height="60.000000dip" android:foreground="?attr/selectableItemBackground">
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_rank" android:visibility="invisible" android:layout_width="30.000000dip" android:layout_height="30.000000dip" android:layout_marginStart="@dimen/leaderboard_item_ranking_margin_start" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextSubtitle"/>
  <View android:id="@id/iv_avatar" android:background="@drawable/background_friends_empty_item_round" android:layout_width="40.000000dip" android:layout_height="40.000000dip" android:layout_marginStart="@dimen/leaderboard_item_icon_margin_start" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toEndOf="@id/tv_rank" app:layout_constraintTop_toTopOf="0"/>
  <View android:id="@id/tv_username_friend_podium_item" android:background="@drawable/background_friends_empty_item_rectangle" android:layout_width="80.000000dip" android:layout_height="12.000000dip" android:layout_marginStart="@dimen/leaderboard_item_name_margin_start" android:layout_marginEnd="4.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintHorizontal_bias="0.000000" app:layout_constraintStart_toEndOf="@id/iv_avatar" app:layout_constraintTop_toTopOf="0"/>
  <View android:background="@drawable/background_friends_empty_item_rectangle" android:layout_width="36.000000dip" android:layout_height="12.000000dip" android:layout_marginEnd="@dimen/leaderboard_item_sparks_margin_end" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
