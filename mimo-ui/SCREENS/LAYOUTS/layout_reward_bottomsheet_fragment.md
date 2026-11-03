# پروندهٔ لایه — `res/layout/reward_bottomsheet_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/reward_bottomsheet_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/reward_bottomsheet_fragment.xml`](../../SOURCE/res/layout/reward_bottomsheet_fragment.xml) |
| SHA-256 دیکد | `00b047cbc140fec591031dc00b79657345699f5e65d9c1e1b404251248496242` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ View  #@id/view_reward_bottom_sheet_handle
   └─ FrameLayout  #@id/root_reward_bottom_sheet_fragment
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `LinearLayout` | `android:minHeight` | `200.000000dip` |
| 5 | `View` | `android:layout_gravity` | `0x00000011` |
| 6 | `View` | `android:id` | `@id/view_reward_bottom_sheet_handle` |
| 7 | `View` | `android:background` | `@drawable/bg_handle` |
| 8 | `View` | `android:layout_width` | `24.000000dip` |
| 9 | `View` | `android:layout_height` | `3.000000dip` |
| 10 | `View` | `android:layout_marginTop` | `2.000000dip` |
| 11 | `FrameLayout` | `android:id` | `@id/root_reward_bottom_sheet_fragment` |
| 12 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 13 | `FrameLayout` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/root_reward_bottom_sheet_fragment
@id/view_reward_bottom_sheet_handle
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.reward.RewardFragment$loadUserName$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent" android:minHeight="200.000000dip">
  <View android:layout_gravity="0x00000011" android:id="@id/view_reward_bottom_sheet_handle" android:background="@drawable/bg_handle" android:layout_width="24.000000dip" android:layout_height="3.000000dip" android:layout_marginTop="2.000000dip"/>
  <FrameLayout android:id="@id/root_reward_bottom_sheet_fragment" android:layout_width="match_parent" android:layout_height="match_parent"/>
</LinearLayout>
```
