from ..基础接口 import 路由映射
from . import 模式
class I路由映射组(路由映射.I路由映射组, 模式.I模式):
	def __init__(self, a, a名称):
		模式.I模式.__init__(self, a)
		self.m名称 = a名称
class I路由映射节点(路由映射.I路由映射节点, 模式.I模式):
	def __init__(self, a, a序号, a动作):
		模式.I模式.__init__(self, a)
		self.m名称 = a.m名称
		self.m动作 = a动作
		self.m序号 = a序号