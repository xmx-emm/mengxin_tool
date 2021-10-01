import bmesh
import bpy
bm = bmesh.new()
o = bpy.context.object.data

bm.from_mesh(o)
for i in bm.verts:
    print(i.co)

bm.free()