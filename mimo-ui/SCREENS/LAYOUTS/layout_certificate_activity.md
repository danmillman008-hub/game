# پروندهٔ لایه — `res/layout/certificate_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/certificate_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/certificate_activity.xml`](../../SOURCE/res/layout/certificate_activity.xml) |
| SHA-256 دیکد | `f73d039b97b96c13959661c25e036062fbf60be0bdb4c16a092697b4a44b0053` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 12 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_certificate_activity
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_certificate
   │  └─ include  #@id/layout_toolbar
   ├─ ImageView  #@id/iv_certificate_pdf
   ├─ ProgressBar  #@id/pb_certificate
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_download_certificate
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_certificate_activity` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `false` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_certificate` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 9 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 10 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 11 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 12 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `include` | `android:id` | `@id/layout_toolbar` |
| 14 | `include` | `android:layout_width` | `match_parent` |
| 15 | `include` | `android:layout_height` | `@dimen/toolbar_height` |
| 16 | `include` | `layout` | `@layout/toolbar` |
| 17 | `ImageView` | `android:id` | `@id/iv_certificate_pdf` |
| 18 | `ImageView` | `android:layout_width` | `match_parent` |
| 19 | `ImageView` | `android:layout_height` | `0.000000dip` |
| 20 | `ImageView` | `android:layout_marginTop` | `28.000000dip` |
| 21 | `ImageView` | `android:layout_marginBottom` | `28.000000dip` |
| 22 | `ImageView` | `android:contentDescription` | `@null` |
| 23 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `ImageView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 25 | `ImageView` | `app:layout_constraintRight_toRightOf` | `0` |
| 26 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_certificate` |
| 27 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 28 | `ProgressBar` | `android:id` | `@id/pb_certificate` |
| 29 | `ProgressBar` | `android:visibility` | `gone` |
| 30 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 31 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 32 | `ProgressBar` | `android:indeterminateTint` | `@color/progress_primary` |
| 33 | `ProgressBar` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `ProgressBar` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 35 | `ProgressBar` | `app:layout_constraintRight_toRightOf` | `0` |
| 36 | `ProgressBar` | `app:layout_constraintTop_toTopOf` | `0` |
| 37 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_download_certificate` |
| 38 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `invisible` |
| 39 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 40 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginRight` | `16.000000dip` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `16.000000dip` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintRight_toRightOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/progress_primary` | `#FF7E4BDE` / `#FFA175EA` (night) |
| `@dimen/toolbar_height` | `56.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/appbar_certificate
@id/btn_download_certificate
@id/iv_certificate_pdf
@id/layout_certificate_activity
@id/layout_toolbar
@id/pb_certificate
```

## ۵. ارجاع به لایه‌های دیگر

```text
@dimen/toolbar_height
@layout/toolbar
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.certificates.CertificateActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/layout_certificate_activity" android:background="@color/background_primary" android:fitsSystemWindows="false" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_certificate" android:background="@color/navbar_background" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:elevation="0.000000dip" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <ImageView android:id="@id/iv_certificate_pdf" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_marginTop="28.000000dip" android:layout_marginBottom="28.000000dip" android:contentDescription="@null" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_certificate"/>
  <ProgressBar android:layout_gravity="0x00000011" android:id="@id/pb_certificate" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:indeterminateTint="@color/progress_primary" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_download_certificate" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginRight="16.000000dip" android:layout_marginBottom="16.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintRight_toRightOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
