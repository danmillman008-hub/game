# پروندهٔ لایه — `res/layout/abc_activity_chooser_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_activity_chooser_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_activity_chooser_view.xml`](../../SOURCE/res/layout/abc_activity_chooser_view.xml) |
| SHA-256 دیکد | `df6dee5f1ea2a095e2bd59a137bd848fc972edc46083355ffff631a7b389ba9e` |
| ریشه | `view` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ view  #@id/activity_chooser_view_content
   ├─ FrameLayout  #@id/expand_activities_button
   │  └─ ImageView  #@id/image
   └─ FrameLayout  #@id/default_activity_button
      └─ ImageView  #@id/image
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `view` | `android:layout_gravity` | `0x00000011` |
| 2 | `view` | `android:id` | `@id/activity_chooser_view_content` |
| 3 | `view` | `android:layout_width` | `wrap_content` |
| 4 | `view` | `android:layout_height` | `match_parent` |
| 5 | `view` | `class` | `androidx.appcompat.widget.ActivityChooserView$InnerLayout` |
| 6 | `view` | `style` | `?attr/activityChooserViewStyle` |
| 7 | `FrameLayout` | `android:layout_gravity` | `0x00000011` |
| 8 | `FrameLayout` | `android:id` | `@id/expand_activities_button` |
| 9 | `FrameLayout` | `android:background` | `?attr/actionBarItemBackground` |
| 10 | `FrameLayout` | `android:paddingLeft` | `12.000000dip` |
| 11 | `FrameLayout` | `android:paddingTop` | `2.000000dip` |
| 12 | `FrameLayout` | `android:paddingRight` | `12.000000dip` |
| 13 | `FrameLayout` | `android:paddingBottom` | `2.000000dip` |
| 14 | `FrameLayout` | `android:focusable` | `true` |
| 15 | `FrameLayout` | `android:addStatesFromChildren` | `true` |
| 16 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 17 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 18 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 19 | `ImageView` | `android:id` | `@id/image` |
| 20 | `ImageView` | `android:layout_width` | `32.000000dip` |
| 21 | `ImageView` | `android:layout_height` | `32.000000dip` |
| 22 | `ImageView` | `android:scaleType` | `fitCenter` |
| 23 | `ImageView` | `android:adjustViewBounds` | `true` |
| 24 | `FrameLayout` | `android:layout_gravity` | `0x00000011` |
| 25 | `FrameLayout` | `android:id` | `@id/default_activity_button` |
| 26 | `FrameLayout` | `android:background` | `?attr/actionBarItemBackground` |
| 27 | `FrameLayout` | `android:paddingLeft` | `12.000000dip` |
| 28 | `FrameLayout` | `android:paddingTop` | `2.000000dip` |
| 29 | `FrameLayout` | `android:paddingRight` | `12.000000dip` |
| 30 | `FrameLayout` | `android:paddingBottom` | `2.000000dip` |
| 31 | `FrameLayout` | `android:focusable` | `true` |
| 32 | `FrameLayout` | `android:addStatesFromChildren` | `true` |
| 33 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 34 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 35 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 36 | `ImageView` | `android:id` | `@id/image` |
| 37 | `ImageView` | `android:layout_width` | `32.000000dip` |
| 38 | `ImageView` | `android:layout_height` | `32.000000dip` |
| 39 | `ImageView` | `android:scaleType` | `fitCenter` |
| 40 | `ImageView` | `android:adjustViewBounds` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/activity_chooser_view_content
@id/default_activity_button
@id/expand_activities_button
@id/image
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<view xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:id="@id/activity_chooser_view_content" android:layout_width="wrap_content" android:layout_height="match_parent" class="androidx.appcompat.widget.ActivityChooserView$InnerLayout" style="?attr/activityChooserViewStyle">
  <FrameLayout android:layout_gravity="0x00000011" android:id="@id/expand_activities_button" android:background="?attr/actionBarItemBackground" android:paddingLeft="12.000000dip" android:paddingTop="2.000000dip" android:paddingRight="12.000000dip" android:paddingBottom="2.000000dip" android:focusable="true" android:addStatesFromChildren="true" android:layout_width="wrap_content" android:layout_height="match_parent">
    <ImageView android:layout_gravity="0x00000011" android:id="@id/image" android:layout_width="32.000000dip" android:layout_height="32.000000dip" android:scaleType="fitCenter" android:adjustViewBounds="true"/>
  </FrameLayout>
  <FrameLayout android:layout_gravity="0x00000011" android:id="@id/default_activity_button" android:background="?attr/actionBarItemBackground" android:paddingLeft="12.000000dip" android:paddingTop="2.000000dip" android:paddingRight="12.000000dip" android:paddingBottom="2.000000dip" android:focusable="true" android:addStatesFromChildren="true" android:layout_width="wrap_content" android:layout_height="match_parent">
    <ImageView android:layout_gravity="0x00000011" android:id="@id/image" android:layout_width="32.000000dip" android:layout_height="32.000000dip" android:scaleType="fitCenter" android:adjustViewBounds="true"/>
  </FrameLayout>
</view>
```
