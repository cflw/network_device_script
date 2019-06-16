from ..基础接口 import 虚拟路由转发
from . import 模式
from . import 接口
class I资源配置(模式.I模式, 虚拟路由转发.I资源配置):
	def __init__(self, a, a名称):
		模式.I模式.__init__(self, a)
		self.m名称 = a名称
	def fg名称(self):
		return self.m名称
class I接口配置(接口.I接口配置基础, 虚拟路由转发.I接口配置):
	def __init__(self, a, a接口):
		接口.I接口配置基础.__init__(self, a, a接口)