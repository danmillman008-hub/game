package com.nhuhuy.algidy.feature.scanner

import android.Manifest
import android.content.Context
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageAnalysis
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.core.content.ContextCompat
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleOwner
import androidx.lifecycle.LifecycleRegistry
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import java.util.concurrent.CountDownLatch
import java.util.concurrent.TimeUnit

/**
 * اثبات اینکه خط لولهٔ دوربین (CameraX) روی دستگاه/امولاتور بدون Google Play Services
 * بالا می‌آید و فریم می‌دهد.
 */
@RunWith(AndroidJUnit4::class)
class CameraSmokeTest {

    private class TestLifecycleOwner : LifecycleOwner {
        val registry: LifecycleRegistry by lazy { LifecycleRegistry(this) }
        override val lifecycle: Lifecycle get() = registry
    }

    private val instrumentation = InstrumentationRegistry.getInstrumentation()
    private val context: Context get() = instrumentation.targetContext

    @Before
    fun grantCamera() {
        // بدون افزودن وابستگی اضافه (androidx.test:rules) مجوز را مستقیم می‌دهیم.
        instrumentation.uiAutomation.grantRuntimePermission(
            context.packageName,
            Manifest.permission.CAMERA,
        )
    }

    @Test
    fun cameraDeliversFrames() {
        val provider = ProcessCameraProvider.getInstance(context).get(90, TimeUnit.SECONDS)
        val owner = TestLifecycleOwner()
        instrumentation.runOnMainSync { owner.registry.currentState = Lifecycle.State.RESUMED }

        val firstFrame = CountDownLatch(1)
        val executor = ContextCompat.getMainExecutor(context)

        instrumentation.runOnMainSync {
            val analysis = ImageAnalysis.Builder()
                .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
                .build()
                .apply {
                    setAnalyzer(executor) { image ->
                        firstFrame.countDown()
                        image.close()
                    }
                }
            provider.bindToLifecycle(owner, CameraSelector.DEFAULT_BACK_CAMERA, analysis)
        }

        assertTrue(
            "camera produced no frames within 90s (no camera on this device image?)",
            firstFrame.await(90, TimeUnit.SECONDS),
        )
        instrumentation.runOnMainSync { provider.unbindAll() }
    }
}
