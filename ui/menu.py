import bpy


# 案例1.基本菜单
class BasicMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_test"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.select_all",
                        text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")


bpy.utils.register_class(BasicMenu)
# 通过代码 调用菜单
bpy.ops.wm.call_menu(name="OBJECT_MT_select_test")


# 案例2.子菜单
class SubMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_submenu"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.select_all",
                        text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")

        # 将操作符作为子菜单访问  access this operator as a submenu
        layout.operator_menu_enum(
            "object.select_by_type", "type", text="Select All by Type...")

        layout.separator()

        # 将操作符的选项展开到菜单中  expand each operator option into this menu
        layout.operator_enum("object.light_add", "type")

        layout.separator()

        # layout调用已存在的菜单  需要传入 菜单类 的 bl_idname
        layout.menu("VIEW3D_MT_transform")


bpy.utils.register_class(SubMenu)
bpy.ops.wm.call_menu(name="OBJECT_MT_select_submenu")


# 案例3.为文件菜单添加自定义菜单

# TOPBAR_MT_file 为顶栏的文件菜单
# 定义绘制函数  绘制函数中仍然有 self 和 context 作为两个基本参数
def menu_draw(self, context):
    self.layout.operator("wm.save_homefile")
    self.layout.prop(bpy.context.object, 'name')


# 将 menu_draw绘制函数 添加到 文件菜单下
bpy.types.TOPBAR_MT_file.append(menu_draw)
