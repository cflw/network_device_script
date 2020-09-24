import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 日志 as 南向日志
class C日志nv7(模式.C同级模式, 南向日志.I日志配置):
	def __init__(self, a):
		南向日志.I日志配置.__init__(self, a)
		self.m地址 = None
	def f生成服务器地址(self, a地址 = None):
		if a地址:
			self.m地址 = 地址.fc网络地址(a地址)
		return 命令.C命令(f"logging server {self.m地址.fg地址s()}")
	def fs服务器开关(self, a操作 = None):
		pass
	def fs服务器地址(self, a地址 = None, a操作 = 操作.E操作.e设置):
		v命令 = self.f生成服务器地址(a地址)
		self.f执行当前模式命令(v命令)
	def fs服务器严重级别(self, a级别, a操作 = 操作.E操作.e设置):
		v命令 = self.f生成服务器地址()
		v命令 += int(a级别)
		self.f执行当前模式命令(v命令)
