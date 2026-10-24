package com.nhuhuy.algidy.feature.scanner

import android.graphics.BitmapFactory
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import com.google.android.gms.tasks.Tasks
import com.google.mlkit.vision.barcode.Barcode
import com.google.mlkit.vision.barcode.BarcodeScannerOptions
import com.google.mlkit.vision.barcode.BarcodeScanning
import com.google.mlkit.vision.common.InputImage
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import java.util.concurrent.TimeUnit

/**
 * اثبات اینکه مدل *باندل‌شدهٔ* ML Kit بدون Google Play Services و بدون اینترنت
 * بارکد را دیکود می‌کند. تصاویر از assets همین APK تست خوانده می‌شوند.
 */
@RunWith(AndroidJUnit4::class)
class BarcodeBundleTest {

    private data class Case(val asset: String, val format: Int, val expectedPrefix: String)

    private val cases = listOf(
        Case("ean13.png", Barcode.FORMAT_EAN_13, "626262040134"),
        Case("qr.png", Barcode.FORMAT_QR_CODE, "0106262620401344"),
        Case("datamatrix.png", Barcode.FORMAT_DATA_MATRIX, "082DA"),
    )

    @Test
    fun bundledScannerDecodesAllThreeFormats() {
        val assets = InstrumentationRegistry.getInstrumentation().context.assets
        val options = BarcodeScannerOptions.Builder()
            .setBarcodeFormats(
                Barcode.FORMAT_EAN_13,
                Barcode.FORMAT_QR_CODE,
                Barcode.FORMAT_DATA_MATRIX,
            )
            .build()
        val scanner = BarcodeScanning.getClient(options)

        try {
            for (case in cases) {
                val bitmap = assets.open(case.asset).use { BitmapFactory.decodeStream(it) }
                assertTrue("asset ${case.asset} could not be decoded", bitmap != null)

                val barcodes = Tasks.await(
                    scanner.process(InputImage.fromBitmap(bitmap!!, 0)),
                    30,
                    TimeUnit.SECONDS,
                )

                assertFalse("no barcode detected in ${case.asset}", barcodes.isEmpty())
                val first = barcodes.first()
                assertEquals(
                    "wrong format for ${case.asset}",
                    case.format,
                    first.format,
                )
                val raw = first.rawValue.orEmpty()
                assertTrue(
                    "unexpected payload for ${case.asset}: '$raw'",
                    raw.contains(case.expectedPrefix),
                )
            }
        } finally {
            scanner.close()
        }
    }
}
