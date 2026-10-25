plugins {
    id("stock.android.library")
}

android {
    namespace = "ir.darookhaneh.stock.core.data"

    testOptions {
        unitTests {
            isIncludeAndroidResources = true
        }
    }
}

dependencies {
    api(libs.timber)
    implementation(project(":core:database"))
    implementation(project(":core:model"))
    implementation(project(":core:network"))
    implementation(project(":core:common"))
    implementation(project(":core:domain"))
    implementation(libs.kotlinx.coroutines.android)
    api(libs.kotlinx.coroutines.play.services)

    // Room (برای تست‌های in-memory هستهٔ داروخانه)
    testImplementation(libs.room.runtime)
    testImplementation(libs.room.ktx)
    testImplementation(libs.androidx.junit)

    //Filkit
    api("io.github.vinceglb:filekit-core:0.15.0")
    api("io.github.vinceglb:filekit-dialogs-compose:0.15.0")


}