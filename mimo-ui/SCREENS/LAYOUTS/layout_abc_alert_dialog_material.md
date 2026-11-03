# پروندهٔ لایه — `res/layout/abc_alert_dialog_material.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_alert_dialog_material.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_alert_dialog_material.xml`](../../SOURCE/res/layout/abc_alert_dialog_material.xml) |
| SHA-256 دیکد | `4e07e9c2ab9431e2bdab5e7f6ae65cfd64010914dd9580eff322fddf429ddb50` |
| ریشه | `androidx.appcompat.widget.AlertDialogLayout` |
| تعداد گره | 13 |
| تعداد شناسه | 10 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 16 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.appcompat.widget.AlertDialogLayout  #@id/parentPanel
   ├─ include
   ├─ FrameLayout  #@id/contentPanel
   │  ├─ ImageView  #@id/scrollIndicatorUp
   │  ├─ androidx.core.widget.NestedScrollView  #@id/scrollView
   │  │  └─ LinearLayout
   │  │     ├─ android.widget.Space  #@id/textSpacerNoTitle
   │  │     ├─ TextView  #@0x0102000B
   │  │     └─ android.widget.Space  #@id/textSpacerNoButtons
   │  └─ ImageView  #@id/scrollIndicatorDown
   ├─ FrameLayout  #@id/customPanel
   │  └─ FrameLayout  #@id/custom
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.widget.AlertDialogLayout` | `android:gravity` | `0x00800033` |
| 2 | `androidx.appcompat.widget.AlertDialogLayout` | `android:orientation` | `vertical` |
| 3 | `androidx.appcompat.widget.AlertDialogLayout` | `android:id` | `@id/parentPanel` |
| 4 | `androidx.appcompat.widget.AlertDialogLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.appcompat.widget.AlertDialogLayout` | `android:layout_height` | `wrap_content` |
| 6 | `include` | `layout` | `@layout/abc_alert_dialog_title_material` |
| 7 | `FrameLayout` | `android:id` | `@id/contentPanel` |
| 8 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 9 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 10 | `FrameLayout` | `android:minHeight` | `48.000000dip` |
| 11 | `ImageView` | `android:layout_gravity` | `0x00000030` |
| 12 | `ImageView` | `android:id` | `@id/scrollIndicatorUp` |
| 13 | `ImageView` | `android:background` | `#1F000000` |
| 14 | `ImageView` | `android:visibility` | `gone` |
| 15 | `ImageView` | `android:layout_width` | `match_parent` |
| 16 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 17 | `ImageView` | `app:backgroundTint` | `?0x01010030` |
| 18 | `androidx.core.widget.NestedScrollView` | `android:id` | `@id/scrollView` |
| 19 | `androidx.core.widget.NestedScrollView` | `android:clipToPadding` | `false` |
| 20 | `androidx.core.widget.NestedScrollView` | `android:layout_width` | `match_parent` |
| 21 | `androidx.core.widget.NestedScrollView` | `android:layout_height` | `wrap_content` |
| 22 | `LinearLayout` | `android:orientation` | `vertical` |
| 23 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 24 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 25 | `android.widget.Space` | `android:id` | `@id/textSpacerNoTitle` |
| 26 | `android.widget.Space` | `android:visibility` | `gone` |
| 27 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 28 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_padding_top_material` |
| 29 | `TextView` | `android:id` | `@0x0102000B` |
| 30 | `TextView` | `android:paddingLeft` | `?attr/dialogPreferredPadding` |
| 31 | `TextView` | `android:paddingRight` | `?attr/dialogPreferredPadding` |
| 32 | `TextView` | `android:layout_width` | `match_parent` |
| 33 | `TextView` | `android:layout_height` | `wrap_content` |
| 34 | `TextView` | `style` | `@style/TextAppearance.AppCompat.Subhead` |
| 35 | `android.widget.Space` | `android:id` | `@id/textSpacerNoButtons` |
| 36 | `android.widget.Space` | `android:visibility` | `gone` |
| 37 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 38 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_padding_top_material` |
| 39 | `ImageView` | `android:layout_gravity` | `0x00000050` |
| 40 | `ImageView` | `android:id` | `@id/scrollIndicatorDown` |
| 41 | `ImageView` | `android:background` | `#1F000000` |
| 42 | `ImageView` | `android:visibility` | `gone` |
| 43 | `ImageView` | `android:layout_width` | `match_parent` |
| 44 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 45 | `ImageView` | `app:backgroundTint` | `?0x01010030` |
| 46 | `FrameLayout` | `android:id` | `@id/customPanel` |
| 47 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 48 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 49 | `FrameLayout` | `android:minHeight` | `48.000000dip` |
| 50 | `FrameLayout` | `android:id` | `@id/custom` |
| 51 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 52 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 53 | `include` | `android:layout_width` | `match_parent` |
| 54 | `include` | `android:layout_height` | `wrap_content` |
| 55 | `include` | `layout` | `@layout/abc_alert_dialog_button_bar_material` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/abc_dialog_padding_top_material` | `18.000000dip` |
| `@style/TextAppearance.AppCompat.Subhead` | `[]` |

## ۴. شناسه‌های `@id`

```text
@0x0102000B
@id/contentPanel
@id/custom
@id/customPanel
@id/parentPanel
@id/scrollIndicatorDown
@id/scrollIndicatorUp
@id/scrollView
@id/textSpacerNoButtons
@id/textSpacerNoTitle
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/abc_alert_dialog_button_bar_material
@layout/abc_alert_dialog_title_material
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.appcompat.widget.AlertDialogLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00800033" android:orientation="vertical" android:id="@id/parentPanel" android:layout_width="match_parent" android:layout_height="wrap_content">
  <include layout="@layout/abc_alert_dialog_title_material"/>
  <FrameLayout android:id="@id/contentPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip">
    <ImageView android:layout_gravity="0x00000030" android:id="@id/scrollIndicatorUp" android:background="#1F000000" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip" app:backgroundTint="?0x01010030"/>
    <androidx.core.widget.NestedScrollView android:id="@id/scrollView" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content">
      <LinearLayout android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
        <android.widget.Space android:id="@id/textSpacerNoTitle" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_padding_top_material"/>
        <TextView android:id="@0x0102000B" android:paddingLeft="?attr/dialogPreferredPadding" android:paddingRight="?attr/dialogPreferredPadding" android:layout_width="match_parent" android:layout_height="wrap_content" style="@style/TextAppearance.AppCompat.Subhead"/>
        <android.widget.Space android:id="@id/textSpacerNoButtons" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_padding_top_material"/>
      </LinearLayout>
    </androidx.core.widget.NestedScrollView>
    <ImageView android:layout_gravity="0x00000050" android:id="@id/scrollIndicatorDown" android:background="#1F000000" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip" app:backgroundTint="?0x01010030"/>
  </FrameLayout>
  <FrameLayout android:id="@id/customPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip">
    <FrameLayout android:id="@id/custom" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  </FrameLayout>
  <include android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/abc_alert_dialog_button_bar_material"/>
</androidx.appcompat.widget.AlertDialogLayout>
```
