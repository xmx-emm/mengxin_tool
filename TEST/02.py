import bpy
import json
import os 
import pathlib
import re


def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


for group in bpy.data.node_groups:
    group.use_fake_user = False
    
for mat in bpy.data.materials:
    mat.use_fake_user = False

bpy.data.orphans_purge(do_recursive = True)



material_categories = {col.name:[obj.material_slots[0].name for obj in col.objects] for col in bpy.data.collections}

for key in material_categories:
    s = natural_sort(material_categories[key])
    material_categories[key] = s

dir_path = pathlib.Path(__file__).parent.parent.absolute()

with open(os.path.join(dir_path,"material_categories.json"), 'w') as f:
    f.write(json.dumps(material_categories))
bpy.ops.wm.previews_ensure() 

if "Export" in bpy.data.images:
    bpy.data.images.remove(bpy.data.images['Export'])
bpy.data.images.new("Export",32,32,alpha=True)
for mat in bpy.data.materials:
    print("Exporting",mat.name)
    img = bpy.data.images["Export"]
    img.pixels = mat.preview.icon_pixels_float
    img.filepath_raw = os.path.join(dir_path,"Icons",mat.name + ".png")
    img.file_format = 'PNG'
    img.save()
