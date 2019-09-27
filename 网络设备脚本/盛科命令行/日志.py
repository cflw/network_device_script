import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 日志 as 南向日志
#ev6
class C日志ev6(模式.C同级模式, 南向日志.I日志配置):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a):
		南向日志.I日志配置.__init__(self, a)
	def fs服务器开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		if 操作.fi开操作(v操作):
			self.f执行当前模式命令("logging server enable")
		else:
			self.f执行当前模式命令("logging server disable")
	def fs服务器地址(self, a地址, a操作 = 操作.E操作.e添加):
		self.f执行当前模式命令(f"logging server address {a地址}")
	def fs服务器严重级别(self, a级别, a操作 = 操作.E操作.e设置):
		self.f执行当前模式命令(f"logging server severity {int(a级别)}")
