from ..基础接口 import 操作
from ..基础接口 import 策略
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 路由映射
from . import 访问控制列表 as 访问列表
class C路由映射组(路由映射.I路由映射组, 模式.C同级模式):
	def __init__(self, a, a名称):
		路由映射.I路由映射组.__init__(self, a, a名称)
	def f模式_节点(self, a序号 = 10, a动作 = True, a操作 = None):
		return C路由映射节点(self, a序号, a动作)
@策略.A自动策略()
class C路由映射节点(路由映射.I路由映射节点):
	def __init__(self, a, a序号, a动作):
		路由映射.I路由映射节点.__init__(self, a, a序号, a动作)
	def fg进入命令(self):
		"""route-map 名称 [动作] [序号]"""
		return f"route-map {self.m名称} {访问列表.f生成允许(self.m动作)} {self.m序号}"
	#匹配
	@策略.A匹配(策略.E类型.e访问列表)
	def f匹配_访问列表(self, a访问列表, a操作 = 操作.E操作.e添加):
		if isinstance(a访问列表, 访问列表.I访问控制列表):
			v命令 = f"match {a访问列表.m协议} address {a访问列表.m名称}"
		else:
			v命令 = f"match ip address {str(a访问列表)}"
		self.f执行当前模式命令(v命令)
	#设置
	@策略.A设置(策略.E类型.e下一跳4)
	def f设置_下一跳4(self, a地址, a操作 = 操作.E操作.e添加):
		v命令 = f"set ip next-hop {a地址}"
		self.f执行当前模式命令(v命令)
	@策略.A设置(策略.E类型.e默认下一跳4)
	def f设置_默认下一跳4(self, a地址, a操作 = 操作.E操作.e添加):
		v命令 = f"set ip default next-hop {a地址}"
		self.f执行当前模式命令(v命令)
	@策略.A设置(策略.E类型.e出接口)
	def f设置_出接口(self, a接口, a操作 = 操作.E操作.e添加):
		v命令 = f"set interface {a接口}"
		self.f执行当前模式命令(v命令)
	@策略.A设置(策略.E类型.e默认出接口)
	def f设置_默认出接口(self, a接口, a操作 = 操作.E操作.e添加):
		v命令 = f"set default interface {a接口}"
		self.f执行当前模式命令(v命令)
