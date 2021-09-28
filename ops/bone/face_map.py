import bpy
from bpy.types import Operator
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class
"""
#TODO通过所选骨骼创建面映射
#TODO通过顶点组权重大于多少添加顶点进面映射
#TODO清除为0的面映射
"""

class 骨骼面映射工具啊(Operator):
    bl_idname = "emm.bone_face_map"
    bl_label = "面映射"
    bl_options = { 'UNDO'}#'REGISTER'
    bl_description = "骨骼面映射工具啊"

    mode: StringProperty(name = '模式',default='face_map')

    def execute(self, context):
        for A in bpy.data.objects:
            SeBolis = []
            if A.parent == bpy.context.object:    
                # print(A)
                Obj = bpy.context.object
                type = Obj.type
                Fmp = A.face_maps

                if type == 'ARMATURE':
                    for i in bpy.context.object.data.bones:
                        if i.select:
                            name = i.name
                            SeBolis.append(name)

                            # print(name)
                            if name not in Fmp or Fmp == None:
                                Fmp.new(name = name)

        return {'FINISHED'}         

if __name__ == "__main__":
    register_class(骨骼面映射工具啊)