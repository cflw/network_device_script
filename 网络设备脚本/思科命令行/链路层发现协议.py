from ..基础接口 import 操作
from ..基础接口 import 链路层发现协议 as 北向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 链路层发现协议 as 南向协议
from .常量 import *
class C进程配置(模式.C同级模式, 南向协议.I进程配置):
	def __init__(self, a):
		南向协议.I进程配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("lldp run")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def f显示_邻居表(self):
		raise NotImplementedError()