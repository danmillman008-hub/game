"""خلاصهٔ نتیجهٔ تست‌های واحد را به فایل (مثلاً GITHUB_STEP_SUMMARY) می‌نویسد.

دو حالت مسیر پوشش داده می‌شود:
  module/build/test-results/...            (ماژول‌های سطح اول)
  group/module/build/test-results/...      (core/data، feature/pharmacy)
"""
import glob
import sys
import xml.etree.ElementTree as ET

PATTERNS = (
    "*/build/test-results/testDebugUnitTest/*.xml",
    "*/*/build/test-results/testDebugUnitTest/*.xml",
)

def main() -> int:
    files = sorted({f for pattern in PATTERNS for f in glob.glob(pattern)})
    total = failed = 0
    rows = []
    for f in files:
        try:
            root = ET.parse(f).getroot()
        except ET.ParseError:
            continue
        n = int(root.get("tests", 0))
        fa = int(root.get("failures", 0))
        er = int(root.get("errors", 0))
        total += n
        failed += fa + er
        rows.append((root.get("name", f), n, n - fa - er, fa + er))

    print()
    for name, n, ok, bad in rows:
        print(f"| {name} | {n} | {ok} | {bad} | {'OK' if bad == 0 else 'FAIL'} |")
    print()
    print(f"**مجموع: {total} تست، {failed} شکست**")
    if total == 0:
        print()
        print("هیچ فایل نتیجه‌ای پیدا نشد — تست‌ها اجرا نشده‌اند.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
