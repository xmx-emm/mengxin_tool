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
    bl_options = {'UNDO'}#'REGISTER', 
    bl_description = """
    合并以及拆分物体的工具，和ZB的子工具大师差不多
    如果合并的物体有相同的顶点组名称会出现拆分错误的问题

    shift 强制拆分
    ctrl     强制合并"""

    mode: StringProperty(name='模式',default='合并')

    前缀 = 'join_'
    后缀 = '_萌新工具箱'

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return context.active_object.type =='MESH'


    def invoke(self, context, event):
        if not event.alt and not event.shift and not event.ctrl and not event.oskey:
            if pr:print('左键')
            self.execute(context)
            return {'FINISHED'}
        if event.ctrl and not event.alt and not event.shift and not event.oskey:
            if pr:print('ctrl+左键')
            self.mode = '强制合并'
            self.execute(context)
            return {'FINISHED'}
        if event.shift and not event.alt and not event.ctrl and not event.oskey:
            if pr:print('shift+左键')
            self.mode = '强制拆分'
            self.execute(context)
            return {'FINISHED'}
        # if event.alt and not event.shift and not event.ctrl and not event.oskey:
        #     if pr:print('alt+左键')
        #     return {'FINISHED'}
        # if event.alt and event.shift and event.ctrl and not event.oskey:
        #     if pr:print('ctrl+alt+shift+左键')
        #     return {'FINISHED'}
        # elif event.oskey and not event.alt and not event.shift and not event.ctrl:
        #     if pr:print('os+左键')
        #     return {'FINISHED'}
        else:
            self.report({"INFO"}, self.bl_description)
            return {'FINISHED'}


    def execute(self, context):
        mode = self.mode
        前缀 = self.前缀
        后缀 = self.后缀
        sel = context.selected_objects.copy()  #所选对像
        act = context.active_object.copy()
        joinobjlist = []


        def 改名():
            for i in context.selected_objects:
                if i.type == 'MESH':
                    print(i.EMM.临时属性,i.EMM.临时属性2)
                    act = i.vertex_groups.active
                    # em = get_infix(i.EMM.临时属性,前缀,后缀) if i.EMM.临时属性2 != "" else get_infix(i.EMM.临时属性2,前缀,后缀) 
                    em = get_infix(act.name,前缀,后缀) 
                    i.name = em
                    i.data.name = em

                    # i.EMM.临时属性 = ''
                    # i.EMM.临时属性2 = ''

                    
            
        def 清理顶点组():            
            for i in context.selected_objects:
                if i.type == 'MESH':
                    
                    for vg in i.vertex_groups:
                        if match_name(vg.name,前缀,后缀):
                            i.vertex_groups.remove(vg)
                            


        def separate():
            for obj in sel:                
                context.view_layer.objects.active = obj

                if obj.EMM.is_join_obj:
                    obj.EMM.is_join_obj = False
                    for vg in obj.vertex_groups:

                        if match_name(vg.name,前缀,后缀):#如果匹配前后缀
                            name = get_infix(vg.name,前缀,后缀)#获取中缀，就是原物体的名称
                            
                            

                            if name ==  obj.name:
                                print(f'保留一个物体不被分离，就是原本的物体{name}')
                                # obj.EMM.临时属性2 = vg.name
                                # obj.EMM.临时属性 = ''
                                continue

                            else:
                                # obj.EMM.临时属性2 = ''
                                # obj.EMM.临时属性3 = vg.name
                                # obj.EMM.临时属性 = vg.name
                                pass
                            
                            if context.mode != 'EDIT_MESH':
                                bpy.ops.object.mode_set(mode='EDIT',toggle=True)                            
                                self.is_ObjectMode = True

                            bpy.ops.mesh.select_all(action='DESELECT')
                            obj.vertex_groups.active = vg
                            bpy.ops.object.vertex_group_select()
                            
                            print(f'vgname{vg.name},obj{obj}')
                            bpy.ops.mesh.separate(type='SELECTED')
                            bpy.context.object.vertex_groups.remove(vg)



                            # name = 创建物体('MESH',name = name)
                    # print('拆_______')

            # print(joinobjlist)
            if  hasattr(self, 'is_ObjectMode'):
                bpy.ops.object.mode_set(mode='EDIT',toggle=True)
                pass
            else:
                # print('2333')
                pass
            改名()
            清理顶点组()
            return {'FINISHED'}

        def join():
            for obj in sel:
                # print(obj)
                # joinobjlist.append(obj)
                if len(sel) <= 1:                
                    self.report({"ERROR"}, "请选择两个或两个以上物体")
                    # break
                    return {'FINISHED'}


                
                if obj.EMM.is_join_obj and mode != '强制合并':
                    # joinobjlist.append(obj.name)
                    # self.report({"INFO"}, "此物体已是合并顶点组")
                    obj.select_set(False)
                    continue
                # elif  mode != '强制合并':
                #     pass


                if obj.type != 'MESH':continue

                print(obj.type)


                name = generate_name(obj.name_full,前缀,后缀)


                vg = obj.vertex_groups
                
                if name not in vg and obj.EMM.is_join_obj ==False:   #如果没有这个顶点组就创建
                    vg.new(name =name)
                    #向顶点组添加顶点
                    vgl = []
                    for edge in obj.data.edges: #vertices
                        vgl.append(edge.index)
                    vg[name].add(vgl,1,'ADD')#('REPLACE', 'ADD', 'SUBTRACT'

                    vgl.clear()

            bpy.ops.object.join()

            context.active_object.EMM.is_join_obj = True    #是合并过的物体
            # print('合_______')
        
            return {'FINISHED'}
    
        if mode in ('拆分','强制拆分'):separate()
        else:join()
        print(mode,'emm')
        
        return {'FINISHED'}

pr = True  # print_re_info True or False

if __name__ == "__main__":
    register_class(EMM_VERTEX_GROUPS)
