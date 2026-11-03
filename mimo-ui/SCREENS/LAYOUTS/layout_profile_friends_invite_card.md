# پروندهٔ لایه — `res/layout/profile_friends_invite_card.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_friends_invite_card.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_friends_invite_card.xml`](../../SOURCE/res/layout/profile_friends_invite_card.xml) |
| SHA-256 دیکد | `0fb2e23ff4a886303b5f4a51ad2c9ac13bb02c1fa83470489c5bd027e5051c94` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView  #@id/cv_profile_invite_card
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_friends_banner
      ├─ TextView  #@id/tv_friends_banner_description
      └─ androidx.compose.ui.platform.ComposeView  #@id/btn_friends_banner_invite
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:id` | `@id/cv_profile_invite_card` |
| 2 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 3 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.cardview.widget.CardView` | `android:foreground` | `?attr/selectableItemBackground` |
| 5 | `androidx.cardview.widget.CardView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 6 | `androidx.cardview.widget.CardView` | `android:layout_marginVertical` | `@dimen/spacing_s_expandable` |
| 7 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 8 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 9 | `androidx.cardview.widget.CardView` | `app:cardElevation` | `2.000000dip` |
| 10 | `androidx.cardview.widget.CardView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `androidx.cardview.widget.CardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `androidx.cardview.widget.CardView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_friends_title` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 15 | `ImageView` | `android:id` | `@id/iv_friends_banner` |
| 16 | `ImageView` | `android:layout_width` | `70.000000dip` |
| 17 | `ImageView` | `android:layout_height` | `87.000000dip` |
| 18 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 19 | `ImageView` | `android:layout_marginBottom` | `@dimen/spacing_s` |
| 20 | `ImageView` | `android:src` | `@drawable/ic_profile_gift` |
| 21 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 22 | `ImageView` | `app:layout_constrainedWidth` | `true` |
| 23 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 26 | `ImageView` | `app:layout_constraintWidth_default` | `1` |
| 27 | `ImageView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 28 | `TextView` | `android:textColor` | `@color/text_weak` |
| 29 | `TextView` | `android:id` | `@id/tv_friends_banner_description` |
| 30 | `TextView` | `android:layout_width` | `0.000000dip` |
| 31 | `TextView` | `android:layout_height` | `wrap_content` |
| 32 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 33 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_l` |
| 34 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 35 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 36 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_friends_banner` |
| 37 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 38 | `TextView` | `style` | `@style/TextP1` |
| 39 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_friends_banner_invite` |
| 40 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_xs` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/spacing_xxs` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toEndOf` | `@id/iv_friends_banner` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_friends_banner_description` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/card_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_friends_banner_invite
@id/cv_profile_invite_card
@id/iv_friends_banner
@id/tv_friends_banner_description
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
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/cv_profile_invite_card" android:layout_width="match_parent" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackground" android:layout_marginHorizontal="@dimen/spacing_m_expandable" android:layout_marginVertical="@dimen/spacing_s_expandable" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large" app:cardElevation="2.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_friends_title">
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="match_parent">
    <ImageView android:id="@id/iv_friends_banner" android:layout_width="70.000000dip" android:layout_height="87.000000dip" android:layout_marginTop="@dimen/spacing_m" android:layout_marginBottom="@dimen/spacing_s" android:src="@drawable/ic_profile_gift" android:layout_marginStart="@dimen/spacing_m" app:layout_constrainedWidth="true" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintWidth_default="1" app:layout_constraintWidth_max="@dimen/general_max_width"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/tv_friends_banner_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginStart="@dimen/spacing_l" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_friends_banner" app:layout_constraintTop_toTopOf="0" style="@style/TextP1"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_friends_banner_invite" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xs" android:layout_marginStart="@dimen/spacing_xxs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toEndOf="@id/iv_friends_banner" app:layout_constraintTop_toBottomOf="@id/tv_friends_banner_description"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.cardview.widget.CardView>
```
