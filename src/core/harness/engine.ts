import type { Lesson } from "@/core/types";

/**
 * LearnHarness — four phases (Measure → Plan → Teach → Practice) executed locally.
 * The offline provider grounds every message in the book proposition graph,
 * so the coach can never invent lesson content (anti-hallucination invariant).
 */

export type HarnessPhase = "measure" | "plan" | "teach" | "practice";

export const PHASE_LABELS: Record<HarnessPhase, string> = {
  measure: "سنجش",
  plan: "برنامه",
  teach: "آموزش",
  practice: "تمرین",
};

export const PHASE_ORDER: HarnessPhase[] = ["measure", "plan", "teach", "practice"];

export interface HarnessMessage {
  id: string;
  role: "coach" | "learner" | "system";
  phase: HarnessPhase;
  textFa: string;
  at: number;
  chips?: string[];
}

export interface HarnessSession {
  lessonId: string;
  phase: HarnessPhase;
  messages: HarnessMessage[];
  attempts: number;
  provider: "offline" | "online";
}

const msg = (
  role: HarnessMessage["role"],
  phase: HarnessPhase,
  textFa: string,
  chips?: string[],
  at = Date.now(),
): HarnessMessage => ({
  id: `h-${at}-${Math.random().toString(36).slice(2, 8)}`,
  role,
  phase,
  textFa,
  at,
  chips,
});

export function createHarnessSession(lesson: Lesson, provider: HarnessSession["provider"] = "offline"): HarnessSession {
  return {
    lessonId: lesson.id,
    phase: "measure",
    provider,
    attempts: 0,
    messages: [
      msg(
        "system",
        "measure",
        `جلسه روی «${lesson.titleFa}» آغاز شد. منبع: ${lesson.sourceRef} · حالت ${provider === "offline" ? "آفلاین (LocalContentProvider)" : "آنلاین"}.`,
      ),
      msg(
        "coach",
        "measure",
        `قبل از هر توضیحی، یک سنجش کوتاه: ${lesson.hookFa}`,
        ["نمی‌دانم، از اصل بدیهی شروع کن", "فکر می‌کنم جوابش با پیوندها مرتبط است"],
      ),
    ],
  };
}

function keywordHit(text: string, lesson: Lesson): boolean {
  const keywords = new Set<string>();
  for (const p of lesson.propositions) {
    for (const word of p.textFa.split(/[\s،.,؟:()]+/)) {
      if (word.length >= 4) keywords.add(word);
    }
  }
  for (const word of lesson.trapFa.split(/[\s،.,؟:()]+/)) {
    if (word.length >= 4) keywords.add(word);
  }
  const normalized = text.replace(/\u200c/g, " ");
  let hits = 0;
  for (const keyword of keywords) {
    if (normalized.includes(keyword)) hits += 1;
    if (hits >= 2) return true;
  }
  return hits >= 1 && text.trim().length > 12;
}

export function advanceHarness(session: HarnessSession, userText: string, lesson: Lesson): HarnessSession {
  const at = Date.now();
  const messages = [...session.messages, msg("learner", session.phase, userText.trim(), undefined, at)];
  const hit = keywordHit(userText, lesson);
  const principle = lesson.propositions[0]?.textFa ?? lesson.axiomFa;

  if (!hit && session.attempts < 1) {
    messages.push(
      msg(
        "coach",
        session.phase,
        `هنوز به واژه‌های کلیدی کتاب نرسیده‌ای. یک سرنخ: ${principle} حالا با کلمات خودت بگو کدام بخش این جمله مرز درستی و نادرستی را می‌سازد؟`,
        ["قید جمله مهم است", "نقش آنزیم‌ها مهم است"],
        at + 1,
      ),
    );
    return { ...session, messages, attempts: session.attempts + 1 };
  }

  const phaseIndex = PHASE_ORDER.indexOf(session.phase);
  const nextPhase = PHASE_ORDER[Math.min(phaseIndex + 1, PHASE_ORDER.length - 1)];

  const transition: Record<HarnessPhase, string> = {
    measure: `خوب است. سنجش انجام شد؛ اکنون برنامه را می‌چینم: از اصل بدیهی شروع می‌کنیم، بعد قید تصمیم‌ساز و در پایان تلهٔ طراح. اصل بدیهی: ${lesson.axiomFa}`,
    plan: `برنامه مشخص است: ۱) فهم ساختار ۲) قید و کلیدواژه ۳) شکار تله. حالا آموزش: ${lesson.propositions.map((p) => p.textFa).join(" ")}`,
    teach: `درس را جمع‌بندی می‌کنم: ${lesson.recapFa.join(" ")} حالا نوبت تمرین است.`,
    practice: `تمرین خوبی بود. برای تثبیت، همین مفهوم را در کارت مرور فردا خواهی دید. اگر آماده‌ای، درس بعدی را از نقشهٔ مسیر باز کن.`,
  };

  messages.push(msg("coach", nextPhase, transition[session.phase], undefined, at + 2));

  if (nextPhase === "practice") {
    const q = lesson.questions[0];
    if (q) {
      messages.push(
        msg(
          "coach",
          "practice",
          `تمرین: ${q.stemFa}`,
          q.options.map((o, i) => `${["الف", "ب", "ج", "د"][i]}) ${o.textFa}`),
          at + 3,
        ),
      );
    }
  }

  return { ...session, phase: nextPhase, messages, attempts: 0 };
}

export function harnessSuggestions(lesson: Lesson): string[] {
  return [
    `این درس در کنکور چطور تله می‌سازد؟`,
    `قید تصمیم‌ساز «${lesson.propositions[0]?.quantifierFa ?? "همه"}» را توضیح بده`,
    `یک مثال از ${lesson.titleFa} بزن`,
    `تفاوت مکانیک این درس با درس قبلی چیست؟`,
  ];
}
