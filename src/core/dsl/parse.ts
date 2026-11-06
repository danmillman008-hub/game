/**
 * Mimo 9.35 lesson DSL — tolerant parser for the 27-tag grammar (`dsl_grammar.ebnf`).
 * Used by the compiler studio to prove every generated block is renderable,
 * and to evaluate the three-state `visible-if` gate.
 */

export const MIMO_DSL_TAGS = [
  "html",
  "body",
  "p",
  "h1",
  "h2",
  "h3",
  "strong",
  "em",
  "code",
  "content",
  "text",
  "interactions",
  "interaction",
  "options",
  "option",
  "selection",
  "item",
  "image",
  "video",
  "audio",
  "table",
  "tr",
  "td",
  "blank",
  "math",
  "diagram",
  "details",
] as const;

export type MimoTag = (typeof MIMO_DSL_TAGS)[number];

export interface DslNode {
  tag: string;
  attrs: Record<string, string>;
  children: DslNode[];
  text?: string;
}

export interface DslParseResult {
  root: DslNode | null;
  tags: Set<string>;
  errors: string[];
  blocks: number;
}

const VOID_TAGS = new Set(["blank", "image", "video", "audio"]);

export function parseDsl(source: string): DslParseResult {
  const errors: string[] = [];
  const tags = new Set<string>();
  const root: DslNode = { tag: "#root", attrs: {}, children: [] };
  const stack: DslNode[] = [root];

  const tokenRegex = /<\/?([a-zA-Z][\w-]*)((?:\s+[^<>]*?)?)\/?>|([^<]+)/g;
  let match: RegExpExecArray | null;
  let blocks = 0;

  while ((match = tokenRegex.exec(source)) !== null) {
    const [raw, tagName, rawAttrs, text] = match;
    if (text !== undefined) {
      const trimmed = text.trim();
      if (trimmed) {
        stack[stack.length - 1].text = `${stack[stack.length - 1].text ?? ""}${trimmed}`;
      }
      continue;
    }
    if (!tagName) continue;

    const tag = tagName.toLowerCase();
    tags.add(tag);
    if (!(MIMO_DSL_TAGS as readonly string[]).includes(tag)) {
      errors.push(`تگ ناشناخته در گرامر میمو: <${tag}>`);
    }
    if (tag === "code") blocks += 1;

    const isClosing = raw.startsWith("</");
    if (isClosing) {
      const top = stack[stack.length - 1];
      if (top.tag === tag) {
        stack.pop();
      } else {
        errors.push(`بستن نامنطبق </${tag}> در حالی که انتظار </${top.tag}> بود.`);
        const index = [...stack].reverse().findIndex((n) => n.tag === tag);
        if (index >= 0) stack.length = stack.length - index - 1;
      }
      continue;
    }

    const attrs: Record<string, string> = {};
    for (const attrMatch of (rawAttrs ?? "").matchAll(/([\w-]+)\s*=\s*"([^"]*)"/g)) {
      attrs[attrMatch[1]] = attrMatch[2];
    }

    const node: DslNode = { tag, attrs, children: [] };
    stack[stack.length - 1].children.push(node);
    if (!VOID_TAGS.has(tag) && !raw.endsWith("/>")) stack.push(node);
  }

  if (stack.length !== 1) {
    errors.push(`تگ‌های بسته‌نشده: ${stack.slice(1).map((n) => `<${n.tag}>`).join(", ")}`);
  }

  const html = root.children.find((child) => child.tag === "html");
  if (!html && tags.size > 0) errors.push("پوستهٔ <html> یافت نشد.");

  return { root: html ?? root, tags, errors, blocks };
}

export type VisibleIfState = "always" | "correct" | "wrong" | "partial" | "hint";

export function visibleNodes(node: DslNode | null, state: VisibleIfState): DslNode[] {
  if (!node) return [];
  const result: DslNode[] = [];
  for (const child of node.children) {
    const gate = child.attrs["visible-if"] ?? "always";
    if (gate === "always" || gate === state) result.push(child);
    result.push(...visibleNodes(child, state));
  }
  return result;
}

export function dslToText(node: DslNode | null): string {
  if (!node) return "";
  const own = node.text ?? "";
  return [own, ...node.children.map((child) => dslToText(child))].filter(Boolean).join(" ");
}
