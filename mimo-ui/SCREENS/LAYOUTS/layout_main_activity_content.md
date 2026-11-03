# پروندهٔ لایه — `res/layout/main_activity_content.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/main_activity_content.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/main_activity_content.xml`](../../SOURCE/res/layout/main_activity_content.xml) |
| SHA-256 دیکد | `1eb9f5d27ac0d75fb171b1dc51eac29238784c60b72339ccde5d71fd02661171` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/main_activity_root
   ├─ FrameLayout  #@id/contentFrame
   └─ FrameLayout  #@id/container_bottombar
      └─ com.getmimo.ui.navigation.NavigationBar  #@id/navigation_bar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/main_activity_root` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `FrameLayout` | `android:id` | `@id/contentFrame` |
| 5 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 6 | `FrameLayout` | `android:layout_height` | `0.000000dip` |
| 7 | `FrameLayout` | `app:layout_constraintBottom_toTopOf` | `@id/container_bottombar` |
| 8 | `FrameLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `FrameLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `FrameLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `FrameLayout` | `android:layout_gravity` | `0x00000050` |
| 12 | `FrameLayout` | `android:id` | `@id/container_bottombar` |
| 13 | `FrameLayout` | `android:background` | `@color/background_secondary` |
| 14 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 15 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 16 | `FrameLayout` | `android:elevation` | `10.000000dip` |
| 17 | `FrameLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 18 | `FrameLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `FrameLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `com.getmimo.ui.navigation.NavigationBar` | `android:layout_gravity` | `0x00000011` |
| 21 | `com.getmimo.ui.navigation.NavigationBar` | `android:id` | `@id/navigation_bar` |
| 22 | `com.getmimo.ui.navigation.NavigationBar` | `android:layout_width` | `match_parent` |
| 23 | `com.getmimo.ui.navigation.NavigationBar` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |

## ۴. شناسه‌های `@id`

```text
@id/container_bottombar
@id/contentFrame
@id/main_activity_root
@id/navigation_bar
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.main.MainActivity
com.getmimo.ui.main.MainActivity$showRewardBottomSheet$1
com.getmimo.ui.main.MainActivity$showRewardBottomSheet$fragment$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/main_activity_root" android:layout_width="match_parent" android:layout_height="match_parent">
  <FrameLayout android:id="@id/contentFrame" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toTopOf="@id/container_bottombar" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <FrameLayout android:layout_gravity="0x00000050" android:id="@id/container_bottombar" android:background="@color/background_secondary" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:elevation="10.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0">
    <com.getmimo.ui.navigation.NavigationBar android:layout_gravity="0x00000011" android:id="@id/navigation_bar" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  </FrameLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
