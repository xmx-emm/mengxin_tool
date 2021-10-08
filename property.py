import bpy
import inspect
import sys
from bpy.utils import register_class,unregister_class
from bpy.types import PropertyGroup
from bpy.props import (StringProperty,
                       BoolProperty,
                       FloatProperty,
                       IntProperty,
                       EnumProperty,
                       PointerProperty,
                       CollectionProperty,
                       )


#雕刻全局属性
class EMMSculptProperty(PropertyGroup):
    uuid:StringProperty(name='EMMSculptProperty',default='这是一个默认名称 EMMSculptProperty')



    rotate_method: BoolProperty(name="自动切换视图旋转方法", default=True, 
        description='''
        当在雕刻模式时,将会自动切换视图旋转方法为 轨迹球
        在其它模式自动切换为  转盘''')

class EMMUvProperty(PropertyGroup):
    name:StringProperty(name='EMMUvProperty',default='这是一个默认名称 EMMUvProperty')


class EMMSceneProperty(PropertyGroup):#场景属性
    name = '场景属性'
    active_object_index: IntProperty(name='活动物体编号(EMM)', default=0)


class EMMObjectProperty(PropertyGroup):
    name = '物体属性'
    object_index: IntProperty(name='物体编号(EMM)',)
    is_join_obj:BoolProperty(name='是合并物体',default=False,description='是子工具大师合并后的物体,顶点组不能丢啊')
    临时属性:StringProperty(name='临时属性',default='')
    临时属性2:StringProperty(name='临时属性2',default='')
    临时属性3:StringProperty(name='临时属性3',default='')


class EMMObjectVertexGroupProperty(PropertyGroup):
    name = '顶点组属性'
    状态:StringProperty(name='顶点组状态',default='emm',description='是子工具大师合并后的物体,顶点组不能丢啊')

class EMM_屏幕_Property(PropertyGroup):

    循环播放: BoolProperty(name="循环播放", default=True,description='播放完所有帧后是否从头开始循环播放')
    回到起始帧: BoolProperty(name="回到起始帧", default=False,description='如果打开循环播放,打开此选项后停止播放动画后时间线回到起始帧')


class EMM_Preferences属性_Property(PropertyGroup):
    循环播放= BoolProperty(name="循环播放", default=True,description='播放完所有帧后是否从头开始循环播放')
    回到起始帧= BoolProperty(name="回到起始帧", default=False,description='如果打开循环播放,打开此选项后停止播放动画后时间线回到起始帧')



排除类列表 = (
    PropertyGroup,
)

def 注册属性_Property():
    for name, class_ in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        if class_ not in 排除类列表:
            register_class(class_)
            # print(class_)

    # bpy.types.Scene.EMM_UV = PointerProperty(type=EMMUvProperty)
    # bpy.types.Scene.EMM_Sculpt = PointerProperty(type=EMMSculptProperty)

    bpy.types.Scene.EMM = PointerProperty(type=EMMSceneProperty,name='萌新工具箱场景属性')
    bpy.types.Scene.active_object_index = IntProperty(name='活动物体编号(EMM)', default=0)

    bpy.types.Object.EMM = PointerProperty(type=EMMObjectProperty,name='萌新工具箱物体属性')
    
    bpy.types.VertexGroupElement.emm = StringProperty(name='临时属性3',default='')
    bpy.types.VertexGroup.EMM = PointerProperty(type=EMMObjectVertexGroupProperty,name='顶点组属性')
    bpy.types.VertexGroups.EMM = PointerProperty(type=bpy.types.VertexGroup.EMM,name='顶点组属性')

    bpy.types.Screen.EMM = PointerProperty(type=EMM_屏幕_Property,name='萌新工具箱屏幕属性')
     
    # bpy.types.PreferencesView.EMM = BoolProperty(name='仅过滤用户插件',description='只过滤用户的插件，其它自带的插件全部启用',default = False)
    # bpy.types.WindowManager.
    # bpy.EMM.仅过滤用户插件= BoolProperty(name='仅过滤用户插件',description='只过滤用户的插件，其它自带的插件全部启用',default = False)





def 注销属性_Property():
    for name, class_ in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        if class_ not in 排除类列表:
            unregister_class(class_)

    # del bpy.types.Scene.EMM_UV
    # del bpy.types.Scene.EMM_Sculpt
    del bpy.types.Scene.EMM
    del bpy.types.Scene.active_object_index

    del bpy.types.Object.EMM
    del bpy.types.VertexGroups.EMM
    del bpy.types.VertexGroup.EMM
    del bpy.types.Screen.EMM

    # del bpy.EMM.仅过滤用户插件

    #插件管理

if __name__ == "__main__":
    注册属性_Property()
