# پروندهٔ لایه — `res/layout/profile_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_fragment.xml`](../../SOURCE/res/layout/profile_fragment.xml) |
| SHA-256 دیکد | `8d91ffbc2d702ccfa88011c8cf82ac538adbc2e65811d315654681321cb10a80` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 12 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_profile_root
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_profile
   │  └─ include  #@id/layout_toolbar
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_profile
   ├─ com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView  #@id/anonymous_user_lock_view
   └─ com.getmimo.ui.components.common.OfflineView  #@id/profile_offline_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_profile_root` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `false` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_profile` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 9 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 10 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 11 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 12 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `include` | `android:id` | `@id/layout_toolbar` |
| 16 | `include` | `android:layout_width` | `match_parent` |
| 17 | `include` | `android:layout_height` | `@dimen/toolbar_height` |
| 18 | `include` | `layout` | `@layout/toolbar` |
| 19 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_profile` |
| 20 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `0.000000dip` |
| 21 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `0.000000dip` |
| 22 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |
| 23 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_profile` |
| 27 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintWidth_max` | `@dimen/content_max_width` |
| 28 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:id` | `@id/anonymous_user_lock_view` |
| 29 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:visibility` | `gone` |
| 30 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:layout_width` | `0.000000dip` |
| 31 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:layout_height` | `0.000000dip` |
| 32 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 33 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 34 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintStart_toStartOf` | `0` |
| 35 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_profile` |
| 36 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintWidth_max` | `@dimen/content_max_width` |
| 37 | `com.getmimo.ui.components.common.OfflineView` | `android:id` | `@id/profile_offline_view` |
| 38 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_width` | `0.000000dip` |
| 39 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_height` | `wrap_content` |
| 40 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 41 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 42 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintStart_toStartOf` | `0` |
| 43 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_profile` |
| 44 | `com.getmimo.ui.components.common.OfflineView` | `app:offline_description` | `@string/profile_offline_description` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/content_max_width` | `608.000000dip` |
| `@dimen/toolbar_height` | `56.000000dip` |
| `@string/profile_offline_description` | `Connect to the internet to see your Profile` / `Verbinde dich mit dem Internet, um dein Profil anzuzeigen` (de) / `Conéctate a internet para ver tu Perfil` (es) / `Connecte-toi à Internet pour voir ton profil` (fr) / `Hubungkan ke internet untuk melihat profilmu` (in) / `Connettiti a internet per vedere il tuo profilo` (it) / `Połącz się z internetem, aby zobaczyć swój profil` (pl) / `Conecte-se à internet para ver seu perfil` (pt-rBR) / `Подключись к Интернету, чтобы посмотреть Профиль` (ru) / `Profilini görmek için internete bağlan` (tr) |

## ۴. شناسه‌های `@id`

```text
@id/anonymous_user_lock_view
@id/appbar_profile
@id/layout_profile_root
@id/layout_toolbar
@id/profile_offline_view
@id/rv_profile
```

## ۵. ارجاع به لایه‌های دیگر

```text
@dimen/toolbar_height
@layout/toolbar
match_parent
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/layout_profile_root" android:background="@color/background_primary" android:fitsSystemWindows="false" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_profile" android:background="@color/navbar_background" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:elevation="0.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_profile" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_profile" app:layout_constraintWidth_max="@dimen/content_max_width"/>
  <com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView android:id="@id/anonymous_user_lock_view" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_profile" app:layout_constraintWidth_max="@dimen/content_max_width"/>
  <com.getmimo.ui.components.common.OfflineView android:id="@id/profile_offline_view" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_profile" app:offline_description="@string/profile_offline_description"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
