

# 最大化插件
from bl_ui.space_userpref import USERPREF_PT_addons as USE  # 导入最大化偏好设置的类
USERPREF = USE.draw  # 从另一个文件调用源始函数，用于恢复重写，不能在一个文件内调用原始又重写它，反正我试了这样不行｛萌新｝

##时间线的重新绘制
from bl_ui.space_time import TIME_PT_playback
TIME_PT_PLAYBACK动画播放 = TIME_PT_playback.draw


from bl_ui.properties_output import RENDER_PT_presets
RENDER_PT_PRESETS = RENDER_PT_presets
# # 物体显示预设
# from bl_ui.properties_object import OBJECT_PT_display as OBJECT_PT_display
# OBJECT_PT_DISPLAY = OBJECT_PT_display


# bpy.types.VIEWLAYER_PT_layer_passes.prepend(eevee_passes_presets)  # EV输出通道
# bpy.types.CYCLES_RENDER_PT_passes.prepend(cycles_passes_presets)  # CY输出通道
# bpy.types.OBJECT_PT_display.prepend(object_display_presets)  # 物体显示属性

# bpy.types.VIEWLAYER_PT_layer_passes.remove(eevee_passes_presets)
# bpy.types.CYCLES_RENDER_PT_passes.remove(cycles_passes_presets)
# bpy.types.OBJECT_PT_display.remove(object_display_presets)
