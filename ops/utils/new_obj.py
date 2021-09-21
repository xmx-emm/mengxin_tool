import bpy
from bpy.props import StringProperty


def 创建物体(type,subtype,name,data,ver,edge,face):

    type: StringProperty(name='type',default='')

    if type in ('曲线','CURVE',
                '曲面','SURFACE',
                '字体','FONT'): #'POLY','NURBS' BEZIER
        bpy.data.curves.new(name,type)
        
        bpy.data.curves[name].splines.new(subtype)
    

    if type in ('网格','MESH'):
        bpy.data.meshes.new(name,data)