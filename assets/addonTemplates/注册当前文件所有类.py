import bpy
import inspect
import sys
from bpy.utils import register_class, unregister_class

排除类列表 = (
    # TIME_PT_PLAYBACK,
    # Panel,
    # UIList,

)
###这个方法需要注意名称的长度，注册的顺序是按名称的长度来的，子面板要后注册
for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
    if class_ not in 排除类列表:
        register_class(class_)

for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
    if class_ not in 排除类列表:
        unregister_class(class_)