// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.settings

import com.getmimo.R

// superclass (DEX): Lcom/getmimo/ui/settings/SettingsListItem;
// annotations (DEX): Lkotlin/Metadata;
class SettingsListLivePreview : com.getmimo.ui.settings.SettingsListItem {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.settings_list_item_live_preview   →  SOURCE/res/layout/settings_list_item_live_preview.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.settings_list_item_live_preview)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.iv_settings_item_icon, R.id.tv_settings_item_title, R.id.pb_settings_list_item

    // Method inventory recovered from DEX (7 methods):
    // DEX: a()V
    // DEX: b(Z)V
    // DEX: getIcon()Landroid/widget/ImageView;
    // DEX: getListener()Landroid/widget/CompoundButton$OnCheckedChangeListener;
    // DEX: getTextView()Landroid/widget/TextView;
    // DEX: setListener(Landroid/widget/CompoundButton$OnCheckedChangeListener;)V
}
