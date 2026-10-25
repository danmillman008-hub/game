plugins {
    id("stock.android.feature")
}

android {
    namespace = "ir.darookhaneh.stock.feature.pharmacy"
}

dependencies {
    implementation(libs.androidx.activity.compose)

    // دوربین و اسکنر باندل‌شدهٔ ML Kit (بدون Play Services — اثبات‌شده در فاز spike)
    implementation(libs.androidx.camera.core)
    implementation(libs.androidx.camera.camera2)
    implementation(libs.androidx.camera.lifecycle)
    implementation(libs.androidx.camera.view)
    // نسخهٔ باندل‌شده: مدل و کتابخانهٔ بومی داخل APK — بدون Play Services و بدون دانلود پویا
    implementation(libs.mlkit.barcode.scanning)
    implementation(libs.accompanist.permissions)
}
