import { NextResponse } from "next/server";
import { curriculumStats, getCurriculum } from "@/core/content";
import { buildKnowledgeGraph } from "@/core/algorithms/kst";
import { parseDsl } from "@/core/dsl/parse";

export const dynamic = "force-dynamic";

export async function GET() {
  const curriculum = getCurriculum();
  const stats = curriculumStats();
  const graph = buildKnowledgeGraph(curriculum);

  const dslFailures = curriculum.lessons.flatMap((lesson) => {
    const parsed = parseDsl(lesson.dslHtml);
    return parsed.errors.length > 0 ? [{ lessonId: lesson.id, errors: parsed.errors }] : [];
  });

  const checks = [
    { code: "CURRICULUM_LOADED", passed: stats.lessons > 0 && stats.questions > 0, detail: `${stats.lessons} درس، ${stats.questions} تست` },
    {
      code: "SIX_ROLE_SEQUENCE",
      passed: curriculum.lessons.every(
        (lesson) => lesson.blocks.map((b) => b.role).join(">") === "hook>check>feedback>explain>practice>recap",
      ),
      detail: "توالی شش‌نقشی در همهٔ دروس",
    },
    {
      code: "GUARDRAILS_M1_M10",
      passed: stats.guardrailPassed === stats.guardrailTotal,
      detail: `${stats.guardrailPassed}/${stats.guardrailTotal} گاردریل سبز`,
    },
    {
      code: "KNOWLEDGE_GRAPH_ACYCLIC",
      passed: graph.topologicalOrder.length === stats.lessons * 2,
      detail: `${graph.topologicalOrder.length} مهارت، بدون چرخه`,
    },
    { code: "DSL_AST_VALID", passed: dslFailures.length === 0, detail: dslFailures.length ? JSON.stringify(dslFailures) : "همهٔ اسناد DSL معتبر" },
    {
      code: "REVIEW_STATUS",
      passed: curriculum.lessons.every((lesson) => lesson.reviewStatus === "approved"),
      detail: "همهٔ دروس approved",
    },
  ];

  const healthy = checks.every((check) => check.passed);

  return NextResponse.json(
    {
      status: healthy ? "ok" : "degraded",
      engine: "konkur-mimo-core/1.0",
      stats,
      checks,
      generatedAt: new Date().toISOString(),
    },
    { status: healthy ? 200 : 500 },
  );
}
