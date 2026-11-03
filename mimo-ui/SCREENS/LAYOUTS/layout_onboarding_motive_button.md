# پروندهٔ لایه — `res/layout/onboarding_motive_button.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_motive_button.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_motive_button.xml`](../../SOURCE/res/layout/onboarding_motive_button.xml) |
| SHA-256 دیکد | `36202177ff5c06fe0deecec5f9738eaa184182fbe5e04567f198273e091ec3cc` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView
   └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_course_card_root
      ├─ ImageView  #@id/iv_motive_button
      └─ TextView  #@id/tv_motive_button
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:clipChildren` | `false` |
| 2 | `androidx.cardview.widget.CardView` | `android:clipToPadding` | `false` |
| 3 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 4 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 5 | `androidx.cardview.widget.CardView` | `android:layout_margin` | `2.000000dip` |
| 6 | `androidx.cardview.widget.CardView` | `android:foreground` | `?attr/selectableItemBackground` |
| 7 | `androidx.cardview.widget.CardView` | `android:minHeight` | `80.000000dip` |
| 8 | `androidx.cardview.widget.CardView` | `android:elevation` | `4.000000dip` |
| 9 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/selection_enabled` |
| 10 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_course_card_root` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:minHeight` | `80.000000dip` |
| 15 | `ImageView` | `android:id` | `@id/iv_motive_button` |
| 16 | `ImageView` | `android:layout_width` | `48.000000dip` |
| 17 | `ImageView` | `android:layout_height` | `48.000000dip` |
| 18 | `ImageView` | `android:layout_marginTop` | `14.000000dip` |
| 19 | `ImageView` | `android:layout_marginBottom` | `14.000000dip` |
| 20 | `ImageView` | `android:src` | `@drawable/freemium_project` |
| 21 | `ImageView` | `android:contentDescription` | `@null` |
| 22 | `ImageView` | `android:layout_marginStart` | `20.000000dip` |
| 23 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 26 | `TextView` | `android:id` | `@id/tv_motive_button` |
| 27 | `TextView` | `android:layout_width` | `0.000000dip` |
| 28 | `TextView` | `android:layout_height` | `wrap_content` |
| 29 | `TextView` | `android:layout_marginStart` | `20.000000dip` |
| 30 | `TextView` | `android:layout_marginEnd` | `20.000000dip` |
| 31 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 32 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 33 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_motive_button` |
| 34 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 35 | `TextView` | `style` | `@style/TextViewMotiveButton` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/selection_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@style/TextViewMotiveButton` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/iv_motive_button
@id/layout_course_card_root
@id/tv_motive_button
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.OnboardingActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_margin="2.000000dip" android:foreground="?attr/selectableItemBackground" android:minHeight="80.000000dip" android:elevation="4.000000dip" app:cardBackgroundColor="@color/selection_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large">
  <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/layout_course_card_root" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="80.000000dip">
    <ImageView android:id="@id/iv_motive_button" android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:layout_marginTop="14.000000dip" android:layout_marginBottom="14.000000dip" android:src="@drawable/freemium_project" android:contentDescription="@null" android:layout_marginStart="20.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
    <TextView android:id="@id/tv_motive_button" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginStart="20.000000dip" android:layout_marginEnd="20.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_motive_button" app:layout_constraintTop_toTopOf="0" style="@style/TextViewMotiveButton"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.cardview.widget.CardView>
```
