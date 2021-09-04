import bpy
from bpy.types import Operator as OPS
from bpy.utils import register_class, unregister_class
from bpy.props import IntProperty, BoolProperty


class EMMMM_REPEAT_LAST(OPS):
    """这是这个操作符的提示"""
    bl_idname = 'emm.repeat_last'
    bl_label = '重复操作'
    bl_options = {'REGISTER', 'UNDO'}
    ok: BoolProperty(name='确认', default=False)
    RepeatNum: IntProperty(name="重复操作数量", default=5,
                           max=114514, min=1, subtype="FACTOR")

    def draw(self, context):

        layout = self.layout
        box = layout.box()
        box.label(text='View Selected')
        column = box.column()
        column.prop(self, 'RepeatNum',toggle=True)
        column.prop(self, 'ok',toggle=True)

    def execute(self, context):
        # self.repeat(context)
        if self.ok:
            for i in range(self.RepeatNum):
                bpy.ops.screen.repeat_last()
                print(i)
        return {'FINISHED'}

    # def repeat(self, context):
    #     if self.ok:
    #         self.ok_(context)

    # def ok_(self, context):
    #     c = bpy.ops.screen
    #     for i in range(self.RepeatNum):
    #         c.repeat_last()
    #         print(i)


def register():
    register_class(EMMMM_REPEAT_LAST)
    print('ok')


def unregister():
    unregister_class(EMMMM_REPEAT_LAST)


if __name__ == "__main__":
    register()
