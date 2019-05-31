from ..基础接口 import 操作
from ..基础接口 import 中间系统到中间系统 as 北向路由协议
from ..命令行接口 import 命令
from ..命令行接口 import 中间系统到中间系统 as 南向路由协议
from ..命令行接口 import 接口 as 南向接口
from . import 接口 as 实现接口
class C进程配置(南向路由协议.I进程配置):
	def __init__(self, a, a进程号):
		南向路由协议.I进程配置.__init__(self, a, a进程号)
	def fg进入命令(self):
		v命令 = 命令.C命令("router isis")
		v命令 += self.fg进程号()
		return v命令
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		if isinstance(a接口, C接口配置):
			return a接口
		v接口 = 实现接口.f创建接口(a接口)
		return C接口配置(self.fg上级模式(), self.fg进程号(), v接口)
	def fs网络标识(self, a标识, a操作 = 操作.E操作.e设置):
		v标识 = 北向路由协议.S网络标识.fc自动(a标识)
		v命令 = 命令.C命令("net")
		v命令 += v标识
		self.f执行当前模式命令(v命令)
	def fs通告接口(self, a接口, a操作 = 操作.E操作.e设置):
		v接口配置 = self.f模式_接口(a接口)
		v接口配置.fs通告接口(a操作)
class C接口配置(南向路由协议.I接口配置):
	def __init__(self, a, a进程号, a接口):
		南向路由协议.I接口配置.__init__(self, a, a进程号, a接口)
	def fs通告接口(self, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("ip router isis")
		v命令 += self.fg进程号()
		self.f执行当前模式命令(v命令)

