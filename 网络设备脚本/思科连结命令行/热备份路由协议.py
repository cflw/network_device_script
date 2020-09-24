import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 热备份路由协议 as 南向协议
from ..思科命令行.常量 import *
class C接口配置nv7(南向协议.I接口配置):
	"""适用于: 浪潮cn8672(v7.3), 浪潮cn8696(v7.3)"""
	def __init__(self, a, a接口, a组号):
		南向协议.I接口配置.__init__(self, a, a接口, a组号)
		self.m组配置 = None
	def fg组配置(self):
		if not self.m组配置:
			self.m组配置 = C组配置nv7(self, self.fg组号())
		return self.m组配置
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		v命令 = f"hsrp version {a版本}"
		self.f执行当前模式命令(v命令)
	def fs地址4(self, a地址, a操作 = 操作.E操作.e设置):
		self.fg组配置().fs地址4(a地址, a操作)
	def fs抢占(self, a操作 = 操作.E操作.e开启):
		self.fg组配置().fs抢占(a操作)
	def fs优先级(self, a优先级, a操作 = 操作.E操作.e设置):
		self.fg组配置().fs优先级(a优先级, a操作)
class C组配置nv7(模式.I模式):
	"""适用于: 浪潮cn8672(v7.3), 浪潮cn8696(v7.3)"""
	def __init__(self, a, a组号):
		模式.I模式.__init__(self, a)
		self.m组号 = a组号
	def fg组号(self):
		return self.m组号
	def fg进入命令(self):
		return f"hsrp {self.m组号}"
	def fs地址4(self, a地址, a操作):
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = 命令.C命令("ip")
		v命令 += v地址.fg地址s()
		v命令.f前置肯定(操作.fi减操作(a操作), c不)
		self.f执行当前模式命令(v命令)
	def fs抢占(self, a操作):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("preempt")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs优先级(self, a优先级, a操作):
		v命令 = 命令.C命令("priority")
		if 操作.fi减操作(a操作):
			v命令.f前面添加(c不)
		else:
			v命令 += a优先级
		self.f执行当前模式命令(v命令)