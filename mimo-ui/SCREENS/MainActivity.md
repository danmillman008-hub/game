# صفحه — `MainActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.main.MainActivity` |
| نوع | `activity` |
| exported (manifest) | `true` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme.NoAnim` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/main_activity_content.xml`](../SOURCE/res/layout/main_activity_content.xml) → [dossier](LAYOUTS/layout_main_activity_content.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/main_activity_content.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/main_activity_root
   ├─ FrameLayout  #@id/contentFrame
   └─ FrameLayout  #@id/container_bottombar
      └─ com.getmimo.ui.navigation.NavigationBar  #@id/navigation_bar
```

## ۳. رشته‌های مرتبط (فهرست کامل)

(none)

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
m3_back_progress_main_container_max_translation_y
m3_back_progress_main_container_min_edge_gap
notification_main_column_padding_top
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

(none)

## ۸. ناوبری / deep link

```json
[
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/profile"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:pathPattern": "/learn/.*"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/learn"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:pathPattern": "/explore/.*"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/deeplink/practicetab"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:pathPattern": "/leaderboard/.*"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:pathPattern": "/invite/.*"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/leaderboard"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:pathPattern": "/allplans"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:pathPattern": "/upgradeapp"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:path": "/deeplink/upgradepaywall"
  },
  {
    "android:scheme": "https",
    "android:host": "getmimo.com",
    "android:pathPattern": "/deeplink/upgradepaywall/.*"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/profile"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:pathPattern": "/learn/.*"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/learn"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:pathPattern": "/explore/.*"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/deeplink/practicetab"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:pathPattern": "/leaderboard/.*"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:pathPattern": "/invite/.*"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/leaderboard"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:pathPattern": "/allplans"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:pathPattern": "/upgradeapp"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:path": "/deeplink/upgradepaywall"
  },
  {
    "android:scheme": "mimo",
    "android:host": "getmimo.com",
    "android:pathPattern": "/deeplink/upgradepaywall/.*"
  }
]
```
