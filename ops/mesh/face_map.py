import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty



#TODO清除为0的面映射

class 面映射工具(Operator):
    bl_idname = "emm.mesh_face_map"
    bl_label = "面映射工具"
    bl_options = {'UNDO'}#'REGISTER', 
    bl_description = "面映射工具啊"

    mode: StringProperty(name='mode',default='模式')

    def execute(self, context):
        mode = self.mode
        
        if mode == '清理':
            pass
        return {'FINISHED'}


if __name__ == "__main__":
    register_class(面映射工具)
