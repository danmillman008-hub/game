# پروندهٔ لایه — `res/layout/m3_alert_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/m3_alert_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/m3_alert_dialog.xml`](../../SOURCE/res/layout/m3_alert_dialog.xml) |
| SHA-256 دیکد | `7148acedf31e236054bbd6f96378732b1ccc7c930887902f41ab48e4d182d646` |
| ریشه | `androidx.appcompat.widget.AlertDialogLayout` |
| تعداد گره | 13 |
| تعداد شناسه | 10 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 17 |

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
| 4 | `androidx.appcompat.widget.AlertDialogLayout` | `android:clipChildren` | `true` |
| 5 | `androidx.appcompat.widget.AlertDialogLayout` | `android:layout_width` | `match_parent` |
| 6 | `androidx.appcompat.widget.AlertDialogLayout` | `android:layout_height` | `wrap_content` |
| 7 | `include` | `layout` | `@layout/m3_alert_dialog_title` |
| 8 | `FrameLayout` | `android:id` | `@id/contentPanel` |
| 9 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 10 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 11 | `FrameLayout` | `android:minHeight` | `48.000000dip` |
| 12 | `ImageView` | `android:layout_gravity` | `0x00000030` |
| 13 | `ImageView` | `android:id` | `@id/scrollIndicatorUp` |
| 14 | `ImageView` | `android:background` | `#1F000000` |
| 15 | `ImageView` | `android:visibility` | `gone` |
| 16 | `ImageView` | `android:layout_width` | `match_parent` |
| 17 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 18 | `ImageView` | `android:contentDescription` | `@null` |
| 19 | `ImageView` | `app:backgroundTint` | `?0x01010030` |
| 20 | `androidx.core.widget.NestedScrollView` | `android:id` | `@id/scrollView` |
| 21 | `androidx.core.widget.NestedScrollView` | `android:clipToPadding` | `false` |
| 22 | `androidx.core.widget.NestedScrollView` | `android:layout_width` | `match_parent` |
| 23 | `androidx.core.widget.NestedScrollView` | `android:layout_height` | `wrap_content` |
| 24 | `LinearLayout` | `android:orientation` | `vertical` |
| 25 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 26 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 27 | `android.widget.Space` | `android:id` | `@id/textSpacerNoTitle` |
| 28 | `android.widget.Space` | `android:visibility` | `gone` |
| 29 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 30 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_padding_top_material` |
| 31 | `TextView` | `android:id` | `@0x0102000B` |
| 32 | `TextView` | `android:paddingLeft` | `?attr/dialogPreferredPadding` |
| 33 | `TextView` | `android:paddingRight` | `?attr/dialogPreferredPadding` |
| 34 | `TextView` | `android:layout_width` | `match_parent` |
| 35 | `TextView` | `android:layout_height` | `wrap_content` |
| 36 | `TextView` | `style` | `?attr/materialAlertDialogBodyTextStyle` |
| 37 | `android.widget.Space` | `android:id` | `@id/textSpacerNoButtons` |
| 38 | `android.widget.Space` | `android:visibility` | `gone` |
| 39 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 40 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_padding_top_material` |
| 41 | `ImageView` | `android:layout_gravity` | `0x00000050` |
| 42 | `ImageView` | `android:id` | `@id/scrollIndicatorDown` |
| 43 | `ImageView` | `android:background` | `#1F000000` |
| 44 | `ImageView` | `android:visibility` | `gone` |
| 45 | `ImageView` | `android:layout_width` | `match_parent` |
| 46 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 47 | `ImageView` | `android:contentDescription` | `@null` |
| 48 | `ImageView` | `app:backgroundTint` | `?0x01010030` |
| 49 | `FrameLayout` | `android:id` | `@id/customPanel` |
| 50 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 51 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 52 | `FrameLayout` | `android:minHeight` | `48.000000dip` |
| 53 | `FrameLayout` | `android:id` | `@id/custom` |
| 54 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 55 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 56 | `include` | `android:layout_width` | `match_parent` |
| 57 | `include` | `android:layout_height` | `wrap_content` |
| 58 | `include` | `layout` | `@layout/m3_alert_dialog_actions` |

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
@layout/m3_alert_dialog_actions
@layout/m3_alert_dialog_title
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
<androidx.appcompat.widget.AlertDialogLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00800033" android:orientation="vertical" android:id="@id/parentPanel" android:clipChildren="true" android:layout_width="match_parent" android:layout_height="wrap_content">
  <include layout="@layout/m3_alert_dialog_title"/>
  <FrameLayout android:id="@id/contentPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip">
    <ImageView android:layout_gravity="0x00000030" android:id="@id/scrollIndicatorUp" android:background="#1F000000" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip" android:contentDescription="@null" app:backgroundTint="?0x01010030"/>
    <androidx.core.widget.NestedScrollView android:id="@id/scrollView" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content">
      <LinearLayout android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
        <android.widget.Space android:id="@id/textSpacerNoTitle" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_padding_top_material"/>
        <TextView android:id="@0x0102000B" android:paddingLeft="?attr/dialogPreferredPadding" android:paddingRight="?attr/dialogPreferredPadding" android:layout_width="match_parent" android:layout_height="wrap_content" style="?attr/materialAlertDialogBodyTextStyle"/>
        <android.widget.Space android:id="@id/textSpacerNoButtons" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_padding_top_material"/>
      </LinearLayout>
    </androidx.core.widget.NestedScrollView>
    <ImageView android:layout_gravity="0x00000050" android:id="@id/scrollIndicatorDown" android:background="#1F000000" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip" android:contentDescription="@null" app:backgroundTint="?0x01010030"/>
  </FrameLayout>
  <FrameLayout android:id="@id/customPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip">
    <FrameLayout android:id="@id/custom" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  </FrameLayout>
  <include android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/m3_alert_dialog_actions"/>
</androidx.appcompat.widget.AlertDialogLayout>
```
