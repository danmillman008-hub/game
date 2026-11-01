# ۰۸ب — قرارداد ابزار/عملکرد مربی

## ۱. آنچه مربی می‌تواند بکند (VERIFIED_STATIC)

| عمل | شاهد | توضیح |
|---|---|---|
| شروع گفتگو | `/v1/aiTutor/conversations` (POST، اطمینان MEDIUM) | بدنه: `StartConversation{systemMessage, userMessage}` |
| ادامهٔ گفتگو | `/v1/aiTutor/conversations/` | شناسه در مسیر (الگو نامعلوم) — **UNKNOWN** |
| پیام فوری | `UserMessage$InstantPrompt$*` | بدون تایپ، یک کلیک |
| ارجاع به ارتقا | `ShowUpgradeDialogType$AiTutor`, `UpgradeSource$AiTutor` | پس از سهمیه |

## ۲. آنچه مربی **نمی‌تواند** بکند (مهم)

| عمل | وضعیت | شاهد |
|---|---|---|
| خواندن پایگاه دادهٔ درس | ❌ | هیچ tool-call در بسته نیست |
| اجرای کد | ❌ | اجرا مسیر جدا (`/v1/code/runfiles`) |
| نوشتن در پیشرفت | ❌ | پیشرفت فقط از رویداد درس |
| دسترسی به سؤال بعدی/کلید | ❌ | — |
| رفتار stateful سمت کلاینت | ❌ | گفتگو سمت سرور |

⇒ Mimo یک **chat ساده** دارد، نه agent. برای محصول هدف، افزودن «ابزار» (مثلاً
`get_concept_prerequisite`, `log_misconception`) یک **قابلیت جدید** است، نه بازتولید.

## ۳. قرارداد پاسخ

```json
{ "conversationId": "…", "content": "…", "finishReason": "Stop|Length" }
```
* `content` متن آزاد (احتمالاً Markdown سبک؛ R6 قطعه‌کد را مجاز می‌کند).
* جریان (streaming): **UNKNOWN** — کلاس stream در بسته دیده نشد؛ احتمال زیاد پاسخ کامل است.
  رشته `ai_tutor_*` حالت «loading» دارد ⇒ انتظار پاسخ کامل (INFERRED).

## ۴. ابزارهای پیشنهادی برای محصول هدف

| ابزار | ورودی | خروجی | چرا |
|---|---|---|---|
| `explain_misconception` | `errorCode`, `questionId` | توضیح هدفمند | Mimo ندارد |
| `next_hint` | `questionId`, `attempt` | راهنمای پله‌ای | Mimo فقط دکمه دارد |
| `prerequisites` | `conceptId` | فهرست پیش‌نیاز | برای کنکور ضروری |
| `similar_questions` | `conceptId`, `difficulty` | ۳ سؤال | — |

## ۵. محدودیت‌های امنیتی

* پرامپت سیستمی باید در سرور نگه داشته شود (در Mimo در کلاینت است ⇒ قابل استخراج و
  همین‌طور شد).
* پاسخ مدل باید پالایش شود: بدون HTML اجرایی، بدون لینک خارجی، سقف طول.
