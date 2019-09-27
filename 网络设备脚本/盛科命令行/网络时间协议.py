from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 网络时间协议 as 南向协议
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..思科命令行.常量 import *
#===============================================================================
# cn系列(v6.x)
#===============================================================================
class C客户端ev6(模式.C同级模式, 南向协议.I客户端配置):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a):
		南向协议.I客户端配置.__init__(self, a)
	def f模式_远端(self, a地址, a端 = 操作.E端.e服务器, a操作 = 操作.E操作.e新建):
		if a端 == 操作.E端.e服务器:
			v命令 = "ntp server"
		elif a端 == 操作.E端.e对等体:
			v命令 = "ntp peer"
		else:
			raise ValueError("a端 必需是服务器或对等体")
		v模式 = C远端ev6(self, a地址, v命令)
		if a操作 == 操作.E操作.e新建:
			v模式.f执行当前模式命令(v模式.fg命令前缀())
		return v模式
class C远端ev6(模式.C同级模式, 南向协议.I远端配置):
	def __init__(self, a, a地址, a命令):
		南向协议.I远端配置.__init__(self, a, a地址)
		self.m命令 = a命令
	def fg命令前缀(self):
		return 命令.C命令(f"{self.m命令} {self.m地址}")
	def fs版本(self, a版本 = 3, a操作 = 操作.E操作.e设置):
		"""命令: ntp server 地址 version 版本
		版本: 范围1~3"""
		v命令 = self.fg命令前缀()
		v命令 += "version", a版本
		self.f执行当前模式命令(v命令)
	def fs优先(self, a操作 = 操作.E操作.e设置):
		"""命令: ntp server 地址 prefer"""
		v命令 = self.fg命令前缀()
		v命令 += "prefer"
		self.f执行当前模式命令(v命令)
	def fs认证(self, a钥匙 = 0, a操作 = 操作.E操作.e设置):
		"""命令: ntp server 地址 key 钥匙号
		钥匙号: 范围1~64000"""
		v命令 = self.fg命令前缀()
		v命令 += "key", a钥匙
		self.f执行当前模式命令(v命令)
	def fs源(self, a源, a操作):
		raise NotImplementedError()
