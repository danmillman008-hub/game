// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.view.database

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Lkotlin/Metadata;
class DatabaseView : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.database_view   →  SOURCE/res/layout/database_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.database_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.nsv_table_content, R.id.code_header_separator, R.id.tl_database_header

    // Method inventory recovered from DEX (4 methods):
    // DEX: a(Lbn/c;)V
    // DEX: getOnTabPositionSelected()Lo70/j;
    // DEX: setOnTabPositionSelected(Lo70/j;)V
}
