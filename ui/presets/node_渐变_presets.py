# 预设菜单
import bpy
from bpy.types import Operator, Panel
from bl_operators.presets import AddPresetBase
# from ...utils.registration import get_prefs
from bpy.utils import register_class, unregister_class
from bl_ui.utils import PresetPanel


class NODE_PT_ColorRamp_Presets(PresetPanel, Panel):
    bl_label = "节点渐变设"
    preset_subdir = "emmmmm/node/渐变"
    preset_operator = "script.execute_preset"
    preset_add_operator = 'emm.node_colorramp_preset_add'

class AddPresetNode_渐变_Passes(AddPresetBase, Operator):
    bl_idname = "emm.node_colorramp_preset_add"
    bl_label = "添加Cy通道预设"
    preset_menu = "NODE_PT_ColorRamp_Presets"

    # 用于存储预设值的变量 <exec>  variable used for all preset values
    preset_defines = ["AC = bpy.context.active_object.active_material.node_tree.nodes[-1].color_ramp"]


    preset_subdir = "emmmmm/node/渐变"

    # 存储在预设中的属性列表 <eval> properties to store in the preset
    preset_values = ["elements",
                        ]


        # 存储预设的位置
        # Mac: /用户/用户名/资源库/Application Support/Blender/2.92/scripts/presets/object/display
        # Win: C:/Users/用户名/....../2.92/scripts/presets/object/display
