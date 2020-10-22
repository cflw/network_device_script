from ..基础接口 import 策略
from ..基础接口 import 服务质量
from . import 模式
class I流量分类(策略.I匹配, 模式.I模式):
	def __init__(self, a, a名称, ai匹配全部):
		模式.I模式.__init__(self, a)
		self.m名称 = a名称
		self.mi匹配全部 = ai匹配全部
class I流量行为(策略.I设置, 模式.I模式):
	def __init__(self, a, a名称):
		模式.I模式.__init__(self, a)
		self.m名称 = a名称
class I流量策略(模式.I模式):
	def __init__(self, a, a名称):
		模式.I模式.__init__(self, a)
		self.m名称 = a名称
	def fs绑定(self, a类, a行为, a操作):
		raise NotImplementedError()
