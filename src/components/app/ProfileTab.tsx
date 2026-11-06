"use client";

import { useRef, useState } from "react";
import Link from "next/link";
import {
  CalendarDays,
  Check,
  Compass,
  Download,
  GraduationCap,
  Info,
  Moon,
  RotateCcw,
  Sun,
  Trash2,
  Upload,
  User,
} from "lucide-react";
import { curriculumStats } from "@/core/content";
import { DAY_MS } from "@/core/algorithms/fsrs";
import { summarize } from "@/core/state/learner";
import { useLearner } from "@/state/LearnerProvider";
import { Button, Card, Chip, Field, Modal, Progress, SectionTitle, cx, inputClass } from "@/components/ui/kit";

export function ProfileTab() {
  const { state, curriculum, actions } = useLearner();
  const summary = summarize(state, curriculum);
  const fileRef = useRef<HTMLInputElement | null>(null);
  const [message, setMessage] = useState<{ tone: "success" | "danger"; text: string } | null>(null);
  const [confirmReset, setConfirmReset] = useState(false);
  const stats = curriculumStats();
  const examDays = Math.max(0, Math.ceil((new Date(state.profile.examDate).getTime() - Date.now()) / DAY_MS));

  const exportData = () => {
    const blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `konkur-mimo-backup-${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="space-y-4">
      <Card className="relative overflow-hidden p-4">
        <div className="mimo-dot-grid pointer-events-none absolute inset-0 opacity-50" />
        <div className="relative flex items-center gap-3">
          <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-[var(--mimo-soft)] text-[var(--mimo-button)]">
            <User size={26} />
          </div>
          <div className="min-w-0 flex-1">
            <h2 className="truncate text-[16px] font-extrabold">{state.profile.name}</h2>
            <p className="text-[11px] text-[var(--ink-faint)]">
              {state.profile.grade} · رشتهٔ {state.profile.major}
            </p>
            <div className="mt-1.5 flex flex-wrap gap-1.5">
              <Chip tone="purple">سطح {Math.max(1, Math.floor(state.wallet.xp / 250) + 1)}</Chip>
              <Chip tone="success" icon={<CalendarDays size={10} />}>
                {examDays} روز تا کنکور
              </Chip>
            </div>
          </div>
        </div>
        <div className="relative mt-3">
          <div className="mb-1 flex items-center justify-between text-[10px] text-[var(--ink-faint)]">
            <span>پیشرفت سطح</span>
            <span className="tabular">{state.wallet.xp % 250} / 250 XP</span>
          </div>
          <Progress value={((state.wallet.xp % 250) / 250) * 100} height={5} />
        </div>
      </Card>

      <Card className="space-y-3 p-4">
        <SectionTitle title="مشخصات" eyebrow="تنظیمات" />
        <Field label="نام نمایشی">
          <input
            className={inputClass}
            value={state.profile.name}
            onChange={(event) => actions.setProfile({ name: event.target.value })}
          />
        </Field>
        <div className="grid grid-cols-2 gap-2">
          <Field label="پایه">
            <select
              className={inputClass}
              value={state.profile.grade}
              onChange={(event) => actions.setProfile({ grade: event.target.value })}
            >
              {["دهم", "یازدهم", "دوازدهم", "فارغ‌التحصیل"].map((grade) => (
                <option key={grade} value={grade}>
                  {grade}
                </option>
              ))}
            </select>
          </Field>
          <Field label="رشته">
            <select
              className={inputClass}
              value={state.profile.major}
              onChange={(event) => actions.setProfile({ major: event.target.value })}
            >
              {["تجربی", "ریاضی", "انسانی", "فنی‌وحرفه‌ای"].map((major) => (
                <option key={major} value={major}>
                  {major}
                </option>
              ))}
            </select>
          </Field>
        </div>
        <div className="grid grid-cols-2 gap-2">
          <Field label="تاریخ کنکور">
            <input
              type="date"
              className={inputClass}
              value={state.profile.examDate}
              onChange={(event) => actions.setProfile({ examDate: event.target.value })}
            />
          </Field>
          <Field label="هدف روزانه (دقیقه)">
            <input
              type="number"
              min={10}
              max={300}
              className={inputClass}
              value={state.profile.dailyGoalMin}
              onChange={(event) => actions.setProfile({ dailyGoalMin: Number(event.target.value) || 45 })}
            />
          </Field>
        </div>

        <div>
          <span className="mb-1.5 block text-[12px] font-bold text-[var(--ink-soft)]">پوسته</span>
          <div className="grid grid-cols-2 gap-2">
            {[
              { id: "day" as const, label: "روز", icon: <Sun size={14} /> },
              { id: "night" as const, label: "شب", icon: <Moon size={14} /> },
            ].map((theme) => (
              <button
                key={theme.id}
                onClick={() => actions.setTheme(theme.id)}
                className={cx(
                  "flex items-center justify-center gap-1.5 rounded-xl border px-3 py-2.5 text-[12px] font-bold transition",
                  state.profile.theme === theme.id
                    ? "border-[var(--mimo-progress)] bg-[var(--mimo-soft)] text-[var(--mimo-button)]"
                    : "border-[var(--line)] text-[var(--ink-soft)]",
                )}
              >
                {theme.icon} {theme.label}
              </button>
            ))}
          </div>
        </div>
      </Card>

      <Card className="p-4">
        <SectionTitle title="گزارش یادگیری من" eyebrow="امتیازها" />
        <div className="grid grid-cols-2 gap-2 text-[11px]">
          {[
            ["درس تکمیل‌شده", `${summary.completedLessons} / ${summary.totalLessons}`],
            ["مهارت مسلط", `${summary.masteredSkills} / ${summary.totalSkills}`],
            ["تلاش ثبت‌شده", String(summary.totalAttempts)],
            ["کارت مرور", String(state.reviewCards.length)],
            ["دقت مستقل", `${Math.round(summary.unaidedAccuracy * 100)}٪`],
            ["زمان تمرین", `${summary.minutesPracticed} دقیقه`],
          ].map(([label, value]) => (
            <div key={label} className="flex items-center justify-between rounded-xl bg-[var(--surface-2)] px-2.5 py-2">
              <span className="text-[var(--ink-faint)]">{label}</span>
              <span className="tabular font-bold">{value}</span>
            </div>
          ))}
        </div>
      </Card>

      <Card className="space-y-2 p-4">
        <SectionTitle title="پشتیبان‌گیری و بازنشانی" eyebrow="دادهٔ محلی" />
        <p className="text-[11px] leading-5 text-[var(--ink-soft)]">
          همهٔ دادهٔ یادگیری روی همین دستگاه (localStorage) ذخیره می‌شود. برای انتقال به دستگاه دیگر، فایل پشتیبان بگیر.
        </p>
        <div className="grid grid-cols-2 gap-2">
          <Button variant="outline" onClick={exportData}>
            <Download size={14} /> خروجی JSON
          </Button>
          <Button variant="outline" onClick={() => fileRef.current?.click()}>
            <Upload size={14} /> بازیابی
          </Button>
        </div>
        <input
          ref={fileRef}
          type="file"
          accept="application/json"
          className="hidden"
          onChange={async (event) => {
            const file = event.target.files?.[0];
            if (!file) return;
            const text = await file.text();
            const result = actions.importState(text);
            setMessage({ tone: result.ok ? "success" : "danger", text: result.messageFa });
            event.target.value = "";
          }}
        />
        {message && (
          <div
            className={cx(
              "rounded-xl px-3 py-2 text-[11px] font-semibold",
              message.tone === "success"
                ? "bg-[var(--success-soft)] text-[var(--success)]"
                : "bg-[var(--danger-soft)] text-[var(--danger)]",
            )}
          >
            {message.text}
          </div>
        )}
        <Button variant="danger" full onClick={() => setConfirmReset(true)}>
          <Trash2 size={14} /> بازنشانی کامل پیشرفت
        </Button>
      </Card>

      <Card className="space-y-2 p-4">
        <SectionTitle title="دربارهٔ این نسخه" eyebrow="معماری" />
        <div className="flex flex-wrap gap-1.5">
          <Chip tone="success" icon={<Check size={10} />}>
            {stats.lessons} درس · {stats.questions} تست
          </Chip>
          <Chip tone="purple">Mimo 9.35 DSL</Chip>
          <Chip tone="purple">KST + BKT + FSRS-5</Chip>
          <Chip tone="neutral">گاردریل {stats.guardrailPassed}/{stats.guardrailTotal}</Chip>
        </div>
        <p className="text-[11px] leading-5 text-[var(--ink-soft)]">
          این نسخه از پلتفرم، بر پایهٔ نقشهٔ راه جامع (فازهای ۰ تا ۱۱) ساخته شده است: هستهٔ خالص دامنه بدون DOM،
          پوستهٔ فارسی، و ذخیره‌سازی محلی. هیچ متن دموی چیدمان یا سؤال تصادفی هش‌پایه در محتوا وجود ندارد؛ هر بلوک
          به منبع کتاب و گاردریل M1–M10 گره خورده است.
        </p>
        <div className="grid gap-2">
          <Link
            href="/blueprint"
            className="flex items-center justify-between rounded-xl border border-[var(--line)] px-3 py-2.5 text-[12px] font-bold text-[var(--ink)] transition hover:bg-[var(--surface-2)]"
          >
            <span className="flex items-center gap-2">
              <Compass size={15} className="text-[var(--mimo-button)]" />
              کنسول نقشهٔ راه و استودیوی DSL
            </span>
            <span className="text-[10px] text-[var(--ink-faint)">۱۲ فاز</span>
          </Link>
          <a
            href="/api/health"
            className="flex items-center justify-between rounded-xl border border-[var(--line)] px-3 py-2.5 text-[12px] font-bold text-[var(--ink)] transition hover:bg-[var(--surface-2)]"
          >
            <span className="flex items-center gap-2">
              <Info size={15} className="text-[var(--success)]" />
              بررسی سلامت موتور
            </span>
            <span className="font-mono-code text-[10px] text-[var(--ink-faint)]">/api/health</span>
          </a>
        </div>
        <div className="flex items-start gap-2 rounded-xl bg-[var(--surface-2)] p-2.5 text-[10px] leading-5 text-[var(--ink-faint)]">
          <GraduationCap size={14} className="mt-0.5 shrink-0" />
          داده‌های نمونه از کتاب‌های درسی دوازدهم تهیه شده و برای نمایش قابلیت‌های موتور است؛ مرجع نهایی، کتاب درسی است.
        </div>
      </Card>

      <Modal
        open={confirmReset}
        onClose={() => setConfirmReset(false)}
        title="بازنشانی کامل پیشرفت"
        subtitle="همهٔ تلاش‌ها، مهارت‌ها، کارت‌های مرور و کارنامه پاک می‌شوند."
        footer={
          <div className="flex gap-2">
            <Button variant="outline" onClick={() => setConfirmReset(false)}>
              انصراف
            </Button>
            <Button
              variant="danger"
              full
              onClick={() => {
                actions.reset();
                setConfirmReset(false);
                setMessage({ tone: "success", text: "پیشرفت بازنشانی شد." });
              }}
            >
              <RotateCcw size={14} /> بازنشانی کن
            </Button>
          </div>
        }
      >
        <div className="space-y-2 text-[12px] leading-6 text-[var(--ink-soft)]">
          <p>قبل از بازنشانی، یک خروجی JSON بگیر تا بتوانی بعداً بازیابی کنی.</p>
          <p className="text-[11px] text-[var(--danger)]">این عمل قابل بازگشت نیست.</p>
        </div>
      </Modal>
    </div>
  );
}
