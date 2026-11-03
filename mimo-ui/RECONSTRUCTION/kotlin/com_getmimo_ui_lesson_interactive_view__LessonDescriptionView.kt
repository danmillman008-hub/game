// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.interactive.view

import com.getmimo.R

// superclass (DEX): Landroid/widget/LinearLayout;
// annotations (DEX): Lkotlin/Metadata;
class LessonDescriptionView : android.widget.LinearLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.browser_view_with_header   →  SOURCE/res/layout/browser_view_with_header.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.browser_view_with_header)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   (none)

    // Method inventory recovered from DEX (8 methods):
    // DEX: a()V
    // DEX: getConfigureEmbeddedWebView()Lo70/j;
    // DEX: getEmbeddedWebViews()Ljava/util/List;
    // DEX: getOnWebViewError()Lo70/m;
    // DEX: setConfigureEmbeddedWebView(Lo70/j;)V
    // DEX: setLessonDescription(Ljava/util/List;)V
    // DEX: setOnWebViewError(Lo70/m;)V
}
