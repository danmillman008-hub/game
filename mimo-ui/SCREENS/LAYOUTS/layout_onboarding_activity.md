# پروندهٔ لایه — `res/layout/onboarding_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_activity.xml`](../../SOURCE/res/layout/onboarding_activity.xml) |
| SHA-256 دیکد | `94c7a602f088c70e9adf1042bfb8300c7a8b47902c00696b53f744276173cf05` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/onboarding_root
   ├─ androidx.compose.ui.platform.ComposeView  #@id/onboarding_progress_bar
   └─ androidx.fragment.app.FragmentContainerView  #@id/container
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/onboarding_root` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/onboarding_progress_bar` |
| 6 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 7 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 8 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 9 | `androidx.fragment.app.FragmentContainerView` | `android:name` | `androidx.navigation.fragment.NavHostFragment` |
| 10 | `androidx.fragment.app.FragmentContainerView` | `android:id` | `@id/container` |
| 11 | `androidx.fragment.app.FragmentContainerView` | `android:layout_width` | `match_parent` |
| 12 | `androidx.fragment.app.FragmentContainerView` | `android:layout_height` | `0.000000dip` |
| 13 | `androidx.fragment.app.FragmentContainerView` | `android:layout_weight` | `1.000000` |
| 14 | `androidx.fragment.app.FragmentContainerView` | `app:defaultNavHost` | `true` |
| 15 | `androidx.fragment.app.FragmentContainerView` | `app:navGraph` | `@navigation/nav_onboarding_graph` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/spacing_m` | `16.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/container
@id/onboarding_progress_bar
@id/onboarding_root
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:id="@id/onboarding_root" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.compose.ui.platform.ComposeView android:id="@id/onboarding_progress_bar" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m"/>
  <androidx.fragment.app.FragmentContainerView android:name="androidx.navigation.fragment.NavHostFragment" android:id="@id/container" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_weight="1.000000" app:defaultNavHost="true" app:navGraph="@navigation/nav_onboarding_graph"/>
</LinearLayout>
```
