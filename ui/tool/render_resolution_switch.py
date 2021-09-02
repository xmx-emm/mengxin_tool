
import bpy
from bpy.utils import register_class , unregister_class
from bl_ui.properties_output import RENDER_PT_dimensions, RENDER_PT_presets
from bpy.types import Operator as OPS
from ...utils.blender_class import RENDER_PT_PRESETS
from bpy.types import Menu, Panel, UIList


class render_resolution_switch(OPS, UIList):
    """切换分辨率"""
    bl_idname = 'emm.render_resolution_switch'
    bl_label = '切换翻译'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = """点一下就可以切换XY的分辨率"""

    def execute(self, context):
        render = bpy.context.scene.render
        x = render.resolution_x
        y = render.resolution_y
        e = x

        render.resolution_x = y
        render.resolution_y = e

        return {'FINISHED'}
    
    # def __init__(self):
    def DRAW_HEADER_PRESET(self, _context):
        self.layout.operator(operator="emm.render_resolution_switch", emboss=False,text='',icon='UV_SYNC_SELECT')

        RENDER_PT_presets.draw_panel_header(self.layout)


    RENDER_PT_DIMENSIONS = RENDER_PT_dimensions
    RENDER_PT_DIMENSIONS.draw_header_preset = DRAW_HEADER_PRESET
    def __del__(self):
        def DRAW_HEADE(self, _context):
            # self.layout.operator(operator="emm.render_resolution_switch", emboss=False,text='',icon='UV_SYNC_SELECT')
            RENDER_PT_presets.draw_panel_header(self.layout)
        RENDER_PT_DIMENSIONS = RENDER_PT_dimensions
        RENDER_PT_DIMENSIONS.draw_header_preset = DRAW_HEADE
