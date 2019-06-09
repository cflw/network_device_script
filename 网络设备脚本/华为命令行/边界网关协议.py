import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 边界网关协议 as 北向路由协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 边界网关协议 as 南向路由协议
from . import 接口 as 实现接口
#路由
class C进程配置(南向路由协议.I进程配置):
	def __init__(self, a, a自治系统号):
		南向路由协议.I进程配置.__init__(self, a, a自治系统号)
	def fg进入命令(self):
		return f"bgp {self.fg自治系统号()}"
	#模式
	def f模式_对等体(self, a对等体, a操作 = 操作.E操作.e设置):
		return C对等体配置(a对等体)
	def f模式_地址族(self, *a地址族, a操作 = 操作.E操作.e设置):
		v地址族类型 = a地址族[0]
		if v地址族类型 == 北向路由协议.E地址族.e单播4:
			return C单播地址族4(self)
		raise NotImplementedError()
#通用
class C对等体配置(模式.C同级模式, 南向路由协议.I对等体配置):
	def __init__(self, a, a对等体):
		南向路由协议.I对等体配置.__init__(self, a, a对等体)
	def fg前置命令(self):
		return 命令.C命令(f"peer {self.fg对等体名()}")
	#操作
	def fs激活(self, a操作 = 操作.E操作.e开启):
		raise NotImplementedError()
	def fs远端自治系统号(self, a自治系统号, a操作 = 操作.E操作.e设置):
		v命令 = self.fg前置命令()
		v命令 += f"as-number {a自治系统号}"
		self.f执行当前模式命令(v命令)
	def fs本端自治系统号(self, a自治系统号, a操作 = 操作.E操作.e设置):
		raise NotImplementedError()
	def fs更新源地址(self, a源, a操作 = 操作.E操作.e设置):
		v命令 = self.fg前置命令()
		v接口 = 实现接口.f创建接口(a源)
		v命令 += f"connect-interface {v接口}"
		self.f执行当前模式命令(v命令)
	def fs对等体组(self, a对等体组, a操作 = 操作.E操作.e设置):
		v命令 = self.fg前置命令()
		v命令 += f"group {a对等体组}"
		self.f执行当前模式命令(v命令)
class C地址族配置(南向路由协议.I地址族配置):
	def __init__(self, a):
		南向路由协议.I地址族配置.__init__(self, a)
	def f模式_对等体(self, a对等体 , a操作 = 操作.E操作.e设置):
		return C对等体配置(self, a对等体)
#ipv4单播
class C单播地址族4(C地址族配置):
	def __init__(self, a):
		C地址族配置.__init__(self, a)
	def fg进入命令(self):
		return "ipv4-family unicast"
	def fs通告网络(self, a网络号, a操作 = 操作.E操作.e设置):
		v网络号 = 地址.S网络地址4.fc自动(a网络号)
		v命令 = 命令.C命令("network")
		v命令 += v网络号.fg网络号s(), v网络号.fg掩码s()
		self.f执行当前模式配置(v命令)