import bmesh
import bpy

def get_bmesh():
    C = bpy.context
    O = C.object
    Od = O.data
    Cm = C.mode

    if Cm == 'EDIT_MESH':
        bm = bmesh.from_edit_mesh(Od)
    else:
        bm = bmesh.new()
        bm.from_object(O,1)
    uv_layers = bm.loops.layers.uv.active
    print(uv_layers.name)




    # bm.from_mesh(o)
    # for i in bm.verts:
    #     print(i.co)

    # bm.free()
if __name__ == "__main__":
    get_bmesh()

