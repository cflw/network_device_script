from ..基础接口 import 开放最短路径优先
from . import 模式
from . import 接口
#===============================================================================
# 基础
#===============================================================================
#===============================================================================
# 配置
#===============================================================================
class I进程配置(模式.I模式, 开放最短路径优先.I进程配置):
	def __init__(self, a, a进程号):
		模式.I模式.__init__(self, a)
		self.m进程号 = a进程号
	def fg模式参数(self):
		"返回进程号"
		return (self.m进程号,)
	def fg进程号(self):
		return self.m进程号
class I区域配置(模式.I模式, 开放最短路径优先.I区域配置):
	def __init__(self, a, a进程号, a区域号):
		模式.I模式.__init__(self, a)
		self.m进程号 = a进程号
		self.m区域号 = a区域号
	def fg进程号(self):
		return self.m进程号
	def fg区域号(self):
		return self.m区域号
class I接口配置(接口.I接口配置基础, 开放最短路径优先.I接口配置):
	def __init__(self, a, a进程号, a接口):
		接口.I接口配置基础.__init__(self, a, a接口)
		self.m进程号 = a进程号
	def fg进程号(self):
		return self.m进程号
class I虚链路配置(模式.I模式, 开放最短路径优先.I虚链路配置):
	def __init__(self, a, a进程号, a区域号, a对端):
		I模式.__init__(self, a)
		self.m区域号 = a区域号
		self.m对端 = a对端
