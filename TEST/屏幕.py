# 从HOPS COPY过来的
# from utility import screen


# def draw(preference, context, layout):

#     write_text(preference, layout, info_text, width=bpy.context.region.width / screen.dpi_factor() / 8)


# def write_text(preference, layout, text, width = 30, icon = "NONE"):
#     col = layout.column(align = True)
#     col.scale_y = 0.85
#     prefix = " "
#     if not preference.wrap_text:
#         width = 540 / screen.dpi_factor() / 8
#     for paragraph in text.split("\n"):
#         for line in textwrap.wrap(paragraph, width):
#             col.label(text=prefix + line, icon = icon)
#             if icon != "NONE": prefix = "     "
#             icon = "NONE"


# info_text = """HardOps is a toolset to maximize hard surface efficiency. This tool began back in
# 2015 and still continues. Perpetually updated and always evolving, we strive to be the best hard
# all in one workflow assistant. Be sure to use the Hops button in the 3d view to find your way. 
# Thanks to everyone's continued support and usage the tool continues to live.
# We hope you enjoy using HardOps. \n

# support@hopscutter.com
# """.replace("\n", " ")


# def system_dpi(ui_scale=True):
#     preference = bpy.context.preferences
#     system = preference.system

#     dpi = system.dpi * system.pixel_size

#     if ui_scale:
#         dpi *= preference.view.ui_scale

#     return dpi


# def dpi_factor(rounded=False, integer=False, ui_scale=True, min=1.0):
#     factor = system_dpi(ui_scale=ui_scale) / 72 if addon.preference().behavior.use_dpi_factor else 1

#     if factor < min:
#         factor = min

#     if rounded:
#         factor = round(factor)

#     if integer:
#         factor = int(factor)

#     return factor


# def tweak_distance(ot):
#     return abs((ot.mouse['location'] - ot.last['mouse']).x) + abs((ot.mouse['location'] - ot.last['mouse']).y)
