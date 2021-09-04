
import keyingsets_utils
from bpy.types import KeyingSetInfo
from keyingsets_builtins import BUILTIN_KSI_WholeCharacter




class BUILTIN_KSI_EMMMMSelected(KeyingSetInfo):
    """Insert a keyframe for all properties that are likely to get animated in a character rig """ \
    """(only selected bones)"""
    bl_idname = 'EMMM'
    bl_label = "EMMM"

    # iterator - all bones regardless of selection
    def iterator(ksi, context, ks):
        # Use either the selected bones, or all of them if none are selected.
        bones = context.selected_pose_bones_from_active_object or context.active_object.pose.bones

        for bone in bones:
            if bone.name.startswith(BUILTIN_KSI_WholeCharacter.badBonePrefixes):
                continue
            ksi.generate(context, ks, bone)

    # Poor man's subclassing. Blender breaks when we actually subclass BUILTIN_KSI_WholeCharacter.
    poll = BUILTIN_KSI_WholeCharacter.poll
    generate = BUILTIN_KSI_WholeCharacter.generate
    addProp = BUILTIN_KSI_WholeCharacter.addProp
    doLoc = BUILTIN_KSI_WholeCharacter.doLoc
    doRot4d = BUILTIN_KSI_WholeCharacter.doRot4d
    doRot3d = BUILTIN_KSI_WholeCharacter.doRot3d
    doScale = BUILTIN_KSI_WholeCharacter.doScale
    doBBone = BUILTIN_KSI_WholeCharacter.doBBone
    doCustomProps = BUILTIN_KSI_WholeCharacter.doCustomProps

classes = (
    BUILTIN_KSI_EMMMMSelected,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)


if __name__ == "__main__":
    register()
