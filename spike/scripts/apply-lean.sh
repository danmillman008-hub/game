#!/usr/bin/env bash
# «نسخهٔ سبک»: حذف موتور OCR تاریخ‌خوان (در هیچ ViewModelی مصرف نمی‌شود) و فونت‌های بلااستفاده.
# هدف: اندازه‌گیری وزن واقعی چیزی که ما لازم داریم.
# Usage: apply-lean.sh <algidy-checkout>
set -euo pipefail
ROOT="${1:?usage: apply-lean.sh <algidy-checkout>}"
cd "$ROOT"

# 1) فونت‌هایی که دیگر ارجاعی ندارند (Type.kt فقط Vazirmatn را صدا می‌زند)
rm -f core/designsystem/src/main/res/font/google_sans_flex_font.ttf
rm -f core/designsystem/src/main/res/font/montserrat_*.ttf
rm -f core/designsystem/src/main/res/font/poppins_*.ttf

# 2) زنجیرهٔ OCR تاریخ‌خوان (ML Kit text-recognition + entity-extraction)
rm -f feature/scanner/src/main/kotlin/com/nhuhuy/algidy/feature/scanner/data/MLKitFoodDateScanner.kt
rm -f feature/scanner/src/main/kotlin/com/nhuhuy/algidy/feature/scanner/domain/FoodDateScanner.kt
rm -f feature/scanner/src/main/kotlin/com/nhuhuy/algidy/feature/scanner/domain/usecase/ScanFoodDateUseCase.kt

# 3) قطع تزریق در DI و حذف دو وابستگی سنگین
python3 - "$ROOT" <<'PY'
import sys, pathlib
root = pathlib.Path(sys.argv[1])

p = root / "feature/scanner/src/main/kotlin/com/nhuhuy/algidy/feature/scanner/di/ScannerModule.kt"
s = p.read_text()
s = s.replace("import com.nhuhuy.algidy.feature.scanner.domain.usecase.ScanFoodDateUseCase\n", "")
s = s.replace("    factoryOf(::ScanFoodDateUseCase)\n", "")
p.write_text(s)

p = root / "feature/scanner/build.gradle.kts"
s = p.read_text()
for dep in ("    implementation(libs.mlkit.text.recognition)\n", "    implementation(libs.entity.extraction)\n"):
    s = s.replace(dep, "")
p.write_text(s)
print("lean edits applied")
PY
