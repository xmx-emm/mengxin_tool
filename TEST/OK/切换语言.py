import bpy
La=bpy.context.preferences.view
if La.language  == 'zh_CN':    La.language  = 'en_US'
else:    La.language  =  'zh_CN'
