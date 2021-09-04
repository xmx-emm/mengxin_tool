import bpy


## get 快捷键里面的空格键作用
def get_spacebar_action():
    bpy.context.window_manager.keyconfigs['Blender'].preferences.spacebar_action
    



print(get_spacebar_action)
