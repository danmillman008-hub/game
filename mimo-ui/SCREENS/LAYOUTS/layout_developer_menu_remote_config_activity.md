# پروندهٔ لایه — `res/layout/developer_menu_remote_config_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/developer_menu_remote_config_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/developer_menu_remote_config_activity.xml`](../../SOURCE/res/layout/developer_menu_remote_config_activity.xml) |
| SHA-256 دیکد | `af6d9b91f60f54e62fdb05f8b07125941d7ea675e7283b030f55a9dfa03358c9` |
| ریشه | `androidx.coordinatorlayout.widget.CoordinatorLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 14 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_developermenu
   │  └─ include  #@id/layout_toolbar
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ EditText  #@id/et_remote_config_id
      ├─ EditText  #@id/et_remote_config_value
      ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_remote_config_add
      └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_remote_config
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:fitsSystemWindows` | `true` |
| 2 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `match_parent` |
| 4 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_developermenu` |
| 5 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `include` | `android:id` | `@id/layout_toolbar` |
| 12 | `include` | `android:layout_width` | `match_parent` |
| 13 | `include` | `android:layout_height` | `wrap_content` |
| 14 | `include` | `android:title` | `@string/developer_menu_override_remote_config` |
| 15 | `include` | `layout` | `@layout/toolbar` |
| 16 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 17 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 18 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_behavior` | `@string/appbar_scrolling_view_behavior` |
| 19 | `EditText` | `android:id` | `@id/et_remote_config_id` |
| 20 | `EditText` | `android:layout_width` | `match_parent` |
| 21 | `EditText` | `android:layout_height` | `wrap_content` |
| 22 | `EditText` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 23 | `EditText` | `android:hint` | `@string/developer_menu_override_remote_config_hint_id` |
| 24 | `EditText` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 25 | `EditText` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 26 | `EditText` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `EditText` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `EditText` | `app:layout_constraintTop_toTopOf` | `0` |
| 29 | `EditText` | `android:id` | `@id/et_remote_config_value` |
| 30 | `EditText` | `android:layout_width` | `match_parent` |
| 31 | `EditText` | `android:layout_height` | `wrap_content` |
| 32 | `EditText` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 33 | `EditText` | `android:hint` | `@string/developer_menu_override_remote_config_hint_value` |
| 34 | `EditText` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 35 | `EditText` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 36 | `EditText` | `app:layout_constraintEnd_toEndOf` | `0` |
| 37 | `EditText` | `app:layout_constraintStart_toStartOf` | `0` |
| 38 | `EditText` | `app:layout_constraintTop_toBottomOf` | `@id/et_remote_config_id` |
| 39 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_remote_config_add` |
| 40 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/et_remote_config_value` |
| 45 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_remote_config` |
| 46 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `0.000000dip` |
| 47 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `0.000000dip` |
| 48 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |
| 49 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 50 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 51 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintStart_toStartOf` | `0` |
| 52 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintTop_toBottomOf` | `@id/btn_remote_config_add` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@string/appbar_scrolling_view_behavior` | `com.google.android.material.appbar.AppBarLayout$ScrollingViewBehavior` |
| `@string/developer_menu_override_remote_config` | `Override remote config` |
| `@string/developer_menu_override_remote_config_hint_id` | `Id` |
| `@string/developer_menu_override_remote_config_hint_value` | `Value` |

## ۴. شناسه‌های `@id`

```text
@id/appbar_developermenu
@id/btn_remote_config_add
@id/et_remote_config_id
@id/et_remote_config_value
@id/layout_toolbar
@id/rv_remote_config
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/toolbar
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.developermenu.DeveloperMenuActivity
com.getmimo.ui.developermenu.DeveloperMenuFragment
com.getmimo.ui.developermenu.remoteconfig.DevMenuRemoteConfigActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_developermenu" android:background="@color/navbar_background" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:title="@string/developer_menu_override_remote_config" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="match_parent" app:layout_behavior="@string/appbar_scrolling_view_behavior">
    <EditText android:id="@id/et_remote_config_id" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:hint="@string/developer_menu_override_remote_config_hint_id" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
    <EditText android:id="@id/et_remote_config_value" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:hint="@string/developer_menu_override_remote_config_hint_value" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/et_remote_config_id"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_remote_config_add" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/et_remote_config_value"/>
    <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_remote_config" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/btn_remote_config_add"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.coordinatorlayout.widget.CoordinatorLayout>
```
