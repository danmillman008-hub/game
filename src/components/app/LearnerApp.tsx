"use client";

import { useState } from "react";
import Link from "next/link";
import {
  BarChart3,
  Bot,
  Compass,
  Flame,
  KeyRound,
  Moon,
  Route,
  Sparkles,
  Sun,
  Target,
  User,
} from "lucide-react";
import { summarize } from "@/core/state/learner";
import { LearnerProvider, useLearner } from "@/state/LearnerProvider";
import { PathTab } from "@/components/app/PathTab";
import { PracticeTab } from "@/components/app/PracticeTab";
import { HarnessTab } from "@/components/app/HarnessTab";
import { StatsTab } from "@/components/app/StatsTab";
import { ProfileTab } from "@/components/app/ProfileTab";
import { LessonPlayer } from "@/components/app/LessonPlayer";
import { cx } from "@/components/ui/kit";

type TabId = "learn" | "practice" | "harness" | "stats" | "profile";

const TABS: { id: TabId; label: string; icon: React.ReactNode }[] = [
  { id: "learn", label: "یادگیری", icon: <Route size={20} /> },
  { id: "practice", label: "تمرین", icon: <Target size={20} /> },
  { id: "harness", label: "هوش مصنوعی", icon: <Bot size={20} /> },
  { id: "stats", label: "امتیازها", icon: <BarChart3 size={20} /> },
  { id: "profile", label: "پروفایل", icon: <User size={20} /> },
];

export function LearnerApp() {
  return (
    <LearnerProvider>
      <Shell />
    </LearnerProvider>
  );
}

function Shell() {
  const { state, curriculum, actions, hydrated } = useLearner();
  const [tab, setTab] = useState<TabId>("learn");
  const [activeLessonId, setActiveLessonId] = useState<string | null>(null);
  const summary = summarize(state, curriculum);
  const isNight = state.profile.theme === "night";

  return (
    <div className="min-h-dvh bg-[var(--bg-app)]">
      <div className="pointer-events-none fixed inset-0 bg-[radial-gradient(120%_60%_at_50%_-10%,rgba(126,75,222,0.10),transparent_70%)]" />

      <div className="relative mx-auto flex min-h-dvh w-full max-w-[640px] flex-col">
        <header className="sticky top-0 z-30 border-b border-[var(--line)] bg-[var(--bg-app)]/90 px-4 pb-2.5 pt-3 backdrop-blur-lg">
          <div className="flex items-center justify-between gap-2">
            <div className="flex items-center gap-2">
              <div className="flex h-9 w-9 items-center justify-center rounded-2xl bg-[var(--mimo-button)] text-white shadow-[0_8px_18px_rgba(126,75,222,0.32)]">
                <Sparkles size={17} />
              </div>
              <div className="leading-tight">
                <div className="text-[13px] font-extrabold">کنکور-میمو</div>
                <div className="text-[9.5px] text-[var(--ink-faint)]">یادگیری تطبیقی × لرن‌هارنس</div>
              </div>
            </div>

            <div className="flex items-center gap-1.5">
              <ChipButton icon={<CoinsIcon />} value={summary.coins} tone="warning" title="سکه" />
              <ChipButton icon={<KeyRound size={12} />} value="∞" tone="purple" title="کلید نامحدود" />
              <ChipButton icon={<Flame size={12} />} value={summary.streak} tone="danger" title="استریک روزانه" />
              <button
                onClick={() => actions.setTheme(isNight ? "day" : "night")}
                aria-label="تغییر پوسته"
                className="rounded-full bg-[var(--surface)] p-2 text-[var(--ink-soft)] shadow-sm"
              >
                {isNight ? <Sun size={14} /> : <Moon size={14} />}
              </button>
              <Link
                href="/blueprint"
                aria-label="کنسول نقشهٔ راه"
                title="کنسول نقشهٔ راه"
                className="hidden rounded-full bg-[var(--surface)] p-2 text-[var(--ink-soft)] shadow-sm sm:block"
              >
                <Compass size={14} />
              </Link>
            </div>
          </div>
        </header>

        <main className="relative flex-1 px-4 pb-28 pt-4">
          {!hydrated ? (
            <div className="space-y-3">
              <div className="h-24 animate-pulse rounded-[var(--radius-card)] bg-[var(--surface-2)]" />
              <div className="h-40 animate-pulse rounded-[var(--radius-card)] bg-[var(--surface-2)]" />
              <div className="h-64 animate-pulse rounded-[var(--radius-card)] bg-[var(--surface-2)]" />
            </div>
          ) : (
            <div key={tab} className="animate-rise">
              {tab === "learn" && <PathTab onStartLesson={setActiveLessonId} />}
              {tab === "practice" && <PracticeTab />}
              {tab === "harness" && <HarnessTab />}
              {tab === "stats" && <StatsTab onStartLesson={setActiveLessonId} />}
              {tab === "profile" && <ProfileTab />}
            </div>
          )}
        </main>

        <nav className="fixed bottom-0 left-1/2 z-30 w-full max-w-[640px] -translate-x-1/2 border-t border-[var(--line)] bg-[var(--surface)]/95 px-2 pb-[max(8px,env(safe-area-inset-bottom))] pt-1.5 backdrop-blur-xl">
          <div className="flex items-stretch justify-around">
            {TABS.map((item) => {
              const active = item.id === tab;
              return (
                <button
                  key={item.id}
                  onClick={() => setTab(item.id)}
                  className={cx(
                    "relative flex flex-1 flex-col items-center gap-1 rounded-2xl px-1 py-1.5 transition",
                    active ? "text-[var(--mimo-button)]" : "text-[var(--ink-faint)]",
                  )}
                >
                  {active && <span className="absolute inset-x-3 top-0 h-0.5 rounded-full bg-[var(--mimo-button)]" />}
                  <span className={cx("transition-transform", active && "scale-110")}>{item.icon}</span>
                  <span className="text-[9.5px] font-bold">{item.label}</span>
                  {item.id === "practice" && summary.dueReviews > 0 && (
                    <span className="absolute right-3 top-0.5 flex h-4 min-w-4 items-center justify-center rounded-full bg-[var(--danger)] px-1 text-[8.5px] font-bold text-white">
                      {summary.dueReviews}
                    </span>
                  )}
                </button>
              );
            })}
          </div>
        </nav>

      </div>

      {activeLessonId && (
        <LessonPlayer
          key={activeLessonId}
          lessonId={activeLessonId}
          onClose={() => setActiveLessonId(null)}
          onNextLesson={(id) => setActiveLessonId(id)}
        />
      )}
    </div>
  );
}

function CoinsIcon() {
  return <span className="text-[11px] leading-none">🪙</span>;
}

function ChipButton({
  icon,
  value,
  tone,
  title,
}: {
  icon: React.ReactNode;
  value: string | number;
  tone: "warning" | "purple" | "danger";
  title: string;
}) {
  const tones = {
    warning: "text-[#B7791F]",
    purple: "text-[var(--mimo-button)]",
    danger: "text-[var(--danger)]",
  } as const;

  return (
    <span
      title={title}
      className="tabular flex items-center gap-1 rounded-full bg-[var(--surface)] px-2 py-1.5 text-[11px] font-extrabold shadow-sm"
    >
      <span className={tones[tone]}>{icon}</span>
      {value}
    </span>
  );
}
