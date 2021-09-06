import bpy


#get 子级
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
                        # print(Fmp)
        print(SeBolis)


# bpy.data.objects["椒酱-头发"].parent