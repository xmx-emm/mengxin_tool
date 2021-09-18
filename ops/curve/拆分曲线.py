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




import bpy
from bpy.types import Operator
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class

# from ..utils.new_obj import 创建物体
#DOTO 拆分 按松散块 按材质 按类型


class 拆分曲线(Operator):
    bl_idname = "emm.separate_splines"
    bl_label = "拆分曲线"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "拆分曲线啊"

    mode: StringProperty(name='mode',default='')
    def execute(self, context):
        mode = self.mode
        edit = False
        context = bpy.context
        A = context.selected_objects.copy()
        for OBJ in A:
            if OBJ.type != 'CURVE':continue    #如果所选不是物体就跳过

            if mode == '按松散块':
                SPLINES = OBJ.data.splines  #样条线
                ITEM = SPLINES.items()      #项
                ACTIVE = SPLINES.active     #活动项曲线

                if len(ITEM) <=1:   #只有一个样条线，跳过
                    print('只有一个样条线，跳过')
                    continue                
                #使用了遍历所选物体，是不是编辑模式已经不重要了
                if OBJ.mode == 'OBJECT':
                    bpy.ops.object.editmode_toggle()
                    edit = True
                
                bpy.ops.curve.select_all(action='DESELECT')
                for spline in SPLINES:
                    # if ACTIVE == spline:continue  #如果有活动项 使用分离操作，不用创建物体了


                    if len(ITEM) <=1:   #只有一个样条线，跳过
                        print('只有一个样条线，跳过')
                        continue
                    
                    if spline.type in ('POLY','NURBS'):#点
                        for p in spline.points:
                            p.select = True
                            # print(f'{OBJ.name}__{spline.type}___{p.select}_')    
                        
                        # bpy.ops.curve.separate()
                        # pass
                        
                        try:
                            bpy.ops.curve.separate()
                        except Exception as e:
                            print(e.args)
                    else: ##BEZIER
                        for bp in spline.bezier_points:
                            bp.select_control_point = True

                        print(f'{OBJ.name}__{spline.type}_')
                        
                        try:
                            bpy.ops.curve.separate()
                        except Exception as e:
                            print(e.args)
                    # print(' ')
            print(A)    


        if edit:bpy.ops.object.editmode_toggle()
        print('______debug')
        return {'FINISHED'}


if __name__ == "__main__":
    register_class(拆分曲线)