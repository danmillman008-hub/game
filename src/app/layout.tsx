import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";
import "./globals.css";

export const metadata: Metadata = {
  title: "کنکور-میمو × لرن‌هارنس | پلتفرم یادگیری تطبیقی",
  description:
    "پلتفرم کنکور با موتور میمو ۹٫۳۵، گراف دانش KST، تسلط BKT کالیبره و مرور فاصله‌دار FSRS-5 — آفلاین، فارسی و بدون توهم درسنامه.",
  applicationName: "کنکور-میمو",
};

export const viewport: Viewport = {
  themeColor: "#7E4BDE",
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="fa" dir="rtl" data-theme="day" suppressHydrationWarning>
      <body className="min-h-screen antialiased">{children}</body>
    </html>
  );
}
