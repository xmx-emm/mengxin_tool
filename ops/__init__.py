from .curve import 注册曲线OPS,注销曲线OPS
from .mesh import 注册网格OPS,注销网格OPS
from .object import 注册物体OPS,注销物体OPS
from .bone import 注册骨骼OPS,注销骨骼OPS



import bpy
import inspect
import sys

from bpy.props import StringProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class 杂项操作(Operator):
    bl_idname = "emm.misc"
    bl_label = "杂项操作"
    bl_options = { 'UNDO'}#'REGISTER'
    bl_description = "杂项操作啊"

    mode: StringProperty(name = '模式',default='')

    def execute(self, context):
        mode = self.moda
        
        if mode == '打开插件面板':
            pass

        return {'FINISHED'}         




排除类列表 = (
    Operator,
)


def 注册OPS():
    try:
        注册曲线OPS()
        注册网格OPS()
        注册物体OPS()
        注册骨骼OPS()

        ###这个方法需要注意名称的长度，注册的顺序是按名称的长度来的，子面板要后注册
        for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
            if class_ not in 排除类列表:
                try:
                    register_class(class_)
                    # print(class_)
                except Exception as e:
                    print(e.args)

    except Exception as e:
        print(e.args)


def 注销OPS():
    try:
        注销曲线OPS()
        注销网格OPS()
        注销物体OPS()
        注销骨骼OPS()
        for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
            if class_ not in 排除类列表:
                
                try:
                    unregister_class(class_)
                    # print(class_)
                except Exception as e:
                    print(e.args)

    except Exception as e:
        print(e.args)
