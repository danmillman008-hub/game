# پروندهٔ لایه — `res/layout/mtrl_alert_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_alert_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_alert_dialog.xml`](../../SOURCE/res/layout/mtrl_alert_dialog.xml) |
| SHA-256 دیکد | `52cdab8002b55a8d05f88922c14a612d116d490bc63a73080184032924ed4ac2` |
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
   │  ├─ View  #@id/scrollIndicatorUp
   │  ├─ androidx.core.widget.NestedScrollView  #@id/scrollView
   │  │  └─ LinearLayout
   │  │     ├─ android.widget.Space  #@id/textSpacerNoTitle
   │  │     ├─ TextView  #@0x0102000B
   │  │     └─ android.widget.Space  #@id/textSpacerNoButtons
   │  └─ View  #@id/scrollIndicatorDown
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
| 6 | `include` | `layout` | `@layout/mtrl_alert_dialog_title` |
| 7 | `FrameLayout` | `android:id` | `@id/contentPanel` |
| 8 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 9 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 10 | `FrameLayout` | `android:minHeight` | `48.000000dip` |
| 11 | `View` | `android:layout_gravity` | `0x00000030` |
| 12 | `View` | `android:id` | `@id/scrollIndicatorUp` |
| 13 | `View` | `android:background` | `?attr/colorControlHighlight` |
| 14 | `View` | `android:visibility` | `gone` |
| 15 | `View` | `android:layout_width` | `match_parent` |
| 16 | `View` | `android:layout_height` | `1.000000dip` |
| 17 | `androidx.core.widget.NestedScrollView` | `android:id` | `@id/scrollView` |
| 18 | `androidx.core.widget.NestedScrollView` | `android:clipToPadding` | `false` |
| 19 | `androidx.core.widget.NestedScrollView` | `android:layout_width` | `match_parent` |
| 20 | `androidx.core.widget.NestedScrollView` | `android:layout_height` | `wrap_content` |
| 21 | `LinearLayout` | `android:orientation` | `vertical` |
| 22 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 23 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 24 | `android.widget.Space` | `android:id` | `@id/textSpacerNoTitle` |
| 25 | `android.widget.Space` | `android:visibility` | `gone` |
| 26 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 27 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_padding_top_material` |
| 28 | `TextView` | `android:id` | `@0x0102000B` |
| 29 | `TextView` | `android:paddingLeft` | `?attr/dialogPreferredPadding` |
| 30 | `TextView` | `android:paddingRight` | `?attr/dialogPreferredPadding` |
| 31 | `TextView` | `android:layout_width` | `match_parent` |
| 32 | `TextView` | `android:layout_height` | `wrap_content` |
| 33 | `TextView` | `style` | `?attr/materialAlertDialogBodyTextStyle` |
| 34 | `android.widget.Space` | `android:id` | `@id/textSpacerNoButtons` |
| 35 | `android.widget.Space` | `android:visibility` | `gone` |
| 36 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 37 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_padding_top_material` |
| 38 | `View` | `android:layout_gravity` | `0x00000050` |
| 39 | `View` | `android:id` | `@id/scrollIndicatorDown` |
| 40 | `View` | `android:background` | `?attr/colorControlHighlight` |
| 41 | `View` | `android:visibility` | `gone` |
| 42 | `View` | `android:layout_width` | `match_parent` |
| 43 | `View` | `android:layout_height` | `1.000000dip` |
| 44 | `FrameLayout` | `android:id` | `@id/customPanel` |
| 45 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 46 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 47 | `FrameLayout` | `android:minHeight` | `48.000000dip` |
| 48 | `FrameLayout` | `android:id` | `@id/custom` |
| 49 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 50 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 51 | `include` | `android:layout_width` | `match_parent` |
| 52 | `include` | `android:layout_height` | `wrap_content` |
| 53 | `include` | `layout` | `@layout/mtrl_alert_dialog_actions` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/abc_dialog_padding_top_material` | `18.000000dip` |

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
@layout/mtrl_alert_dialog_actions
@layout/mtrl_alert_dialog_title
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
<androidx.appcompat.widget.AlertDialogLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00800033" android:orientation="vertical" android:id="@id/parentPanel" android:layout_width="match_parent" android:layout_height="wrap_content">
  <include layout="@layout/mtrl_alert_dialog_title"/>
  <FrameLayout android:id="@id/contentPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip">
    <View android:layout_gravity="0x00000030" android:id="@id/scrollIndicatorUp" android:background="?attr/colorControlHighlight" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip"/>
    <androidx.core.widget.NestedScrollView android:id="@id/scrollView" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content">
      <LinearLayout android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
        <android.widget.Space android:id="@id/textSpacerNoTitle" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_padding_top_material"/>
        <TextView android:id="@0x0102000B" android:paddingLeft="?attr/dialogPreferredPadding" android:paddingRight="?attr/dialogPreferredPadding" android:layout_width="match_parent" android:layout_height="wrap_content" style="?attr/materialAlertDialogBodyTextStyle"/>
        <android.widget.Space android:id="@id/textSpacerNoButtons" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_padding_top_material"/>
      </LinearLayout>
    </androidx.core.widget.NestedScrollView>
    <View android:layout_gravity="0x00000050" android:id="@id/scrollIndicatorDown" android:background="?attr/colorControlHighlight" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip"/>
  </FrameLayout>
  <FrameLayout android:id="@id/customPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip">
    <FrameLayout android:id="@id/custom" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  </FrameLayout>
  <include android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/mtrl_alert_dialog_actions"/>
</androidx.appcompat.widget.AlertDialogLayout>
```
