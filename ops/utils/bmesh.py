import bmesh
import bpy

def test(matrix):
    # if bpy.context.mode == "EDIT_MESH":
    #     bm = bmesh.from_edit_mesh(bpy.context.object.data)
    #     uv_layer = bm.loops.layers.uv.active
    #     for face in bm.faces:
    #         me = bpy.data.meshes.new(name='name')
    #         vertices = []
    #         for loop in face.loops:
    #             vertices.append((*loop[uv_layer].uv[:], 0))
    #         edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    #         face = [(0, 1, 2, 3)]
    #         me.from_pydata(vertices=vertices, edges=edges, faces=face)
    #         obj = bpy.data.objects.new(name=me.name, object_data=me)
    #         bpy.context.collection.objects.link(obj)
    #     bm.free()
    me = bpy.data.meshes.new(name='name')

    vertices = [(1, 1,0), (-1,1,0), (-1,-1,0), (1,-1,0)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    face = [(0, 1, 2, 3)]

    me.from_pydata(vertices=vertices, edges=edges, faces=face)
    obj = bpy.data.objects.new(name=me.name, object_data=me)

    if matrix != None:
        obj.matrix_world = matrix

    bpy.context.collection.objects.link(obj)


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
    test(bpy.context.object.matrix_world)

