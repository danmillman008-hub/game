# پروندهٔ لایه — `res/layout/leaderboard_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_fragment.xml`](../../SOURCE/res/layout/leaderboard_fragment.xml) |
| SHA-256 دیکد | `dcc8fa0019af143ae20c22eb3e767b8690b5e6c3bc1e6567b06a196e11379bde` |
| ریشه | `androidx.coordinatorlayout.widget.CoordinatorLayout` |
| تعداد گره | 9 |
| تعداد شناسه | 8 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout  #@id/root_leaderboard_fragment
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_leaderboard
   │  └─ include  #@id/layout_toolbar
   └─ FrameLayout
      ├─ com.getmimo.ui.components.common.OfflineView  #@id/layout_leaderboard_offline
      ├─ ProgressBar  #@id/pb_leaderboard_loading_progress
      ├─ include  #@id/layout_leaderboard_locked
      ├─ include  #@id/layout_leaderboard_active
      └─ com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView  #@id/anonymous_user_lock_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:id` | `@id/root_leaderboard_fragment` |
| 2 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `match_parent` |
| 4 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_leaderboard` |
| 5 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:visibility` | `gone` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 9 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 10 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 11 | `include` | `android:id` | `@id/layout_toolbar` |
| 12 | `include` | `android:layout_width` | `match_parent` |
| 13 | `include` | `android:layout_height` | `@dimen/toolbar_height` |
| 14 | `include` | `layout` | `@layout/toolbar` |
| 15 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 16 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 17 | `FrameLayout` | `app:layout_behavior` | `@string/appbar_scrolling_view_behavior` |
| 18 | `com.getmimo.ui.components.common.OfflineView` | `android:id` | `@id/layout_leaderboard_offline` |
| 19 | `com.getmimo.ui.components.common.OfflineView` | `android:visibility` | `gone` |
| 20 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_width` | `match_parent` |
| 21 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_height` | `match_parent` |
| 22 | `com.getmimo.ui.components.common.OfflineView` | `app:offline_description` | `@string/leaderboard_offline_message` |
| 23 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 24 | `ProgressBar` | `android:id` | `@id/pb_leaderboard_loading_progress` |
| 25 | `ProgressBar` | `android:visibility` | `gone` |
| 26 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 27 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 28 | `include` | `android:id` | `@id/layout_leaderboard_locked` |
| 29 | `include` | `android:visibility` | `gone` |
| 30 | `include` | `android:layout_width` | `match_parent` |
| 31 | `include` | `android:layout_height` | `match_parent` |
| 32 | `include` | `layout` | `@layout/leaderboard_fragment_locked` |
| 33 | `include` | `android:id` | `@id/layout_leaderboard_active` |
| 34 | `include` | `android:visibility` | `gone` |
| 35 | `include` | `android:layout_width` | `match_parent` |
| 36 | `include` | `android:layout_height` | `match_parent` |
| 37 | `include` | `layout` | `@layout/leaderboard_fragment_active` |
| 38 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:id` | `@id/anonymous_user_lock_view` |
| 39 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:visibility` | `gone` |
| 40 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:layout_width` | `match_parent` |
| 41 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/toolbar_height` | `56.000000dip` |
| `@string/appbar_scrolling_view_behavior` | `com.google.android.material.appbar.AppBarLayout$ScrollingViewBehavior` |
| `@string/leaderboard_offline_message` | `Connect to the internet to
use Weekly Leaderboard` / `Verbinde dich mit dem Internet, um das 
Wöchentliche Leaderboard zu nutzen` (de) / `Conéctate a internet para usar la Clasificación Semanal` (es) / `Connecte-toi à Internet 
pour accéder au Classement Hebdomadaire.` (fr) / `Hubungkan ke internet untuk
memakai Papan Peringkat Mingguan` (in) / `Connettiti a internet per usare
la classifica settimanale` (it) / `Połącz się z internetem, aby
korzystać z rankingu tygodnia` (pl) / `Conecte-se à internet para
usar a Leaderboard semanal` (pt-rBR) / `Подключись к интернету, чтобы
просмотреть Еженедельный Рейтинг` (ru) / `Haftalık Liderlik Tablosunu kullanmak için
internete bağlan` (tr) |

## ۴. شناسه‌های `@id`

```text
@id/anonymous_user_lock_view
@id/appbar_leaderboard
@id/layout_leaderboard_active
@id/layout_leaderboard_locked
@id/layout_leaderboard_offline
@id/layout_toolbar
@id/pb_leaderboard_loading_progress
@id/root_leaderboard_fragment
```

## ۵. ارجاع به لایه‌های دیگر

```text
@dimen/toolbar_height
@layout/leaderboard_fragment_active
@layout/leaderboard_fragment_locked
@layout/toolbar
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/root_leaderboard_fragment" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_leaderboard" android:background="@color/navbar_background" android:visibility="gone" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:elevation="0.000000dip">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <FrameLayout android:layout_width="match_parent" android:layout_height="match_parent" app:layout_behavior="@string/appbar_scrolling_view_behavior">
    <com.getmimo.ui.components.common.OfflineView android:id="@id/layout_leaderboard_offline" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" app:offline_description="@string/leaderboard_offline_message"/>
    <ProgressBar android:layout_gravity="0x00000011" android:id="@id/pb_leaderboard_loading_progress" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
    <include android:id="@id/layout_leaderboard_locked" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" layout="@layout/leaderboard_fragment_locked"/>
    <include android:id="@id/layout_leaderboard_active" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" layout="@layout/leaderboard_fragment_active"/>
    <com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView android:id="@id/anonymous_user_lock_view" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent"/>
  </FrameLayout>
</androidx.coordinatorlayout.widget.CoordinatorLayout>
```
