import bpy
import sys
import inspect
from bpy.types import UIList
from bpy.utils import register_class, unregister_class


class OBJECT_UL_render_check_slow(UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index,):
        obj = item
        print(item)
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(obj,'name',text = '')
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="emm", icon_value=icon)



排除类列表 = (
    UIList,
)


def 注册template_list():
    ###这个方法需要注意名称的长度，注册的顺序是按名称的长度来的，子面板要后注册
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            try:
                register_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)


def 注销template_list():
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            
            try:
                unregister_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)

            # unregister_class(class_)
    
