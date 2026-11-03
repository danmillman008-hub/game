# پروندهٔ لایه — `res/layout/toolbar.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/toolbar.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/toolbar.xml`](../../SOURCE/res/layout/toolbar.xml) |
| SHA-256 دیکد | `0ea83d2f245a94bb130a8ba5f2a6e509ae313707ef97055f9ceb5d191fc1dfc8` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.appcompat.widget.Toolbar  #@id/toolbar
   └─ View
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.appcompat.widget.Toolbar` | `android:theme` | `@style/Toolbar` |
| 4 | `androidx.appcompat.widget.Toolbar` | `android:id` | `@id/toolbar` |
| 5 | `androidx.appcompat.widget.Toolbar` | `android:background` | `@color/navbar_background` |
| 6 | `androidx.appcompat.widget.Toolbar` | `android:layout_width` | `0.000000dip` |
| 7 | `androidx.appcompat.widget.Toolbar` | `android:layout_height` | `wrap_content` |
| 8 | `androidx.appcompat.widget.Toolbar` | `app:contentInsetStartWithNavigation` | `0.000000dip` |
| 9 | `androidx.appcompat.widget.Toolbar` | `app:elevation` | `0.000000dip` |
| 10 | `androidx.appcompat.widget.Toolbar` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 11 | `androidx.appcompat.widget.Toolbar` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `androidx.appcompat.widget.Toolbar` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `androidx.appcompat.widget.Toolbar` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `androidx.appcompat.widget.Toolbar` | `app:navigationIcon` | `@drawable/ic_arrow_left` |
| 15 | `androidx.appcompat.widget.Toolbar` | `app:popupTheme` | `@style/ThemeOverlay.AppCompat.DayNight` |
| 16 | `androidx.appcompat.widget.Toolbar` | `app:titleTextAppearance` | `@style/TextToolbarTitle` |
| 17 | `View` | `android:background` | `@color/navbar_line` |
| 18 | `View` | `android:layout_width` | `0.000000dip` |
| 19 | `View` | `android:layout_height` | `1.000000dip` |
| 20 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 21 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 22 | `View` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/navbar_line` | `#FFEDEEF6` / `#FF4A4D85` (night) |
| `@style/TextToolbarTitle` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}]` |
| `@style/ThemeOverlay.AppCompat.DayNight` | `[]` / `[]` (night) |
| `@style/Toolbar` | `[{'attr': 'attr.colorControlNormal', 'attr_id': '0x7F040122', 'value': '@color/icon_weak', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/toolbar
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/abtest_config_activity.xml
res/layout/build_tab_fragment.xml
res/layout/certificate_activity.xml
res/layout/developer_menu_campaign_activity.xml
res/layout/developer_menu_content_experiment_activity.xml
res/layout/developer_menu_discount_activity.xml
res/layout/developer_menu_remote_config_activity.xml
res/layout/developermenu_activity.xml
res/layout/integrated_webview_activity.xml
res/layout/leaderboard_fragment.xml
res/layout/practice_tab_fragment.xml
res/layout/profile_fragment.xml
res/layout/public_profile_fragment.xml
res/layout/set_daily_goal_activity.xml
res/layout/settings_activity.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content">
  <androidx.appcompat.widget.Toolbar android:theme="@style/Toolbar" android:id="@id/toolbar" android:background="@color/navbar_background" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:contentInsetStartWithNavigation="0.000000dip" app:elevation="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:navigationIcon="@drawable/ic_arrow_left" app:popupTheme="@style/ThemeOverlay.AppCompat.DayNight" app:titleTextAppearance="@style/TextToolbarTitle"/>
  <View android:background="@color/navbar_line" android:layout_width="0.000000dip" android:layout_height="1.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
