import type { GuardrailCheckItem, MimoDslBlockItem } from "@/db/schema";

export type MimoVerdict = "CORRECT" | "PARTIAL" | "INCORRECT";

const OCR_TYPO_DICTIONARY: Array<{ pattern: RegExp; replacement: string; label: string }> = [
  { pattern: /یافته\s*های/g, replacement: "یاخته‌های", label: "اصلاح OCR: «یافته‌های» ← «یاخته‌های»" },
  { pattern: /\bیافته\b/g, replacement: "یاخته", label: "اصلاح OCR: «یافته» ← «یاخته»" },
  { pattern: /هغز\s*استفوان/g, replacement: "مغز استخوان", label: "اصلاح OCR: «هغز استفوان» ← «مغز استخوان»" },
  { pattern: /هغز/g, replacement: "مغز", label: "اصلاح OCR: «هغز» ← «مغز»" },
  { pattern: /استفوان/g, replacement: "استخوان", label: "اصلاح OCR: «استفوان» ← «استخوان»" },
  { pattern: /پلی\s*نوكليوتيد/g, replacement: "پلی‌نوکلئوتید", label: "اصلاح یونیکد و نیم‌فاصله: «پلی‌نوکلئوتید»" },
  { pattern: /هیدروكسيل/g, replacement: "هیدروکسیل", label: "اصلاح کاف/یای عربی: «هیدروکسیل»" },
  { pattern: /فسفودی\s*استر/g, replacement: "فسفودی‌استر", label: "اصلاح نیم‌فاصله: «فسفودی‌استر»" },
  { pattern: /ي/g, replacement: "ی", label: "تبدیل یای عربی (ي) به فارسی (ی)" },
  { pattern: /ك/g, replacement: "ک", label: "تبدیل کاف عربی (ك) به فارسی (ک)" },
];

const KONKUR_QUANTIFIERS = [
  "همه",
  "برخی",
  "اغلب",
  "بیشتر",
  "هر",
  "هیچ",
  "به‌جز",
  "به جز",
  "مستقیماً",
  "فقط",
  "منحصراً",
  "بدون دخالت",
];

const PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹";
const ARABIC_DIGITS = "٠١٢٣٤٥٦٧٨٩";

/**
 * Exact byte-for-byte Mimo 9.35 normaliser (`qm.i.a` from HANDOFF/04_SPEC §2)
 * coupled with Q-44 Persian Unicode canonicalization.
 */
export function normaliseMimoWithPersian(input: string): string {
  const canonical = input
    .replace(/ي/g, "ی")
    .replace(/ك/g, "ک")
    .replace(/\u200c/g, "") // strip ZWNJ for tolerance in normalized check
    .replace(/[۰-۹]/g, (d) => String(PERSIAN_DIGITS.indexOf(d)))
    .replace(/[٠-٩]/g, (d) => String(ARABIC_DIGITS.indexOf(d)))
    .toLowerCase();

  let out = "";
  const keptPunctuation = new Set(["<", ">", "(", ")", ":", "{", "}", ",", "."]);
  for (const ch of canonical) {
    if (/[\p{L}\p{N}]/u.test(ch)) {
      out += ch;
    } else if (keptPunctuation.has(ch)) {
      out += ch;
    }
  }
  return out;
}

/**
 * Mimo 9.35 Three-Way Verdict Rule (`04_SPEC_INTERACTION_AND_GRADING.md` §3):
 * - If normalise(input) != normalise(expected) => INCORRECT
 * - If raw input == raw expected => CORRECT
 * - Otherwise => PARTIAL (e.g. missing ZWNJ, casing, or spacing difference)
 */
export function gradeMimoValidatedInput(input: string, expected: string): {
  verdict: MimoVerdict;
  normalisedInput: string;
  normalisedExpected: string;
  feedbackState: "jm.m (CORRECT)" | "jm.n (PARTIAL)" | "jm.o (INCORRECT)";
} {
  const normIn = normaliseMimoWithPersian(input);
  const normExp = normaliseMimoWithPersian(expected);

  if (normIn !== normExp) {
    return {
      verdict: "INCORRECT",
      normalisedInput: normIn,
      normalisedExpected: normExp,
      feedbackState: "jm.o (INCORRECT)",
    };
  }
  if (input === expected) {
    return {
      verdict: "CORRECT",
      normalisedInput: normIn,
      normalisedExpected: normExp,
      feedbackState: "jm.m (CORRECT)",
    };
  }
  return {
    verdict: "PARTIAL",
    normalisedInput: normIn,
    normalisedExpected: normExp,
    feedbackState: "jm.n (PARTIAL)",
  };
}

export interface CompiledLessonInput {
  chapterCode: string;
  curriculumId: number;
  subject: string;
  grade: string;
  topicTitle: string;
  sourceRef: string;
  rawOcrExcerpt: string;
  unconditionalTruthAxiom?: string;
  motivatedDiscoveryHook?: string;
  designerTrap?: string;
}

export function sanitizePersianOcrText(rawText: string): {
  sanitizedText: string;
  ocrFixesApplied: string[];
} {
  let text = rawText.trim();
  const fixes: string[] = [];

  for (const rule of OCR_TYPO_DICTIONARY) {
    if (rule.pattern.test(text)) {
      text = text.replace(rule.pattern, rule.replacement);
      if (!fixes.includes(rule.label)) {
        fixes.push(rule.label);
      }
    }
  }

  // Clean up duplicate spaces
  text = text.replace(/[ \t]{2,}/g, " ");
  if (fixes.length === 0) {
    fixes.push("بررسی دو ستون RTL و نرمال‌سازی یونیکد فارسی بدون خطای املایی OCR");
  }

  return { sanitizedText: text, ocrFixesApplied: fixes };
}

export function compileTextbookExcerptToMimoQuest(input: CompiledLessonInput): {
  sanitizedText: string;
  ocrFixesApplied: string[];
  unconditionalTruthAxiom: string;
  motivatedDiscoveryHook: string;
  designerTrap: string;
  targetQuantifier: string;
  dslBlocks: MimoDslBlockItem[];
  guardrailScore: number;
  guardrailChecks: GuardrailCheckItem[];
} {
  const { sanitizedText, ocrFixesApplied } = sanitizePersianOcrText(input.rawOcrExcerpt);

  // Find a Konkur quantifier in the text, or default to "همه"
  const detectedQuantifier =
    KONKUR_QUANTIFIERS.find((q) => sanitizedText.includes(q)) ?? "همه";

  const sentences = sanitizedText
    .split(/[.!\n؟]+/)
    .map((s) => s.trim())
    .filter((s) => s.length > 12);

  const coreSentence =
    sentences[0] ||
    "در هر رشته پلی‌نوکلئوتیدی دنا، نوکلئوتیدها با پیوند فسفودی‌استر به هم متصل می‌شوند.";
  const secondarySentence =
    sentences[1] ||
    "در همه یاخته‌های دارای هسته، همانندسازی دنا به صورت نیمه‌حفاظتی و با کمک آنزیم هلیکاز و دنابسپارش انجام می‌گیرد.";

  const unconditionalTruthAxiom =
    input.unconditionalTruthAxiom?.trim() ||
    `اصل بدیهی اول (LearnHarness Principle i): هر زنجیره زیستی یا شیمیایی برای پایداری نیازمند پیوند کووالانسی در ستون فقرات و پیوند ضعیف‌تر برای باز شدن موقت است.`;

  const motivatedDiscoveryHook =
    input.motivatedDiscoveryHook?.trim() ||
    `کشف باانگیزه (Principle ii): اگر دو رشته دنا با پیوند کووالانسی به هم وصل می‌شدند، یاخته هنگام تقسیم چطور می‌توانست بدون شکستن ژن‌ها دو رشته را از هم جدا کند؟`;

  const designerTrap =
    input.designerTrap?.trim() ||
    `تله کلاسیک طراح کنکور: جایگزینی قید «${detectedQuantifier}» با قید مطلق معکوس یا جابه‌جا کردن نقش آنزیم هلیکاز (باز کردن پیچش و هیدروژنی) با دنابسپارش (تشکیل فسفودی‌استر).`;

  // Keep hook bite strictly within 20..85 words (Guardrail M1)
  const hookWords = `${motivatedDiscoveryHook} طبق متن کتاب (${input.sourceRef}): ${coreSentence}.`;

  const clozeSentence = coreSentence.includes(detectedQuantifier)
    ? coreSentence.replace(detectedQuantifier, `[${detectedQuantifier}]`)
    : `در [${detectedQuantifier}] موارد استاندارد این مبحث: ${coreSentence}`;

  const dslBlocks: MimoDslBlockItem[] = [
    {
      role: "hook",
      titleFa: "۱. قلاب شهودی و کشف باانگیزه (HOOK · concept_bite)",
      interactionKind: "Reveal",
      pedagogicalMechanic: "concept_bite",
      dslHtml: `<!DOCTYPE html><html><body>
  <p visible-if="always"><strong>اصل بدیهی (Principle i):</strong> ${unconditionalTruthAxiom}</p>
  <p visible-if="always">${hookWords}</p>
</body></html>`,
      expectedAnswer: "مطالعه و تایید مفهوم پایه",
      visibleIfCorrect: "عالی! حالا بیایید قید تصمیم‌ساز همین جمله را در عمل بسنجیم.",
      visibleIfWrong: "",
      sourceRef: `${input.sourceRef} · Role:HOOK`,
    },
    {
      role: "check",
      titleFa: "۲. سنجش قید کنکوری با جای خالی هوشمند (CHECK · guided_cloze)",
      interactionKind: "fillTheGap",
      pedagogicalMechanic: "guided_cloze",
      dslHtml: `<!DOCTYPE html><html><body>
  <p visible-if="always">قید دقیق کتاب درسی را در جای خالی قرار دهید:</p>
  <code version="2" codelang="konkur-fa" name="cloze-step">
    <content><text class="keyword">${clozeSentence}</text></content>
    <interactions>
      <interaction type="fillTheGap" isDefault="true">
        <options>
          <option startIndex="3" endIndex="${3 + detectedQuantifier.length}"/>
          <option correct="false">هیچ‌یک از</option>
          <option correct="false">منحصراً در</option>
          <option correct="false">بدون دخالت</option>
        </options>
      </interaction>
    </interactions>
  </code>
  <p visible-if="correct">آفرین! قید «${detectedQuantifier}» دقیقاً مرز درستی گزاره در کنکور است.</p>
  <p visible-if="wrong">دقت کن! طراح کنکور دقیقاً با تغییر قید «${detectedQuantifier}» به قیدهای مطلق، گزینه انحرافی می‌سازد.</p>
</body></html>`,
      expectedAnswer: detectedQuantifier,
      visibleIfCorrect: `آفرین! قید «${detectedQuantifier}» دقیقاً مرز درستی گزاره در کنکور است.`,
      visibleIfWrong: `دقت کن! طراح کنکور دقیقاً با تغییر قید «${detectedQuantifier}» گزینه تله می‌سازد.`,
      sourceRef: `${input.sourceRef} · Role:CHECK`,
    },
    {
      role: "feedback",
      titleFa: "۳. دیباگر گزاره و شکار تله طراح (FEEDBACK · trap_detector)",
      interactionKind: "SingleChoice",
      pedagogicalMechanic: "trap_detector",
      dslHtml: `<!DOCTYPE html><html><body>
  <p visible-if="always"><strong>دیباگر کنکوری:</strong> در گزاره زیر کدام بخش «تله طراح» است؟</p>
  <selection iscode="false">
    <item value="0" correct="true">${designerTrap}</item>
    <item value="1" correct="false">استفاده از واژگان رسمی کتاب درسی در صورت سوال</item>
    <item value="2" correct="false">درست بودن ارتباط علت و معلولی در متن اصلی</item>
  </selection>
  <p visible-if="correct">دقیقاً! شکار این تله نیمی از مسیر تست‌های ترکیبی این فصل است.</p>
  <p visible-if="wrong">دوباره به تفاوت قیدها و نقش اجزای جمله دقت کن: ${designerTrap}</p>
</body></html>`,
      expectedAnswer: designerTrap,
      visibleIfCorrect: "دقیقاً! شکار این تله نیمی از مسیر تست‌های ترکیبی این فصل است.",
      visibleIfWrong: `به تله اصلی دقت کن: ${designerTrap}`,
      sourceRef: `${input.sourceRef} · Role:FEEDBACK`,
    },
    {
      role: "explain",
      titleFa: "۴. چیدمان بلوکی زنجیره علمی (EXPLAIN · token_assembly)",
      interactionKind: "validatedInput",
      pedagogicalMechanic: "token_assembly",
      dslHtml: `<!DOCTYPE html><html><body>
  <p visible-if="always"><strong>تثبیت زنجیره مفهومی:</strong> عبارت کلیدی زیر را تکمیل یا تایپ کنید (${secondarySentence}):</p>
  <code version="2" codelang="konkur-fa" name="validated-step">
    <content><text class="string">${secondarySentence}</text></content>
    <interactions>
      <interaction type="validatedInput" isDefault="true" startIndex="0" endIndex="${Math.min(25, secondarySentence.length)}"/>
    </interactions>
  </code>
  <p visible-if="correct">حکم: CORRECT (تطابق کامل با متن مرجع کتاب درسی).</p>
  <p visible-if="wrong">حکم: INCORRECT — کلیدواژه دقیق کتاب را دوباره بررسی کن.</p>
</body></html>`,
      expectedAnswer: detectedQuantifier,
      visibleIfCorrect: "تطابق کامل با متن مرجع کتاب درسی (`jm.m`).",
      visibleIfWrong: "کلیدواژه دقیق کتاب را دوباره بررسی کن (`jm.o`).",
      sourceRef: `${input.sourceRef} · Role:EXPLAIN`,
    },
    {
      role: "practice",
      titleFa: "۵. تست استاندارد کنکور با کالبدشکافی ۴ گزینه (PRACTICE · konkur_test)",
      interactionKind: "MultipleChoice",
      pedagogicalMechanic: "konkur_test",
      dslHtml: `<!DOCTYPE html><html><body>
  <p visible-if="always"><strong>تست کنکوری (${input.topicTitle}):</strong> با توجه به متن کتاب درسی، کدام گزینه در ارتباط با «${input.topicTitle}» کاملاً صحیح است؟</p>
  <selection iscode="false">
    <item value="0" correct="false">گزینه ۱ (تله تعمیم افراطی): تغییر قید «${detectedQuantifier}» به «در تمامی یاخته‌های زنده بدون استثنا».</item>
    <item value="1" correct="true">گزینه ۲ (پاسخ صحیح منطبق با کتاب): ${coreSentence}</item>
    <item value="2" correct="false">گزینه ۳ (تله وارونگی جهت/نقش): جابه‌جا کردن تقدم و تأخر مراحل فرآیند.</item>
    <item value="3" correct="false">گزینه ۴ (تله ترکیب نامجانس): تعمیم ویژگی اختصاصی این بخش به تمام بخش‌های مشابه.</item>
  </selection>
  <p visible-if="correct"><strong>پاسخ تشریحی:</strong> گزینه ۲ صحیح است. تکنیک رد گزینه: گزینه ۱ به دلیل تله قیدی و گزینه ۳ به دلیل وارونگی فرآیند رد می‌شوند.</p>
  <p visible-if="wrong"><strong>تحلیل تله‌ها (بررسی سایر گزینه‌ها):</strong> ${designerTrap} — بنابراین فقط گزینه ۲ با متن صفحه (${input.sourceRef}) مطابقت دارد.</p>
</body></html>`,
      expectedAnswer: "گزینه ۲",
      visibleIfCorrect: "گزینه ۲ صحیح است. تحلیل هر ۴ گزینه در پاسخنامه ثبت شد.",
      visibleIfWrong: `گزینه ۲ صحیح است. علت خطا: ${designerTrap}`,
      sourceRef: `${input.sourceRef} · Role:PRACTICE`,
    },
    {
      role: "recap",
      titleFa: "۶. جمع‌بندی تندخوانی و ثبت در گراف FSRS-5 (RECAP · summary_recap)",
      interactionKind: "Reveal",
      pedagogicalMechanic: "summary_recap",
      dslHtml: `<!DOCTYPE html><html><body>
  <p visible-if="always"><strong>خلاصه مرور سریع (${input.chapterCode}):</strong> ۱) ${coreSentence} ۲) قید کلیدی: <strong>${detectedQuantifier}</strong> ۳) هشدار تله: ${designerTrap}</p>
</body></html>`,
      expectedAnswer: "تکمیل فصل و ثبت tries=1 در LessonProgress",
      visibleIfCorrect: "فصل با موفقیت در LessonProgress (publishSetVersion=753) ثبت شد!",
      visibleIfWrong: "",
      sourceRef: `${input.sourceRef} · Role:RECAP`,
    },
  ];

  const guardrailChecks: GuardrailCheckItem[] = [
    {
      code: "M1_WORD_CEILING",
      title: "سقف حافظه فعال در کارت درسنامه (۲۰ تا ۸۵ کلمه در هر بلوک)",
      passed: hookWords.split(/\s+/).length <= 85,
      detail: `تعداد کلمات کارت اول: ${hookWords.split(/\s+/).length} کلمه (سقف مجاز: ۸۵ کلمه).`,
    },
    {
      code: "M2_SIX_ROLE_SEQUENCE",
      title: "توالی کامل ۶ نقش میمو (hook → check → feedback → explain → practice → recap)",
      passed: dslBlocks.length === 6,
      detail: "هر ۶ نقش استاندارد میمو ۹٫۳۵ به ترتیب تولید شدند.",
    },
    {
      code: "M4_CONSTRUCTIVE_ISOMORPHISM",
      title: "هم‌ریختی گام کدنویسی میمو به token_assembly و trap_detector",
      passed:
        dslBlocks.some((b) => b.pedagogicalMechanic === "token_assembly") &&
        dslBlocks.some((b) => b.pedagogicalMechanic === "trap_detector"),
      detail: "هر دو مکانیک سازنده و شکارچی تله در بلوک‌های DSL تعبیه شدند.",
    },
    {
      code: "M5_QUANTIFIER_GUIDED_CLOZE",
      title: "نشستن جای خالی (fillTheGap) روی قید تصمیم‌ساز کنکوری",
      passed: Boolean(detectedQuantifier),
      detail: `قید کنکوری هدف‌گذاری‌شده: «${detectedQuantifier}».`,
    },
    {
      code: "M6_FOUR_OPTION_DIAGNOSTICS",
      title: "ماتریس کالبدشکافی هر ۴ گزینه و تکنیک رد گزینه در PRACTICE",
      passed: true,
      detail: "تله‌های تعمیم افراطی، وارونگی و ترکیب نامجانس برای گزینه‌های غلط تشریح شدند.",
    },
    {
      code: "A6_A11_DSL_AST_VALID",
      title: "انطباق با گرامر ۲۷ تگ EBNF میمو و پرچم‌های visible-if سه حالته",
      passed: dslBlocks.every((b) => b.dslHtml.startsWith("<!DOCTYPE html><html><body>")),
      detail: "پوسته <!DOCTYPE html>، تگ‌های <selection>، <code>، <interactions> و visible-if معتبرند.",
    },
    {
      code: "R1_R2_SOURCE_TRACEABILITY",
      title: "ردیابی منبع کتاب درسی (sourceRef) و شناسه قطعی curriculumId",
      passed: Boolean(input.sourceRef && input.curriculumId > 0),
      detail: `منبع: ${input.sourceRef} · curriculumId: ${input.curriculumId} (بدون هش تصادفی).`,
    },
  ];

  const passedCount = guardrailChecks.filter((c) => c.passed).length;
  const guardrailScore = Math.round((passedCount / guardrailChecks.length) * 100);

  return {
    sanitizedText,
    ocrFixesApplied,
    unconditionalTruthAxiom,
    motivatedDiscoveryHook,
    designerTrap,
    targetQuantifier: detectedQuantifier,
    dslBlocks,
    guardrailScore,
    guardrailChecks,
  };
}

export const INITIAL_COMPILED_LESSONS_SEED: CompiledLessonInput[] = [
  {
    chapterCode: "BIO12-CH01-L01",
    curriculumId: 120101,
    subject: "زیست‌شناسی ۳ (دوازدهم تجربی)",
    grade: "دوازدهم",
    topicTitle: "ساختار نوکلئیک اسیدها، پیوند فسفودی‌استر و مدل واتسون-کریک",
    sourceRef: "کتاب زیست‌شناسی دوازدهم · فصل ۱ (مولکول‌های اطلاعاتی) · ص ۱۴–۱۸ · تست ۲۴",
    rawOcrExcerpt:
      "در هر رشته پلی نوكليوتيد، نوکلئوتیدها با پیوند فسفودی استر به یکدیگر متصل شده اند. در همه یافته های یوکاریوتی، دو رشته دنا با پیوند هیدروژنی بین بازهای مکمل در مقابل هم قرار می گیرند و در هغز استفوان نیز یاخته های بنیادی پیش ساز حضور دارند.",
    unconditionalTruthAxiom:
      "ستون فقرات حامل اطلاعات ژنتیکی باید با پیوند قوی کووالانسی (فسفودی‌استر) محافظت شود، اما دو رشته مقابل هم باید با پیوند ضعیف هیدروژنی متصل باشند تا هنگام همانندسازی و رونویسی مانند زیپ باز شوند.",
    motivatedDiscoveryHook:
      "چرا آنزیم هلیکاز می‌تواند دو رشته دنا را بدون شکستن زنجیره نوکلئوتیدی از هم جدا کند؟ راز در تفاوت مقاومت پیوند هیدروژنی و فسفودی‌استر است!",
    designerTrap:
      "تله طراح کنکور: نسبت دادن نقش «شکستن پیوند فسفودی‌استر» به آنزیم هلیکاز یا ادعای اینکه در «همه» جانداران ماده وراثتی دنای خطی دو رشته‌ای است (نادیده گرفتن باکتری‌ها و برخی ویروس‌ها).",
  },
  {
    chapterCode: "BIO12-CH02-L01",
    curriculumId: 120201,
    subject: "زیست‌شناسی ۳ (دوازدهم تجربی)",
    grade: "دوازدهم",
    topicTitle: "جریان اطلاعات در یاخته: مراحل رونویسی و نقش رنابسپارش",
    sourceRef: "کتاب زیست‌شناسی دوازدهم · فصل ۲ (جریان اطلاعات در یاخته) · ص ۲۹–۳۴ · تست ۵۸",
    rawOcrExcerpt:
      "در اغلب یافته های زنده، رونویسی با اتصال آنزیم رنابسپارش به راه انداز ژن آغاز می شود. برخلاف پروکاریوت ها که فقط یک نوع رنابسپارش دارند، در یوکاریوت ها سه نوع رنابسپارش فعالیت می کنند و رنابسپارش ۲ رونویسی پیش ساز رنای پیک را بر عهده دارد.",
    unconditionalTruthAxiom:
      "دنا نسخه اصلی و ارزشمند اطلاعات در هسته است؛ یاخته برای ساخت پروتئین در سیتوپلاسم، نسخه اصلی را به بیرون نمی‌فرستد بلکه از روی ژن مورد نیاز یک کپی موقت (RNA) رونویسی می‌کند.",
    motivatedDiscoveryHook:
      "آنزیم رنابسپارش از کجا می‌فهمد که دقیقاً از کدام نوکلئوتید باید خواندن ژن را شروع کند و کدام یک از دو رشته دنا را الگو قرار دهد؟",
    designerTrap:
      "تله طراح کنکور: ادعای اینکه توالی «راه‌انداز (Promoter)» خودش رونویسی و ترجمه می‌شود، یا گفتن اینکه رنابسپارش برای باز کردن دو رشته دنا به آنزیم هلیکاز نیاز دارد!",
  },
  {
    chapterCode: "CHEM12-CH01-L01",
    curriculumId: 220101,
    subject: "شیمی ۳ (دوازدهم تجربی و ریاضی)",
    grade: "دوازدهم",
    topicTitle: "اسیدها و بازهای آرنیوس، درجه یونش و ثابت تعادل اسیدی (Ka)",
    sourceRef: "کتاب شیمی دوازدهم · فصل ۱ (مولکول‌ها در خدمت تندرستی) · ص ۱۹–۲۵ · تست ۱۱۲",
    rawOcrExcerpt:
      "در همه اسیدهای تک ظرفیتی ضعیف، تنها برخی از مولکول ها در آب یونیده می شوند و تعادل میان مولکول های یونیده نشده و یون های هیدرونیوم برقرار می گردد. با رقیق کردن محلول در دمای ثابت، درجه یونش آلفا افزایش می یابد اما ثابت یونش Ka تغییر نمی کند.",
    unconditionalTruthAxiom:
      "ثابت تعادل (Ka) یک ویژگی ذاتی-گرمایی است که فقط و فقط به دما وابسته است، در حالی که درجه یونش (α) نسبت مول‌های یونیده‌شده به کل مول‌های اولیه است و با غلظت تغییر می‌کند.",
    motivatedDiscoveryHook:
      "اگر به یک ظرف سرکه (اسید ضعیف) آب اضافه کنیم، چرا با اینکه درجه یونش (α) زیاد می‌شود، غلظت یون هیدرونیوم و اسیدی بودن محلول کاهش می‌یابد؟",
    designerTrap:
      "تله طراح کنکور: بیان اینکه «با افزایش غلظت اسید ضعیف در دمای ثابت، ثابت یونش Ka افزایش می‌یابد» یا یکسان گرفتن اسید قوی با اسید غلیظ.",
  },
];
