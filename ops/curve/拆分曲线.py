import bpy
from bpy.props import StringProperty




import bpy
from bpy.types import Operator
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class

# from ..utils.new_obj import 创建物体
###TODO 拆分 按松散块 按材质 按类型


class 拆分曲线(Operator):
    bl_idname = "emm.separate_splines"
    bl_label = "拆分曲线"
    bl_options = { 'UNDO'}#'REGISTER',
    bl_description = "拆分曲线啊"

    mode: StringProperty(name='mode',default='拆分曲线模式')

    def execute(self, context):
        mode = self.mode

        A = context.selected_objects.copy()
        
        if context.mode != 'EDIT_CURVE':
            bpy.ops.object.mode_set(mode='EDIT',toggle=True)                            
            self.is_ObjectMode = True
        # for c in context.active_object:
        if context.active_object.type == 'CURVE': 
            for i in reversed(context.active_object.data.splines):
                # print(i)
                bpy.ops.curve.select_all(action='DESELECT')
                if len(context.active_object.data.splines) <= 1:
                    continue
                if mode == '按松散块':
                    for j in i.points:
                        j.select = True
                        
                    for j in i.bezier_points:
                        j.select_control_point = True
                
                # for j in i.points:
                #     print(j.select)
                    
                # for j in i.bezier_points:
                #     print(j.select_control_point)
                bpy.ops.curve.separate()
                print(i.type)

        # for OBJ in A:
            # if OBJ.type != 'CURVE':continue    #如果所选不是物体就跳过

            # if mode == '按松散块':
            #     SPLINES = OBJ.data.splines  #样条线
            #     ITEM = SPLINES.items()      #项
            #     ACTIVE = SPLINES.active     #活动项曲线

            #     if len(ITEM) <=1:   #只有一个样条线，跳过
            #         print('只有一个样条线，跳过')
            #         continue                
            #     #使用了遍历所选物体，是不是编辑模式已经不重要了
            #     if OBJ.mode == 'OBJECT':
            #         bpy.ops.object.editmode_toggle()
            #         edit = True
                
            #     bpy.ops.curve.select_all(action='DESELECT')
            #     for spline in SPLINES:
            #         # if ACTIVE == spline:continue  #如果有活动项 使用分离操作，不用创建物体了


            #         if len(ITEM) <=1:   #只有一个样条线，跳过
            #             print('只有一个样条线，跳过')
            #             continue
                    
            #         if spline.type in ('POLY','NURBS'):#点
            #             for p in spline.points:
            #                 p.select = True
            #                 # print(f'{OBJ.name}__{spline.type}___{p.select}_')    
                        
            #             # bpy.ops.curve.separate()
            #             # pass
                        
            #             try:
            #                 bpy.ops.curve.separate()
            #             except Exception as e:
            #                 print(e.args)
            #         else: ##BEZIER
            #             for bp in spline.bezier_points:
            #                 bp.select_control_point = True

            #             print(f'{OBJ.name}__{spline.type}_')
                        
            #             try:
            #                 bpy.ops.curve.separate()
            #             except Exception as e:
            #                 print(e.args)
            #         # print(' ')


        if  hasattr(self, 'is_ObjectMode'):
            bpy.ops.object.mode_set(mode='EDIT',toggle=True)
            # if edit:bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


if __name__ == "__main__":
    register_class(拆分曲线)