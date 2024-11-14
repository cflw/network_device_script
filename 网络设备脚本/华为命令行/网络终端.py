from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 网络终端 as 南向网络终端
from .常量 import *
class C网络终端配置(南向网络终端.I网络终端配置, 模式.C同级模式):
	def __init__(self, a):
		南向网络终端.I网络终端配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("telnet server enable")
		v命令.f前置否定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs端口号(self, a):
		v命令 = 命令.C命令("telnet server port")
		v命令 += a
		self.f执行当前模式命令(v命令)
