from ..基础接口 import 操作
from ..基础接口 import 中间系统到中间系统 as 北向路由协议
from ..命令行接口 import 命令
from ..命令行接口 import 中间系统到中间系统 as 南向路由协议
from .常量 import *
from . import 接口 as 实现接口
ca级别 = {
	北向路由协议.E级别.e级别1: "level-1",
	北向路由协议.E级别.e级别2: "level-2",
	北向路由协议.E级别.e级别1和2: "level-1-2",
}
class C进程配置(南向路由协议.I进程配置):
	def __init__(self, a, a进程号):
		南向路由协议.I进程配置.__init__(self, a, a进程号)
	def fg进入命令(self):
		return f"isis {self.fg进程号()}"
	def f模式_接口(self, a接口):
		v接口 = 实现接口.f创建接口(a接口)
		return C接口配置(self.fg上级模式(), self.fg进程号(), v接口)
	def fs网络标识(self, a标识, a操作 = 操作.E操作.e设置):
		v命令 = f"network-entity {a标识}"
		self.f执行当前模式命令(v命令)
	def fs通告接口(self, a接口, a操作 = 操作.E操作.e设置):
		v接口配置 = self.f模式_接口(a接口)
		v接口配置.fs通告接口(a操作)
	def fs级别(self, a级别, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("is-level")
		v命令 += ca级别[a级别]
		v操作 = 操作.f解析操作(a操作)
		v命令.f前置肯定(操作.fi减操作(v操作), c不)
		self.f执行当前模式命令(v命令)
class C接口配置(南向路由协议.I接口配置):
	def __init__(self, a, a进程号, a接口):
		南向路由协议.I接口配置.__init__(self, a, a进程号, a接口)
	def fs通告接口(self, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令(f"isis enable {self.fg进程号()}")
		v操作 = 操作.f解析操作(a操作)
		v命令.f前置肯定(操作.fi减操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs被动接口(self, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("isis slient")
		v操作 = 操作.f解析操作(a操作)
		v命令.f前置肯定(操作.fi减操作(v操作), c不)
		self.f执行当前模式命令(v命令)
