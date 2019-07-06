import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 日志 as 北向日志
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 日志 as 南向日志
class C日志配置(模式.C同级模式, 南向日志.I日志配置):
	def __init__(self, a):
		南向日志.I日志配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v命令 = 命令.C命令("logging on")
		self.f执行当前模式命令(v命令)
	def fs大小(self, a字节, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("logging buffer")
		v命令 += int(a字节)
		self.f执行当前模式命令(v命令)
	def fs服务器地址(self, a地址, a操作 = 操作.E操作.e添加):
		v地址 = 地址.fc网络地址(a地址)
		v命令 = 命令.C命令("logging host")
		v命令 += v地址.fg地址s()
		self.f执行当前模式命令(v命令)
	def fs服务器严重级别(self, a级别, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令(f"logging trap {int(a级别)}")
		self.f执行当前模式命令(v命令)		