import bpy
from ...utils.registration import get_emm_prefs

a = {
    "Animation": '动画',
    "Compositing": '合成',
    "Geometry Nodes": '几何节点',
    "Layout": '布局',
    "Modeling": '建模',
    "Rendering": '渲染',
    "Scripting": '脚本',
    "Sculpting": '雕刻',
    "Shading": '着色',
    "Texture Paint": '纹理绘制',
    "UV Editing": 'UV编辑',
}

def workspaces_cn():
    ok = get_emm_prefs().activate_workspaces_cn

    for i in bpy.data.workspaces:
        wk = i.name_full  # get 场景内的wp名称
        ln = a.get(i.name_full)  # get 在字典内的中文名，如果没有就反回None
        av = a.values()

        if ok:
            if ln != None:
                n = (list(a.keys())[list(a.values()).index(ln)])  # 根据值板回键
                if wk == n:
                    i.name = ln
        else:
            if wk in av:
                n = (list(a.keys())[list(a.values()).index(wk)])  # 根据值板回键
                i.name = n
