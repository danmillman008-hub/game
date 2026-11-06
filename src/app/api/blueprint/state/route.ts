import { NextResponse } from "next/server";
import { getBlueprintState } from "@/server/blueprint-store";
import { MASTER_AUTONOMOUS_AGENT_PROMPT } from "@/lib/phases-playbook-data";
import {
  REPO_BRANCHES_AND_ARCHIVES,
  FRANKENSTEIN_ROOT_CAUSES,
  EXTERNAL_REPOS_AND_TOOLS,
  STACK_ARCHITECTURE_DECISION_MATRIX,
  DEAD_ENDS_AND_ANTI_DRIFT_GUARDRAILS,
} from "@/lib/repo-forensics-data";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const state = getBlueprintState();
    return NextResponse.json({
      ...state,
      masterPrompt: MASTER_AUTONOMOUS_AGENT_PROMPT,
      forensics: {
        branchesAndArchives: REPO_BRANCHES_AND_ARCHIVES,
        rootCauses: FRANKENSTEIN_ROOT_CAUSES,
        externalRepos: EXTERNAL_REPOS_AND_TOOLS,
        stackMatrix: STACK_ARCHITECTURE_DECISION_MATRIX,
        deadEnds: DEAD_ENDS_AND_ANTI_DRIFT_GUARDRAILS,
      },
    });
  } catch (error) {
    console.error("Failed to load blueprint state:", error);
    return NextResponse.json(
      { error: "خطا در بارگذاری وضعیت نقشهٔ جامع" },
      { status: 500 },
    );
  }
}
