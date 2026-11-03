# صفحه — `DeveloperMenuCampaignActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.developermenu.campaign.DeveloperMenuCampaignActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/developer_menu_campaign_activity.xml`](../SOURCE/res/layout/developer_menu_campaign_activity.xml) → [dossier](LAYOUTS/layout_developer_menu_campaign_activity.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/developer_menu_campaign_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_abtest__config
   │  └─ include  #@id/layout_toolbar
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_dev_menu_campaign
         ├─ TextView  #@id/tv_dev_menu_campaign_parameter
         ├─ TextView  #@id/tv_dev_menu_campaign_value
         ├─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_dev_menu_campaign
         ├─ TextView  #@id/tv_dev_menu_campaign_allows_free_trial
         ├─ TextView  #@id/tv_dev_menu_campaign_allows_free_trial_value
         └─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_dev_menu_campaign_allows_free_trial
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
developer_menu_campaign
developer_menu_campaign_allows_free_trial
developer_menu_campaign_parameter
developer_menu_campaign_user_coming_from_campaign
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

(none)

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

(none)

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
