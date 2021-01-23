import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 虚拟路由器冗余协议 as 北向协议
from ..基础接口 import 操作
from ..命令行接口 import 模式
from ..命令行接口 import 接口
from ..命令行接口 import 命令
from .常量 import *
class C冗余路由(北向协议.I冗余路由, 模式.I模式):
	"""适用于: 浪潮cn61108pcvh()"""
	def __init__(self, a, a接口, a组号, a虚拟路由转发 = None):
		模式.I模式.__init__(self, a)
		self.m接口 = a接口	#类型:S接口
		self.m当前接口 = None	#当前配置的接口,类型:S接口
		self.m组号 = int(a组号)
		self.m虚拟路由转发 = a虚拟路由转发
		self.m当前开关 = None
	def fg组号(self):
		return self.m组号
	def fg进入命令(self):
		"""命令: router vrrp 组号 [vrf 虚拟路由转发]"""
		v命令 = 命令.C命令(f"router vrrp {self.fg组号()}")
		if self.m虚拟路由转发:
			v命令 += "vrf", self.m虚拟路由转发
		return v命令
	def f事件_进入模式后(self):
		self.fs接口(self.m接口)
	def f事件_退出模式前(self):
		self.fs开关(True)
	#配置
	def fs开关(self, a操作):
		"""命令: enable|disable"""
		v操作 = 操作.f解析操作(a操作)
		v开关 = 操作.fi开操作(v操作)
		if self.m当前开关 == v开关:
			return
		self.m当前开关 = v开关
		v命令 = "enable" if v开关 else "disable"
		self.f执行当前模式命令(v命令)
	def fs接口(self, a接口, a操作 = 操作.E操作.e设置):
		"""命令: interface 接口"""
		if self.m当前接口 == self.m接口:
			return
		self.m当前接口 = a接口
		v命令 = f"interface {a接口}"
		self.fs开关(False)
		self.f执行当前模式命令(v命令)
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		"""命令: virtual-ip 地址"""
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = f"virtual-ip {v地址.fg地址s()}"
		self.fs开关(False)
		self.f执行当前模式命令(v命令)
	def fs优先级(self, a优先级, a操作 = 操作.E操作.e设置):
		"""命令: priority 优先级"""
		v优先级 = int(a优先级)
		v命令 = f"priority {v优先级}"
		self.fs开关(False)
		self.f执行当前模式命令(v命令)
	def fs抢占(self, a操作):
		"""命令: preempt"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("preempt")
		v命令.f前置否定(操作.fi开操作(v操作), c不)
		self.fs开关(False)
		self.f执行当前模式命令(v命令)
	def fs抢占模式(self, a操作):
		"""命令: preempt-mode 布尔"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = "true" if 操作.fi开操作(v操作) else "false"
		self.fs开关(False)
		self.f执行当前模式命令(v命令)
