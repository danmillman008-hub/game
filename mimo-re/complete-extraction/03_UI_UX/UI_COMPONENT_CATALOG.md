# ۰۳ب — کاتالوگ کامپوننت‌های رابط

**پایه:** ۸۷ کلاس bottom sheet، ۴۴ دیالوگ، ۲۲ `ModalData`، ۱۹ کلاس ویجت، ۸۰۹ layout.
هر ردیف یا کلاس واقعی است یا الگوی تکرارشونده‌ای که از ترکیب کلاس+رشته استخراج شده.

| کامپوننت | شناسه | رفتار | شاهد |
|---|---|---|---|
| کارت مسیر | path card | پیشرفت + CTA «ادامه» | `continue_learning` |
| نوار پیشرفت درس | `lesson_progressbar_height 8dp` | خط باریک بالای درس | dimens |
| تراشهٔ زنجیره | `ArcProgressView` | کمان پیشرفت روز | کلاس + dimens |
| حلقهٔ هدف روزانه | `DailySparksGoalProgressView` | XP روز، متن ۴۲sp | dimens کلیددار |
| کیبورد کدنویسی | `CodingKeyboardKt` | ۶۴dp، دکمهٔ AI با پالس | Compose + dimen |
| تب فایل کد | `codeeditor_tab_color` | تب هر فایل درس | رنگ اختصاصی |
| کنسول | `InputConsole*` | خروجی/خطا | رشته‌های `input_console_*` |
| کارت تست | `Condition %d` | یک ردیف به‌ازای هر تست | رشته |
| باتم‌شیت جایزه | `RewardSheet` | کشیدن برای بستن | `reward_drag_to_dismiss` |
| شیت چالش زنجیره | — | پذیرش شرط با هزینه | `streak_challenge_prompt_accept` |
| دراور تخفیف | `RemoteConfigDiscount` | شمارش معکوس + CTA + رد کردن | `in_app_offer_countdown` |
| دیالوگ «دیدن راه‌حل» | `see_solution_confirm_dialog_*` | تأیید جایگزینی کد | ۷ رشته |
| فلش‌بار | `flashbar_*` dimens | پیام شناور | ۷ رشته/دایمن |
| کارت گواهی | `certificate_*` | پیشرفت تا گواهی | ۵۰ رشته |
| ویجت زنجیره | `MimoStreakWidget` | ۴ اندازه | Glance + `widget_*` |

## الگوهای تکرارشونده (قابل استفادهٔ مستقیم در محصول جدید)

1. **Offline view با دکمهٔ «تازه‌سازی»** برای هر سطح شبکه‌ای (۱۲ سطح).
2. **حالت خالی با CTA** (نه پیام خالی).
3. **Modal-first flow** در پایان فصل (جایزه → چالش → ارتقا → اعلان).
4. **دو لایه بازخورد**: متن کوتاه درجا + بلوک توضیحی `visible-if="wrong"`.
5. **پیام‌های چرخشی تشویق** (۶ نسخه) برای جلوگیری از تکرار مکانیکی.
