// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.view.tags

import com.getmimo.R

// superclass (DEX): Landroid/widget/LinearLayout;
// annotations (DEX): Lkotlin/Metadata;
class TagSelectionView : android.widget.LinearLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.tag_item_layout   →  SOURCE/res/layout/tag_item_layout.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.tag_item_layout)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.item_name

    // Method inventory recovered from DEX (18 methods):
    // DEX: getItemLayoutParams()Landroid/widget/LinearLayout$LayoutParams;
    // DEX: getSelectorNormal()Landroid/graphics/drawable/StateListDrawable;
    // DEX: getSelectorSelected()Landroid/graphics/drawable/StateListDrawable;
    // DEX: a(Landroid/view/View; Landroid/widget/LinearLayout$LayoutParams; Z)V
    // DEX: b()V
    // DEX: c(Lcn/d;)Landroid/graphics/drawable/StateListDrawable;
    // DEX: getMaxSelectableItemsCount()Ljava/lang/Integer;
    // DEX: getOnItemClickListener()Lcn/b;
    // DEX: getSelectedItems()Ljava/util/List;
    // DEX: getSingleChoice()Z
    // DEX: getTagViewItems()Ljava/util/List;
    // DEX: onDetachedFromWindow()V
    // DEX: onSizeChanged(I I I I)V
    // DEX: setMaxSelectableItemsCount(Ljava/lang/Integer;)V
    // DEX: setOnItemClickListener(Lcn/b;)V
    // DEX: setSingleChoice(Z)V
    // DEX: setTagViewItems(Ljava/util/List;)V
}
