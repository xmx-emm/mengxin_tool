
from .panel import register_注册面板,register_注销面板
from .presets import 注册预设,注销预设
from .menu import 注册菜单,注销菜单
from .template_list import 注册template_list,注销template_list

def 注册UI():
    注册template_list()
    注册菜单()
    register_注册面板()## 需要先注册面板，不然在插件属性里面更新面板的名称会找不到 Panel_Class 这个列表而报错
    注册预设()  #先注册预设再更改UI,不然改UI没有预设按钮给加上去    这里只管注册，添加到界面让下一个更改UI来做

def 注销UI():
    注销template_list()
    register_注销面板()
    注销菜单()
    注销预设()