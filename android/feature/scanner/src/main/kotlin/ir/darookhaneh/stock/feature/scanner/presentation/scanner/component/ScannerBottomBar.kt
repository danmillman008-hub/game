package ir.darookhaneh.stock.feature.scanner.presentation.scanner.component

import android.net.Uri
import androidx.compose.animation.ExperimentalAnimationApi
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.designsystem.theme.LocalCameraColorScheme
import ir.darookhaneh.stock.core.presentation.PhotoPickerContainer

@OptIn(ExperimentalAnimationApi::class)
@Composable
fun ScannerBottomBar(
    modifier: Modifier = Modifier,
    isAutoScanned: Boolean,
    onLaunch: () -> Unit,
    onImageStaged: (Uri?) -> Unit,
    onAddManualBarcode: () -> Unit,
    onAutoScanChange: (Boolean) -> Unit
) {

    val cameraScheme = LocalCameraColorScheme.current
    Row(
        modifier = modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp, vertical = 24.dp),
        horizontalArrangement = Arrangement.SpaceEvenly,
        verticalAlignment = Alignment.CenterVertically
    ) {
        PhotoPickerContainer(
            onImagePicked = onImageStaged,
            onLaunch = onLaunch
        ) { launcher ->
            SelectImageButton(
                modifier = Modifier.size(64.dp),
                onClick = launcher,
                containerColor = cameraScheme.secondaryContainer,
                contentColor = cameraScheme.onSecondaryContainer
            )
        }

        AutoScanButton(
            modifier = Modifier.size(104.dp),
            autoScanning = isAutoScanned,
            onClick = onAutoScanChange
        )

        AddManuallyBarcodeButton(
            modifier = Modifier.size(64.dp),
            onClick = onAddManualBarcode
        )
    }
}
