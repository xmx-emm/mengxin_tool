import bpy
owner = object()


def msgbus_callback():
    print("objects")


bpy.msgbus.subscribe_rna(
    key=(bpy.types.ViewLayer, 'objects'),
    owner=owner,
    args=(),
    notify=msgbus_callback,
)
