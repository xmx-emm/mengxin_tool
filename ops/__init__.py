from .curve import 注册曲线OPS,注销曲线OPS
from .mesh import 注册网格OPS,注销网格OPS
from .object import 注册物体OPS,注销物体OPS
from .bone import 注册骨骼OPS,注销骨骼OPS

def 注册OPS():
    try:
        注册曲线OPS()
        注册网格OPS()
        注册物体OPS()
        注册骨骼OPS()
    except Exception as e:
        print(e.args)


def 注销OPS():
    try:
        注销曲线OPS()
        注销网格OPS()
        注销物体OPS()
        注销骨骼OPS()
    except Exception as e:
        print(e.args)
