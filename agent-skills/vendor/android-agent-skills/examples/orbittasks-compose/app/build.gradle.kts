plugins {
  id("com.android.application")
  id("org.jetbrains.kotlin.plugin.compose")
  id("io.github.takahirom.roborazzi")
}

android {
  namespace = "dev.androidagentskills.orbittasks.compose"
  compileSdk = 36

  defaultConfig {
    applicationId = "dev.androidagentskills.orbittasks.compose"
    minSdk = 26
    targetSdk = 36
    versionCode = 1
    versionName = "0.1.0"
    testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
  }

  buildFeatures {
    compose = true
  }

  compileOptions {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
  }

  testOptions {
    unitTests.isIncludeAndroidResources = true
    unitTests.isReturnDefaultValues = true
    unitTests.all {
      it.systemProperties["robolectric.pixelCopyRenderMode"] = "hardware"
    }
  }
}

roborazzi {
  outputDir.set(file("src/test/screenshots"))
}

dependencies {
  val composeBom = platform("androidx.compose:compose-bom:2026.02.01")
  implementation(composeBom)
  testImplementation(composeBom)
  androidTestImplementation(composeBom)

  implementation("androidx.activity:activity-compose:1.12.4")
  implementation("androidx.core:core-ktx:1.15.0")
  implementation("androidx.compose.material3:material3")
  implementation("androidx.compose.ui:ui")
  implementation("androidx.compose.ui:ui-tooling-preview")
  implementation("androidx.lifecycle:lifecycle-runtime-compose:2.9.3")
  implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.9.3")
  implementation("io.coil-kt.coil3:coil-compose:3.4.0")
  implementation("org.jetbrains.kotlin:kotlin-stdlib:2.3.10")

  debugImplementation("androidx.compose.ui:ui-tooling")
  debugImplementation("androidx.compose.ui:ui-test-manifest")

  testImplementation("junit:junit:4.13.2")
  testImplementation("androidx.compose.ui:ui-test-junit4")
  testImplementation("androidx.test.ext:junit:1.2.1")
  testImplementation("io.github.takahirom.roborazzi:roborazzi:1.59.0")
  testImplementation("io.github.takahirom.roborazzi:roborazzi-compose:1.59.0")
  testImplementation("org.robolectric:robolectric:4.16")
  androidTestImplementation("androidx.test.ext:junit:1.2.1")
  androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
  androidTestImplementation("androidx.compose.ui:ui-test-junit4")
}
