from ..基础接口 import 操作
from ..基础接口 import 策略
from ..基础接口 import 服务质量 as 北向服务质量
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 服务质量 as 南向服务质量
from .常量 import *
@策略.A自动策略()
class C类映射(南向服务质量.I流量分类):
	def __init__(self, a, a名称, ai匹配全部 = False):
		南向服务质量.I流量分类.__init__(self, a, a名称, ai匹配全部)
	def fg进入命令(self):
		"""命令: class-map [type 类型] [匹配方式] 名称"""
		return f"class-map {self.m名称}"
	#匹配
	@策略.A匹配(策略.E类型.e访问列表)
	def f匹配_访问列表(self, a值, a操作 = 操作.E操作.e设置):
		"""命令: match access-group 访问列表"""
		v命令 = f"match access-group {a值}"
		self.f执行当前模式命令(v命令)
class C策略映射(模式.I模式):
	def __init__(self, a, a名称):
		模式.I模式.__init__(self, a)
		self.m名称 = a名称
	def fg进入命令(self):
		"""命令: policy-map [type 类型] 名称"""
		return f"policy-map {self.m名称}"
	def f模式_绑定类(self, a分类名称: str, a操作 = 操作.E操作.e设置):
		v类 = C绑定类(self, a分类名称)
		return v类
@策略.A自动策略()
class C绑定类(南向服务质量.I流量行为):
	def __init__(self, a, a分类名称):
		南向服务质量.I流量行为.__init__(self, a, a分类名称)
	def fg进入命令(self):
		"""命令: class 名称"""
		return f"class {self.m名称}"
	#动作
	def fs允许(self, a允许 = True):
		"""命令: [no] drop"""
		v命令 = 命令.C命令("drop")
		v命令.f前置肯定(a允许, c不)
		self.f执行当前模式命令(v命令)
	#设置
	@策略.A设置(策略.E类型.e优先级)
	def f设置_优先级(self, a值, a操作 = 操作.E操作.e设置):
		"""命令: set ip precedence 值"""
		v命令 = f"set ip precedence {a值}"
		self.f执行当前模式命令(v命令)
class C助手(北向服务质量.I助手):
	def __init__(self, a策略: str, a分类: str, a行为: str):
		self.m策略名称 = a策略
		self.m分类名称 = a分类
		self.m行为名称 = a行为
	def fg策略名称(self):
		return self.m策略名称
	def fg分类名称(self):
		return self.m分类名称
	def fg行为名称(self):
		return self.m行为名称
		