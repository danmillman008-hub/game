plugins {
    id("stock.android.library")
    alias(libs.plugins.jetbrains.kotlin.serialization)
}

android {
    namespace = "ir.darookhaneh.stock.core.model"
}

dependencies {
    implementation(libs.kotlinx.serialization.json)
}
