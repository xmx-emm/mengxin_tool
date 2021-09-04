import bpy

# ksp.data_path

# bpy.context.object.data.bones.active 活动项

# get所选骨骼列表


for i in bpy.context.object.data.bones:
    

    if i.select:

        name = i.name
        
        for i in ('rotation_euler','location','scale','rotation_quaternion'):
            bpy.ops.anim.keying_set_path_add()

            scene = bpy.context.scene
            ks = scene.keying_sets.active
            ksp = ks.paths.active
            lis = []
            # print(f'pose.bones["{name}"].{i}') 
            # bpy.context.scene.keying_sets.active.paths.active.id_type

            # ksp.id_type = 'ARMATURE'
            # print(ksp.id_type)
            ksp.id = bpy.context.active_object
            # print(ksp.id)
            ksp.data_path = f'pose.bones["{name}"].{i}'
            # print(ksp.data_path)
            # print('_____________________')



# bpy.context.active_object.data
        # bpy.ops.anim.keying_set_path_remove()
            # bpy.ops.anim.keying_set_path_add()

# print(lis)
# lis.clear()

#  bpy.context.object.pose.bones['toes_ref.r'].

# bpy.data.objects["椒酱模型"].pose.bones["c_foot_ik.r"].lock_location[0]

# bpy.ops.anim.keying_set_path_add()
# ksp.id = bpy.context.active_object
# print(ksp.id)

# bpy.data.objects["椒酱模型"].pose.bones["c_foot_roll_cursor.l"].scale[1]