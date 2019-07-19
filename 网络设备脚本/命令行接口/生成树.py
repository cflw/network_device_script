from ..基础接口 import 生成树
from . import 模式
from . import 接口 as 南向接口
class I多生成树配置(模式.I模式, 生成树.I多生成树配置):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
class I接口配置(南向接口.I接口配置基础, 生成树.I接口配置):
	def __init__(self, a, a接口):
		南向接口.I接口配置基础.__init__(self, a, a接口)
