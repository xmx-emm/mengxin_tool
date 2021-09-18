import bpy
import inspect
import sys

from bpy.utils import register_class, unregister_class
from bpy.types import Menu

class EMM_MESH_MT_FACE_MAP(Menu):
    bl_label = "网格面映射菜单"
    
    def draw(self, _context):
        layout = self.layout
        layout.operator("object.shape_key_add", icon='ADD', text="New Shape from Mix").from_mix = True
        layout.separator()
        layout.operator("object.shape_key_mirror", icon='ARROW_LEFTRIGHT').use_topology = False
        layout.operator("object.shape_key_mirror", text="Mirror Shape Key (Topology)").use_topology = True
        layout.separator()
        layout.operator("object.join_shapes")
        layout.operator("object.shape_key_transfer")
        layout.separator()
        layout.operator("object.shape_key_remove", icon='X', text="Delete All Shape Keys").all = True
        layout.separator()
        layout.operator("object.shape_key_move", icon='TRIA_UP_BAR', text="Move to Top").type = 'TOP'
        layout.operator("object.shape_key_move", icon='TRIA_DOWN_BAR', text="Move to Bottom").type = 'BOTTOM'


排除类列表 = (
    Menu,
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
    