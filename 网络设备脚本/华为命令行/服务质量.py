from ..基础接口 import 操作
from ..基础接口 import 策略
from ..基础接口 import 服务质量 as 北向服务质量
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 服务质量 as 南向服务质量
from .常量 import *
#===============================================================================
# 分类
#===============================================================================
@策略.A自动策略()
class C分类(南向服务质量.I流量分类):
	def __init__(self, a, a名称, ai匹配全部 = False):
		南向服务质量.I流量分类.__init__(self, a, a名称, ai匹配全部)
	#模式
	def fg进入命令(self):
		"""命令: traffic classifier 名称 [选项]"""
		v匹配全部 = "all" if self.mi匹配全部 else "or"
		v命令 = f"traffic classifier {self.m名称} operator {v匹配全部}"
		return v命令
	#匹配
	@策略.A匹配(策略.E类型.e访问列表4)
	def f匹配_访问列表4(self, a值, a操作 = 操作.E操作.e设置):
		"""命令: if-match acl 访问列表"""
		v命令 = f"if-match acl {a值}"
		self.f执行当前模式命令(v命令)
	@策略.A匹配(策略.E类型.e访问列表6)
	def f匹配_访问列表6(self, a值, a操作 = 操作.E操作.e设置):
		"""命令: if-match ipv6 acl 访问列表"""
		v命令 = f"if-match ipv6 acl {a值}"
		self.f执行当前模式命令(v命令)
#===============================================================================
# 行为
#===============================================================================
@策略.A自动策略()
class C行为(南向服务质量.I流量行为):
	def __init__(self, a, a名称):
		南向服务质量.I流量行为.__init__(self, a, a名称)
	#模式
	def fg进入命令(self):
		"""命令: traffic behavior 名称"""
		v命令 = f"traffic behavior {self.m名称}"
		return v命令
	#动作
	def fs允许(self, a允许 = True):
		"""命令: 动作"""
		v命令 = "permit" if a允许 else "deny"
		self.f执行当前模式命令(v命令)
	#设置
	@策略.A设置(策略.E类型.e下一跳4)
	def f设置_下一跳4(self, a值, a操作 = 操作.E操作.e设置):
		"""命令: redirect ip-nexthop 地址"""
		v命令 = f"redirect ip-nexthop {a值}"
		self.f执行当前模式命令(v命令)
	@策略.A设置(策略.E类型.e出接口)
	def f设置_出接口(self, a接口, a操作 = 操作.E操作.e设置):
		"""命令: redirect interface 接口 [forced]"""
		v命令 = f"redirect interface {a接口}"
		self.f执行当前模式命令(v命令)
#===============================================================================
# 策略
#===============================================================================
class C策略(南向服务质量.I流量策略):
	def __init__(self, a, a名称):
		南向服务质量.I流量策略.__init__(self, a, a名称)
	def fg进入命令(self):
		"""命令: traffic policy 名称"""
		v命令 = f"traffic policy {self.m名称}"
		return v命令
	def fs绑定(self, a分类, a行为, a操作 = 操作.E操作.e设置):
		"""命令: classifier 名称 behavior 名称"""
		v命令 = f"classifier {a分类} behavior {a行为}"
		self.f执行当前模式命令(v命令)
#===============================================================================
# 助手
#===============================================================================
class C助手(北向服务质量.I助手):
	def __init__(self, a策略, a分类, a行为, ai自动绑定 = True):
		self.m策略名称 = a策略
		self.m分类名称 = a分类
		self.m行为名称 = a行为
		self.mi自动绑定 = True
		self.mi已绑定 = False
		self.m策略模式 = None
		self.m分类模式 = None
		self.m行为模式 = None
	def fg策略名称(self):
		return self.m策略名称
	def fg分类名称(self):
		return self.m分类名称
	def fg行为名称(self):
		return self.m行为名称