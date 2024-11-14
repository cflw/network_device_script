from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 网络终端 as 南向网络终端
from .常量 import *
from . import 接口 as 实现接口
class C网络终端配置(南向网络终端.I网络终端配置, 模式.C同级模式):
	def __init__(self, a):
		南向网络终端.I网络终端配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		"""service telnet {enable|disable}"""
		v命令 = 命令.C命令("service telnet")
		v命令 += "enable" if 操作.fi开操作(a操作) else "disable"
