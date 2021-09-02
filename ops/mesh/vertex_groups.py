import bpy
from bpy.types import Operator as OPS
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.ops import object as O


class NewName_Vertex_Groups(OPS):
    """顶点组操作  mode: delAllvg = 删除所有顶点组  delnv = 删除new顶点组  addvg = 添加顶点组
    prn = 前缀  sun = 后缀 ，PrInfo = 打印创建信息"""
    bl_idname = 'emm.new_vertex_groups_name'
    bl_label = '新建顶点组'
    bl_options = {'REGISTER', 'UNDO'}

    mode: EnumProperty(
        name="操作的模式",
        default='addvg',
        items=(
            ('delAllvg', "删除所有顶点组", ""),
            ('delnv', "删除new顶点组", ""),
            ('addvg', "添加顶点组", ""),
            ('jone', "", ""),
            ('', "", ""),
            ('', "", ""),

        ),
    )

    prn: StringProperty(name="前缀名称",
                        description="前缀的名称",
                        default="",
                        maxlen=10,
                        options={'ANIMATABLE'},
                        subtype='NONE')

    sun: StringProperty(name="后缀名称",
                        description="前缀的名称",
                        default="-emmmm",
                        maxlen=10,
                        options={'ANIMATABLE'},
                        subtype='NONE')

    PrInfo: BoolProperty(name="打印统记信息", default=False)

    @classmethod
    def poll(cls, context):
        return (
            context.space_data.type == 'VIEW_3D'
            and context.active_object is not None
            and context.active_object.mode == 'OBJECT')

    def newvg(self):
        selname = []
        om = self.mode

        # TODO:for all 所选物体
        for i in bpy.context.selected_objects:

            # bpy.context.view_layer.objects.active = i   # bpy.context.view_layer.objects.active.name_full,'emmm'  set 活动对象
            if i.type == 'MESH':
                prn = self.prn
                sun = self.sun
                vglist = []

                selname.append(i.name_full)

                nvgn = (prn + i.name_full + sun)  # new vg name
                print(i.name_full, '____i.name_full')
                # print(str(bpy.context.view_layer.objects.active.name_full))

                # for 所选物体的 vg
                f = i.vertex_groups
                for j in f:
                    vglist.append(j.name)
                    # print("_for_vg__")  #test vg for

                    # 删除此顶点组 删除需要for一下激活顶点
                    if om == 'delnv' and j.name == nvgn:
                        bpy.context.view_layer.objects.active = i
                        bpy.ops.object.vertex_group_set_active(
                            group=str(j.name))
                        bpy.ops.object.vertex_group_remove(
                            all=False, all_unlocked=False)
                        print('____del__nv____')

                print(vglist)

                if (vglist == [] or nvgn not in vglist) and om == 'addvg':
                    f.new(name=nvgn)
                    print('addvg')

                if om == 'delAllvg' and vglist != []:
                    bpy.context.view_layer.objects.active = i
                    O.vertex_group_remove(all=True)

                if self.PrInfo == True:

                    # print("____________________________test")
                    if vglist == []:
                        self.report(
                            {"INFO"}, f"在物体 '{i}' 中无顶点组,已新建顶点组 '{nvgn}' ")
                    elif nvgn in vglist:
                        self.report(
                            {"INFO"}, "顶点组 '%s' 已在 '%s' 内，无需新建" % (nvgn, vglist))
                    else:
                        self.report(
                            {"INFO"}, "找到顶点组 '%s' ,但顶点组内无 '%s'" % (vglist, nvgn))

                vglist.clear()
            print('_________________for__obj_________________________')
        self.report({"INFO"}, f'列表：{selname}')
        selname.clear()
        print('------------------------ops-ok-------------------------------')

    def execute(self, context):
        self.mode = 'delAllvg'
        self.newvg()

        # print('execute_____test')
        return {'FINISHED'}


def register():
    # print('re_vg')
    register_class(NewName_Vertex_Groups)


def unregister():
    # print('unre_vg')
    unregister_class(NewName_Vertex_Groups)


if __name__ == "__main__":
    register()
