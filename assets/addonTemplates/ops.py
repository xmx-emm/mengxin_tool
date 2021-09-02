import bpy
from bpy.types import Operator as OPS
from bpy.utils import register_class,unregister_class


class emm(OPS):
    """这是这个操作符的提示"""
    bl_idname = 'emm.emm'
    bl_label = '新建顶点组'

    def __init__(self,prn = ""):
        self.prn = prn  #前缀
    def __del__(self):
        pass
    def emm(self,context):
        bpy.ops.mesh.primitive_uv_sphere_add()
    def execute(self,context):
        self.emm(context)        
        return {'FINISHED'}
    @classmethod
    def poll(cls,conext):
        pass
def register():
    register_class(emm)

def unregister():
    unregister_class(emm)

if __name__ == "__main__":
    register()
