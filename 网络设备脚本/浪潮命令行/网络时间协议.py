from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 网络时间协议 as 南向协议
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..思科命令行.常量 import *
#===============================================================================
# 基础
#===============================================================================
def f模式(a全局配置, a端, at客户端, at服务器, a操作):
	if a端 == 操作.E端.e客户端:
		vt类 = at客户端
	elif a端 == 操作.E端.e服务器:
		vt类 = at服务器
	else:
		raise ValueError("错误的网络时间协议端")
	v模式 = vt类(a全局配置)
	return v模式
#===============================================================================
# cn系列(v7.x)
#===============================================================================
class C客户端cnv7_0(模式.C同级模式, 南向协议.I客户端配置):
	"""适用于: cn61108(v7.0)"""
	def __init__(self, a):
		南向协议.I客户端配置.__init__(self, a)
	def f模式_远端(self, a地址, a端 = 操作.E端.e服务器, a操作 = 操作.E操作.e新建):
		if a端 == 操作.E端.e服务器:
			v命令 = "ntp server"
		elif a端 == 操作.E端.e对等体:
			v命令 = "ntp peer"
		v模式 = C远端cnv7_0(self, a地址, v命令)
		if a操作 == 操作.E操作.e新建:
			v模式.f执行当前模式命令(v模式.fg命令前缀())
		return v模式
class C远端cnv7_0(模式.C同级模式, 南向协议.I远端配置):
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
class C客户端cnv7_3(C客户端cnv7_0):
	"""适用于: cn8672(v7.3), cn8696(v7.3)"""
	def __init__(self, a):
		C客户端cnv7_0.__init__(self, a)
	def f模式_远端(self, a地址, a端 = 操作.E端.e服务器, a操作 = 操作.E操作.e新建):
		if a端 == 操作.E端.e服务器:
			v命令 = "ntp server"
		elif a端 == 操作.E端.e对等体:
			v命令 = "ntp peer"
		v模式 = C远端cnv7_0(self, a地址, v命令)
		if a操作 == 操作.E操作.e新建:
			v模式.f执行当前模式命令(v模式.fg命令前缀())
		self.fs分发(a操作)
		return v模式
	def fs分发(self, a操作 = 操作.E操作.e开启):
		v命令 = "ntp distrubute"
		self.f执行当前模式命令(v命令)
#===============================================================================
# s系列(v3.x)
#===============================================================================
class C客户端sv3(模式.C同级模式, 南向协议.I客户端配置):
	"""适用于: s6550(v3.x)"""
	def __init__(self, a):
		南向协议.I客户端配置.__init__(self, a)
	def f模式_远端(self, a地址, a端 = 操作.E端.e服务器, a操作 = 操作.E操作.e新建):
		if a端 == 操作.E端.e服务器:
			v命令 = "ntp server"
		elif a端 == 操作.E端.e对等体:
			v命令 = "ntp peer"
		else:
			raise ValueError("a端 必需是服务器或对等体")
		v模式 = C远端sv3(self, a地址, v命令)
		if a操作 == 操作.E操作.e新建:
			v模式.f执行当前模式命令(v模式.fg命令前缀())
		return v模式
class C远端sv3(模式.C同级模式, 南向协议.I远端配置):
	"""适用于: s6550(v3.x)"""
	def __init__(self, a, a地址, a命令):
		南向协议.I远端配置.__init__(self, a, a地址)
		self.m命令 = a命令
	def fg命令前缀(self):
		"""ntp server 地址"""
		return 命令.C命令(f"{self.m命令} {self.m地址}")
	def fs版本(self, a版本 = 3, a操作 = 操作.E操作.e设置):
		"""命令: ntp server 地址 version 版本
		版本: v1, v2, v3, v4 其中之一"""
		v命令 = self.fg命令前缀()
		v命令 += "version", f"v{a版本}"
		self.f执行当前模式命令(v命令)
	def fs认证(self, a钥匙 = 0, a操作 = 操作.E操作.e设置):
		"""命令: ntp server 地址 key 钥匙号
		钥匙号: 范围1~4294967295"""
		v命令 = self.fg命令前缀()
		v命令 += "key", a钥匙
		self.f执行当前模式命令(v命令)