from ..基础接口 import 操作
from ..基础接口 import 文件
from ..基础接口 import 简单网络管理协议 as 北向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..思科命令行.常量 import *
#===============================================================================
# cn系列(v6.x)
#===============================================================================
class C代理配置_ev6(模式.C同级模式, 北向协议.I代理配置):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		"""命令: [no] snmp-server enable"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-server enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs团体字符串(self, a字符串, a权限 = 文件.E访问权限.e只读, a操作 = 操作.E操作.e设置):
		"""命令: snmp-server community 字符串 权限"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-server community")
		v命令 += a字符串
		if 操作.fi加操作(v操作):
			v命令 += "read-write" if 文件.fi含写(a权限) else "read-only"
		elif 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		else:
			raise ValueError("未知的操作")
		self.f执行当前模式命令(v命令)
class C陷阱配置_ev6(模式.C同级模式, 北向协议.I陷阱配置):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-server traps enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs服务器(self, a地址, a字符串, a操作 = 操作.E操作.e添加):
		"""命令: snmp-server trap target-address 地址 community 字符串"""
		v命令 = 命令.C命令("snmp-server trap target-address")
		v命令 += a地址
		v命令 += "community", a字符串
		self.f执行当前模式命令(v命令)
