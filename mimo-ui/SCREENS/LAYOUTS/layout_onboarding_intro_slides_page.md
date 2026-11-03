# پروندهٔ لایه — `res/layout/onboarding_intro_slides_page.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/onboarding_intro_slides_page.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/onboarding_intro_slides_page.xml`](../../SOURCE/res/layout/onboarding_intro_slides_page.xml) |
| SHA-256 دیکد | `0f4ab7bbb266a0db3b8a805ef1e71ea3caf44ed0b6f6289826a06e52986ab0f2` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 11 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_rive_animation
   └─ LinearLayout  #@id/layout_slide_text_views
      ├─ TextView  #@id/tv_onboarding_page_title
      └─ TextView  #@id/tv_onboarding_page_description
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 5 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/iv_rive_animation` |
| 6 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `0.000000dip` |
| 7 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `wrap_content` |
| 8 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 9 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constrainedHeight` | `true` |
| 10 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintBottom_toTopOf` | `@id/layout_slide_text_views` |
| 11 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 12 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintRight_toRightOf` | `0` |
| 13 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 15 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 16 | `LinearLayout` | `android:orientation` | `vertical` |
| 17 | `LinearLayout` | `android:id` | `@id/layout_slide_text_views` |
| 18 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 19 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 20 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 21 | `LinearLayout` | `android:layout_centerHorizontal` | `true` |
| 22 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 23 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `LinearLayout` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 25 | `LinearLayout` | `app:layout_constraintRight_toRightOf` | `0` |
| 26 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/iv_rive_animation` |
| 27 | `TextView` | `android:gravity` | `0x00000001` |
| 28 | `TextView` | `android:id` | `@id/tv_onboarding_page_title` |
| 29 | `TextView` | `android:layout_width` | `wrap_content` |
| 30 | `TextView` | `android:layout_height` | `wrap_content` |
| 31 | `TextView` | `android:layout_marginBottom` | `10.000000dip` |
| 32 | `TextView` | `android:text` | `@string/onboarding_page_1_title` |
| 33 | `TextView` | `style` | `@style/TextViewOnBoardingPageTitle` |
| 34 | `TextView` | `android:gravity` | `0x00000001` |
| 35 | `TextView` | `android:id` | `@id/tv_onboarding_page_description` |
| 36 | `TextView` | `android:layout_width` | `wrap_content` |
| 37 | `TextView` | `android:layout_height` | `wrap_content` |
| 38 | `TextView` | `android:text` | `@string/onboarding_page_1_description` |
| 39 | `TextView` | `android:minLines` | `3` |
| 40 | `TextView` | `style` | `@style/TextViewOnBoardingPageDescription` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@string/onboarding_page_1_description` | `Bite-sized lessons that fit your schedule` / `Kurze Lektionen, die in deinen Zeitplan passen` (de) / `Lecciones breves que se adaptan a tu horario` (es) / `Des leçons courtes adaptées à ton emploi du temps` (fr) / `Pelajaran singkat yang pas dengan jadwalmu` (in) / `Lezioni brevi che si adattano ai tuoi tempi` (it) / `Krótkie lekcje, które zmieszczą się w twoim planie dnia` (pl) / `Aulas curtas que cabem na sua rotina` (pt-rBR) / `Короткие уроки, которые впишутся в твой график` (ru) / `Programına uyan kısa dersler` (tr) |
| `@string/onboarding_page_1_title` | `Learn at your own pace` / `Lerne in deinem eigenen Tempo` (de) / `Aprende a tu propio ritmo` (es) / `Apprends à ton propre rythme` (fr) / `Belajar sesuai ritmemu` (in) / `Impara al tuo ritmo` (it) / `Ucz się we własnym tempie` (pl) / `Aprenda no seu próprio ritmo` (pt-rBR) / `Учись в своём темпе` (ru) / `Kendi hızında öğren` (tr) |
| `@style/TextViewOnBoardingPageDescription` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}]` |
| `@style/TextViewOnBoardingPageTitle` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/iv_rive_animation
@id/layout_slide_text_views
@id/tv_onboarding_page_description
@id/tv_onboarding_page_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.OnboardingActivity
com.getmimo.ui.onboarding.intro.IntroSlidesActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="match_parent" android:maxWidth="@dimen/general_max_width">
  <app.rive.runtime.kotlin.RiveAnimationView android:id="@id/iv_rive_animation" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constrainedHeight="true" app:layout_constraintBottom_toTopOf="@id/layout_slide_text_views" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2"/>
  <LinearLayout android:gravity="0x00000011" android:orientation="vertical" android:id="@id/layout_slide_text_views" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_centerHorizontal="true" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/iv_rive_animation">
    <TextView android:gravity="0x00000001" android:id="@id/tv_onboarding_page_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="10.000000dip" android:text="@string/onboarding_page_1_title" style="@style/TextViewOnBoardingPageTitle"/>
    <TextView android:gravity="0x00000001" android:id="@id/tv_onboarding_page_description" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/onboarding_page_1_description" android:minLines="3" style="@style/TextViewOnBoardingPageDescription"/>
  </LinearLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
