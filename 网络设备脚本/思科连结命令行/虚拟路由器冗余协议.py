import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 虚拟路由器冗余协议 as 北向协议
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from . import 接口 as 实现接口
from ..思科命令行.常量 import *
class C接口(北向协议.I冗余路由, 实现接口.I接口配置):
	"""适用于: 思科n7k系列"""
	def __init__(self, a, a接口, a组号):
		实现接口.I接口配置.__init__(self, a, a接口)
		self.m组号 = int(a组号)
		self.m组配置 = None
	def fg命令前缀(self):
		return 命令.C命令(f"vrrp {self.m组号}")
	def fg组配置(self):
		if not self.m组配置:
			self.m组配置 = C组配置vrrp1_nv4(self, self.fg组号())
		return self.m组配置
	#显示
	def fg组号(self):
		return self.m组号
	#配置
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		self.fg组配置().fs网络地址4(a地址, a操作)
	def fs抢占(self, a操作 = 操作.E操作.e开启):
		self.fg组配置().fs抢占(a操作)
	def fs优先级(self, a优先级, a操作 = 操作.E操作.e设置):
		self.fg组配置().fs优先级(a优先级, a操作)
class C组配置vrrp1_nv4(模式.I模式):
	"""vrrp
	适用于: 思科n7k系列(至少v4.0)"""
	def __init__(self, a, a组号):
		模式.I模式.__init__(self, a)
		self.m组号 = a组号
		self.m开关 = None
	def fg进入命令(self):
		return f"vrrp {self.m组号}"
	def f事件_退出模式前(self):
		self.fs开关(True)
	#显示
	def fg组号(self):
		return self.m组号
	#配置
	def fs开关(self, a操作):
		"""命令: [no] shutdown"""
		v操作 = 操作.f解析操作(a操作)
		v开关 = 操作.fi开操作(v操作)
		if self.m开关 == v开关:
			return
		v命令 = 命令.C命令("shutdown")
		v命令.f前置肯定(v开关, c不)
		self.f执行当前模式命令(v命令)
		self.m开关 = v开关
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		"""命令: address 地址"""
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = 命令.C命令("ip", v地址.fg地址s())
		self.fs开关(False)
		self.f执行当前模式命令(v命令)
	def fs抢占(self, a开关 = True):
		"""命令: [no] preempt [delay minimum 抢占延时]"""
		v操作 = 操作.f解析操作(a开关)
		v命令 = 命令.C命令("preempt")
		v命令.f前置否定(操作.fi开操作(v操作), c不)
		self.fs开关(False)
		self.f执行当前模式命令(v命令)
	def fs优先级(self, a优先级, a操作 = 操作.E操作.e设置):
		"""命令: priority 优先级"""
		v操作 = 操作.f解析操作(a操作)
		v优先级 = int(a优先级)
		v命令 = 命令.C命令("priority", v优先级)
		v命令.f前置否定(操作.fi开操作(v操作), c不)
		self.fs开关(False)
		self.f执行当前模式命令(v命令)
class C组配置vrrp3_nv6(C组配置vrrp1_nv4):
	"""vrrp v3
	适用于: 思科n7k系列(至少v6.2)"""
	def fg进入命令(self):
		"""命令: vrrpv3 组号 address-family [ipv4|ipv6]"""
		return f"vrrpv3 {self.m组号} address-famliy ipv4"