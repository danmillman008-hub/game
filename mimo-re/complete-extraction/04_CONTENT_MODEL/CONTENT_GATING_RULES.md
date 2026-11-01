# ۰۴ج — قواعد بازکردن/قفل محتوا

**کلاس شواهد:** PARTIALLY_VERIFIED — قواعد از رشته‌ها و قراردادهای مدل استخراج شده؛
منطق دقیق قفل در سرور است و در بستهٔ نصب نیست.

| دروازه | شاهد | رفتار کاربر | محل تصمیم |
|---|---|---|---|
| کلید (Keys) | `keys_left_today = %d keys left today`, `keys_left_today_subtitle = "Use keys to unlock lessons"`, `/v1/user/keys`, `/v1/user/keys/consume` | درس با مصرف کلید باز می‌شود | سرور (کسر کلید یک POST مستقل است) |
| Pro/MAX | `keys_unlimited_keys_pro_subtitle`, `keys_unlimited_keys_max_subtitle`, `track_content_upgrade_pro_*` | محتوا/امکانات بیشتر | RevenueCat + سرور |
| تمرین هوشمند | `SmartPracticeChargedModal`, `SmartPracticeMasteredModal` | تمرین پیشرفته پولی | سرور (INFERRED) |
| مربی هوشمند | `feature_flag_ai_tutor_android`, ۵ پرسش رایگان | ۵ پیام، سپس ارتقا | سرور (شمارنده) |
| زنجیره/چالش | `streak_challenge_prompt_accept = "Accept for %d"` | شرط با هزینه | سرور |
| گواهی | `certificate_upselling_get_your_certificate_now` | گواهی در درصد مشخص | سرور |
| ترتیب آموزش لازم | `practiceRequired` (۱۵۷ آموزش) | تمرین اجباری | **UNKNOWN** (منطق در سرور/کلاینت مبهم) |

**قاعدهٔ استخراج‌شده (INFERRED، شاهد رشته‌ای):** کلید دروازهٔ *درس* است، نه *محتوا*؛
و بازتولید روزانه دارد (`keys_zero_subtitle = "New keys arrive tomorrow"`).
برای کنکور توصیه می‌شود دروازهٔ کلید روی «آزمون شبیه‌سازی» و «تحلیل عمیق» باشد، نه سؤالات سیلابس.
