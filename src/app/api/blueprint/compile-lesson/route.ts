import { NextResponse } from "next/server";
import { addCompiledLesson, getBlueprintState } from "@/server/blueprint-store";

export async function POST(request: Request) {
  try {
    const body = (await request.json()) as {
      chapterCode?: string;
      curriculumId?: number;
      subject?: string;
      grade?: string;
      topicTitle?: string;
      sourceRef?: string;
      rawOcrExcerpt?: string;
      unconditionalTruthAxiom?: string;
      motivatedDiscoveryHook?: string;
      designerTrap?: string;
    };

    if (!body.topicTitle?.trim() || !body.rawOcrExcerpt?.trim()) {
      return NextResponse.json(
        { error: "عنوان مبحث و متن منبع/کتاب درسی الزامی است." },
        { status: 400 },
      );
    }

    addCompiledLesson({
      chapterCode: body.chapterCode?.trim() || `KONKUR-${Math.floor(1000 + Math.random() * 8999)}`,
      curriculumId: Number(body.curriculumId) > 0 ? Number(body.curriculumId) : 120000 + Math.floor(Math.random() * 9000),
      subject: body.subject?.trim() || "زیست‌شناسی ۳ (دوازدهم تجربی)",
      grade: body.grade?.trim() || "دوازدهم",
      topicTitle: body.topicTitle.trim(),
      sourceRef: body.sourceRef?.trim() || "کتاب درسی کنکور · صفحهٔ تأییدشده · نگاشت قطعی curriculumId",
      rawOcrExcerpt: body.rawOcrExcerpt.trim(),
      unconditionalTruthAxiom: body.unconditionalTruthAxiom,
      motivatedDiscoveryHook: body.motivatedDiscoveryHook,
      designerTrap: body.designerTrap,
    });

    return NextResponse.json(getBlueprintState());
  } catch (error) {
    console.error("Failed to compile lesson:", error);
    return NextResponse.json({ error: "خطا در کامپایل متن کتاب به بستهٔ ساختاریافتهٔ میمو" }, { status: 500 });
  }
}
