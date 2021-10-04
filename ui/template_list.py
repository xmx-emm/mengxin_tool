import bpy
import sys
import inspect
from bpy.types import UIList
from bpy.utils import register_class, unregister_class


class EMM_OBJECT_UL_render_check_slow(UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index,):
        obj = item
        hide_viewport = obj.hide_viewport
        hide_render = obj.hide_render


        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            r = layout.row(align=True)
            r.prop(obj,'name',text = '',emboss=False, )#icon_value=icon

            icon=  'RESTRICT_VIEW_OFF' if obj.hide_viewport else'RESTRICT_VIEW_ON'
            r.prop(obj,'hide_viewport',text = '',emboss=False, )
            # r.prop(obj,'hide_select',text = '',emboss=False, icon_value=icon)
            r.prop(obj,'hide_render',text = '',emboss=False)
            
            # r.prop(obj,'hide_get()',text = '',emboss=False)
            # r.prop(obj,'hide_viewport',text = '',emboss=False, icon=  'HIDE_OFF' if obj.hide_viewport else'HIDE_ON')

        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            # layout.label(text="emm", icon_value=icon)





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
    
