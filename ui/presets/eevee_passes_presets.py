# 预设菜单
import bpy
from bpy.types import Operator, Panel
from bl_operators.presets import AddPresetBase
from ...utils.registration import get_prefs
from bpy.utils import register_class, unregister_class
from bl_ui.utils import PresetPanel
from bl_ui.properties_view_layer import (
VIEWLAYER_PT_layer_passes, 
VIEWLAYER_PT_layer_passes_aov, 
VIEWLAYER_PT_layer_passes_cryptomatte, 
# VIEWLAYER_PT_layer, 
VIEWLAYER_PT_eevee_layer_passes_data, 
VIEWLAYER_PT_eevee_layer_passes_light, 
VIEWLAYER_PT_eevee_layer_passes_effects, 
VIEWLAYER_UL_aov)


class EEVEE_PT_Passes_presets(PresetPanel, Panel):
    bl_label = "EV通道预设"
    preset_subdir = "emmmmm/eevee_passes"
    preset_operator = "script.execute_preset"
    preset_add_operator = 'emm.eevee_passes_preset_add'

class AddPresetEEVEE_Passes(AddPresetBase, Operator):
    bl_idname = "emm.eevee_passes_preset_add"
    bl_label = "添加EV通道预设"
    preset_menu = "EEVEE_PT_Passes_presets"

    # 用于存储预设值的变量 <exec>  variable used for all preset values
    preset_defines = ["vl = bpy.context.view_layer"]

    # 存储在预设中的属性列表 <eval> properties to store in the preset
    preset_values = ["vl.use_pass_combined",
                     "vl.use_pass_z",
                     "vl.use_pass_mist",
                     "vl.use_pass_normal",
                     "vl.use_pass_diffuse_direct",
                     "vl.use_pass_diffuse_color",
                     "vl.use_pass_glossy_direct",
                     "vl.use_pass_glossy_color",
                     "vl.use_pass_cryptomatte_object",
                     "vl.use_pass_cryptomatte_material",
                     "vl.use_pass_cryptomatte_asset",
                     "vl.pass_cryptomatte_depth",
                     "vl.use_pass_cryptomatte_accurate",
                     #  "vl.",
                     #  "vl.",
                     #  "vl.",
                     #  "vl.",
                     #  "vl.",
                     #  "vl.",
                     #  "vl.",
                     #  "vl.",
                     #  "vl.",
                     "vl.use_pass_ambient_occlusion",
                     "vl.use_pass_shadow",
                     "vl.use_pass_environment",
                     "vl.use_pass_emit",
                     "vl.eevee.use_pass_volume_direct",
                     "vl.eevee.use_pass_bloom",
                     #  "vl.",
                     #  "vl.",
                     ]

    # 存储预设的位置
    # Mac: /用户/用户名/资源库/Application Support/Blender/2.92/scripts/presets/object/display
    # Win: C:/Users/用户名/....../2.92/scripts/presets/object/display
    preset_subdir = "emmmmm/eevee_passes"


def display_presets_draw_header_preset(self, _context):
    EEVEE_PT_Passes_presets.draw_panel_header(self.layout)


classes = (
    # VIEWLAYER_PT_layer,
    VIEWLAYER_PT_layer_passes,
    VIEWLAYER_PT_eevee_layer_passes_data,
    VIEWLAYER_PT_eevee_layer_passes_light,
    VIEWLAYER_PT_eevee_layer_passes_effects,
    VIEWLAYER_PT_layer_passes_cryptomatte,
    VIEWLAYER_PT_layer_passes_aov,
    VIEWLAYER_UL_aov,
)


def register():
    try:
        print(bpy.types.VIEWLAYER_PT_layer_passes.draw_header_preset, '重写面板类')

        if get_prefs().render_passes_presets == False:
            for i in classes:
                unregister_class(i)
            del VIEWLAYER_PT_layer_passes.draw_header_preset
            for i in classes:
                register_class(i)
    except AttributeError:
        if get_prefs().render_passes_presets:
            for i in classes:
                unregister_class(i)
            VIEWLAYER_PT_layer_passes.draw_header_preset = display_presets_draw_header_preset
            for i in classes:
                register_class(i)
        else:
            pass


def unregister():

    try:
        print(bpy.types.VIEWLAYER_PT_layer_passes.draw_header_preset, '重写面板类')
        for i in classes:
            unregister_class(i)
        del VIEWLAYER_PT_layer_passes.draw_header_preset
        for i in classes:
            register_class(i)

    except AttributeError:
        pass
