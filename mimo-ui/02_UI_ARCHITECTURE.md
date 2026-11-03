# ۰۲ — معماری رابط کاربری (چطور چیده شده)

## یک جمله

Mimo 9.35 یک **اپ هیبریدی سه لایه** است: اسکلت `Activity/Fragment` با **XML View**،
جزایر **Jetpack Compose** داخل همان لایهها، و **WebView** برای رندر محتوای درس/ادیتور کد.

## لایهٔ ۱ — اعلان در manifest

| مورد | تعداد / مقدار |
|---|---|
| `<activity>` | ۶۱ (۳۶ تای آن `com.getmimo.*`) |
| `<activity-alias>` | ۶ (`SplashActivity_default`، `_ninja`، `_ukraine`، `_chemist`، `_bat`، `_proud`) |
| اکتیویتی راهانداز | `com.getmimo.ui.SplashActivity_default` (alias) |
| تم پیشفرض اپلیکیشن | `@style/MaterialDarkModeTheme` |
| تمهای اکتیویتی | `@style/AllPlansUpgradeScreen`، `DialogModalTheme`، `MaterialTheme.Launcher`، `Theme.Hidden`، `ProfilePicturePickerTheme`، `GistActivityTheme`، … |
| عناصر `<data>` (deep link/query) | ۴۶ |
| تنها گراف ناوبری اعلانی | `res/navigation/nav_onboarding_graph.xml` |
| منوها | `bottom_navigation_menu`، `menu_profile`، `menu_public_profile`، `menu_settings`، `crop_image_menu` |

تغییر آیکون اپ با **فعال/غیرفعال کردن alias** انجام میشود، نه عوض کردن drawable — این همان
مکانیزمی است که `ChangeAppIconActivity` با آن کار میکند.

## لایهٔ ۲ — XML View (بدنهٔ اصلی)

- **۱٬۲۹۹ فایل لایه** در ۱۰ پوشهٔ config-qualified:

| پوشه | تعداد |
|---|---|
| layout | 809 |
| layout-v33 | 319 |
| layout-v31 | 150 |
| layout-land | 11 |
| layout-sw600dp-v13 | 3 |
| layout-v26 | 2 |
| layout-watch-v20 | 2 |
| layout-ldrtl-v17 | 1 |
| layout-sw600dp-land-v13 | 1 |
| layout-w270dp-h560dp-v13 | 1 |

- ۵٬۱۴۴ گره در کل لایهها؛ ۲٬۷۷۱ `<include>`/`<ViewStub>`؛ ۷٬۵۳۶ ارجاع به منابع.
- ریشههای پرتکرار: `merge` ۳۳۰، `LinearLayout` ۲۱۰، `FrameLayout` ۱۷۷،
  `ConstraintLayout` ۹۲، `RadioGroup` ۸۸، `ImageView` ۸۱، `GridView` ۷۳، `TextView` ۴۸.
- **۵۳ ویوی سفارشی `com.getmimo.*`** مستقیماً در XML استفاده شدهاند (فهرست کامل در `05`).
- `ViewPager2` صفحات درس را نگه میدارد؛ `FragmentContainerView` زنجیرهٔ مودالهای پایان فصل را.

نمونهٔ واقعی (دیکدشده، `res/layout/chapter_activity.xml`) — همان چیزی که در APK نوشته شده:

```xml
<FrameLayout android:id="@id/chapter_activity_root" android:layout_width="match_parent" ...>
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_view" .../>
  <androidx.coordinatorlayout.widget.CoordinatorLayout ...>
    <androidx.viewpager2.widget.ViewPager2 android:id="@id/vp_lessons" .../>
    <androidx.fragment.app.FragmentContainerView android:id="@id/layout_chapter_finished_share_fragment" .../>
    <com.google.android.material.appbar.AppBarLayout android:background="@color/navbar_background" ...>
      <com.getmimo.ui.chapter.view.ChapterToolbar android:layout_height="@dimen/lesson_progress_navbar_height"/>
    </com.google.android.material.appbar.AppBarLayout>
  </androidx.coordinatorlayout.widget.CoordinatorLayout>
</FrameLayout>
```

## لایهٔ ۳ — Compose (جزیرهها، نه بازنویسی کامل)

- **۷۱ لایه** حداقل یک `androidx.compose.ui.platform.ComposeView` دارند.
- **۱۲۷ کلاس** در DEX با نشانهٔ Compose/`*Kt` شناسایی شدند
  (`SOURCE/dex/COMPOSE_INVENTORY.csv`).
- نمونهٔ شواهد: `AiTutorButton$…$pulseDiameterAnimation` / پالس دکمهٔ مربی هوشمند،
  کیبورد کدنویسی Compose بارتفاع `64dp`.
- الگو: `setContentView(R.layout.x)` → پیدا کردن `ComposeView` → `setContent { … }`.
  یعنی Compose **روی** XML سوار است، نه جایگزین آن.

## لایهٔ ۴ — WebView (رندر محتوای درس)

- **۶ لایه** حاوی `WebView`/`MimoWebView` هستند.
- کد جاوااسکریپت داخل بسته: `lesson-webview.js`، `lesson-webview-fonts.js`،
  `highlight.min.js`، `beautify/*`، `prettier/*`، `spieglein/editor.bundle.js`،
  ۲ فایل CSS تم روشن/تیره، ۲۱۵ آیکون SVG، ۱۳ فیکسچر HTML.
- جزئیات کامل پروتکل پیامرسانی در `07_LESSON_RENDERER_WEBVIEW.md`.

## لایهٔ ۵ — داراییها و حرکت

- ۱٬۳۱۹ فایل drawable/mipmap (برداری، شکل، سلکتور، PNG/WebP)، ۳۰۴ لیست حالت رنگ.
- ۱۴۳ فایل حرکت: ۷۲ `anim` + ۴۷ `animator` + ۲۴ `interpolator`.
- **59 فایل Rive `.riv`** در `res/raw` (+ ۱۵ نسخهٔ `raw-night-v8`) برای جشن پایان فصل/زنجیره.
- **12 فایل فونت** در `res/font` به علاوهٔ `Aeonik Mono` در `assets/spieglein/assets/`.

## لایهٔ ۶ — بایتکد

| گروه | تعداد |
|---|---|
| کل کلاسهای DEX (۱۲ فایل) | ۲۹٬۴۵۴ |
| کلاسهای `com.getmimo.*` | ۳٬۱۳۳ |
| کلاسهای `com.getmimo.ui.*` | ۱٬۹۲۳ |
| کلاسهای اپ واردشده در فهرست UI | ۳٬۲۵۵ |
| کلاسهایی که با `const` مستقیماً `R.layout.*` را inflate میکنند | ۱۰۹ |
| DEXهای واقعی | ۴ (`classes.dex`, `classes2.dex`, `classes3.dex`, `classes12.dex`) |
| DEXهای پوچ ۱٬۰۹۶ بایتی | ۸ (`classes4` … `classes11`) |

عدد آخر یکی از نشانههای **بستهٔ دستکاریشده** است؛ به `11` مراجعه کنید.
