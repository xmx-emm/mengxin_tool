import bpy
import os
from bpy.types import Menu
from ..utils.registration import get_prefs
from .presets.object_display_presets import OBJECT_PT_display_presets
from ..utils.addon import get_addon
from ..utils.addon import get_addon_prefs
from ..utils.system import abspath
decalmachine = None

class PieModes_pie(Menu):
    bl_idname = "EMMMMM_MT_modes_pie"
    bl_label = "模式饼菜单"

    # def draw(self, context):
        #     layout = self.layout
        #     pie = layout.menu_pie()
        #     C = context
        #     Co = C.object

        #     active = context.active_object
        #     shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        #     overlay = context.space_data.overlay

        #     if C.area.type == "VIEW_3D" and active:
        #         if Co.type=="MESH":
        #             if Co.mode=="OBJECT":
        #                 # 左
        #                 p1 = pie.prop_enum(shading, "type", value='WIREFRAME')
        #                 p1

        #                 # 右
        #                 p2 = pie.prop_enum(shading, "type", value='SOLID')
        #                 p2

        #                 # 底
        #                 p3 = pie.prop(overlay, "show_wireframes",icon='MOD_WIREFRAME')
        #                 p3
                        
        #                 # 顶
        #                 p4 = pie.prop(overlay, "show_face_orientation",icon='FACESEL')
        #                 p4

        #                 # 左上
        #                 p5 = pie.prop_enum(shading, "type", value='MATERIAL')
        #                 p5


        #                 #右上
        #                 p6 = pie.prop_enum(shading, "type", value='RENDERED')
        #                 p6
                        
                        
        #                 #左下
        #                 p7 = pie.operator('object.shade_smooth')
        #                 p7


        #                 #右下
        #                 p8 = pie.operator('object.shade_flat')
        #                 p8


    ####M3
    def M3(self,context,active,pie,toolsettings):
        layout = self.layout
        pie = layout.menu_pie()
        if context.mode in ['OBJECT', 'EDIT_MESH', 'EDIT_ARMATURE', 'POSE', 'EDIT_CURVE', 'EDIT_TEXT', 'EDIT_SURFACE', 'EDIT_METABALL', 'EDIT_LATTICE', 'EDIT_GPENCIL', 'PAINT_GPENCIL', 'SCULPT_GPENCIL', 'WEIGHT_GPENCIL']:
            if active.type == 'MESH':
                if context.area.type == "VIEW_3D":

                    if active.library:
                        blendpath = abspath(active.library.filepath)
                        library = active.library.name

                        op = pie.operator("machin3.open_library_blend", text="Open %s" % (os.path.basename(blendpath)))
                        op.blendpath = blendpath
                        op.library = library

                    else:
                        pie.operator("machin3.mesh_mode", text="Vertex", icon='VERTEXSEL').mode = 'VERT'

                        pie.operator("machin3.mesh_mode", text="Face", icon='FACESEL').mode = 'FACE'

                        pie.operator("machin3.mesh_mode", text="Edge", icon='EDGESEL').mode = 'EDGE'

                        text, icon = ("Edit", 'EDITMODE_HLT') if active.mode == "OBJECT" else ("Object", 'FILE_3D')
                        pie.operator("machin3.edit_mode", text=text, icon=icon)

                        self.draw_mesh_modes(context, pie)

                        pie.separator()

                        if get_addon_prefs('MACHIN3tools').activate_surface_slide:
                            hassurfaceslide = [mod for mod in active.modifiers if mod.type == 'SHRINKWRAP' and 'SurfaceSlide' in mod.name]

                            if context.mode == 'EDIT_MESH':
                                box = pie.split()
                                column = box.column(align=True)

                                row = column.row(align=True)
                                row.scale_y = 1.2

                                if hassurfaceslide:
                                    row.operator("machin3.finish_surface_slide", text='Finish Surface Slide', icon='OUTLINER_DATA_SURFACE')
                                else:
                                    row.operator("machin3.surface_slide", text='Surface Slide', icon='OUTLINER_DATA_SURFACE')

                            elif hassurfaceslide:
                                box = pie.split()
                                column = box.column(align=True)

                                row = column.row(align=True)
                                row.scale_y = 1.2
                                row.operator("machin3.finish_surface_slide", text='Finish Surface Slide', icon='OUTLINER_DATA_SURFACE')

                            else:
                                pie.separator()

                        else:
                            pie.separator()


                        if context.mode == "EDIT_MESH":
                            box = pie.split()
                            column = box.column()

                            row = column.row()
                            row.scale_y = 1.2
                            row.prop(context.scene.M3, "pass_through", text="Pass Through" if context.scene.M3.pass_through else "Occlude", icon="XRAY")

                            column.prop(toolsettings, "use_mesh_automerge", text="Auto Merge")

                        else:
                            pie.separator()

                if context.area.type == "IMAGE_EDITOR":
                    toolsettings = context.scene.tool_settings

                    if context.mode == "OBJECT":
                        pie.operator("machin3.image_mode", text="UV Edit", icon="GROUP_UVS").mode = "UV"

                        pie.operator("machin3.image_mode", text="Paint", icon="TPAINT_HLT").mode = "PAINT"

                        pie.operator("machin3.image_mode", text="Mask", icon="MOD_MASK").mode = "MASK"

                        pie.operator("machin3.image_mode", text="View", icon="FILE_IMAGE").mode = "VIEW"


                    elif context.mode == "EDIT_MESH":
                        pie.operator("machin3.uv_mode", text="Vertex", icon='EDITMODE_HLT').mode = "VERTEX"

                        pie.operator("machin3.uv_mode", text="Face",  icon='FACESEL').mode = "FACE"

                        pie.operator("machin3.uv_mode", text="Edge",  icon='EDGESEL').mode = "EDGE"

                        pie.operator("object.mode_set", text="Object", icon='MESH_CUBE').mode = "OBJECT"

                        pie.prop(context.scene.M3, "uv_sync_select", text="Sync Selection", icon="UV_SYNC_SELECT")

                        if toolsettings.use_uv_select_sync:
                            pie.separator()
                        else:
                            pie.operator("machin3.uv_mode", text="Island", icon='UV_ISLANDSEL').mode = "ISLAND"

                        pie.separator()

                        pie.separator()

            elif active.type == 'ARMATURE':
                pie.operator("object.mode_set", text="Edit Mode", icon='EDITMODE_HLT').mode = "EDIT"

                pie.operator("object.mode_set", text="Pose", icon='POSE_HLT').mode = "POSE"

                pie.separator()

                text, icon = ("Edit", "EDITMODE_HLT") if active.mode == "OBJECT" else ("Object", "OBJECT_DATAMODE")
                if active.mode == "POSE":
                    pie.operator("object.posemode_toggle", text=text, icon=icon)
                else:
                    pie.operator("object.editmode_toggle", text=text, icon=icon)

                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

            elif active.type in ['CURVE', 'FONT', 'SURFACE', 'META', 'LATTICE']:
                pie.operator("object.mode_set", text="Edit Mode", icon='EDITMODE_HLT').mode = "EDIT"

                pie.separator()

                pie.separator()

                text, icon = ("Edit", "EDITMODE_HLT") if active.mode == "OBJECT" else ("Object", "OBJECT_DATAMODE")
                pie.operator("object.editmode_toggle", text=text, icon=icon)

                pie.separator()

                pie.separator()

                pie.separator()

                if bpy.context.mode in ['EDIT_SURFACE', 'EDIT_METABALL']:
                    box = pie.split()
                    column = box.column()

                    row = column.row()
                    row.scale_y = 1.2
                    row.prop(context.scene.M3, "pass_through", text="Pass Through" if context.scene.M3.pass_through else "Occlude", icon="XRAY")
                else:
                    pie.separator()

            elif active.type == 'GPENCIL':
                gpd = context.gpencil_data

                pie.operator("object.mode_set", text="Edit Mode", icon='EDITMODE_HLT').mode = "EDIT_GPENCIL"

                pie.operator("object.mode_set", text="Sculpt", icon='SCULPTMODE_HLT').mode = "SCULPT_GPENCIL"

                pie.operator("object.mode_set", text="Draw", icon='GREASEPENCIL').mode = "PAINT_GPENCIL"

                text, icon = ("Draw", "GREASEPENCIL") if active.mode == "OBJECT" else ("Object", "OBJECT_DATAMODE")

                if active.mode == "WEIGHT_GPENCIL":
                    pie.operator("gpencil.weightmode_toggle", text=text, icon=icon)
                elif active.mode == "EDIT_GPENCIL":
                    pie.operator("gpencil.editmode_toggle", text=text, icon=icon)
                elif active.mode == "SCULPT_GPENCIL":
                    pie.operator("gpencil.sculptmode_toggle", text=text, icon=icon)
                else:
                    pie.operator("gpencil.paintmode_toggle", text=text, icon=icon)

                self.draw_gp_modes(context, pie)

                self.draw_gp_extra(active, pie)

                box = pie.split()
                column = box.column()
                column.scale_y = 1.2
                column.scale_x = 1.2

                if context.mode == "PAINT_GPENCIL":
                    row = column.row(align=True)
                    row.prop(toolsettings, "use_gpencil_draw_onback", text="", icon="MOD_OPACITY")
                    row.prop(toolsettings, "use_gpencil_weight_data_add", text="", icon="WPAINT_HLT")
                    row.prop(toolsettings, "use_gpencil_draw_additive", text="", icon="FREEZE")

                elif context.mode == "EDIT_GPENCIL":
                    row = column.row(align=True)
                    row.prop(toolsettings, "gpencil_selectmode_edit", text="", expand=True)

                    if bpy.app.version >= (2, 92, 0):
                        row.prop(active.data, "use_curve_edit", text="", icon='IPO_BEZIER')


                box = pie.split()
                column = box.column(align=True)

                if context.mode == "EDIT_GPENCIL":
                    row = column.row(align=True)
                    row.prop(gpd, "use_multiedit", text="", icon='GP_MULTIFRAME_EDITING')

                    r = row.row(align=True)
                    r.active = gpd.use_multiedit
                    r.popover(panel="VIEW3D_PT_gpencil_multi_frame", text="Multiframe")

                    row = column.row(align=True)
                    row.popover(panel="VIEW3D_PT_tools_grease_pencil_interpolate", text="Interpolate")

                elif context.mode == "SCULPT_GPENCIL":
                    row = column.row(align=True)
                    row.prop(toolsettings, "use_gpencil_select_mask_point", text="")
                    row.prop(toolsettings, "use_gpencil_select_mask_stroke", text="")
                    row.prop(toolsettings, "use_gpencil_select_mask_segment", text="")

                    row.separator()
                    row.prop(gpd, "use_multiedit", text="", icon='GP_MULTIFRAME_EDITING')

                    r = row.row(align=True)
                    r.active = gpd.use_multiedit
                    r.popover(panel="VIEW3D_PT_gpencil_multi_frame", text="Multiframe")

            elif active.type == 'EMPTY':
                if active.instance_collection and active.instance_collection.library:
                    blendpath = abspath(active.instance_collection.library.filepath)
                    library = active.instance_collection.library.name

                    op = pie.operator("machin3.open_library_blend", text="Open %s" % (os.path.basename(blendpath)))
                    op.blendpath = blendpath
                    op.library = library

                else:
                    pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

        elif context.mode == "SCULPT":
                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

                self.draw_mesh_modes(context, pie)

                pie.separator()

                pie.separator()

                pie.separator()

        elif context.mode == "PAINT_TEXTURE":
                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

                self.draw_mesh_modes(context, pie)

                box = pie.split()
                column = box.column()
                column.scale_y = 1.5
                column.scale_x = 1.5

                row = column.row(align=True)
                row.prop(active.data, "use_paint_mask", text="", icon="FACESEL")

                pie.separator()

                pie.separator()

        elif context.mode == "PAINT_WEIGHT":
                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

                self.draw_mesh_modes(context, pie)

                box = pie.split()
                column = box.column()
                column.scale_y = 1.5
                column.scale_x = 1.5

                row = column.row(align=True)
                row.prop(active.data, "use_paint_mask", text="", icon="FACESEL")
                row.prop(active.data, "use_paint_mask_vertex", text="", icon="VERTEXSEL")

                pie.separator()

                pie.separator()

        elif context.mode == "PAINT_VERTEX":
                pie.separator()

                pie.separator()

                pie.separator()

                pie.separator()

                self.draw_mesh_modes(context, pie)

                box = pie.split()
                column = box.column()
                column.scale_y = 1.5
                column.scale_x = 1.5

                row = column.row(align=True)
                row.prop(active.data, "use_paint_mask", text="", icon="FACESEL")
                row.prop(active.data, "use_paint_mask_vertex", text="", icon="VERTEXSEL")

                pie.separator()

                pie.separator()

    def draw_gp_modes(self, context, pie):
        box = pie.split()
        column = box.column()
        column.scale_y = 1.5
        column.scale_x = 1.5

        row = column.row(align=True)
        r = row.row(align=True)
        r.active = False if context.mode == "WEIGHT_GPENCIL" else True
        r.operator("object.mode_set", text="", icon="WPAINT_HLT").mode = 'WEIGHT_GPENCIL'
        r = row.row(align=True)
        r.active = False if context.mode == "PAINT_GPENCIL" else True
        r.operator("object.mode_set", text="", icon="GREASEPENCIL").mode = 'PAINT_GPENCIL'
        r = row.row(align=True)
        r.active = False if context.mode == "SCULPT_GPENCIL" else True
        r.operator("object.mode_set", text="", icon="SCULPTMODE_HLT").mode = 'SCULPT_GPENCIL'
        r = row.row(align=True)
        r.active = False if context.mode == "OBJECT" else True
        r.operator("object.mode_set", text="", icon="OBJECT_DATA").mode = 'OBJECT'
        r = row.row(align=True)
        r.active = False if context.mode == 'EDIT_GPENCIL' else True
        r.operator("object.mode_set", text="", icon="EDITMODE_HLT").mode = 'EDIT_GPENCIL'

    def draw_gp_extra(self, active, pie):
        box = pie.split()
        column = box.column(align=True)

        row = column.row(align=True)
        row.scale_y = 1.5

        row.operator('machin3.shrinkwrap_grease_pencil', text='Shrinkwrap')
        row.prop(active.data, 'zdepth_offset', text='')

        opacity = [mod for mod in active.grease_pencil_modifiers if mod.type == 'GP_OPACITY']
        thickness = [mod for mod in active.grease_pencil_modifiers if mod.type == 'GP_THICK']

        if opacity:
            row = column.row(align=True)
            row.prop(opacity[0], 'factor', text='Opacity')

        if thickness:
            row = column.row(align=True)
            row.prop(thickness[0], 'thickness_factor', text='Thickness')

    def draw_mesh_modes(self, context, pie):
        box = pie.split()
        column = box.column()
        column.scale_y = 1.5
        column.scale_x = 1.5

        row = column.row(align=True)

        r = row.row(align=True)
        r.active = False if context.mode == 'PAINT_GPENCIL' else True
        r.operator("machin3.surface_draw_mode", text="", icon="GREASEPENCIL")

        r = row.row(align=True)
        r.active = False if context.mode == 'TEXTURE_PAINT' else True
        r.operator("object.mode_set", text="", icon="TPAINT_HLT").mode = 'TEXTURE_PAINT'

        r = row.row(align=True)
        r.active = False if context.mode == 'WEIGHT_PAINT' else True
        r.operator("object.mode_set", text="", icon="WPAINT_HLT").mode = 'WEIGHT_PAINT'

        r = row.row(align=True)
        r.active = False if context.mode == 'VERTEX_PAINT' else True
        r.operator("object.mode_set", text="", icon="VPAINT_HLT").mode = 'VERTEX_PAINT'

        r = row.row(align=True)
        r.active = False if context.mode == 'SCULPT' else True
        r.operator("object.mode_set", text="", icon="SCULPTMODE_HLT").mode = 'SCULPT'

        r = row.row(align=True)
        r.active = False if context.mode == 'OBJECT' else True
        r.operator("object.mode_set", text="", icon="OBJECT_DATA").mode = 'OBJECT'

        r = row.row(align=True)
        r.active = False if context.mode == 'EDIT_MESH' else True
        r.operator("object.mode_set", text="", icon="EDITMODE_HLT").mode = 'EDIT'
    ####M3

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        toolsettings = context.tool_settings

        active = context.active_object
        area = context.area
        ## WARNING area.type 和area.ui_type不一样
        mode = context.mode
        is_m3 = get_prefs().使用M3模式切换饼菜单    #替换M3模式
        
        #m3
        global decalmachine
        if decalmachine is None:
            decalmachine, _, _, _ = get_addon("DECALmachine")
        #m3

        
        if is_m3 and area.type in ('VIEW_3D','IMAGE_EDITOR'):
            if active:
                self.M3(context,active,toolsettings)

            else:
                self.空(context)
        
        else:
            self.萌新模式(context,area)
        
        print(f"ui_tyep({area.ui_type})_context.mode({context.mode})")

    def 萌新模式(self,context,area):        
        layout = self.layout
        pie = layout.menu_pie()
        ui = area.type
        space = context.space_data
        if ui == 'VIEW_3D': #3D
            self.空(context)

        elif ui == 'NODE_EDITOR':#节点编辑
            self.节点编辑(area,context)

        elif ui == 'OUTLINER':#大纲
            pie.prop_enum(space, "display_mode",value = 'SCENES')
            pie.prop_enum(space, "display_mode",value = 'VIEW_LAYER')
            pie.prop_enum(space, "display_mode",value = 'SEQUENCE')
            pie.prop_enum(space, "display_mode",value = 'LIBRARIES')
            pie.prop_enum(space, "display_mode",value = 'DATA_API')
            pie.prop_enum(space, "display_mode",value = 'LIBRARY_OVERRIDES')
            pie.prop_enum(space, "display_mode",value = 'ORPHAN_DATA')

        elif ui == 'PROPERTIES':#属性
            self.空(context)
            # pie.prop(context.area,'ui_type')

        elif ui == 'FILE_BROWSER':#文件浏览
            self.空(context)

        else:
            self.空(context)

    def 节点编辑(self,area,context):
        ui = area.ui_type

        if ui == 'ShaderNodeTree':#着色器
            pass

        if ui == 'CompositorNodeTree':
            pass

        if ui == 'GeometryNodeTree':
            pass

        if ui == 'TextureNodeTree':
            pass

        else:
            self.空(context)



    def 模式切换(self,context,pie):
        self.空(context)

    def 空(self,context):
        layout = self.layout
        pie = layout.menu_pie()

        p = pie.box()
        p.label(text = '啥都还没写呢，快去找小萌新填充内容吧')
        p = pie.box()
        p.label(text = f'OBJmode_({context.mode})')
        p = pie.box()
        p.label(text = f'area.ui_type({context.area.ui_type})')#context.area.ui_type
        p = pie.box()
        p.label(text = f'活动物体({context.active_object})')
        p = pie.box()
        p.label(text = f'context({context})')
        p = pie.box()
        p.label(text = f'area.type({context.area.type})')
        # p = pie.box()
        # p.label(text = f'.mode_({context.mode})')
        # p = pie.box()
        # p.label(text = f'.mode_({context.mode})')

        # pie.separator()

        # pie.separator()

        # pie.separator()

        # pie.separator()

        # pie.separator()

        # pie.separator()

        # pie.separator()       

class PieViewport(Menu):
    bl_idname = "EMMMMM_MT_viewport_pie"
    bl_label = "第一个PIE菜单测试"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        C = context
        Co = C.object

        active = context.active_object
        shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        overlay = context.space_data.overlay

        if C.area.type == "VIEW_3D" and active:
            if Co.type == "MESH":
                if Co.mode == "OBJECT":
                    # 左
                    p1 = pie.prop_enum(shading, "type", value='WIREFRAME')
                    p1

                    # 右
                    p2 = pie.prop_enum(shading, "type", value='SOLID')
                    p2

                    # 底
                    p3 = pie.prop(overlay, "show_wireframes",
                                  icon='MOD_WIREFRAME')
                    p3

                    # 顶
                    p4 = pie.prop(
                        overlay, "show_face_orientation", icon='FACESEL')
                    p4

                    # 左上
                    p5 = pie.prop_enum(shading, "type", value='MATERIAL')
                    p5

                    #右上
                    p6 = pie.prop_enum(shading, "type", value='RENDERED')
                    p6

                    #左下
                    p7 = pie.operator('object.shade_smooth')
                    p7

                    #右下
                    p8 = pie.operator('object.shade_flat')
                    p8

class PieSpace_pie(Menu):
    bl_idname = "EMMMMM_MT_space_pie"
    bl_label = "空格饼菜单"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        C = context
        Co = C.object

        active = context.active_object
        shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        overlay = context.space_data.overlay

        if C.area.type == "VIEW_3D" and active:
            if Co.type == "MESH":
                if Co.mode == "OBJECT":
                    # 左
                    p1 = pie.prop_enum(shading, "type", value='WIREFRAME')
                    p1

                    # 右
                    p2 = pie.prop_enum(shading, "type", value='SOLID')
                    p2

                    # 底
                    p3 = pie.prop(overlay, "show_wireframes",
                                  icon='MOD_WIREFRAME')
                    p3

                    # 顶
                    p4 = pie.prop(
                        overlay, "show_face_orientation", icon='FACESEL')
                    p4

                    # 左上
                    p5 = pie.prop_enum(shading, "type", value='MATERIAL')
                    p5

                    #右上
                    p6 = pie.prop_enum(shading, "type", value='RENDERED')
                    p6

                    #左下
                    p7 = pie.operator('object.shade_smooth')
                    p7

                    #右下
                    p8 = pie.operator('object.shade_flat')
                    p8


class PieSelect_pie(Menu):
    bl_idname = "EMMMMM_MT_select_pie"
    bl_label = "选择饼菜单"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        C = context
        Co = C.object

        active = context.active_object
        shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        overlay = context.space_data.overlay

        if C.area.type == "VIEW_3D" and active:
            # #网格
            # if Co.type == "MESH":
                #物体模式
                if Co.mode == "OBJECT":
                    # 左
                    b = pie.column(align=True)
                    b.scale_y = 1.3
                    b.scale_x = 0.8
                    # b.ui_units_y = -80
                    b.ui_units_x = 10
                    c = b.row(align=False)
                    c.operator_enum("object.select_by_type", "type")
                    c.operator_enum("object.select_grouped", "type")

                    # 右
                    b = pie.column(align=True)
                    b.scale_y = 1.7
                    b.scale_x = 1
                    c = b.row(align=True)
                    c.operator('object.select_mirror')
                    c.operator('object.select_pattern')
                    c = b.row(align=True)
                    c.operator('object.select_all',text='反选',icon='UV_SYNC_SELECT').action = 'INVERT'
                    b.separator(factor=0.5)

                    c = b.row()
                    c.separator(factor=0.5)
                    c = b.row(align=True)
                    c.operator('object.select_random',icon='RESTRICT_SELECT_ON')
                    c = b.row(align=True)
                    c.operator('object.select_camera',icon='CAMERA_DATA')

                    # 底
                    b = pie.column(align=True)
                    b.scale_y = 1.3
                    b.scale_x = 1.3
                    b.operator_enum("object.select_linked", "type")

                    # 顶
                    b = pie.column(align=True)
                    b.scale_y = 1.5
                    b.scale_x = 1
                    c = b.row(align=True)
                    operator = c.operator('object.select_hierarchy',text='扩展父级')
                    operator.direction = 'PARENT'
                    operator.extend = True
                    operator = c.operator('object.select_hierarchy',text='扩展子级')
                    operator.direction = 'CHILD'
                    operator.extend = True
                    b.separator(factor=0.5)

                    c = b.row(align=True)
                    operator = c.operator('object.select_hierarchy',text='父级')
                    operator.direction = 'PARENT'
                    operator.extend = False
                    operator = c.operator('object.select_hierarchy',text='子级')
                    operator.direction = 'CHILD'
                    operator.extend = False

                    # 左上
                    # p5 = pie.operator('mesh.select_random')
                    # p5

                    #右上
                    # # pie.ui_units_x = 0.5
                    # # pie.ui_units_y = 0.5
                    # b = pie.column(align=True)
                    # b.ui_units_y = 5
                    # b.scale_y = 1.5
                    # b.scale_x = 3
                    # b.alert = True
                    # b.operator('mesh.select_more', icon='ADD', text='')

                    #左下
                    # p7 = pie.operator('mesh.select_face_by_sides').number = 3
                    # p7

                    #右下
                    # b = pie.column(align=True)
                    # b.ui_units_y = -20
                    # b.scale_y = 1.5
                    # b.scale_x = 3
                    # b.alert = True
                    # b.operator('mesh.select_less', icon='REMOVE', text='')



                #编辑模式
                if Co.mode == "EDIT" and Co.type == "MESH":
                    # 左
                    p1 = pie.operator('mesh.select_nth')
                    p1

                    # 右
                    b = pie.column(align=True)
                    b.scale_y = 1.3
                    b.scale_x = 0.8
                    b.ui_units_y = 7
                    c = b.row(align=True)
                    c.operator('mesh.select_linked')
                    c.operator('mesh.faces_select_linked_flat')
                    c = b.row(align=True)
                    c.operator('mesh.select_axis')
                    c.operator('mesh.select_ungrouped')
                    c = b.row(align=True)
                    c.operator('mesh.loop_to_region')
                    c.operator('mesh.region_to_loop')
                    c = b.row(align=True)
                    c.operator('mesh.loop_multi_select').ring = False
                    c.operator('mesh.edges_select_sharp')

                    # 底
                    b = pie.column(align=True)
                    b.scale_y = 1.1
                    b.scale_x = 1.3
                    # b = b.row()
                    b.operator('mesh.select_similar_region')
                    b.operator_enum("mesh.select_similar", "type")
                    # b.menu(menu='VIEW3D_MT_edit_mesh_select_more_less')

                    # 顶
                    b = pie.column(align=True)
                    b.scale_y = 1.5
                    b.scale_x = 0.8
                    b.operator('mesh.select_non_manifold')
                    c = b.row(align=True)
                    c.operator('mesh.select_loose')
                    c.operator('mesh.select_interior_faces')
                    c = b.row(align=True)
                    c.operator('mesh.select_mirror')
                    c.operator('mesh.select_ungrouped')
                    # b.scale_y = 1.1
                    b.operator('mesh.select_all',text='反选').action = 'INVERT'
                    
                    # 左上
                    p5 = pie.operator('mesh.select_random')
                    p5

                    #右上
                    # pie.ui_units_x = 0.5
                    # pie.ui_units_y = 0.5
                    b = pie.column(align=True)
                    b.ui_units_y = 5
                    b.scale_y = 1.5
                    b.scale_x = 3
                    b.alert = True
                    b.operator('mesh.select_more', icon='ADD',text='')
                    
                    #左下
                    p7 = pie.operator('mesh.select_face_by_sides').number = 3
                    p7


                    #右下
                    b = pie.column(align=True)
                    b.ui_units_y = -20
                    b.scale_y = 1.5
                    b.scale_x = 3
                    b.alert = True
                    b.operator('mesh.select_less', icon='REMOVE',text='')

class PieDelete_pie(Menu):
    bl_idname = "EMMMMM_MT_delete_pie"
    bl_label = "删除饼菜单"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        C = context
        Co = C.object


        active = context.active_object
        shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        overlay = context.space_data.overlay

        if C.area.type == "VIEW_3D" and active:
            if Co.type == "MESH":
                # if Co.mode == "OBJECT":
                #     # 左
                #     p1 = pie.prop_enum(shading, "type", value='WIREFRAME')
                #     p1

                #     # 右
                #     p2 = pie.prop_enum(shading, "type", value='SOLID')
                #     p2

                #     # 底
                #     p3 = pie.prop(overlay, "show_wireframes",
                #                   icon='MOD_WIREFRAME')
                #     p3

                #     # 顶
                #     p4 = pie.prop(
                #         overlay, "show_face_orientation", icon='FACESEL')
                #     p4

                #     # 左上
                #     p5 = pie.prop_enum(shading, "type", value='MATERIAL')
                #     p5

                #     #右上
                #     p6 = pie.prop_enum(shading, "type", value='RENDERED')
                #     p6

                #     #左下
                #     p7 = pie.operator('object.shade_smooth')
                #     p7

                #     #右下
                #     p8 = pie.operator('object.shade_flat')
                #     p8

                if Co.mode == "EDIT":
                    # 左
                    # p1 = pie.prop_enum(shading, "type", value='WIREFRAME')
                    p1 = pie.operator('mesh.delete',icon='VERTEXSEL',text='顶点').type = 'VERT'
                    p1

                    # 右
                    # p2 = pie.prop_enum(shading, "type", value='SOLID')
                    p2 = pie.operator('mesh.delete',icon='EDGESEL',text='边').type = 'EDGE'
                    p2

                    # 底
                    p3 = pie.operator('mesh.delete',icon='FACESEL',text='面').type = 'FACE'
                    p3

                    # 顶
                    # p4 = pie.prop(overlay, "show_face_orientation", icon='FACESEL')
                    p4 = pie.operator('mesh.delete_edgeloop',text='循环边')
                    p4

                    # 左上
                    # p5 = pie.prop_enum(shading, "type", value='MATERIAL')
                    p5 = pie.operator('mesh.delete', text='仅面').type = 'ONLY_FACE'
                    # separator()
                    p5

                    #右上
                    p6 = pie.operator('mesh.delete', text='边和面').type = 'EDGE_FACE'
                    p6


                    #左下
                    p7 = pie.operator('mesh.dissolve_limited')
                    p7



                    #右下
                    p8 = pie.operator('mesh.edge_collapse')
                    p8


class Pie_C_pie(Menu):
    bl_idname = "EMMMMM_MT_c_pie"
    bl_label = "C键饼菜单测试"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        C = context
        Co = C.object

        active = context.active_object
        shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        overlay = context.space_data.overlay
        if C.area.type == "VIEW_3D" and active:
            if Co.type == "MESH":
                if Co.mode == "EDIT":
                    #左
                    # pie.
                    try:
                        pie.operator("mesh.merge",text='首选点').type = 'FIRST'
                    except TypeError:
                        pass


                    # 右
                    try:
                        pie.operator("mesh.merge",text = '末选点').type = 'LAST'
                    except Exception:
                        pass

                    # 底
                    p3 = pie.operator("mesh.merge",text='中心').type = 'CENTER'
                    p3

                    # 顶
                    p4 = pie.operator("mesh.merge",text='游标').type = 'CURSOR'
                    p4

                    # 左上
                    p5 = pie.operator("mesh.merge",text='塌陷').type = 'COLLAPSE'
                    p5

                    #右上
                    # p6 = pie.operator("mesh.merge").type = 'CENTER'
                    # p6 = pie.separator_spacer()
                    p6 = pie.separator()
                    p6

                    #左下
                    p6 = pie.separator()
                    p6

                    #右下
                    p8 = pie.operator("mesh.remove_doubles").threshold = get_prefs().remove_doubles_threshold
                    p8

                else:
                    pass
                    # p1 = pie.prop_enum(shading, "type", value='WIREFRAME')
                    # p1

                    # # 右
                    # p2 = pie.prop_enum(shading, "type", value='SOLID')
                    # p2

                    # # 底
                    # p3 = pie.prop(overlay, "show_wireframes",icon='MOD_WIREFRAME')
                    # p3
                    
                    # # 顶
                    # p4 = pie.prop(overlay, "show_face_orientation",icon='FACESEL')
                    # p4

                    # # 左上
                    # p5 = pie.prop_enum(shading, "type", value='MATERIAL')
                    # p5


                    # #右上
                    # p6 = pie.prop_enum(shading, "type", value='RENDERED')
                    # p6
                    
                    
                    # #左下
                    # p7 = pie.operator('object.shade_smooth')
                    # p7


                    # #右下
                    # p8 = pie.operator('object.shade_flat')
                    # p8



class Pie_B_pie(Menu):
    bl_idname = "EMMMMM_MT_b_pie"
    bl_label = "B键饼菜单"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        C = context
        Co = C.object

        active = context.active_object
        shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        overlay = context.space_data.overlay

        if C.area.type == "VIEW_3D" and active:
            if Co.type == "MESH":
                # if Co.mode == "OBJECT":
                    # # 左
                    # p1 = pie.prop_enum(shading, "type", value='WIREFRAME')
                    # p1

                    # # 右
                    # p2 = pie.prop_enum(shading, "type", value='SOLID')
                    # p2

                    # # 底
                    # p3 = pie.prop(overlay, "show_wireframes",
                    #               icon='MOD_WIREFRAME')
                    # p3

                    # # 顶
                    # p4 = pie.prop(
                    #     overlay, "show_face_orientation", icon='FACESEL')
                    # p4

                    # # 左上
                    # p5 = pie.prop_enum(shading, "type", value='MATERIAL')
                    # p5

                    # #右上
                    # p6 = pie.prop_enum(shading, "type", value='RENDERED')
                    # p6

                    # #左下
                    # p7 = pie.operator('object.shade_smooth')
                    # p7

                    # #右下
                    # p8 = pie.operator('object.shade_flat')
                    # p8
                    # pass

                if Co.mode == "EDIT":
                    # 左
                    p1 = pie.separator()
                    

                    # 右
                    p2 = pie.operator('mesh.mark_sharp')
                    p2.clear = p2.clear ^ False

                    # 底
                    p3 = pie.prop(overlay, "show_wireframes",
                                  icon='MOD_WIREFRAME')
                    

                    # # 顶
                    p4 = pie.prop(
                        overlay, "show_face_orientation", icon='FACESEL')
                    

                    # 左上
                    p5 = pie.operator('mesh.mark_sharp')
                    p5.use_verts = True
                    p5.clear = p5.clear ^ False

                    #右上
                    p6 = pie.prop_enum(shading, "type", value='RENDERED')
                    

                    #左下
                    p7 = pie.operator('mesh.mark_freestyle_edge')
                    p7.clear = p7.clear ^ False

                    #右下
                    p8 = pie.operator('mesh.mark_seam')
                    p8.clear = p8.clear ^ False

# bpy.ops.transform.edge_crease(value=1)
# bpy.ops.transform.edge_bevelweight(value=1)
# bpy.ops.mesh.mark_seam(clear=True)
# bpy.ops.mesh.mark_seam(clear=False)

# bpy.ops.mesh.mark_sharp(use_verts=True)
# bpy.ops.mesh.mark_sharp(use_verts=False)
# bpy.ops.mesh.mark_sharp()
# bpy.ops.mesh.mark_sharp(clear=True)

# bpy.ops.mesh.mark_freestyle_edge(clear=False)
# bpy.ops.mesh.mark_freestyle_edge(clear=True)

class Pie_V_pie(Menu):
    bl_idname = "EMMMMM_MT_v_pie"
    bl_label = "V键饼菜单"    
    bl_options = {'REGISTER', 'UNDO'}

    def 通用视图绘制(self,pie,Co,display):
        # 左
        b = pie.box()
        b = b.column()
        b.scale_y = 1.3
        b.scale_x = 0.8
        # b.ui_units_y = -80
        # b.ui_units_x = 10
        c = b.split(align=True)
        c.prop(Co, 'name',text='')
        c.prop_menu_enum(Co, "display_type")
        OBJECT_PT_display_presets.draw_panel_header(c)

        c = b.split(align=True,factor=0.5)
        c.prop(Co, 'show_name', toggle=True, emboss=True)
        c.prop(Co, 'show_axis', toggle=True, emboss=True)
        c = b.split(align=True,factor=0.5)
        c.prop(Co, 'show_wire')
        c.prop(Co, 'show_all_edges')
        c = b.split(align=True,factor=0.5)
        c.prop(display, 'show_shadows')
        c.prop(Co, 'show_in_front')
        c = b.row(align=True)
        c.prop(Co, 'color',text='')
        c.prop(Co, 'show_bounds',text='',icon='SHADING_BBOX')
        c.prop_menu_enum(Co, "display_bounds_type",text='边界类型')

    def 骨骼_视图切换(self,pie,Co):
        A_骨架 = bpy.context.active_object.data

        b = pie.box()
        b = b.column()
        b.scale_y = 1.3
        b.scale_x = 0.8
        # b.ui_units_y = -80
        # b.ui_units_x = 10
        b.prop_menu_enum(A_骨架, "display_type")
        c = b.split(align=True,factor=0.5)
        c.prop(A_骨架, 'show_names',emboss = True,text='名称')
        c.prop(A_骨架, 'show_bone_custom_shapes',emboss = True,text='自定义形状')
        c = b.split(align=True,factor=0.5)
        c.prop(A_骨架, 'show_group_colors',text='组颜色',emboss = True)
        c.prop(Co, 'show_in_front',text='在前面',emboss = True)
        c = b.split(align=True,factor=0.5)
        c.prop(A_骨架, 'show_axes',emboss = True)
        c.prop(A_骨架, 'axes_position',emboss = True)
        


    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        C = context
        Co = C.object

        active = context.active_object
        shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        overlay = context.space_data.overlay
        display = Co.display
        活动物体类型 = bpy.context.active_object.type

        if C.area.type == "VIEW_3D" and active:
                if Co.mode == "EDIT":
                    pass
                
                OBJ = (Co.mode == "OBJECT")
                if 活动物体类型 == 'MESH'and OBJ:
                    self.通用视图绘制(pie,Co,display)
                if 活动物体类型 == 'ARMATURE':
                    self.通用视图绘制(pie,Co,display)
                    self.骨骼_视图切换(pie,Co)


    def obj_display(pie, Co, layout):
        column = layout.column(align=True)

        row = column.row()
        row = column.split(factor=0.6)
        row.prop_menu_enum(Co, "display_type")
        row.props_enum(Co, "display_type")


def register():
    bpy.utils.register_class(PieViewport)

def unregister():
    bpy.utils.unregister_class(PieViewport)


if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="EMMMMM_MT_viewport_pie")
