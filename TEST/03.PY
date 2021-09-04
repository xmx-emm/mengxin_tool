import bpy
from bpy.types import Panel, Menu
# from bl_ui.space_userpref import USERPREF_PT_addons
from bl_ui.properties_object import ObjectButtonsPanel, OBJECT_PT_display
from bpy.utils import register_class
    
# # class OBJECT_PT_display(ObjectButtonsPanel, Panel):
# #     bl_label = "Viewport Display"
# #     bl_options = {'DEFAULT_CLOSED'}
# #     bl_order = 10

# def draw(self, context):
#     layout = self.layout
#     layout.use_property_split = True


# bpy.types.OBJECT_PT_display.draw = draw
from bl_ui.utils import PresetPanel

class OBJECT_PT_display(ObjectButtonsPanel, Panel):
    bl_label = "Viewport Display"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 10

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        obj = context.object
        obj_type = obj.type
        is_geometry = (obj_type in {
                       'MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'VOLUME', 'HAIR', 'POINTCLOUD'})
        is_wire = (obj_type in {'CAMERA', 'EMPTY'})
        is_empty_image = (
            obj_type == 'EMPTY' and obj.empty_display_type == 'IMAGE')
        is_dupli = (obj.instance_type != 'NONE')
        is_gpencil = (obj_type == 'GPENCIL')

        col = layout.column(heading="Show")
        col.prop(obj, "show_name", text="Name")
        col.prop(obj, "show_axis", text="Axis")

        # Makes no sense for cameras, armatures, etc.!
        # but these settings do apply to dupli instances
        if is_geometry or is_dupli:
            col.prop(obj, "show_wire", text="Wireframe")
        if obj_type == 'MESH' or is_dupli:
            col.prop(obj, "show_all_edges", text="All Edges")
        if is_geometry:
            col.prop(obj, "show_texture_space", text="Texture Space")
            col.prop(obj.display, "show_shadows", text="Shadow")
        col.prop(obj, "show_in_front", text="In Front")
        # if obj_type == 'MESH' or is_empty_image:
        #    col.prop(obj, "show_transparent", text="Transparency")
        sub = layout.column()
        if is_wire:
            # wire objects only use the max. display type for duplis
            sub.active = is_dupli
        sub.prop(obj, "display_type", text="Display As")

        if is_geometry or is_dupli or is_empty_image or is_gpencil:
            # Only useful with object having faces/materials...
            col.prop(obj, "color")

        col = layout.column(align=False, heading="Bounds")
        col.use_property_decorate = False
        row = col.row(align=True)
        sub = row.row(align=True)
        sub.prop(obj, "show_bounds", text="")
        sub = sub.row(align=True)
        sub.active = obj.show_bounds or (obj.display_type == 'BOUNDS')
        sub.prop(obj, "display_bounds_type", text="")
        row.prop_decorator(obj, "display_bounds_type")


class RENDER_PT_presets(PresetPanel, Panel):
    bl_label = "Render Presets"
    preset_subdir = "render"
    preset_operator = "script.execute_preset"
    preset_add_operator = "render.preset_add"



module_name = 'mengxin_tool'


def emm(self, context):

    prefs = context.preferences

    # for mod, info in addons:
    # module_name = mod.__name__
    layout = self.layout
    col = layout.column()
    col_box = col.column()
    addon_preferences = prefs.addons[module_name].preferences
    # if addon_preferences is not None:
    draw = getattr(addon_preferences, "draw", None)
    if draw is not None:
        addon_preferences_class = type(addon_preferences)
        box_prefs = col_box.box()
        addon_preferences_class.layout = box_prefs
        try:
            draw(context)

            box_prefs.label(text=f"萌新工具箱  {module_name}")
        except:
            import traceback
            traceback.print_exc()
            box_prefs.label(
                text="Error (see console)", icon='ERROR')
        del addon_preferences_class.layout


def draw_header(self, context):
    layout = self.layout
    layout.label(text="emm")


# register_class(RENDER_PT_presets)
# print(RENDER_PT_presets)
# bpy.types.OBJECT_PT_display.draw = draw_header_preset

# bpy.types.RENDER_PT_dimensions.draw_header_preset = draw_header_preset


class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Layout Demo"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"


    def draw_header_preset(self, _context):
        RENDER_PT_presets.draw_panel_header(self.layout)

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create a simple row.
        layout.label(text=" Simple Row:")

        row = layout.row()
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create an row where the buttons are aligned to each other.
        layout.label(text=" Aligned Row:")

        row = layout.row(align=True)
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        col.label(text="Column One:")
        col.prop(scene, "frame_end")
        col.prop(scene, "frame_start")

        # Second column, aligned
        col = split.column(align=True)
        col.label(text="Column Two:")
        col.prop(scene, "frame_start")
        col.prop(scene, "frame_end")

        # Big render button
        layout.label(text="Big Button:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("render.render")

        # Different sizes in a row
        layout.label(text="Different button sizes:")
        row = layout.row(align=True)
        row.operator("render.render")

        sub = row.row()
        sub.scale_x = 2.0
        sub.operator("render.render")

        row.operator("render.render")


def register():
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)

def draw_header_preset(self, _context):
    RENDER_PT_presets.draw_panel_header(self.layout)

if __name__ == "__main__":
    register()
bpy.types.SCENE_PT_rigid_body_world.prepend(draw_header_preset)
