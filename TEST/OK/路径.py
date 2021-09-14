from bl_ui.utils import PresetPanel
from bpy.types import Panel
import bpy
from cycles.ui import CyclesButtonsPanel as cb
import sys


class CYCLES_PT_sampling_presets(PresetPanel, Panel):
    bl_label = "Sampling Presets"
    preset_subdir = "cycles/sampling"
    preset_operator = "script.execute_preset"
    preset_add_operator = "render.cycles_sampling_preset_add"
    COMPAT_ENGINES = {'CYCLES'}
class cl(cb, Panel):
    bl_label = "Passes"
    bl_context = "view_layer"

    # print('----------------')
    #     def draw(self, context):
    #         pass
    def draw_header_preset(self, context):
        CYCLES_PT_sampling_presets.draw_panel_header(self.layout)

bpy.types.CYCL
bpy.types.CYCLES_RENDER_PT_passes_data = cl

for i in sys.path:

    print(i)
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\scripts\startup
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\scripts\modules
# C: \Program Files(x86)\Steam\steamapps\common\Blender\python39.zip
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\python\DLLs
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\python\lib
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\python\bin
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\python
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\python\lib\site-packages
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\scripts\freestyle\modules
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\scripts\addons\modules
# C: \Users\32099\AppData\Roaming\Blender Foundation\Blender\2.93\scripts\addons\modules
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\scripts\addons
# C: \Users\32099\AppData\Roaming\Blender Foundation\Blender\2.93\scripts\addons
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\scripts\addons_contrib
# C: \Program Files(x86)\Steam\steamapps\common\Blender\2.93\scripts\addons\io_import_palette\..\io_import_palette
