import { NextResponse } from "next/server";
import { getBlueprintState, updatePhase } from "@/server/blueprint-store";

export async function PATCH(request: Request) {
  try {
    const body = (await request.json()) as {
      phaseNumber?: number;
      status?: string;
      toggleDeliverableId?: string;
      notes?: string;
    };

    if (typeof body.phaseNumber !== "number") {
      return NextResponse.json({ error: "شمارهٔ فاز الزامی است" }, { status: 400 });
    }

    const result = updatePhase({
      phaseNumber: body.phaseNumber,
      status: body.status,
      toggleDeliverableId: body.toggleDeliverableId,
      notes: body.notes,
    });

    if (!result.ok) {
      return NextResponse.json({ error: result.error ?? "فاز یافت نشد" }, { status: 404 });
    }

    return NextResponse.json(getBlueprintState());
  } catch (error) {
    console.error("Failed to update phase:", error);
    return NextResponse.json({ error: "خطا در به‌روزرسانی وضعیت فاز" }, { status: 500 });
  }
}
