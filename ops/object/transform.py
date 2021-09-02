# import bpy

##变换
# class transform(bpy.types.Operator):
#     def __init__(self):
#         self.C0=(0,0,0)
#         self.C1=(1,1,1)

#     Co = bpy.context.object
    
#     Cre = Co.rotation_euler                 #物体旋转欧拉
#     Crq = Co.rotation_quaternion            #物体旋转四元数
#     Cl = Co.location                        #位置
#     Cs = Co.scale                           #缩放
#     ###---------------------------#######
#     Cdre = Co.delta_rotation_euler           #增量
#     Cdrq = Co.delta_rotation_quaternion
#     Cdl = Co.delta_location 
#     Cds = Co.delta_scale
#     ###

    
#     def transform_to_delta(self,Cre,Cdre,Crq,Cdrq,Cl,Cdl,Cs,Cds):
#         Cre += Cdre
#         Crq += Cdrq
#         Cl += Cdl
#         Cs += Cds

def register():
    # print('re_transform')
    pass
def unregister():
    # print('unre_transform')
    pass
