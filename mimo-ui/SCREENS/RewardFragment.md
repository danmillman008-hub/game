# صفحه — `RewardFragment`

> **خاستگاه ثبت:** `DEX UI_CLASSES.json` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.reward.RewardFragment$loadUserName$1` |
| نوع | `dex-ui-class` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 6 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/reward_bottomsheet_dialog_status_1.xml`](../SOURCE/res/layout/reward_bottomsheet_dialog_status_1.xml) → [dossier](LAYOUTS/layout_reward_bottomsheet_dialog_status_1.md)
- [`res/layout/reward_bottomsheet_dialog_status_2.xml`](../SOURCE/res/layout/reward_bottomsheet_dialog_status_2.xml) → [dossier](LAYOUTS/layout_reward_bottomsheet_dialog_status_2.md)
- [`res/layout/reward_bottomsheet_fragment.xml`](../SOURCE/res/layout/reward_bottomsheet_fragment.xml) → [dossier](LAYOUTS/layout_reward_bottomsheet_fragment.md)
- [`res/layout/reward_box.xml`](../SOURCE/res/layout/reward_box.xml) → [dossier](LAYOUTS/layout_reward_box.md)
- [`res/layout/reward_fragment.xml`](../SOURCE/res/layout/reward_fragment.xml) → [dossier](LAYOUTS/layout_reward_fragment.md)
- [`res/layout/reward_tablet_dialog_fragment.xml`](../SOURCE/res/layout/reward_tablet_dialog_fragment.xml) → [dossier](LAYOUTS/layout_reward_tablet_dialog_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/reward_bottomsheet_dialog_status_1.xml`

```text
└─ TextView
```

### `res/layout/reward_bottomsheet_dialog_status_2.xml`

```text
└─ TextView
```

### `res/layout/reward_bottomsheet_fragment.xml`

```text
└─ LinearLayout
   ├─ View  #@id/view_reward_bottom_sheet_handle
   └─ FrameLayout  #@id/root_reward_bottom_sheet_fragment
```

### `res/layout/reward_box.xml`

```text
└─ FrameLayout
   ├─ com.airbnb.lottie.LottieAnimationView  #@id/lottie_reward_box
   ├─ TextView  #@id/tv_reward_box_label_main
   └─ TextView  #@id/tv_reward_box_label_light
```

### `res/layout/reward_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_reward_bottom_sheet_header
   ├─ TextView  #@id/tv_reward_bottom_sheet_description
   ├─ View  #@id/divider_reward_bottom_sheet
   ├─ TextSwitcher  #@id/tv_reward_bottom_sheet_status_line_1
   ├─ TextSwitcher  #@id/tv_reward_bottom_sheet_status_line_2
   └─ LinearLayout  #@id/layout_reward_boxes
      ├─ com.getmimo.ui.reward.RewardBox  #@id/reward_box_1
      ├─ com.getmimo.ui.reward.RewardBox  #@id/reward_box_2
      └─ com.getmimo.ui.reward.RewardBox  #@id/reward_box_3
```

### `res/layout/reward_tablet_dialog_fragment.xml`

```text
└─ FrameLayout  #@id/root_reward_tablet_dialog_fragment
   └─ androidx.cardview.widget.CardView
      └─ FrameLayout  #@id/container_reward_tablet_dialog_fragment
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
collect_reward
developer_menu_add_test_reward
developer_menu_create_test_reward
reward_choose_box
reward_drag_to_dismiss
reward_header_with_name
reward_header_without_name
reward_tap_to_open
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
