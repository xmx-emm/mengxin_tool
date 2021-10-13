import bpy
import inspect
import sys

from bpy.utils import register_class, unregister_class
from bpy.types import Menu,Operator

class EMM_MESH_MT_FACE_MAP(Menu):
    bl_label = "网格面映射菜单"
    
    def draw(self, _context):
        layout = self.layout
        layout.separator()
        layout.separator()
        layout.separator()
        layout.separator()
        layout.operator("emm.mesh_face_map", text="清理面映射").mode = '清理'
        layout.operator("emm.mesh_face_map", text="Move to Bottom").mode = 'BOTTOM'



class 右键上下文菜单_cl(Operator):  #TODO 复制属性菜单
    bl_idname = "emm.context_menu"
    bl_label = "复制属性菜单"
    bl_description = ""
    bl_options = {'INTERNAL'}

    prop: bpy.props.StringProperty(options={'SKIP_SAVE'})
    operator: bpy.props.StringProperty(options={'SKIP_SAVE'})
    name: bpy.props.StringProperty(options={'SKIP_SAVE'})

    def draw_menu(self, menu, context):
        layout = menu.layout
        layout.operator_context = 'INVOKE_DEFAULT'


        button_pointer = getattr(context, "button_pointer", None)
        button_prop = getattr(context, "button_prop", None)

        button_operator = getattr(context, "button_operator", None)
        layout.label(text=self.prop, )

    def execute(self, context):

        context.window_manager.popup_menu(
            self.draw_menu, title=self.bl_label)
        return {'FINISHED'}


排除类列表 = (
    Menu,
    Operator,
)

def 注册菜单():

    ###这个方法需要注意名称的长度，注册的顺序是按名称的长度来的，子面板要后注册
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            try:
                register_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)


def 注销菜单():
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            
            try:
                unregister_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)

            # unregister_class(class_)
    