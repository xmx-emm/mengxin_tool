import bpy
import inspect
import sys
from bpy.utils import register_class, unregister_class

排除类列表 = (
    # TIME_PT_PLAYBACK,
    # Panel,
    # UIList,

)

for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
    if class_ not in 排除类列表:
        register_class(class_)

for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
    if class_ not in 排除类列表:
        unregister_class(class_)