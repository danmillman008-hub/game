# صفحه — `ReportLessonFragment`

> **خاستگاه ثبت:** `DEX UI_CLASSES.json` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.lesson.report.ReportLessonFragment$onViewCreated$1` |
| نوع | `dex-ui-class` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 1 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/report_lesson_fragment.xml`](../SOURCE/res/layout/report_lesson_fragment.xml) → [dossier](LAYOUTS/layout_report_lesson_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/report_lesson_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ FrameLayout  #@id/report_lesson_header
   │  ├─ TextView  #@id/tv_report_lesson_header
   │  └─ ImageButton  #@id/btn_report_lesson_close
   ├─ androidx.core.widget.NestedScrollView  #@id/nsv_report_content
   │  └─ androidx.constraintlayout.widget.ConstraintLayout
   │     ├─ TextView  #@id/tv_report_lesson_title
   │     └─ ViewFlipper  #@id/vf_report_lesson_view_flipper
   │        ├─ com.getmimo.ui.common.ChoiceCard  #@id/layout_report_lesson_choice_card
   │        └─ com.google.android.material.textfield.TextInputLayout
   │           └─ com.google.android.material.textfield.TextInputEditText  #@id/et_report_lesson_feedback
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_report_lesson_report
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
report_lesson_btn_report_text
report_lesson_btn_submit
report_lesson_header
report_lesson_offline_message
report_lesson_option_app_issue
report_lesson_option_content_confusing
report_lesson_option_content_typo
report_lesson_option_content_wrong
report_lesson_option_unclear_translation
report_lesson_other_hint
report_lesson_title
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

(none)

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
report_lesson_offline_message
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
