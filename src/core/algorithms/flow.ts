/**
 * Flow-band controller: keep the learner's rolling accuracy inside 70–85 %.
 * Too easy → raise difficulty; too hard → inject scaffolding and easier items.
 */

export const FLOW_BAND: [number, number] = [0.7, 0.85];

export interface FlowStatus {
  accuracy: number;
  samples: number;
  band: "too_easy" | "in_band" | "too_hard" | "unknown";
  labelFa: string;
  recommendationFa: string;
  difficultyBias: -1 | 0 | 1;
  showHints: boolean;
}

export function flowStatus(recentOutcomes: boolean[]): FlowStatus {
  if (recentOutcomes.length === 0) {
    return {
      accuracy: 0,
      samples: 0,
      band: "unknown",
      labelFa: "در حال کالیبراسیون",
      recommendationFa: "چند پاسخ دیگر لازم است تا کنترلر باند جریان فعال شود.",
      difficultyBias: 0,
      showHints: true,
    };
  }

  const recent = recentOutcomes.slice(-8);
  const accuracy = recent.filter(Boolean).length / recent.length;

  if (accuracy > FLOW_BAND[1]) {
    return {
      accuracy,
      samples: recent.length,
      band: "too_easy",
      labelFa: "بالاتر از باند جریان",
      recommendationFa: "سطح سخت‌تر و تست‌های ترکیبی‌تر فعال شد؛ راهنماها کم می‌شوند.",
      difficultyBias: 1,
      showHints: false,
    };
  }

  if (accuracy < FLOW_BAND[0]) {
    return {
      accuracy,
      samples: recent.length,
      band: "too_hard",
      labelFa: "پایین‌تر از باند جریان",
      recommendationFa: "یک پله عقب می‌رویم: راهنمای گام‌به‌گام و تست ساده‌تر فعال شد.",
      difficultyBias: -1,
      showHints: true,
    };
  }

  return {
    accuracy,
    samples: recent.length,
    band: "in_band",
    labelFa: "داخل باند جریان ۷۰–۸۵٪",
    recommendationFa: "سطح فعلی بهینه است؛ با همین چالش ادامه بده.",
    difficultyBias: 0,
    showHints: false,
  };
}

/** Weight used by the adaptive item selector. */
export function difficultyWeight(difficulty: 1 | 2 | 3, status: FlowStatus): number {
  const target = status.band === "too_hard" ? 1 : status.band === "too_easy" ? 3 : 2;
  return 1 / (1 + Math.abs(difficulty - target));
}
