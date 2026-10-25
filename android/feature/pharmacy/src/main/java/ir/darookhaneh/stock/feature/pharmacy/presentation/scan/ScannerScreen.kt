package ir.darookhaneh.stock.feature.pharmacy.presentation.scan

import android.Manifest
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageAnalysis
import androidx.camera.core.ImageProxy
import androidx.camera.core.Preview
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.camera.view.PreviewView
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawingPadding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalLifecycleOwner
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.viewinterop.AndroidView
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import com.google.mlkit.vision.barcode.BarcodeScannerOptions
import com.google.mlkit.vision.barcode.BarcodeScanning
import com.google.mlkit.vision.barcode.common.Barcode
import com.google.mlkit.vision.common.InputImage
import ir.darookhaneh.stock.feature.pharmacy.R
import org.koin.androidx.compose.koinViewModel

/**
 * اسکن بارکد با ML Kit باندل‌شده (بدون Play Services).
 * نتیجه به‌صورت محلی جست‌وجو می‌شود؛ کد ناشناخته فقط فرم ثبت دستی را باز می‌کند.
 */
@Composable
fun ScannerRoute(
    onUnknownCode: (String) -> Unit,
    onDrugFound: (Long) -> Unit,
    onNavigateBack: () -> Unit,
) {
    val viewModel: ScannerViewModel = koinViewModel()
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    LaunchedEffect(uiState.unknownCode) {
        uiState.unknownCode?.let { code ->
            viewModel.onUnknownHandled()
            onUnknownCode(code)
        }
    }
    LaunchedEffect(uiState.foundDrugId) {
        uiState.foundDrugId?.let { drugId ->
            viewModel.onFoundHandled()
            onDrugFound(drugId)
        }
    }

    ScannerScreen(
        uiState = uiState,
        onCodeScanned = viewModel::onCodeScanned,
        onNavigateBack = onNavigateBack,
    )
}

@Composable
fun ScannerScreen(
    uiState: ScannerUiState,
    onCodeScanned: (String) -> Unit,
    onNavigateBack: () -> Unit,
) {
    val currentOnCode = rememberUpdatedState(onCodeScanned)

    Box(modifier = Modifier.fillMaxSize()) {
        BarcodeCameraPreview(
            modifier = Modifier.fillMaxSize(),
            onCodeScanned = { code -> currentOnCode.value(code) },
        )

        // راهنما
        Box(
            modifier = Modifier
                .align(Alignment.Center)
                .fillMaxWidth()
                .padding(horizontal = 40.dp)
                .background(Color.Black.copy(alpha = 0.35f), RoundedCornerShape(16.dp))
                .padding(16.dp),
        ) {
            Text(
                text = stringResource(R.string.pharmacy_scan_hint),
                color = Color.White,
                style = MaterialTheme.typography.bodyMedium,
                textAlign = TextAlign.Center,
                modifier = Modifier.fillMaxWidth(),
            )
        }

        Column(
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .fillMaxWidth()
                .safeDrawingPadding()
                .padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            if (uiState.isResolving) {
                CircularProgressIndicator(color = MaterialTheme.colorScheme.primary)
            }
            uiState.lastCode?.let { code ->
                Text(
                    text = stringResource(R.string.pharmacy_scan_last_code, code),
                    style = MaterialTheme.typography.bodySmall,
                    color = Color.White,
                )
            }
            Button(onClick = onNavigateBack, modifier = Modifier.fillMaxWidth()) {
                Text(stringResource(R.string.pharmacy_scan_manual_instead))
            }
        }
    }
}

@Composable
private fun BarcodeCameraPreview(
    modifier: Modifier = Modifier,
    onCodeScanned: (String) -> Unit,
) {
    val context = LocalContext.current
    val lifecycleOwner = LocalLifecycleOwner.current
    val previewView = remember {
        PreviewView(context).apply { scaleType = PreviewView.ScaleType.FILL_CENTER }
    }
    val currentOnCode = rememberUpdatedState(onCodeScanned)

    DisposableEffect(Unit) {
        val providerFuture = ProcessCameraProvider.getInstance(context)
        val executor = java.util.concurrent.Executors.newSingleThreadExecutor()

        val scanner = BarcodeScanning.getClient(
            BarcodeScannerOptions.Builder()
                .setBarcodeFormats(
                    Barcode.FORMAT_EAN_13,
                    Barcode.FORMAT_EAN_8,
                    Barcode.FORMAT_UPC_A,
                    Barcode.FORMAT_UPC_E,
                    Barcode.FORMAT_QR_CODE,
                    Barcode.FORMAT_DATA_MATRIX,
                    Barcode.FORMAT_CODE_128,
                )
                .build()
        )

        var debounceCode: String? = null
        var lastEmitAt = 0L

        providerFuture.addListener({
            val provider = providerFuture.get()
            val preview = Preview.Builder().build().also {
                it.surfaceProvider = previewView.surfaceProvider
            }
            val analysis = ImageAnalysis.Builder()
                .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
                .build()
                .also { imageAnalysis ->
                    imageAnalysis.setAnalyzer(executor) { imageProxy: ImageProxy ->
                        val mediaImage = imageProxy.image
                        if (mediaImage == null) {
                            imageProxy.close()
                            return@setAnalyzer
                        }
                        val inputImage = InputImage.fromMediaImage(
                            mediaImage,
                            imageProxy.imageInfo.rotationDegrees,
                        )
                        scanner.process(inputImage)
                            .addOnSuccessListener { barcodes ->
                                val raw = barcodes.firstNotNullOfOrNull { it.rawValue }
                                val now = System.currentTimeMillis()
                                if (raw != null && (raw != debounceCode || now - lastEmitAt > 1_500)) {
                                    debounceCode = raw
                                    lastEmitAt = now
                                    currentOnCode.value(raw)
                                }
                            }
                            .addOnCompleteListener { imageProxy.close() }
                    }
                }

            runCatching {
                provider.unbindAll()
                provider.bindToLifecycle(
                    lifecycleOwner,
                    CameraSelector.DEFAULT_BACK_CAMERA,
                    preview,
                    analysis,
                )
            }
        }, androidx.core.content.ContextCompat.getMainExecutor(context))

        onDispose {
            runCatching { providerFuture.get().unbindAll() }
            runCatching { scanner.close() }
            executor.shutdown()
        }
    }

    AndroidView(
        modifier = modifier,
        factory = { previewView },
    )
}

/** برای استفاده در آینده: بررسی وجود مجوز دوربین در فراخوان. */
@Composable
fun requireCameraPermission(): Boolean =
    androidx.core.content.ContextCompat.checkSelfPermission(
        LocalContext.current,
        Manifest.permission.CAMERA,
    ) == android.content.pm.PackageManager.PERMISSION_GRANTED
