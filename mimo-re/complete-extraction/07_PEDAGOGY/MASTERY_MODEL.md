# ۰۷ه — مدل تسلط (آنچه می‌دانیم و نمی‌دانیم)

## ۱. شواهد موجود در بسته

| شاهد | معنا | اطمینان |
|---|---|---|
| `/v1/practice/statistics` | آمار تمرین، سمت سرور | VERIFIED_STATIC (مسیر) |
| ۳۶ رشتهٔ `practice_*` | فرانت آمار تمرین | PARTIALLY_VERIFIED |
| `practiceLevel1..3` | طبقه‌بندی تمرین | VERIFIED_STATIC |
| `Tutorial.type = practiceRequired` | تمرین اجباری به‌عنوان شرط | VERIFIED_STATIC (نوع) |
| `SmartPracticeChargedModal`, `SmartPracticeMasteredModal` | دو حالت «نیازمند تلاش» و «تسلط‌یافته» | PARTIALLY_VERIFIED |
| `AiTutorialConversationMessageCount` | شمارش پیام‌های مربی | VERIFIED_STATIC (کلاس) |

**نتیجه:** Mimo مفهوم «تسلط» را در UI دارد (Mastered) ولی مدل ریاضی آن در کلاینت نیست.

## ۲. آنچه ادعا نمی‌کنیم

* ❌ «الگوریتم SM-2/FSRS دارد» — هیچ شاهدی نیست.
* ❌ «آستانهٔ تسلط ۳ پاسخ درست متوالی دارد» — حدس است.
* ❌ «ضریب فراموشی دارد» — شاهدی نیست.

## ۳. مدل پیشنهادی برای محصول هدف (قابل ساخت، مبتنی بر ادبیات استاندارد)

```
mastery(concept) = weighted mean of evidence
evidence: correctness, latency, hint usage, recency, difficulty
schedule: FSRS-style (stability, difficulty, retrievability)
gate: practice unlocks when retrievability < 0.7  (قابل تنظیم)
```

| مؤلفه | فرمول/آستانهٔ پیشنهادی |
|---|---|
| شواهد اولیه | درست=1، غلط=0، با وزن سختی `1/(1+level)` |
| حافظه | S (پایداری) با FSRS؛ بازهٔ بعدی `S × factor(retrievability)` |
| تسلط مفهوم | میانگین وزنی ۵ شاهد آخر + پایداری |
| خروج از مرور | `retrievability > 0.9` در سه بازهٔ متوالی |
| تشخیص ضعف | `errorCode` تکرارشده ≥ ۲ بار |

Mimo این را ندارد؛ افزودن آن **الزام بخش ۱۷** است.
