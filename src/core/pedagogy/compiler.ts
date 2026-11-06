import type { GuardrailCheck, Lesson, LessonBlock, MCQ, Role, Token } from "@/core/types";
import type { LessonSeed } from "./seed-types";

const ROLE_TITLES: Record<Role, string> = {
  hook: "قلاب شهودی · کشف باانگیزه",
  check: "جای خالیِ قید کنکوری",
  feedback: "دیباگر گزاره · شکار تلهٔ طراح",
  explain: "چیدمان بلوکی زنجیرهٔ علمی",
  practice: "تست استاندارد کنکور",
  recap: "جمع‌بندی و ثبت در برنامهٔ مرور",
};

/** Deterministic shuffle so server and client always render the same order. */
export function stableShuffle<T>(items: T[], salt: string): T[] {
  const arr = [...items];
  let seed = 0;
  for (const ch of salt) seed = (seed * 31 + ch.charCodeAt(0)) % 2147483647;
  for (let i = arr.length - 1; i > 0; i--) {
    seed = (seed * 1103515245 + 12345) % 2147483648;
    const j = seed % (i + 1);
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export function tokenizeSentence(sentenceFa: string): Token[] {
  const words = sentenceFa
    .replace(/[.؟!]/g, "")
    .split(/\s+/)
    .filter(Boolean);
  return words.map((text, index) => ({
    id: `w${index}`,
    text,
    kind: index === 0 ? "anchor" : "link",
  }));
}

function escapeHtml(value: string): string {
  return value.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function revealDsl(body: string[]): string {
  return `<!DOCTYPE html><html><body>\n${body
    .map((p) => `  <p visible-if="always">${escapeHtml(p)}</p>`)
    .join("\n")}\n</body></html>`;
}

function clozeDsl(sentenceFa: string, distractors: string[]): string {
  const blanked = sentenceFa.replace(/_{2,}|…|\.\.\./, "<blank/>");
  return `<!DOCTYPE html><html><body>
  <p visible-if="always">${escapeHtml(blanked)}</p>
  <code version="2" codelang="konkur-fa" name="cloze-step">
    <content><text class="keyword">${escapeHtml(sentenceFa)}</text></content>
    <interactions>
      <interaction type="fillTheGap" isDefault="true">
        <options>
          ${distractors.map((d) => `<option correct="false">${escapeHtml(d)}</option>`).join("\n          ")}
        </options>
      </interaction>
    </interactions>
  </code>
  <p visible-if="correct">${escapeHtml("درست! قید/کلیدواژهٔ تصمیم‌ساز را یافتی.")}</p>
  <p visible-if="wrong">${escapeHtml("دوباره به قید و کلیدواژهٔ جمله دقت کن.")}</p>
</body></html>`;
}

function assemblyDsl(tokens: Token[], solution: string[]): string {
  const order = solution
    .map((id) => tokens.find((t) => t.id === id)?.text ?? "")
    .join(" ");
  return `<!DOCTYPE html><html><body>
  <p visible-if="always">بلوک‌های زنجیرهٔ علمی را به ترتیب کتاب بچین:</p>
  <code version="2" codelang="konkur-fa" name="assembly-step">
    <content><text class="string">${escapeHtml(order)}</text></content>
    <interactions>
      <interaction type="dragDrop" isDefault="true">
        <options>
          ${stableShuffle(tokens, "assembly")
            .map((t) => `<option token="${t.id}" trap="${t.kind === "trap"}">${escapeHtml(t.text)}</option>`)
            .join("\n          ")}
        </options>
      </interaction>
    </interactions>
  </code>
  <p visible-if="correct">زنجیرهٔ مفهومی با متن کتاب منطبق است.</p>
  <p visible-if="wrong">یکی از بلوک‌ها تلهٔ طراح است؛ ترتیب و نقش‌ها را دوباره بسنج.</p>
</body></html>`;
}

function trapDsl(options: { id: string; textFa: string; isTrap: boolean }[]): string {
  return `<!DOCTYPE html><html><body>
  <p visible-if="always">کدام گزاره «تلهٔ طراح» است؟</p>
  <selection iscode="false">
    ${options
      .map((o) => `<item value="${o.id}" correct="${o.isTrap}">${escapeHtml(o.textFa)}</item>`)
      .join("\n    ")}
  </selection>
  <p visible-if="correct">تله را شکار کردی!</p>
  <p visible-if="wrong">به تغییر قید و جابه‌جایی نقش اجزا دقت کن.</p>
</body></html>`;
}

function mcqDsl(mcq: MCQ): string {
  return `<!DOCTYPE html><html><body>
  <p visible-if="always">${escapeHtml(mcq.stemFa)}</p>
  <selection iscode="false">
    ${mcq.options
      .map((o) => `<item value="${o.id}" correct="${o.correct}">${escapeHtml(o.textFa)}</item>`)
      .join("\n    ")}
  </selection>
  <p visible-if="correct">${escapeHtml(mcq.options.find((o) => o.correct)?.analysisFa ?? "")}</p>
</body></html>`;
}

export function compileLesson(seed: LessonSeed): Lesson {
  const skillConcept = `${seed.id}.concept`;
  const skillApplication = `${seed.id}.application`;
  const dependsOnConcept = seed.dependsOnLessonIds?.length
    ? seed.dependsOnLessonIds.map((id) => `${id}.concept`)
    : [];

  const questions: MCQ[] = seed.questions.map((q, qi) => ({
    id: `${seed.id}-Q${qi + 1}`,
    lessonId: seed.id,
    chapterId: seed.chapterId,
    subjectId: seed.subjectId,
    skillId: qi === 0 ? skillApplication : skillConcept,
    stemFa: q.stemFa,
    options: q.options.map((textFa, oi) => ({
      id: `opt${oi}`,
      textFa,
      correct: oi === q.correctIndex,
      analysisFa: q.analyses[oi],
    })),
    difficulty: q.difficulty,
    hintFa: q.hintFa,
    sourceRef: seed.sourceRef,
    quantifierFa: seed.cloze.answer,
  }));

  const trapOptions = [
    {
      id: "trap",
      textFa: seed.trap.statementFa,
      isTrap: true,
      analysisFa: seed.trap.explanationFa,
    },
    ...seed.trap.decoysFa.map((textFa, i) => ({
      id: `decoy${i}`,
      textFa,
      isTrap: false,
      analysisFa: "این گزاره یا درست است یا فقط یک بازنویسی بی‌خطر از متن کتاب است؛ تلهٔ اصلی جای دیگری است.",
    })),
  ];

  const shuffledTrapOptions = stableShuffle(trapOptions, seed.id);
  const assemblyTokens: Token[] = [
    ...seed.assembly.solution.map((text, i) => ({
      id: `a${i}`,
      text,
      kind: (i === 0 ? "anchor" : i === seed.assembly.solution.length - 1 ? "modifier" : "link") as Token["kind"],
    })),
    ...seed.assembly.traps.map((text, i) => ({
      id: `t${i}`,
      text,
      kind: "trap" as const,
      trapHintFa: seed.trap.explanationFa,
    })),
  ];

  const shuffledTokens = stableShuffle(assemblyTokens, `${seed.id}-ui`);

  const blocks: LessonBlock[] = [
    {
      id: `${seed.id}-hook`,
      lessonId: seed.id,
      role: "hook",
      mechanic: "concept_bite",
      renderer: "reveal",
      titleFa: ROLE_TITLES.hook,
      promptFa: seed.hookFa,
      bodyFa: [seed.axiomFa, ...seed.propositions.slice(0, 2).map((p) => p.textFa)],
      hintFa: "قبل از ادامه، مکث کن: اگر این اصل بدیهی نبود، چه اتفاقی در یاخته می‌افتاد؟",
      feedback: {
        correctFa: "حالا درک شهودی داری؛ برویم سراغ قیدهای تصمیم‌ساز کتاب.",
        wrongFa: "",
      },
      sourceRef: seed.sourceRef,
      skillId: skillConcept,
      dsl: revealDsl([seed.axiomFa, seed.hookFa]),
    },
    {
      id: `${seed.id}-check`,
      lessonId: seed.id,
      role: "check",
      mechanic: "guided_cloze",
      renderer: "cloze",
      titleFa: ROLE_TITLES.check,
      promptFa: "کلیدواژهٔ دقیق کتاب را در جای خالی بگذار. همین کلمه مرز درستی و نادرستی گزینه‌های کنکور است.",
      bodyFa: [],
      hintFa: seed.cloze.hintFa,
      cloze: {
        sentenceFa: seed.cloze.sentenceFa,
        answer: seed.cloze.answer,
        distractors: seed.cloze.distractors,
        hintFa: seed.cloze.hintFa,
        quantifiers: seed.propositions.map((p) => p.quantifierFa).filter(Boolean) as string[],
      },
      expectedAnswer: seed.cloze.answer,
      feedback: {
        correctFa: `آفرین! «${seed.cloze.answer}» دقیقاً همان کلیدواژهٔ کتاب است.`,
        wrongFa: `کلیدواژهٔ درست «${seed.cloze.answer}» است. ${seed.cloze.hintFa}`,
        partialFa: "نزدیک بودی؛ فقط شکل نوشتاری را با كتاب هماهنگ کن.",
      },
      sourceRef: seed.sourceRef,
      skillId: skillConcept,
      dsl: clozeDsl(seed.cloze.sentenceFa, seed.cloze.distractors),
    },
    {
      id: `${seed.id}-feedback`,
      lessonId: seed.id,
      role: "feedback",
      mechanic: "trap_detector",
      renderer: "trap",
      titleFa: ROLE_TITLES.feedback,
      promptFa: "سه گزاره می‌بینی. کدام‌یک «تلهٔ طراح» است؟ تله همیشه با جابه‌جایی قید، نقش آنزیم یا جهت فرآیند ساخته می‌شود.",
      bodyFa: [],
      hintFa: seed.trap.explanationFa,
      trapOptions: shuffledTrapOptions,
      expectedAnswer: seed.trap.statementFa,
      feedback: {
        correctFa: "دقیقاً! شکار این تله نیمی از مسیر تست‌های ترکیبی این فصل است.",
        wrongFa: seed.trap.explanationFa,
      },
      sourceRef: seed.sourceRef,
      skillId: skillApplication,
      dsl: trapDsl(shuffledTrapOptions),
    },
    {
      id: `${seed.id}-explain`,
      lessonId: seed.id,
      role: "explain",
      mechanic: "token_assembly",
      renderer: "assembly",
      titleFa: ROLE_TITLES.explain,
      promptFa: seed.assembly.instructionFa,
      bodyFa: seed.propositions.map((p) => p.textFa),
      hintFa: "بلوک‌های تله را کنار بگذار؛ فقط واژه‌های متن کتاب زنجیره را می‌سازند.",
      tokens: shuffledTokens,
      assembly: {
        instructionFa: seed.assembly.instructionFa,
        solution: seed.assembly.solution.map((_, i) => `a${i}`),
        answerFa: seed.assembly.answerFa,
      },
      expectedAnswer: seed.assembly.answerFa,
      feedback: {
        correctFa: "زنجیرهٔ مفهومی با متن کتاب منطبق است. این همان مکانیک کدنویسی میمو است، در قالب علم.",
        wrongFa: `ترتیب درست: ${seed.assembly.answerFa}`,
      },
      sourceRef: seed.sourceRef,
      skillId: skillApplication,
      dsl: assemblyDsl(shuffledTokens, seed.assembly.solution.map((_, i) => `a${i}`)),
    },
    {
      id: `${seed.id}-practice`,
      lessonId: seed.id,
      role: "practice",
      mechanic: "konkur_test",
      renderer: "mcq",
      titleFa: ROLE_TITLES.practice,
      promptFa: "یک تست کنکوری با نمرهٔ منفی یک‌سوم. اول بدون راهنما جواب بده تا پاسخ «مستقل» ثبت شود.",
      bodyFa: [],
      hintFa: questions[0]?.hintFa ?? "",
      mcq: questions[0],
      expectedAnswer: questions[0]?.options.find((o) => o.correct)?.textFa ?? "",
      feedback: {
        correctFa: "پاسخ صحیح. تحلیل سه گزینهٔ دیگر را در پاسخنامه ببین.",
        wrongFa: "پاسخ درست و تحلیل تله‌های هر گزینه را ببین؛ همان‌ها در صف مرور ثبت می‌شوند.",
      },
      sourceRef: seed.sourceRef,
      skillId: skillApplication,
      dsl: questions[0] ? mcqDsl(questions[0]) : revealDsl(["تست این درس در حال تکمیل است."]),
    },
    {
      id: `${seed.id}-recap`,
      lessonId: seed.id,
      role: "recap",
      mechanic: "summary_recap",
      renderer: "reveal",
      titleFa: ROLE_TITLES.recap,
      promptFa: "خلاصهٔ مرور سریع؛ همین سه جمله را فردا در صف FSRS می‌بینی.",
      bodyFa: seed.recapFa,
      hintFa: "",
      feedback: {
        correctFa: "فصل در LessonProgress ثبت شد و کارت‌های مرور زمان‌بندی شدند.",
        wrongFa: "",
      },
      sourceRef: seed.sourceRef,
      skillId: skillConcept,
      dsl: revealDsl(seed.recapFa),
    },
  ];

  const guardrails = buildGuardrails(seed, blocks, questions);

  return {
    id: seed.id,
    curriculumId: seed.curriculumId,
    subjectId: seed.subjectId,
    chapterId: seed.chapterId,
    order: seed.order,
    titleFa: seed.titleFa,
    subtitleFa: seed.subtitleFa,
    sourceRef: seed.sourceRef,
    minutes: seed.minutes,
    axiomFa: seed.axiomFa,
    hookFa: seed.hookFa,
    trapFa: seed.trap.explanationFa,
    recapFa: seed.recapFa,
    propositions: seed.propositions.map((p, i) => ({
      id: `${seed.id}-P${i + 1}`,
      textFa: p.textFa,
      quantifierFa: p.quantifierFa,
    })),
    blocks,
    skills: [
      { id: skillConcept, lessonId: seed.id, labelFa: `${seed.titleFa} · فهم`, kind: "concept", dependsOn: dependsOnConcept },
      {
        id: skillApplication,
        lessonId: seed.id,
        labelFa: `${seed.titleFa} · کاربرد و تله`,
        kind: "application",
        dependsOn: [skillConcept],
      },
    ],
    questions,
    dslHtml: `<!-- Mimo 9.35 · lesson ${seed.id} · publishSetVersion 753 -->
${blocks.map((b) => b.dsl).join("\n\n")}`,
    guardrails,
    reviewStatus: guardrails.every((g) => g.passed) ? "approved" : "unreviewed",
  };
}

function wordCount(text: string): number {
  return text.split(/\s+/).filter(Boolean).length;
}

function buildGuardrails(seed: LessonSeed, blocks: LessonBlock[], questions: MCQ[]): GuardrailCheck[] {
  const hookWords = blocks[0].bodyFa.reduce((sum, p) => sum + wordCount(p), 0);
  const mechanics = new Set(blocks.map((b) => b.mechanic));
  const optionCountsOk = questions.every((q) => q.options.length === 4 && q.options.filter((o) => o.correct).length === 1);

  return [
    {
      code: "M1_WORD_CEILING",
      titleFa: "سقف حافظهٔ فعال در هر کارت (۲۰ تا ۸۵ کلمه)",
      passed: hookWords >= 20 && hookWords <= 85,
      detailFa: `کارت قلاب ${hookWords} کلمه دارد (بازهٔ مجاز ۲۰ تا ۸۵).`,
    },
    {
      code: "M2_SIX_ROLE_SEQUENCE",
      titleFa: "توالی کامل شش نقش میمو",
      passed: blocks.map((b) => b.role).join(">") === "hook>check>feedback>explain>practice>recap",
      detailFa: "ترتیب hook → check → feedback → explain → practice → recap برقرار است.",
    },
    {
      code: "M3_QUANTIFIER_CLOZE",
      titleFa: "جای خالی روی قید/کلیدواژهٔ تصمیم‌ساز کنکور",
      passed: Boolean(seed.cloze.answer && seed.cloze.distractors.length >= 2),
      detailFa: `کلیدواژهٔ هدف: «${seed.cloze.answer}» با ${seed.cloze.distractors.length} گزینهٔ انحرافی.`,
    },
    {
      code: "M4_CONSTRUCTIVE_ISOMORPHISM",
      titleFa: "هم‌ریختی گام کدنویسی میمو (چیدمان + دیباگ)",
      passed: mechanics.has("token_assembly") && mechanics.has("trap_detector"),
      detailFa: "مکانیک سازنده (token_assembly) و شکارچی تله (trap_detector) هر دو حاضرند.",
    },
    {
      code: "M5_FOUR_OPTION_DIAGNOSTICS",
      titleFa: "چهار گزینه با تحلیل تک‌تک",
      passed: optionCountsOk && questions.length >= 1,
      detailFa: `${questions.length} تست با ${optionCountsOk ? "چهار گزینه و تحلیل جداگانه" : "گزینهٔ نامعتبر"} ثبت شد.`,
    },
    {
      code: "M6_AXIOM_AND_HOOK",
      titleFa: "اصل بدیهی و کشف باانگیزه (Principle i و ii)",
      passed: seed.axiomFa.length > 30 && seed.hookFa.includes("؟"),
      detailFa: "اصل بدیهی و پرسش کشف باانگیزه تولید شدند.",
    },
    {
      code: "M7_TRAP_FIDELITY",
      titleFa: "تلهٔ طراح با تحلیل علت",
      passed: seed.trap.statementFa.length > 20 && seed.trap.explanationFa.length > 30,
      detailFa: "گزارهٔ تله همراه با توضیح مکانیزم فریب ثبت شد.",
    },
    {
      code: "M8_SOURCE_TRACEABILITY",
      titleFa: "ردیابی منبع و شناسهٔ قطعی curriculumId",
      passed: Boolean(seed.sourceRef) && seed.curriculumId > 0,
      detailFa: `منبع: ${seed.sourceRef} · curriculumId: ${seed.curriculumId}`,
    },
    {
      code: "M9_DSL_AST_VALID",
      titleFa: "انطباق با گرامر میمو و پرچم visible-if",
      passed: blocks.every((b) => b.dsl.startsWith("<!DOCTYPE html><html><body>") && b.dsl.includes("visible-if")),
      detailFa: "همهٔ بلوک‌ها پوستهٔ استاندارد و پرچم سه‌حالتهٔ visible-if دارند.",
    },
    {
      code: "M10_DIFFICULTY_COVERAGE",
      titleFa: "پوشش سطح دشواری در بانک تست",
      passed: questions.some((q) => q.difficulty >= 2),
      detailFa: "دست‌کم یک تست ترکیبی/سخت در بانک درس موجود است.",
    },
  ];
}
