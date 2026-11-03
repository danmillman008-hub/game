# پروندهٔ لایه — `res/layout/profile_friend_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_friend_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_friend_item.xml`](../../SOURCE/res/layout/profile_friend_item.xml) |
| SHA-256 دیکد | `3e9ea93dd44b7ae728a940a98fc21f40e3503be13f179bf6b69b58bfe25e1b31` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 8 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_friend_item
   ├─ ImageView  #@id/iv_avatar
   ├─ TextView  #@id/tv_username_friend_podium_item
   ├─ TextView  #@id/tv_sparks
   ├─ ImageView  #@id/iv_sparks
   ├─ TextView  #@id/tv_streak
   ├─ ImageView  #@id/iv_streak
   └─ View  #@id/v_separator
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/root_friend_item` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `60.000000dip` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_s` |
| 7 | `ImageView` | `android:id` | `@id/iv_avatar` |
| 8 | `ImageView` | `android:layout_width` | `40.000000dip` |
| 9 | `ImageView` | `android:layout_height` | `40.000000dip` |
| 10 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_xxs` |
| 11 | `ImageView` | `android:layout_marginVertical` | `@dimen/spacing_s` |
| 12 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/v_separator` |
| 13 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `ImageView` | `app:srcCompat` | `@drawable/avatar_fallback_6` |
| 16 | `TextView` | `android:textColor` | `@color/text_primary` |
| 17 | `TextView` | `android:ellipsize` | `end` |
| 18 | `TextView` | `android:id` | `@id/tv_username_friend_podium_item` |
| 19 | `TextView` | `android:layout_width` | `0.000000dip` |
| 20 | `TextView` | `android:layout_height` | `wrap_content` |
| 21 | `TextView` | `android:maxLines` | `1` |
| 22 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 23 | `TextView` | `android:layout_marginEnd` | `4.000000dip` |
| 24 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/v_separator` |
| 25 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/iv_streak` |
| 26 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_avatar` |
| 27 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 28 | `TextView` | `style` | `@style/TextSubtitle` |
| 29 | `TextView` | `android:textColor` | `@color/text_primary` |
| 30 | `TextView` | `android:id` | `@id/tv_sparks` |
| 31 | `TextView` | `android:layout_width` | `wrap_content` |
| 32 | `TextView` | `android:layout_height` | `wrap_content` |
| 33 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xxs` |
| 34 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/v_separator` |
| 35 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 36 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 37 | `TextView` | `style` | `@style/TextSubtitle` |
| 38 | `ImageView` | `android:id` | `@id/iv_sparks` |
| 39 | `ImageView` | `android:layout_width` | `16.000000dip` |
| 40 | `ImageView` | `android:layout_height` | `16.000000dip` |
| 41 | `ImageView` | `android:layout_marginEnd` | `4.000000dip` |
| 42 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/tv_sparks` |
| 43 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_sparks` |
| 44 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_sparks` |
| 45 | `ImageView` | `app:srcCompat` | `@drawable/ic_bolt_charged` |
| 46 | `TextView` | `android:textColor` | `@color/text_primary` |
| 47 | `TextView` | `android:id` | `@id/tv_streak` |
| 48 | `TextView` | `android:layout_width` | `wrap_content` |
| 49 | `TextView` | `android:layout_height` | `wrap_content` |
| 50 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xs` |
| 51 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/v_separator` |
| 52 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/iv_sparks` |
| 53 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 54 | `TextView` | `style` | `@style/TextSubtitle` |
| 55 | `ImageView` | `android:id` | `@id/iv_streak` |
| 56 | `ImageView` | `android:layout_width` | `16.000000dip` |
| 57 | `ImageView` | `android:layout_height` | `16.000000dip` |
| 58 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_sparks` |
| 59 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_streak` |
| 60 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/iv_sparks` |
| 61 | `ImageView` | `app:srcCompat` | `@drawable/ic_streak_active` |
| 62 | `View` | `android:id` | `@id/v_separator` |
| 63 | `View` | `android:background` | `@color/line_primary` |
| 64 | `View` | `android:layout_width` | `0.000000dip` |
| 65 | `View` | `android:layout_height` | `1.000000dip` |
| 66 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 67 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 68 | `View` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/TextSubtitle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_avatar
@id/iv_sparks
@id/iv_streak
@id/root_friend_item
@id/tv_sparks
@id/tv_streak
@id/tv_username_friend_podium_item
@id/v_separator
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/root_friend_item" android:layout_width="match_parent" android:layout_height="60.000000dip" android:foreground="?attr/selectableItemBackground" android:layout_marginHorizontal="@dimen/spacing_m_expandable" android:paddingHorizontal="@dimen/spacing_s">
  <ImageView android:id="@id/iv_avatar" android:layout_width="40.000000dip" android:layout_height="40.000000dip" android:layout_marginStart="@dimen/spacing_xxs" android:layout_marginVertical="@dimen/spacing_s" app:layout_constraintBottom_toTopOf="@id/v_separator" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/avatar_fallback_6"/>
  <TextView android:textColor="@color/text_primary" android:ellipsize="end" android:id="@id/tv_username_friend_podium_item" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:maxLines="1" android:layout_marginStart="@dimen/spacing_s" android:layout_marginEnd="4.000000dip" app:layout_constraintBottom_toBottomOf="@id/v_separator" app:layout_constraintEnd_toStartOf="@id/iv_streak" app:layout_constraintStart_toEndOf="@id/iv_avatar" app:layout_constraintTop_toTopOf="0" style="@style/TextSubtitle"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_sparks" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_xxs" app:layout_constraintBottom_toTopOf="@id/v_separator" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextSubtitle"/>
  <ImageView android:id="@id/iv_sparks" android:layout_width="16.000000dip" android:layout_height="16.000000dip" android:layout_marginEnd="4.000000dip" app:layout_constraintBottom_toBottomOf="@id/tv_sparks" app:layout_constraintEnd_toStartOf="@id/tv_sparks" app:layout_constraintTop_toTopOf="@id/tv_sparks" app:srcCompat="@drawable/ic_bolt_charged"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_streak" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_xs" app:layout_constraintBottom_toTopOf="@id/v_separator" app:layout_constraintEnd_toStartOf="@id/iv_sparks" app:layout_constraintTop_toTopOf="0" style="@style/TextSubtitle"/>
  <ImageView android:id="@id/iv_streak" android:layout_width="16.000000dip" android:layout_height="16.000000dip" app:layout_constraintBottom_toBottomOf="@id/iv_sparks" app:layout_constraintEnd_toStartOf="@id/tv_streak" app:layout_constraintTop_toTopOf="@id/iv_sparks" app:srcCompat="@drawable/ic_streak_active"/>
  <View android:id="@id/v_separator" android:background="@color/line_primary" android:layout_width="0.000000dip" android:layout_height="1.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
