import { describe, expect, it } from "vitest";
import { getCurriculum, curriculumStats, lessonsOfChapter } from "@/core/content";
import { buildKnowledgeGraph, outerFringe, selectNextSkill, innerFringe } from "@/core/algorithms/kst";
import { parseDsl, visibleNodes } from "@/core/dsl/parse";

const curriculum = getCurriculum();

describe("compiled curriculum", () => {
  it("contains every subject, chapter and lesson", () => {
    const stats = curriculumStats();
    expect(stats.subjects).toBe(3);
    expect(stats.chapters).toBe(7);
    expect(stats.lessons).toBe(18);
    expect(stats.questions).toBeGreaterThanOrEqual(36);
    expect(stats.guardrailPassed).toBe(stats.guardrailTotal);
  });

  it("emits the exact six-role Mimo sequence for every lesson", () => {
    for (const lesson of curriculum.lessons) {
      expect(lesson.blocks.map((b) => b.role)).toEqual([
        "hook",
        "check",
        "feedback",
        "explain",
        "practice",
        "recap",
      ]);
      expect(lesson.reviewStatus).toBe("approved");
    }
  });

  it("keeps every generated DSL document parseable and inside the 27-tag grammar", () => {
    for (const lesson of curriculum.lessons) {
      const parsed = parseDsl(lesson.dslHtml);
      expect(parsed.errors, `${lesson.id}: ${parsed.errors.join(" | ")}`).toEqual([]);
      expect(parsed.blocks).toBeGreaterThanOrEqual(2);
    }
  });

  it("gates correct/wrong feedback through visible-if", () => {
    const lesson = curriculum.lessonById.get("BIO12-C1-L1");
    expect(lesson).toBeDefined();
    const checkBlock = lesson!.blocks.find((b) => b.role === "check")!;
    const parsed = parseDsl(checkBlock.dsl);
    const correctNodes = visibleNodes(parsed.root, "correct");
    const wrongNodes = visibleNodes(parsed.root, "wrong");
    expect(correctNodes.length).toBeGreaterThan(0);
    expect(wrongNodes.length).toBeGreaterThan(0);
    expect(correctNodes.map((n) => n.text).join(" ")).not.toEqual(wrongNodes.map((n) => n.text).join(" "));
  });

  it("links lessons into a chapter chain without hash-based mapping", () => {
    const lessons = lessonsOfChapter("BIO12-C1");
    expect(lessons.map((l) => l.id)).toEqual(["BIO12-C1-L1", "BIO12-C1-L2", "BIO12-C1-L3"]);
    expect(lessons[1].skills[0].dependsOn).toContain("BIO12-C1-L1.concept");
    expect(lessons[0].curriculumId).toBe(120101);
  });

  it("only has one correct option and an analysis for every option", () => {
    for (const question of curriculum.questions) {
      expect(question.options).toHaveLength(4);
      expect(question.options.filter((o) => o.correct)).toHaveLength(1);
      for (const option of question.options) expect(option.analysisFa.length).toBeGreaterThan(5);
    }
  });
});

describe("Knowledge Space Theory", () => {
  it("builds an acyclic graph and exposes the first outer fringe", () => {
    const graph = buildKnowledgeGraph(curriculum);
    expect(graph.topologicalOrder.length).toBe(curriculum.lessons.length * 2);
    expect(outerFringe(graph, {}).length).toBeGreaterThan(0);
  });

  it("only unlocks a skill when its whole prerequisite closure is mastered", () => {
    const graph = buildKnowledgeGraph(curriculum);
    const mastery = { "BIO12-C1-L1.concept": 0.9 };
    const fringe = outerFringe(graph, mastery);
    expect(fringe).toContain("BIO12-C1-L1.application");
    expect(fringe).toContain("BIO12-C1-L2.concept");
    expect(fringe).not.toContain("BIO12-C1-L2.application");
    expect(fringe).not.toContain("BIO12-C1-L3.concept");
  });

  it("keeps mastered-but-load-bearing skills in the inner fringe", () => {
    const graph = buildKnowledgeGraph(curriculum);
    const mastery = { "BIO12-C1-L1.concept": 0.9 };
    expect(innerFringe(graph, mastery)).toContain("BIO12-C1-L1.concept");
  });

  it("recommends the easiest unlocked skill when accuracy is below the flow band", () => {
    const graph = buildKnowledgeGraph(curriculum);
    const choice = selectNextSkill(graph, {}, 0.5);
    expect(choice.skillId).toBeTruthy();
    expect(choice.reasonFa).toContain("باند جریان");
  });
});
