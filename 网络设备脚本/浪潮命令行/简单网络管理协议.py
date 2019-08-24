from ..基础接口 import 操作
from ..基础接口 import 文件
from ..命令行接口 import 简单网络管理协议 as 南向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..思科命令行.常量 import *
#===============================================================================
# cn系列(v6.x)
#===============================================================================
class C代理配置cnv6(模式.C同级模式, 南向协议.I代理配置):
	"""适用于: cn61108(v6.x)"""
	def __init__(self, a):
		南向协议.I代理配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		"""命令: [no] snmp-server enable"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-server enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs团体字符串(self, a字符串, a权限 = 文件.E读写权限.e只读, a操作 = 操作.E操作.e设置):
		"""命令: snmp-server community 字符串 权限"""
		v命令 = 命令.C命令("snmp-server community")
		v命令 += a字符串
		v命令 += "read-write" if 文件.fi含写(a权限) else "read-only"
		self.f执行当前模式命令(v命令)
class C陷阱配置cnv6(模式.C同级模式, 南向协议.I陷阱配置):
	"""适用于: cn61108(v6.x)"""
	def __init__(self, a):
		南向协议.I陷阱配置.__init__(self, a)
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
#===============================================================================
# s系列(v3.x)
#===============================================================================
class C代理配置sv3(模式.C同级模式, 南向协议.I代理配置):
	"""适用于: s6550(v3.x)"""
	def __init__(self, a):
		南向协议.I代理配置.__init__(self, a)
	def fs团体字符串(self, a字符串, a权限 = 文件.E读写权限.e只读, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("snmp-server community")
		v命令 += a字符串
		v命令 += "rw" if 文件.fi含写(a权限) else "ro"
		v输出 = self.f执行当前模式命令(v命令)
		#Community exist. if you want to modify the community information,please input 'yes' to confirm:
		if "confirm" in v输出:
			self.m设备.f执行命令("yes")
class C陷阱配置sv3(模式.C同级模式, 南向协议.I陷阱配置):
	"""适用于: s6550(v3.x)"""
	def __init__(self, a):
		南向协议.I陷阱配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-server trap transceiver")
		v命令 += "enable" if 操作.fi开操作(v操作) else "disable"
		self.f执行当前模式命令(v命令)
	def fs服务器(self, a地址, a字符串, a操作 = 操作.E操作.e添加):
		v命令 = 命令.C命令("snmp-server host")
		v命令 += a地址, a字符串
		self.f执行当前模式命令(v命令)