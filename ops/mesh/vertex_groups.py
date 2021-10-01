import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
# from ..utils.name import *
from bpy.props import StringProperty

import re
def generate_name(name,前缀,后缀):
    return 前缀+name+后缀
def match_name(name,前缀,后缀): #匹配名称
    pattern = 前缀+r'.+'+后缀    
    return re.findall(pattern=pattern,string=name)

def get_infix(name,前缀,后缀):
    name = str(name)
    name = name.split(前缀)[1]
    return name.split(后缀)[0]



def 创建物体(type,name):
    subtype = None
    data=None
    ver=None
    edge=None
    face=None

    type: StringProperty(name='type',default='')

    if type in ('曲线','CURVE',
                '曲面','SURFACE',
                '字体','FONT'): #'POLY','NURBS' BEZIER
        bpy.data.curves.new(name,type)
        
        bpy.data.curves[name].splines.new(subtype)
    

    if type in ('网格','MESH'):        
        new = bpy.data.meshes.new(name)
        return new


def create_mesh_face_hack(faces):
    faces_copy = []
    for f in faces:
        f_copy = []
        for i in f:
            if i not in f_copy:
                f_copy.append(i)
        faces_copy.append(f_copy)
    faces[:] = faces_copy


from bpy_extras import object_utils

def create_mesh_object(self, context, verts, edges, faces, name):

    create_mesh_face_hack(faces)

    # Create new mesh
    mesh = bpy.data.meshes.new(name)
    # Make a mesh from a list of verts/edges/faces.
    mesh.from_pydata(verts, edges, faces)
    # Update mesh geometry after adding stuff.
    mesh.update()

    return object_utils.object_data_add(context, mesh, operator=self)



class EMM_VERTEX_GROUPS(Operator):
    bl_idname = "emm.join_mesh"
    bl_label = "顶点组工具集"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "顶点组操作集！！！"

    mode: StringProperty(name='模式',default='合并')

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        # len(sel) >= 1
        return context.active_object.type =='MESH'

    def execute(self, context):
        sel = context.selected_objects
        act = context.active_object.copy()
        mode = self.mode
        objlist = []

        前缀 = 'join_'
        后缀 = '_萌新工具箱'

        if mode == '合并':
            for obj in sel:
                if len(sel) <= 1:                
                    self.report({"ERROR"}, "请选择两个或两个以上物体")
                    # break
                    return {'FINISHED'}


                
                if obj.EMM.is_join_obj:
                    objlist.append(obj.name)
                    self.report({"INFO"}, "此物体已是合并顶点组")

                    continue

                if obj.type !='MESH':continue


                name = generate_name(obj.name_full,前缀,后缀)


                vg = obj.vertex_groups
                
                if name not in vg:   #如果没有这个顶点组就创建
                    vg.new(name =name)
                    print(name)
                
                #向顶点组添加顶点
                vgl = []    
                for edge in obj.data.edges: #vertices
                    vgl.append(edge.index)
                vg[name].add(vgl,1,'ADD')#('REPLACE', 'ADD', 'SUBTRACT'

                vgl.clear()

            bpy.ops.object.join()

            context.active_object.EMM.is_join_obj = True    #是合并过的物体
            return {'FINISHED'}
        if mode == '拆分':
            for obj in sel:
                for vg in obj.vertex_groups:

                    if match_name(vg.name,前缀,后缀):#如果匹配前后缀

                        name = get_infix(vg.name,前缀,后缀)#获取中缀，就是原物体的名称

                        if name ==  obj.name:
                            print(f'保留一个物体不被分离，就是原本的物体{name}')

                            continue   #保留一个物体不被分离，就是原本的物体

                        # if name in  bpy.data.meshes:
                        #     print(f'已有这个物体数据__{name}')
                        #     continue

                        name = 创建物体('MESH',name = name)
                        print(name.name)

            print('拆_______')
            return {'FINISHED'}


if __name__ == "__main__":
    register_class(EMM_VERTEX_GROUPS)
