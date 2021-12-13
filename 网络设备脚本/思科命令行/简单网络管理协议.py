from ..基础接口 import 操作
from ..基础接口 import 文件
from ..基础接口 import 简单网络管理协议 as 北向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from .常量 import *
class C代理配置(模式.C同级模式, 北向协议.I代理配置):
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs开关(self, a操作 = None):
		"""没有命令"""
		pass
	def fs团体字符串(self, a字符串, a权限 = 文件.E访问权限.e只读, a操作 = 操作.E操作.e设置):
		"""命令: snmp-server community 团体字 访问权限
		删除命令: no snmp-server community 团体字"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-server community")
		v命令 += a字符串
		if 操作.fi加操作(v操作):
			v命令 += "rw" if 文件.fi含写(a权限) else "ro"
		elif 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		else:
			raise ValueError("未知的操作")
		self.f执行当前模式命令(v命令)
	def fi团体字符串(self, a字符串, a权限 = None):
		pass
class C陷阱配置(模式.C同级模式, 北向协议.I陷阱配置):
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		"""命令: [no] snmp-server enable traps"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-server enable traps")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs服务器(self, a地址, a字符串, a操作 = 操作.E操作.e添加):
		"""命令: snmp-server host 地址 字符串"""
		v命令 = 命令.C命令("snmp-server host")
		v命令 += a地址, a字符串
		self.f执行当前模式命令(v命令)