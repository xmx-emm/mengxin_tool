# 预设菜单
import bpy
from bpy.types import Operator, Panel
from bl_operators.presets import AddPresetBase
from ...utils.registration import get_prefs
from bpy.utils import register_class, unregister_class
from bl_ui.utils import PresetPanel


class CYCLES_PT_Passes_presets(PresetPanel, Panel):
    bl_label = "CY通道预设"
    # preset_subdir = "emmmmm/cycles_passes"
    preset_operator = "script.execute_preset"
    preset_add_operator = 'emm.cycles_passes_preset_add'

    if bpy.app.version >= (2, 94, 0):
        ## 3.0版本
        preset_subdir = "emmmmm/cycles_passes/3.0+"
    else:
        ## 2.93版本
        preset_subdir = "emmmmm/cycles_passes/2.93"
class AddPresetCycles_Passes(AddPresetBase, Operator):
    bl_idname = "emm.cycles_passes_preset_add"
    bl_label = "添加Cy通道预设"
    preset_menu = "CYCLES_PT_Passes_presets"

    # 用于存储预设值的变量 <exec>  variable used for all preset values
    preset_defines = ["vl = bpy.context.view_layer",
                      "cy = bpy.context.view_layer.cycles"]


    if bpy.app.version >= (2, 94, 0):
        ## 3.0版本
        preset_subdir = "emmmmm/cycles_passes/3.0+"

        # 存储在预设中的属性列表 <eval> properties to store in the preset
        preset_values = ["vl.use_pass_z",
                        "vl.use_edge_enhance",
                        "vl.use_freestyle",
                        "vl.use_halo",
                        "vl.use_pass_ambient_occlusion",
                        "vl.use_pass_combined",
                        "vl.use_pass_cryptomatte_accurate",
                        "vl.use_pass_cryptomatte_asset",
                        "vl.use_pass_cryptomatte_material",
                        "vl.use_pass_cryptomatte_object",
                        "vl.use_pass_diffuse_color",
                        "vl.use_pass_diffuse_direct",
                        "vl.use_pass_diffuse_indirect",
                        "vl.use_pass_emit",
                        "vl.use_pass_environment",
                        "vl.use_pass_glossy_color",
                        "vl.use_pass_glossy_direct",
                        "vl.use_pass_glossy_indirect",
                        "vl.use_pass_material_index",
                        "vl.use_pass_mist",
                        "vl.use_pass_normal",
                        "vl.use_pass_object_index",
                        "vl.use_pass_shadow",
                        "vl.use_pass_subsurface_color",
                        "vl.use_pass_subsurface_direct",
                        "vl.use_pass_subsurface_indirect",
                        "vl.use_pass_transmission_color",
                        "vl.use_pass_transmission_direct",
                        "vl.use_pass_transmission_indirect",
                        "vl.use_pass_uv",
                        "vl.use_pass_vector",
                        "vl.use_pass_z",
                        # 这些是滤镜的
                        #  "vl.use_ao",
                        #  "vl.use_sky",
                        #  "vl.use_solid",
                        #  "vl.use_strand",
                        #  "vl.use_volumes",

                        "vl.pass_cryptomatte_depth",
                        #  "cy.use_ztransp",
                        "vl.pass_alpha_threshold",
                        #  "cy.pass_debug_sample_count",
                        "vl.cycles.use_pass_volume_direct",
                        "vl.cycles.use_pass_volume_indirect",

                        "vl.cycles.denoising_store_passes",
                        "vl.cycles.pass_debug_render_time",
                        "vl.cycles.pass_debug_sample_count",
                        "vl.cycles.use_pass_shadow_catcher",
                        ]

    else:
        ## 2.93版本
        preset_subdir = "emmmmm/cycles_passes/2.93"

        # 存储在预设中的属性列表 <eval> properties to store in the preset
        preset_values = ["vl.use_all_z",
                        "vl.use_edge_enhance",
                        "vl.use_freestyle",
                        "vl.use_halo",
                        "vl.use_pass_ambient_occlusion",
                        "vl.use_pass_combined",
                        "vl.use_pass_cryptomatte_accurate",
                        "vl.use_pass_cryptomatte_asset",
                        "vl.use_pass_cryptomatte_material",
                        "vl.use_pass_cryptomatte_object",
                        "vl.use_pass_diffuse_color",
                        "vl.use_pass_diffuse_direct",
                        "vl.use_pass_diffuse_indirect",
                        "vl.use_pass_emit",
                        "vl.use_pass_environment",
                        "vl.use_pass_glossy_color",
                        "vl.use_pass_glossy_direct",
                        "vl.use_pass_glossy_indirect",
                        "vl.use_pass_material_index",
                        "vl.use_pass_mist",
                        "vl.use_pass_normal",
                        "vl.use_pass_object_index",
                        "vl.use_pass_shadow",
                        "vl.use_pass_subsurface_color",
                        "vl.use_pass_subsurface_direct",
                        "vl.use_pass_subsurface_indirect",
                        "vl.use_pass_transmission_color",
                        "vl.use_pass_transmission_direct",
                        "vl.use_pass_transmission_indirect",
                        "vl.use_pass_uv",
                        "vl.use_pass_vector",
                        "vl.use_pass_z",
                        # 这些是滤镜的
                        #  "vl.use_ao",
                        #  "vl.use_sky",
                        #  "vl.use_solid",
                        #  "vl.use_strand",
                        #  "vl.use_volumes",

                        "vl.pass_cryptomatte_depth",
                        #  "cy.use_ztransp",
                        "vl.pass_alpha_threshold",
                        #  "cy.pass_debug_sample_count",
                        "vl.cycles.use_pass_volume_direct",
                        "vl.cycles.use_pass_volume_indirect",

                        "vl.cycles.denoising_store_passes",
                        "vl.cycles.pass_debug_render_time",
                        "vl.cycles.pass_debug_sample_count",
                        ]

    # 存储预设的位置
    # Mac: /用户/用户名/资源库/Application Support/Blender/2.92/scripts/presets/object/display
    # Win: C:/Users/用户名/....../2.92/scripts/presets/object/display



def presets_cycles_mt_passes_presets(self, _context):
    CYCLES_PT_Passes_presets.draw_panel_header(self.layout)


if bpy.app.version >= (2, 94, 0):
    ## 3.0版本
    from cycles.ui import (
    CYCLES_RENDER_PT_passes,
    CYCLES_RENDER_PT_passes_data,
    CYCLES_RENDER_PT_passes_light,
    CYCLES_RENDER_PT_passes_crypto,
    # CYCLES_RENDER_PT_passes_debug,
    CYCLES_RENDER_PT_passes_aov,
    )
    classes = (
        CYCLES_RENDER_PT_passes,
        CYCLES_RENDER_PT_passes_data,
        CYCLES_RENDER_PT_passes_light,
        CYCLES_RENDER_PT_passes_crypto,
        # CYCLES_RENDER_PT_passes_debug,
        CYCLES_RENDER_PT_passes_aov,
    )

else:
    ## 2.93版本
    from cycles.ui import (
        CYCLES_RENDER_PT_passes,
        CYCLES_RENDER_PT_passes_data,
        CYCLES_RENDER_PT_passes_light,
        CYCLES_RENDER_PT_passes_crypto,
        CYCLES_RENDER_PT_passes_debug,
        CYCLES_RENDER_PT_passes_aov,
    )
    classes = (
        CYCLES_RENDER_PT_passes,
        CYCLES_RENDER_PT_passes_data,
        CYCLES_RENDER_PT_passes_light,
        CYCLES_RENDER_PT_passes_crypto,
        CYCLES_RENDER_PT_passes_debug,
        CYCLES_RENDER_PT_passes_aov,
    )

def register():
    try:

        print(bpy.types.CYCLES_RENDER_PT_passes.draw_header_preset,'   重写面板类')

        if get_prefs().render_passes_presets == False:
            for i in classes:
                unregister_class(i)
            del CYCLES_RENDER_PT_passes.draw_header_preset
            for i in classes:
                register_class(i)
    except AttributeError:
        if get_prefs().render_passes_presets:
            for i in classes:
                unregister_class(i)
            CYCLES_RENDER_PT_passes.draw_header_preset = presets_cycles_mt_passes_presets
            for i in classes:
                register_class(i)
        else:
            pass

def unregister():

    try:
        print(bpy.types.CYCLES_RENDER_PT_passes.draw_header_preset, '   重写面板类')
        for i in classes:
            unregister_class(i)
        del CYCLES_RENDER_PT_passes.draw_header_preset
        for i in classes:
            register_class(i)

    except AttributeError:
        pass
