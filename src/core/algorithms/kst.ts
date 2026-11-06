import type { Curriculum, Skill } from "@/core/types";

export interface KnowledgeGraph {
  nodes: Map<string, Skill>;
  prereqs: Map<string, string[]>;
  closure: Map<string, Set<string>>;
  roots: string[];
  topologicalOrder: string[];
}

/**
 * Knowledge Space Theory — prerequisite graph with transitive closure.
 * `surmise` edges (implied by transitivity) are removed automatically,
 * mirroring the Gramophone `surmise.py` step.
 */
export function buildKnowledgeGraph(curriculum: Curriculum): KnowledgeGraph {
  const nodes = new Map<string, Skill>();
  const prereqs = new Map<string, string[]>();

  for (const lesson of curriculum.lessons) {
    for (const skill of lesson.skills) {
      nodes.set(skill.id, skill);
      prereqs.set(skill.id, skill.dependsOn.filter((d) => curriculum.skillById.has(d)));
    }
  }

  // Reject cycles (a cycle makes outer-fringe computation meaningless).
  const state = new Map<string, 0 | 1 | 2>();
  const topologicalOrder: string[] = [];
  const visit = (id: string, path: string[]): void => {
    const current = state.get(id) ?? 0;
    if (current === 1) {
      throw new Error(`چرخه در گراف پیش‌نیاز: ${[...path, id].join(" → ")}`);
    }
    if (current === 2) return;
    state.set(id, 1);
    for (const dep of prereqs.get(id) ?? []) visit(dep, [...path, id]);
    state.set(id, 2);
    topologicalOrder.push(id);
  };
  for (const id of nodes.keys()) visit(id, []);

  const closure = new Map<string, Set<string>>();
  for (const id of nodes.keys()) {
    const seen = new Set<string>();
    const stack = [...(prereqs.get(id) ?? [])];
    while (stack.length) {
      const next = stack.pop() as string;
      if (seen.has(next)) continue;
      seen.add(next);
      stack.push(...(prereqs.get(next) ?? []));
    }
    closure.set(id, seen);
  }

  const roots = [...nodes.keys()].filter((id) => (prereqs.get(id) ?? []).length === 0);
  return { nodes, prereqs, closure, roots, topologicalOrder };
}

export const MASTERY_THRESHOLD = 0.6;

export function isMastered(mastery: Record<string, number>, skillId: string, threshold = MASTERY_THRESHOLD): boolean {
  return (mastery[skillId] ?? 0) >= threshold;
}

/** Skills whose entire prerequisite closure is mastered, but which are not yet mastered. */
export function outerFringe(
  graph: KnowledgeGraph,
  mastery: Record<string, number>,
  threshold = MASTERY_THRESHOLD,
): string[] {
  const fringe: string[] = [];
  for (const id of graph.topologicalOrder) {
    if (isMastered(mastery, id, threshold)) continue;
    const deps = graph.prereqs.get(id) ?? [];
    if (deps.every((dep) => isMastered(mastery, dep, threshold))) fringe.push(id);
  }
  return fringe;
}

/** Mastered skills that still have unmastered dependants: the natural review set. */
export function innerFringe(
  graph: KnowledgeGraph,
  mastery: Record<string, number>,
  threshold = MASTERY_THRESHOLD,
): string[] {
  return graph.topologicalOrder.filter((id) => {
    if (!isMastered(mastery, id, threshold)) return false;
    return [...graph.nodes.values()].some(
      (skill) => (skill.dependsOn ?? []).includes(id) && !isMastered(mastery, skill.id, threshold),
    );
  });
}

/** Skills that are unlocked right now, regardless of mastery (used for the path map). */
export function unlockedSkills(
  graph: KnowledgeGraph,
  mastery: Record<string, number>,
  threshold = MASTERY_THRESHOLD,
): Set<string> {
  return new Set([...outerFringe(graph, mastery, threshold), ...innerFringe(graph, mastery, threshold)]);
}

export interface NextSkillChoice {
  skillId: string | null;
  reasonFa: string;
  priority: number;
}

/**
 * Adaptive next-step selection: outer fringe first, then weakest mastered skill
 * (spaced review) — biased by the observed flow band accuracy.
 */
export function selectNextSkill(
  graph: KnowledgeGraph,
  mastery: Record<string, number>,
  recentAccuracy: number,
  threshold = MASTERY_THRESHOLD,
): NextSkillChoice {
  const fringe = outerFringe(graph, mastery, threshold);
  if (fringe.length > 0) {
    // Keep the flow band inside 70–85%: teach the easiest unlocked skill when struggling,
    // and the least-known skill when the learner is coasting.
    const scored = fringe
      .map((id) => ({ id, p: mastery[id] ?? 0 }))
      .sort((a, b) => (recentAccuracy < 0.7 ? b.p - a.p : a.p - b.p));
    return {
      skillId: scored[0].id,
      reasonFa:
        recentAccuracy < 0.7
          ? "برای برگشتن به باند جریان، آسان‌ترین مهارت آزادشده را تمرین کن."
          : "مهارت بعدی در حاشیهٔ بیرونی دانش تو آزاد شده است.",
      priority: 1,
    };
  }

  const review = innerFringe(graph, mastery, threshold);
  if (review.length > 0) {
    const weakest = review.sort((a, b) => (mastery[a] ?? 0) - (mastery[b] ?? 0))[0];
    return {
      skillId: weakest,
      reasonFa: "همهٔ مهارت‌های جدید قفل‌اند؛ ضعیف‌ترین مهارت تسلط‌یافته را مرور کن تا قفل بعدی باز شود.",
      priority: 2,
    };
  }

  const all = [...graph.nodes.keys()];
  if (all.length === 0) return { skillId: null, reasonFa: "گراف دانش خالی است.", priority: 3 };
  const lowest = all.sort((a, b) => (mastery[a] ?? 0) - (mastery[b] ?? 0))[0];
  return { skillId: lowest, reasonFa: "همهٔ مهارت‌ها تسلط یافته‌اند؛ برای نگهداری، مرور دوره‌ای لازم است.", priority: 3 };
}

/** Approximate size of the knowledge space (capped to avoid exponential blow-up). */
export function knowledgeSpaceSize(graph: KnowledgeGraph, cap = 100000): number {
  const order = graph.topologicalOrder;
  const index = new Map(order.map((id, i) => [id, i]));
  let count = 1;
  for (const id of order) {
    const deps = graph.prereqs.get(id) ?? [];
    const maxDepIndex = deps.reduce((max, dep) => Math.max(max, index.get(dep) ?? -1), -1);
    if (maxDepIndex < 0) {
      count *= 2;
      if (count > cap) return cap;
    }
  }
  return Math.min(count, cap);
}
