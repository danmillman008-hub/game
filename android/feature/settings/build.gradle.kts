
plugins {
    id("stock.android.feature")
    alias(libs.plugins.jetbrains.kotlin.serialization)
}

android {
    namespace = "ir.darookhaneh.stock.feature.settings"
}

dependencies {
    implementation(project(":core:datastore"))
    implementation(project(":core:network"))
    implementation(project(":core:notifications"))
    implementation(libs.kotlinx.serialization.core)
    implementation(libs.kotlinx.serialization.json)
    implementation(libs.aboutlibraries.compose)

}
