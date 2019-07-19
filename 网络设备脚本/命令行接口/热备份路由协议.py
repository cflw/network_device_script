from ..基础接口 import 热备份路由协议
from . import 模式
from . import 接口 as 南向接口
class I接口配置(南向接口.I接口配置基础, 热备份路由协议.I接口配置):
	def __init__(self, a, a接口, a组号):
		南向接口.I接口配置基础.__init__(self, a, a接口)
		self.m组号 = a组号
	def fg组号(self):
		return self.m组号