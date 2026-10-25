plugins {
    id("stock.android.library")
    alias(libs.plugins.jetbrains.kotlin.serialization)
}

android {
    namespace = "ir.darookhaneh.stock.core.network"
}

dependencies {
    implementation(project(":core:model"))
    implementation(project(":core:common"))
    api(libs.retrofit.core)
    api(libs.retrofit.kotlin.serialization)
    api(libs.okhttp.logging)
    api(libs.kotlinx.serialization.json)
}
