// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.components.placeholder

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Lkotlin/Metadata;
class PlaceholderView : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.placeholder_view   →  SOURCE/res/layout/placeholder_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.placeholder_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   (none)

    // Method inventory recovered from DEX (6 methods):
    // DEX: a()V
    // DEX: getCardRadius()F
    // DEX: onAttachedToWindow()V
    // DEX: onDetachedFromWindow()V
    // DEX: setCardRadius(F)V
}
