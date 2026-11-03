// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.view.code

import com.getmimo.R

// superclass (DEX): Landroidx/constraintlayout/widget/ConstraintLayout;
// annotations (DEX): Lkotlin/Metadata;
class BrowserBar : androidx.constraintlayout.widget.ConstraintLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.browser_bar   →  SOURCE/res/layout/browser_bar.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.browser_bar)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.btn_browser_bar_refresh, R.id.btn_browser_bar_share, R.id.container_browser_bar_url, R.id.tv_browser_bar_url

    // Method inventory recovered from DEX (4 methods):
    // DEX: setOnRefreshClickListener(Lkotlin/jvm/functions/Function0;)V
    // DEX: setOnShareClickListener(Lo70/j;)V
    // DEX: setUrl(Ljava/lang/String;)V
}
