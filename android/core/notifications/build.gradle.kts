plugins {
    id("stock.android.library")
}

android {
    namespace = "ir.darookhaneh.stock.core.notifications"
}

dependencies {
    implementation(project(":core:model"))
    implementation(project(":core:datastore"))
    implementation(project(":core:data"))
    implementation(project(":core:common"))
    implementation(project(":core:presentation"))
    implementation(project(":core:domain"))

    implementation(libs.koin.androidx.workmanager)
    implementation(libs.accompanist.permissions)
    implementation(libs.androidx.work.runtime.ktx)
}
