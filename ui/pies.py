import bpy
from bpy.types import Menu
from ..utils.registration import get_prefs
from .presets.object_display_presets import OBJECT_PT_display_presets


class PieModes_pie(Menu):
    bl_idname = "EMMMMM_MT_modes_pie"
    bl_label = "模式饼菜单"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        C = context
        Co = C.object

        active = context.active_object
        shading = C.space_data.shading  # 显示切换 WIREFRAME    MATERIAL    RENDERED    SOLID
        overlay = context.space_data.overlay

        if C.area.type == "VIEW_3D" and active:
            if Co.type=="MESH":
                if Co.mode=="OBJECT":
                    # 左
                    p1 = pie.prop_enum(shading, "type", value='WIREFRAME')
                    p1

                    # 右
                    p2 = pie.prop_enum(shading, "type", value='SOLID')
                    p2

                    # 底
                    p3 = pie.prop(overlay, "show_wireframes",icon='MOD_WIREFRAME')
                    p3
                    
                    # 顶
                    p4 = pie.prop(overlay, "show_face_orientation",icon='FACESEL')
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
                
                if Co.mode == "OBJECT":
                    if 活动物体类型 == 'MESH':
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
