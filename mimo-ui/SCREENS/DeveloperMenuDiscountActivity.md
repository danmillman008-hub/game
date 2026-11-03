# صفحه — `DeveloperMenuDiscountActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.developermenu.discount.DeveloperMenuDiscountActivity` |
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

- [`res/layout/developer_menu_discount_activity.xml`](../SOURCE/res/layout/developer_menu_discount_activity.xml) → [dossier](LAYOUTS/layout_developer_menu_discount_activity.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/developer_menu_discount_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_discount_config
   │  └─ include  #@id/layout_toolbar
   └─ ScrollView  #@id/sv_developermenu_discount
      └─ LinearLayout
         ├─ TextView  #@id/tv_smart_discount_chapter_completed
         ├─ TextView  #@id/tv_smart_discount
         ├─ TextView  #@id/tv_discount_theme
         ├─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_override_subscription_reactivate_discount
         ├─ TextView  #@id/tv_external_subscription
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_fake_remote_discount
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_fake_remote_discount_image
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_force_last_call_discount
         ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_smart_discount
         └─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_smart_discount_send_push_notification
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
developer_menu_discount
developer_menu_discount_chapter_completed
developer_menu_discount_current_discount
developer_menu_discount_current_subscription
developer_menu_discount_fake_remote_discount
developer_menu_discount_fake_remote_discount_image
developer_menu_discount_force_last_call_discount
developer_menu_discount_local_discount_theme
developer_menu_discount_override_subscription
developer_menu_discount_reset_local_discount
developer_menu_discount_send_push_notification
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
