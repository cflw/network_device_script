from ..基础接口 import 中间系统到中间系统
from . import 模式
from . import 接口
class I进程配置(模式.I模式, 中间系统到中间系统.I进程配置):
	def __init__(self, a, a进程号):
		模式.I模式.__init__(self, a)
		self.m进程号 = a进程号
	def fg进程号(self):
		return self.m进程号
class I接口配置(接口.I接口配置基础, 中间系统到中间系统.I接口配置):
	def __init__(self, a, a进程号, a接口):
		接口.I接口配置基础.__init__(self, a, a接口)
		self.m进程号 = a进程号
	def fg进程号(self):
		return self.m进程号
	