// @vitest-environment jsdom
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { cleanup, render, screen, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { LearnerApp } from "@/components/app/LearnerApp";

vi.mock("next/link", () => ({
  default: ({ children, href, ...rest }: { children: React.ReactNode; href: string }) => (
    <a href={href} {...rest}>
      {children}
    </a>
  ),
}));

async function startFirstLesson(user: ReturnType<typeof userEvent.setup>) {
  const startButton = await screen.findByRole("button", { name: /ادامهٔ مسیر/ });
  await user.click(startButton);
  const dialog = await screen.findByText(/اصل بدیهی \(Principle i\)/);
  expect(dialog).toBeTruthy();
  await user.click(screen.getByRole("button", { name: /شروع درس|ادامهٔ درس/ }));
}

describe("learner app smoke flow", () => {
  beforeEach(() => {
    window.localStorage.clear();
  });

  afterEach(() => {
    cleanup();
  });

  it("renders the five-tab Persian shell", async () => {
    render(<LearnerApp />);
    expect(await screen.findByText("کنکور-میمو")).toBeTruthy();
    for (const label of ["یادگیری", "تمرین", "هوش مصنوعی", "امتیازها", "پروفایل"]) {
      expect(screen.getAllByText(label).length).toBeGreaterThan(0);
    }
    expect(await screen.findByText(/زیست‌شناسی ۳/)).toBeTruthy();
  });

  it("walks a full six-role lesson and persists progress", async () => {
    const user = userEvent.setup();
    render(<LearnerApp />);
    await startFirstLesson(user);

    // 1. hook
    expect(await screen.findByText(/اگر دو رشتهٔ دنا/)).toBeTruthy();
    await user.click(screen.getByRole("button", { name: /فهمیدم، ادامه بده/ }));

    // 2. guided cloze (deliberately wrong, then verify the correct answer is revealed)
    const input = await screen.findByPlaceholderText("…");
    await user.type(input, "هیدروژنی");
    await user.click(screen.getByRole("button", { name: "بررسی پاسخ" }));
    expect(await screen.findByText(/پاسخ کتاب:/)).toBeTruthy();
    expect(screen.getAllByText("فسفودی‌استر").length).toBeGreaterThan(0);
    await user.click(screen.getByRole("button", { name: "ادامه" }));

    // 3. trap detector
    expect(await screen.findByText(/کدام‌یک «تلهٔ طراح» است/)).toBeTruthy();
    await user.click(
      screen.getByRole("button", { name: /آنزیم هلیکاز با شکستن پیوند فسفودی‌استر/ }),
    );
    await user.click(screen.getByRole("button", { name: "شکار تله" }));
    expect(screen.getAllByText(/تله:|سالم:/).length).toBeGreaterThan(0);
    await user.click(screen.getByRole("button", { name: "ادامه" }));

    // 4. token assembly
    expect(await screen.findByText(/زنجیرهٔ تو/)).toBeTruthy();
    const tokens = ["دو رشتهٔ دنا", "با پیوند هیدروژنی", "بین بازهای مکمل", "در مقابل هم قرار می‌گیرند"];
    for (const token of tokens) {
      await user.click(screen.getByRole("button", { name: token }));
    }
    await user.click(screen.getByRole("button", { name: /بررسی چیدمان/ }));
    expect(await screen.findByText(/ترتیب کتاب/)).toBeTruthy();
    await user.click(screen.getByRole("button", { name: "ادامه" }));

    // 5. Konkur MCQ
    expect(await screen.findByText(/آنزیم هلیکاز در همانندسازی دنا کدام پیوند را می‌شکند/)).toBeTruthy();
    await user.click(screen.getByRole("button", { name: /پیوند هیدروژنی بین بازهای مکمل/ }));
    await user.click(screen.getByRole("button", { name: "ثبت پاسخ" }));
    expect(screen.getAllByText(/تلهٔ طراح/).length).toBeGreaterThan(0);
    await user.click(screen.getByRole("button", { name: "ادامه" }));

    // 6. recap + completion
    const finishButton = await screen.findByRole("button", { name: /پایان درس و ثبت پیشرفت/ });
    await user.click(finishButton);
    expect(await screen.findByText(/درس تکمیل شد!/)).toBeTruthy();
    await user.click(screen.getByRole("button", { name: /بازگشت به نقشه/ }));

    const stored = JSON.parse(window.localStorage.getItem("konkur-mimo:learner:v2") ?? "{}");
    expect(stored.lessons["BIO12-C1-L1"].completions).toBeGreaterThan(0);
    expect(stored.attempts.length).toBeGreaterThan(0);
    expect(stored.reviewCards.length).toBeGreaterThan(0);
  }, 30000);

  it("runs a practice exam and shows the answer key", async () => {
    const user = userEvent.setup();
    render(<LearnerApp />);
    await user.click(await screen.findByText("تمرین"));

    const bankMode = await screen.findByText("بانک تست");
    await user.click(bankMode);
    await user.click(screen.getByRole("button", { name: /شروع بانک تست/ }));

    expect(await screen.findByRole("button", { name: /بعدی/ })).toBeTruthy();
    const options = screen.getAllByRole("button").filter((button) => button.textContent?.length ?? 0 > 25);
    await user.click(options[0]);
    await user.click(screen.getByRole("button", { name: /بعدی/ }));
    expect(await screen.findByRole("button", { name: /قبلی/ })).toBeTruthy();

    await user.click(screen.getByRole("button", { name: /پایان آزمون و تصحیح/ }));
    const dialog = await screen.findByText(/پایان آزمون؟/);
    expect(dialog).toBeTruthy();
    await user.click(screen.getByRole("button", { name: /تصحیح و مشاهدهٔ کارنامه/ }));

    expect(await screen.findByText(/پاسخ‌برگ/)).toBeTruthy();
    await user.click(screen.getByRole("button", { name: /پاسخنامهٔ تشریحی/ }));
    expect(screen.getAllByText(/درست است|تله|پاسخ صحیح/).length).toBeGreaterThan(0);
    await user.click(screen.getByRole("button", { name: /پایان و بازگشت به هاب آزمون/ }));

    const stored = JSON.parse(window.localStorage.getItem("konkur-mimo:learner:v2") ?? "{}");
    expect(stored.examResults.length).toBeGreaterThan(0);
  }, 30000);

  it("answers the offline LearnHarness coach", async () => {
    const user = userEvent.setup();
    render(<LearnerApp />);
    await user.click(await screen.findByText("هوش مصنوعی"));
    expect(await screen.findByText(/مربی لرن‌هارنس/)).toBeTruthy();

    const input = screen.getByPlaceholderText(/پاسخ یا سؤالت را بنویس/);
    await user.type(input, "فکر می‌کنم پیوند هیدروژنی بین بازهای مکمل شکسته می‌شود");
    await user.keyboard("{Enter}");

    expect(await screen.findByText(/اکنون برنامه را می‌چینم|هنوز به واژه‌های کلیدی/)).toBeTruthy();
    const stepper = screen.getByText("آموزش");
    expect(stepper).toBeTruthy();
  }, 20000);

  it("switches to the night theme and profile tab", async () => {
    const user = userEvent.setup();
    render(<LearnerApp />);
    await user.click(await screen.findByText("پروفایل"));
    expect(await screen.findByText("مشخصات")).toBeTruthy();
    await user.click(screen.getByRole("button", { name: /شب/ }));
    expect(document.documentElement.dataset.theme).toBe("night");

    const card = screen.getByText("دربارهٔ این نسخه").closest("div");
    expect(card).toBeTruthy();
    expect(within(document.body).getByText(/کنسول نقشهٔ راه و استودیوی DSL/)).toBeTruthy();
  }, 20000);
});
