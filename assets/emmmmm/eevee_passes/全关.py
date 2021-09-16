import bpy
vl = bpy.context.view_layer

vl.use_pass_combined = False
vl.use_pass_z = False
vl.use_pass_mist = False
vl.use_pass_normal = False
vl.use_pass_diffuse_direct = False
vl.use_pass_diffuse_color = False
vl.use_pass_glossy_direct = False
vl.use_pass_glossy_color = False
vl.use_pass_cryptomatte_object = False
vl.use_pass_cryptomatte_material = False
vl.use_pass_cryptomatte_asset = False
vl.pass_cryptomatte_depth = 2
vl.use_pass_cryptomatte_accurate = False
vl.use_pass_ambient_occlusion = False
vl.use_pass_shadow = False
vl.use_pass_environment = False
vl.use_pass_emit = False
vl.eevee.use_pass_volume_direct = False
vl.eevee.use_pass_bloom = False
