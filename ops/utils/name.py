import bpy
import random
import re
import string
from bpy.props import StringProperty, BoolProperty, EnumProperty
import pinyin
# from pypinyin import pinyin

def generate_name(name,前缀,后缀):
    return 前缀+name+后缀
    
def match_name(name,前缀,后缀): #匹配名称
    pattern = 前缀+r'.+'+后缀    
    return re.findall(pattern=pattern,string=name)

def get_infix(name,前缀,后缀):
    name = str(name)
    name = name.split(前缀)[1]
    return name.split(后缀)[0]

def range_name(*,k=10):
    return "".join(random.choices(string.ascii_letters, k = k))

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def pinyin_2_hanzi(pinyinList):
    from Pinyin2Hanzi import DefaultDagParams
    from Pinyin2Hanzi import dag

    list = dict()
    dagParams = DefaultDagParams()
    # 10个候选值
    result = dag(dagParams, pinyinList, path_num=10, log=True)
    for item in result:
        socre = item.score # 得分
        res = item.path # 转换结果
        list[socre]= res
    return list
    



def to_pinyin(str):
    pinyin.pinyin.get_pinyin(str)
# for i in 'EM是中文MM':
def to_cn(set):
    pass

print(range_name())