from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 网络时间协议 as 南向协议
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..思科命令行.常量 import *
#===============================================================================
# cn系列(v7.*)
#===============================================================================
class C客户端nv7_0(模式.C同级模式, 南向协议.I客户端配置):
	"""适用于: 思科nexus9000(v7.0), 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a):
		南向协议.I客户端配置.__init__(self, a)
	def f模式_远端(self, a地址, a端 = 操作.E端.e服务器, a操作 = 操作.E操作.e新建):
		if a端 == 操作.E端.e服务器:
			v命令 = "ntp server"
		elif a端 == 操作.E端.e对等体:
			v命令 = "ntp peer"
		v模式 = C远端nv7_0(self, a地址, v命令)
		if a操作 == 操作.E操作.e新建:
			v模式.f执行当前模式命令(v模式.fg命令前缀())
		return v模式
class C远端nv7_0(模式.C同级模式, 南向协议.I远端配置):
	def __init__(self, a, a地址, a命令):
		南向协议.I远端配置.__init__(self, a, a地址)
		self.m命令 = a命令
	def fg命令前缀(self):
		return 命令.C命令(f"{self.m命令} {self.m地址}")
	def fs优先(self, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = self.fg命令前缀()
		v命令 += "prefer"
		v命令.f前置肯定(操作.fi减操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		pass
class C客户端nv7_3(C客户端nv7_0):
	"""适用于: 浪潮cn8672(v7.3), 浪潮cn8696(v7.3)"""
	def __init__(self, a):
		C客户端nv7_0.__init__(self, a)
	def f模式_远端(self, a地址, a端 = 操作.E端.e服务器, a操作 = 操作.E操作.e新建):
		if a端 == 操作.E端.e服务器:
			v命令 = "ntp server"
		elif a端 == 操作.E端.e对等体:
			v命令 = "ntp peer"
		v模式 = C远端nv7_0(self, a地址, v命令)
		if a操作 == 操作.E操作.e新建:
			v模式.f执行当前模式命令(v模式.fg命令前缀())
		self.fs分发(a操作)
		return v模式
	def fs分发(self, a操作 = 操作.E操作.e开启):
		v命令 = "ntp distrubute"
		self.f执行当前模式命令(v命令)
