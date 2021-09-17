import bpy
import inspect
import sys
from bpy.utils import register_class, unregister_class

from .cycles_passes_presets import CYCLES_PT_Passes_presets,AddPresetCycles_Passes
from .eevee_passes_presets import EEVEE_PT_Passes_presets,AddPresetEEVEE_Passes
from .object_display_presets import OBJECT_PT_display_presets,AddPresetObjectDisplay
from .node_渐变_presets import NODE_PT_ColorRamp_Presets,AddPresetNode_渐变_Passes
# from . import cycles_passes_presets,eevee_passes_presets,object_display_presets

排除类列表 = (
    # TIME_PT_PLAYBACK,
    # Panel,
    # UIList,
)

def 注册预设():
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            try:
                register_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)


def 注销预设():
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            
            try:
                unregister_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)
