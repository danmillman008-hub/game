import { NextResponse } from "next/server";
import { getCurriculum } from "@/core/content";
import {
  advanceHarness,
  createHarnessSession,
  type HarnessSession,
} from "@/core/harness/engine";

export const dynamic = "force-dynamic";

interface HarnessRequest {
  lessonId?: string;
  message?: string;
  phase?: HarnessSession["phase"];
  history?: { role: "coach" | "learner"; textFa: string }[];
}

/**
 * LearnHarness gateway.
 * - Offline: deterministic LocalContentProvider grounded in the book proposition graph.
 * - Online: optional server-side LLM proxy (key stays in process.env, never shipped to the client).
 */
export async function POST(request: Request) {
  const body = (await request.json().catch(() => ({}))) as HarnessRequest;
  const curriculum = getCurriculum();
  const lesson = body.lessonId ? curriculum.lessonById.get(body.lessonId) : curriculum.lessons[0];

  if (!lesson) {
    return NextResponse.json({ error: "درس یافت نشد" }, { status: 404 });
  }

  const hasKey = Boolean(process.env.OPENAI_API_KEY);
  const provider: HarnessSession["provider"] = hasKey ? "online" : "offline";

  if (!body.message?.trim()) {
    const session = createHarnessSession(lesson, provider);
    return NextResponse.json({
      provider,
      phase: session.phase,
      messages: session.messages,
      lessonId: lesson.id,
    });
  }

  const session: HarnessSession = {
    lessonId: lesson.id,
    phase: body.phase ?? "measure",
    messages: [],
    attempts: 0,
    provider,
  };
  const offline = advanceHarness(session, body.message, lesson);
  const lastCoach = [...offline.messages].reverse().find((message) => message.role === "coach");

  if (provider === "online") {
    try {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 9000);
      const response = await fetch("https://api.openai.com/v1/chat/completions", {
        method: "POST",
        signal: controller.signal,
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
        },
        body: JSON.stringify({
          model: process.env.OPENAI_MODEL ?? "gpt-4o-mini",
          temperature: 0.4,
          messages: [
            {
              role: "system",
              content: `تو مربی LearnHarness برای درس «${lesson.titleFa}» هستی. فقط از گزاره‌های زیر استفاده کن و هرگز محتوای تازه نساز:\n${lesson.propositions
                .map((proposition) => `- ${proposition.textFa}`)
                .join("\n")}\nتلهٔ طراح: ${lesson.trapFa}\nفاز: ${offline.phase}. پاسخ کوتاه فارسی بده.`,
            },
            ...(body.history ?? []).slice(-6).map((item) => ({
              role: item.role === "coach" ? ("assistant" as const) : ("user" as const),
              content: item.textFa,
            })),
            { role: "user", content: body.message },
          ],
        }),
      });
      clearTimeout(timeout);

      if (response.ok) {
        const data = (await response.json()) as {
          choices?: { message?: { content?: string } }[];
        };
        const text = data.choices?.[0]?.message?.content?.trim();
        if (text) {
          return NextResponse.json({
            provider: "online",
            phase: offline.phase,
            messages: [{ id: "online-reply", role: "coach", phase: offline.phase, textFa: text, at: Date.now() }],
            lessonId: lesson.id,
          });
        }
      }
    } catch (error) {
      console.error("Harness online provider failed, falling back to local provider:", error);
    }
  }

  return NextResponse.json({
    provider: "offline",
    phase: offline.phase,
    messages: lastCoach ? [lastCoach] : [],
    lessonId: lesson.id,
  });
}
