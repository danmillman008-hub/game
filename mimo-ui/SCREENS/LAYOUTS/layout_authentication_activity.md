# پروندهٔ لایه — `res/layout/authentication_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/authentication_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/authentication_activity.xml`](../../SOURCE/res/layout/authentication_activity.xml) |
| SHA-256 دیکد | `90a8bb590884cac71b2614ab6f3a13226ff5502d3c868096f6c1d9839b95f551` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container
   └─ ProgressBar  #@id/authentication_progress
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/container` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 6 | `ProgressBar` | `android:id` | `@id/authentication_progress` |
| 7 | `ProgressBar` | `android:visibility` | `gone` |
| 8 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 9 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 10 | `ProgressBar` | `android:elevation` | `2.000000dip` |
| 11 | `ProgressBar` | `android:indeterminateTint` | `@color/progress_primary` |
| 12 | `ProgressBar` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 13 | `ProgressBar` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 14 | `ProgressBar` | `app:layout_constraintRight_toRightOf` | `0` |
| 15 | `ProgressBar` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/progress_primary` | `#FF7E4BDE` / `#FFA175EA` (night) |

## ۴. شناسه‌های `@id`

```text
@id/authentication_progress
@id/container
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.authentication.AuthenticationActivity
com.getmimo.ui.authentication.AuthenticationFragment$configureButtons$2
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/container" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <ProgressBar android:layout_gravity="0x00000011" android:id="@id/authentication_progress" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:elevation="2.000000dip" android:indeterminateTint="@color/progress_primary" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
