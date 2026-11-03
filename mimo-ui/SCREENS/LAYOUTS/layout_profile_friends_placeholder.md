# پروندهٔ لایه — `res/layout/profile_friends_placeholder.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_friends_placeholder.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_friends_placeholder.xml`](../../SOURCE/res/layout/profile_friends_placeholder.xml) |
| SHA-256 دیکد | `96fc49c30c9c47fb8758f03ab056cc61fa5dff1a720e77ff6070e5a1f41c0b44` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_friend_item
   ├─ com.getmimo.ui.components.placeholder.PlaceholderView  #@id/iv_avatar
   ├─ com.getmimo.ui.components.placeholder.PlaceholderView  #@id/tv_username_friend_podium_item
   └─ com.getmimo.ui.components.placeholder.PlaceholderView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/root_friend_item` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `60.000000dip` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 7 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:id` | `@id/iv_avatar` |
| 8 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:background` | `@drawable/background_friends_empty_item_round` |
| 9 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_width` | `40.000000dip` |
| 10 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_height` | `40.000000dip` |
| 11 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_marginStart` | `52.000000dip` |
| 12 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:corner_radius` | `60.000000dip` |
| 13 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 14 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintStart_toStartOf` | `0` |
| 15 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintTop_toTopOf` | `0` |
| 16 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:id` | `@id/tv_username_friend_podium_item` |
| 17 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:background` | `@drawable/background_friends_empty_item_rectangle` |
| 18 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_width` | `160.000000dip` |
| 19 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_height` | `16.000000dip` |
| 20 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_marginStart` | `@dimen/leaderboard_item_name_margin_start` |
| 21 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_marginEnd` | `4.000000dip` |
| 22 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 23 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintEnd_toStartOf` | `@id/iv_avatar` |
| 24 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintHorizontal_bias` | `0.000000` |
| 25 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintStart_toEndOf` | `@id/iv_avatar` |
| 26 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintTop_toTopOf` | `0` |
| 27 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:background` | `@drawable/background_friends_empty_item_rectangle` |
| 28 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_width` | `50.000000dip` |
| 29 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_height` | `16.000000dip` |
| 30 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `android:layout_marginEnd` | `@dimen/spacing_s_expandable` |
| 31 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 32 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 33 | `com.getmimo.ui.components.placeholder.PlaceholderView` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/leaderboard_item_name_margin_start` | `20.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_avatar
@id/root_friend_item
@id/tv_username_friend_podium_item
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/root_friend_item" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="60.000000dip" android:foreground="?attr/selectableItemBackground" android:layout_marginHorizontal="@dimen/spacing_m_expandable">
  <com.getmimo.ui.components.placeholder.PlaceholderView android:id="@id/iv_avatar" android:background="@drawable/background_friends_empty_item_round" android:layout_width="40.000000dip" android:layout_height="40.000000dip" android:layout_marginStart="52.000000dip" app:corner_radius="60.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <com.getmimo.ui.components.placeholder.PlaceholderView android:id="@id/tv_username_friend_podium_item" android:background="@drawable/background_friends_empty_item_rectangle" android:layout_width="160.000000dip" android:layout_height="16.000000dip" android:layout_marginStart="@dimen/leaderboard_item_name_margin_start" android:layout_marginEnd="4.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/iv_avatar" app:layout_constraintHorizontal_bias="0.000000" app:layout_constraintStart_toEndOf="@id/iv_avatar" app:layout_constraintTop_toTopOf="0"/>
  <com.getmimo.ui.components.placeholder.PlaceholderView android:background="@drawable/background_friends_empty_item_rectangle" android:layout_width="50.000000dip" android:layout_height="16.000000dip" android:layout_marginEnd="@dimen/spacing_s_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
