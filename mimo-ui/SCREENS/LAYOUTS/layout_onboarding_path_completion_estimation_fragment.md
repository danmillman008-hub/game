# پروندهٔ لایه — `res/layout/onboarding_path_completion_estimation_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_path_completion_estimation_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_path_completion_estimation_fragment.xml`](../../SOURCE/res/layout/onboarding_path_completion_estimation_fragment.xml) |
| SHA-256 دیکد | `19ba7fd5934ca419af609549f21e62c515b8ace4e4317701d822c8a0b8f4e09b` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 14 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_daily_goal_title
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rav_path_completion_estimation
   ├─ ProgressBar  #@id/progressbar
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:animateLayoutChanges` | `true` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_l` |
| 7 | `TextView` | `android:textColor` | `@color/text_primary` |
| 8 | `TextView` | `android:gravity` | `0x00000011` |
| 9 | `TextView` | `android:id` | `@id/tv_set_daily_goal_title` |
| 10 | `TextView` | `android:layout_width` | `0.000000dip` |
| 11 | `TextView` | `android:layout_height` | `wrap_content` |
| 12 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 13 | `TextView` | `android:text` | `@string/onboarding_path_completion_estimation_title` |
| 14 | `TextView` | `android:minLines` | `2` |
| 15 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 16 | `TextView` | `app:layout_constraintRight_toRightOf` | `0` |
| 17 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 18 | `TextView` | `style` | `@style/TextH1` |
| 19 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/rav_path_completion_estimation` |
| 20 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `0.000000dip` |
| 21 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `0.000000dip` |
| 22 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 23 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginHorizontal` | `@dimen/spacing_xs_expandable` |
| 24 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 25 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintDimensionRatio` | `1:1` |
| 26 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_daily_goal_title` |
| 29 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintVertical_bias` | `0.350000` |
| 30 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 31 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveAssetLoaderClass` | `com.getmimo.apputil.RiveFontAssetLoader` |
| 32 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveAutoPlay` | `false` |
| 33 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveLoop` | `3` |
| 34 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveResource` | `@raw/path_completion_estimation` |
| 35 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveStateMachine` | `default` |
| 36 | `ProgressBar` | `android:id` | `@id/progressbar` |
| 37 | `ProgressBar` | `android:visibility` | `gone` |
| 38 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 39 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 40 | `ProgressBar` | `android:elevation` | `1.000000dip` |
| 41 | `ProgressBar` | `android:indeterminateTint` | `@color/progress_primary` |
| 42 | `ProgressBar` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 43 | `ProgressBar` | `app:layout_constraintEnd_toEndOf` | `0` |
| 44 | `ProgressBar` | `app:layout_constraintStart_toStartOf` | `0` |
| 45 | `ProgressBar` | `app:layout_constraintTop_toTopOf` | `0` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_content` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 51 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/progress_primary` | `#FF7E4BDE` / `#FFA175EA` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs_expandable` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@string/onboarding_path_completion_estimation_title` | `You’ll be creating programs in no time!` / `Du wirst im Nullkommanichts Programme erstellen!` (de) / `¡Crearás programas muy pronto!` (es) / `Crée des applications en un rien de temps !` (fr) / `Sebentar lagi kamu bisa bikin program!` (in) / `Creerai programmi in men che non si dica!` (it) / `W mig zaczniesz tworzyć programy!` (pl) / `Você estará criando programas em pouco tempo!` (pt-rBR) / `Ты сразу сможешь начать создавать программы!` (ru) / `Çok kısa sürede program yazıyor olacaksın!` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/compose_content
@id/progressbar
@id/rav_path_completion_estimation
@id/tv_set_daily_goal_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.OnboardingActivity
com.getmimo.ui.onboarding.pathcompletionestimation.PathCompletionEstimationFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="match_parent" android:maxWidth="@dimen/general_max_width" android:animateLayoutChanges="true" android:paddingHorizontal="@dimen/spacing_l">
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_set_daily_goal_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/onboarding_path_completion_estimation_title" android:minLines="2" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
  <app.rive.runtime.kotlin.RiveAnimationView android:id="@id/rav_path_completion_estimation" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_marginTop="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_xs_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintDimensionRatio="1:1" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_set_daily_goal_title" app:layout_constraintVertical_bias="0.350000" app:layout_constraintWidth_max="@dimen/general_max_width" app:riveAssetLoaderClass="com.getmimo.apputil.RiveFontAssetLoader" app:riveAutoPlay="false" app:riveLoop="3" app:riveResource="@raw/path_completion_estimation" app:riveStateMachine="default"/>
  <ProgressBar android:id="@id/progressbar" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:elevation="1.000000dip" android:indeterminateTint="@color/progress_primary" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_content" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
