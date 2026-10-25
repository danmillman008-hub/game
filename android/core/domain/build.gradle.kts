plugins {
    id("stock.android.library")
}

android {
    namespace = "ir.darookhaneh.stock.core.domain"
}

dependencies {
    // Bây giờ bạn có thể sử dụng bản android
    implementation(libs.kotlinx.coroutines.android)
    implementation(project(":core:model"))
}