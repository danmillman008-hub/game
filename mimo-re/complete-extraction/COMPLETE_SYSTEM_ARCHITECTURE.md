# معماری کامل سیستم — Mimo 9.35 (بازسازی‌شده از شواهد)

منبع دیاگرام قابل ویرایش: `COMPLETE_SYSTEM_ARCHITECTURE.mmd` (Mermaid).
هر جعبه با یک ردیف شاهد در `MASTER_EVIDENCE_DATABASE.csv` پشتیبانی می‌شود.

## ۱. نمای کلی

```
[Android client] ⇄ [HTTP v1 API] ⇄ [Mimo backend] ⇄ [third-party]
        │                                  │
   assets content                   mastery / practice / exam
   Room outbox                      (not observable)
```

## ۲. لایهٔ کلاینت

| لایه | فناوری | اندازه | شاهد |
|---|---|---|---|
| UI | XML View + Compose (جزئی) | ۸۰۹ layout + ۵۹ `layout-v33` | `02_ANDROID_RESOURCES/` |
| ناوبری | Activity/Fragment (imperative) | ۶۱ activity، ۱ graph | `03_UI_UX/NAVIGATION_MAP.md` |
| حالت | MVI/Orbit + interactor | `ChapterViewModel` (۳۲ یال) | `01_STATIC_CODE/CALL_GRAPH/` |
| محتوا | JSON در assets | ۱۰,۳۰۴ فایل | `04_CONTENT_MODEL/` |
| درس | DSL + پارسر/رندرر | ۲۷ تگ، ۲۰,۳۰۶ سند | `05_LESSON_DSL/` |
| تصحیح | محلی (تعاملی) + سرور (کدی) | ۴ مکانیزم | `06_EXECUTION_ENGINE/` |
| پایداری | Room (۳ جدول) + DataStore | outbox | `11_DATABASE_PERSISTENCE/` |
| شبکه | Retrofit مبهم‌شده | ۶۲ مسیر | `10_BACKEND_API/` |
| تحلیل | Facade + ۳۰۵ کلاس property | → Segment/Mixpanel/Adjust | `14_ANALYTICS_NOTIFICATIONS/` |
| پرداخت | RevenueCat | ۲,۴۳۶ کلاس | `12_SUBSCRIPTIONS/` |
| مربی | ساخت پرامپت در کلاینت | ۲ حالت | `08_AI_TUTOR/` |

## ۳. جریان‌های کلیدی

### جریان یادگیری
```
Splash → (auth) → Onboarding(12) → Main → Track → Section → Tutorial → Chapter
   → Lesson(DSL parse) → interact → check(local) → feedback(visible-if)
   → progress(Room, in_queue) → outbox flush → /v1/tutorials/{id}/progress
   → chapter end → Reward → Streak challenge → Upgrade drawer → next
```

### جریان تصحیح کد
```
Lesson(executable) → files + solvedContent → /v1/code/runfiles → verdict → console UI
```

### جریان مربی
```
Lesson context + user message → SystemMessage/UserMessage (client) 
  → /v1/aiTutor/conversations → {conversationId, content, finishReason}
```

### جریان خرید
```
Paywall trigger → Plans → Play Billing → RevenueCat → webhook → /v1/account → entitlement
```

## ۴. مرزهای دانش (چه چیزی SRV است و چه چیزی CLT)

| تصمیم | محل | قابل استخراج؟ |
|---|---|---|
| ترتیب محتوا | CLT (بستهٔ محتوا) | ✅ کامل |
| تصحیح تعاملی | CLT | ✅ کامل |
| تصحیح کدی | SRV (فرض) | ❌ |
| تسلط/تمرین | SRV | ❌ |
| زنجیره/کلید/XP | SRV | ❌ |
| کلید پیام مربی | SRV | ❌ |
| پرچم‌ها | RC + SRV | جزئی |
| قفل محتوا | SRV | ❌ |

## ۵. مقایسهٔ معماری با محصول هدف

| محور | Mimo | هدف کنکور |
|---|---|---|
| منبع محتوا | assets در APK | پکیج دانلودی نسخه‌دار |
| سنجش | درون‌درس، محلی | آزمون + بانک سؤال، سرور |
| مدل دانش | نامعلوم (SRV) | FSRS + mastery محلی/سرور |
| معیار موفقیت | XP/زنجیره | درصد/تراز/رتبه |
| رسمی‌سازی محتوا | CMS + publishSetVersion | CMS + version در سطح سؤال |
| آفلاین | outbox | outbox + بانک آفلاین |
