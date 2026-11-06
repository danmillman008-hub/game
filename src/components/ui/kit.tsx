"use client";

import { useEffect, type ButtonHTMLAttributes, type ReactNode } from "react";
import { Star, X } from "lucide-react";

export function cx(...values: Array<string | false | null | undefined>): string {
  return values.filter(Boolean).join(" ");
}

export function Card({
  children,
  className,
  as = "div",
}: {
  children: ReactNode;
  className?: string;
  as?: "div" | "section" | "article";
}) {
  const Tag = as;
  return (
    <Tag className={cx("surface rounded-[var(--radius-card)]", className)}>{children}</Tag>
  );
}

type ButtonVariant = "primary" | "soft" | "ghost" | "outline" | "danger" | "success";
type ButtonSize = "sm" | "md" | "lg";

const BUTTON_VARIANTS: Record<ButtonVariant, string> = {
  primary:
    "bg-[var(--mimo-button)] text-white shadow-[0_10px_24px_rgba(126,75,222,0.28)] hover:bg-[var(--mimo-button-dark)] active:scale-[0.99]",
  soft: "bg-[var(--mimo-soft)] text-[var(--mimo-button)] hover:bg-[var(--mimo-soft)]/80",
  ghost: "bg-transparent text-[var(--ink-soft)] hover:bg-[var(--surface-2)]",
  outline: "border border-[var(--line)] bg-[var(--surface)] text-[var(--ink)] hover:bg-[var(--surface-2)]",
  danger: "bg-[var(--danger)] text-white hover:opacity-90",
  success: "bg-[var(--success)] text-white hover:opacity-90",
};

const BUTTON_SIZES: Record<ButtonSize, string> = {
  sm: "text-[12px] px-3 py-1.5 rounded-xl gap-1.5",
  md: "text-[13px] px-4 py-2.5 rounded-2xl gap-2",
  lg: "text-[15px] px-6 py-3.5 rounded-2xl gap-2",
};

export function Button({
  children,
  variant = "primary",
  size = "md",
  className,
  full,
  ...rest
}: ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: ButtonVariant;
  size?: ButtonSize;
  full?: boolean;
}) {
  return (
    <button
      {...rest}
      className={cx(
        "inline-flex items-center justify-center font-semibold transition-all disabled:cursor-not-allowed disabled:opacity-45",
        BUTTON_VARIANTS[variant],
        BUTTON_SIZES[size],
        full && "w-full",
        className,
      )}
    >
      {children}
    </button>
  );
}

export function Chip({
  children,
  icon,
  tone = "neutral",
  className,
  title,
}: {
  children: ReactNode;
  icon?: ReactNode;
  tone?: "neutral" | "purple" | "success" | "danger" | "warning";
  className?: string;
  title?: string;
}) {
  const tones = {
    neutral: "bg-[var(--surface-2)] text-[var(--ink-soft)]",
    purple: "bg-[var(--mimo-soft)] text-[var(--mimo-button)]",
    success: "bg-[var(--success-soft)] text-[var(--success)]",
    danger: "bg-[var(--danger-soft)] text-[var(--danger)]",
    warning: "bg-[var(--warning-soft)] text-[var(--warning)]",
  } as const;

  return (
    <span
      title={title}
      className={cx(
        "inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-[11.5px] font-semibold whitespace-nowrap",
        tones[tone],
        className,
      )}
    >
      {icon}
      {children}
    </span>
  );
}

export function Progress({
  value,
  height = 6,
  color = "var(--mimo-progress)",
  className,
}: {
  value: number;
  height?: number;
  color?: string;
  className?: string;
}) {
  const pct = Math.max(0, Math.min(100, value));
  return (
    <div
      className={cx("w-full overflow-hidden rounded-full bg-[var(--surface-3)]", className)}
      style={{ height }}
      role="progressbar"
      aria-valuenow={Math.round(pct)}
      aria-valuemin={0}
      aria-valuemax={100}
    >
      <div
        className="h-full rounded-full transition-all duration-500"
        style={{ width: `${pct}%`, background: color }}
      />
    </div>
  );
}

export function Ring({
  value,
  size = 92,
  stroke = 8,
  color = "var(--mimo-progress)",
  track = "var(--surface-3)",
  children,
}: {
  value: number;
  size?: number;
  stroke?: number;
  color?: string;
  track?: string;
  children?: ReactNode;
}) {
  const radius = (size - stroke) / 2;
  const circumference = 2 * Math.PI * radius;
  const pct = Math.max(0, Math.min(100, value));
  const dash = (pct / 100) * circumference;

  return (
    <div className="relative inline-flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        <circle cx={size / 2} cy={size / 2} r={radius} fill="none" stroke={track} strokeWidth={stroke} />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke={color}
          strokeWidth={stroke}
          strokeLinecap="round"
          strokeDasharray={`${dash} ${circumference - dash}`}
          className="transition-all duration-700"
        />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">{children}</div>
    </div>
  );
}

export function Modal({
  open,
  onClose,
  title,
  subtitle,
  children,
  footer,
  wide,
}: {
  open: boolean;
  onClose: () => void;
  title: string;
  subtitle?: string;
  children: ReactNode;
  footer?: ReactNode;
  wide?: boolean;
}) {
  useEffect(() => {
    if (!open) return;
    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") onClose();
    };
    window.addEventListener("keydown", onKey);
    const previous = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", onKey);
      document.body.style.overflow = previous;
    };
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center bg-[rgba(18,19,38,0.45)] p-0 backdrop-blur-sm sm:items-center sm:p-6">
      <div
        className={cx(
          "animate-rise surface flex max-h-[92vh] w-full flex-col overflow-hidden rounded-t-[26px] sm:rounded-[26px]",
          wide ? "sm:max-w-3xl" : "sm:max-w-lg",
        )}
        style={{ boxShadow: "var(--shadow-float)" }}
      >
        <div className="flex items-start justify-between gap-3 border-b border-[var(--line)] px-5 py-4">
          <div>
            <h3 className="text-[15px] font-extrabold">{title}</h3>
            {subtitle && <p className="mt-1 text-[12px] text-[var(--ink-faint)]">{subtitle}</p>}
          </div>
          <button
            onClick={onClose}
            aria-label="بستن"
            className="rounded-full bg-[var(--surface-2)] p-2 text-[var(--ink-soft)] transition hover:bg-[var(--surface-3)]"
          >
            <X size={16} />
          </button>
        </div>
        <div className="scrollbar-thin flex-1 overflow-y-auto px-5 py-4">{children}</div>
        {footer && <div className="border-t border-[var(--line)] bg-[var(--surface-2)] px-5 py-3">{footer}</div>}
      </div>
    </div>
  );
}

export function Stars({ count, size = 13 }: { count: number; size?: number }) {
  return (
    <span className="inline-flex items-center gap-0.5" aria-label={`${count} ستاره`}>
      {[0, 1, 2].map((index) => (
        <Star
          key={index}
          size={size}
          className={index < count ? "text-[var(--warning)]" : "text-[var(--ink-faint)] opacity-30"}
          fill={index < count ? "var(--warning)" : "transparent"}
        />
      ))}
    </span>
  );
}

export function Stat({
  label,
  value,
  suffix,
  icon,
  tone = "purple",
}: {
  label: string;
  value: string | number;
  suffix?: string;
  icon?: ReactNode;
  tone?: "purple" | "success" | "warning" | "danger" | "neutral";
}) {
  const tones = {
    purple: "bg-[var(--mimo-soft)] text-[var(--mimo-button)]",
    success: "bg-[var(--success-soft)] text-[var(--success)]",
    warning: "bg-[var(--warning-soft)] text-[var(--warning)]",
    danger: "bg-[var(--danger-soft)] text-[var(--danger)]",
    neutral: "bg-[var(--surface-2)] text-[var(--ink-soft)]",
  } as const;

  return (
    <Card className="p-3.5">
      <div className="flex items-center justify-between">
        <span className="text-[11.5px] font-semibold text-[var(--ink-faint)]">{label}</span>
        {icon && <span className={cx("rounded-xl p-1.5", tones[tone])}>{icon}</span>}
      </div>
      <div className="mt-2 flex items-baseline gap-1">
        <span className="tabular text-[22px] font-extrabold leading-none">{value}</span>
        {suffix && <span className="text-[11px] text-[var(--ink-faint)]">{suffix}</span>}
      </div>
    </Card>
  );
}

export function SectionTitle({
  eyebrow,
  title,
  action,
}: {
  eyebrow?: string;
  title: string;
  action?: ReactNode;
}) {
  return (
    <div className="mb-3 flex items-end justify-between gap-3">
      <div>
        {eyebrow && (
          <div className="mb-0.5 text-[10.5px] font-bold tracking-wide text-[var(--mimo-button)]">{eyebrow}</div>
        )}
        <h2 className="text-[15px] font-extrabold">{title}</h2>
      </div>
      {action}
    </div>
  );
}

export function Sparkline({ values, color = "var(--mimo-progress)" }: { values: number[]; color?: string }) {
  if (values.length === 0) return <div className="h-10 rounded-lg bg-[var(--surface-2)]" />;
  const width = 120;
  const height = 40;
  const max = Math.max(...values, 1);
  const min = Math.min(...values, 0);
  const points = values
    .map((value, index) => {
      const x = (index / Math.max(1, values.length - 1)) * width;
      const y = height - ((value - min) / Math.max(1, max - min)) * height;
      return `${x.toFixed(1)},${y.toFixed(1)}`;
    })
    .join(" ");

  return (
    <svg width={width} height={height} className="overflow-visible" aria-hidden>
      <polyline
        points={points}
        fill="none"
        stroke={color}
        strokeWidth={2.2}
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}

export function EmptyState({
  icon,
  title,
  hint,
  action,
}: {
  icon: ReactNode;
  title: string;
  hint: string;
  action?: ReactNode;
}) {
  return (
    <div className="flex flex-col items-center gap-2 rounded-[var(--radius-card)] border border-dashed border-[var(--line)] px-6 py-8 text-center">
      <div className="rounded-2xl bg-[var(--surface-2)] p-3 text-[var(--mimo-button)]">{icon}</div>
      <div className="text-[13.5px] font-bold">{title}</div>
      <p className="max-w-xs text-[12px] leading-6 text-[var(--ink-faint)]">{hint}</p>
      {action}
    </div>
  );
}

export function Field({
  label,
  hint,
  children,
}: {
  label: string;
  hint?: string;
  children: ReactNode;
}) {
  return (
    <label className="block">
      <span className="mb-1.5 block text-[12px] font-bold text-[var(--ink-soft)]">{label}</span>
      {children}
      {hint && <span className="mt-1 block text-[10.5px] text-[var(--ink-faint)]">{hint}</span>}
    </label>
  );
}

export const inputClass =
  "w-full rounded-xl border border-[var(--line)] bg-[var(--surface-2)] px-3 py-2.5 text-[13px] outline-none transition focus:border-[var(--mimo-progress)] focus:ring-2 focus:ring-[var(--mimo-soft)]";
