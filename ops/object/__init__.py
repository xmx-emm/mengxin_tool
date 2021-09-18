import bpy
import inspect
import sys

from bpy.types import Operator
from bpy.utils import register_class, unregister_class



排除类列表 = (
    Operator,
)

def 注册物体OPS():

    ###这个方法需要注意名称的长度，注册的顺序是按名称的长度来的，子面板要后注册
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            try:
                register_class(class_)
                print(class_)
            except Exception as e:
                print(e.args)

def 注销物体OPS():
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            
            try:
                unregister_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)