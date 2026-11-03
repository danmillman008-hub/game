// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.settings

import com.getmimo.R

// superclass (DEX): Lcom/getmimo/ui/settings/SettingsListItem;
// annotations (DEX): Lkotlin/Metadata;
class SettingsListSwitchItem : com.getmimo.ui.settings.SettingsListItem {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.settings_list_item_switcher   →  SOURCE/res/layout/settings_list_item_switcher.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.settings_list_item_switcher)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.sw_settings_item_switcher, R.id.tv_settings_item_switcher_title, R.id.iv_settings_item_switcher_icon

    // Method inventory recovered from DEX (8 methods):
    // DEX: a()V
    // DEX: getIcon()Landroid/widget/ImageView;
    // DEX: getListener()Landroid/widget/CompoundButton$OnCheckedChangeListener;
    // DEX: getTextView()Landroid/widget/TextView;
    // DEX: setChecked(Z)V
    // DEX: setListener(Landroid/widget/CompoundButton$OnCheckedChangeListener;)V
    // DEX: setOnCheckedChangeListener(Landroid/widget/CompoundButton$OnCheckedChangeListener;)V
}
