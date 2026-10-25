package dev.androidagentskills.orbittasks.compose

import androidx.compose.ui.test.onRoot
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import com.dropbox.differ.SimpleImageComparator
import com.github.takahirom.roborazzi.captureRoboImage
import com.github.takahirom.roborazzi.RoborazziOptions
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode

@RunWith(AndroidJUnit4::class)
@GraphicsMode(GraphicsMode.Mode.NATIVE)
@Config(sdk = [34])
class MainActivityScreenshotTest {
    @get:Rule
    val composeRule = createComposeRule()

    private val roborazziOptions = RoborazziOptions(
        compareOptions = RoborazziOptions.CompareOptions(
            changeThreshold = 0.01f,
            imageComparator = SimpleImageComparator(
                maxDistance = 0.007f,
                vShift = 2,
                hShift = 2,
            ),
        ),
    )

    @Test
    fun orbitTasksBoard_matchesGolden() {
        composeRule.setContent { OrbitTasksApp() }
        composeRule.onRoot().captureRoboImage(roborazziOptions = roborazziOptions)
    }
}
