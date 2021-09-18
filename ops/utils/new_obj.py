import bpy
from bpy.props import StringProperty


def 创建物体(type,name,data,ver,edge,face):
    type: StringProperty(name='type',default='')

    if type in ('曲线','曲面','字体'):
        bpy.data.curves.new(name,type)
        bpy.data.curves[name].splines
    
    if type in ('网格','MESH'):
        bpy.data.meshes.new(name,data)