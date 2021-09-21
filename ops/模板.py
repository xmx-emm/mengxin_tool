import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class



class 拆分曲线(Operator):
    bl_idname = "emm.separate_splines"
    bl_label = "拆分曲线"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "拆分曲线啊"

    def execute(self, context):
        pass

if __name__ == "__main__":
    register_class(拆分曲线)
