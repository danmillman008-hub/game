#!/usr/bin/env python3
"""
تست خودکار جریان واقعی روی دستگاه/امولاتور (بدون هیچ ابزار بیرونی).

چرا این فایل وجود دارد: کاربر گفت «بعد از ثبت اولین دارو اپ کرش می‌کند» و هیچ
لاگی در دست نبود. حدس‌زدن دربارهٔ کرش بی‌فایده است؛ این اسکریپت همان کاری را
می‌کند که کاربر با انگشت انجام می‌دهد (تب داروها → افزودن دستی → نام → ذخیره)
و بعد بررسی می‌کند که پروسه زنده است و صفحهٔ جزئیات باز شده یا نه.

اجرا:
    python3 tools/ui-flow-test.py [--serial emulator-5554]

خروجی: کد ۰ اگر همهٔ مراحل رد شوند، ۱ اگر چیزی شکست بخورد. تمام متن‌های
UI در انتها چاپ می‌شوند تا در Issue قابل بررسی باشند.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

PACKAGE = "ir.darookhaneh.stock"
ACTIVITY = f"{PACKAGE}/.MainActivity"
DUMP_PATH = "/sdcard/ui-dump.xml"

# متن‌هایی که با آن‌ها مرحلهٔ بعد را پیدا می‌کنیم (از strings.xml اپ).
ADD_MANUAL = "افزودن دستی دارو"
NAME_LABEL = "نام دارو"
SAVE = "ذخیره"
DRUGS_TAB = "داروها"
DETAIL_MARKERS = ("بچ‌ها", "موجودی کل", "ثبت شد")


class Ui:
    def __init__(self, serial: str | None) -> None:
        self.serial = serial
        self.log: list[str] = []

    def adb(self, *args: str, timeout: int = 60) -> str:
        cmd = ["adb"]
        if self.serial:
            cmd += ["-s", self.serial]
        cmd += list(args)
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return proc.stdout

    def need(self, *args: str, timeout: int = 60) -> str:
        cmd = ["adb"]
        if self.serial:
            cmd += ["-s", self.serial]
        cmd += list(args)
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if proc.returncode != 0:
            raise RuntimeError(f"adb {' '.join(args)} → {proc.returncode}: {proc.stderr.strip()}")
        return proc.stdout

    def say(self, message: str) -> None:
        print(message, flush=True)
        self.log.append(message)

    # ---------------------------------------------------------------- UI tree
    def nodes(self) -> list[dict]:
        self.adb("shell", "uiautomator", "dump", DUMP_PATH)
        raw = self.adb("shell", "cat", DUMP_PATH)
        start = raw.find("<?xml")
        if start < 0:
            return []
        try:
            root = ET.fromstring(raw[start:])
        except ET.ParseError:
            return []

        out: list[dict] = []
        for node in root.iter("node"):
            bounds = node.get("bounds") or ""
            match = re.match(r"\[(\d+),(\d+)]\[(\d+),(\d+)]", bounds)
            if not match:
                continue
            x1, y1, x2, y2 = (int(v) for v in match.groups())
            label = " ".join(
                part for part in (node.get("text"), node.get("content-desc")) if part
            ).strip()
            out.append(
                {
                    "text": label,
                    "cls": node.get("class") or "",
                    "clickable": node.get("clickable") == "true",
                    "center": ((x1 + x2) // 2, (y1 + y2) // 2),
                    "bounds": (x1, y1, x2, y2),
                }
            )
        return out

    def find(self, needle: str, timeout: float = 15.0) -> dict | None:
        """منتظر می‌ماند تا عنصری با این متن پیدا شود (تطبیق جزئی، بدون حساسیت به فاصله)."""
        deadline = time.time() + timeout
        target = normalize(needle)
        while time.time() < deadline:
            for node in self.nodes():
                if target in normalize(node["text"]):
                    return node
            time.sleep(1.0)
        return None

    def tap(self, node: dict) -> None:
        x, y = node["center"]
        self.need("shell", "input", "tap", str(x), str(y))
        time.sleep(0.7)

    def tap_text(self, needle: str, timeout: float = 15.0) -> bool:
        node = self.find(needle, timeout=timeout)
        if node is None:
            self.say(f"❌ پیدا نشد: «{needle}»")
            return False
        self.tap(node)
        return True

    def tap_edit_text(self, timeout: float = 15.0) -> bool:
        """اولین فیلد ورودی قابل‌ویرایش را لمس می‌کند."""
        deadline = time.time() + timeout
        while time.time() < deadline:
            for node in self.nodes():
                if "EditText" in node["cls"]:
                    self.tap(node)
                    return True
            time.sleep(1.0)
        self.say("❌ هیچ فیلد ورودی پیدا نشد")
        return False

    def alive(self) -> bool:
        return bool(self.need("shell", "pidof", PACKAGE).strip())

    def screen_text(self) -> str:
        return " | ".join(sorted({n["text"] for n in self.nodes() if n["text"]}))

    def crash_log(self) -> str:
        return self.adb("logcat", "-d", "-b", "crash")


def normalize(text: str) -> str:
    """حذف نیم‌فاصله/فاصله‌های اضافه و یکسان‌سازی ارقام، تا تطبیق متن شکننده نباشد."""
    text = text.replace("\u200c", " ").replace("\u200f", "").replace("\u200e", "")
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--serial", default=None)
    parser.add_argument("--name", default="TESTDRUG")
    args = parser.parse_args()

    ui = Ui(args.serial)
    failures: list[str] = []

    def step(title: str, ok: bool) -> None:
        ui.say(("✅ " if ok else "❌ ") + title)
        if not ok:
            failures.append(title)

    ui.say("== شروع تست جریان «ثبت داروی اول» ==")
    ui.need("shell", "am", "force-stop", PACKAGE)
    ui.need("logcat", "-c")
    ui.need("shell", "am", "start", "-W", "-n", ACTIVITY)
    time.sleep(4)

    step("اپ باز شد و پروسه زنده است", ui.alive())
    if not ui.alive():
        ui.say(ui.crash_log()[-4000:])
        return 1

    # تب «داروها» (اگر در همان تب نیستیم)
    if ui.find(DRUGS_TAB, timeout=3):
        ui.tap_text(DRUGS_TAB)
    step("صفحهٔ «داروها» دیده شد", ui.find(ADD_MANUAL, timeout=10) is not None)

    step("دکمهٔ «افزودن دستی دارو» زده شد", ui.tap_text(ADD_MANUAL))
    step("فرم افزودن دارو باز شد", ui.find(NAME_LABEL, timeout=10) is not None)

    step("فیلد نام لمس شد", ui.tap_edit_text())
    ui.need("shell", "input", "text", args.name)
    time.sleep(0.5)

    # بستن کیبورد تا دکمهٔ ذخیره دیده شود — همان جایی که کاربر گیر می‌کرد.
    ui.need("shell", "input", "keyevent", "111")  # ESC
    time.sleep(0.5)
    step("دکمهٔ «ذخیره» پیدا و زده شد", ui.tap_text(SAVE))
    time.sleep(3)

    step("بعد از ذخیره اپ کرش نکرد", ui.alive())
    text = ui.screen_text()
    ui.say("متن صفحه بعد از ذخیره: " + text[:600])
    step(
        "بعد از ذخیره صفحهٔ جزئیات/تأیید باز شد",
        any(normalize(m) in normalize(text) for m in DETAIL_MARKERS),
    )

    # ثبت خروجی دارو روی همان صفحه (اگر بچ ساخته شده باشد)
    if ui.find("عملیات موجودی", timeout=3):
        step("کارت عملیات موجودی دیده شد", True)

    if failures:
        ui.say("== شکست‌ها: " + "، ".join(failures) + " ==")
        crashes = ui.crash_log()
        if crashes.strip():
            ui.say("== crash buffer ==")
            ui.say(crashes[-4000:])
        return 1

    ui.say("== همهٔ مراحل رد شد ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
